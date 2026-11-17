# Exact three-mode support and a unique covariance-volume resonance in dichotomous linear dynamics

## Finding

For a common stationary two-state Markov input driving three distinct linear relaxations with rate ratio \(1:2:3\), the full stationary support is a fixed, explicitly bounded three-dimensional moment body of volume \(1/30\), independent of the input's switching rates and stationary bias. In contrast, the determinant of the stationary covariance has exactly one maximizer as the total switching rate varies, at a universal dimensionless rate \(\kappa_*\in(9/10,1)\). This distinguishes *accessible geometry* from *concentration of stationary mass* in a nonelliptic random switching system.

More precisely, let \(0<\pi<1\), \(\gamma>0\), and \(\kappa>0\). Let \(S_t\in\{0,1\}\) be a stationary continuous-time Markov chain with transitions \(0\to1\) at rate \(\pi\kappa\gamma\) and \(1\to0\) at rate \((1-\pi)\kappa\gamma\). For \(j=1,2,3\), let \(X_j\) solve
\[
\dot X_j(t)=j\gamma\bigl(S_t-X_j(t)\bigr)
\]
in its stationary regime. Write \(m=X_1\), \(x=X_2\), \(z=X_3\). The topological support of \((m,x,z)\), and the support conditional on either current input mode, is the same compact set \(K\), consisting of the two points \((0,0,0)\), \((1,1,1)\), and the points satisfying
\[
0<m<1,\qquad m^2\le x\le2m-m^2,
\]
\[
\frac{3x^2}{4m}+\frac{m^3}{4}
\le z\le
1-\frac{3(1-x)^2}{4(1-m)}-\frac{(1-m)^3}{4}.
\]
Its ordinary three-dimensional Lebesgue volume is exactly \(\operatorname{Vol}_3(K)=1/30\).

All stationary coordinate means equal \(\pi\), and the covariance matrix is
\[
\operatorname{Cov}(X_i,X_j)
=\pi(1-\pi)\frac{ij}{i+j}
\left(\frac1{i+\kappa}+\frac1{j+\kappa}\right),
\qquad i,j\in\{1,2,3\}.
\]
In particular,
\[
\det\operatorname{Cov}(X_1,X_2,X_3)
=[\pi(1-\pi)]^3\,
\frac{\kappa^2(\kappa+6)}{150(\kappa+1)^2(\kappa+2)^2(\kappa+3)^2}.
\]
This determinant is strictly increasing for \(0<\kappa<\kappa_*\) and strictly decreasing for \(\kappa>\kappa_*\), where \(\kappa_*\) is the **unique positive zero** of
\[
Q(\kappa)=3\kappa^4+30\kappa^3+61\kappa^2-18\kappa-72.
\]
Numerically \(\kappa_*=0.9802645581\ldots\). The optimum is independent of \(\pi\) and \(\gamma\), with vanishing determinant at both zero- and infinite-rate limits.

## Assumptions and scope

The driving chain is time-homogeneous, stationary, irreducible, binary and independent of the past response except through the specified forcing. All rates are strictly positive. The three relaxation rates are fixed in proportion \(1:2:3\); the conclusion does not assert an optimum at the same dimensionless rate for arbitrary triples or other driving laws. We consider the unique stationary solution on \(\mathbb R^3\), not transient response from an arbitrary initial condition. All support statements concern closed topological supports, including limiting histories of arbitrarily many switches. No assumption of stationarity-density smoothness is made.

## Proof

**1. Stationary construction and input correlation.** Stable variation of constants gives a unique stationary solution
\[
X_j(t)=j\gamma\int_0^\infty e^{-j\gamma s}S_{t-s}\,ds,
\]
and any other solution under the same driving path approaches it exponentially. For the irreducible two-state input,
\[
\mathbb ES_t=\pi,\qquad
\operatorname{Cov}(S_t,S_{t+h})=\pi(1-\pi)e^{-\kappa\gamma|h|}.
\]
The convolution kernels integrate to one, so \(\mathbb EX_j=\pi\).

**2. Covariance and its unique maximum.** Substitute the correlation identity into the double convolution for \(X_i,X_j\), rescale by \(\gamma\), and split the integration domain into \(s\ge t\) and \(s<t\). The elementary integral is
\[
\int_0^\infty\!\int_0^\infty
ij\,e^{-is-jt-\kappa|s-t|}\,ds\,dt
=\frac{ij}{i+j}\left(\frac1{i+\kappa}+\frac1{j+\kappa}\right).
\]
This proves every covariance entry. Taking its \(3\times3\) determinant yields the stated rational function. Exact differentiation yields
\[
\frac{d}{d\kappa}\frac{\kappa^2(\kappa+6)}{150\prod_{j=1}^3(\kappa+j)^2}
=-\frac{\kappa Q(\kappa)}{150\prod_{j=1}^3(\kappa+j)^3}.
\]
The coefficient sequence of \(Q\) in descending powers has one sign change. By Descartes' rule \(Q\) has at most one positive root, counted with multiplicity. Its value at zero is negative, while its leading coefficient is positive, so continuity gives exactly one positive root. Direct rational substitution gives \(Q(9/10)<0<Q(1)\). The sign of the derivative gives strict increase and decrease on either side. Finally the determinant divided by \([\pi(1-\pi)]^3\) behaves as \(\kappa^2/900\) as \(\kappa\downarrow0\) and as \(1/(150\kappa^3)\) as \(\kappa\to\infty\). Thus the critical point is the unique global maximizer.

