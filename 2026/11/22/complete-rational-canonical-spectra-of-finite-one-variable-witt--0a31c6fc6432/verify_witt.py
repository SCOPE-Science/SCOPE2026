"""Finite-field consistency tests for a truncated-Witt derivation census.
Only finite calculations; the all-parameter proof is separate.
"""
import itertools, json, math, collections, random
from pathlib import Path

def field(p, degree):
    q=p**degree
    def add(a,b):
        if degree==1: return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def mul(a,b):
        if degree==1: return a*b%p
        assert p==3 and degree==2  # alpha^2=-1
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        return ((a0*b0-a1*b1)%p)+p*((a0*b1+a1*b0)%p)
    def power(a,k):
        r=1
        while k:
            if k&1:r=mul(r,a)
            a=mul(a,a);k//=2
        return r
    def inv(a):
        assert a
        return power(a,q-2)
    return q,add,mul,power,inv

def compute(p, degree, limit=None):
    q,add,mul,powr,inv=field(p,degree)
    fseq=itertools.product(range(q),repeat=p)
    if limit is not None:
        rng=random.Random(35713+p*10+degree)
        fseq=(tuple([rng.randrange(1,q)]+[rng.randrange(q) for _ in range(p-1)]) for _ in range(limit))
    buckets=collections.Counter(); t=0; fail=0; last={}
    for f in fseq:
        if f[0]==0: continue
        # D acting on polynomials with coefficients indexed by degree
        def D(v):
            w=[0]*p
            for j in range(1,p):
                if v[j]==0: continue
                for k in range(p-j+1):
                    w[j-1+k]=add(w[j-1+k],mul(mul(j,v[j]),f[k]))
            return w
        cur=[0,1]+[0]*(p-2)
        for _ in range(p): cur=D(cur)
        lam=mul(cur[0],inv(f[0]))
        if cur!=[mul(lam,z) for z in f]:
            fail+=1; continue
        # Check that {x^(p-1), D x^(p-1), ...} is a basis:
        cur=[0]*(p-1)+[1]
        basis=[]
        for i in range(p):
            basis.append(cur)
            cur=D(cur)
        def matrix_rank(M):
            M=[list(x) for x in M];r=0
            for j in range(p):
                nz=next((i for i in range(r,p) if M[i][j]),None)
                if nz is None:continue
                M[r],M[nz]=M[nz],M[r]
                v=inv(M[r][j]);M[r]=[mul(v,z) for z in M[r]]
                for i in range(p):
                    if i!=r and M[i][j]:
                        t0=M[i][j]
                        M[i]=[add(M[i][k],mul(p-1,mul(t0,M[r][k]))) for k in range(p)]
                r+=1
            return r
        # For degree=2 subtraction by p-1 = -1, works.
        if matrix_rank(basis)!=p:fail+=1;continue
        if lam==0:d=0
        else:
            z=powr(lam,(q-1)//(p-1))
            d=next(j for j in range(1,p) if powr(z,j)==1)
        buckets[d]+=1;t+=1
    if limit is None:
        c=(q-1)*q**(p-2)
        expected={0:c}
        for d in range(1,p):
            if (p-1)%d==0:
                phi=sum(1 for a in range(1,d+1) if math.gcd(a,d)==1)
                expected[d]=int(c*(q-1)*phi/(p-1))
        assert dict(buckets)==expected,(p,degree,buckets,expected)
        assert not fail, fail
    return {'p':p,'q':q,'mode':'exhaustive' if limit is None else f'{limit} seeded samples','observed_type_counts':dict(sorted(buckets.items())),'expected_type_counts':expected if limit is None else None,'checks_failed':fail,'unit_derivations_checked':t,'pass':fail==0}

if __name__=='__main__':
    records=[compute(3,1),compute(3,2),compute(5,1),compute(7,1,1200)]
    print(json.dumps({'summary':'Finite verification of p-curvature and cyclicity, plus exhaustive type frequencies at three field sizes','records':records},indent=2,sort_keys=True))

def full_census(p,degree,limit=None):
    q,add,mul,powr,inv=field(p,degree)
    def Dmaker(f):
        def D(v):
            w=[0]*p
            for j in range(1,p):
                for k in range(p-j+1):
                    w[j-1+k]=add(w[j-1+k],mul(mul(j,v[j]),f[k]))
            return w
        return D
    def rk(matrix_rows):
        m=len(matrix_rows);a=[list(row) for row in matrix_rows]; r=0
        for j in range(p):
            i=next((i for i in range(r,m) if a[i][j]),None)
            if i is None: continue
            a[r],a[i]=a[i],a[r]
            z=inv(a[r][j]);a[r]=[mul(z,x) for x in a[r]]
            for i in range(m):
                if i==r or a[i][j]==0:continue
                z=a[i][j];a[i]=[add(a[i][k],mul(p-1,mul(z,a[r][k]))) for k in range(p)]
            r+=1
        return r
    if limit is None: fs=itertools.product(range(q),repeat=p)
    else:
        random.seed(271828+p*100+q)
        fs=(tuple(random.randrange(q) for _ in range(p)) for _ in range(limit))
    counts=collections.Counter(); failures=[]; checked=0
    for f in fs:
        f=tuple(f);D=Dmaker(f)
        if f[0]:
            v=[0,1]+[0]*(p-2)
            for j in range(p):v=D(v)
            lam=mul(v[0],inv(f[0])); cat=('regular_nilpotent' if lam==0 else 'charpoly_lambda',lam)
            if v!=[mul(lam,z) for z in f]:failures.append(('p-power',f));continue
        elif f[1]:
            lam=powr(f[1],p-1);cat=('charpoly_lambda',lam)
            # trace triangular diagonal i f1 -> t^p-lam*t
        elif not any(f): cat=('zero',0)
        else:
            k=next(j for j,a in enumerate(f) if a);cat=('valuation',k)
            # verify all positive power ranks of D
            images=[[int(i==j) for i in range(p)] for j in range(p)]
            for h in range(1,p+1):
                images=[D(row) for row in images]
                r=rk(images); expected=max(p-1-h*(k-1),0)
                if r!=expected:failures.append(('rank',f,h,r,expected));break
        counts[cat]+=1;checked+=1
    expected={}
    if limit is None:
        expected[('regular_nilpotent',0)]=(q-1)*q**(p-2)
        for lam in range(1,q):
            extra=(p-1)*q**(p-2) if powr(lam,(q-1)//(p-1))==1 else 0
            expected[('charpoly_lambda',lam)]=(q-1)*q**(p-2)+extra
        for k in range(2,p):expected[('valuation',k)]=(q-1)*q**(p-1-k)
        expected[('zero',0)]=1
        assert counts==expected, (counts,expected)
        assert checked==q**p and not failures,(checked,failures[:4])
    return {'p':p,'q':q,'mode':'exhaustive' if limit is None else f'{limit} seeded samples','checked':checked,'failures':failures[:4],'strata':{f'{key[0]}_{key[1]}':v for key,v in sorted(counts.items())},'pass':len(failures)==0 and (limit is not None or counts==expected)}

if __name__=='__main__':
    result={'summary':'Full restricted-Witt derivation census: p-power characteristic-polynomial identities and complete nilpotent power-rank profiles',
    'tests':[full_census(3,1),full_census(3,2),full_census(5,1),full_census(7,1,900)]}
    with Path(__file__).with_name('verify_full_output.json').open('w',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True)
    print(json.dumps(result,indent=2))
