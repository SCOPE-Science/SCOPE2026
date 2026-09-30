# Forced (7,4)-configurations above C q^{5.5} in the Hermitian-truncated collinear-triple 3-graph

## Context

The Brown–Erdős–Sós (7,4) problem — whether every linear 3-uniform hypergraph
with ω(n²) edges contains four edges on at most seven vertices — is the
recognized first-open case after Ruzsa–Szemerédi (6,3). A proposed route via a
Hermitian direction-restricted collinear-triple lift H_q on AG(3,q) with
p-thinning plus deletion was investigated for a (7,4)-free N^{7/4}/polylog
family and found blocked (target-exit evidence: same-line (7,4)-density wall,
envelopes 2.6–15× short at small q). The result below is the admitted preset
fallback: the exact density wall for the fixed lift H_q.

## Definitions

Let q ≥ 7 be a prime power, V_q = AG(3,q) = F_q³ (N_q = q³). A direction is a
point of PG(2,q) (normalized nonzero vector, first nonzero coordinate 1).

- If q = r² is a square, S_q ⊂ PG(2,q) is the Hermitian locus
  S_q = {[x_0:x_1:x_2] : x_0^{r+1}+x_1^{r+1}+x_2^{r+1} = 0},
  of size r³+1 = q^{3/2}+1 (e.g. |S_9| = 28).
- If q is not a square, S_q is the first m_q = ⌊q^{3/2}⌋+1 directions of
  PG(2,q) in lexicographic order of normalized representatives.

In all cases q^{3/2} ≤ |S_q| ≤ q^{3/2}+1. The host H_q has as edges all
collinear triples of AG(3,q) lying on a line whose direction is in S_q.
With q² lines per direction and C(q,3) triples per line,
|E(H_q)| = |S_q| q² C(q,3) ≥ q⁶/4 for q ≥ 7 (c_0 = 1/4).

A (7,4)-configuration is four distinct edges spanning at most 7 vertices.

## Result (preset fallback)

With absolute C = 3/4 and q_0 = 7: for every prime power q ≥ q_0, every
F ⊆ E(H_q) with |F| ≥ C q^{5.5} contains four distinct edges spanning at
most 7 vertices (in fact at most 6 — four triples sharing one pair).

## Proof

Lemma (pair-disjointness). Distinct lines of H_q share no pair: two distinct
points of AG(3,q) lie on a unique line with a unique direction; that pair is
covered iff the direction is in S_q, by exactly one host line.

Let P_q be the set of pairs covered by host lines. By the lemma,
|P_q| = |S_q| q² C(q,2) = |S_q| q³(q−1)/2.
Since |S_q| ≤ q^{3/2}+1 ≤ 1.054 q^{3/2} for q ≥ 7 and (q−1)/q ≤ 1,
|P_q| ≤ 0.527 q^{5.5} ≤ 9/16 q^{5.5} (q ≥ 7).

Let F ⊆ E(H_q), |F| ≥ 3/4 q^{5.5}. Count edge-pair incidences
I = {(e,P): e ∈ F, P ⊂ e}: each edge has 3 pairs, so I = 3|F| ≥ 9/4 q^{5.5}.
Every such pair lies in P_q, so the average pair-degree is
d̄ = I/|P_q| ≥ (9/4)/(9/16) = 4.
Hence some pair {u,v} lies in at least 4 distinct edges of F. Those four
edges differ in the third vertex and their union is {u,v} plus at most 4
further vertices: at most 6 ≤ 7 vertices. ∎

## Machine certificate (key incidence count)

`output/artifacts/verify_fallback.py` (stdlib only) replays in seconds,
emits `fallback_certificate.json`, prints VERIFY_OK (independently replayed
by auditor):

- q = 9 (true Hermitian model x_0⁴+x_1⁴+x_2⁴ = 0 over F_9 = F_3[x]/(x²+1)):
  |S_9| = 28; N = 729; lines = 2268 = 28·9²; |E(H_9)| = 190512 ≥ 9⁶/4;
  |P_9| = 81648 ≤ 9/16·9^{5.5}; pair-disjointness asserted (no pair on two
  lines). First ⌈3/4·9^{5.5}⌉ = 132861 host edges contain a pair of degree 7
  ≥ 4; four edges through it with union size 6 ≤ 7 exhibited.
- q = 7 (same-scale model, |S_7| = 19): N = 343, lines = 931,
  |E(H_7)| = 32585 ≥ 7⁶/4, |P_7| = 19551 ≤ 9/16·7^{5.5},
  pair-disjointness asserted. Here |E(H_7)| < 3/4·7^{5.5}, so the wall is
  vacuous at q = 7; the counting proof covers all q ≥ 7 uniformly.

## Limitations

Proves only the preset q^{5.5} wall for this fixed H_q. Does not construct
the N^{7/4} target family (blocked per target-exit evidence), does not
optimize C, gives no bound for hosts outside this H_q. Vacuous at q = 7
(non-vacuous from q ≥ 8). Non-square S_q is a lexicographic same-scale set;
the proof uses only its size, not Hermitian geometry, in that case.

## Reproducibility

Run `python3 output/artifacts/verify_fallback.py` (stdlib only) → VERIFY_OK
plus `fallback_certificate.json`.

## References

- Keevash–Long, The Brown–Erdős–Sós Conjecture for hypergraphs of large
  uniformity — BES only for r ≥ r_0(ε); (7,4) for 3-graphs explicitly open.
- Conlon–Gishboliner–Levanzov–Shapira, A New Bound for the Brown–Erdős–Sós
  Problem — upper-bound progress only.
- Solymosi, The (7,4)-conjecture in finite groups; Solymosi–Wong, BES in
  finite abelian groups — containment (upper) direction, no Hermitian lift.
- Bohman–Warnke, Large girth approximate Steiner triple systems;
  Kwan–Sah–Sawhney–Simkin, High-Girth Steiner Triple Systems — forbid
  (j,j−2), not (7,4) = (7,7−3).
