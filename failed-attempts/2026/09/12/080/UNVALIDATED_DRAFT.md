# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact census of minimum-genus orientable embeddings of K(4,8)

## Result

**N = 1.** Up to orientation-preserving graph-automorphism equivalence there is exactly
one minimum-genus orientable cellular embedding of K(4,8). It has genus 3 and all 16
faces are 4-cycles.

## Setup and conventions

Vertices: A = {A0,A1,A2,A3}, B = {B0,...,B7}; edges all 32 pairs (Ai,Bj).
A rotation system is a cyclic ordering of incident edges at each vertex:
- `rotA[a]`: cyclic list of the 8 B-neighbours around Aa,
- `rotB[b]`: cyclic list of the 4 A-neighbours around Bb.
Write sigma_a for the successor permutation at Aa and tau_b for the successor at Bb.
Face tracing (orientation-preserving convention): from dart u -> v, the next dart is
v -> succ_v(u). So from dart a -> b the walk is

  a -> b -> a1 -> b1 -> a2 -> b2 -> ...

with a1 = tau_b(a), b1 = sigma_{a1}(b), a2 = tau_{b1}(a1), b2 = sigma_{a2}(b1), etc.

Genus: V = 12, E = 32. Minimum orientable genus is ceil((4-2)(8-2)/4) = 3.
Since K(4,8) is simple, bipartite and bridgeless, every face in a cellular embedding
has degree >= 4 and even, so 2E = sum face-deg >= 4F gives F <= 16, hence
g = (2 - V + E - F)/2 >= (2-12+32-16)/2 = 3, with equality iff F = 16 and every
face is a 4-cycle. So minimum-genus embeddings are exactly the quadrangular
embeddings (16 quad faces), all of genus 3.

## Representative (unique class)

At A-vertices (B-neighbours in cyclic order):

- rotA0 = [0,1,2,3,4,5,6,7]
- rotA1 = [0,7,6,5,4,3,2,1]
- rotA2 = [0,1,2,3,4,5,6,7]
- rotA3 = [0,7,6,5,4,3,2,1]

At B-vertices (A-neighbours in cyclic order):

- rotB_even = [0,1,2,3] for b in {0,2,4,6}
- rotB_odd = [0,3,2,1] for b in {1,3,5,7}

Face-trace verification (script `output/artifacts/census_full.py`, independently
replicated by `output/artifacts/ilp_exact.py`) gives exactly 16 faces, each of
length 4, hence genus (2-12+32-16)/2 = 3. The 16 faces as dart cycles
(tail -> head), writing (X,i) for vertex Xi:

- F0:  (A0->B0), (B0->A1), (A1->B7), (B7->A0)
- F1:  (B0->A0), (A0->B1), (B1->A3), (A3->B0)
- F2:  (B1->A0), (A0->B2), (B2->A1), (A1->B1)
- F3:  (B2->A0), (A0->B3), (B3->A3), (A3->B2)
- F4:  (B3->A0), (A0->B4), (B4->A1), (A1->B3)
- F5:  (B4->A0), (A0->B5), (B5->A3), (A3->B4)
- F6:  (B5->A0), (A0->B6), (B6->A1), (A1->B5)
- F7:  (B6->A0), (A0->B7), (B7->A3), (A3->B6)
- F8:  (A1->B0), (B0->A2), (A2->B1), (B1->A1)
- F9:  (A1->B2), (B2->A2), (A2->B3), (B3->A1)
- F10: (A1->B4), (B4->A2), (A2->B5), (B5->A1)
- F11: (A1->B6), (B6->A2), (A2->B7), (B7->A1)
- F12: (A2->B0), (B0->A3), (A3->B7), (B7->A2)
- F13: (B1->A2), (A2->B2), (B2->A3), (A3->B1)
- F14: (B3->A2), (A2->B4), (B4->A3), (A3->B3)
- F15: (B5->A2), (A2->B6), (B6->A3), (A3->B5)

