"""Exhaustive exact-match search over small 0/1 block graphons.

Enumerate symmetric 0/1 n x n matrices (n=3,4), group by EXACT integer
homomorphism counts (K2, P2, P3, K3, C4, star S3, K4 minus edge, K4),
then within each exact-match group compute exact cut distance
(min over block permutations, max over subsets) and report the largest gap.
A nonzero exact-match gap is a disproof pattern for the polynomial-vertex
inverse counting lemma; absence confirms rigidity (blocked disproof route).
"""
import itertools, json, os

def hom_int(A, H):
    n = len(A); m = max(max(e) for e in H)+1 if H else 1
    tot = 0
    for phi in itertools.product(range(n), repeat=m):
        p = 1
        for i, j in H:
            if A[phi[i]][phi[j]] == 0:
                p = 0; break
        tot += p
    return tot

def sig(A, Hs):
    return tuple(hom_int(A, H) for H in Hs)

def cutdist(A, B):
    n = len(A)
    D0 = [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]
    subs = list(itertools.product([0,1], repeat=n))
    best = None
    for perm in itertools.permutations(range(n)):
        D = [[A[i][j]-B[perm[i]][perm[j]] for j in range(n)] for i in range(n)]
        mx = 0
        for S in subs:
            for T in subs:
                s = sum(D[i][j] for i in range(n) for j in range(n) if S[i] and T[j])
                if abs(s) > mx: mx = abs(s)
        v = mx / n**2
        if best is None or v < best: best = v
    return best

# edge lists (undirected, one orientation each)
K2 = [(0,1)]
P2 = [(0,1),(1,2)]
P3 = [(0,1),(1,2),(2,3)]
K3 = [(0,1),(1,2),(0,2)]
C4 = [(0,1),(1,2),(2,3),(0,3)]
S3 = [(0,1),(0,2),(0,3)]
K4 = [(i,j) for i in range(4) for j in range(i+1,4)]
K4me = [e for e in K4 if e != (2,3)]          # diamond
paw = [(0,1),(1,2),(0,2),(2,3)]               # triangle with pendant edge
Hs = [K2,P2,P3,K3,C4,S3,K4,K4me,paw]

out = {}
for n in (3,4):
    pairs = [(i,j) for i in range(n) for j in range(i,n)]
    groups = {}
    for bits in itertools.product([0,1], repeat=len(pairs)):
        A = [[0]*n for _ in range(n)]
        for (i,j),b in zip(pairs,bits):
            A[i][j]=A[j][i]=b
        s = sig(A,Hs)
        groups.setdefault(s,[]).append(A)
    multi = {s:gs for s,gs in groups.items() if len(gs)>1}
    maxgap = 0.0; ex = None; nexact_pairs=0
    for s,gs in multi.items():
        # dedupe under permutation
        reps=[]
        for A in gs:
            if not any(cutdist(A,R)==0.0 for R in reps): reps.append(A)
        for a in range(len(reps)):
            for b in range(a+1,len(reps)):
                nexact_pairs += 1
                d = cutdist(reps[a],reps[b])
                if d>maxgap: maxgap=d; ex=(reps[a],reps[b],s)
    out[n]=dict(n_matrices=2**len(pairs), n_groups=len(groups),
                n_multigroups=len(multi), n_exact_pairs=nexact_pairs,
                max_exact_gap=maxgap)
    print(f"n={n}: matrices={2**len(pairs)} groups={len(groups)} "
          f"multigroups={len(multi)} exactpairs={nexact_pairs} maxgap={maxgap}",
          flush=True)
    if ex: print("example:", ex[0], ex[1], ex[2], flush=True)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "search_exact_match_results.json"),"w") as f:
    json.dump(out,f,indent=2)
print("RESULT_JSON:"+json.dumps(out))
