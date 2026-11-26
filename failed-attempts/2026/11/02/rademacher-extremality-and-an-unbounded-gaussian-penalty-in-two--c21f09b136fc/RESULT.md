# Rademacher extremality and an unbounded Gaussian penalty in two-mode randomized SVD

## Finding
Consider the one-sample randomized SVD/range-finder approximation \(\widehat A=qq^{\mathsf T}A\) for \(A=\operatorname{diag}(\sigma_1,\sigma_2)\), with \(\sigma_1>\sigma_2>0\), \(q=A\omega/\|A\omega\|_2\). Suppose the entries of the real vector \(\omega\) are independent and identically distributed, centered, unit-variance and nonzero almost surely. Among this class of isotropic product sketches, independent Rademacher coordinates uniquely minimize the expected **squared Frobenius** approximation error. The optimum and its Gaussian counterpart are respectively
\[\mathbb E\|A-\widehat A_R\|_F^2=\frac{2\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2},\qquad \mathbb E\|A-\widehat A_G\|_F^2=\sigma_1\sigma_2.\]
The ratio of Gaussian to Rademacher mean squared errors is \((\kappa+\kappa^{-1})/2\), where \(\kappa=\sigma_1/\sigma_2>1\). This ratio is unbounded as \(\kappa\) grows. In particular the two isotropic distributions need not have comparable **expected one-sample error**, even though both can perform well with oversampling.

## Assumptions and scope
The theorem applies to every pair \(\sigma_1>\sigma_2>0\) and every product distribution satisfying the conditions above. The sketch coordinates must be expressed in the right singular-vector basis; for the displayed diagonal matrix this is the coordinate basis. We assume exact arithmetic, one random vector, no power iteration, no oversampling and the standard orthogonal range projection. The norm in the claim is squared Frobenius norm, not operator norm. Denote \(a=\sigma_1^2\), \(b=\sigma_2^2\), \(X=\omega_1^2\), and \(Y=\omega_2^2\), which are strictly positive iid random variables. All integrals below are finite because the random residual lies between \(b\) and \(a\).

## Proof
First, \(q=(\sigma_1\omega_1,\sigma_2\omega_2)^{\mathsf T}/\sqrt{aX+bY}\). Orthogonal projection gives
\[R(X,Y):=\|A-qq^{\mathsf T}A\|_F^2=\|A\|_F^2-\|q^{\mathsf T}A\|_2^2=\frac{ab(X+Y)}{aX+bY}.\tag{1}\]
Constant coordinate magnitudes \(X=Y=1\) yield the deterministic residual \(R_R=2ab/(a+b)\). For arbitrary positive \(x,y\), direct common-denominator reduction gives the exact symmetrization identity
\[\frac{R(x,y)+R(y,x)}2-\frac{2ab}{a+b}=\frac{ab(a-b)^2(x-y)^2}{2(a+b)(ax+by)(ay+bx)}.\tag{2}\]
Since \((X,Y)\) and \((Y,X)\) have the same joint law, expectation in (2) proves the distribution-free lower bound with equality precisely when \(X=Y\) almost surely, as \(a>b>0\). Independence of the iid variables forces each squared magnitude to be almost surely a constant; unit variance makes that constant one. Centering then gives equal probabilities for \(\omega_i=+1\) and \(\omega_i=-1\). Thus the only equality-achieving iid-coordinate law is independent Rademacher.

For independent standard Gaussian entries, use polar coordinates \((\omega_1,\omega_2)=T(\cos\theta,\sin\theta)\), with \(\theta\) uniform on \([0,2\pi)\) and \(T>0\) independent. Equation (1) becomes \(R_G=ab/(a\cos^2\theta+b\sin^2\theta)\). The elementary substitution \(t=\tan\theta\) on one quadrant yields
\[\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{a\cos^2\theta+b\sin^2\theta}=\frac1{\sqrt{ab}}.\tag{3}\]
Consequently \(\mathbb E R_G=\sqrt{ab}\). Dividing by \(R_R\) gives \((a+b)/(2\sqrt{ab})=(\kappa+\kappa^{-1})/2\), proving the claimed unbounded ratio. The zero singular-gap case \(a=b\), excluded above, yields identical squared error for every nonzero sketch direction and therefore no strict optimizer.

## Verification
The supplied standalone `checker.py` tests (2) using exact rational arithmetic for positive integer squared singular values and sketch magnitudes and tests (3) by periodic midpoint quadrature for a variety of positive singular values. Executing `python checker.py` yielded `PASS 5316 exact-rational and numerical cases`. These finite checks only supplement the algebraic identities (1)--(3); the universal quantifiers follow from the proof. No stochastic Monte Carlo sampling is required for the analytical comparison.

## Relationship to prior work
Lynch-Davies and Webb (2026) formulate randomized SVD for general sub-Gaussian sketch distributions, explicitly include independent Rademacher sketches, and show numerical comparisons with Gaussian sketches. Their bounds and experiments do not state the two-mode exact expectation formulas, distribution-free optimality among iid coordinate laws, or the unbounded one-sample Gaussian/Rademacher ratio. Diouane, Gürol, Scotto Di Perrotolo and Vasseur (2022) analyze expected low-rank approximation errors in Gaussian settings, but do not present a Rademacher comparison or the universal two-mode extremality statement. The classical randomized range finder and orthogonal projection identity are not new; the result here is the exact distribution comparison and strict equality classification.

## Limitations
This is a complete two-dimensional, single-vector, squared-Frobenius result for sketches aligned with the singular vectors. Coordinatewise Rademacher sketches are not rotationally invariant, so the result must not be applied to arbitrary rotated matrices without corresponding alignment. Neither the magnitude ordering nor the unbounded ratio is claimed for algorithms with oversampling, for arbitrary dependent coordinate laws, or for expectations of unsquared errors. The singular basis may be unknown in applications; the theorem supplies a controlled diagnostic and not a universally superior sketch-selection rule. Historical priority is not independently audited; a more specialized older two-mode formula remains a possible risk.

## References
- M. Lynch-Davies and M. Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1 (first public 2026-10-22), https://arxiv.org/html/2610.31333v1.
- Y. Diouane, S. Gürol, A. Scotto Di Perrotolo, and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793 (2022), https://arxiv.org/abs/2206.08793.
- N. Halko, P.-G. Martinsson, and J. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review **53** (2011), 217–288.
