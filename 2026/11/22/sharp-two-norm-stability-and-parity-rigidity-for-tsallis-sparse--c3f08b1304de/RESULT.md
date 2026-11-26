# Sharp two-norm stability and parity rigidity for Tsallis sparse probability maps

## Finding

For \(n\ge2\) and \(1<\alpha\le2\), let
\[
E_\alpha(z)=\operatorname*{argmax}_{p\in\Delta_{n-1}}
\left\{\langle z,p\rangle+\frac{1-\sum_i p_i^\alpha}{\alpha(\alpha-1)}\right\},
\qquad \Delta_{n-1}=\{p_i\ge0,\ \sum_i p_i=1\}.
\]
Write \(m=\lfloor n/2\rfloor\), \(\ell=\lceil n/2\rceil\), and \(\gamma=(\alpha-1)/(3-\alpha)\). The smallest constant in \(\|E_\alpha(z)-E_\alpha(z')\|_1\le L_{n,\alpha}\|z-z'\|_\infty\) is
\[
\boxed{L_{n,\alpha}=\frac{4(m\ell)^{\alpha-1}}{(m^\gamma+\ell^\gamma)^{3-\alpha}}.}
\]
It equals \(n^{\alpha-1}\) for even \(n\) and is strictly smaller for odd \(n\). For \(n=1\) the map is constant and the coefficient is zero. For \(n\ge2\), the \(\alpha\downarrow1\) limit is the sharp corresponding softmax coefficient, one.

For \(1<\alpha<2\), the only interior probability patterns giving Jacobian norm \(L_{n,\alpha}\) have, up to permutation and exchange of the named blocks, \(m\) equal entries of total mass \(q=\ell^\gamma/(m^\gamma+\ell^\gamma)\) and \(\ell\) equal entries of total mass \(1-q\). At \(\alpha=2\) every interior output has the same Jacobian and its norm is \(4m\ell/n\). At an interior maximizing output, the nonzero directions giving the maximal differential ratio in the ordinary norms are exactly the nonzero multiples of sign vectors of the maximizing cuts, with constant opposite signs on the two blocks. At \(\alpha=2\) any balanced cut is maximizing. Scores themselves can be translated by a constant; for direction classes modulo constants the displayed sign directions are the centered representatives. A nonzero constant shift of such a direction does not preserve equality in the ordinary, unquotiented norm.

## Assumptions and scope

The inputs are arbitrary real scores, the norms are the ordinary unweighted coordinate norms, and the regularizer has exactly the stated normalization. The bound is global in the scores, with no fixed-support or score-diameter restriction. The direction classification is differential, at interior maximizing outputs, not a claim of finite-score-pair attainment. The endpoint \(\alpha=1\) is included only for softmax and the stated limit.

## Proof

**1. Existence, derivative and support changes.** Strict concavity gives a unique output. Set \(\beta=2-\alpha\in[0,1)\). The optimality conditions give
\[
p_i=\big[(\alpha-1)(z_i-\tau)\big]_+^{1/(\alpha-1)},\qquad \sum_i p_i=1,
\]
with a unique threshold \(\tau\). Every positive simplex point is realized by \(z_i=p_i^{\alpha-1}/(\alpha-1)\). For \(\beta>0\), the threshold equation is \(C^1\) including where a positive-part argument vanishes. The derivative of the sum in \(\tau\) is \(-S=-\sum_i p_i^\beta<0\), so the implicit function theorem yields a \(C^1\) score map with Jacobian
\[
J(p)=\operatorname{diag}(s)-ss^{\mathsf T}/S,
\qquad s_i=p_i^\beta,\quad S=\sum_i s_i.
\]
For \(\beta=0\) the map is Euclidean simplex projection. On an affine score segment it is continuous and piecewise affine: for each nonempty active set \(I\) the threshold is \((\sum_{i\in I}z_i-1)/|I|\), and its admissibility is given by affine inequalities. On each open subinterval with constant positive support the derivative along the segment is given by the same matrix with \(s_i=1\) on the positive support and \(0\) elsewhere. This includes segments lying in a support-boundary hyperplane. Thus a uniform bound on these matrices integrates along any score segment.

**2. Exact sign-cut norm.** The matrix \(J\) is positive semidefinite by weighted Cauchy–Schwarz. By cube duality and Cauchy–Schwarz for \(J\),
\[
\|J\|_{\infty\to1}=\max_{\varepsilon,\delta\in\{-1,1\}^n}\delta^{\mathsf T}J\varepsilon
=\max_{\varepsilon\in\{-1,1\}^n}\varepsilon^{\mathsf T}J\varepsilon.
\]
For the cut \(I\) of positive signs this quadratic form equals \(4AB/(A+B)\), where \(A=\sum_{i\in I}s_i\), \(B=\sum_{i\notin I}s_i\). Empty and full cuts give zero.

**3. Optimize a cut.** For nonempty blocks of sizes \(k,h\), and mass \(u=\sum_{i\in I}p_i\), Jensen gives \(A\le k^{1-\beta}u^\beta\), \(B\le h^{1-\beta}(1-u)^\beta\) when \(\beta>0\), with equality precisely at constant entries in each block. A zero-mass block gives zero cut value. For two positive masses, the cut value is strictly increasing in each weight sum. The remaining optimization minimizes \(k^{\beta-1}/u^\beta+h^{\beta-1}/(1-u)^\beta\). It is strictly convex, diverges at the endpoints, and its derivative gives \(u/(1-u)=(h/k)^\gamma\), \(\gamma=(1-\beta)/(1+\beta)\). Substitution gives
\[
F_{k,h}=\frac{4(kh)^{1-\beta}}{(k^\gamma+h^\gamma)^{1+\beta}}.
\]
When \(\beta=0\), use directly \(A\le k\), \(B\le h\), including at sparse outputs. The same expression \(F_{k,h}=4kh/(k+h)\) then follows and is attained for any positive output.

**4. Balanced cuts.** For fixed \(n\), use \(x=k/h\le1\) and relax to real cut sizes. Differentiating gives
\[
\frac{d}{dx}\log F_{nx/(1+x),n/(1+x)}
=\frac{(1-\beta)(1-x^{1+\gamma})}{x(1+x)(1+x^\gamma)}.
\]
This is positive for \(0<x<1\), so by symmetry only the balanced integer sizes maximize, including the complementary tie. The equal-size value is \(n^{\alpha-1}\), giving the strict odd deficit. The equality cases of the cut optimization yield the stated patterns and maximizing cuts.

**5. Sharpness and directions.** The interior pattern in the finding (any positive output at \(\alpha=2\)) has the asserted norm, and differentiation along a maximizing sign direction gives the matching lower bound on the global coefficient. For the direction classification, let \(M=\|J\|_{\infty\to1}>0\) at such an output and normalize a direction \(w\) by \(\|w\|_\infty=1\). If \(\|Jw\|_1=M\), choose a dual sign to attain that value. Cauchy–Schwarz forces \(w^{\mathsf T}Jw\ge M\), and convexity bounds it above by the maximum \(M\) on the cube. Since \(J_{ii}=s_i(1-s_i/S)>0\) for all \(i\), strict convexity on each coordinate line shows that a maximizing \(w\) has no interior coordinate. Conversely a maximizing sign vertex realizes the norm by testing against itself. This proves the claimed directions. For such a sign vector \(\varepsilon\), \(J(t\varepsilon+c\mathbf1)=tJ\varepsilon\) but \(\|t\varepsilon+c\mathbf1\|_\infty=|t|+|c|\), explaining the centering requirement. The one-coordinate case is immediate. At \(\alpha\downarrow1\), the formula tends to one. Softmax has the same Jacobian form with \(s_i=p_i\), so its cut values are \(4u(1-u)\le1\), with equality at any positive pattern having a cut with both masses one-half.

## Verification

The proof applies to all stated dimensions and parameters. The supplementary standard-library script `verify.py` compares exhaustive cube-vertex norms with sign-cut norms for \(2\le n\le9\), checks predicted values and witnesses for five exponents, and tests finite differences using a separate threshold-equation implementation. The recorded run reported 11,040 deterministic assertions (`python3 verify.py`). These finite checks neither prove the all-dimension formula nor classify the equality directions.

## Relationship to prior work and limitations

The Tsallis variational map and normalization are in the Fenchel–Young loss and entmax literature. The separable-entropy Jacobian is attributed to Peters, Niculae and Martins (2019, Appendix B); neither the map nor that Jacobian is claimed as new. The contribution is its sharp heterogeneous cross-norm optimization over the simplex for the power entropy, including the strict odd-dimensional deficit and the maximizing patterns. The diagonal-plus-rank-one calculation for a fixed output by itself does not supply this optimization. Published same-exponent softmax bounds and other-norm projection bounds are different questions. The result makes no claim for weighted norms, additional temperatures, or composed layers. Exact priority remains subject to possible earlier sharp-modulus or equivalent simplex-cut formulations.

## References

1. M. Blondel, A. F. T. Martins, V. Niculae, *Learning Classifiers with Fenchel-Young Losses: Generalized Entropies, Margins, and Algorithms*, arXiv:1805.09717.
2. B. Peters, V. Niculae, A. F. T. Martins, *Sparse Sequence-to-Sequence Models*, arXiv:1905.05702, §3 and Appendix B.
3. A. F. T. Martins, R. F. Astudillo, *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*, arXiv:1602.02068.
4. P. Nair, *Softmax is 1/2-Lipschitz: A tight bound across all ℓp norms*, arXiv:2510.23012.
