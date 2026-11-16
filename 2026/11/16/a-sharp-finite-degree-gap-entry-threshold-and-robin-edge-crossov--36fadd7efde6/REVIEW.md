# Scientific review

## Correctness

**PASS.** A two-step elimination gives the exact Chebyshev formula for every even degree. Its roots coincide with eigenvalues of a real symmetric tridiagonal matrix carrying one negative diagonal boundary defect. Rank-one interlacing permits at most one left exterior Chebyshev root, and the exact characteristic value at \(-1\) fixes the threshold at \(\sqrt{c/b}=1+1/k\). A hyperbolic ratio inequality guarantees the resulting two roots in the original variable are real, nonzero, and strictly inside the bulk gap. The trigonometric and hyperbolic root equations yield the two critical scaling branches by monotone, locally uniform limits. The degree and parameter quantifiers and all equality cases are addressed in the proof. The supplied checker gives exact finite-degree recurrence identities and independent numerical tests, not an infinite certificate.

## Originality

**PASS relative to the inspected sources; historical priority is provisional.** The precise recurrence is Proposition 15 of Barry's 2026 Sprugnoli paper; its recurrence, bulk spectrum and orthogonality are not new. Simon's 2004/2006 theory determines fixed periodic Dirichlet zeros and general band counting, but the inspected Theorems 2.1 and 2.3 do not state the exact finite-even-degree gap-entry parameter \((k+1)/k\) or the varying-coefficient critical transition. Peherstorfer's multi-interval treatment provides general gap-zeros theory without stating this recurrence's explicit degree-dependent threshold or the cotangent/coth scaling transition in the inspected material. A 1991 Peherstorfer paper on periodic recurrence coefficients was accessible only by bibliographic metadata, while a 2004 elliptic-case study was accessible only by abstract. Both remain originality risks. General boundary-defect Chebyshev identities may be equivalent under a different terminology and also remain a priority risk. Cross-comparisons focused on implications, not just titles.

## Value

**PASS.** An exact degree-by-degree band-to-gap zero classification is a natural invariant of periodic orthogonal polynomials and of finite Jacobi compressions. The \(1/k\) critical parameter is sharp, and the \(k^{-2}\) two-branch transition gives an interpretable continuum limit connecting band-side and gap-side roots. This addresses a nontrivial spectral-boundary question not determined by a generic periodic zero-density theorem; it is not a decimal refinement or isolated numerical experiment.

## Limits

This is a special explicit period-two family, not an arbitrary periodic Jacobi model. The outcome tracks the root closest to zero (by squared value) in the varying-parameter regime; it does not describe full limiting eigenvectors. An equivalent older finite Jacobi boundary-defect calculation cannot be ruled out. A complete independent mathematical audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
