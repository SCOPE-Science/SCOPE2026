# Scientific review — centered-cell Bernstein comparison

## Correctness — PASS

The proof establishes the pointwise Lipschitz norm using a single continuous interlacing spline with slopes of absolute value one. This supplies an exact common dual witness, rather than inferring equality from a transport upper bound. Jensen's inequality is applied separately at every binomial atom; positivity at interior arguments and the equality criterion for absolute value give the full pointwise minimizer classification. The globally admissible kernel \(\nu_x=\delta_x\) is weakly continuous. The De Moivre binomial mean absolute deviation formula yields finitely many beta-monomial peaks, whose symmetric products have a strictly log-concave factor, proving the parity-sensitive global maximum. Stirling's formula gives the asymptotic coefficient. Boundary cases \(n=1\), \(x=0\), and \(x=1\) are included.

The independent rational CDF calculation, exact common-spline evaluation and all-cell peak comparisons in `verify_jitter.py` passed. Finite tests corroborate but are not relied upon for the universal quantifiers. The theorem is limited to common cell-jitter distributions independent of the binomial index.

## Originality — PASS, qualified

The binomial mean absolute deviation identity itself is classical (explicitly credited to De Moivre by Berend–Kontorovich, 2013). The already known neighboring-degree Bernstein bound is also acknowledged as the Bernoulli-mixing special case, not presented as new. The comparison targeted is the precise *minimax over all weakly continuous mean-preserving cell jitter kernels*, with simultaneous global extremizing function, all pointwise minimizers and the parity-dependent optimal rate. Full-text inspection of Altomare et al. (2016) revealed the generalized Kantorovich construction and approximation and preservation estimates, not the stated minimax. Gonska–Piţul–Raşa (2006) and the Acu–Hodiş–Raşa survey (2018) cover operator-difference modulus bounds rather than this sharp constrained optimization. Relevant searchable research records likewise did not reveal a stronger claim. This is evidence for provisional originality, not a proof of absolute historical priority. Acu–Raşa (2016) was only accessible in publisher preview and surveyed forms; this remains a specific priority risk.

## Mathematical value — PASS

Affine-preserving positive refinements of Bernstein approximation are a standard, motivated class. The exact best perturbation of a fixed binomial sampling law is a complete natural optimization, not an arbitrary finite parameter value. The common extremizer shows that an apparently naive cellwise transport coupling is globally sharp for every admissible law. The full equality classification identifies *every* optimal mixing measure pointwise; the odd/even maximizer change is mathematically forced by strict log-concavity. The optimal \(n^{-3/2}\) Lipschitz discrepancy improves the \(n^{-1}\) scale of common Bernstein–Kantorovich and neighboring-degree perturbations. No conjecture about operators outside the specified class is inferred.

## Closest sources and remaining limits

Berend–Kontorovich, *Statistics & Probability Letters* 83 (2013), 1254–1259, DOI 10.1016/j.spl.2013.01.023; Altomare–Cappelletti Montano–Leonessa–Raşa, arXiv:1605.06768 (2016); Gonska–Piţul–Raşa, *Carpathian J. Math.* 22 (2006), 65–78; Acu–Hodiş–Raşa, *Constructive Mathematical Analysis* 1 (2018), 113–127, DOI 10.33205/cma.478408. An incomplete comparison with Acu–Raşa, *Numerical Algorithms* 73 (2016), DOI 10.1007/s11075-016-0117-8 remains disclosed. The binomial MAD formula is prior work, and an equivalent optimization could exist in older approximation theory under different terminology. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
