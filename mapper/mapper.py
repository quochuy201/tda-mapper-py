# ------------------------------------------------------
# A straightforward implementation of the mapper construction by Carlsson--Memoli--Singh.
# (I wrote a little blog post about it at http://mapsfunctionsandarrows.blogspot.de)
# ------------------------------------------------------

from oneNerve import compute_one_nerve
from abstractClusterFunction import AbstractClusterFunction
from referenceMap import ReferenceMap


def mapper(clusterFct, referenceFct, funcCover):
    """Mapper is a construction that uses a given cluster-algorithm to 
    associate a simplicial complex to a reference map on a given data set.

    Args:
        clusterFct: A class that inherits from AbstractClusterFunction. 
        referenceFct: A ReferenceFunction class. A callable class that can be called with elements form the dataset.
        funcCover: A dict of boolean functions (characteristic functions), 
            that are defined on the target space of the given filter.
    Returns:
        A simplicial complex.
    """
    if not isinstance(clusterFct, AbstractClusterFunction) or not isinstance(referenceFct, ReferenceMap):
        raise TypeError("Please take look at the function signature....")
        
    clusterCover = clusterFct.push_forward(referenceFct.pull_back(funcCover))
    oneNerve = compute_one_nerve(clusterCover)

    return (clusterCover, oneNerve)


