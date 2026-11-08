"""Independent finite-field incidence verification for split-quadric affine-plane X-ray spectra.
Run: python null_regulus_checker.py
"""
import itertools
import math
import numpy as np

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else -a%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:
            return a*b%self.q
        ret=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    k=i+j
                    ret ^= (1<<k) if k<=1 else 3 # x^2=x+1
        return ret


def rulings(F):
    q=F.q
    P=[(1,t) for t in range(q)]+[(0,1)]
    A=[]; B=[]
    for (a,b) in P:
        A.append(frozenset((F.mul(a,z),F.mul(a,w),F.mul(b,z),F.mul(b,w)) for z in range(q) for w in range(q)))
        B.append(frozenset((F.mul(z,a),F.mul(z,b),F.mul(w,a),F.mul(w,b)) for z in range(q) for w in range(q)))
    return A,B

def matrix_for(F,ds):
    q=F.q
    V=list(itertools.product(range(q),repeat=4))
    index={x:i for i,x in enumerate(V)}
    rows=[]
    for D in ds:
        visited=set()
        for x in V:
            if x in visited: continue
            coset={tuple(F.add(x[j],z[j]) for j in range(4)) for z in D}
            visited.update(coset)
            row=np.zeros(q**4,dtype=np.int16)
            for y in coset:row[index[y]]=1
            rows.append(row)
        assert len(visited)==q**4
    return np.vstack(rows) if rows else np.zeros((0,q**4),dtype=np.int16)

def theory(q,A,B):
    a,b=len(A),len(B)
    out={}
    if a+b:out[q*q*(a+b)]=1
    else:out[0]=1
    out[0]=out.get(0,0)+q**4-1-(q-1)*(q+1)**2
    for i in range(q+1):
        for j in range(q+1):
            lam=q*q*(int(i in A)+int(j in B))
            out[lam]=out.get(lam,0)+q-1
    return {x:y for x,y in out.items() if y}

def check(q):
    F=Field(q)
    A,B=rulings(F)
    assert len(A)==len(B)==q+1
    assert all(len(d)==q*q for d in A+B)
    assert len(set.union(*(set(s) for s in A)))==1+(q-1)*(q+1)**2
    for i in range(q+1):
        for j in range(q+1):
            assert len(A[i]&B[j])==q
        for j in range(i+1,q+1):
            assert len(A[i]&A[j])==1 and len(B[i]&B[j])==1
    trials=[(list(range(q+1)),[]), (list(range(q+1)),[0]), (list(range(q+1)),list(range(q+1))), (list(range(q)),list(range(q)))]
    for a,b in trials:
        R=matrix_for(F,[A[i] for i in a]+[B[j] for j in b])
        Gram=(R.T.astype(np.int64)@R.astype(np.int64))
        # Quadratic form is det(a,b;c,d), and every direction is totally null.
        for d in A+B:
            assert all(F.sub(F.mul(x[0],x[3]),F.mul(x[1],x[2]))==0 for x in d)
        evals=np.linalg.eigvalsh(Gram)
        observed={}
        for eig in evals:
            k=int(round(eig))
            assert abs(eig-k)<1e-7, (q,a,b,eig)
            observed[k]=observed.get(k,0)+1
        expected=theory(q,a,b)
        assert observed==expected,(q,a,b,observed,expected)
        if len(a)==q+1 and not b:
            nonzero=sorted(z for z in observed if z)
            assert nonzero==[q*q,q*q*(q+1)]
        print('q',q,'directions',len(a),len(b),'rows',len(R),'spectrum',observed)
def weighted_check(q):
    F=Field(q)
    A,B=rulings(F)
    sides=[(list(range(q+1)),[0]),(list(range(q+1)),list(range(q+1))), (list(range(q)),list(range(q)))]
    for ai,bi in sides:
        a_w={i:i+1 for i in ai}
        b_w={j:2*j+3 for j in bi}
        parts=[]
        weights=[]
        for i in ai:
            parts.append(matrix_for(F,[A[i]]));weights.append(a_w[i])
        for j in bi:
            parts.append(matrix_for(F,[B[j]]));weights.append(b_w[j])
        Gram=np.zeros((q**4,q**4),dtype=np.int64)
        for R,w in zip(parts,weights):Gram+=w*(R.T.astype(np.int64)@R.astype(np.int64))
        observed={}
        for eig in np.linalg.eigvalsh(Gram):
            z=int(round(eig)); assert abs(eig-z)<1e-7
            observed[z]=observed.get(z,0)+1
        expected={q*q*(sum(a_w.values())+sum(b_w.values())):1}
        base=(q*q-1)*(q*q-q)
        expected[0]=base
        for i in range(q+1):
            for j in range(q+1):
                lam=q*q*(a_w.get(i,0)+b_w.get(j,0))
                expected[lam]=expected.get(lam,0)+q-1
        expected={k:v for k,v in expected.items() if v}
        assert observed==expected,(q,ai,bi,observed,expected)
        print('weighted q',q,'directions',len(ai),len(bi),'eigenvalues',sorted(observed))
for q in (2,3,4):
    check(q)
    weighted_check(q)
print('NULL_REGULUS_INCIDENCE_SPECTRUM_CHECKS_PASS')
