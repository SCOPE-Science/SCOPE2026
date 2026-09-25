"""S_14-inequivalence test: backtracking isomorphism search (two orders, must both agree)."""
import glob

def load(f):
    return [int(l.strip(), 2) for l in open(f) if l.strip()]

def iso_exists(A, B, seed):
    FA = [frozenset(i for i in range(14) if (x >> (13 - i)) & 1) for x in A]
    FBset = set(frozenset(i for i in range(14) if (x >> (13 - i)) & 1) for x in B)
    degA = [sum(1 for s in FA if i in s) for i in range(14)]
    degB = [sum(1 for s in FBset if i in s) for i in range(14)]
    order = sorted(range(14), key=lambda i: (degA[i], (i + seed) % 14))
    pairA = [[sum(1 for s in FA if i in s and j in s) for j in range(14)] for i in range(14)]
    pairB = [[sum(1 for s in FBset if i in s and j in s) for j in range(14)] for i in range(14)]
    img = [None]*14
    used = [False]*14
    found = [False]
    def ok():
        for s in FA:
            t = {img[p] for p in s if img[p] is not None}
            if t and not any(t <= set(F) for F in FBset):
                return False
        return True
    def dfs(k):
        if found[0]:
            return
        if k == 14:
            if all(frozenset(img[p] for p in s) in FBset for s in FA):
                found[0] = True
            return
        p = order[k]
        for q in range(14):
            if used[q] or degA[p] != degB[q]:
                continue
            good = True
            for r in range(14):
                if img[r] is not None and pairA[p][r] != pairB[q][img[r]]:
                    good = False
                    break
            if not good:
                continue
            img[p] = q
            used[q] = True
            if ok():
                dfs(k+1)
            img[p] = None
            used[q] = False
            if found[0]:
                return
    dfs(0)
    return found[0]

A = load('output/artifacts/brouwer42.txt')
B = load(sorted(glob.glob('output/artifacts/clique*.txt'))[0])
for seed in (0, 5):
    print(f"seed {seed}: iso = {iso_exists(A, B, seed)}")
print("self-iso Brouwer:", iso_exists(A, A, 0), "(sanity, must be True)")
