# Cap-lattice rigidity for the Sigma(2,3,11) cork closing: Q = <+1> perp E8 with certified SW-vanishing on the definite plumbing cap

## Context

The lane target was a Seiberg-Witten basic-class distinction for a fixed
Mazur-type cork twist pair (X, X_tau) with boundary Sigma(2,3,11), the
smallest Brieskorn boundary outside the triple treated by Cavallo
(arXiv:2605.15095: Sigma(2,3,13), Sigma(2,5,7), Sigma(3,4,5)). The first
witness route tested was the naive definite-plumbing closing
Xhat = C U N, where N = -P is the orientation reversal of the
negative-definite star plumbing P bounding the homology sphere. That route
fails (SW = 0 on both sides). This record hardens that failure localizer
into a positive, citable lattice-topology fact about the exact fixed cap,
plus the short-vector census and E8 identification explaining it.

## Definitions

- Y = Sigma(2,3,11), oriented as the Seifert manifold
  M(-2; 1/2, 2/3, 9/11), Euler number e = -2 + 1/2 + 2/3 + 9/11 = -1/66.
- P = negative-definite star plumbing with 9 vertices ordered
  (c0, a1, b1, b2, c1, c2, c3, c4, c5):
  central c0(-2); leg [2]: a1(-2); leg [2,2]: b1(-2)-b2(-2);
  leg [2,2,2,2,3]: c1(-2)-c2(-2)-c3(-2)-c4(-2)-c5(-3),
  i.e. the Hirzebruch-Jung expansions of 2/1, 3/2, 11/9.
- Q_P = 9x9 plumbing Gram matrix; N = -P with Q_N = -Q_P.
- C = C(2,3,11): fixed Mazur-type cork (one dotted 1-handle U plus one
  0-framed 2-handle K with lk(U,K) = +1; contractible balance sheet).
- Xhat = C U N (and its cork twist Xhat_tau): closed simply connected caps
  sharing the unimodular form Q_N (C contractible, Y a homology sphere).

## Result

For the fixed 9-vertex cap above:

1. **SW-vanishing on the naive cap.** The closed naive cap Xhat = C U N
   carries no Seiberg-Witten basic classes on either twist side: SW = 0
   identically. Each of the 9 cap spheres S_v is an embedded S^2 of genus
   0 with square +2 (x8) or +3 (x1), so the standard closed b2+ > 1
   adjunction inequality 2g-2 >= S^2 + |K.S| reads -2 >= S^2 + |K.S| >= +2,
   unsatisfiable for every spin-c structure K. Characteristic parity
   diag(Q_N) = (0,...,0,1) mod 2 forces K.S_{c5} = K_8 odd, so the last
   sphere gives RHS >= 3+1 = 4 (uniform margin >= 6).
2. **Short-vector census.** Q_N represents +1 by exactly one pair
   +-v0 with v0 = (6,3,4,2,5,4,3,2,1) (v0^2 = +1, integer-exact); there
   are exactly 240 square-+2 vectors and minimum nonzero square +1.
   Completeness for squares <= 2 is certified by the per-coordinate
   ellipsoid bound x_i^2 <= Q^{-1}[i,i]*S plus pruned recursion
   (independently closable by exact-rational LDL enumeration).
3. **Splitting and E8 identification.** Q_N v0 = e8 = (0,...,0,1) exactly,
   so v0 is primitive and its Q-orthogonal complement is literally
   span(e0..e7) with Gram G = Q_N[:8,:8], det(G) = +1 integer-exact,
   positive-definite rank 8. G is even (diagonal all 2s), symmetric,
   unimodular rank 8; its 240 norm-2 roots contain 8 with Gram exactly the
   E8 Cartan matrix E, and U = M_p^{-1} (det -1, integral) satisfies
   U^T E U = G integer-exactly. **Hence Q_N = <+1> perp E8.**

## Proof / evidence

- Machine-checked (sympy integer-exact): det(Q_P) = -1 (|H1(Y)| = 1),
  signature(Q_P) = -9, negative-definite; det(Q_N) = +1, signature +9,
  positive-definite.
- Adjunction: 9/9 cap-sphere violations machine-checked
  (adjunction.py / plumbing_result.json adjunction table).
- Census: ellipsoid-bound + Cholesky partial-norm pruned recursion gives
  counts {0:1, 1:2, 2:240} (short_vector.py); auditor closed the float
  soundness gap with an independent exact-rational LDL (Fractions,
  A = L D L^T, backward recursion) DFS confirming the same counts.
- Splitting: v0^2 = +1, Q_N v0 = e8, primitivity (gcd 1), det(G) = +1,
  positive-definite (splitting.py), all integer-exact.
- Isometry: 240 roots of G enumerated completely; 8 selected with
  M_p^T G M_p = E and U^T E U = G integer-exactly, det(U) = -1
  (e8_isometry.py).
- Master replay: `python3 output/artifacts/verify_emergent.py` replays all
  scripts and asserts every verification-critical fact, printing VERIFY_OK.

## Limitations / non-claims

- The Sigma(2,3,11) boundary identification is verified at the
  determinant / H1 / negative-definite / Euler layer; the full
  diffeomorphism to the Brieskorn link cites standard Seifert-plumbing
  theory. The explicit-matrix lattice identities are self-contained and
  unaffected.
- SW-vanishing uses the standard adjunction inequality for closed b2+ > 1
  manifolds (here b2+ = 9) plus simple type; no new SW computation is
  claimed.
- The M0-M4 Kirby schematic logs a twist-path template with
  determinant/H1 preservation; it does not realize tau as a diffeomorphism
  and is not claimed as the preset-fallback ribbon certificate.
- The symplectic-cap witness route (Milnor fiber M(2,3,11) plus
  concave/positive extension to b2+ > 1, with tau basic-set evaluation)
  is context with explicitly open steps; this record does not prove the
  lane target distinction.

## Reproducibility

From `output/artifacts/`, run `python3 verify_emergent.py` (requires
python3, sympy, numpy). It replays plumbing, cork-link, adjunction,
short-vector, splitting, E8-isometry, Milnor-cap/symplectic/homeomorphism
context legs and asserts: det(Q_P) = -1, sig -9/+9, cork det/H1 agreement,
9/9 adjunction violations, census {0:1, 1:2, 2:240}, v0^2 = 1,
Qv0 = e8, det(complement) = 1, U^T E U = G with det(U) = +-1 and 240 roots.

## References

- A. Cavallo, Mazur manifolds and symplectic structures, arXiv:2605.15095
  (covers only Sigma(2,3,13), Sigma(2,5,7), Sigma(3,4,5)).
- R. Chatterjee, M. Kegel, Contact surgery numbers of Sigma(2,3,11) and
  L(4m+3,4), arXiv:2404.18177 (contact structures; different question).
- Admission triage: Mukohara (instanton strong corks), Ladu
  (complexity-2 protocorks), Yasui (cork-to-concordance transfer) --
  different invariants/families, no cap-lattice certificate for this pair.
- arXiv live searches "Sigma(2,3,11) E8" and "Mazur cork E8": no results
  (checked 2026-09-09).
