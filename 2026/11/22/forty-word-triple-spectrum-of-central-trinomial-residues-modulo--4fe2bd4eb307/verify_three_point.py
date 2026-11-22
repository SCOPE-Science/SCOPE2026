#!/usr/bin/env python3
"""Independent exact checks for ternary consecutive central-trinomial residues modulo five."""
from collections import Counter
from fractions import Fraction

E = (0, 0, 1, 3, 2)


def digit_exponent(n):
    s = 0
    while n:
        s = (s + E[n % 5]) % 4
        n //= 5
    return s


def A(r, s):
    return (5**r - 1)//4 + (s % 4 == 0)


def B(r, s, d):
    s %= 4
    d %= 4
    total = 0
    for k in range(r):
        a = (d + 2*k) % 4
        total += (5**(r-k-1)-1)//4
        total += ((E[a]+2*k) % 4 == s)
    return total + ((2*r) % 4 == s and (-2*r) % 4 == d)


def exact_count(r, a, b, c):
    R = r - 1
    count = 0
    for t in range(3):
        s = (a - E[t]) % 4
        if (b, c) == ((s+E[t+1])%4, (s+E[t+2])%4):
            count += A(R, s)
    if b == (a-1) % 4:
        s = (a-3) % 4
        count += B(R, s, (c-s)%4)
    if b == c:
        s = (a-2) % 4
        count += B(R, s, (b-s)%4)
    return count


def leading(a, b, c):
    result = Fraction(int(b == (a-1)%4)+int(b==c), 80)
    for t in range(3):
        s = (a-E[t])%4
        if (b,c) == ((s+E[t+1])%4, (s+E[t+2])%4):
            result += Fraction(1,20)
    return result


def check():
    tests=0
    # Independent integer recurrence: (n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}.
    T0, T1 = 1, 1
    assert digit_exponent(0) == 0
    observed = [T0%5, T1%5]
    for n in range(1, 3126):
        num = (2*n+1)*T1 + 3*n*T0
        assert num%(n+1)==0
        T0,T1=T1,num//(n+1)
        observed.append(T1%5)
        assert T1%5 == pow(3,digit_exponent(n+1),5)
        tests+=1
    for r in range(1,7):
        size=5**r
        counts=Counter((digit_exponent(n),digit_exponent(n+1),digit_exponent(n+2))
                       for n in range(size))
        assert sum(counts.values())==size
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    assert counts.get((a,b,c),0)==exact_count(r,a,b,c),(r,a,b,c)
                    tests+=1
        if r>=3:
            assert sum(v>0 for v in counts.values())==40
            tests+=1
        if size+2<=len(observed):
            actual=Counter((observed[n],observed[n+1],observed[n+2]) for n in range(size))
            transformed=Counter({(pow(3,a,5),pow(3,b,5),pow(3,c,5)):v for (a,b,c),v in counts.items()})
            assert actual==transformed
            tests+=1
    mass=Counter()
    for a in range(4):
        for b in range(4):
            for c in range(4):
                p=leading(a,b,c)
                mass[p]+=1
                tests+=1
    assert mass == {Fraction(0):24,Fraction(1,80):24,Fraction(1,40):4,Fraction(1,20):12}, mass
    assert sum(x*n for x,n in mass.items())==1
    for a in range(4):
        for b in range(4):
            assert sum(leading(a,b,c) for c in range(4))==Fraction(1,16)
            assert sum(leading(c,a,b) for c in range(4))==Fraction(1,16)
            tests+=2
    # Checks the lag-two marginal against its independently published ratio vector.
    ratio=[Fraction(0)]*4
    for a in range(4):
        for b in range(4):
            for c in range(4):
                ratio[(c-a)%4]+=leading(a,b,c)
    assert ratio==[Fraction(1,10),Fraction(1,2),Fraction(1,10),Fraction(3,10)], ratio
    print(f'VERIFY_OK assertions={tests} exact_depths=1..6 integer_terms={len(observed)} words=40 forbidden=24')

if __name__=='__main__':
    check()
