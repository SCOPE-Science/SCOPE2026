# Review of the sharp second-Specht projection theorem

## Correctness — PASS
The degree-\(n(n-3)/2\) Specht constituent is isolated by subtracting the trivial and standard modules from the two-subset permutation representation. The resulting character \(\chi(g)=F(g)(F(g)-3)/2+T_2(g)\) is negative exactly for \(F\in\{1,2\}\) and \(T_2=0\), with negative value \(-1\). Orthogonality converts its absolute mean to twice the probability of this event; class counting yields \(2q_{n-1}+q_{n-2}\). The central character idempotent has precisely this row \(\ell^1\)-norm multiplied by its degree. Averaging arbitrary projections over left and right regular translations proves minimum norm, not merely the canonical projector's norm. The cycle exponential generating function gives the finite formula, limit, and explicit Cauchy-tail bound. Full exact-rational enumeration for \(n=4,5,6,7,8\) and the forbidden-cycle recurrence up to \(m=14\) support, but do not substitute for, these all-\(n\) arguments.

## Originality — PASS, qualified
The primary texts of Wildon (arXiv:math/0612292), Diaconis–Fulman–Guralnick (arXiv:0708.2643), and Scarabotti–Tolli (arXiv:math/0701533) were compared at the level of their main relevant statements and material. They supply the classical character decomposition, pair fixed-point statistics, and Fourier projections, respectively, but not the evaluated sharp norm and full norming classification for the regular \((n-2,2)\) block. The closest indexed calculations concern the standard Specht character on the full group or the second Johnson spherical projector on a different homogeneous space. There is no implication from those exact endpoint constants to the present absolute \(\chi^{(n-2,2)}\) sum without the sign-support analysis. Targeted external searches and similarity-search comparisons did not produce a covering result. Residual risk: an unindexed character \(L^1\) table or general-representation formula might encode the same evaluated number.

## Value — PASS
For a natural next irreducible layer following the standard permutation representation, the result gives the exact minimum projection norm in every dimension, a complete norming-input classification, and a short-cycle-avoidance model whose asymptotics can be controlled extremely sharply. This reveals genuine quadratic rather than linear endpoint amplification and supplies a new closed-form invariant, not an arbitrary finite slice or a known character table recomputation. The general character and idempotent formulas themselves are prior knowledge and are not claimed as new.

## Closest literature and limitations
The theorem is restricted to the full matrix-coefficient block and endpoint supremum norm, and it is a self-review, not an independent verification. See the cited primary works and the explicit bibliographic risk in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
