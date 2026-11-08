"""Independent finite checks for field-resonant weak one-spin stability of K_{n,n,n}.

Run with `python3 verify.py`. Standard library only.
"""
from itertools import product
from fractions import Fraction
from math import comb


def predicted(n, t):
    t = abs(Fraction(t))
    if t == 0:
        return 6 * (2**n - 1) + (comb(n, n//2)**3 if n % 2 == 0 else 0)
    if t > 2*n:
        return 1
    if t == 2*n:
        return 3*2**n - 2
    if t.denominator != 1 or t.numerator % 2:
        return 3
    k = t.numerator//2
    return 3 + 3*comb(n,k)**2 + (comb(n,(n+k)//2)**3 if (n+k)%2==0 else 0)


def predicted_strict(n,t):
    t=abs(Fraction(t))
    return 3 if 0<t<2*n else (1 if t>2*n else 0)


def group_count(n,t, strict=False):
    t = Fraction(t)
    answer = 0
    for a,b,c in product(range(n+1), repeat=3):
        A,B,C=2*a-n,2*b-n,2*c-n
        conditions=[]
        for count,neighbor in ((a,B+C),(b,A+C),(c,A+B)):
            if count:
                conditions.append((t>neighbor) if strict else (t>=neighbor))
            if count<n:
                conditions.append((t<neighbor) if strict else (t<=neighbor))
        if all(conditions):
            answer+=comb(n,a)*comb(n,b)*comb(n,c)
    return answer


def energy(spins,n,t):
    a=sum(spins[:n]);b=sum(spins[n:2*n]);c=sum(spins[2*n:])
    return Fraction(a*b+a*c+b*c) - Fraction(t)*(a+b+c)


def brute_count(n,t):
    # Independent bit-level spin enumeration using local energy differences.
    t=Fraction(t)
    weak = strict = non_ground =0
    for bits in range(1<<(3*n)):
        spins=[1 if bits>>i&1 else -1 for i in range(3*n)]
        A=sum(spins[:n]);B=sum(spins[n:2*n]);C=sum(spins[2*n:])
        e=A*B+A*C+B*C-t*(A+B+C)
        # Exact ground energy for positive field below saturation and outside,
        # independently from the single-flip formula.
        u=abs(t)
        emin=-n*n-u*n if u<=2*n else 3*n*n-u*3*n
        deltas=[]
        for i,s in enumerate(spins):
            neighbor=(B+C if i<n else A+C if i<2*n else A+B)
            deltas.append(2*s*(t-neighbor))
        if min(deltas)>=0:
            weak+=1
            if e>emin:
                non_ground+=1
                escaped=False
                for i,d in enumerate(deltas):
                    if d==0:
                        p=i//n
                        for j in range(3*n):
                            if j//n==p:continue
                            # The first spin flip changes the neighbor sum
                            # of every spin in a different part by -2*spins[i].
                            if deltas[j]+4*spins[i]*spins[j] < 0:
                                escaped=True;break
                    if escaped:break
                assert escaped,(n,t,bits)
        if min(deltas)>0:strict+=1
    return weak,strict,non_ground

def test():
    checks=0
    for n in range(1,18):
        fields=[Fraction(i,2) for i in range(-4*n-3,4*n+4)]
        for t in fields:
            a=group_count(n,t)
            b=predicted(n,t)
            assert a==b,(n,t,a,b)
            checks+=1
            a=group_count(n,t,strict=True)
            b=predicted_strict(n,t)
            assert a==b,(n,t,a,b,'strict')
            checks+=1
    for n in range(1,5):
        fields=[Fraction(i,2) for i in range(-4*n-2,4*n+3)]
        for t in fields:
            weak,strict,_=brute_count(n,t)
            assert weak==predicted(n,t),(n,t,weak,'weak')
            assert strict==predicted_strict(n,t),(n,t,strict,'strict')
            checks+=2
    # Stronger finite checksum at n=5 on all exceptional and generic positive fields.
    for t in (Fraction(0),Fraction(1),Fraction(2),Fraction(4),Fraction(6),Fraction(8),Fraction(10),Fraction(11)):
        weak,strict,_=brute_count(5,t)
        assert weak==predicted(5,t)
        assert strict==predicted_strict(5,t)
        checks+=2
    print(f'PASS: {checks} independent group and full-spin assertions; n<=17 group, n<=5 brute.')

if __name__=='__main__':test()
