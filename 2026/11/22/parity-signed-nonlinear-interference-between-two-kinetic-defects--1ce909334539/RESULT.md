# Parity-signed nonlinear interference between two kinetic defects in one-dimensional dimer deposition

## Finding

Place independently arriving irreversible dimers on the integer line: a dimer arriving on edge \(e_i=\{i,i+1\}\) succeeds only if both endpoints are vacant. All edge clocks have rate one except \(e_0\) and \(e_d\), with respective first-arrival rates \(a,b>0\), where the integer separation is \(d\ge2\). Write \(p_j(a,b)\) for the eventual probability that \(e_j\) itself accepts a dimer.

For each intermediate edge \(1\le j<d\), define the nonadditive two-defect response
\[
I_{d,j}(a,b)=p_j(a,b)-p_j(a,1)-p_j(1,b)+p_j(1,1).
\]
Set \(f(x)=e^{-x}\) and, for every \(a>0\), define functions on \(0\le x\le1\) by
\[
\delta_1^{(a)}(x)=\int_0^x e^{-y}\bigl[1-a(1-y)^{a-1}\bigr]dy,
\qquad \delta_{r+1}^{(a)}(x)=-\int_0^x\delta_r^{(a)}(y)dy\quad(r\ge1).
\]
Then the complete mixed-response identity is
\[
\boxed{I_{d,j}(a,b)=\int_0^1\delta_j^{(a)}(x)\delta_{d-j}^{(b)}(x)\,dx.}
\]
For \(a\ne1\) and \(b\ne1\), this quantity is **strictly nonzero** and satisfies
\[
\boxed{\operatorname{sgn}I_{d,j}(a,b)=(-1)^d\operatorname{sgn}[(a-1)(b-1)].}
\]
Thus all intermediate edges have precisely the same sign of nonlinear interference, irrespective of their distance from either anomaly. A uniform factorial bound is
\[
0<|I_{d,j}(a,b)|\le\frac{1}{(d-1)(j-1)!(d-j-1)!}.
\]
If either marked rate is one, the mixed response vanishes. The result is an exact infinite-volume, all-rate statement, not a small-perturbation expansion.

## Assumptions and scope

The substrate is \(\mathbb Z\), initially completely vacant. Edge \(e_i\) receives an independent Poisson arrival process with rate \(r_i\): \(r_0=a\), \(r_d=b\), and \(r_i=1\) elsewhere. Failed arrivals never become successful later, so only independent first-arrival times \(T_i\sim\operatorname{Exp}(r_i)\) matter. The observables are the indicator of *accepted dimers on the specified edge*, not occupancy of its two sites by possibly distinct dimers. Here \(a,b\) range over all positive reals and \(d,j\) over the integers \(d\ge2\), \(1\le j\le d-1\).

The infinite greedy matching is the increasing-first-clock limit of finite boxes. Dependence across a distance \(m\) requires an oriented chain of at least \(m\) strictly descending independent continuous priorities. Outside the two defects all clocks have the same rate, so summing the finite-length factorial tail gives almost sure local stabilization; finite boxes define the same local limit. The infinite-time final matching is well defined by the first-arrival priority ordering.

## Proof

**Half-line vacancy cavity.** With one boundary edge removed, let \(f(t)\) be the probability that a homogeneous half-line's boundary vertex has not yet been occupied at time \(t\). The empty-interval equations \(F_m'(t)=-(m-1)F_m(t)-F_{m+1}(t)\), initialized by \(F_m(0)=1\), admit the unique graphical-process solution \(F_m(t)=e^{-(m-1)t}f(t)\) with \(f(t)=\exp(e^{-t}-1)\). Hence putting \(x=1-e^{-t}\), the homogeneous cavity is \(f(x)=e^{-x}\). This is the usual one-dimensional dimer deposition cavity, restated to fix normalization.

**Directed defect cavities.** Remove an ordinary edge to the right of \(e_0\). When the boundary lies exactly one edge to the right of \(e_0\), denote its vacancy probability by \(q_1^{(a)}(t)\). Independence of the untouched half-line beyond the marked edge gives
\[
q_1^{(a)}(t)=1-\int_0^t a e^{-as} f(s)\,ds.
\]
Moving the removed boundary rightwards, the last edge now has unit rate. Therefore, for every \(r\ge1\),
\[
q_{r+1}^{(a)}(t)=1-\int_0^t e^{-s}q_r^{(a)}(s)\,ds.
\]
Subtract the homogeneous cavity, and replace time by \(x=1-e^{-t}\). Since \(e^{-s}ds=dx\) and \(e^{-as}ds=(1-x)^{a-1}dx\), these are exactly the stated recurrences for \(\delta_r^{(a)}=q_r^{(a)}-f\). Reflection gives the same recurrence for a right-side defect at \(e_d\) with rate \(b\).

**Nonlinear factorization.** Fix an intermediate edge \(e_j\). Condition on its first clock ringing at time \(t\). Delete \(e_j\); the two endpoint half-lines have independent clocks. The left endpoint sees the rate-\(a\) anomaly at distance \(j\); the right endpoint sees the rate-\(b\) anomaly at distance \(d-j\). Because \(e_j\) has rate one,
\[
p_j(a,b)=\int_0^\infty e^{-t}q_j^{(a)}(t)q_{d-j}^{(b)}(t)\,dt
=\int_0^1[f(x)+\delta_j^{(a)}(x)][f(x)+\delta_{d-j}^{(b)}(x)]dx.
\]
Inclusion-exclusion over the four rate choices cancels the homogeneous and both linear single-defect terms *exactly*, leaving the asserted product integral. This factorization depends on the distinct half-lines; it is not a consequence of linear superposition in the interacting adsorption process.

