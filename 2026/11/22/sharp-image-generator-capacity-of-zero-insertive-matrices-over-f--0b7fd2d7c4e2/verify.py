"""Finite checks of zero-product sandwich image-generator capacity."""
import itertools, random, math
from collections import Counter

def mul(x,y,k):
    mask=(1<<k)-1
    z=0
    while y:
        if y&1: z^=x
        x=(x<<1)&mask
        y >>=1
    return z&mask

def mm(A,B,n,k):
    return tuple(
        functools_xor(mul(A[i*n+h],B[h*n+j],k) for h in range(n))
        for i in range(n) for j in range(n))

def functools_xor(xs):
    z=0
    for x in xs:z^=x
    return z

def mu_image(X,n,k):
    """F2-linear dimensions of image and t-image; independent of Smith reduction."""
    cols=[]
    for j in range(n):
        v=0
        for i in range(n):v|=X[i*n+j]<<(i*k)
        cols.append(v)
    def dim(gens):
        piv={}
        for x in gens:
            while x:
                b=x.bit_length()-1
                if b in piv:x^=piv[b]
                else:piv[b]=x;break
        return len(piv)
    def shift(v):
        return sum(((((v>>(i*k))&((1<<k)-1))<<1)&((1<<k)-1))<<(i*k) for i in range(n))
    e=[];f=[]
    for v in cols:
        for _ in range(k):
            e.append(v);v=shift(v)
            if v:f.append(v)
    return dim(e)-dim(f)

def diag(vals):
    n=len(vals)
    return tuple(vals[i] if i==j else 0 for i in range(n) for j in range(n))

def upper(lab,n,k):
    a=diag([1<<u if u<k else 0 for u in lab]);b=diag([1<<(k-u) if k-u<k else 0 for u in lab])
    return a,b

def max_matching(lab):
    n=len(lab)
    adj=[[j for j in range(n) if lab[i]<lab[j]] for i in range(n)]
    match=[-1]*n
    def aug(i,used):
        for j in adj[i]:
            if j in used:continue
            used.add(j)
            if match[j]<0 or aug(match[j],used):match[j]=i;return True
        return False
    return sum(aug(i,set()) for i in range(n))

def random_mat(n,k,rng):
    return tuple(rng.randrange(1<<k) for _ in range(n*n))

def run():
    rng=random.Random(202611150603)
    cases=0
    # Exhaustively test every A-invariant profile and every S,H at n=2,k=2.
    n,k=2,2
    mats=list(itertools.product(range(1<<k),repeat=n*n))
    for lab in itertools.combinations_with_replacement(range(k+1),n):
        a,b=upper(lab,n,k)
        want=n-max(Counter(lab).values())
        assert max_matching(lab)==want
        reached=set()
        Bs=[mm(b,H,n,k) for H in mats]
        for S in mats:
            AS=mm(a,S,n,k)
            for B in Bs:
                X=mm(AS,B,n,k)
                m=mu_image(X,n,k)
                assert m<=want,(n,k,lab,S,B,X,m,want)
                reached.add(m);cases+=1
        assert reached==set(range(want+1)),(lab,reached,want)
    print('EXHAUSTIVE_N2_K2_OK',cases,'sandwich products')
    # All Smith profile patterns; independent combinatorial matching check.
    for n in range(1,8):
        for k in range(1,6):
            profiles=list(itertools.combinations_with_replacement(range(k+1),n))
            for lab in profiles:
                m=n-max(Counter(lab).values())
                assert max_matching(lab)==m,(lab,m)
            best=max(n-max(Counter(z).values()) for z in profiles)
            assert best==n-math.ceil(n/(k+1)),(n,k,best)
    print('ALL_MATCHING_PROFILES_OK',sum(math.comb(n+k,k) for n in range(1,8) for k in range(1,6)))
    # Sample S,H for every length/dimension; test module-generator rank directly.
    samples=0
    for n,k in [(2,3),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3)]:
        for lab in itertools.combinations_with_replacement(range(k+1),n):
            a,b=upper(lab,n,k)
            want=n-max(Counter(lab).values())
            for _ in range(80):
                S=random_mat(n,k,rng);H=random_mat(n,k,rng)
                B=mm(b,H,n,k)
                assert mm(a,B,n,k)==(0,)*(n*n)
                X=mm(mm(a,S,n,k),B,n,k)
                got=mu_image(X,n,k)
                assert got<=want,(n,k,lab,got,want)
                samples+=1
    print('SAMPLED_MODULE_RANK_OK',samples)
    # A sharp witness showing strict field-to-chain-ring growth at n=3,k=2.
    n,k=3,2;lab=(0,1,2)
    A,B=upper(lab,n,k)
    S=(0,1,0, 0,0,1, 0,0,0)
    assert mm(A,B,n,k)==(0,)*9
    X=mm(mm(A,S,n,k),B,n,k)
    assert mu_image(X,n,k)==2
    print('SHARP_WITNESS_N3_K2',X,'IMAGE_GENERATORS',mu_image(X,n,k))
    # Mixed-characteristic corroboration over Z/(2^k), independent of bit-polynomial arithmetic.
    def mm_z(A,B,n,mod):
        return tuple(sum(A[i*n+h]*B[h*n+j] for h in range(n))%mod
                     for i in range(n) for j in range(n))
    def mu_z(X,n,mod):
        image=set()
        for v in itertools.product(range(mod),repeat=n):
            image.add(tuple(sum(X[i*n+j]*v[j] for j in range(n))%mod
                            for i in range(n)))
        twice={tuple((2*x)%mod for x in w) for w in image}
        quotient=len(image)//len(twice)
        assert quotient*len(twice)==len(image)
        assert quotient.bit_count()==1
        return quotient.bit_length()-1
    mixed=0
    for n,k in [(2,2),(2,3),(3,2),(3,3),(4,2)]:
        mod=2**k
        for lab in itertools.combinations_with_replacement(range(k+1),n):
            A=diag([2**u%mod for u in lab])
            D=diag([2**(k-u)%mod for u in lab])
            for _ in range(30):
                S=tuple(rng.randrange(mod) for _ in range(n*n))
                H=tuple(rng.randrange(mod) for _ in range(n*n))
                B=mm_z(D,H,n,mod)
                assert mm_z(A,B,n,mod)==(0,)*(n*n)
                X=mm_z(mm_z(A,S,n,mod),B,n,mod)
                assert mu_z(X,n,mod)<=n-max(Counter(lab).values())
                mixed+=1
    print('MIXED_CHARACTERISTIC_OK',mixed)
    print('VERIFY_OK')

if __name__=='__main__':run()
