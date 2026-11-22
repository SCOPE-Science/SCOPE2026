# Scientific review

## Correctness — PASS

The claimed object is the reduced normal-crossings divisor formed from all 45 strict line transforms and 201 exceptional curves of the classical complex Wiman arrangement. The proof accounts for all 990 original line pairs and the 120 triple, 45 quadruple and 36 quintuple points. It verifies that all 45 lines remain distinct modulo 19 and that the characteristic-19 reduction also has 201 distinct intersection points. The historical complex 201-point census therefore excludes any incidence loss under reduction, justifying the use of the finite graph as a certificate of the complex one. The resulting 246-vertex, 720-edge graph has genus 475 and no unstable components.

The standalone checker reconstructs every edge, proves the five block spectral identities as integer-matrix identities, derives the whole Laplacian characteristic polynomial, checks the 44-by-44 integer Schur cofactor by fraction-free elimination, and computes local Smith valuations at all six primes dividing the tree count, with four different roots. Every factor, valuation sum, integer divisibility and group order agrees. The Néron interpretation is expressly conditional on regular split semistable smoothing with unit node thickness, as in the standard component-group correspondence.

## Originality — PASS (historical-priority risk remains)

Bauer et al., arXiv:1407.2966, §4.2 and arXiv:1609.08648, §2.3, determine the original Wiman line equations and singularities, not the integral critical group of the full resolved boundary. Innamorati, doi:10.3390/axioms13050321, §5, studies an associated characteristic-19 configuration, not its 246-vertex integral Laplacian. An earlier complete Wiman-boundary Frobenius/zeta classification gives rational point and genus data, but does not compute this integral geometric critical group; zeta data do not determine Smith factors. The existing quintuple-only 81-vertex incidence construction excludes 165 other singular-point components and 540 graph edges, and does not imply the full-group result. The general Néron component-group theorem in Bosch–Lütkebohmert–Raynaud gives an interpretation, not the exceptional Smith form. Targeted searches under Wiman, Valentiner, graph critical group, component group, Smith form, spectrum, spanning trees and the specific incidence parameters revealed no stronger matching statement. Search non-detection does not establish absolute priority; an unindexed graph calculation remains possible.

## Mathematical value — PASS

The entire singular-point resolution is the geometrically canonical stable curve boundary of an exceptionally symmetric reflection-line arrangement. The complete integral group is not recoverable from the classical 201-point census, arithmetic genus or rational spectrum. The decomposition reveals six distinct prime supports, including 7-, 19- and 47-primary torsion and two different high 3-primary valuations. It supplies an exact degeneration invariant for Jacobians under the stated standard geometric hypotheses and an independently useful integral refinement of the symmetry-reduced Laplacian polynomial. No arbitrary graph deletion or ad hoc parameter selection is involved.

## Sources and limits

Primary source material read: Bauer et al., arXiv:1407.2966, §4.2 and line equations; Bauer et al., arXiv:1609.08648, §2.3 and Valentiner generator formulas; Innamorati, doi:10.3390/axioms13050321, §5; Bosch–Lütkebohmert–Raynaud, *Néron Models*, §9.6, component-group comparison. The finite arithmetic proof is reproducible with `verify_wiman.py` (Python 3 and NumPy). The group does not purport to classify unrelated arrangements, changes of node thickness, or general arithmetic forms, and independent review remains needed.

Self-review: passed. Independent audit: not yet performed.
