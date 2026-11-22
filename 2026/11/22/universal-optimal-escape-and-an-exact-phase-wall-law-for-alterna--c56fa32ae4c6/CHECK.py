"""Direct exact-rational consistency tests for the two-state alternating-hole theorem.
This finite test battery is not a substitute for the all-parameter proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def rowmul(v, A):
    return [sum(v[k]*A[k][j] for k in range(2)) for j in range(2)]

def survival(a,b,word):
    q=1-a
    pi=[b/(b+q),q/(b+q)]
    K=[[[F(0),q],[b,1-b]],[[a,q],[b,F(0)]]]
    for z in word: pi=rowmul(pi,K[z])
    return sum(pi)

def direct(a,b,word):
    q=1-a; pi=[b/(b+q),q/(b+q)]
    P=[[a,q],[b,1-b]]
    v=F(0)
    for seq in product((0,1),repeat=len(word)+1):
        if all(not(seq[t]==word[t] and seq[t+1]==word[t]) for t in range(len(word))):
            p=pi[seq[0]]
            for x,y in zip(seq,seq[1:]):p*=P[x][y]
            v+=p
    return v

checks=0
for a,b in [(F(1,2),F(1,2)),(F(1,3),F(3,4)),(F(99,100),F(99,100)),(F(1,10),F(9,10)),(F(4,5),F(1,5))]:
    q=1-a; d=b+q; r=b*q; gamma=(a+1-b)/d
    K0=[[F(0),q],[b,1-b]]; K1=[[a,q],[b,F(0)]]
    B=mm(K0,K1)
    assert B==[[r,F(0)],[b*(a+1-b),r]]; checks+=1
    for n in range(7):
        w=[i%2 for i in range(2*n)]
        expected=r**n*(1+n*gamma)
        assert survival(a,b,w)==expected; checks+=1
        assert direct(a,b,w)==expected; checks+=1
        w.append(0)
        expected_odd=r**n*q/d*((1+b)+n*(a+1-b))
        assert survival(a,b,w)==expected_odd;checks+=1
    for length in range(1,7):
        for w in product((0,1),repeat=length):
            assert survival(a,b,w)==direct(a,b,w);checks+=1
    # for n>=1, a bridge at block j has identical rational mass for each j
    for n in range(1,7):
        mass=b/d * r**(n-1)*b*(a+1-b)
        for j in range(n):
            # begin at state 1, loop j times; bridge once; then loop n-j-1 times
            assert mass==b/d * r**j * b*(a+1-b)*r**(n-j-1);checks+=1
assert survival(F(99,100),F(99,100),(0,0)) < survival(F(99,100),F(99,100),(0,1))
checks+=1
print('PASS:',checks,'exact-rational checks; finite tests do not prove infinite claims')
