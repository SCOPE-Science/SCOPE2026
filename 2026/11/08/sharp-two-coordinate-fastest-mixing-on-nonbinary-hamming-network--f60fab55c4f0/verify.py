"""Exact reproducibility checks for two-coordinate Hamming mixing."""
from fractions import Fraction as F
from itertools import product
from math import comb


def eigendata(d, q, a, b):
    D = d * (q - 1)
    E = comb(d, 2) * (q - 1)**2
    vals=[]
    for k in range(d + 1):
        K1 = D - q*k
        K2 = ((D-q*k)**2-(d-k)*(q-1)**2-k)//2
        vals.append(1-a-b+a*F(K1,D)+b*F(K2,E))
    return vals


def choice(d,q):
    if d == 2:
        return F(2*(q-1),q*q), F((q-1)**2,q*q), F(0)
    if (d,q)==(3,3):
        return F(4,21),F(16,21),F(1,7)
    if (d,q)==(3,4):
        return F(0),F(27,28),F(1,7)
    return F(0),F(1),1-F(2*q,d*(q-1))


def full_matrix_test(d,q,a,b,mu):
    X=list(product(range(q),repeat=d))
    D=d*(q-1); E=comb(d,2)*(q-1)**2
    rows=0
    for x in X:
        probs=[]
        for y in X:
            dist=sum(xx!=yy for xx,yy in zip(x,y))
            val= (1-a-b) if dist==0 else (a/D if dist==1 else (b/E if dist==2 else 0))
            probs.append(F(val))
        assert sum(probs)==1
        if d>=3 and not ((d,q)==(3,3) or (d,q)==(3,4)):
            assert all(prob==0 for prob,y in zip(probs,X) if sum(xx!=yy for xx,yy in zip(x,y))!=2)
            for coordinate in range(d):
                for yvalue in range(q):
                    marginal=sum(prob for prob,y in zip(probs,X) if y[coordinate]==yvalue)
                    expected=F(1,1)-F(2,d) if yvalue==x[coordinate] else F(2,d*(q-1))
                    assert marginal==expected
        rows+=1
    return rows


def main():
    trials=0
    for d in range(2,61):
        for q in range(3,51):
            a,b,mu=choice(d,q)
            assert 0<=a and 0<=b and a+b<=1
            ev=eigendata(d,q,a,b)
            assert ev[0]==1
            assert max(map(abs,ev[1:]))==mu,(d,q,ev,mu)
            if d>=3 and (d,q) not in [(3,3),(3,4)]:
                assert ev[1]==mu
                assert a==0 and b==1
            trials+=1
    rows=0
    for d,q in [(2,3),(3,3),(3,4),(4,3),(3,5)]:
        a,b,mu=choice(d,q)
        rows+=full_matrix_test(d,q,a,b,mu)
    # Exact global dual witnesses for the two exceptional three-coordinate cases.
    a,b,_=choice(3,3)
    ev=eigendata(3,3,a,b)
    assert F(3,7)*ev[1]-F(3,7)*ev[2]+F(1,7)*ev[3]==F(1,7)
    a,b,_=choice(3,4)
    ev=eigendata(3,4,a,b)
    assert F(4,7)*ev[1]-F(3,7)*ev[2]==F(1,7)
    print('PASS: %d exact Hamming-spectrum instances; %d full stochastic-matrix rows; two exceptional dual identities.'%(trials,rows))

if __name__=='__main__':
    main()
