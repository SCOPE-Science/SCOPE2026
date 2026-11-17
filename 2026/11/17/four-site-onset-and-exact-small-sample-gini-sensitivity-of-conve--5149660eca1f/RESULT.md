# Four-site onset and exact small-sample Gini sensitivity of convex least-squares regression

## Finding
For each integer \(n\ge 2\), let \(Q_n:\mathbb R^n\to\mathbb R^n\) be Euclidean nearest-point projection onto the cone of convex sequences on equally spaced sites,
\[
\mathcal C_n=\bigl\{y\in\mathbb R^n:y_i-2y_{i+1}+y_{i+2}\ge0\ (1\le i\le n-2)\bigr\}.
\]
For real \(u\in\mathbb R^n\), define complete-pair Gini variation and its two-input projector modulus by
\[
G_n(u)=\sum_{1\le i<j\le n}|u_i-u_j|,\qquad
\Lambda_n=\sup_{G_n(a-b)>0}\frac{G_n(Q_n(a)-Q_n(b))}{G_n(a-b)}.
\]
The sharp values through eight observations are
\[
\boxed{\begin{array}{c|rrrrrrr}
n&2&3&4&5&6&7&8\\\hline
\Lambda_n&1&1&10/9&41/35&213/175&191/153&463/357
\end{array}}.
\]
Consequently, **four observations are the first dimension in which Euclidean convex regression can increase the Gini variation of a perturbation**. In every dimension \(n\ge4\), one has the explicit strict lower bound
\[
\boxed{\Lambda_n\ge\frac{4n-6}{3(n-1)}>1.}
\]
An exact finite expression for the full modulus in every dimension is given below. No optimal larger-dimensional closed form is asserted.

## Assumptions and scope
The observations, fitted sequences, and variations are real, the design sites are equally spaced, and all squared-error weights equal one. There are no monotonicity, endpoint, or sign restrictions. The metric projection is uniquely defined using squared Euclidean error; the *two-input* sensitivity is measured with the Gini seminorm, whose nullspace is the constant vectors. For \(n=2\) the feasible cone is all of \(\mathbb R^2\).

## Proof
**1. Attainable active-face Jacobians.** Let \(D\) be the \((n-2)\times n\) matrix whose row \(i\) has entries \((1,-2,1)\) in coordinates \(i,i+1,i+2\). The rows are linearly independent. For each active subset \(A\subseteq\{1,\ldots,n-2\}\) let \(D_A\) contain the indicated rows, and put
\[
P_A=I-D_A^{\mathsf T}(D_AD_A^{\mathsf T})^{-1}D_A,\qquad P_\varnothing=I.
\]
Every subset \(A\) actually occurs on an open region of the Euclidean projection. Indeed, prescribe second differences zero on \(A\) and one outside \(A\), obtaining a feasible sequence \(y\) by surjectivity of \(D\). With all multipliers \(\lambda_i=1\) on \(A\), let input \(x=y-D_A^{\mathsf T}\lambda\). Strictly positive active multipliers and strictly positive inactive second differences give strict complementarity. The projection of \(x\) is \(y\), and nearby data have Jacobian \(P_A\). Conversely, the polyhedral projection is a continuous, finitely piecewise affine map with these local linear maps. Integrating on a generic input segment and passing to limits proves its global seminorm modulus equals the largest induced seminorm of an attainable \(P_A\).

**2. Binary-cut reduction of the Gini norm.** If the coordinates of \(u\) are ordered increasingly, decompose \(u\) into a constant vector plus nonnegative combinations of indicators of upper level sets. For a subset \(S\) with \(|S|=k\),
\[
G_n(\mathbf1_S)=k(n-k).
\]
Each \(P_A\) fixes constant vectors. The triangle inequality in this level-set decomposition therefore shows that its induced Gini seminorm is exactly
\[
\max_{\varnothing\ne S\subsetneq\{1,\ldots,n\}}
\frac{G_n(P_A\mathbf1_S)}{|S|(n-|S|)}.
\]
Taking complementary subsets gives the same quotient since \(P_A\mathbf1=\mathbf1\). Combining this with Step 1 gives the **exhaustive finite formula**, valid for every integer \(n\ge2\):
\[
\boxed{\Lambda_n=
\max_{A\subseteq\{1,\ldots,n-2\}}
\max_{\substack{\varnothing\ne S\subseteq\{1,\ldots,n-1\}}}
\frac{G_n(P_A\mathbf1_S)}{|S|(n-|S|)}.}\tag{1}
\]
The second maximum uses one representative of each complementary pair of nontrivial subsets.

**3. Exact finite classifications.** Formula (1) requires precisely \(2^{n-2}(2^{n-1}-1)\) rational comparisons. The standalone checker `verify_gini_convex.py` constructs every inverse in (1) over exact rational arithmetic and enumerates *every* active subset and representative cut for each \(2\le n\le8\). Its complete results give the seven fractions in the Finding. The maximizing active sets, indexed from one, and representative cuts are respectively \((\varnothing,\{1\})\) for \(n=2,3\); \((\{1\},\{1\})\) for \(n=4\); \((\{1,3\},\{1\})\) for \(n=5,6\); \((\{1,3,5\},\{1\})\) for \(n=7\); and \((\{1,3,5\},\{3\})\) for \(n=8\). They are representative maximizers, not an asserted classification of all equality cases.

