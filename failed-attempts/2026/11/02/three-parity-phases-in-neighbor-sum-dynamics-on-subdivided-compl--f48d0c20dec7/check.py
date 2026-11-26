"""Finite checks for neighbor-sum evolution on subdivided bicliques.
Pure Python; no external dependency.  This checks finite instances only.
"""
from collections import Counter

def graph(a, b):
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    N=n+len(edges)
    rows=[0]*N
    for k,(i,j) in enumerate(edges):
        u=n+k
        rows[i]^=1<<u;rows[j]^=1<<u
        rows[u]^=(1<<i)|(1<<j)
    return rows

def times(A,x):
    return sum(((x&row).bit_count()&1)<<i for i,row in enumerate(A))

def mprod(A,B):
    out=[]
    for row in A:
        v=0
        while row:
            low=row&-row;k=low.bit_length()-1; v^=B[k]; row-=low
        out.append(v)
    return out

def rank(A):
    basis={}
    for row in A:
        while row:
            k=row.bit_length()-1
            if k in basis: row^=basis[k]
            else:
                basis[k]=row;break
    return len(basis)

def expected(a,b):
    n=a+b; N=n+a*b
    if a%2==0 and b%2==0:
        nil={4:2,3:n-4,1:(a-2)*(b-2)};uni={};d=0
    elif a%2 and b%2:
        nil={3:1,1:(a-1)*(b-1)};uni={2:n-2};d=2*(n-2)
    else:
        s=a if a%2==0 else b
        o=b if a%2==0 else a
        nil={3:o-1,1:(s-2)*(o-1)+1};uni={4:1,2:s-2};d=2*s
    assert sum(k*v for k,v in nil.items())+sum(k*v for k,v in uni.items())==N
    ranks=[sum(max(k-t,0)*v for k,v in nil.items())+d for t in range(8)]
    fixes=[sum(min(k,(1 if t==1 else (2 if t==2 else 4)))*v for k,v in uni.items()) for t in [1,2,4]]
    return ranks,fixes,nil,uni

def sum_xor(vals):
    v=0
    for x in vals:v^=x
    return v

def check():
    cases=rank_comparisons=fixed_comparisons=0
    for a in range(1,10):
        for b in range(1,10):
            A=graph(a,b);N=len(A)
            er,ef,_,_=expected(a,b)
            P=[1<<i for i in range(N)]
            assert rank(P)==N
            for t in range(8):
                if t:P=mprod(P,A)
                assert rank(P)==er[t],(a,b,t,rank(P),er[t])
                rank_comparisons+=1
                if t in (1,2,4):
                    qrank=rank([row^(1<<i) for i,row in enumerate(P)])
                    assert N-qrank==ef[(1,2,4).index(t)],(a,b,t,N-qrank,ef)
                    fixed_comparisons+=1
            cases+=1
    print('GF(2) matrix rank matches:', cases, 'parameter pairs;', rank_comparisons,'ranks;',fixed_comparisons,'return-space ranks')
    trajectories=0;checked_groups=0
    for a in range(1,5):
        for b in range(1,5):
            A=graph(a,b);N=len(A)
            if N>15:continue
            er,ef,_,_=expected(a,b)
            d=er[-1]
            direct=[0]*6
            cycles=Counter()
            for x in range(1<<N):
                hist=[x]
                for t in range(1,9):hist.append(times(A,hist[-1]))
                is_per=lambda t:hist[t]==hist[t+4]
                tau=next(i for i in range(5) if is_per(i))
                direct[tau]+=1
                if tau==0:
                    per=next(k for k in [1,2,4] if hist[k]==hist[0]);cycles[per]+=1
                trajectories+=1
            for t in range(5):
                predicted=2**(N-er[t]+d) if t<4 else 2**N
                assert sum(direct[:t+1])==predicted,(a,b,t,direct,predicted)
            assert sum(cycles.values())==2**d
            assert cycles[1]==2**ef[0]
            assert cycles[1]+cycles[2]==2**ef[1]
            assert cycles[1]+cycles[2]+cycles[4]==2**ef[2]
            checked_groups+=1
    print('GF(2) exhaustive:',checked_groups,'parameter pairs;', trajectories,'initial states with transient and orbit census checks')
    # GF(4) additive evolution, directly on q-ary coordinate lists.
    # No multiplication is used by the neighbor-sum update.
    pairs=[(1,1),(1,2),(1,3),(2,2)]
    Nstates=0
    for a,b in pairs:
        A=graph(a,b);N=len(A)
        er,ef,_,_=expected(a,b)
        total=4**N
        hist_count=[0]*5; fcounts=[0]*3
        # Verify all states using explicit four-valued coordinates.
        for x in range(total):
            y=x; arr=[]
            for _ in range(N):arr.append(y%4);y//=4
            H=[arr]
            for t in range(8):
                old=H[-1];H.append([sum_xor([old[j] for j in range(N) if (A[i]>>j)&1]) for i in range(N)])
            tau=next(t for t in range(5) if H[t]==H[t+4]);hist_count[tau]+=1
            if H[0]==H[1]:fcounts[0]+=1
            if H[0]==H[2]:fcounts[1]+=1
            if H[0]==H[4]:fcounts[2]+=1
        for t in range(5): assert sum(hist_count[:t+1])==4**(N-er[t]+er[-1]),(a,b,t)
        for obs,ex in zip(fcounts,ef): assert obs==4**ex,(a,b,obs,ex)
        Nstates+=total
    print('GF(4) exhaustive:',len(pairs),'parameter pairs;',Nstates,'initial states, all transient and fixed-space counts')

if __name__=='__main__':check()
