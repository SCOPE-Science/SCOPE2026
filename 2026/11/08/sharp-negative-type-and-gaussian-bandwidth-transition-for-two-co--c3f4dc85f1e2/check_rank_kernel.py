"""Independent finite checks for rank-distance power kernels on two-column matrix spaces.
Only standard-library Python is needed.
"""
import itertools, cmath, math

def rank2(M, q):
    a,b=M[::2],M[1::2]
    if all(x == 0 for x in M): return 0
    if all((a[i]*b[j]-a[j]*b[i])%q==0 for i in range(len(a)) for j in range(len(a))): return 1
    return 2

def test(q,m):
    N=q**(2*m)
    mats=list(itertools.product(range(q),repeat=2*m))
    rows=[rank2(A,q) for A in mats]
    C1=(q**m-1)*(q+1)
    C2=(q**m-1)*(q**m-q)
    assert rows.count(0)==1 and rows.count(1)==C1 and rows.count(2)==C2
    # Build exact frequency-residue histograms, then Fourier sum, over all dual ranks.
    checks=0
    for A,r in zip(mats,rows):
        hist=[[0]*q for _ in range(3)]
        for X,s in zip(mats,rows):
            trace=sum(x*y for x,y in zip(A,X))%q
            hist[s][trace]+=1
        vals=[]
        for s in (1,2):
            v=sum(hist[s][h]*cmath.exp(2j*math.pi*h/q) for h in range(q))
            assert abs(v.imag)<1e-8
            vals.append(int(round(v.real)))
        predicted1=(q*q*(q**(m-r)-1)-(q**m-1))//(q-1)
        predicted2=(-1-predicted1) if r else C2
        assert (vals[0],vals[1])==(predicted1,predicted2), (q,m,r,vals,predicted1,predicted2)
        checks+=1
    for alpha in (0.25, math.log2(1+1/q),1.0,2.0):
        a=2**alpha
        for z in (0.1,0.3,1/q,0.7,0.95):
            c0=1+C1*z+C2*z**a
            c1=1+(q**m-q-1)*z+(q-q**m)*z**a
            c2=1-(q+1)*z+q*z**a
            assert c0>0 and c1>0
            # Direct Fourier of the radial power kernel for rank-2 sample frequencies.
            for A,r in zip(mats,rows):
                if r==2:
                    s=sum((1 if t==0 else (z if t==1 else z**a))*cmath.exp(2j*math.pi*(sum(x*y for x,y in zip(A,X))%q)/q) for X,t in zip(mats,rows))
                    assert abs(s-c2)<1e-7,(q,m,alpha,z,s,c2)
                    break
    print('EXACT_PRIME_FOURIER_OK',q,m,'frequency_tests',checks,'rank1_count',C1,'rank2_count',C2)

for q,m in ((2,2),(3,2),(2,3)):
    test(q,m)

# Purely analytic phase-diagram equation independent of m. At alpha=1, z*=1/q.
for q in (2,3,4,5,7,9):
    root=1/q
    assert abs(1-(q+1)*root+q*root**2)<1e-12
    a_c=1+1/q
    for z in (0.001,0.2,0.45,0.75,0.99):
        assert 1-(q+1)*z+q*z**a_c>=-1e-11
    print('ANALYTIC_THRESHOLD_OK',q,'alpha_crit',math.log2(a_c),'t_crit_for_alpha1',math.log(q))
# Independent extension-field case: GF(4) = GF(2)[a]/(a^2+a+1).
def f4mul(x,y):
    a=(x&1)*(y&1)
    b=((x&1)*((y>>1)&1)) ^ (((x>>1)&1)*(y&1))
    c=((x>>1)&1)*((y>>1)&1)
    return (a^c)|((b^c)<<1)

def f4rank(M):
    if not any(M): return 0
    r0=M[::2]; r1=M[1::2]
    if all(f4mul(r0[i],r1[j])^f4mul(r0[j],r1[i])==0 for i in range(len(r0)) for j in range(len(r0))): return 1
    return 2

q=4;m=2
mats=list(itertools.product(range(q),repeat=2*m))
ranks=[f4rank(M) for M in mats]
for A,j in zip(mats,ranks):
    counts=[[0,0] for _ in range(3)]
    for X,r in zip(mats,ranks):
        phase=0
        for x,y in zip(A,X): phase^=f4mul(x,y)
        counts[r][(phase>>1)&1]+=1 # GF(4)/GF(2) trace
    R1=counts[1][0]-counts[1][1]
    R2=counts[2][0]-counts[2][1]
    assert R1==(q**m*(q**(2-j)-1)-(q*q-1))//(q-1)
    assert R2==((q**m-1)*(q**m-q) if j==0 else (-1-R1))
# Test the critical projective-line Hamming identity for every difference.
for X,r in zip(mats,ranks):
    nonzero=0
    for v in [(1,t) for t in range(4)]+[(0,1)]:
        image=[f4mul(X[2*i],v[0])^f4mul(X[2*i+1],v[1]) for i in range(m)]
        nonzero+=bool(any(image))
    assert nonzero==(0 if r==0 else (q if r==1 else q+1))
print('EXACT_EXTENSION_FIELD_OK',q,m,'frequencies',len(mats),'projective_identity_checked',len(mats))
print('ALL_TWO_COLUMN_RANK_KERNEL_CHECKS_OK')
