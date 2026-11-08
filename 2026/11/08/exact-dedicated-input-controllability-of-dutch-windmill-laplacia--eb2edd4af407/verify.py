from itertools import combinations

def graph(m,l):
    n=1+m*(l-1)
    L=[[0]*n for _ in range(n)]
    for r in range(m):
        cyc=[0]+[1+r*(l-1)+k for k in range(l-1)]
        for k in range(l):
            a,b=cyc[k],cyc[(k+1)%l]
            L[a][a]+=1;L[b][b]+=1
            L[a][b]-=1;L[b][a]-=1
    return L

def rank_mod_cols(cols,p,n):
    basis={}
    for c in cols:
        v=[a%p for a in c]
        while True:
            nz=next((i for i,x in enumerate(v) if x),None)
            if nz is None:break
            if nz in basis:
                b=basis[nz]; c0=v[nz]
                for j in range(nz,n):v[j]=(v[j]-c0*b[j])%p
            else:
                d=pow(v[nz],-1,p)
                basis[nz]=[t*d%p for t in v]
                break
        if len(basis)==n:return n
    return len(basis)

def krylov_rank(L,S,p):
    n=len(L)
    col=[]
    cur=[[int(i==s) for i in range(n)] for s in S]
    for _ in range(n):
        col.extend(cur)
        cur=[[sum(L[i][j]*v[j] for j in range(n))%p for i in range(n)] for v in cur]
    return rank_mod_cols(col,p,n)

def forcing_possible(L,S):
    n=len(L); color=set(S)
    while True:
        t=set(color)
        for v in color:
            w=[i for i in range(n) if L[v][i]==-1 and i not in color]
            if len(w)==1:t.add(w[0])
        if len(t)==len(color):break
        color=t
    return len(color)==n

if __name__=='__main__':
    tested=0
    for m in range(2,6):
        for ell in range(3,12):
            L=graph(m,ell); n=len(L)
            S=[1+r*(ell-1) for r in range(m)]
            for p in (1000003,1000033):
                k=krylov_rank(L,S,p)
                assert k==n,(m,ell,p,k,n)
            assert not forcing_possible(L,S)
            assert forcing_possible(L,[0]+S)
            tested+=1
    exhaust=0
    for m,ell in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5)]:
        L=graph(m,ell)
        for k in range(m+1):
            for S in combinations(range(len(L)),k):
                assert not forcing_possible(L,S),(m,ell,S)
                exhaust+=1
    print('VERIFY_OK', 'pairs',tested, 'modular full-rank checks',2*tested,'exhaustive low-cardinality forcing trials',exhaust)
