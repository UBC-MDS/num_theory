def arithmetic_progression(a, d, n, compute_sum=False, nth_term=False):
    """
    Generate terms of an arithmetic progression (AP), compute the nth term, or calculate the sum of the first n terms.

    Parameters
    ----------
    a : float
        The first term of the AP.
    d : float
        The common difference between consecutive terms.
    n : int
        The number of terms, the term to compute, or the term index.
    compute_sum : bool, optional
        If True, computes the sum of the first n terms. Default is False.
    nth_term : bool, optional
        If True, computes the nth term of the AP instead of generating terms. Default is False.

    Returns
    -------
    list or float
        - If `compute_sum` and `nth_term` are both False, returns a list of the first n terms of the AP.
        - If `nth_term` is True, returns the nth term as a float.
        - If `compute_sum` is True, returns the sum of the first n terms as a float.

    Examples
    --------
    Generate the first 5 terms of an AP with first term 2 and common difference 3:
    >>> arithmetic_progression(a=2, d=3, n=5)
    [2, 5, 8, 11, 14]

    Compute the sum of the first 5 terms of the AP:
    >>> arithmetic_progression(a=2, d=3, n=5, compute_sum=True)
    40.0

    Find the 5th term of the AP:
    >>> arithmetic_progression(a=2, d=3, n=5, nth_term=True)
    14
    """
    pass
