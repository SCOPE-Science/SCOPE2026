#!/usr/bin/env python3
"""Exact finite certificates for nonadjacent centered-nonagonal subset sums."""

def c(n: int) -> int:
    assert n >= 1
    return 1 + 9*n*(n-1)//2


def bitset(n: int) -> int:
    """Encode all obtainable nonnegative integers with a 1-bit."""
    old2 = old1 = 1  # B_{-1}=B_0={0}
    for k in range(1, n+1):
        new = old1 | (old2 << c(k))
        old2, old1 = old1, new
    return old1


def boolean_dp(n: int, cap: int) -> bytearray:
    """Different implementation of the recurrence, truncated at cap."""
    old2 = bytearray(cap+1)
    old1 = bytearray(cap+1)
    old2[0] = old1[0] = 1
    for k in range(1,n+1):
        v = c(k)
        now = old1[:] 
        for target in range(v, cap+1):
            if old2[target-v]:
                now[target] = 1
        old2, old1 = old1, now
    return old1


def run() -> None:
    L = 9084
    for n in (41,42):
        B = bitset(n)
        U = n**3//4
        assert ((B >> L) & ((1<<(U-L+1))-1)) == (1<<(U-L+1))-1, (n, U)
        alt = boolean_dp(n,U)
        assert all(alt[k] == ((B>>k)&1) for k in range(U+1))
        print('BASE_OK n=%d L=%d U=%d checked=%d'%(n,L,U,U+1))
    B45 = bitset(45)
    assert ((B45>>9083)&1)==0
    assert c(45)<=9083<c(46)
    alt45=boolean_dp(45,9083)
    assert alt45[9083]==0
    assert all(alt45[k]==((B45>>k)&1) for k in range(9084))
    print('OBSTRUCTION_OK x=9083 max_applicable_index=45 checked=9084')
    # Confirm the inductive inequalities for many values; the all-n proof is algebraic.
    for n in range(43,501):
        U=lambda k:k**3//4
        assert U(n-1)+1>=L+c(n)
        assert U(n-2)+c(n)>=U(n)
        assert U(n)>U(n-1)
    print('INEQUALITY_SPOTCHECK_OK n=43..500; symbolic bounds required for infinity')
    # For additional confidence, direct recurrence tests beyond base.
    for n in range(43,61):
        B=bitset(n); U=n**3//4
        assert ((B>>L)&((1<<(U-L+1))-1)) == ((1<<(U-L+1))-1)
    print('EXTENDED_FINITE_OK n=43..60')
    print('CHECKER_PASS')


if __name__=='__main__':
    run()
