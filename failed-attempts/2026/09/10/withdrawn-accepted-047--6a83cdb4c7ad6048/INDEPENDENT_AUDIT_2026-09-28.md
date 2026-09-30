# Independent Audit — 2026-09-28

**Record:** `2026/09/10/047`  
**Title:** Braid-orbit census for (2,3,7) tuples in PSL(2,7) and PSL(2,8)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0d136e5e73afef0242270b3c2cfd3b5c6c7abf72`  
**Disposition:** **FAILED**

## Independent checks

- Rebuilt PSL(2,7) over F7 and PSL(2,8) over F8 from 2×2 determinant-one matrices and independently enumerated exact element orders.
- Enumerated all ordered (2,3,7) pairs and ran pure Hurwitz BFS using squared braid generators; obtained the filed counts exactly.
- Compared raw tuple orbits with simultaneous-conjugation quotient sizes and with current Macbeath-Hurwitz literature on outer equivalence.

## Three-axis assessment

- **Correctness — FAIL**: The finite-group enumeration itself survives independent reconstruction: |PSL(2,7)|=168 and |PSL(2,8)|=504; there are respectively 336 and 1512 ordered (2,3,7) pairs, and pure Hurwitz moves give raw-tuple orbit sizes 168+168 and 504+504+504. The record then over-identifies these raw tuple orbits with Hurwitz-space/Galois-orbit degrees. Because every generating tuple has trivial simultaneous-conjugation stabilizer, each 168- or 504-element fiber is one inner Nielsen class after quotient by Inn(G), so 168 and 504 are conjugation-orbit sizes (also regular-cover degrees), not degrees of Hurwitz-space components. The q=8 three class fibers are additionally fused by outer/field automorphisms; current Macbeath-Hurwitz literature describes the q=8 map as unique. Thus the headline geometric interpretation and slogan are not valid as written.
- **Originality — UNRESOLVED**: The exact raw enumeration may be useful computational data, but the literature already treats Macbeath-Hurwitz maps and their automorphism/outer-automorphism identifications. The audit did not find a source tabulating the exact 336/1512 raw pair counts, yet absence of a table does not establish novelty, and the claimed “Galois-orbit degrees” are not a new invariant once the quotient convention is corrected.
- **Scientific Value — FAIL**: The reproducible finite-group census has some benchmark value, but the record’s stated payoff is the Hurwitz-space/component/Galois interpretation. That payoff is conventionally wrong or at least materially underspecified (inner versus absolute/outer equivalence), and the reported 168/504 “component degrees” conflate tuple-conjugacy orbit size with Hurwitz moduli degree. The package therefore should not remain a validated finding without a substantive rewrite.

## Findings

- Current main tree equals the assigned tree SHA.
- Independent finite-field reconstruction reproduced group sizes 168 and 504, ordered-pair counts 336 and 1512, and pure-braid raw orbit partitions [168,168] and [504,504,504].
- Each generating-tuple simultaneous-conjugacy orbit has size |G|, so each fixed order-7-class raw fiber collapses to one inner Nielsen class.
- The statement that 168/504 are Hurwitz-component or Galois-orbit degrees is unsupported; for q=8, field/outer automorphisms fuse the three order-7 classes and the Macbeath-Hurwitz map is described as unique.

## Sources compared

- Repository record 047 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/047/RESULT.md — Contains the raw orbit census and the disputed Hurwitz-space/Galois interpretation.
- Fried, Hurwitz space components; and the Coleman–Oort Conjecture (2025): https://arxiv.org/abs/2509.08904 — States that Hurwitz-space components are braid orbits on Nielsen classes and explicitly distinguishes equivalence conventions such as inner and absolute.
- Jones, Regularity properties of Macbeath-Hurwitz and related maps and surfaces (2025): https://arxiv.org/abs/2505.02089 — For q=p^3 with p≡±2,±3 mod 7, describes the Macbeath-Hurwitz map as unique; q=8=2^3 is in this case.
- Top–Verschoor, Counting points on the Fricke–Macbeath curve over finite fields (2018): https://doi.org/10.5802/jtnb.1019 — Provides standard genus-7/PSL2(8) Fricke–Macbeath context; the curve is a single isomorphism class, not three curves of degree 504.

## Limitations

- The audit does not reject the finite-group enumeration; it rejects the passage from that enumeration to the stated moduli/Galois conclusion.
- A repaired version could be publishable if it explicitly fixes inner versus absolute equivalence and reports raw, inner, and outer-quotient orbit sizes separately.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