For transparency, the complete lists of *facewise maxima* at four and five sites, with each bit encoding active curvature equality in increasing site order, are
\[
\begin{array}{c|rrrr}
 n=4,\ A&00&10&01&11\\\hline
 \max_S(\cdots)&1&10/9&10/9&1
\end{array}
\]
\[
\begin{array}{c|rrrrrrrr}
 n=5,\ A&000&100&010&110&001&101&011&111\\\hline
 \max_S(\cdots)&1&7/6&7/6&11/10&7/6&41/35&11/10&1
\end{array}.
\]
In particular, at five sites the separated-curvature face has matrix
\[
P_{\{1,3\}}=\frac1{35}
\begin{pmatrix}
29&12&-5&-2&1\\
12&11&10&4&-2\\
-5&10&25&10&-5\\
-2&4&10&11&12\\
1&-2&-5&12&29
\end{pmatrix}.
\]
Its first-column Gini variation equals \(164/35\), versus \(G_5(e_1)=4\), yielding \(41/35\). The exhaustive face and cut comparisons prove it is the global maximum, not merely a local lower bound.

**4. A finite pair and every-dimensional strict amplification.** At four sites take data \(a=(-1,2,-1,1)\) and \(b=(-9/10,2,-1,1)\). Their exact convex fits are
\[
Q_4(a)=(0,0,0,1),\qquad Q_4(b)=(1/12,1/30,-1/60,1).
\]
The active first second difference vanishes, the second is strictly positive, and the associated multiplier is positive at both inputs. Direct subtraction gives
\[
\frac{G_4(Q_4(b)-Q_4(a))}{G_4(b-a)}=\frac{10}{9}.
\]
For arbitrary \(n\ge4\), use the face consisting solely of the first curvature equality. Its projector sends the first unit vector to
\[
P_{\{1\}}e_1=(5/6,\,1/3,\,-1/6,\,0,\ldots,0).
\]
Consequently \(G_n(P_{\{1\}}e_1)=(4n-6)/3\) and \(G_n(e_1)=n-1\). Attainability from Step 1 proves the strict lower bound in the Finding in every such dimension. For \(n=2,3\), the exhaustive formula gives one, proving the first-instability threshold. \(\square\)

## Verification
Execute `python3 verify_gini_convex.py` with Python 3's standard library. The checker uses `fractions.Fraction`, exact Gram matrix inversion, complete active-face and complementary-cut enumeration for every size \(2\le n\le8\), exact projector symmetry/idempotence and constant preservation checks, the four-site finite KKT witness, and the fixed-face lower identity for \(4\le n\le30\). It reports `ALL_EXACT_CONVEX_GINI_CHECKS_PASS 24782`. The code establishes the finite enumerated fractions after the general finite-reduction theorem; it is not presented as an infinite proof by testing sample sizes. Steps 1, 2, and 4 provide independent analytical arguments for the unrestricted statements.

## Relationship to prior work
Guntuboyina and Sen (first public May 7, 2013, arXiv:1305.1648v1) formulate convex least squares as projection onto a convex-sequence cone and study statistical risk, rather than the two-input Gini operator modulus. Bellec (arXiv:1510.08029v1) gives sharp oracle inequalities for shape-restricted least squares, likewise in squared-error statistical metrics. Published exact computations for the same convex-cone projector with **coordinate maximum norm** give \(1,4/3,7/5,11/7\) at sizes two through five and an all-size lower bound, but they do not determine the Gini norm: coordinatewise amplification and all-pair variation have distinct extreme directions and normalization. Here the first strict Gini amplification occurs at four sites, while coordinatewise amplification already occurs at three.

## Limitations
The exact numerical classification is proved only through eight observations. Formula (1) is exact for any finite dimension but not a closed asymptotic solution. The larger-dimensional lower bound need not be optimal; no nontrivial universal upper bound or full maximizing-face classification is claimed. Results for nonuniform weights, unequal design spacings, and other pair-distance metrics are not asserted. Full historical priority, especially against unindexed stability literature, remains a risk. Independent mathematical audit has not been performed.

## References
1. A. Guntuboyina and B. Sen, *Global risk bounds and adaptation in univariate convex regression*, arXiv:1305.1648v1 (2013-05-07), https://arxiv.org/abs/1305.1648 .
2. P. C. Bellec, *Sharp oracle inequalities for Least Squares estimators in shape restricted regression*, arXiv:1510.08029v1 (2015-10-27), https://arxiv.org/abs/1510.08029 .
3. Y. Chen and J. A. Wellner, *On convex least squares estimation when the truth is linear*, arXiv:1411.4626v1 (2014-11-17), https://arxiv.org/abs/1411.4626 .
4. *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-five-point-nonlocal-instability-and-a-persistent-lower-bound-for--45dce1453393 .
5. *First interior worst-case amplification in five-point convex regression*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-first-interior-worst-case-amplification-in-five-point-convex-reg--5b2e2c46bf91 .
