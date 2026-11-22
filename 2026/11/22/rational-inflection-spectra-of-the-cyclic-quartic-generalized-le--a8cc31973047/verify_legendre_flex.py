#!/usr/bin/env python3
"""Independent finite-prime checks of the stated flex arithmetic.
Run: python3 verify_legendre_flex.py
No third-party packages required. Tests do not prove all prime powers.
"""

def chi(v, p):
    v %= p
    if v == 0:
        return 0
    return 1 if pow(v, (p-1)//2, p) == 1 else -1


def Q(x, t, p):
    return (3*x**4-4*(t+1)*x**3+(4*t*t+2*t+4)*x*x-4*t*(t+1)*x+3*t*t) % p


def g(x, t, p):
    return x*(x-1)*(x-t) % p


def is_prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))


def verify(p):
    assert is_prime(p) and p>=7 and p%4==3
    excluded = {0,1,-1%p,2,pow(2,-1,p)}
    expected_count = (p-11)//8 if p%8==3 else (p+1)//8
    predicted_split = 2*expected_count
    count_12=count_4=count_split=0
    for t in range(p):
        if t in excluded:
            continue
        roots = [x for x in range(p) if Q(x,t,p)==0]
        D1= -(t-2)*(2*t-1)
        D2= (t-2)*(t+1)
        split = chi(D1,p)==chi(D2,p)==1
        assert (len(roots)==4)==split, (p,t,roots,D1,D2)
        if split:
            count_split+=1
            chars={chi(g(x,t,p),p) for x in roots}
            assert len(chars)==1 and 0 not in chars, (p,t,chars)
        fourth_powers = [pow(y,4,p) for y in range(p)]
        ordinary_direct = sum(fourth_powers.count(g(x,t,p)) for x in roots)
        assert ordinary_direct in {0,8}, (p,t,ordinary_direct)
        if ordinary_direct:
            count_12+=1
            assert split
        else:
            count_4+=1
    assert count_split==predicted_split, (p,count_split,predicted_split)
    assert count_12==expected_count, (p,count_12,expected_count)
    assert count_4==p-5-expected_count
    return p,len(range(p))-len(excluded),count_4,count_12


def main():
    primes=[p for p in range(7,220) if is_prime(p) and p%4==3]
    for p in primes:
        print('p=%d generic=%d four=%d twelve=%d' % verify(p))
    print('GENERALIZED_LEGENDRE_RATIONAL_FLEX_SPECTRUM_VERIFIED')

if __name__ == '__main__':
    main()
