# Certified realizable Fano-type cell of Dr(3,8)

## Context

The Dressian Dr(3,8) parametrizes valuated matroids / tropical Plücker
vectors of rank 3 on 8 elements; the tropical Grassmannian TGr(3,8) is the
tropicalization of the classical Grassmannian Gr(3,8), i.e. the locus of
valuations actually realized by a matrix over a valued field. Deciding which
Dressian cells lift (Dr vs.\ TGr boundary at n=8) is the recognized gap
studied by Herrmann–Joswig–Speyer (whole fan Dr(3,8): rays/rigidity, no
per-cell realizability verdicts) and Bendle–Böhm–Ren–Schröter (TGr_0(3,8)
computed; 23 special cones obstructed by a different computational method).
General matroid-foundation theory (Baker–Lorscheid; Baker–Lorscheid–Zhang)
supplies an obstruction vocabulary but decides no Dr(3,8) cell. This record
certifies one exact lifting fact on the realizable side.

## Definitions

- K = F_2(t), v = t-adic valuation (v(0) = +infinity).
- A = 3x8 matrix over K:
  row 0: 1 0 0 1 1 0 1 1
  row 1: 0 1 0 1 0 1 1 t
  row 2: 0 0 1 0 1 1 1 t^2.
  Columns 0–6 are the seven nonzero vectors of F_2^3 (Fano configuration);
  column 7 = (1,t,t^2)^T.
- For T in C(8,3), p_T = det A_T in F_2[t], w_T = v(p_T).
- M_0 = {T : w_T = 0} (initial matroid at w).
- F_7 = Fano matroid on {0..6} with nonbases 013,024,056,125,146,236,345.

## Result

**Theorem.** With A, w, M_0 as above:

1. Exactly 7 of the 56 minors vanish identically: the 7 Fano lines
   013, 024, 056, 125, 146, 236, 345. All 21 triples containing column 7
   are nonzero polynomials (bases).
2. 40 triples have w = 0; 9 triples containing column 7 have w > 0
   (six 1's, three 2's); 7 have w = +infinity.
3. w satisfies all 1960 three-term tropical Plücker relations on
   C(8,2) x C(8,4), hence w lies in Dr(3,8).
4. M_0 has 40 bases, satisfies symmetric basis exchange, is connected
   (no separator S with r(S)+r(S^c)=3), and M_0 \ 7 = F_7 as basis sets.
5. By construction w is the tropicalization of a K-point of Gr(3,8),
   hence lies in TGr(3,8): this Fano-type cell of Dr(3,8) is realizable.

## Proof / evidence

Hand: (a) Triples within columns 0–6 have constant F_2 entries, so the
determinant is 0 iff the triple is an F_2-linear dependency, i.e. a Fano
line. (b) Any two distinct nonzero vectors of F_2^3 are linearly independent
(the only nonzero scalar is 1), hence span an F_2-plane {x : a.x=0};
evaluating a on (1,t,t^2) gives a nonzero polynomial of degree <= 2, so
every pair plus column 7 is a basis. (c) K with its valuation embeds in its
algebraic closure, so the K-realization exhibits w in TGr(3,8).

Machine-checked (replayable, stdlib only): exact bitmask polynomial
arithmetic recomputes all 56 minors; checks the 7-nonbasis identity, the
40/6/3 value split, all 1960 tropical Plücker relations (minimum attained
at least twice; all-+infinity octahedra pass vacuously), the full
40x40 symmetric-exchange table for M_0, separator-free connectedness, and
the deletion identity M_0\7 == F_7. Run:

    python3 output/artifacts/verify_dressian_cell.py

prints ALL CHECKS PASS (instant). The vector w and M_0 basis list are
archived in output/artifacts/cell_data.json. The auditor independently
re-ran the script (all checks pass up to the archiving path) and
independently recomputed minors, value distribution, exchange axiom,
separator scan, deletion identity, and relation count.

## Limitations

Single-cell fallback certificate only. No census of the Fano-type window,
no S_8-orbit enumeration, no non-realizability / foundation-morphism /
chirotope side, and no statement about other Dr(3,8) cones or the 23
Bendle et al. obstructed cones. The tropical Plücker / exchange /
connectedness checks are machine-verified, not hand-proved. The all-INF
octahedra convention follows Speyer's thesis convention (unsupported
octahedra impose no condition); the claim does not depend on excluding them.

## Reproducibility

- Matrix A as above over F_2(t), t-adic valuation.
- Scripts: output/artifacts/verify_dressian_cell.py (verifier),
  output/artifacts/cell_data.json (archived w and bases).
- Environment: any Python 3 stdlib, < 1 s.

## References

- Herrmann–Joswig–Speyer, Dressians, Tropical Grassmannians, and Their
  Rays. https://arxiv.org/abs/1112.1278 — whole fan Dr(3,8); rays/rigidity;
  no per-cell realizability verdicts.
- Bendle–Böhm–Ren–Schröter, Parallel Computation of tropical varieties,
  their positive part, and tropical Grassmannians.
  https://arxiv.org/abs/2003.13752 — TGr_0(3,8); 23 cones obstructed by a
  different computational method.
- Baker–Lorscheid, Foundations of matroids I.
  https://arxiv.org/abs/2008.00014 — general foundation/pasture theory.
- Baker–Lorscheid–Zhang, Foundations of matroids Part 2.
  https://arxiv.org/abs/2310.19952 — minimal building-block list.
- Speyer–Sturmfels, The Tropical Grassmannian.
  https://arxiv.org/abs/math/0304218 — background; G(3,6) worked example.
