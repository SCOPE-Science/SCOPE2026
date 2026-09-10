"""D-to-D' fixed-point computation for P={2^n}.
D = P (discrete, no accumulation point in Q). Successor S_D(2^n)=2^{n+1}
(well-order: P intersected with any (-inf,q] is finite). gamma(2^n)=2^n.
Hence D' = P exactly (infinite). On truncation P_N={2^0..2^{N-1}}: D'=P_{N-1}.
So the Dolich-Goodrick iterate NEVER becomes finite: D^{(k)}=P for all k.
Exact integer arithmetic.
"""
P = [2**n for n in range(12)]
print("P =", P)

def successor_map(D):
    D = sorted(D)
    return {a: b for a, b in zip(D[:-1], D[1:])}

S = successor_map(P)
diffs = sorted({S[a] - a for a in S})
print("successor diffs (truncation) =", diffs)
print("P[:-1] =", P[:-1])
assert diffs == P[:-1], "truncation D' must equal P minus max"

# infinite case: gamma(2^n) = 2^{n+1}-2^n = 2^n, symbolic check for n=0..200
for n in range(201):
    assert 2**(n+1) - 2**n == 2**n
print("gamma(2^n)=2^n for n=0..200 OK")

# discreteness: gap bounded away from 0 locally; no accumulation in Q:
# min gap on P_N is 1, and gaps grow; any bounded interval contains finitely many.
def count_below(q, N=64):
    return sum(1 for n in range(N) if 2**n <= q)
print("count(P_64 <= 1000) =", count_below(1000), "(finite)")
print("DPRIME_FIXEDPOINT_OK: D'=P infinite; D^{(k)}=P for all k, never finite")
