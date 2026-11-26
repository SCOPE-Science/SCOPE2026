"""Exact finite-field consistency tests for a Hermitian-relative curve's projective stabilizer.
Pure Python. Commands: python3 verify.py. Checks s=3,5,7 (prime cases only).
Proof of the uniform result is mathematical, not finite enumeration.
"""

def field(p):
    d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    N=p*p
    add=[[0]*N for _ in range(N)]
    mul=[[0]*N for _ in range(N)]
    for a in range(N):
        a0,a1=a%p,a//p
        for b in range(N):
            b0,b1=b%p,b//p
            add[a][b]=((a0+b0)%p)+p*((a1+b1)%p)
            mul[a][b]=((a0*b0+d*a1*b1)%p)+p*((a0*b1+a1*b0)%p)
    neg=[(-a%p)+p*((-a//p)%p) for a in range(N)]  # overwritten using direct pairs
    neg=[(-(a%p))%p+p*((-(a//p))%p) for a in range(N)]
    def pw(a,k):
        z=1
        while k:
            if k&1:z=mul[z][a]
            a=mul[a][a]; k>>=1
        return z
    conj=[pw(a,p) for a in range(N)]
    return N,add,mul,neg,conj,pw

def solve(p,exhaustive=False):
    N,add,mul,neg,conj,pw=field(p)
    A=[[1,0,0],[0,p,1],[0,1,0]]  # eta = u, not in F_p; integer code 'p'
    def mm(X,Y):
        return [[sum_field(mul[X[i][k]][Y[k][j]] for k in range(3)) for j in range(3)] for i in range(3)]
    def sum_field(vals):
        r=0
        for v in vals:r=add[r][v]
        return r
    def star(T):return [[conj[T[j][i]] for j in range(3)] for i in range(3)]
    def check(T):return mm(mm(star(T),A),T)==A
    def gen():
        for u in range(1,N):
            if mul[u][conj[u]]!=1:continue
            for v in range(N):
                norm=mul[v][conj[v]]
                for h in range(N):
                    if add[h][conj[h]]!=neg[norm]:continue
                    T=[[u,v,0],[0,1,0],[neg[mul[u][conj[v]]],h,1]]
                    if not check(T):raise AssertionError(('not invariant',p,T))
                    yield T
    group=list(gen())
    assert len(group)==p**3*(p+1),(p,len(group))
    assert len(set(tuple(sum(t,[])) for t in group))==len(group)
    print('field F_%d: %d distinct normalized automorphisms satisfy T* A T=A'%(N,len(group)))
    # Check all F_(p^2)-projective points if reasonable: equation  X^(p+1)+eta Y^(p+1)+Y^p Z+ Y Z^p=0.
    points=[]
    for x in range(N):
        for y in range(N):
            if sum_field([pw(x,p+1),mul[p][pw(y,p+1)],conj[y],mul[y][1]])==0:points.append((x,y,1))
    for x in range(N):
        if sum_field([pw(x,p+1),mul[p][1]])==0:points.append((x,1,0))
    if 1==0:points.append((1,0,0))
    assert points==[(0,0,1)],(p,points)
    print('field F_%d: unique rational point [0:0:1] verified'%N)
    if exhaustive:
        # All PGL_3(K) matrices fixing the unique rational point admit unique normalization
        # [[a,b,0],[c,d,0],[e,f,1]]. These matrices preserve the polynomial up to scalar
        # lambda, equal to (1,1) coefficient from sesquilinear congruence.
        candidates=0; stabilizers=[]
        for a in range(N):
          for b in range(N):
            for c in range(N):
              for d in range(N):
                if mul[a][d]==mul[b][c]:continue
                for e in range(N):
                  for f in range(N):
                    T=[[a,b,0],[c,d,0],[e,f,1]]
                    B=mm(mm(star(T),A),T)
                    if B[0][0]==0:continue
                    lam=B[1][2]  # since A[1][2]=1, lambda fixed
                    if lam==0:continue
                    if all(B[i][j]==mul[lam][A[i][j]] for i in range(3) for j in range(3)):
                        stabilizers.append(T)
        assert len(stabilizers)==len(group),(len(stabilizers),len(group))
        assert {tuple(sum(t,[])) for t in stabilizers}=={tuple(sum(t,[])) for t in group}
        print('field F_%d: exhaustive PGL_3 stabilizer enumeration = %d'% (N,len(stabilizers)))

for p in (3,5,7):solve(p,exhaustive=(p==3))
print('VERIFY_OK')
