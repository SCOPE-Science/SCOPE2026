# Scientific review: optimal Bernstein–Durrmeyer diffusion clock

## Correctness — PASS

The selfadjoint finite-rank Bernstein–Durrmeyer kernel and the Legendre differential operator are diagonal in the same complete orthonormal basis. The eigenvalue product is independently obtained from beta moments and the leading coefficient of the polynomial action. Applying the exact \(\operatorname{artanh}\) identity proves the minimum integer clock and positive spectral error. A two-region bound on this error dominates it by the summable diagonal \(4h_k^2e^{-h_k}/(n+1)^2\); fixed-mode Taylor expansion plus dominated convergence proves the asserted trace-class limit. The fixed-offset first-order limit follows from the same summable domination. A separate finite computational check confirms 148 assertions but is not used as an infinite proof.

## Originality — PASS, with residual priority risk

The primary literature has been compared by mathematical implication. Altomare (2019, published online 4 January 2019) gives semigroup approximation by Markov iterates in strong/uniform function senses, not the stated spectral order, smallest integer clock, or second-order trace-norm operator limit. Abel–Berdysheva (2010) provides the eigenvalues and complete **single-step** expansions: these are expressly treated as prior results, not newly discovered formulas. The separate public research record *Spectral-power trace cancellation for Dirichlet Bernstein–Durrmeyer operators on simplices* concerns fixed real powers and high-degree traces, rather than powers with the iteration index of size \(n\) and their trace-distance from Legendre heat. Inaccessible older papers about quantitative convergence of genuine/ultraspherical Durrmeyer iterates may contain related operator approximation estimates; their full texts could not be compared, so priority is qualified, not guaranteed. The full new conjunction has not been identified in the inspected literature.

## Mathematical value — PASS

The standard approximation problem is determining the time-step count to approximate the diffusion semigroup. This result identifies the **exact smallest** integer count providing one-sided spectral approximation and demonstrates a non-obvious cancellation of the usual first-order bias. The limit determines all asymptotic eigenmode errors at once in the stronger trace-class topology, gives a finite-degree universal order bound and sharp trace/operator constants, and proves that no other fixed integer offset has the same second-order accuracy. The natural parameter is the iteration clock, not an arbitrary slice or a tabulated invariant.

## Closest sources and limitations

- F. Altomare, *Iterates of Markov Operators and Constructive Approximation of Semigroups* (2019), https://doi.org/10.33205/cma.491601 , entire manuscript including semigroup-iteration section inspected.
- U. Abel and E. Berdysheva, *Complete asymptotic expansion for multivariate Bernstein–Durrmeyer operators and quasi-interpolants* (2010), journal full-text mirror inspected for eigenvalue formulas and expansion theorem.
- H. Gonska, M. Heilmann and I. Raşa, *Convergence of iterates of genuine and ultraspherical Durrmeyer operators to the limiting semigroup: C²-estimates* (2009), https://doi.org/10.1016/j.jat.2008.11.002 , abstract only; full text unavailable, so specialized overlap is a residual risk.
- F. Altomare, M. Cappelletti Montano and V. Leonessa (2019), https://doi.org/10.3934/cpaa.2019017 , abstract only due to restricted full text.
- T. Hirano and R. Namba, *Iterates of multidimensional Bernstein-type operators and diffusion processes in population genetics* (2023), https://arxiv.org/abs/2310.13983 , full-text introduction and central convergence statements inspected; this treats Bernstein rather than the classical selfadjoint Durrmeyer family.

This is a self-contained result for the unweighted one-dimensional classical family only. Exact original eigenvalues are known; no novelty is claimed for them. No independent external validation has occurred.

Self-review: passed. Independent audit: not yet performed.
