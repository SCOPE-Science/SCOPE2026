"""Exact checks for two-environment coordination on fully shared complete graphs.

Run: python verify.py
Uses only the Python standard library and rational arithmetic.
"""
from fractions import Fraction as Q
from math import comb, log


def data(N,a,b,p):
    assert 2 <= N and 0 <= a < b <= N-1 and 0 < p < 1
    pi=[Q(comb(N,k))*p**k*(1-p)**(N-k) for k in range(N+1)]
    # Fictitious reversible conductances at the absorbing endpoints
    R={j: Q(N)/(pi[j]*p*(N-j)) for j in range(a,b+1)}
    S={a-1:Q(0)}
    for j in range(a,b+1):S[j]=S[j-1]+R[j]
    z=S[b]
    lower=N*sum((Q(1,j) for j in range(1,a+1)),Q(0))
    upper=N*sum((Q(1,j) for j in range(1,N-b)),Q(0))
    H=[Q(0) for _ in range(N+1)]
    E=[Q(0) for _ in range(N+1)]
    for i in range(N+1):
        if i<=a: H[i]=Q(0); E[i]=N*sum((Q(1,j) for j in range(1,i+1)),Q(0))
        elif i>=b+1: H[i]=Q(1); E[i]=N*sum((Q(1,j) for j in range(1,N-i+1)),Q(0))
        else:
            H[i]=S[i-1]/z
            hit=sum((pi[k]*S[min(i,k)-1]*(z-S[max(i,k)-1])/z for k in range(a+1,b+1)),Q(0))
            E[i]=hit+(1-H[i])*lower+H[i]*upper
    return H,E


def direct_one_step(mask,N,a,b,p):
    # Test actual pairwise game payoffs (not birth-death aggregation).
    choices={}
    for th,env_p in ((a,p),(b,1-p)):
        for v in range(N):
            bit=(mask>>v)&1
            neighbours_A=mask.bit_count()-bit
            A=Q(neighbours_A)-Q(N-1-neighbours_A)*Q(th,N-1)
            B=Q(neighbours_A)*Q(th,N-1)
            new=bit if A==B else int(A>B)
            nxt=(mask | (1<<v)) if new else (mask &~(1<<v))
            choices[nxt]=choices.get(nxt,Q(0))+env_p/N
    assert sum(choices.values())==1
    return choices


def inspect():
    Ncases=0; states=0
    for N in range(3,9):
      for a in range(0,N-1):
       for b in range(a+1,N):
        for p in (Q(1,3),Q(1,2),Q(3,5)):
            H,E=data(N,a,b,p)
            assert H[0]==0 and H[N]==1 and E[0]==E[N]==0
            for mask in range(1<<N):
                i=mask.bit_count()
                if i in (0,N):continue
                moves=direct_one_step(mask,N,a,b,p)
                assert H[i]==sum((w*H[t.bit_count()] for t,w in moves.items()),Q(0)),('H',N,a,b,p,mask)
                assert E[i]==1+sum((w*E[t.bit_count()] for t,w in moves.items()),Q(0)),('E',N,a,b,p,mask,E[i])
                states+=1
            Ncases+=1
    assert data(4,1,2,Q(1,2))[0][2]==Q(1,2)
    print('Exact rational test: PASS, parameter cases:',Ncases,'labeled-state Bellman equations:',states)
    for N,a,b,p,i in [(10,2,7,Q(1,2),5),(10,2,7,Q(2,5),5),(12,2,8,Q(3,5),7)]:
        H,E=data(N,a,b,p)
        print('Example',N,a,b,str(p),i,'P_A',str(H[i]),'E',str(E[i]),'~',float(E[i]))
    # Check finite-scale log rate near several entropy barriers, never as proof.
    for al,be,p in [(Q(1,4),Q(3,4),Q(1,2)),(Q(1,5),Q(3,5),Q(2,5))]:
        D=lambda t: float(t)*log(float(t/p))+float(1-t)*log(float((1-t)/(1-p)))
        print('Expected entropy barrier',min(D(al),D(be)))

if __name__=='__main__':inspect()
