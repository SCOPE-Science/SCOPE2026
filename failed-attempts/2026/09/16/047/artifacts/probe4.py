import random, sys
sys.path.insert(0,"output/artifacts")
from probe2 import dist_mat, bottleneck_assignment, supports_inf
import numpy as np

def gd_interleave(SF,SG,restarts=15,it=400,seed=0):
    r=len(SF); SFa=np.array(SF,bool); SGa=np.array(SG,bool)
    I=np.eye(r); rng=np.random.default_rng(seed)
    best=(1e18,None,None)
    for _ in range(restarts):
        F=rng.standard_normal((r,r))*SFa; G=rng.standard_normal((r,r))*SGa.T
        # G stored as [j,i]; as maps use F (ixj), G (jxi)
        lr=0.1
        for t in range(it):
            FG=F@G; GF=G@F
            R1=FG-I; R2=GF-I
            gF=(R1@G.T)+(G.T@R2) if False else None
            gradF=R1@G.T + (G.T@R2)
            gradG=F.T@R1 + R2@F.T
            F-=lr*gradF*SFa; G-=lr*gradG*(SGa.T)
            lr*=0.998
        res=float(np.linalg.norm(F@G-I)+np.linalg.norm(G@F-I))
        if res<best[0]: best=(res,F.copy(),G.copy())
        if best[0]<1e-8: break
    return best

if __name__=="__main__":
    n=3; r=3; grid=4; trials=4000; seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
    rnd=random.Random(seed); hits=0; tested=0
    for trial in range(trials):
        A=[[float(rnd.randint(0,grid)) for _ in range(n)] for _ in range(r)]
        C=[[float(rnd.randint(0,grid)) for _ in range(n)] for _ in range(r)]
        D=dist_mat(A,C); db=bottleneck_assignment(D)
        if db>=4:
            tested+=1
            SF,SG=supports_inf(A,C,1)
            # quick necessary: SF and SG need nonzero-permutation (det pattern)
            res,F,G=gd_interleave(SF,SG,seed=trial)
            print(f"trial={trial} db={db} res={res:.4f} A={A} C={C}",flush=True)
            if res<1e-4:
                hits+=1
                print("  HIT F=",np.array_str(F,precision=3,suppress_small=True),flush=True)
                print("  HIT G=",np.array_str(G,precision=3,suppress_small=True),flush=True)
                print("  SF=",SF,"SG=",SG,"D=",D,flush=True)
            if tested>=40: break
    print(f"done tested={tested} hits={hits}",flush=True)
