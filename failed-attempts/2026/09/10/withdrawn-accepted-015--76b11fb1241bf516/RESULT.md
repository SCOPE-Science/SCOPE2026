# T3S Trivialization: literal frozen tripartite synchronous GHZ-parity game has values 1, gap 0

## Context
The Tsirelson / MIP*=RE / Connes-embedding program seeks small explicit
finite-vs-infinite entanglement witnesses. The admitted target froze one
minimal tripartite synchronous game T3S and conjectured
omega_qc(T3S)=1 vs omega_q(T3S)<=23/24 (gap >=1/24), with a GHZ-rigidity
fallback. Frei (2209.07940) records the quest for an explicit synchronous
witness as open. The audit plan froze the table, ran an exhaustive
deterministic census, and compared NPA/tracial values.

## Definitions
T3S: X=Y=Z={0,1}, A=B=C={0,1}, uniform over 8 question triples.
Win predicate V: if x=y=z, win iff a=b=c (win set {000,111});
else win iff a XOR b XOR c = 1 (odd parity, win set {001,010,100,111}).
Full 64-entry table: `artifacts/t3s_table.json`, `artifacts/t3s_table.csv`
(28 winning entries: 2+2 diagonal + 6x4 off-diagonal).
omega_c/omega_q/omega_qc: optimal win probability over classical /
finite-dimensional tensor-product / commuting-operator strategies.
NPA optimum: SDP hierarchy upper bound.

## Result
**Theorem.** On literal T3S:
omega_c = omega_q = omega_qc = 1 (hence omega_qs = omega_qa = 1),
the NPA optimum is 1 at every level, gap delta = 0.
The unique deterministic optimum is the constant-1 strategy (8/8).
The conjectured tensor bound omega_q <= 23/24 is false
(witness exceeds it by exactly 1/24).
GHZ-only rigidity is refuted: the eps=0 perfect product strategy const-1
is at total-variation distance 1 from the canonical GHZ/XXX distribution,
so no O(sqrt(eps)) GHZ-closeness can hold at eps=0.

## Proof / evidence
Lemma 1 (const-1 perfect): V(1,1,1|x,y,z)=1 for all 8 triples —
diagonal since 1=1=1; off-diagonal since 1^1^1=1. Scores 8/8.
Lemma 2 (uniqueness): diagonal play forces f(0)=g(0)=h(0)=:u,
f(1)=g(1)=h(1)=:v. Q001 needs u^u^v=v=1; Q110 needs v^v^u=u=1,
hence (u,v)=(1,1). Exhaustive census over all 64 deterministic strategies
corroborates: win-count spectrum {0:3, 2:7, 3:24, 4:18, 5:8, 6:3, 8:1},
second-best 6/8=3/4. Values: 1-dim embeddings carry const-1 into every
class (product state, POVMs {0,I}, joints delta_111; commuting scalars;
tracial id, tau=1), each scoring exactly 1; every value <=1 by
normalization, so 1=omega_c<=omega_q<=omega_qs<=omega_qa<=omega_qc<=1.
Delta=0; 1>23/24 by 1/24. NPA: primal feasible 1 plus analytic dual
1-J = average lose-mass >= 0 gives optimum 1 every level.
GHZ legs: canonical GHZ/XXX gives P(a=b=c)=1/4 on diagonal,
Z-only value 5/8; GHZ+trivial measurements gives delta_111, value 1
(entanglement irrelevant). Refutation: const-1 (rank 1, support {111})
vs GHZ/XXX (rank 2, support {000,011,101,110}) have disjoint supports on
Q000, TV=1 (maximal); local isometries preserve rank.
Root cause: diagonal admits 111 and odd parity admits 111, so a global
constant winner exists (Mermin differs: even parity on Q000 forbids 111).

## Limitations
Certified obstruction / negative decision on T3S-literal, not a separation
witness. Redirects gap-hunting to weight-restricted or larger games.
Predicate reading: parity (XOR, mod 2) per frozen text; integer-sum
exactly-one reading excluded. No uncertainty in the finite mathematics
(exact checks + definitional chain, zero external theorems).

## Reproducibility
`python3 artifacts/verify.py` -> VERIFY_OK
(table=64, const1=8/8, omega_c=1, omega_q=omega_qc=1,
23/24-bound refuted, delta=0). Stdlib only.

## References
- Ji et al., MIP*=RE, arXiv:2001.04383 (huge non-explicit games).
- Navascues-Pironio-Acin, NPA hierarchy, arXiv:0803.4290 (generic machinery).
- Slofstra, arXiv:1606.03140 (bipartite linear-system witnesses).
- Coladangelo-Stark, arXiv:1708.06522 (infinite Q/A separations only).
- Frei, arXiv:2209.07940 (explicit synchronous quest open).
- Kar arXiv:2503.23500; Zhao arXiv:2411.03259 (generic robust self-testing).
