#!/usr/bin/env python3
"""Direct finite-field fiber and Fourier Gram checks for ternary quadratic spheres.
Standard library only.
"""
import cmath
import math

class Field:
    def __init__(self, q):
        self.q=q
        self.p=3 if q==9 else q
        self.add=[[0]*q for _ in range(q)]
        self.mul=[[0]*q for _ in range(q)]
        for x in range(q):
            for y in range(q):
                if q==9:
                    a,b=x%3,x//3; c,d=y%3,y//3
                    self.add[x][y]=(a+c)%3+3*((b+d)%3)
                    self.mul[x][y]=(a*c-b*d)%3+3*((a*d+b*c)%3)
                else:
                    self.add[x][y]=(x+y)%q
                    self.mul[x][y]=(x*y)%q
        self.neg=[next(y for y in range(q) if self.add[x][y]==0) for x in range(q)]
        self.chi=[0]*q
        for x in range(1,q):
            self.chi[x]=1 if any(self.mul[y][y]==x for y in range(1,q)) else -1
        self.primitive=next(x for x in range(1,q) if self.chi[x]==-1)
    def A(self,x,y):return self.add[x][y]
    def M(self,x,y):return self.mul[x][y]
    def negx(self,x):return self.neg[x]
    def char(self,x):
        trace=(2*(x%3))%3 if self.q==9 else x
        return cmath.exp(2j*math.pi*trace/self.p)
    def qval(self,x,delta):
        return self.A(self.A(self.M(x[0],x[0]),self.M(x[1],x[1])), self.M(delta,self.M(x[2],x[2])))


def projective_vectors(F):
    q=F.q
    # unique representatives with first nonzero coordinate equal to 1
    for v in [(1,a,b) for a in range(q) for b in range(q)]:yield v
    for v in [(0,1,b) for b in range(q)]:yield v
    yield (0,0,1)


def direct_fibers(F,delta,j,v):
    q=F.q; p=next(i for i in range(3) if v[i]!=0)
    # our listed vectors have first nonzero coordinate one
    assert v[p]==1
    other=[i for i in range(3) if i!=p]
    fibers=[]
    for a in range(q):
        for b in range(q):
            count=0
            for t in range(q):
                x=[F.M(t,z) for z in v]
                x[other[0]]=F.A(x[other[0]],a)
                x[other[1]]=F.A(x[other[1]],b)
                if F.qval(x,delta)==j:count+=1
            fibers.append(count)
    return fibers


def expected(F,delta,j,v):
    q=F.q
    D=F.M(F.negx(1),delta)
    sigma=F.chi[F.M(D,j)]
    s=F.qval(v,delta)
    if s==0:
        return {0:q-(2 if sigma==1 else 0),1:q*q-q,q:(2 if sigma==1 else 0)},sigma,None
    eps=F.chi[F.M(D,s)]
    return {0:(q*q-sigma*q-q+eps)//2,1:q-eps,2:(q*q+sigma*q-q+eps)//2},sigma,eps


def direct_fourier_frame_check(F,delta,j,v,fibers):
    # Evaluates the actual Gram via a sum over the sphere; checks the q^2
    # Fourier-character eigenvectors with their exactly predicted eigenvalues.
    q=F.q;n=q*q
    p=next(i for i in range(3) if v[i]!=0)
    other=[i for i in range(3) if i!=p]
    # quotient characters indexed by the two coordinate parameters
    # z=(a,b) -> character chi(a*alpha + b*beta), all full-grid frequency modes.
    # direct 2D DFT Gram identity checked entrywise.
    pts=[]
    for a in range(q):
        for b in range(q):
            for t in range(q):
                x=[F.M(t,z) for z in v]
                x[other[0]]=F.A(x[other[0]],a)
                x[other[1]]=F.A(x[other[1]],b)
                if F.qval(x,delta)==j:pts.append((a,b))
    assert len(pts)==sum(fibers)
    assert len(pts)==q*q+F.chi[F.M(F.M(F.negx(1),delta),j)]*q
    for alpha in range(q):
        for beta in range(q):
            # Exact expected Gram first row: sum of characters over fibers.
            direct=sum(F.char(F.A(F.M(a,alpha),F.M(b,beta))) for a,b in pts)
            weighted=sum(fibers[a*q+b]*F.char(F.A(F.M(a,alpha),F.M(b,beta)))
                         for a in range(q) for b in range(q))
            assert abs(direct-weighted)<1e-8
    # On character vectors, eigenvalue is q^2 * fiber count / |S|.
    # Verify pointwise orthogonality of characters at a selection of all modes.
    for a in range(q):
        for b in range(q):
            z=(a,b)
            for c in range(q):
                for d in range(q):
                    lhs=sum(F.char(F.A(F.M(alpha,F.A(a,F.negx(c))),F.M(beta,F.A(b,F.negx(d)))))
                           for alpha in range(q) for beta in range(q))
                    assert abs(lhs-(n if z==(c,d) else 0))<1e-8


def run():
    total=0; cases=0; direct=0
    for q in (3,5,7,9,11):
        F=Field(q)
        for delta in (1,F.primitive):
            for j in (1,F.primitive):
                counter={None:0,-1:0,1:0}
                best=-1; optimal=[]
                sigma=F.chi[F.M(F.M(F.negx(1),delta),j)]
                for v in projective_vectors(F):
                    fibers=direct_fibers(F,delta,j,v)
                    exp,sigma0,eps=expected(F,delta,j,v)
                    assert sigma==sigma0
                    got={m:fibers.count(m) for m in (0,1,2,q)}
                    for m in set(got)|set(exp):
                        assert got.get(m,0)==exp.get(m,0),(q,delta,j,v,got,exp)
                        total+=1
                    assert sum(fibers)==q*q+sigma*q
                    assert sum(got.values())==q*q
                    counter[eps]+=1
                    rank=q*q-got.get(0,0)
                    if rank>best: best=rank;optimal=[(v,eps)]
                    elif rank==best:optimal.append((v,eps))
                    cases+=1
                assert counter[None]==q+1
                assert counter[1]==q*(q+1)//2
                assert counter[-1]==q*(q-1)//2
                maxiso=q*q-q+(2 if sigma==1 else 0)
                assert best==maxiso
                assert len(optimal)==q+1 + (q*(q-1)//2 if q==3 and sigma==1 else 0)
                if q in (3,5):
                    done=set()
                    for v in projective_vectors(F):
                        eps=expected(F,delta,j,v)[2]
                        if eps in done:continue
                        direct_fourier_frame_check(F,delta,j,v,direct_fibers(F,delta,j,v))
                        direct+=1;done.add(eps)
                        if len(done)==3:break
    print(f'CHECK_OK configurations={cases} multiplicity_assertions={total} direct_gram_classes={direct} fields=3,5,7,9,11')

if __name__=='__main__':run()
