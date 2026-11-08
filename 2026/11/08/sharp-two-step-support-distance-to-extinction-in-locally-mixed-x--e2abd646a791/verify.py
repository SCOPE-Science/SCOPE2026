"""Standalone finite checks of two-step support controllability for the locally mixed ECA 60/102.
No external dependencies. Run: python3 verify.py
"""
from fractions import Fraction


def bit(x, i, n):
    return (x >> (i % n)) & 1


def permitted(x, y, n):
    """Independent direct evaluation of local 60/102 support."""
    for i in range(n):
        a = bit(x, i-1, n) ^ bit(x, i, n)
        b = bit(x, i, n) ^ bit(x, i+1, n)
        if bit(y, i, n) not in (a, b):
            return False
    return True


def no_singletons(y, n):
    return all(not (bit(y, i-1, n) == bit(y, i+1, n) != bit(y, i, n)) for i in range(n))


def witness(x, n):
    """Run-smoothing witness: use previous non-singleton wall run for singleton runs."""
    w = [bit(x, i, n) ^ bit(x, i-1, n) for i in range(n)]
    # Locate a cyclic run of length >= 2.
    long_start = next((i for i in range(n) if w[i] == w[(i+1)%n]), None)
    if long_start is None:  # Completely alternating wall word: all sites freely update.
        return 0
    out = [None]*n
    # Begin at a position in a long run and traverse in cyclic order. Every singleton
    # run after a long run inherits its last value; longer runs keep their own bit.
    first = long_start
    previous_long = w[first]
    i = first
    while True:
        j = (i+1) % n
        if w[i] == w[j]:
            out[i] = w[i]
            previous_long = w[i]
        else:
            # If this bit is part of a long run (equal to predecessor), retain it;
            # otherwise inherit the preceding long-run value.
            if w[i] == w[(i-1)%n]:
                out[i] = w[i]
                previous_long = w[i]
            else:
                out[i] = previous_long
        i = j
        if i == first:
            break
    return sum(value << i for i,value in enumerate(out))


def prob_step(x, y, n, p):
    v = Fraction(1)
    for i in range(n):
        a = bit(x,i-1,n)^bit(x,i,n)
        b = bit(x,i,n)^bit(x,i+1,n)
        z = bit(y,i,n)
        if a == b:
            if z != a:
                return Fraction(0)
        else:
            v *= p if z == b else (1-p)
    return v


if __name__=='__main__':
    witnesses=0
    one_step_counts=[]
    for n in range(2,16):
        for x in range(1<<n):
            y=witness(x,n)
            assert permitted(x,y,n), (n,x,y,'first')
            assert no_singletons(y,n), (n,x,y,'admissible')
            assert permitted(y,0,n), (n,x,y,'second')
            witnesses+=1
        good_count=sum(1 for x in range(1<<n) if permitted(x,0,n))
        a,b=2,1  # Lucas numbers L_0,L_1
        for _ in range(n): a,b=b,a+b
        cosine=[2,1,-1,-2,-1,1][n%6]
        assert good_count==a+cosine, (n,good_count,a+cosine)
        one_step_counts.append((n,good_count))
        one_hot=1
        assert not permitted(one_hot,0,n), (n,'sharp')
    brute_cases=0
    for n in range(2,10):
        admissible=[y for y in range(1<<n) if permitted(y,0,n)]
        for x in range(1<<n):
            assert any(permitted(x,y,n) for y in admissible)
            brute_cases+=1
    probability_cases=0
    for n in range(2,8):
        for x in range(1<<n):
            p=Fraction(1,3)
            exact=sum((prob_step(x,y,n,p)*prob_step(y,0,n,p) for y in range(1<<n)),Fraction(0))
            assert exact >= min(p,1-p)**(2*n)
            probability_cases+=1
    print(f'VERIFY_OK constructed_support_paths={witnesses} one_step_distance_counts={len(one_step_counts)} independently_exhausted_states={brute_cases} exact_probability_cases={probability_cases} n_range=2..15')
