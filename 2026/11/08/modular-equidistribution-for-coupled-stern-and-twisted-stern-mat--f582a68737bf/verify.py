"""Exact finite checks for coupled Stern/twisted-Stern matrix distribution."""
from collections import Counter, deque
from math import gcd

def compute(max_r=16):
    N=1<<(max_r+1)
    s=[0]* (N+2); t=[0]*(N+2)
    s[1]=t[1]=1
    for n in range(2,N+2):
        if n%2==0:
            s[n]=s[n//2];t[n]=-t[n//2]
        else:
            k=n//2;s[n]=s[k]+s[k+1];t[n]=-t[k]-t[k+1]
    assert s[:16]==[0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4]
    group_checks=0; det_checks=0; pair_checks=0
    report=[]
    for m in (3,5,7,9,11,15):
        G=sum(1 for a in range(m) for b in range(m) for c in range(m) for d in range(m) if (a*d-b*c)%m==(-2)%m)
        P=sum(1 for a in range(m) for b in range(m) if gcd(gcd(a,b),m)==1)
        assert G==m*P,(m,G,m*P)
        # Independent finite Cayley-graph reachability check.
        queue=deque([(1,0,0,1)]); reached={(1,0,0,1)}
        while queue:
            a,b,c,d=queue.popleft()
            for nxt in ((a,(a+b)%m,c,(c+d)%m),((a+b)%m,b,(c+d)%m,d)):
                if nxt not in reached:
                    reached.add(nxt);queue.append(nxt)
        assert len(reached)==G,(m,len(reached),G)
        for n in range(1,1025):
            a,b,c,d=1,0,0,1
            for bit in bin(n)[3:]:
                if bit=='0':a,b,c,d=a,(a+b)%m,c,(c+d)%m
                else:a,b,c,d=(a+b)%m,b,(c+d)%m,d
            # M_1 has entries (1,1;1,-1).
            A,B,C,D=(a+c)%m,(b+d)%m,(a-c)%m,(b-d)%m
            r=n.bit_length()-1
            assert (A,B,C,D)==(s[n]%m,s[n+1]%m,(-1)**r*t[n]%m,(-1)**r*t[n+1]%m)

        for r in range(1,max_r+1):
            counts=Counter(); pairs=Counter()
            for n in range(1<<r,1<<(r+1)):
                M=((s[n]%m,s[n+1]%m),(t[n]%m,t[n+1]%m))
                det=(M[0][0]*M[1][1]-M[0][1]*M[1][0])%m
                assert det==(-2*(-1)**r)%m,(m,r,n)
                det_checks+=1
                normalized=(M[0][0],M[0][1],(-1)**r*M[1][0]%m,(-1)**r*M[1][1]%m)
                assert (normalized[0]*normalized[3]-normalized[1]*normalized[2])%m==(-2)%m
                counts[normalized]+=1;pairs[(M[0][0],M[1][0])]+=1
                pair_checks+=1
            if r==max_r:
                present=len(counts); expected=G
                assert present<=expected, (m,r,present,expected)
                assert len(pairs)<=P, (m,r,len(pairs),P)
                maxmatrixdev=max([abs(v-(1<<r)/G) for v in counts.values()]+([(1<<r)/G] if present<expected else []))/((1<<r)/G)
                maxpairdev=max([abs(v-(1<<r)/P) for v in pairs.values()]+([(1<<r)/P] if len(pairs)<P else []))/((1<<r)/P)
                report.append((m,G,P,present,len(pairs),round(maxmatrixdev,3),round(maxpairdev,3)))
        group_checks+=1
    # algebraic word identity, using first-row/right multiplication recurrences for n up to 2^12
    for n in range(1,1<<12):
        for d in (0,1):
            k=2*n+d
            if d==0:
                assert (s[k],s[k+1],t[k],t[k+1])==(s[n],s[n]+s[n+1],-t[n],-t[n]-t[n+1])
            else:
                assert (s[k],s[k+1],t[k],t[k+1])==(s[n]+s[n+1],s[n+1],-t[n]-t[n+1],-t[n+1])
    print('VERIFY_OK determinant_cases=%d residue_pair_cases=%d group_moduli=%d recurrence_checked=%d' %(det_checks,pair_checks,group_checks,8190))
    print('modulus,|SL2|,primitive_pairs,observed_matrices,observed_pairs,max_matrix_rel_discrepancy,max_pair_rel_discrepancy')
    for row in report: print(*row,sep=',')

if __name__=='__main__':compute()
