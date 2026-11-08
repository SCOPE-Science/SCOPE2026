"""Direct bracket/stabilizer enumeration for a three-vertex length-two path algebra."""
import itertools, collections, math

# Finite fields of orders 2,3,4,5. 4=F2[t]/(t^2+t+1).
def field(q):
    def add(x,y): return x ^ y if q==4 else (x+y)%q
    def neg(x): return x if q==4 else (-x)%q
    def mul(x,y):
        if q!=4:return x*y%q
        v=0
        for i in range(2):
            for j in range(2):
                if (x>>i)&1 and (y>>j)&1:v^=1<<(i+j)
        # t^2=t+1
        if v&4:v^=7
        return v
    def inv(x):
        for y in range(1,q):
            if mul(x,y)==1:return y
        raise ZeroDivisionError(x)
    return add,neg,mul,inv

def gaussian_rank(mat, q, add, neg, mul, inv):
    a=[list(row) for row in mat]; rows=len(a);cols=len(a[0]) if rows else 0;r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        k=inv(a[r][c]);a[r]=[mul(v,k) for v in a[r]]
        for i in range(rows):
            if i!=r and a[i][c]:
                k=neg(a[i][c]);a[i]=[add(a[i][j],mul(k,a[r][j])) for j in range(cols)]
        r+=1
    return r

def gaussian_rank_cols(cols, q, add,neg,mul,inv):
    if not cols:return 0
    return gaussian_rank(list(map(list,zip(*cols))),q,add,neg,mul,inv)

def calc(a,b,q, enumerate_units=False):
    add,neg,mul,inv=field(q)
    # path basis: e0,e1,e2, u_i (0->1), v_j (1->2), w_ij (0->2)
    paths=[(i,i,()) for i in range(3)]+[(0,1,(i,)) for i in range(a)]+[(1,2,(a+j,)) for j in range(b)]+[(0,2,(i,a+j)) for i in range(a) for j in range(b)]
    D=len(paths); di={p:k for k,p in enumerate(paths)}
    prod=[[None]*D for i in range(D)]
    for i,(x,y,s) in enumerate(paths):
        for j,(z,w,t) in enumerate(paths):
            if y==z:prod[i][j]=di[(x,w,s+t)]
    comm=[[(prod[i][j],prod[j][i]) for j in range(D)] for i in range(D)]
    def fbr(f,i,j):
        h,k=comm[i][j]
        return add(f[h] if h is not None else 0,neg(f[k] if k is not None else 0))
    # rank function matches predicted formula and optionally count actual stabilizer among units.
    unit_coords=None
    if enumerate_units:
        unit_coords=list(itertools.product(range(1,q),repeat=3))
        unit_coords=[v+tail for v in unit_coords for tail in itertools.product(range(q),repeat=D-3)]
    results=collections.Counter()
    Ccounts=collections.Counter()
    nchecked=0
    for alpha in itertools.product(range(q),repeat=a):
      for beta in itertools.product(range(q),repeat=b):
       for C in itertools.product(range(q),repeat=a*b):
        f=(0,0,0)+alpha+beta+C
        Crank=gaussian_rank([list(C[i*b:(i+1)*b]) for i in range(a)],q,add,neg,mul,inv)
        # row and col space: check rank of C with append alpha column, append beta row
        Cmat=[list(C[i*b:(i+1)*b]) for i in range(a)]
        Ra=gaussian_rank([Cmat[i]+[alpha[i]] for i in range(a)],q,add,neg,mul,inv)
        Rb=gaussian_rank(Cmat+[list(beta)],q,add,neg,mul,inv)
        E=(Ra==Crank and Rb==Crank)
        if Crank==0:
            t=int(any(alpha))+int(any(beta));expected=(q*(q-1))**t
        else:
            expected=(q-1)*q**(2*Crank+1) if E else (q-1)**2*q**(2*Crank+2)
        # brute algebra Lie rank
        B=[[fbr(f,i,j) for j in range(D)] for i in range(D)]
        rr=gaussian_rank(B,q,add,neg,mul,inv)
        # brute stabilizer via diagonal constraints and linear kernel count
        possible=0
        for diag in itertools.product(range(1,q),repeat=3):
            L=[B[i] for i in range(D)]
            rhs=[]
            for i in range(D):
                bval=0
                for j in range(3):bval=add(bval,mul(B[i][j],diag[j]))
                rhs.append(neg(bval))
            sub=[row[3:] for row in L]
            r0=gaussian_rank(sub,q,add,neg,mul,inv)
            r1=gaussian_rank([sub[i]+[rhs[i]] for i in range(D)],q,add,neg,mul,inv)
            if r0==r1:possible+=q**((D-3)-r0)
        actual=(q-1)**3*q**(D-3)//possible
        assert actual==expected,(a,b,q,Crank,E,expected,actual,alpha,beta,C,rr)
        assert rr%2==0
        if enumerate_units:
            slow=0
            for g in unit_coords:
                ok=True
                for i in range(D):
                    total=0
                    for j in range(D):total=add(total,mul(B[i][j],g[j]))
                    if total:ok=False;break
                if ok:slow+=1
            assert slow==possible,(a,b,q,f,slow,possible)
        # q^3 diagonal f coefficients have no effect.
        results[expected]+=q**3
        Ccounts[Crank,E,expected]+=q**3
        nchecked+=1
    # Compare independently with the theorem's closed orbit table.
    def qbinom(n,r):
        if r<0 or r>n:return 0
        num=1;den=1
        for i in range(r):num*=q**(n-i)-1;den*=q**(r-i)-1
        return num//den
    def gl(n):
        return math.prod(q**n-q**i for i in range(n))
    predicted=collections.Counter()
    predicted[1]=q**3
    predicted[q*(q-1)]=q**2*((q**a-1)+(q**b-1))//(q-1)
    predicted[q*q*(q-1)**2]=q*(q**a-1)*(q**b-1)//(q-1)**2
    for s in range(1,min(a,b)+1):
        N=qbinom(a,s)*qbinom(b,s)*gl(s)
        predicted[(q-1)*q**(2*s+1)]+=N*q**2//(q-1)
        predicted[(q-1)**2*q**(2*s+2)]+=N*q*(q**(a+b-2*s)-1)//(q-1)**2
    assert {k:v for k,v in predicted.items() if v}=={k:v//k for k,v in results.items()},(a,b,q,predicted,results)
    # expected mathematical group size and total full dual space
    assert sum(results.values())==q**D
    for size,cnt in results.items():assert cnt%size==0
    print('a,b,q:',a,b,q,'dimension',D,'functionals checked',nchecked, 'orbit table:',sorted((k,v//k) for k,v in results.items()))
    return results

if __name__=='__main__':
 for a,b,q,brute in [(1,1,2,True),(1,1,3,True),(1,2,2,True),(1,2,3,False),(2,2,2,False),(2,2,3,False),(1,2,4,False)]:calc(a,b,q,brute)
 print('ALL_PATH_COADJOINT_FIBERS_PASS')
