"""Self-contained finite checks for distinct quadratic-value triple convolution."""
from collections import Counter
from fractions import Fraction


def squares(k):
    m = 1 << k
    return {x*x % m for x in range(m)}


def S(k):
    if k == 0: return 1
    if k in (1, 2): return 2
    return (1 << (k - 3)) + S(k - 2)


def formula(k, t):
    m = 1 << k
    t %= m
    if k < 5:
        ss = squares(k)
        return sum(1 for a in ss for b in ss if (t-a-b) % m in ss)
    u = 1 << (k - 3)
    a = S(k - 4)
    b = 1 << (k - 5)
    if t % 4 == 0:
        return formula(k-2, t//4)
    return {1: 3*(a*a+b*b),2:3*u*a,3:u*u,
            5:6*a*b,6:3*u*b}.get(t%8,0)


def test():
    checks=0
    for k in range(1, 13):
        m=1<<k
        q=squares(k)
        assert S(k)==len(q)
        c2=[0]*m
        for a in q:
            for b in q:
                c2[(a+b)%m]+=1
        c3=[0]*m
        for t,v in enumerate(c2):
            if v:
                for a in q:
                    c3[(t+a)%m]+=v
        for t,n in enumerate(c3):
            assert formula(k,t)==n,(k,t,formula(k,t),n)
            checks+=1
        assert sum(c3)==len(q)**3
        if k>=6:
            u=1 << (k-3)
            assert max(c3)==u*u
            assert {i for i,n in enumerate(c3) if n==u*u}==set(range(3,m,8))
        if k>=5:
            a,b,u=S(k-4),1<<(k-5),1<<(k-3)
            vals=(3*(a*a+b*b),3*u*a,u*u,6*a*b,3*u*b)
            E_k=sum(z*z for z in c3)
            E_prev=sum(formula(k-2,t)**2 for t in range(1<<(k-2)))
            assert E_k==E_prev+(1<<(k-3))*sum(z*z for z in vals)
    expected=Fraction(485,9427968)
    coeffs=(Fraction(5,1536),Fraction(1,256),Fraction(1,64),Fraction(1,512),Fraction(3,256))
    assert expected == sum(z*z for z in coeffs)/8/(1-Fraction(1,1024))
    print('TRIPLE_SQUARE_IMAGE_CHECK_OK',checks,'target comparisons, 12 levels')


if __name__=='__main__':
    test()
