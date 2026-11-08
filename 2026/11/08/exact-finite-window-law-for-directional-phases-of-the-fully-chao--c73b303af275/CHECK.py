"""Independent exact-rational finite-cylinder checks for logistic directional signs.

The logistic map at parameter four is represented by x=sin(pi*z)**2,
with z uniform on [0,1] and z -> 2*z modulo 1. This checker uses
only fractions and interval breakpoints; it does not approximate pi.
"""
from fractions import Fraction as Q
from collections import defaultdict

P = {'+':{'+':Q(1,2),'-':Q(1,2)}, '-':{'+':Q(1),'-':Q(0)}}
PI = {'+':Q(2,3), '-':Q(1,3)}

def cylinders(n):
    cuts={Q(0),Q(1)}
    for j in range(n):
        den=2**j
        for k in range(den):
            cuts.add((Q(k)+Q(1,3))/den)
            cuts.add((Q(k)+Q(2,3))/den)
    cuts=sorted(cuts)
    out=defaultdict(Q)
    for a,b in zip(cuts,cuts[1:]):
        z=(a+b)/2
        w=''
        for j in range(n):
            w+='-' if Q(1,3)<z<Q(2,3) else '+'
            z=(2*z)%1
        out[w]+=b-a
    return dict(out)

def markov_prob(w):
    v=PI[w[0]]
    for a,b in zip(w,w[1:]):
        v*=P[a][b]
    return v

def markov_count_polynomial(n):
    state={('+',0):PI['+'],('-',1):PI['-']}
    for _ in range(n-1):
        next_state=defaultdict(Q)
        for (s,k),v in state.items():
            for t in '+-':
                next_state[(t,k+(t=='-'))]+=v*P[s][t]
        state=next_state
    out=defaultdict(Q)
    for (_,k),v in state.items():
        out[k]+=v
    return {k:v for k,v in out.items() if v}

def main():
    checks=0
    for n in range(1,12):
        paths=cylinders(n)
        assert sum(paths.values())==1
        assert len(paths)>0
        for w,prob in paths.items():
            assert '--' not in w
            assert prob==markov_prob(w),(n,w,prob,markov_prob(w))
            checks+=1
        counts=defaultdict(Q)
        for w,v in paths.items():
            counts[w.count('-')]+=v
        assert counts==markov_count_polynomial(n)
        checks+=1
        if n<=9:
            m=sum(Q(n-2*w.count('-'),n)*v for w,v in paths.items())
            v=sum((Q(n-2*w.count('-'),n)-Q(1,3))**2*p for w,p in paths.items())
            expected=Q(8,27*n)+Q(32,81*n*n)*(1-(-Q(1,2))**n)
            assert m==Q(1,3),(n,m)
            assert v==expected,(n,v,expected)
            checks+=2
    for k in range(0,10):
        paths=cylinders(k+1)
        moment=sum((1 if w[0]=='+' else -1)*(1 if w[-1]=='+' else -1)*p for w,p in paths.items())
        covariance=moment-Q(1,9)
        assert covariance==Q(8,9)*(-Q(1,2))**k,(k,covariance)
        checks+=1
    assert P['+']['+']+P['+']['-']==1
    assert P['-']['+']+P['-']['-']==1
    print('VERIFY_OK checks='+str(checks)+' exact rational cylinders through length 11')

if __name__=='__main__':
    main()