**Strict sign.** The boundary site next to the rate-\(a\) edge is still vacant at time \(t\) precisely when the exponential first attempt has not yet successfully deposited. Conditional on the independent opposite-end homogeneous half-line, earlier attempts cannot be less successful than later attempts. Consequently \(q_1^{(a)}(t)\) is strictly decreasing in \(a\) for every \(t>0\). Equivalently, for \(0<x\le1\), \(\delta_1^{(a)}(x)\) has sign opposite to \(a-1\). The displayed Volterra recursion flips sign at each further step, so
\[
\operatorname{sgn}\delta_j^{(a)}(x)=(-1)^j\operatorname{sgn}(a-1)
\quad (0<x\le1,\ a\ne1).
\]
Multiplying the two signs yields \((-1)^d\operatorname{sgn}[(a-1)(b-1)]\), constant over the integration domain. Strict positivity of the kernel ensures the integral is nonzero.

**Factorial screening.** Since \(q_1\) and \(f\) are vacancy probabilities, \(|\delta_1^{(a)}(x)|\le1\). By integrating the Volterra recursion, \(|\delta_j^{(a)}(x)|\le x^{j-1}/(j-1)!\). Multiply the two bounds and integrate \(x^{d-2}\) over \([0,1]\) to obtain \(|I_{d,j}|\le1/[(d-1)(j-1)!(d-j-1)!]\). The strict sign was independently proved and does not follow from this bound. This completes the proof.

## Verification

The standalone program `verify_two_defects.py` independently computes finite-path edge-acceptance probabilities by exact rational first-success conditioning on intervals. It compares their alternating mixed difference with independent numerical quadrature of the infinite-line cavity formula for every intermediate edge at separations \(2\le d\le5\), using defect rates \(a=2,b=3\). With twelve additional homogeneous edges at both ends, all ten rational comparisons differ from the infinite-line integrals by less than \(10^{-10}\). These are finite-size consistency checks; the all-separation, all-rate theorem follows from the preceding analytical argument.

Run `python -m pip install -r requirements.txt` followed by `python verify_two_defects.py`. Exact finite enumeration uses Python's standard-library `fractions` and `functools`; integration uses `mpmath` at 45-digit precision. Infinite-volume convergence and strict signs are mathematical consequences of the proof, not conclusions drawn from finite computation.

## Relationship to prior work

Homogeneous one-dimensional dimer parking, reviewed by Evans, establishes the baseline vacancy cavity. Lee (1997) analyzes an initially impurity-populated substrate rather than the nonlinear mixed response to two changed arrival rates. De Oliveira and Tomé (1994) solve periodic bipartite-rate adsorption, which does not directly specify two localized rate anomalies on an otherwise uniform infinite chain. An indexed 2026 calculation, *Alternating factorial screening of one anomalous dimer-adsorption bond*, proves the response to **one** kinetic defect. Its result does not determine the two-defect mixed difference, because that difference cancels both single-defect contributions and depends on the product of left and right cavity perturbations. A separately indexed 2026 result about *two preseeded dimers* concerns imposed initial occupation, not dynamically altered clocks.

Stacchiola and coauthors' 1998 *Cooperative sequential adsorption processes on heterogeneous substrates* reports exact one-dimensional heterogeneous dimer calculations. Only its abstract and bibliographic information were accessible; it might contain more general formulas implying this specialized factorization. The assertion of originality is therefore limited to the actually inspected text and indexed comparisons. No priority claim is made against inaccessible stronger work.

## Limitations

This is a local, two-defect, infinite-line result for independent memoryless first-attempt times. It concerns intermediate edge-acceptance probabilities, not pair covariances of deposition events, not arbitrary infinitely many defects, and not higher-dimensional substrates. The factorial estimate is an upper bound, not an asserted sharp distance asymptotic. The closest 1998 heterogeneous-substrate source could not be inspected in full, leaving historical-priority uncertainty. Independent scientific validation has not been performed.

## References

1. M. J. de Oliveira and T. Tomé, *Inhomogeneous random sequential adsorption on bipartite lattices*, Physical Review E 50, 4523 (1994), https://doi.org/10.1103/PhysRevE.50.4523.
2. J. W. Lee, *Effects of Impurities in Random Sequential Adsorption on a One-Dimensional Substrate*, arXiv:cond-mat/9701167 (first posted 1997-01-22), https://arxiv.org/abs/cond-mat/9701167.
3. D. J. Stacchiola, M. Ciacera, C. Zuppa, T. P. Eggarter and G. Zgrablich, *Cooperative sequential adsorption processes on heterogeneous substrates*, Journal of Chemical Physics 108, 1730 (1998), https://doi.org/10.1063/1.475545.
4. *Alternating factorial screening of one anomalous dimer-adsorption bond*, indexed mathematical research note (2026), available in the published mathematical research index.
5. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics 65, 1281 (1993), https://doi.org/10.1103/RevModPhys.65.1281.
