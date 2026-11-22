"""Exact finite-state verification of one-defect cycle cover-endpoint law.
Run with Python 3.10+; no third-party dependencies."""
from fractions import Fraction as F
from itertools import product
import json

def solve_system(A, B):
    """Gauss-Jordan on a rational matrix with multiple right-hand sides."""
    m=len(A); w=len(B[0]); a=[list(A[i])+list(B[i]) for i in range(m)]
    for j in range(m):
        pivot=next((i for i in range(j,m) if a[i][j]),None)
        assert pivot is not None
        a[j],a[pivot]=a[pivot],a[j]
        t=a[j][j];a[j]=[x/t for x in a[j]]
        for i in range(m):
            if i==j:continue
            t=a[i][j]
            if t: a[i]=[a[i][k]-t*a[j][k] for k in range(m+w)]
    return [row[m:] for row in a]

def independent_full_cover(n,p):
    """Exact first-step solution on (current vertex, visited mask)."""
    allmask=(1<<n)-1
    f={(allmask,i):[F(int(j==i)) for j in range(n)] for i in range(n)}
    for size in range(n-1,0,-1):
        for mask in range(1,allmask):
            if mask.bit_count()!=size:continue
            verts=[v for v in range(n) if mask>>v&1]; z={v:i for i,v in enumerate(verts)}
            A=[[F(int(i==j)) for j in range(size)] for i in range(size)]
            B=[[F(0) for j in range(n)] for i in range(size)]
            for i,v in enumerate(verts):
                for nbr,prob in [((v+1)%n,p if v==0 else F(1,2)),
                                 ((v-1)%n,1-p if v==0 else F(1,2))]:
                    nxt=mask|(1<<nbr)
                    if nxt==mask:A[i][z[nbr]]-=prob
                    else:
                        outcome=f[nxt,nbr]
                        for j in range(n):B[i][j]+=prob*outcome[j]
            val=solve_system(A,B)
            for i,v in enumerate(verts):f[mask,v]=val[i]
    return f[1,0]

def tail(n,k,p):
    q=1-p
    return (n-k)*p/((k-1)*q+(n-k)*p)

def law(n,p):
    q=1-p
    return [F(0)]+[(n-1)*p*q/(((k-1)*q+(n-k)*p)*(k*q+(n-k-1)*p)) for k in range(1,n)]

def numerical_independent(n,p):
    # Non-absorbing one-dimensional Dirichlet problem: first-step
    # equations on the path between absorbing neighbors k-1,k.
    from fractions import Fraction
    out=[]
    for k in range(2,n):
        left=k;right=k-1
        path=[(k+i)%n for i in range(n)]
        interior=path[1:-1];size=len(interior);z={v:i for i,v in enumerate(interior)}
        A=[[F(int(i==j)) for j in range(size)] for i in range(size)]
        B=[[F(0)] for _ in interior]
        for i,v in enumerate(interior):
            for nb,prob in [((v+1)%n,p if v==0 else F(1,2)),((v-1)%n,1-p if v==0 else F(1,2))]:
                if nb==right:B[i][0]+=prob
                elif nb!=left:A[i][z[nb]]-=prob
        out.append(solve_system(A,B)[z[0]][0])
    return out

def main():
    asserts=0
    grid=[F(1,5),F(1,3),F(1,2),F(3,5),F(4,5)]
    for n in range(3,22):
        for p in grid:
            z=law(n,p)
            assert z[0]==0;assert sum(z)==1;assert all(v>0 for v in z[1:]);asserts+=3
            for k in range(1,n):
                assert z[k] == tail(n,k,p) - (tail(n,k+1,p) if k+1<n else F(0));asserts+=1
            for k,first in enumerate(numerical_independent(n,p),2):
                assert first==tail(n,k,p);asserts+=1
    exact_states=0
    for n in range(3,8):
        for p in [F(1,4),F(2,5),F(1,2),F(3,4)]:
            got=independent_full_cover(n,p)
            expected=law(n,p)
            for a,b in zip(got,expected):assert a==b;asserts+=1
            exact_states+=1
    # p-derivative of the tail is strictly positive for every nontrivial cut.
    import math
    for n in range(3,22):
        for k in range(2,n):
            a=n-k;b=k-1
            for p in grid:
                q=1-p
                assert a*b>0 and (a*p+b*q)>0;asserts+=1
    output={"status":"PASS","assertions":asserts,"exact_cover_system_cases":exact_states,"largest_checked_cycle":21,"rational_parameters":[str(x) for x in grid],"checker":"self-contained exact rational finite-state Markov verification; the universal claim is proved analytically"}
    print(json.dumps(output,sort_keys=True))
if __name__=='__main__':main()
