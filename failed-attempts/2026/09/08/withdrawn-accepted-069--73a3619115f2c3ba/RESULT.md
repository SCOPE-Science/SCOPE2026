# Ternary Sylvester–Gallai minimum on eight points: E_3 = 4 with two minimizer types

## Context
The Sylvester–Gallai theorem (every rank-3 real-representable matroid has a 2-point line), Kelly's complex rank-3 extension, and the Geelen–Kroeker complex rank-k-flat generalization leave open the finite-field boundary: which GF(q)-representable classes force ordinary lines at small n. The ternary (GF(3)-representable) 8-point stratum, defined by Seymour's excluded minors, is the first scope above the 7-point Fano/non-Fano threshold where binary (Fano plane has 0 ordinary lines), ternary, and complex behaviors diverge.

## Definitions
- Work with spanning simple matroids of rank 3 on ground set [8] = {0,…,7}, presented by rank-2 flats ("lines"): a family F of subsets each of size ≥ 2 partitioning the C(8,2) = 28 pairs (linear-space axiom), spanning rank 3 (more than one flat).
- An **ordinary line** is a flat of size exactly 2.
- A matroid is **ternary** if GF(3)-representable. Every ternary rank-3 matroid is a restriction of the projective plane PG(2,3): 13 points, 13 lines of 4 points each, collineation group PGL(3,3) of order 5616.

## Result (headline claim)
Among ternary spanning simple rank-3 matroids on 8 points:
- (a) the minimum number of ordinary (2-point) lines is **E_3 = 4**;
- (b) exactly **two** isomorphism types attain 4, with automorphism orders **8 and 48**;
- (c) the third PGL(3,3)-orbit of 8-sets has 7 ordinary lines (Aut order 12);
- (d) orbit sizes **702 + 117 + 468 = C(13,8) = 1287**, closing the ternary census.

Minimizer witnesses (labels 0..7 of the coordinate vector):
- Type A (Aut 8, 11 lines, size distribution 4^1·3^6·2^4): V_A = [(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,2,2),(0,1,2),(1,2,1),(1,1,2)]. Flats: 01 | 02 | 034 | 0567 | 125 | 136 | 147 | 237 | 246 | 35 | 45 (4 two-point lines: 01, 02, 35, 45). S8-permutation [2,5,6,4,7,3,0,1] carries this onto PGL-orbit 0's flat family.
- Type B (Aut 48, 12 lines, size distribution 3^8·2^4): V_B = [(1,0,0),(0,1,0),(0,0,1),(1,0,1),(0,1,1),(1,2,2),(1,2,1),(1,1,2)]. Flats: 01 | 023 | 045 | 067 | 124 | 136 | 157 | 256 | 27 | 347 | 35 | 46 (4 two-point lines: 01, 27, 35, 46). S8-permutation [0,7,1,2,4,3,5,6] carries this onto PGL-orbit 1's flat family.

Separation gloss: the all-abstract minimum is also 4 but on three coarse types; the third (Aut order 24, 1680 labeled members) is provably non-ternary by exhaustive normalized coordinate-search failure, so the ternary filter cuts the 4-line locus from 3 types to 2.

## Proof / evidence
1. Ternary universe: enumerate PG(2,3) (13 canonical projective points, 13 four-point lines) and all of PGL(3,3) (invertible 3×3 matrices over GF(3), deduplicated to 5616 point-permutations; recomputed in the verifier). Canonicalizing all C(13,8) = 1287 eight-sets under this group yields 3 orbits. Restriction flats = maximal intersections of PG-lines with the 8-set of size ≥ 2; ordinary counts are 4, 4, 7. Orbit–stabilizer sizes (PGL-stabilizers 8, 48, 12) give orbit sizes 702, 117, 468 summing to 1287, so no ternary 8-set is missed. Completeness is by group-action partition, i.e. proof, not sampling.
2. Each coordinatization uses 8 distinct projective points and its collinearity flats equal (up to the logged permutation) the claimed PGL-orbit flat family, so both minimizers are ternary with exactly 4 ordinaries. Canonical-form comparison confirms V_A ≅ PGL orbit 0, V_B ≅ PGL orbit 1, orbits pairwise non-isomorphic, abstract Aut orders 8/48/12 (labeled class sizes 5040/840/3360).
3. Abstract cross-check: independent K8-edge clique-partition backtracking over all linear spaces on 8 points gives 433038 labeled spanning simple rank-3 families in 62 size-signature groups. Group ordinary minimum is 4 on groups of labeled sizes 1680 (Aut 24), 5040 (Aut 8), 840 (Aut 48). Canonical comparison shows 5040 = PGL orbit 0, 840 = PGL orbit 1, and the 1680 rep is distinct from all three PGL orbits; normalized exhaustive GF(3) search (basis fixed to e1,e2,e3, all 10^5 completions, 30240 distinct-point cases) finds no realization, certifying non-ternarity by search failure.
4. `python3 output/artifacts/verify.py` recomputes |PGL(3,3)| = 5616, replays all flat families and ordinary counts, checks orbit sizes sum to 1287, replays both coordinatizations with explicit matching permutations, and checks Aut orders and census totals. Output ends `ALL CHECKS PASS`. Independently re-run by the auditor.

## Limitations
- The 62 census groups are coarse (line-size-signature) classes, not the 68 isomorphism types of Mayhew–Royle/SCOPE026; only the three 4-ordinary groups were split into true isomorphism types.
- Non-ternarity of the third abstract minimizer is certified by exhaustive normalized coordinate-search failure, not by a named Seymour excluded minor (no U_{2,5}/U_{3,5}/F_7/F_7* minor witness exhibited).
- The 7-point ternary line table and full 68-type coordinatization/excluded-minor library are not delivered.
- Novelty rests on title/abstract/theorem-level gap analysis (Geelen–Kroeker, Green–Tao, Mayhew–Royle state no ternary 8-point ordinary-line minimum).

## Reproducibility
Stdlib-only Python 3. Scripts: `output/artifacts/enumerate.py` (PGL census → `results.json`), `output/artifacts/census8.py` (abstract census → `census_summary.json`), `output/artifacts/verify.py` (independent replay). Runtimes: PGL census seconds; abstract census ~6 s; ternary decisions seconds each; full verifier minutes (includes 40320-permutation automorphism computations and PGL-stabilizer scan over 5616 maps).

## References
- J. Geelen and M. E. Kroeker, A Sylvester-Gallai-type theorem for complex-representable matroids, arXiv:2212.03307.
- B. Green and T. Tao, On sets defining few ordinary lines, arXiv:1208.4714.
- D. Mayhew and G. F. Royle, Matroids with nine elements, arXiv:math/0702316.
- J. Oxley, Matroid Theory, 2nd ed. (Oxford, 2011) — Seymour ternary excluded-minor background.
