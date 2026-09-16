import random, sys
sys.path.insert(0,"output/artifacts")
from probe2 import dist_mat, bottleneck_assignment, supports_inf, invert_test
import numpy as np

def run(n,r,grid,trials,seed=1,db_thresh=4,inv_trials=120):
    rnd=random.Random(seed)
    hits=0
    for trial in range(trials):
        A=[[float(rnd.randint(0,grid)) for _ in range(n)] for _ in range(r)]
        C=[[float(rnd.randint(0,grid)) for _ in range(n)] for _ in range(r)]
        D=dist_mat(A,C)
        db=bottleneck_assignment(D)
        if db>=db_thresh:
            SF,SG=supports_inf(A,C,1)
            ok,F,G=invert_test(SF,SG,trials=inv_trials)
            if ok:
                hits+=1
                print(f"HIT n={n} r={r} trial={trial} db={db}",flush=True)
                print(" A=",A,"C=",C,flush=True)
                print(" SF=",SF,flush=True)
                print(" SG=",SG,flush=True)
                print(" F=",np.array_str(F,precision=3,suppress_small=True),flush=True)
                print(" G=",np.array_str(G,precision=3,suppress_small=True),flush=True)
                print(" D=",D,flush=True)
                if hits>=10: break
    print(f"done n={n} r={r} hits={hits}",flush=True)

if __name__=="__main__":
    n=int(sys.argv[1]) if len(sys.argv)>1 else 3
    r=int(sys.argv[2]) if len(sys.argv)>2 else 3
    grid=int(sys.argv[3]) if len(sys.argv)>3 else 3
    trials=int(sys.argv[4]) if len(sys.argv)>4 else 30000
    seed=int(sys.argv[5]) if len(sys.argv)>5 else 1
    run(n,r,grid,trials,seed)
