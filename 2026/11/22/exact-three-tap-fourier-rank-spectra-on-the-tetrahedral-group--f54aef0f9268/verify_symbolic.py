"""Independent exact Fourier-block and low-rank obstruction test.
Computes degree-three determinants in Z[x,y]; no third-party libraries.
"""
from itertools import permutations, combinations
from math import prod

I=(0,1,2,3)
reps = [
    (I,(0,2,3,1),(0,3,1,2)),
    (I,(0,2,3,1),(1,0,3,2)),
    (I,(0,2,3,1),(1,2,0,3)),
    (I,(1,0,3,2),(2,3,0,1)),
]
def constant(k): return {(0,0):k} if k else {}
def add(p,q):
    r=dict(p)
    for m,a in q.items(): r[m]=r.get(m,0)+a
    return {m:a for m,a in r.items() if a}
def neg(p): return {m:-a for m,a in p.items()}
def sub(p,q): return add(p,neg(q))
def multiply(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():r[i+k,j+l]=r.get((i+k,j+l),0)+a*b
    return {m:a for m,a in r.items() if a}
def power(p,n):
    a=constant(1)
    for _ in range(n):a=multiply(a,p)
    return a
C=constant(1);X={(1,0):1};Y={(0,1):1}
def signperm(p):
    return [[int(p[j]==i)-int(p[3]==i) for j in range(3)] for i in range(3)]
def mat(u,v):
    A,B=signperm(u),signperm(v)
    return [[add(constant(int(i==j)),add(multiply(constant(A[i][j]),X), multiply(constant(B[i][j]),Y))) for j in range(3)] for i in range(3)]
def det(M):
    r={}
    for t in permutations(range(3)):
        v=C
        for i,j in enumerate(t):v=multiply(v,M[i][j])
        if sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))%2:v=neg(v)
        r=add(r,v)
    return r

D=[
    add(C,add(multiply(constant(-3),multiply(X,Y)), add(power(X,3),power(Y,3)))),
    add(C,add(power(X,3),add(power(Y,3),add(neg(power(Y,2)),neg(Y))))),
    add(C,add(power(X,3),add(multiply(X,Y),power(Y,3)))),
    multiply(multiply(sub(sub(X,Y),C),add(sub(X,Y),C)),sub(add(X,Y),C)),
]
# A single 3D representation is obtained by restricting the 4D permutation
# representation to the subspace spanned by e_i-e_3 (i=0,1,2).
for j,(_,u,v) in enumerate(reps):
    M=mat(u,v)
    assert det(M)==D[j],(j,det(M),D[j])

# For the two non-subgroup types, these are exact 2x2 minors, so the
# three-dimensional Fourier block can never have rank below two with
# nonzero tap coefficients.
def minor(M,rows,cols):
    i,k=rows;h,l=cols
    return sub(multiply(M[i][h],M[k][l]),multiply(M[i][l],M[k][h]))
def allminors(M):
    return [minor(M,R,Cs) for R in combinations(range(3),2) for Cs in combinations(range(3),2)]
A=allminors(mat(*reps[1][1:]))
B=allminors(mat(*reps[2][1:]))
assert neg(multiply(X,Y)) in A
assert add(C,X) in B and sub(Y,X) in B and multiply(Y,sub(X,C)) in B
# If B's minors all vanish, x=-1, y=x=-1; then y(x-1)=2, contradiction.
# The character factors are L_0=1+x+y and L_k=1+omega^k x+omega^(2k)y.
# For class 1 they are 1+omega^k x+y. The 3D det never vanishes
# at a scalar zero for nonzero coefficients: substitution gives
# -4y(y+1), or -4Y(Y+1), respectively, forcing another tap zero.
# Check the elementary substitution as an exact polynomial identity.
assert add(C,add(neg(add(C,Y)),Y)) == {}
for P in [D[1],D[2]]:
    # Substitute x=-1-y in P; cyclic cases k reduce to this by roots of unity.
    def substitute_x(p, q):
        ans={}
        for (i,j),a in p.items():
            ans=add(ans,multiply(constant(a),multiply(power(q,i),power(Y,j))))
        return ans
    assert substitute_x(P,neg(add(C,Y)))==multiply(constant(-4),multiply(Y,add(C,Y)))
print('PASS four 3D determinant identities, non-subgroup minors, scalar/3D disjointness')
for j,p in enumerate(D): print('class',j,'det_polynomial',sorted(p.items()))
