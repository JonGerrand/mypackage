import numpy as np

def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Parameters
    ----------
    items : array
        List or array-like object containing numerical values.
    n : int
        Number of top items to return.

    Returns
    -------
    array
        Top n items, in descending order.

    Examples
    --------
    >>> top_n([8,3,2,7,4], 3)
    [8, 7, 3]
    """

    for i in range(n): # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j + 1]: # If this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # Perform a swap

    # Get the last n items
    top_n = items[-n:]
    return top_n [::-1]