Each consecutive pair shares the pivot vertex, each step follows the successor
in the rotation above (directly checkable), each cycle alternates A/B vertices
with pattern A,B,A,B, and the four edges are distinct, i.e. a 4-cycle in K(4,8).
Every one of the 64 darts appears exactly once. So this is a quadrangular
cellular embedding of genus 3.

## Proof of completeness (N = 1)

Fix a quadrangular embedding with successor maps sigma_a (on the 8 B's) and
tau_b (on the 4 A's). Each sigma_a is an 8-cycle, each tau_b a 4-cycle.

**Step 1 — quad-closure equations.** For edge (a,b) put a1 = tau_b(a) and
b1 = sigma_{a1}(b). The face through dart a -> b has length 4 iff the next two
successor steps close it:

  (b) sigma_a(b1) = b,
  (a) tau_{b1}(a1) = a.

Indeed the walk is a->b->a1->b1->a2->b2->...; length exactly 4 with distinct
vertices (bipartite, no 2-faces since the graph is simple) is equivalent to
a2 = a and b2 = b, i.e. (a),(b). (Length 2 would need a1 = a, impossible since
tau_b is a fixed-point-free 4-cycle.) Both must hold for every edge (a,b).

**Step 2 — involution identity.** Condition (b) says, as permutations of B:

  sigma_a ∘ sigma_{a1} = id, i.e. sigma_{a1} = sigma_a^{-1},  for a1 = tau_b(a).

Since tau_b is a 4-cycle, hence onto A, every a in A occurs as some a1; thus
every sigma_a is an involution product: with f(a) := sigma_a,

  f(tau_b(a)) = f(a)^{-1} for all a, b.   (Eq*)

**Step 3 — fiber structure.** Let Im(f) = {s_1,...,s_k} be the distinct
8-cycle successor perms used, and F_i = f^{-1}(s_i) the fibers (partition of A).
Eq* says each tau_b permutes fibers, sending F_i to F_j where s_j = s_i^{-1}.
Since each tau_b is a single 4-cycle on A, all fibers in one tau_b-orbit have
equal size. Varying over all 8 values of b, but more directly: pick any i, any
a in F_i; tau_b(a) ranges over all of A as b varies? No — fix b: tau_b is one
4-cycle. For the constraint to hold for all b simultaneously with perms in S_8:
consider T = <tau_0,...,tau_7> acting on A; if some tau_b has a cycle meeting
two fibers, those fibers have equal size. We argue sharper: s and s^{-1} split.

Take any a, a' in A. Because each tau_b is a 4-cycle, the union of the tau_b's
generates a transitive subgroup of S_4 unless all tau_b preserve a common
partition — but Eq* forces the partition {F_i} to be tau_b-invariant as a set
for every b (each tau_b maps fibers to fibers). A partition of a 4-set
preserved (as a set) by a 4-cycle must be: indiscrete (1 fiber), discrete
(4 singletons), or 2+2 with the two pairs swapped by the 4-cycle. (A 1+3 or
1+1+2 partition cannot be preserved by a 4-cycle.) We rule out indiscrete and
discrete:

- Indiscrete (k=1, s_1 = s): Eq* gives s = s^{-1}, i.e. s^2 = id, contradicting
  s an 8-cycle (order 8). So k >= 2.
- Discrete (k=4, f injective): applying Eq* twice gives f(tau_b^2(a)) = f(a)
  for all a, b; since f is injective, tau_b^2 = id for every b. But each tau_b
  is a 4-cycle, and a direct check of all six 4-cycles of S_4 shows every one
  squares to a fixed-point-free double transposition, never id —
  contradiction. So the discrete case is impossible.

- Hence (up to Aut relabelling) the only surviving shape is 2+2:
  f = s on P = {0,1}, f = s^{-1} on Q = {2,3} (after applying an S_4
  permutation), where s is an 8-cycle.

**Step 4 — normalization.** Apply (pa, pb) in S_4 x S_8 = Aut(K(4,8)):
conjugate s to the standard 8-cycle sigma = (0 1 ... 7) via pb, so
sigma_0 = sigma_1 = sigma, sigma_2 = sigma_3 = sigma^{-1} (after ordering P
first). Each tau_b interchanges P and Q (else it would map a fiber to itself,
contradicting f(tau_b(a)) = f(a)^{-1} ≠ f(a)). After the S_4 normalization
P = {0,1}, Q = {2,3}, there are exactly two 4-cycles of S_4 swapping P and Q
— an inverse pair {gamma, gamma^{-1}} (direct check: the 4-cycles with image
of {0,1} equal to {2,3} are (0 2 1 3) and (0 3 1 2) = its inverse) — so every
tau_b is already in that pair with no per-vertex S_8 normalization; cyclic-order
starting points are quotiented by rotation comparison in Step 6. Thus EVERY
quadrangular embedding is Aut-equivalent to a member of the explicit
256-element normalized family:

  rotA in {sigma, sigma^{-1}}^4 (16 options),
  rotB in {gamma-order, gamma^{-1}-order}^8 (256 options / combined 256 after
  fixing the A-pattern normalization; scripts enumerate 16 x 256 with the
  A-normalization factored, i.e. 256 with schoice fixed up to swap — in fact
  the code enumerates all 16 x 256 = 4096 pairs, a superset, so normalization
  gaps are impossible).

**Step 5 — exhaustive check of the normalized family.** Face-tracing each of
the 4096 (reported as the 256 quotient — the script `census_full.py`
enumerates all 16 schoice x 256 tchoice) candidates gives quadrangular
(F = 16, all 4-cycles) for exactly 4 assignments:

  schoice in {(0,1,0,1), (1,0,1,0)}, tchoice alternating (0,1,...) or (1,0,...),

listed in `output/artifacts/census.json`. An independent second tracer
(`output/artifacts/ilp_exact.py`, separately coded integer-dart implementation)
confirms the count 4. Therefore, up to the normalization, there are exactly
4 solutions.

**Step 6 — quotient by Aut.** The 4 normalized solutions are pairwise
Aut-equivalent (explicit isomorphisms found by brute force over S_4 x S_8,
24 x 40320 elements, exact cyclic-order comparison):

- sol_1 -> sol_0 via pa = id, pb = +1 cyclic shift (b -> b+1 mod 8);
- sol_2 -> sol_0 via (pa,pb) = (id, reversal b -> -b mod 8);
- sol_3 -> sol_0 similarly (see script output).

Hence they form a single Aut-orbit. Combined with Step 4 (every quad is
equivalent to one of the 4), there is exactly one isomorphism class: **N = 1**.

**Aut size (record, not needed for N).** The stabilizer of the representative
in S_4 x S_8 has order 32 (computed by the same brute force).

## Limitations / uncertainty

- The fiber-shape argument (Step 3) is fully theoretical: indiscrete excluded
  since an 8-cycle is not an involution; discrete excluded via
  f(tau_b^2(a)) = f(a) forcing tau_b^2 = id, against the 6-element check that
  no 4-cycle of S_4 squares to id. The exhaustive enumeration covers exactly
  the surviving normalized 2+2 two-value family.
- Equivalence is orientation-preserving graph-automorphism equivalence
  (S_4 x S_8 acting by relabelling, cyclic orders compared up to rotation, not
  reversal), as specified.
- Face tracing uses the successor (left-hand) convention; the mirror
  (predecessor) convention gives the mirror embedding, equivalent here via the
  reversal isomorphism above.

## Reproduction

- `python3 output/artifacts/census_full.py` — enumerates normalized family,
  finds 4 quads, finds pairwise isomorphisms, computes Aut order 32, writes
  `output/artifacts/census.json`.
- `python3 output/artifacts/ilp_exact.py` — independent tracer recount (4).
- `python3 output/artifacts/finalize.py` — writes
  `output/artifacts/representative.json`.
- `python3 output/artifacts/crosscheck.py` — stochastic hill-climb cross-check
  harness (found 0 quads from 40 short restarts; kept as a harness, not as
  evidence for completeness — completeness rests on the exhaustive
  normalized-family enumeration, not on stochastic search).
