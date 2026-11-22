# Self-review

## Correctness — PASS

The theorem's objects are the 27 geometric lines of any smooth characteristic-zero cubic surface and their five-singular-fiber conic pencils. The standard six-point blow-up classes yield all lines and their intersection numbers, and every center line has ten neighbor components in five pairs. Each column has even formal degree and Picard image \(5(-K_S-[\ell])\). The adjacency matrix has parameters \((27,10,1,5)\), identity \(A^2=5I-4A+5J\), eigenvalues \(10,1,-5\) with multiplicities \(1,20,6\), and determinant \(2\cdot5^7\). The independently surjective parity/Picard-mod-five map has an index of exactly \(2\cdot5^7\), proving image equality. The package's standard-library verifier reconstructs and independently checks every finite incidence and determinant step. Exact SymPy Smith normal form separately agreed. The argument does not infer general geometry merely from sampled surfaces.

## Originality — PASS, with historical priority risk

Casalaina-Martin–Grushevsky–Hulek, arXiv:2312.15369, §3.2, provide the five-fiber geometric marking but not the integral support-image criterion; their principal statements concern moduli cones. Published spectrum data for the complement of the Schläfli graph determine rational eigenvalues, not by themselves the integral Picard-congruence equality. Özçelebi (2012), §6.3, analyzes generalized-quadrangle non-collinearity graphs, a different integer adjacency map. The closest published tritangent and double-six integral incidence results concern respectively 45 three-line supports and 36 twelve-line supports, not these 27 ten-line supports; none of their stated implications determines the present parity-and-Picard congruence test. Repeated semantic searches for conic-pencil support lattices, Schläfli collinearity Smith forms, equivalent graph parameters, and invariant factors found no covering claim. A potentially equivalent older graph-Smith computation remains a specific priority risk; this review is not a claim of exhaustive historical uniqueness.

## Mathematical value — PASS

A conic-bundle marking has five singular fibers, and each line's entire exceptional-component support is geometrically canonical. Integral reconstruction from these 27 supports is a natural finite-level question, not an arbitrary selected submatrix: the answer gives both an effective coordinate-free membership test and a sharp, nontrivial tenfold obstruction. It separates a parity condition from seven independent Picard-mod-five conditions and strengthens a known rational graph spectrum to an exact integrality theorem. It supplies a reusable arithmetic-lattice constraint for calculations on marked cubic-surface configurations, without claiming a separate downstream theorem.

## Boundaries and residual risks

The conclusions concern formal line supports, not actual Picard torsion or arithmetic descent. Positive characteristic has not been asserted. Old finite-geometry and association-scheme literature might contain an equivalent integral calculation. An independent external audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
