# Self-review of the nine-line two-nodal quartic chamber distribution

## Correctness: PASS
For the blow-up of five distinct complex plane points with exactly the two stated triple-point lines, the Bézout inequalities force every negative curve beyond the exceptional divisors and the two root curves to be a cross-pair line. Together, adjunction and anticanonical nefness exclude other negative curves; there are nine \((-1)\)-curves and two disjoint \((-2)\)-curves. For selected disjoint \((-1)\)-curves, the matrix Schur complement \(2I-MM^{T}\) gives necessary and sufficient restrictions on the allowed root curves. These restrictions reduce the chamber count to the finite combinatorial sum in `RESULT.md`. Two exact methods (all \(2048\) subsets via principal minors and a separate incidence-graph count) agree on every coefficient, giving \(221\) chambers, \(80\) root-free and \(141\) root-containing. Bauer--Schmitz's volume theorem identifies the latter as infinite-volume chambers; the root-free blow-downs retain nef and big anticanonical class and have bounded nef slice. The geometric exhaustiveness proof is essential; a finite computer census is not by itself a proof that no other negative curves exist.

## Originality: PASS, with historical-priority qualification
The smooth quartic count of \(393\) is already due to Bauer--Funke--Neumann; their general correspondence is part of the proof, not a new contribution. Bauer--Schmitz already established the volume dichotomy. Derenthal distinguishes the nine-line and eight-line quartic \(2A_1\) types, but the inspected table does not give the bivariate Zariski-chamber polynomial. The assessed claim is exactly the nine-line \(2A_1\) distribution \(F(t,u)\), the \(80/141\) volume split, and the \(33\) simultaneous-root supports. Searches under Zariski-chamber, negative-definite support, two-nodal quartic, nine-line, and numerical aliases found no dominating statement in inspected primary material or accessible prior research claims. An inaccessible older thesis and unlocated specialist tables remain explicit priority risks; no uniqueness certificate is claimed.

## Mathematical value: PASS
The negative-support polynomial is a complete natural invariant of the chamber decomposition of the simplest weak quartic del Pezzo type with two disjoint exceptional roots. It quantifies the structural change from the smooth \(393\)-chamber surface and from one-root degenerations, while distinguishing single-root from simultaneous-root supports. The number \(33\) is the interaction term of the two roots, not an arbitrary subfamily selection. The finite/infinite distinction measures a natural geometric volume invariant and requires the established finite-volume criterion.

## Closest literature and limitations
- Bauer--Funke--Neumann, *Counting Zariski chambers on Del Pezzo surfaces* (arXiv:0912.0958): negative-definite-support correspondence and \(393\) chambers for the **smooth** quartic type. The present surface has two root curves and only nine lines.
- Bauer--Schmitz, *Volumes of Zariski chambers* (arXiv:1205.3817): the general volume test, which implies but does not numerically count the \(80/141\) distribution.
- Derenthal, *Singular del Pezzo surfaces whose universal torsors are hypersurfaces* (arXiv:math/0604194), Table 6: distinct nine-line and eight-line quartic \(2A_1\) types, but no inspected chamber-count table.
- Bauer--Schmitz, *Zariski chambers on surfaces of high Picard number* (arXiv:1204.4373): alternative general chamber machinery, not a direct numerical enumeration of this surface.

The result is for ordinary complex blow-ups under exactly two specified triple collinearities. It does not enumerate the other quartic \(2A_1\) type, all singular configurations, or individual chamber volumes. Additional specialist literature may contain the same numerical invariant. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
