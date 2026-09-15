import sys
sys.path.insert(0,'output/artifacts')
from exact2 import F,ZERO,ONE,mat_eye,mat_mul,rref
def flat(M):
    n=len(M); return [M[i][j] for i in range(n) for j in range(n)]
def span_contains(Bvecs,f):
    if not Bvecs: return all(x.is0() for x in f)
    r1=len(rref([list(r) for r in Bvecs])[0])
    r2=len(rref([list(r) for r in Bvecs]+[list(f)])[0])
    return r2==r1
def image_dim(gens, max_rounds=60):
    n=len(gens[0])
    Bvecs=[]
    def add(M):
        f=flat(M)
        if not span_contains(Bvecs,f):
            Bvecs.append(f); return True
        return False
    add(mat_eye(n))
    for g in gens: add(g)
    for _ in range(max_rounds):
        grew=False
        cur=list(Bvecs)
        # materialize basis mats
        # instead: keep mats list
        break
    return None
def image_dim2(gens,max_rounds=60):
    n=len(gens[0])
    mats=[mat_eye(n)]+list(gens)
    # independent list
    indep=[]
    for M in mats:
        f=flat(M)
        if not span_contains([flat(X) for X in indep],f): indep.append(M)
    for _ in range(max_rounds):
        grew=False
        for g in gens:
            for X in list(indep):
                Y=mat_mul(g,X)
                f=flat(Y)
                if not span_contains([flat(Z) for Z in indep],f):
                    indep.append(Y); grew=True
                if len(indep)==n*n: return len(indep)
    return len(indep)
if __name__=="__main__":
    sys.path.insert(0,'output/artifacts')
    from exactM2 import M_of
    from exact2 import F,ONE,II,ZETA8
    Z=ZETA8
    for name,t in {"t11":(ONE,ONE),"t1m1":(ONE,F(-1)),"ti1":(II,ONE),"tz1":(Z,ONE),"tgen":(F(2),F(3))}.items():
        gens=M_of(t)
        print(name,"image_dim=",image_dim2(gens),flush=True)
