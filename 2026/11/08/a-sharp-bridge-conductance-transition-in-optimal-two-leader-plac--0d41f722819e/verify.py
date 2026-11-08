#!/usr/bin/env python3
"""Exact rational checks for the weighted two-clique leader placement theorem.

Uses Python's standard library. Finite tests supplement, and do not replace,
the all-parameter rational proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def trace_inverse(A):
    n = len(A)
    aug = [list(map(F, row)) + [F(i == j) for j in range(n)]
           for i, row in enumerate(A)]
    for c in range(n):
        pivot = next((i for i in range(c, n) if aug[i][c]), None)
        if pivot is None:
            raise AssertionError('singular grounded matrix')
        aug[c], aug[pivot] = aug[pivot], aug[c]
        piv = aug[c][c]
        aug[c] = [a / piv for a in aug[c]]
        for r in range(n):
            if r != c and aug[r][c]:
                factor = aug[r][c]
                aug[r] = [a - factor * b for a, b in zip(aug[r], aug[c])]
    return sum(aug[i][n + i] for i in range(n))


def laplacian(p, q, t):
    N = p + q
    A = [[F(0) for _ in range(N)] for _ in range(N)]
    def edge(i,j,w):
        A[i][i] += w; A[j][j] += w
        A[i][j] -= w; A[j][i] -= w
    for lo, hi in ((0,p), (p,N)):
        for i in range(lo,hi):
            for j in range(i+1,hi):edge(i,j,F(1))
    edge(0,p,t)
    return A


def objective(A,S):
    rem = [i for i in range(len(A)) if i not in S]
    return trace_inverse([[A[i][j] for j in rem] for i in rem])


def predicted(p,q,t):
    p=F(p);q=F(q);t=F(t)
    phi=4-F(2,p)-F(2,q)
    delta=t*(p*p*(q+2)+q*q*(p+2))/(p*q*(p*q+2*(p+q)*t))
    gain_p=t*(p+2)/(p*(p+2*t))
    gain_q=t*(q+2)/(q*(q+2*t))
    ga=phi+q/t-(p+2)/(2*p)
    gb=phi+p/t-(q+2)/(2*q)
    return {'GG':phi,'IG':phi-gain_p,'GI':phi-gain_q,
            'II':phi-delta,'GA':ga,'GB':gb,
            'AA':ga+3*q/(2*p),'BB':gb+3*p/(2*q)}


def category(S,p):
    a,b=S
    def kind(v):
        return ('G' if v==0 else 'I') if v<p else ('G' if v==p else 'I')
    if a<p and b>=p:return kind(a)+kind(b)
    if b<p:return ('GA' if a==0 else 'AA')
    return ('GB' if a==p else 'BB')


def theorem_types(p,q,t):
    assert p<=q
    if p==q: return {'II'}
    threshold=F(p*p*(q+2), 4*(q-p))
    if t<threshold:return {'II'}
    if t>threshold:return {'IG'}
    return {'II','IG'}


def main():
    matrices=0;pairs=0;ties=0
    for p in range(3,7):
        for q in range(p,8):
            weights={F(1,7),F(1,2),F(1),F(2),F(7),F(19)}
            if p<q:
                tc=F(p*p*(q+2),4*(q-p))
                weights.update({tc/2,tc,tc*2})
            for t in sorted(weights):
                A=laplacian(p,q,t); forms=predicted(p,q,t)
                values={}
                for pair in combinations(range(p+q),2):
                    lab=category(pair,p)
                    actual=objective(A,pair)
                    assert actual==forms[lab],(p,q,t,pair,lab,actual,forms[lab])
                    values[pair]=actual; pairs+=1
                best=min(values.values())
                labels={category(S,p) for S,v in values.items() if v==best}
                want=theorem_types(p,q,t)
                assert labels==want,(p,q,t,labels,want)
                if len(labels)>1:ties+=1
                matrices+=1
    # Exact algebraic sign certificates, tested at arbitrary-scale rational instances
    for p in range(3,17):
        for q in range(p,21):
            for t in [F(1,17),F(2,3),F(1),F(49),F(1100,3)]:
                f=predicted(p,q,t)
                assert f['GG']-f['II']==t*(p*p*q+2*p*p+p*q*q+2*q*q)/(p*q*(p*q+2*t*(p+q)))
                assert f['AA']-f['GA']==F(3*q,2*p)
                assert f['BB']-f['GB']==F(3*p,2*q)
                assert f['GA']-f['IG']==(2*p*q+(4*q-p-2)*t)/(2*t*(p+2*t))
                assert f['GB']-f['IG']==(2*p**3*q+p*p*(3*q-2)*t+4*(q-p)*t*t)/(2*p*q*t*(p+2*t))
                assert f['GI']-f['IG']==t*(q-p)*(p*q+2*p+2*q+4*t)/(p*q*(p+2*t)*(q+2*t))
                assert f['IG']-f['II']==t*(p*p*(q+2)-4*(q-p)*t)/(q*(p+2*t)*(p*q+2*t*(p+q)))
    print('VERIFY_OK:',matrices,'exact rational graph-weight cases,',pairs,
          'exhaustive leader-pair objectives,',ties,'two-class threshold cases;'
          ' exact sign-identity comparisons passed')

if __name__=='__main__': main()
