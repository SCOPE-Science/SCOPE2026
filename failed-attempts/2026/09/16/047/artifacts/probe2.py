import random, itertools

def bottleneck_assignment(D):
    r=len(D)
    vals=sorted({v for row in D for v in row})
    def has_perf(th):
        adj=[[j for j in range(r) if D[i][j]<=th+1e-9] for i in range(r)]
        mt=[-1]*r
        def dfs(u,seen):
            for v in adj[u]:
                if seen[v]: continue
                seen[v]=True
                if mt[v]==-1 or dfs(mt[v],seen):
                    mt[v]=u; return True
            return False
        m=0
        for u in range(r):
            if dfs(u,[False]*r): m+=1
            else: break
        return m==r
    for v in vals:
        if has_perf(v): return v
    return vals[-1]

def supports_inf(A,C,delta=1):
    # infinite rectangles [a,inf), [c,inf): SF_ij iff c_j<=a_i+d; SG_ji iff a_i<=c_j+d
    r=len(A); n=len(A[0])
    SF=[[all(C[j][k]<=A[i][k]+delta+1e-9 for k in range(n)) for j in range(r)] for i in range(r)]
    SG=[[all(A[i][k]<=C[j][k]+delta+1e-9 for k in range(n)) for i in range(r)] for j in range(r)]
    # SG indexed [j][i]
    return SF,SG

def dist_mat(A,C):
    r=len(A); n=len(A[0])
    return [[max(abs(C[j][k]-A[i][k]) for k in range(n)) for j in range(r)] for i in range(r)]

def invert_test(SF,SG,trials=200):
    # generic F on SF -> G=inv(F), check support on SG; and vice versa. Use numpy.
    import numpy as np
    r=len(SF)
    SFa=np.array(SF,dtype=bool); SGa=np.array(SG,dtype=bool)
    rng=np.random.default_rng(0)
    for _ in range(trials):
        F=rng.standard_normal((r,r))*(SFa)
        if np.linalg.matrix_rank(F)<r: continue
        try: G=np.linalg.inv(F)
        except: continue
        ok=True
        for j in range(r):
            for i in range(r):
                if abs(G[j,i])>1e-6 and not SGa[j,i]:
                    ok=False; break
            if not ok: break
        if ok: return True, F, G
    for _ in range(trials):
        G=rng.standard_normal((r,r))*(SGa.T)  # careful: G rows=j cols=i
        # G as j,i matrix; as linear map N->M? F is i,j? Let's treat F(rxr) rows=i cols=j, G rows=j cols=i
        if np.linalg.matrix_rank(G)<r: continue
        try: F=np.linalg.inv(G)
        except: continue
        ok=True
        for i in range(r):
            for j in range(r):
                if abs(F[i,j])>1e-6 and not SFa[i,j]:
                    ok=False; break
            if not ok: break
        if ok: return True, F, G
    return False, None, None

def test_config(A,C,delta=1):
    SF,SG=supports_inf(A,C,delta)
    D=dist_mat(A,C)
    db=bottleneck_assignment(D)
    ok,F,G=invert_test(SF,SG)
    return db,SF,SG,ok

if __name__=="__main__":
    import numpy as np
    # Try to reproduce n=2 ratio 3: brute force small integer points r=3
    rnd=random.Random(0)
    n=2; r=3; delta=1
    found=[]
    for trial in range(20000):
        A=[[float(rnd.randint(0,3)) for _ in range(n)] for _ in range(r)]
        C=[[float(rnd.randint(0,3)) for _ in range(n)] for _ in range(r)]
        D=dist_mat(A,C)
        db=bottleneck_assignment(D)
        if db>=3:
            SF,SG=supports_inf(A,C,delta)
            ok,F,G=invert_test(SF,SG,trials=60)
            if ok:
                print("HIT n=2 trial",trial,"db=",db)
                print(" A=",A,"C=",C)
                print(" SF=",SF,"SG=",SG)
                print(" F=",np.array_str(F,precision=2),"G=",np.array_str(G,precision=2))
                found.append((A,C))
                if len(found)>=5: break
    print("done found=",len(found))
