"""Script B: B_rec builder, brute-force C7 detector (small n), star-gadget sharpness test,
and binary-pattern enumeration for the star analysis."""
import itertools
from math import comb

def brec_dp(N):
    b = [0]*(N+1); ch = [None]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a, 2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch

B, CH = brec_dp(60)

def build_brec(n, offset=0):
    """Return (edges set of sorted triples, blocks list of lists, top V1 set)."""
    edges = set(); blocks = []
    def rec(verts):
        m = len(verts)
        if m <= 2: return
        a = CH[m]
        V1 = verts[:a]; V2 = verts[a:]
        blocks.append(list(V1))
        for i in range(len(V1)):
            for j in range(i+1, len(V1)):
                for w in V2:
                    edges.add(tuple(sorted((V1[i], V1[j], w))))
        rec(V2)
    rec(list(range(offset, offset+n)))
    top = set(blocks[0]) if blocks else set()
    return edges, blocks, top

def has_C7(edges, n):
    E = set(edges)
    for tup in itertools.permutations(range(n), 7):
        ok = True
        for i in range(7):
            t = tuple(sorted((tup[i], tup[(i+1)%7], tup[(i+2)%7])))
            if t not in E:
                ok = False; break
        if ok:
            return tup
    return None

print("== B_rec C7-freeness sanity (brute force, n<=9) ==")
for n in range(3, 10):
    E, blocks, top = build_brec(n)
    cyc = has_C7(E, n)
    print(f"n={n} brec={len(E)} (dp {B[n]}) blocks={[len(bl) for bl in blocks]} C7={cyc}")

print("== star gadget: B_rec + full star inside top V1 ==")
for n in range(3, 11):
    E, blocks, top = build_brec(n)
    V1 = sorted(top)
    if len(V1) >= 3:
        x = V1[0]
        add = set()
        rest = [v for v in V1 if v != x]
        for i in range(len(rest)):
            for j in range(i+1, len(rest)):
                add.add(tuple(sorted((x, rest[i], rest[j]))))
        E2 = E | add
        cyc = has_C7(E2, n)
        print(f"n={n} |V1|={len(V1)} brec={len(E)} +star={len(add)} total={len(E2)} C7={cyc}")
    else:
        print(f"n={n} |V1|={len(V1)} skip")

print("== binary patterns, window sums in {0,2,3} (star analysis) ==")
surv = []
for bits in itertools.product([0,1], repeat=7):
    if all((bits[i]+bits[(i+1)%7]+bits[(i+2)%7]) in (0,2,3) for i in range(7)):
        surv.append(bits)
print("count:", len(surv))
for bits in surv:
    n3 = sum(1 for i in range(7) if bits[i]+bits[(i+1)%7]+bits[(i+2)%7] == 3)
    print(bits, "sum=", sum(bits), "#3-windows=", n3)
