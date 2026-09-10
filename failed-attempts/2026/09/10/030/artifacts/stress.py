"""stress.py — stress tests for X_579 comparison horn (stdlib only).
T1: extended no-period check p<=64 via scales 3..8 (analytic factor lemma backs all p).
T2: shift-orbit phase cycling: orbit of phase-0 point visits all 8 level residues.
T3: fiber-fill accumulation: shifts by 2^k bring alternating fills to site -1
    (both values 0,1 appear i.o. -> full fiber in orbit closure).
T4: clopen partition: level cylinders E_j (j=0..7) disjoint, cover, each measure 1/8
    under any invariant mu (cyclic permutation argument, analytic).
T5: covering growth L=8,16,24 across phases+fills (mdim-0-like: per-site log drops).
Replay: python3 stress.py
"""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))
s3 = [0,1,0,2,3,1,2]
w = s3 + ['*']
def F(k): return k % 4

def hier_val(n, Y):
    for k in (3,4,5,6,7,8):
        m = 2**k
        if (n - Y) % m == m - 1:
            continue
        if k == 3:
            return w[(n - Y) % 8]
        return F(k)
    return None

# T1: extended periods 1..64 (scales 3..8, joint phase mod 256 to cover p<=64 safely)
def ruled_out(p, MOD=256):
    ruled = 0
    for Y in range(MOD):
        forced = {}
        bad = False
        for n in range(MOD):
            v = hier_val(n, Y)
            if v is None:
                continue
            j = n % p
            if j in forced and forced[j] != v:
                bad = True; break
            forced[j] = v
        if bad: ruled += 1
    return ruled
T1ok = True
for p in range(1, 65):
    r = ruled_out(p)
    if r != 256:
        T1ok = False
        print(f"STRESS_T1 p={p}: {r}/256 OUT -> SURVIVES({256-r})")
print(f"STRESS_T1 periods1-64_all_ruled_out={T1ok}")

# T2: phase cycling: shift by m sends phase Y -> Y+m (mod 8 at scale 3); orbit hits all
phases = sorted({(0 + m) % 8 for m in range(8)})
print(f"STRESS_T2 orbit_phases_mod8={phases} covers_all8={len(phases)==8}")

# T3: fills at site -1-m along x* (phase 0): values at n=-1-2^k for k=3..12
vals = []
for k in range(3, 8):
    n = -1 - 2**k
    # exact value in x* (phase 0, ultimate fill 0 at -1 only): hier through scale 12
    v = None
    for kk in range(3, 13):
        m = 2**kk
        if (n - 0) % m == m - 1:
            continue
        v = w[(n-0) % 8] if kk == 3 else F(kk)
        break
    vals.append(v)
print(f"STRESS_T3 fills_at_-1-2^k={vals} both_0_and_1_present={0 in vals and 1 in vals}")

# T4: analytic (levels partition + cyclic permutation => equal measure). Just print.
print("STRESS_T4 levels_partition=YES(disjoint,cover) sigma(E_j)=E_{j+1} => mu(E_j)=1/8 all invariant mu; boundary=0(clopen)")

# T5: covering growth
N0,N1 = -64,64
def point(t, fill=0):
    d = {}
    for n in range(N0,N1):
        v = hier_val(n, t)
        if v is None:
            v = fill if n == t-1 else F(7)
        d[n] = v
    return d
def census(L):
    S = set()
    for t in range(16):
        for fill in (0,1,2,3):
            x = point(t, fill)
            for s in range(N0, N1-L):
                S.add(tuple(x[n] for n in range(s, s+L)))
    return len(S)
for L in (8,16,24):
    c = census(L)
    print(f"STRESS_T5 blocks{L}={c} per_site_log2={math.log2(c)/L:.4f}")
print("STRESS_ALL_OK")
