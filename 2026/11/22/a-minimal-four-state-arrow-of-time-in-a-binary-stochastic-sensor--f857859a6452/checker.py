"""Reproducible finite checks for the four-state binary-observation theorem.

Requires Python 3, SymPy, NumPy, SciPy. This program is not a proof
of the all-rates or all-time statements; those appear in RESULT.md.
"""
import itertools
import random
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
import sympy as sp


def exact_coefficient_check():
    a, b, c, d = rates = sp.symbols('a b c d', positive=True)
    Q = sp.zeros(4)
    for i, rate in enumerate(rates):
        Q[i, i] = -rate
        Q[i, (i + 1) % 4] = rate
    Z = a*b*c + a*b*d + a*c*d + b*c*d
    pi = sp.Matrix([[b*c*d, a*c*d, a*b*d, a*b*c]])/Z
    M = {1: sp.diag(1,0,1,0), 0: sp.diag(0,1,0,1)}
    one = sp.ones(4, 1)
    powers = [sp.eye(4), Q, Q**2/2, Q**3/6]
    def coefficient(word, k):
        result = 0
        for i in range(k + 1):
            for j in range(k - i + 1):
                l = k - i - j
                result += (pi*M[word[0]]*powers[i]*M[word[1]]*
                           powers[j]*M[word[2]]*powers[l]*M[word[3]]*one)[0]
        return sp.factor(result)
    for k in range(3):
        assert sp.cancel(coefficient((1,1,0,0),k)-coefficient((0,0,1,1),k)) == 0
    expected = a*b*c*d*(a-c)*(b-d)/Z
    assert sp.factor(coefficient((1,1,0,0),3)-coefficient((0,0,1,1),3)-expected)==0
    print('PASS: all-symbol exact stationary vector, zero coefficients 0..2 and cubic coefficient')


def numerical_checks():
    rng = random.Random(14708)
    M = {1: np.diag([1,0,1,0]), 0: np.diag([0,1,0,1])}
    one = np.ones(4)
    word1, word0 = (1,1,0,0), (0,0,1,1)
    trials=0
    for _ in range(20):
        rates = np.array([rng.uniform(.7, 5.0) for _ in range(4)])
        Q=np.zeros((4,4))
        for i,v in enumerate(rates):
            Q[i,i]=-v;Q[i,(i+1)%4]=v
        pi=(1/rates)/np.sum(1/rates)
        a,b,c,d=rates
        predicted=a*b*c*d*(a-c)*(b-d)/(a*b*c+a*b*d+a*c*d+b*c*d)
        def prob(word,h):
            T=expm(h*Q)
            vec=pi@M[word[0]]
            for label in word[1:]:vec=vec@T@M[label]
            return vec@one
        hs=[0.0009,0.0015,0.0025]
        observed=np.array([(prob(word1,h)-prob(word0,h))/h**3 for h in hs])
        # The asymptotic error is O(h), with a moderate rate-dependent coefficient.
        assert abs(observed[0]-predicted)<.10 +.08*abs(predicted)
        if abs(predicted)>.005:
            assert abs(observed[0]-predicted)<abs(observed[-1]-predicted)+.015
        trials+=1
    for rr in ([1,2,1,4],[1,2,3,2],[1,2,1,2]):
        Q=np.zeros((4,4))
        for i,v in enumerate(rr):Q[i,i]=-v;Q[i,(i+1)%4]=v
        pi=(1/np.array(rr))/sum(1/np.array(rr))
        for h in (.02,.07,.2,.6,1.0):
            T=expm(h*Q)
            def p(word):
                v=pi@M[word[0]]
                for label in word[1:]:v=v@T@M[label]
                return v@one
            assert abs(p(word1)-p(word0))<4e-14
    print(f'PASS: {trials} random rate instances, {15} exact-reversible equality tests')

    # Three-state directed cycles can be irreversible microscopically, yet
    # every nonconstant two-color observation is path-reversible.
    for forward, backward in (([1.3,2.1,3.7],[.4,.8,.9]),([3.1,1.7,2.4],[.1,.3,.7])):
        Q3=np.zeros((3,3))
        for i in range(3):
            Q3[i,(i+1)%3]+=forward[i]
            Q3[i,(i-1)%3]+=backward[i]
            Q3[i,i]-=forward[i]+backward[i]
        A3=Q3.T.copy();A3[-1,:]=1
        pi3=np.linalg.solve(A3,np.array([0.,0.,1.]))
        for sensor in (np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1])):
            D={1:np.diag(sensor),0:np.diag(1-sensor)}
            for gaps in ((.07,.2,.32),(.2,.2,.2),(.1,.4,.09)):
                TT=[expm(t*Q3) for t in gaps]
                for word in itertools.product((0,1), repeat=4):
                    v=pi3@D[word[0]]
                    for T,label in zip(TT,word[1:]):v=v@T@D[label]
                    pforward=v@np.ones(3)
                    v=pi3@D[word[-1]]
                    for T,label in zip(TT[::-1],word[-2::-1]):v=v@T@D[label]
                    preverse=v@np.ones(3)
                    assert abs(pforward-preverse)<3e-13
    print('PASS: 288 variable-gap binary four-time reversibility checks on irreversible three-state rings')

    # Positive backward rates on every ring edge, positive finite-affinity cycle.
    rr=np.array([1.,2.,3.,4.]); eps=0.025
    Q=np.zeros((4,4))
    for i,v in enumerate(rr):
        Q[i,(i+1)%4]+=v;Q[i,(i-1)%4]+=eps;Q[i,i]-=v+eps
    A=Q.T.copy();A[-1,:]=1.
    rhs=np.array([0.,0.,0.,1.]);pi=np.linalg.solve(A,rhs)
    T=expm(.1*Q)
    def p(word):
        v=pi@M[word[0]]
        for label in word[1:]:v=v@T@M[label]
        return v@one
    delta=p(word1)-p(word0)
    assert delta>.00005 and np.min(pi)>0
    print(f'PASS: bidirectional ring with positive backward rate {eps}; finite-lag witness {delta:.12g}')

if __name__=='__main__':
    exact_coefficient_check()
    numerical_checks()
    print('All finite diagnostics passed; analytic proof is separate.')
