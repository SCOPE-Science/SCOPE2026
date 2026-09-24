# Strict-EKR verdicts for explicit transitive groups of degree 8, with certified non-canonical maximum intersecting witnesses

## Context

The Erdős–Ko–Rado (EKR) program for transitive permutation groups asks not
only for the maximum size of an intersecting family (intersection density)
but for which maxima are canonical (strict-EKR). For prime-power degree,
Hujdurović–Marušič–Miklavič–Kutnar proved intersection density 1, so every
transitive group of degree 8 has maximum intersecting size |G|/8. What was
open for the explicit models below is strictness (canonicity). Degree 8 is
the smallest 2-power window combining this background with abundant
imprimitive wreath-type actions where non-canonical maxima are expected.

## Definitions

Points are {0,...,7}; permutations are one-line image tuples.
G ≤ S_8 is transitive. F ⊆ G is *intersecting* if every pair agrees
somewhere: for all g,h ∈ F there is i with g(i)=h(i). Equivalently F is a
clique of the *agreement graph* (complement of the derangement graph).
A *star* (canonical set) is a coset aG_x of a point stabilizer G_x.
G has the *EKR property* if no intersecting set exceeds |G|/8, and
*strict-EKR* if every maximum intersecting set is a star.
Maximum size k = |G|/8; maximum cliques of the agreement graph are the
maximum intersecting sets.

## Result

Explicit models are identified by their archived generators (isomorphism
labels are descriptive only). Verified claims:

- (a) Lemma: every transitive G of degree 8 with |G| ≤ 16 has strict-EKR.
- (b) G24 (order 24, stabilizer 3, imprimitive, described as S4 on its eight
  3-cycles): maximum intersecting size 3; exactly 128 maximum cliques, of
  which 32 (as sets) are stars; strict-EKR FAILS. Witness indices
  [12,21,22]: [4,2,1,7,0,6,5,3], [7,5,1,3,0,2,6,4], [7,5,2,0,4,6,1,3].
- (c) G32 (order 32, stabilizer 4, imprimitive): maximum size 4; exactly 16
  maximum cliques, all stars; strict-EKR HOLDS.
- (d) G48 (order 48, stabilizer 6, imprimitive, described as S4×C2 product
  action): maximum size 6; exactly 32 maximum cliques, all stars;
  strict-EKR HOLDS.
- (e) GW64 (order 64, stabilizer 8, imprimitive wreath-type, described as
  C2 wr V4): maximum size 8; exactly 1024 maximum cliques, of which 32 are
  stars; strict-EKR FAILS. Witness indices [48,56,57,58,59,60,61,62]:
  [6,7,4,5,2,3,0,1], [7,6,4,5,2,3,0,1], [7,6,4,5,2,3,1,0],
  [7,6,4,5,3,2,0,1], [7,6,4,5,3,2,1,0], [7,6,5,4,2,3,0,1],
  [7,6,5,4,2,3,1,0], [7,6,5,4,3,2,0,1].
- (f) AGL18 (order 56, stabilizer 7, primitive, described as AGL(1,8)):
  maximum size 7 certified by two independent branch-and-bound codes (plus
  auditor third code); one explicit non-canonical 7-set at indices
  [48,49,50,51,52,53,54] (perms in §4 of DRAFT / artifacts); strict-EKR
  FAILS. Total number of maxima not enumerated (capped at 2M; at least 2M
  found).

No 50-class census is claimed. C8 (order 8) check: omega=1, 8 maxima, holds.

## Proof / evidence

Distinguish proof from computation. (a) is proved: |Gx|=|G|/8 ≤ 2; if
|G|=8 maxima are singletons = stars of trivial stabilizer; if |G|=16 then
Gx={1,tx}, intersecting pair {g,h} has g^{-1}h ∈ Gy hence equals coset gGy.
(b)–(f) sizes and verdicts are exact-computation certificates, independently
replayed:

- Groups built from generators by permutation multiplication only;
  transitivity (orb(0)=8), orders, stabilizer orders verified.
- Agreement graphs built by direct comparison. Maxima certified by exact
  color-sort branch-and-bound max-clique, cross-checked by an independently
  written degeneracy-order branch-and-bound plus greedy-coloring upper bound,
  plus brute force C(24,3)=2024 for G24 (128 cliques) and C(32,4) for G32
  (16 cliques) and no-(k+1)-clique checks; auditor re-ran a third BB
  (omega 1/3/4/6/8/7) and independent counting recursions (G48: 32,
  GW64: 1024) and confirmed listed G48 cliques equal the star set.
- Canonicity tested against all 8·|G|/8 point-stabilizer cosets as sets;
  each witness verified pairwise-intersecting and not in the star set.
  verify.py reports ALL VERIFY CHECKS PASSED; logs in results.json.
- AGL(1,8) model independently confirmed 2-transitive, block-free
  (primitive), Frobenius (non-identity stabilizer elements fix only the
  base point).

## Limitations

- Covers only the six explicit models, not the full transitive degree-8
  class (50 classes); no claim about remaining classes.
- Isomorphism labels beyond verified numerical data (order, stabilizer
  order, block data) are descriptive; identity rests on explicit generators.
- rho=1 background theorem is cited, not re-proved; size equalities are
  additionally cross-checked by exact computation.
- AGL(1,8) failure verdict alone follows from the known Frobenius
  strict-EKR criterion (|H|=7>2); novelty there is the explicit witness
  plus omega=7 certificate, not the bare verdict. Its total maxima count
  is not established.
- Order-384 C2 wr S4 exploration was inconclusive and carries no claim.

## Reproducibility

Artifacts: output/artifacts/groups.json (archived element lists),
output/artifacts/results.json (logs, clique indices, counts),
output/artifacts/compute.py (search), output/artifacts/verify.py
(independent replay). Re-run compute.py to regenerate groups/results,
then verify.py (expects output/artifacts/ paths) to replay omega values,
brute-force G24/G32 counts, and witness clique/non-star checks with stdlib
Python only.

## References

- Hujdurović, Marušič, Miklavič, Kutnar — Intersection density of
  transitive groups of certain degrees. https://arxiv.org/abs/2104.04699
- Hujdurović, Kutnar, Marušič, Miklavič — On maximum intersecting sets in
  direct and wreath product of groups. https://arxiv.org/abs/2108.03943
- Ahmadi, Meagher — The Erdős–Ko–Rado property for some permutation
  groups. https://arxiv.org/abs/1311.7060
- Pantangi — All 3-transitive groups satisfy the strict-EKR property.
  https://arxiv.org/abs/2311.13055
