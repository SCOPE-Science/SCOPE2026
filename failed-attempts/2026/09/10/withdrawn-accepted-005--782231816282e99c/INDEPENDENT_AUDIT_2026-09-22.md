# Independent audit — SCOPE-20260910-005

## Scope
Independent review of `2026/09/10/005` at tree `c0fa96814611dbfe3dc06d79c7c4448bd53b37f1`.

## Correctness
**FAIL as a complete research claim.** The local differential calculations are sound: on `M`, direct differentiation recovers the displayed gradient, Levi matrix, tangential block `diag(1,0)`, winding rates `(1,2)`, and coefficients `c1=-i/conj(w)` and `c2=e^(3it)`.

The problem is the advertised conclusion. Nonvanishing of `c1` and `c2` in the chosen frame does not by itself prove that the Diederich–Fornaess boundary problem is an irreducible coupled `2x2` system or that a scalar/slice reduction is impossible. The package gives neither the full transformed boundary inequalities nor an invariant obstruction under admissible changes of tangential/normal frame. The verifier checks the coefficients and their nonvanishing; it does not check the claimed irreducibility theorem.

## Originality
**PASS only narrowly for the exact engineered coefficient tuple.** Recent higher-dimensional worm literature already provides broad constructions with prescribed codimension and D'Angelo winding data, so the scientific novelty cannot be the existence of a higher-dimensional winding pattern itself.

## Scientific value
**FAIL.** Once the unsupported irreducibility/no-slice conclusion is removed, the package supplies a direct local differentiation table for a bespoke defining function. It proves no Diederich–Fornaess index bound, no global pseudoconvex-domain theorem, and no invariant PDE obstruction.

## Literature checked
- B. Liu, *The Diederich-Fornaess index I: for domains of non-trivial index*, arXiv:1701.00293.
- S. Calamai, G. M. Dall'Ara, *Higher dimensional worm domains*, arXiv:2410.08736 / Bull. London Math. Soc. 57 (2025).
- S. G. Krantz, M. M. Peloso, C. Stoppato, *On a higher dimensional worm domain and its geometric properties*, arXiv:2406.04905.

## Disposition
**FAILED.** Relocate the complete package atomically. A future salvage would need a rigorous invariant reduction/obstruction theorem (or a genuine DF-index/global-domain result), not only pointwise nonzero coefficients.
