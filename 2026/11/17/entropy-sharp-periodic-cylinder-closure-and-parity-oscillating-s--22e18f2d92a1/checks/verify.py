"""Exact finite-word checks for periodic-cylinder deficit in finite directed graphs."""
from itertools import product
from math import exp,log

def words(B,n):
    q=len(B)
    walks=[(a,) for a in range(q)]
    for _ in range(n-1):
        walks=[w+(b,) for w in walks for b in range(q) if B[w[-1]][b]]
    return walks

def deficit(B,w):
    n=len(w)
    for p in range(1,n):
        if all(w[i]==w[i+p] for i in range(n-p)) and B[w[p-1]][w[0]]:
            return n-p
    return 0

def trace_power(B,p):
    q=len(B)
    current=[[int(i==j) for j in range(q)] for i in range(q)]
    for _ in range(p):
        current=[[sum(current[i][k]*B[k][j] for k in range(q)) for j in range(q)] for i in range(q)]
    return sum(current[i][i] for i in range(q))

def inspect(B,name,lmb,nmax):
    for n in range(4,nmax+1):
        W=words(B,n); Z=[deficit(B,w) for w in W]
        traces=[trace_power(B,p) for p in range(1,n)]
        assert sum(traces) >=0
        for k in range(1,n):
            N=sum(z>=k for z in Z)
            assert N<=sum(traces[:n-k]),(name,n,k,N,'upper')
            assert N>=traces[n-k-1],(name,n,k,N,'lower')
        if name=='three_colors':
            assert len(W)==3*2**(n-1)
            for p in range(1,n):
                assert traces[p-1]==2**p+2*(-1)**p
        if n in (5,nmax):
            # The exact sum is over uniform admissible length-n words.
            L=log(lmb)
            sub=sum(exp(.7*L*z) for z in Z)/len(W)
            critical=sum(lmb**z for z in Z)/len(W)
            sup=sum(exp(1.3*L*z) for z in Z)/len(W)
            print(name,'n',n,'count',len(W),'EexpBelow',round(sub,5),'EexpCritical/n',round(critical/n,5),'EexpAbove/expectedScale',round(sup/exp(.3*L*n),5))
    print('VERIFY_OK',name,'lengths=4..'+str(nmax),'all_exact_tail_counts_and_traces')

if __name__=='__main__':
    rotor=[[int(i!=j) for j in range(3)] for i in range(3)]
    golden=[[1,1],[1,0]]
    bip=[[0 if (i<2)==(j<2) else 1 for j in range(5)] for i in range(5)]
    inspect(rotor,'three_colors',2,11)
    inspect(golden,'golden_mean',(1+5**.5)/2,13)
    inspect(bip,'period_two',6**.5,8)
