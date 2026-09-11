"""Adversarial search: random colorings, structured extremal sets, annealing."""
import numpy as np, itertools, sys, time
from search import batch_hits, build_tets, partitions_for_deletion, tet_planes

def count_capped(P, cols, dep, delidx, cap):
    rem = [list(c) for c in cols]
    rem[dep] = [i for i in rem[dep] if i != delidx]
    tets = build_tets(P, rem)
    SA, Sb = [], []
    count = 0
    for ks in partitions_for_deletion(rem, dep):
        SA.append(np.vstack([tets[k][0] for k in ks])); Sb.append(np.concatenate([tets[k][1] for k in ks]))
        if len(SA) == 256:
            count += int(batch_hits(np.array(SA), np.array(Sb)).sum())
            SA, Sb = [], []
            if count >= cap: return count
    if SA: count += int(batch_hits(np.array(SA), np.array(Sb)).sum())
    return count

def objective(P, cols, cap=4):
    tot = 0; worst = None
    for dep in range(4):
        for delidx in cols[dep]:
            c = count_capped(P, cols, dep, delidx, cap)
            tot += c
            if worst is None or c < worst[0]: worst = (c, dep, delidx)
            if tot >= cap * 16: pass
    return tot, worst

def full_dist(P, cols):
    return {(dep, d): count_capped(P, cols, dep, d, 10**9) for dep in range(4) for d in cols[dep]}

def rand_coloring(rng):
    idx = rng.permutation(16); return [sorted(idx[4*c:4*c+4].tolist()) for c in range(4)]

def transversal_coloring(rng):
    # 4 centers; each color takes one point near each center
    centers = np.array([[5,5,5], [5,-5,-5], [-5,5,-5], [-5,-5,5]], float)
    P = np.zeros((16, 3)); cols = [[], [], [], []]
    for m in range(4):
        perm = rng.permutation(4)
        for c in range(4):
            i = 4*m + c
            P[i] = centers[m] + rng.normal(scale=0.4, size=3)
            cols[perm[c]].append(i)
    return P, cols

def four_lines(rng, L=10.0):
    P = np.zeros((16, 3))
    dirs = [np.array([1,0,0],float), np.array([0,1,0],float), np.array([0,0,1],float), np.array([1,1,1],float)/np.sqrt(3)]
    offs = [np.array([0,3,0],float), np.array([0,0,3],float), np.array([3,0,0],float), np.array([0,0,0],float)]
    for c in range(4):
        for k in range(4):
            P[4*c+k] = offs[c] + (k-1.5)*L/4*dirs[c] + rng.normal(scale=0.05, size=3)
    return P

def two_skew(rng, L=10.0):
    P = np.zeros((16, 3))
    for k in range(8):
        P[k] = np.array([(k-3.5)*L/8, 0, 0]) + rng.normal(scale=0.05, size=3)
        P[8+k] = np.array([0, (k-3.5)*L/8, 5]) + rng.normal(scale=0.05, size=3)
    return P

def cyclic44(rng, noise=0.02):
    t = np.linspace(1, 4, 16)
    P = np.column_stack([t, t**2/4, t**3/16]) + rng.normal(scale=noise, size=(16,3))
    return P

def anneal(rng, P0, cols0, iters=600, step=0.5, cap=4, recolor=False, seed_note=''):
    P = P0.copy(); cols = [list(c) for c in cols0]
    best, w = objective(P, cols, cap); cur = best
    print(f'  init obj={cur} worst={w}', flush=True)
    for it in range(iters):
        P2 = P + (np.arange(16)[:,None]==rng.integers(16))*rng.normal(scale=step, size=(16,3))*0 + 0
        P2 = P.copy(); i = rng.integers(16); P2[i] += rng.normal(scale=step, size=3)
        cols2 = cols
        if recolor and rng.random() < 0.15:
            a, b = rng.integers(4, size=2)
            if a != b and cols[a] and cols[b]:
                cols2 = [list(c) for c in cols]
                ia = rng.integers(len(cols2[a])); ib = rng.integers(len(cols2[b]))
                cols2[a][ia], cols2[b][ib] = cols2[b][ib], cols2[a][ia]
        o, w = objective(P2, cols2, cap)
        if o <= cur or rng.random() < np.exp(-(o-cur)/max(1.0, 0.02*cur+1)):
            P, cols, cur = P2, cols2, o
            if o < best:
                best = o
                print(f'  it={it} newbest={best} worst={w} {seed_note}', flush=True)
                if best == 0:
                    np.save(f'/tmp/anneal_blocker_{seed_note}.npy', P)
                    with open(f'/tmp/anneal_blocker_{seed_note}_cols.json','w') as f:
                        import json; json.dump(cols, f)
                    return P, cols, best
    return P, cols, best

if __name__ == '__main__':
    rng = np.random.default_rng(777)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'sweep'
    if mode == 'sweep':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        base_gens = {'cube': lambda r: r.uniform(0,10,size=(16,3)),
                     'lines': four_lines, 'skew': two_skew, 'cyclic': cyclic44,
                     'planar': lambda r: np.column_stack([r.uniform(0,10,size=(16,2)), 0.05*r.normal(size=16)])}
        for name, g in base_gens.items():
            nk = 0; frag = []
            for t in range(n):
                P = g(rng); cols = rand_coloring(rng)
                tot, w = objective(P, cols, cap=2)
                if w[0] == 0:
                    nk += 1; print(f'HIT {name} t={t} worst={w} cols={cols}', flush=True)
                    np.save(f'/tmp/sweep_{name}_{t}.npy', P)
                    import json; json.dump(cols, open(f'/tmp/sweep_{name}_{t}_cols.json','w'))
                frag.append(w[0])
            print(f'{name}: {n} trials, kills={nk}, min-worst={min(frag)} mean-worst={np.mean(frag):.2f}', flush=True)
        # transversal colorings
        nk = 0
        for t in range(n):
            P, cols = transversal_coloring(rng)
            tot, w = objective(P, cols, cap=2)
            if w[0] == 0:
                nk += 1; print(f'HIT transversal t={t} worst={w}', flush=True)
                np.save(f'/tmp/sweep_trans_{t}.npy', P)
        print(f'transversal: {n} trials, kills={nk}', flush=True)
    elif mode == 'anneal':
        iters = int(sys.argv[2]) if len(sys.argv) > 2 else 400
        for s in range(4):
            P = rng.uniform(0, 10, size=(16, 3)); cols = rand_coloring(rng)
            print(f'anneal seed {s}:', flush=True)
            anneal(rng, P, cols, iters=iters, step=0.6, cap=5, recolor=True, seed_note=f's{s}')
    elif mode == 'dist':
        P = np.load(sys.argv[2]); import json
        cols = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else [list(range(0,4)),list(range(4,8)),list(range(8,12)),list(range(12,16))]
        d = full_dist(P, cols)
        print(sorted(d.items(), key=lambda kv: kv[1])[:6])
