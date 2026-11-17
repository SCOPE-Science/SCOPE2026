#!/usr/bin/env python3
"""Standalone finite-field checks of the Fourier commutator construction.
The general theorem is proved symbolically; these are independent finite checks.
"""
import itertools
import random


def primitive_root(p):
    factors=[a for a in range(2,p) if (p-1)%a==0 and all(a%b for b in range(2,int(a**0.5)+1))]
    for g in range(2,p):
        if all(pow(g,(p-1)//a,p)!=1 for a in factors): return g
    raise AssertionError('generator not found')


def solve_cycle(w,p):
    n=len(w)
    assert n>=3
    if n==3:
        if not any(w): return [(0,0)]*3
        k=next(i for i,v in enumerate(w) if v)
        a,b,c=[w[(k+i)%3] for i in range(3)]
        rr=[(1,0),(0,a),(-b*pow(a,-1,p)%p,-c%p)]
        r=[None]*3
        for i in range(3):r[(k+i)%3]=rr[i]
        return r
    s=solve_cycle([1]+w[2:],p)
    def lin(x,a,y,b):return ((x*a+y*b)%p)
    inserted=(lin(w[1],s[0][0],w[0],s[1][0]),lin(w[1],s[0][1],w[0],s[1][1]))
    out=[s[0],inserted]+s[1:]
    assert all((out[i][0]*out[(i+1)%n][1]-out[i][1]*out[(i+1)%n][0])%p==w[i] for i in range(n))
    return out


def rank(vectors,p):
    piv={}
    for row in vectors:
        r=list(row)
        while True:
            k=next((i for i,x in enumerate(r) if x%p),None)
            if k is None:break
            if k in piv:
                lead=piv[k]
                c=r[k]
                r=[(a-c*b)%p for a,b in zip(r,lead)]
            else:
                scale=pow(r[k],-1,p)
                piv[k]=[(a*scale)%p for a in r]
                break
    return len(piv)


def run(moduli,p,samples,seed):
    n=1
    for m in moduli:n*=m
    assert (p-1)%max(moduli)==0
    g=primitive_root(p)
    roots=[pow(g,(p-1)//m,p) for m in moduli]
    points=list(itertools.product(*(range(m) for m in moduli)))
    assert len(points)==n
    idx={a:i for i,a in enumerate(points)}
    def op(a,b):return tuple((2*y-x)%m for x,y,m in zip(a,b,moduli))
    def flip(a):return tuple((-a_i)%m for a_i,m in zip(a,moduli))
    def t(a):return tuple((-2*a_i)%m for a_i,m in zip(a,moduli))
    def F(a,x):
        y=1
        for j,xi,zeta,m in zip(a,x,roots,moduli):y=y*pow(zeta,(j*xi)%m,p)%p
        return y
    fourier=[[F(a,x) for x in points] for a in points]
    inv=[[F(flip(a),x) for a in points] for x in points]
    rinv=pow(n,-1,p)
    allowed={a for a in points if t(a)!=a}
    assert len(allowed)==n-sum(all((3*x)%m==0 for x,m in zip(a,moduli)) for a in points)
    # Compare the span of all elementary commutators with the spectral formula.
    brackets=[]
    for a in points:
        for b in points:
            out=[0]*n
            out[idx[op(a,b)]]=(out[idx[op(a,b)]]+1)%p
            out[idx[op(b,a)]]=(out[idx[op(b,a)]]-1)%p
            brackets.append(out)
    assert rank(brackets,p)==len(allowed),('rank mismatch',moduli,p)
    # Direct Fourier product identity, including zero and nonzero products.
    for ia,a in enumerate(points):
        for ib,b in enumerate(points):
            uv=[0]*n
            for ix,x in enumerate(points):
                for iy,y in enumerate(points):
                    uv[idx[op(x,y)]]=(uv[idx[op(x,y)]]+fourier[ia][ix]*fourier[ib][iy])%p
            expect=[n*F(flip(a),x)%p if b==t(a) else 0 for x in points]
            assert uv==expect,('Fourier multiplication',moduli,p,a,b)
    rng=random.Random(seed)
    tested=0
    for sample in range(samples):
        c={a:(rng.randrange(p) if sample%4 else (1 if (idx[a]+sample)%3==0 else 0)) for a in allowed}
        u={a:0 for a in points}; v={a:0 for a in points}; visited=set()
        for a in points:
            if a in visited:continue
            cyc=[]; cur=a
            while cur not in visited:
                visited.add(cur);cyc.append(cur);cur=t(cur)
            if len(cyc)==1:continue
            assert len(cyc)>=3
            w=[c[flip(b)]*rinv%p for b in cyc]
            rr=solve_cycle(w,p)
            for b,row in zip(cyc,rr):u[b],v[b]=row
        ux=[sum(u[a]*fourier[ia][ix] for ia,a in enumerate(points))%p for ix in range(n)]
        vx=[sum(v[a]*fourier[ia][ix] for ia,a in enumerate(points))%p for ix in range(n)]
        actual=[0]*n
        for ix,x in enumerate(points):
            for iy,y in enumerate(points):
                z=(ux[ix]*vx[iy]-vx[ix]*ux[iy])%p
                actual[idx[op(x,y)]]=(actual[idx[op(x,y)]]+z)%p
        target=[sum(c[a]*fourier[ia][ix] for ia,a in enumerate(points) if a in allowed)%p for ix in range(n)]
        
        if actual!=target:
            print('MISMATCH',moduli,p,sample,'c',c,'u',u,'v',v,'ux',ux,'vx',vx,'actual',actual,'target',target)
            raise AssertionError(('witness mismatch',moduli,p,sample))
        tested+=1
    return {'A':moduli,'p':p,'size':n,'derived_dim':len(allowed),'witnesses':tested}


def main():
    for q in (2,3,5,7):
        for length in range(3,9 if q==2 else 6 if q==3 else 5):
            if q**(2*length)>300000:continue
            seen=set()
            for digits in itertools.product(range(q*q),repeat=length):
                rows=[(d//q,d%q) for d in digits]
                seen.add(tuple((rows[i][0]*rows[(i+1)%length][1]-rows[i][1]*rows[(i+1)%length][0])%q for i in range(length)))
            assert len(seen)==q**length,(q,length,len(seen))
            for vals in itertools.product(range(q),repeat=length):
                rr=solve_cycle(list(vals),q)
                assert tuple((rr[i][0]*rr[(i+1)%length][1]-rr[i][1]*rr[(i+1)%length][0])%q for i in range(length))==vals
    results=[]
    cases=[((1,),7,3),((3,),7,5),((3,3),7,4),((5,),11,18),((7,),29,14),((9,),19,14),((3,5),31,12),((5,5),11,5),((3,9),19,5)]
    for i,(A,p,samples) in enumerate(cases):
        results.append(run(A,p,samples,seed=17+i))
        print('CASE_OK',results[-1])
    print('VERIFY_OK cases='+str(len(results))+' witnesses='+str(sum(x['witnesses'] for x in results))+' cyclic_minor_exhaustive=passed Fourier_product=passed rank=passed')

if __name__=='__main__':main()
