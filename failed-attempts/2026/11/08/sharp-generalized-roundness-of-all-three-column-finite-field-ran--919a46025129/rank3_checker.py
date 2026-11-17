"""Exact finite-field Fourier checks for three-column rank-distance powers.
Run: python rank3_checker.py . Requires Python 3 standard library only.
No external artifacts are needed.
"""
from itertools import product


def formulas(q,m,s):
    t=q**m; h=q*q+q+1
    H1={0:t*h, 1:t*(q+1), 2:t, 3:0}[s]
    H2={0:t*t*h, 1:t*t, 2:0, 3:0}[s]
    F1=H1-h
    F2=H2-(q+1)*F1-h
    F3=(t**3 if s==0 else 0)-1-F1-F2
    return (1,F1,F2,F3)


def rank_matrix_flat(v,m,p,addition,multiplication,inv):
    a=[list(v[3*i:3*i+3]) for i in range(m)]
    r=0
    for col in range(3):
        pivot=next((i for i in range(r,m) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        mul=inv[a[r][col]]
        a[r]=[multiplication[mul][x] for x in a[r]]
        for i in range(r+1,m):
            f=a[i][col]
            if f:
                a[i]=[addition[x][multiplication[f][y]] for x,y in zip(a[i],a[r])]
        r+=1
        if r==3:break
    return r


def field(q):
    if q in (2,3):
        add=[[ (a+b)%q for b in range(q)] for a in range(q)]
        mul=[[ (a*b)%q for b in range(q)] for a in range(q)]
        inv=[0]+[next(b for b in range(1,q) if a*b%q==1) for a in range(1,q)]
        # character values represented as counts by phase in F_p
        tr=list(range(q))
        return add,mul,inv,tr,q
    if q==4:
        # x^2+x+1, symbols bit-coded 0,1,x,x+1.
        add=[[a^b for b in range(4)] for a in range(4)]
        def mult(a,b):
            out=0
            if a&1:out^=b
            if a&2:
                xb=((b&1)<<1)^(3 if b&2 else 0) # x*x=x+1 in GF(4)
                out^=xb
            return out
        mul=[[mult(a,b) for b in range(4)] for a in range(4)]
        inv=[0]+[next(b for b in range(1,4) if mul[a][b]==1) for a in range(1,4)]
        # Tr(z)=z+z², zero on 0,1, one on x and x+1.
        tr=[0,0,1,1]
        return add,mul,inv,tr,2
    raise ValueError(q)


def direct(q,m):
    addition,multiplication,inv,tr,p=field(q)
    X=list(product(range(q),repeat=3*m))
    ranks=[rank_matrix_flat(x,m,q,addition,multiplication,inv) for x in X]
    if q==2 and m==3:
        # Full Walsh transform of each rank shell at every frequency.
        spectra=[]
        for j in range(4):
            a=[int(r==j) for r in ranks]
            n=len(a); step=1
            while step<n:
                for k in range(0,n,2*step):
                    for i in range(k,k+step):
                        u,v=a[i],a[i+step]
                        a[i],a[i+step]=u+v,u-v
                step*=2
            spectra.append(a)
        for b in range(len(X)):
            sb=ranks[b]
            assert tuple(spectra[j][b] for j in range(4))==formulas(q,m,sb),(b,sb)
        print('FULL_WALSH_F2_M3',len(X))
    else:
        # Rank representatives B of each possible frequency rank.
        for s in range(4):
            B=[0]*(3*m)
            for i in range(s): B[3*i+i]=1
            assert rank_matrix_flat(B,m,q,addition,multiplication,inv)==s
            phase=[0]*p
            vals=[[0]*p for _ in range(4)]
            for x,r in zip(X,ranks):
                z=0
                for a,b in zip(x,B):
                    z=addition[z][multiplication[a][b]]
                vals[r][tr[z]]+=1
            if p==2:
                got=tuple(v[0]-v[1] for v in vals)
                assert got==formulas(q,m,s),(q,m,s,got,formulas(q,m,s))
            else:
                # For odd p the predicted value is an integer, so its
                # cyclotomic coefficient vector is constant off phase zero.
                pred=formulas(q,m,s)
                for r in range(4):
                    assert len(set(vals[r][1:]))<=1
                    got=vals[r][0]-vals[r][1]
                    assert got==pred[r],(q,m,s,r,got,pred[r],vals[r])
        print('EXACT_FOURIER_REPRESENTATIVES',q,m,len(X))


def crit(q,m):
    t=q**m;h=q*q+q+1
    def f(a):
        return (t-h)+ (-(q+1)*t+q*h)*2**a+(q*t-(q-1)*h-1)*3**a
    lo,hi=0.,1.
    assert f(lo)<0<f(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    root=(lo+hi)/2
    for a in (0.0,root*0.5,root, min(.99,(1+root)/2)):
        ds=[]
        for s in range(1,4):
            _,a1,a2,a3=formulas(q,m,s)
            ds.append(a1+2**a*a2+3**a*a3)
        assert ds[1]>=ds[0]-1e-7 and ds[1]>=ds[2]-1e-7,(q,m,a,ds)
    return root

if __name__=='__main__':
    direct(2,3)
    direct(2,4)
    direct(3,3)
    direct(4,3)
    for q in (2,3,4,5,7):
        for m in (3,4,6):
            r=crit(q,m)
            print('CRITICAL',q,m,'%.10f'%r)
    print('ALL_RANK3_FOURIER_CHECKS_PASSED')