**3. Recovering the entire support.** Under the substitution \(u=e^{-\gamma s}\), the stationary vector is the first three weighted moments of a binary history \(\eta:[0,1]\to\{0,1\}\):
\[
(m,x,z)=\left(\int_0^1\eta(u)\,du,
2\int_0^1u\eta(u)\,du,
3\int_0^1u^2\eta(u)\,du\right).
\]
The closure of moment vectors of binary measurable histories equals that for measurable \(0\le\eta\le1\): approximate any fractional density by increasingly fine binary subdivisions preserving moments in the limit. The Markov chain assigns positive probability to each finite alternating-switch history within any fixed time window. Earlier history contributes at most \(e^{-j\gamma T}\) to coordinate \(j\), and an arbitrarily short final interval can prescribe either value of the present input mode. Therefore the stationary joint law has precisely this closed moment image as its support in each mode, independently of the positive transition rates.

Let \(0<m<1\). Among densities \(0\le\eta\le1\) of mass \(m\), the first moment \(x/2\) lies in \([m^2/2,m-m^2/2]\), by filling the leftmost or rightmost interval. This gives \(m^2\le x\le2m-m^2\). For an admissible pair \((m,x)\) set \(c=x/(2m)\) and \(I=[c-m/2,c+m/2]\subset[0,1]\). The indicator of \(I\) has the prescribed mass and first moment. Since the quadratic \((u-c)^2\) is no larger inside \(I\) than outside, the bathtub principle (or direct subtraction at the threshold \((m/2)^2\)) gives
\[
\int_0^1 (u-c)^2(\eta(u)-\mathbf1_I(u))\,du\ge0.
\]
The equal mass and first moment cancel the affine terms, so this inequality minimizes the second moment, giving \(z_{\min}=3x^2/(4m)+m^3/4\). Apply the same argument to \(1-\eta\), of mass \(1-m\) and first moment \((1-x)/2\), to get the upper bound \(z_{\max}=1-3(1-x)^2/(4(1-m))-(1-m)^3/4\). Every intermediate value of \(z\) occurs for a convex combination of the two minimizing/maximizing fractional controls; approximation by binary histories then puts it in the closed support. If \(m\in\{0,1\}\), only the all-zero/all-one moment vector is possible.

**4. Volume.** The vertical section height simplifies exactly to
\[
z_{\max}-z_{\min}=
\frac{3(x-m^2)(2m-m^2-x)}{4m(1-m)}.
\]
Integrate over the stated planar region: for each \(0<m<1\),
\[
\int_{m^2}^{2m-m^2}(z_{\max}-z_{\min})\,dx=m^2(1-m)^2.
\]
A final integral yields \(\operatorname{Vol}_3(K)=\int_0^1 m^2(1-m)^2\,dm=1/30\).

## Verification

The accompanying `check_covariance.py` uses exact symbolic algebra to reconstruct the covariance determinant and derivative, check the polynomial support-bound identity and compute the support volume. It checks positive definiteness for six positive rational switching rates and tests multiple rational support slices; execution prints `THREE_MODE_TELEGRAPH_EXACT_OK determinant=1 derivative=1 support=1 volume=1 rational_cases=6`. The continuous support argument, Descartes uniqueness and the positive-probability reachability reasoning are proved above; neither finite tests nor a symbolic computation alone are substituted for them. Reproduce with `python check_covariance.py` after installing SymPy.

## Relationship to prior work

Benaïm and Bichard, arXiv:2406.17891, analyze the same class of piecewise-deterministic affine contractions in arbitrary dimension. In particular their Example 1.5 encompasses diagonal three-mode contraction, and their Proposition 2.1 already supplies unique invariant law and a general accessible-support identity. Their Theorem 2.2 concerns regularity under sufficiently fast switching. The present statement does **not** claim either existence, absolute continuity or regularity as new results; its assessed additional content is the complete *explicit* three-coordinate accessible body, its exact volume, and the sharp unique rate optimizing stationary covariance volume. The full-text model, Proposition 2.1, Theorem 2.2 and support discussion were compared directly.

Bakhtin, Hurth, Lawley and Mattingly, arXiv:2009.01299, already give the planar support between two single-switch curves and analyze density singularities in two dimensions. That planar region is not claimed here as original. The current three-mode moment body is not a relabeling of the planar support; three independent moment constraints and a quadratic rearrangement identify its additional bounding coordinate. General telegraph-filter moment identities are classical, so the covariance-entry calculation alone is not an originality claim. The precise three-mode determinant optimum is the assessed nontrivial new quantitative conclusion.

## Limitations

This is a specified diagonal \(1:2:3\) contraction family, not a classification of arbitrary positive relaxation spectra, input states, or non-Markov residence times. A general formula for correlations of linear filters is standard and may already imply parts of the calculation algebraically. No claim is made about optimal information, density regularity, or joint distribution shape beyond the specified support and covariance. Although two closely related primary articles were inspected, unindexed signal-processing or moment-problem publications might contain equivalent geometric or optimum formulas. 
## References

1. Michel Benaïm and Améthyste Bichard, *Regularity of invariant densities for random switching between two linear ODEs in* \(\mathbb R^d\), arXiv:2406.17891, first posted June 25, 2024. https://arxiv.org/abs/2406.17891
2. Yuri Bakhtin, Tobias Hurth, Sean D. Lawley and Jonathan C. Mattingly, *Singularities of invariant densities for random switching between two linear ODEs in 2D*, arXiv:2009.01299, first posted September 2, 2020. https://arxiv.org/abs/2009.01299
3. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Physical Review A 35 (1987), 3102, https://doi.org/10.1103/PhysRevA.35.3102 (abstract inspected; a relevant general higher-order-filter moment predecessor, not a source for claims of noncoverage of the full article).
