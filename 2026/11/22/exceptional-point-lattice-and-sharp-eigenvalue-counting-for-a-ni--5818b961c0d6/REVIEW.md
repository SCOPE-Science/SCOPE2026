# Review of the exact factorial-shift rank-one spectral law

## Correctness — PASS

The operator and functional are bounded by factorial decay and square-summable coefficients. The rank-one resolvent gives the entire equation \(e^z-1-z=\alpha^{-1}\) exactly. A contour trace identity equates algebraic multiplicities with orders of scalar zeros, yielding only double points at nonzero imaginary integer multiples of \(2\pi\). Direct logarithmic contraction controls *all* large roots, not merely a selected subset, proving the bounded-remainder counting law and the critical eigenvalue-modulus sum. Positivity of all coefficients starting at degree two proves the unique positive maximal-modulus eigenvalue and the real weak-coupling asymptotics. The standalone checker passed 186 finite diagnostics; no infinite statement relies solely on testing.

## Originality — PASS, with explicit priority risks

The 2018 Tcaciuc example is the closest structural precursor: it uses the same shift but a rank-one direction with nonzero zeroth coefficient and characteristic function \(e^z-1\), including one nonzero exceptional quasinilpotent coupling. Changing to a nilpotent rank-one direction forces \(e^z-1-z\) and produces a different complete coupling bifurcation, a defective Jordan lattice, a bounded-error spectral counting law, and split real weak-coupling scales. The 2026 Bračič–Kandić paper establishes generic infinite-component results and square-zero directions for summable shift weights, but does not imply the exact spectral invariant, the exceptional-point classification or the counting coefficient here. The inspected literature and independent mathematical-record comparisons did not reveal a covering theorem. Residual risk is that the same scalar exponential-minus-linear root analysis may occur in older, unindexed operator examples; lack of a search hit is not proof of priority.

## Mathematical value — PASS

The object is a canonical factorially damped quasinilpotent unilateral shift with the minimal alteration of the classical perturbation needed to impose \(F^2=0\). A complete exact spectral description answers how the removal of the exceptional quasinilpotent coupling interacts with algebraic multiplicity and eigenvalue accumulation. The countable Jordan-exceptional set accumulates at zero perturbation norm; its sharp \(1/(\pi r)\) eigenvalue counting coefficient matches the Schatten threshold of the operator. The unique dominant positive eigenvalue has a singular logarithmic weak-coupling scale distinct from the negative branch. These are motivated operator-theoretic invariants, not merely a numerical or parameter substitution exercise.

## Sources and residual limits

Directly inspected: Bračič–Kandić (arXiv:2611.12208v1), §6 including Lemmas 6.1–6.2 and Theorems 6.3–6.4; Tcaciuc (arXiv:1805.03277), §2 including Lemma 2.1, Proposition 2.4 and the explicit factorial shift example. Lambert W branch documentation supports the optional formula, not scientific priority. An older exact equivalent for this particular nilpotent direction remains possible; no claim is made about general rank-one perturbations or eigenvector completeness.

Self-review: passed. Independent audit: not yet performed.
