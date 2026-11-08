"""Exact small-case checks of split-graph spanning-tree covariance.

Run: python3 artifacts/verify.py
Uses only the Python standard library. Finite tests supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations


def graph_edges(p,q):
    return [(i,j) for i in range(p) for j in range(i+1,p)] + [(i,p+j) for i in range(p) for j in range(q)]


def transfer(p,q,edges):
    n=p+q
    arr=[]
    for a,b in edges:
        v=[0]*n; v[a]+=1; v[b]-=1; arr.append(v)
    out=[]
    for u in arr:
        row=[]
        for v in arr:
            dot=sum(a*b for a,b in zip(u,v))
            idot=sum(u[i]*v[i] for i in range(p,n))
            isum=sum(u[p:]); jsum=sum(v[p:])
            row.append(F(dot,n)+(F(1,p)-F(1,n))*(F(idot)-F(isum*jsum,q)))
        out.append(row)
    return out


def theoretical_covariance(p,q):
    ed=graph_edges(p,q)
    K=transfer(p,q,ed)
    return ed, [[K[i][i]-K[i][i]*K[i][i] if i==j else -K[i][j]*K[i][j]
                 for j in range(len(ed))] for i in range(len(ed))]


def is_tree(n, ed, chosen):
    par=list(range(n)); cnt=n
    def root(a):
        while par[a]!=a: a=par[a]
        return a
    for i in chosen:
        u,v=ed[i];u=root(u);v=root(v)
        if u==v: return False
        par[u]=v;cnt-=1
    return cnt==1


def exhaustive_case(p,q):
    ed, cov=theoretical_covariance(p,q)
    n=p+q; m=len(ed)
    first=[0]*m; pairs=[[0]*m for _ in range(m)]; trees=0
    for chosen in combinations(range(m),n-1):
        if not is_tree(n,ed,chosen):continue
        trees+=1
        for i in chosen:
            first[i]+=1
            for j in chosen: pairs[i][j]+=1
    assert trees==n**(p-1)*p**(q-1), (p,q,trees)
    for i in range(m):
        for j in range(m):
            observed=F(pairs[i][j],trees)-F(first[i]*first[j],trees*trees)
            assert observed==cov[i][j],(p,q,i,j,observed,cov[i][j])
    return trees,m*m


def spectrum_trace_case(p,q):
    ed,C=theoretical_covariance(p,q)
    n=p+q
    T=F(2*p+q-3,p*n)
    Q=F(p-1,p*n)
    V=F(p+2*q-1,n*n)
    actual_tr=sum(C[i][i] for i in range(len(C)))
    actual_sq=sum(c*c for row in C for c in row)
    if p==2:
        vals=[(V,1),(Q,q-1),(T,q)]
        tr=sum(val*mul for val,mul in vals)
        sq=sum(val*val*mul for val,mul in vals)
        assert T>V>Q
    else:
        Y=F(2*(n-1),n*n)
        a=F(p+2*q,n*n)
        d=F(2*p*p+2*p*q-3*p+q*q-q,p*n*n)
        zsq=F(q*(p-2),n**4)
        Btr=a+d; Bdet=a*d-zsq
        vals=[(V,1),(Q,q-1),(T,(p-1)*(q-1)),(Y,p*(p-3)//2)]
        tr=sum(val*mul for val,mul in vals)+(p-1)*Btr
        sq=sum(val*val*mul for val,mul in vals)+(p-1)*(Btr*Btr-2*Bdet)
        assert T>Y and T>V and T>Q
        detT=(a-T)*(d-T)-zsq
        assert detT==F(q*(p-2)*(q-3),p*p*n**3)
        detQ=(a-Q)*(d-Q)-zsq
        assert detQ>0 and Btr-2*Q>0
        assert (detT<0 if q==2 else detT==0 if q==3 else detT>0)
    assert tr==actual_tr,(p,q,'trace',tr,actual_tr)
    assert sq==actual_sq,(p,q,'trace2',sq,actual_sq)
    return len(C)*len(C)


def run():
    cases=((2,2),(2,3),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2))
    total_trees=0; total_entries=0
    for p,q in cases:
        trees,entries=exhaustive_case(p,q)
        total_trees+=trees;total_entries+=entries
    profiles=0
    for p in range(2,10):
        for q in range(2,10):
            spectrum_trace_case(p,q)
            profiles+=1
    print('SPLIT_TREE_COVARIANCE_CHECKS_PASSED',
          'profiles='+str(profiles),
          'trees='+str(total_trees),
          'enumerated_entries='+str(total_entries))

if __name__=='__main__':run()
