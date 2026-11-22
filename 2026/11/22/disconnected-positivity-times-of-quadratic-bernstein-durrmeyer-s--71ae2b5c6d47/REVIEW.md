# Mathematical review

## Correctness — PASS

For the unweighted quadratic Bernstein–Durrmeyer operator, direct polynomial-kernel integration gives the orthonormal shifted-Legendre eigenbasis with eigenvalues \(1,1/2,1/10\). The spectral-power kernel is therefore an explicit symmetric bivariate quartic. With \(r=|2x-1|\), \(s=|2y-1|\), and \(p=rs\), opposite signs minimize the linear product; \((1-r^2)(1-s^2)\ge0\) bounds the remaining quadratic and yields an exact lower quadratic \(Q_t(p)\). Every \(p\in[0,1]\) is attained at \(x=1\), \(y=(1-p)/2\), making the reduction an equality, not merely an estimate. The vertex \(5^{t-1}\) gives the two piecewise minimum functions. Concavity on \((0,1)\) and the unique stationary point on \((1,\infty)\) prove that their zero set has the stated two positive components. The degree-one case follows directly from its two eigenvalues. Boundary minimizers give genuine negative-kernel witnesses with nonnegative test functions supported near the boundary.

The standalone `VERIFY.py` reconstructs the polynomial kernels with exact rational arithmetic, checks the spectral basis and selected powered kernels, and tests stationary and boundary minima, with 31,260 assertions. The continuum and real-exponent claims are analytic theorems, not deductions from finite tests.

## Originality — PASS, qualified

Altomare (2019, §6, full text inspected in relevant part) studies integer iterates, positive Markov approximations and diffusion semigroups, not noninteger spectral powers of a fixed quadratic Bernstein–Durrmeyer operator. Guillot–Khare–Rajaratnam (2013, Theorem 1.6 and Corollary 2.3, full text read in relevant part) characterize positive entrywise powers of finite doubly nonnegative matrices; their finite-dimensional statement is not an equivalent theorem about continuum integral kernels of powered projections. The published *Spectral-power trace cancellation for Dirichlet Bernstein–Durrmeyer operators on simplices* (2026, full statement and proof read) concerns sums of spectral eigenvalues, whereas the present phenomenon concerns pointwise nonnegative kernels and has two disconnected permitted exponent intervals. Berdysheva–Jetter (2010) establishes related positive kernels and polynomial eigenstructure, but the fully relevant primary document was not accessible in this review and a historical spectral-power result cannot be excluded. The claim is distinguished by its precise quantifiers and by comparing implication rather than titles. Residual historical-priority uncertainty is expressly retained.

## Mathematical value — PASS

The minimal-degree classification identifies an obstruction to inserting a natural positive selfadjoint Markov averaging operator into a pointwise-positive spectral-power interpolation. Noninteger positivity disappears immediately after an integer iterate and reappears at a sharp later exponent. The exact transition values and explicit negative witnesses provide a meaningful boundary for positive-kernel interpolation in approximation and operator-semigroup theory. It is a complete exact classification of a canonical, low-rank nontrivial operator family, not an arbitrary parameter slice or a previously known eigenvalue table recast as a new theorem.

## Limits

The proved domain is the unweighted degree-two operator, plus a degree-one minimality comparison. The operator is noninjective and its spectral powers are not strongly continuous at zero on all \(L^2\). A separate study is needed for weighted, higher-degree or non-selfadjoint analogues. Independent expert or mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
