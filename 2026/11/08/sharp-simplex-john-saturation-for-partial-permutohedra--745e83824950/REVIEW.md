# Review of the partial-permutohedron simplex-John saturation theorem

## Correctness — PASS

The result specifies all integer parameters and proves the sharp positive regime. The known facet description of the partial permutohedron is combined with a directly derived support formula for the simplex John ellipsoid. The support inequalities reduce at the worst dimension to the exact nonnegative integer factor \((s-1)(n-s)\); strict failure in the complementary range reduces to \((m-1)(n-m)>0\). The ellipsoid determinant and all facet-contact equality cases follow from its explicit shape matrix. The included standard-library checker executes 110526 exact-rational checks. The finite checks corroborate but do not replace the proof.

## Originality — PASS (provisional historical priority)

Behrend et al., arXiv:2207.14253, supply the polytope, its vertices, and subset facets; these are prerequisites, not new claims. Liu–Zhang, arXiv:2607.03854, prove Ehrhart magic positivity and coefficient properties, not the present geometric ellipsoid saturation. The classical John ellipsoid of a simplex supplies the candidate, but not its simultaneous inclusion in all partial-permutohedron facet halfspaces. Accessible related geometric records give Euclidean inballs or minimum-volume **enclosing** ellipsoids; those optimization problems cannot imply an exact maximum-volume **inscribed** ellipsoid classification without additional information. Targeted title-, synonym-, and implication-based searches identified no direct stronger theorem. Full historical priority is not independently established.

## Mathematical value — PASS

Partial permutohedra are a canonical two-parameter family of lattice polytopes with exponentially many subset facets. The sharp threshold \(m=n\), the strict failure immediately below it, the exact maximum-volume ellipsoid in an unbounded parameter regime, and the change from \(m+1\) to \(2m+1\) tangencies identify a nontrivial structural phenomenon: all additional facet truncations become invisible to the John ellipsoid beyond a finite dimension. The original claim is not merely the classical ellipsoid formula for a simplex; the central result is its sharp survival under the nontrivial partial-permutohedral cuts.

## Sources and limitations

Primary references: Behrend et al., *Partial permutohedra*, arXiv:2207.14253, Proposition 2.8 and Sections 2–3, 5; Liu and Zhang, *Magic Positivity for the Ehrhart Polynomials of Partial Permutohedra*, arXiv:2607.03854 (July 4, 2026); Lin–Ge–Leng, *The John Theorem for Simplex*, arXiv:1001.4223; Eydelzon, arXiv:2609.08045. Non-saturation ellipsoids are not classified. Possible aliases under anti-blocking permutohedra and polymatroids remain a historical-priority risk. The assertions have not undergone independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
