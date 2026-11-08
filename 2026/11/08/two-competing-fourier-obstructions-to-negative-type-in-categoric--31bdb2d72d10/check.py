"""Independent finite graph-distance and Fourier checks for categorical Hamming covers."""
import itertools, collections, cmath, math

def check(q,d,p):
    sizes=(2,)+(q,)*d
    verts=list(itertools.product(*(range(s) for s in sizes)))
    zero=tuple(0 for _ in sizes)
    step=[x for x in verts if x[0]==1 and all(x[j]!=0 for j in range(1,len(sizes)))]
    todo=collections.deque([zero]);dist={zero:0}
    while todo:
        v=todo.popleft()
        for z in step:
            w=tuple((v[j]+z[j])%sizes[j] for j in range(len(sizes)))
            if w not in dist:dist[w]=dist[v]+1;todo.append(w)
    assert len(dist)==len(verts)
    N=q**d;Q=(q-1)**d
    for x in verts:
        b=x[0];different=all(z!=0 for z in x[1:])
        expected=0 if x==zero else (2 if b==0 else (1 if different else 3))
        assert dist[x]==expected,(q,d,x,dist[x],expected)
    a=2**p;c=3**p
    got=[];expected=[]
    for k in verts:
        val=sum(dist[x]**p*cmath.exp(-2j*math.pi*sum(k[j]*x[j]/sizes[j] for j in range(len(sizes)))) for x in verts if dist[x])
        assert abs(val.imag)<1e-8,(q,d,p,k,val)
        eps=(-1)**k[0];j=sum(ki!=0 for ki in k[1:])
        if j==0:formula=(N-1)*a+eps*(Q+(N-Q)*c)
        else: formula=-a+eps*(1-c)*((-1)**j)*(q-1)**(d-j)
        assert abs(val.real-formula)<2e-8,(q,d,p,k,val,formula)
        got.append(val.real);expected.append(formula)
    return min(got[1:]) if False else len(verts)
if __name__=='__main__':
    cases=0
    for q,d in [(3,1),(4,1),(5,1),(3,2),(4,2),(5,2),(3,3)]:
        for p in [0.1,0.4,0.8,1.0]:
            n=check(q,d,p);cases+=1
    print('CATEGORICAL_FOURIER_DISTANCE_PASS',cases,'parameter-exponent cases')


def root(f,lo,hi):
    flo=f(lo)
    assert flo<=0 and f(hi)>=0
    for _ in range(65):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def critical_test(q,d):
    N=q**d;Q=(q-1)**d;M=(q-1)**(d-1)
    p1=root(lambda p:M*(3**p-1)-2**p,0.,1.)
    F=lambda p:(N-1)*2**p-Q-(N-Q)*3**p
    # For these checked cases, F has no earlier first root if F(p1) <=0.
    beta=root(F,0.,p1) if F(p1)>1e-8 else p1
    sizes=(2,)+(q,)*d
    verts=list(itertools.product(*(range(z) for z in sizes)))
    def minmode(p):
        vals=[]
        for v in verts:
            eps=(-1)**v[0];j=sum(ki!=0 for ki in v[1:]);P=((-1)**j)*(q-1)**(d-j)
            vals.append((N-1)*2**p+eps*(Q+(N-Q)*3**p) if j==0 else -2**p+eps*(1-3**p)*P)
        return vals
    before=min(minmode(beta*.9)[1:])
    # Remove the constant character explicitly, avoiding any assumption about ordering of remaining elements.
    order=[v for v in verts if v!=(0,)*len(sizes)]
    vals=[]
    for v in order:
        eps=(-1)**v[0];j=sum(ki!=0 for ki in v[1:]);P=((-1)**j)*(q-1)**(d-j)
        vals.append((N-1)*2**beta+eps*(Q+(N-Q)*3**beta) if j==0 else -2**beta+eps*(1-3**beta)*P)
    zero_count=sum(abs(v)<1e-8 for v in vals)
    assert max(vals)<1e-8
    expected_zero=1 if beta<p1-1e-8 else d*(q-1)
    assert zero_count==expected_zero,(q,d,beta,p1,zero_count,expected_zero)
    assert max(minmode(beta*1.05)[1:]) > 1e-6 if beta>.01 else max(minmode(beta*1.05)[1:]) > 1e-12
    return beta,expected_zero

if __name__=='__main__':
    for q,d in [(3,2),(4,2),(5,2),(4,3),(5,3)]:
        print('CRITICAL',q,d,critical_test(q,d))
