# Scientific review: complete fifth-period census in an affine nilpotent-Jacobian family

## Correctness — PASS
The parameter reduction consists of two invertible polynomial coordinate changes, and the normalized map has an exact period-preserving correspondence with the planar recurrence \(F(a,b)=(b,a^2-b^2)\). The fifth-iterate fixed-point scheme has exact lexicographic Gröbner basis \(\{a-R(b),bQ_{15}(b)\}\), with a square-free degree-sixteen eliminant. Exact Sturm counting gives six real fifth-fixed points, five primitive. Since period five is prime, the other ten complex fifth-fixed points form exactly two additional primitive cycles, interchanged by conjugation. The fraction-arithmetic return-matrix enclosure proves one multiplier in \((0,1)\) and one below \(-1\) for the real orbit; the third is zero. `CHECK.py` recomputes the polynomial ideal and rational root and multiplier certificates. No infinite-orbit extrapolation is used.

## Originality — PASS within the inspected sources
The 2006 work of Chamberland studies precisely the simplest planar recurrence, but does not give its fifth-period enumeration. The 2022 arXiv paper of Castañeda and Rebollo-Perdomo (Remark 3.2) **already announces existence** of a five-cycle using Gröbner elimination; this fact is explicitly excluded from the originality claim. It does not give the total complex/real fifth-period census or the hyperbolic saddle classification. A 2026 published mathematical record supplies a sharp four-cycle degree threshold for the same nilpotent-Jacobian family, not the fifth-period census. Published findings on multiple three-cycles concern different polynomial degrees/periods. The remaining publication-priority risk is an unindexed equivalent enumeration or an expanded inaccessible 2024 journal version.

## Value — PASS
This is the first nontrivial prime-period census beyond the already-known three-cycle in the most elementary polynomial example, a case singled out by its original authors as displaying complicated dynamics. The result distinguishes existence from **uniqueness over the reals**, gives the full complex orbit structure, and determines the real cycle's saddle nature, despite pointwise nilpotent Jacobians. The coefficient-independent outcome and contrast with the known absence of period four reveal a genuine period-spectrum structure, rather than merely another numerical periodic witness. The result does not claim a classification of all periods.

## Limitations
Only period-five points are classified. The 2006 and 2022 sources had already established the map and the existence of other periods. The 2024 journal version of the source paper was not separately read; the lawful 2022 arXiv full text was inspected. The exact checker uses SymPy to construct a Gröbner basis and Sturm isolations, followed by rational interval arithmetic. Unindexed equivalent results cannot be ruled out absolutely.

Self-review: passed. Independent audit: not yet performed.
