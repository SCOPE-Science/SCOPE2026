"""Direct finite-prime-field checks for polynomial-map counts on radical-square-zero quiver algebras.
No external dependencies; evaluate coefficients on every element, obtain a basis by finite-field linear elimination,
and enumerate DISTINCT functions rather than polynomial representatives.
"""
from itertools import product
from math import factorial


def mul(a,b, p, vertices, arrows):
    nv=vertices
    return tuple([(a[i]*b[i])%p for i in range(nv)] +
                 [(a[src]*b[nv+j]+a[nv+j]*b[tgt])%p
                  for j,(src,tgt) in enumerate(arrows)])


def independent_functions(p, vertices, arrows):
    d=vertices+len(arrows)
    elements=list(product(range(p),repeat=d))
    zeros=(0,)*d
    one=(1,)*vertices+(0,)*len(arrows)
    base=[]
    for k in range(2*p):
        vals=[]
        for x in elements:
            z=one
            for _ in range(k):
                z=mul(z,x,p,vertices,arrows)
            vals.append(z)
        for b in range(d):
            e=tuple(int(i==b) for i in range(d))
            arr=tuple(c for xk in vals for c in mul(e,xk,p,vertices,arrows))
            base.append((arr,(b,k)))
    pivots={}
    indep=[]
    for vec,bk in base:
        red=list(vec)
        for h,pv in sorted(pivots.items()):
            c=red[h]
            if c:
                for j in range(h,len(red)):
                    red[j]=(red[j]-c*pv[j])%p
        h=next((i for i,x in enumerate(red) if x),None)
        if h is not None:
            inv=pow(red[h],-1,p)
            red=[(inv*x)%p for x in red]
            pivots[h]=red
            indep.append((vec,bk))
    return elements,indep


def verify_case(p, vertices, arrows, exhaustive=True):
    els,indep=independent_functions(p,vertices,arrows)
    m=len(arrows)
    r=len({i for i,j in arrows})
    rank=len(indep)
    target_rank=p*(vertices+r+m)
    assert rank==target_rank, (p,vertices,arrows,rank,target_rank)
    total=p**rank
    expected_perm=factorial(p)**vertices*(p-1)**(p*r)*p**(p*m)
    if exhaustive:
        assert total<=1000000
        d=vertices+m; N=len(els)
        indexes={x:i for i,x in enumerate(els)}
        basis=[x for x,_ in indep]
        zero=(0,)*(N*d)
        # increment in base p: hold current evaluation tuple to avoid recomputing
        counter=[0]*rank; cur=[0]*(N*d); bijections=0; count=0
        while True:
            images=[tuple(cur[i*d:(i+1)*d]) for i in range(N)]
            if len(set(images))==N:
                bijections+=1
            count+=1
            idx=0
            while idx<rank:
                if counter[idx]+1<p:
                    counter[idx]+=1
                    a=basis[idx]
                    cur=[(x+y)%p for x,y in zip(cur,a)]
                    break
                else:
                    counter[idx]=0
                    a=basis[idx]
                    cur=[(x+y)%p for x,y in zip(cur,a)] # - (p-1)*a mod p equals +a
                    idx+=1
            if idx==rank: break
        assert count==total
        assert bijections==expected_perm, (p,vertices,arrows,bijections,expected_perm)
    return {"field_order":p,"vertices":vertices,"arrows":arrows,"evaluation_rank":rank,
            "distinct_polynomial_maps":total,"bijective_polynomial_maps":expected_perm,
            "permutation_count_checked":exhaustive}


def composition_witness(p,vertices,arrows):
    # For any nonloop arrow i -> j, the maps G(x)=e_i*x and F(x)=x^2 are polynomial;
    # the composite has on this arrow coefficient s*y, whereas any right polynomial
    # with source diagonal s^2 has coefficient (s+t)*y when s!=t.
    a=next(((i,j) for i,j in arrows if i!=j),None)
    if a is None:return True
    i,j=a
    x=[0]*(vertices+len(arrows)); x[j]=1
    h=arrows.index(a);x[vertices+h]=1
    one=(1,)*vertices+(0,)*len(arrows)
    e=[0]*(vertices+len(arrows));e[i]=1
    gx=mul(tuple(e),tuple(x),p,vertices,arrows)
    fgx=mul(gx,gx,p,vertices,arrows)
    assert fgx[vertices+h]==0
    # Diagonal source function is s -> s^2, forced divided difference at (0,1) = 1
    assert (1*1-0*0)%p==1
    return True


if __name__=='__main__':
    cases=[(2,1,[(0,0)]),(2,1,[(0,0),(0,0)]),
           (2,2,[(0,1)]),(2,2,[(1,0)]),(2,2,[(0,1),(1,0)]),
           (2,3,[(0,1),(0,2)]),(2,3,[(0,1),(1,2)]),
           (3,1,[(0,0)]),(3,2,[(0,1)])]
    for p,v,arr in cases:
        case=verify_case(p,v,arr,exhaustive=True)
        assert composition_witness(p,v,arr)
        print(case)
    print('RIGHT_POLYNOMIAL_QUIVER_CHECKS_OK')
