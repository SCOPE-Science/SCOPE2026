# Exact John–Löwner ellipsoids and distortion of a critical log-cosh projection body for parallelotopes

## Finding

A recently introduced critical projection-type functional has an exact affine-geometric solution on every centered volume-one parallelotope. Fix an integer \(d\ge2\), a real parameter \(\beta>0\), an invertible \(d\times d\) real matrix \(A\) with \(|\det A|=1\), and the centered parallelotope \(K=A[-1/2,1/2]^d\). Define
\[
\Phi_K(y)=\int_{\partial K} \langle x,n_K(x)\rangle
\log\cosh\!\left(\frac{\langle y,n_K(x)\rangle}{2\langle x,n_K(x)\rangle}\right)
\,d\mathcal H^{d-1}(x),\qquad
T_{K,\beta}=\{y\in\mathbb R^d:\Phi_K(y)\le\beta\}.
\]
The integral is the finite facet integral; its values on edges are immaterial. Let \(c(s)=\operatorname{arcosh}(e^s)\), \(s>0\). Then
\[
\boxed{T_{K,\beta}=A\left\{z\in\mathbb R^d:\sum_{i=1}^d\log\cosh(z_i)\le\beta\right\}.}
\]
The **unique maximal-volume inscribed (John) ellipsoid** and **unique minimum-volume circumscribed (Löwner) ellipsoid** are, respectively,
\[
\boxed{J_{K,\beta}=A\big(\sqrt d\,c(\beta/d)B_2^d\big),\qquad
L_{K,\beta}=A\big(c(\beta)B_2^d\big).}
\]
The complete John contacts, in affine coordinates \(A^{-1}y\), are the \(2^d\) points with each coordinate equal to \(\pm c(\beta/d)\). The complete Löwner contacts are the \(2d\) points \(\pm c(\beta)e_i\). In particular the exact multiplicative Banach–Mazur distance to Euclidean space is
\[
\boxed{d_{\mathrm{BM}}(T_{K,\beta},B_2^d)=
\frac{c(\beta)}{\sqrt d\,c(\beta/d)}.}
\]
For fixed \(d\ge2\), this ratio is **strictly increasing** in \(\beta\), from \(1\) as \(\beta\downarrow0\) to \(\sqrt d\) as \(\beta\to\infty\). For fixed \(\beta>0\), it is **strictly increasing in the integer dimension \(d\ge1\)** and has the finite high-dimensional limit
\[
\boxed{\lim_{d\to\infty}d_{\mathrm{BM}}(T_{K,\beta},B_2^d)
=\frac{c(\beta)}{\sqrt{2\beta}}.}
\]
In the coordinates of \(A\), the normalized bodies converge in Euclidean Hausdorff distance, for each fixed \(d\), as
\[
\frac1{\sqrt{2\beta}}A^{-1}T_{K,\beta}\longrightarrow B_2^d
\quad(\beta\downarrow0),\qquad
\frac1\beta A^{-1}T_{K,\beta}\longrightarrow B_1^d
\quad(\beta\to\infty).
\]

## Assumptions and scope

The Euclidean unit ball is \(B_2^d=\{x: \sum x_i^2\le1\}\), and the cross-polytope is \(B_1^d=\{x:\sum|x_i|\le1\}\). The surface integrand is interpreted on relative interiors of facets of the polytope \(K\). The determinant-one assumption fixes the scale of the boundary integral; general parallelotopes of other volumes obey a corresponding rescaling of \(\beta\). All listed ellipsoids are affine images of Euclidean balls and are centered at the origin. We use the multiplicative Banach–Mazur distance, not its logarithm. The formula describes a **facet-defined Orlicz body** for a nonsmooth parallelotope, not a theorem asserting convergence of smoothed covariogram level sets for nonsmooth polytopes.

## Proof

**1. Facet reduction and affine covariance.** For \(Q=[-1/2,1/2]^d\), each facet has area \(1\), outer normal \(\pm e_i\), and support distance \(1/2\). The two facets indexed by \(i\) contribute \(\log\cosh y_i\) together. Hence \(\Phi_Q(y)=\sum_i\log\cosh y_i\). Under \(K=AQ\) with \(|\det A|=1\), the unit normal at an affine image of a facet has direction \(A^{-T}e_i\); the product of its support distance and area is still \(1/2\). The argument of \(\log\cosh\) becomes the \(i\)-th coordinate of \(A^{-1}y\). Consequently \(\Phi_K(y)=\Phi_Q(A^{-1}y)\).

**2. Exact inner and outer Euclidean radii.** Write \(f(t)=\log\cosh t\) for \(t\ge0\), and \(g(u)=f(\sqrt u)\) for \(u\ge0\). For \(u=t^2>0\), direct differentiation gives
\[
 g''(u)=\frac{t\operatorname{sech}^2t-\tanh t}{4t^3}<0.
\]
Indeed \(q(t)=\tanh t-t\operatorname{sech}^2t\) starts at zero and has derivative \(2t\operatorname{sech}^2t\tanh t>0\). Thus \(g\) is strictly concave, increasing, and vanishes at zero.

For every \(z\) of Euclidean norm \(r\), Jensen's inequality gives
\[
 \sum_{i=1}^d f(|z_i|)=\sum_i g(z_i^2)
 \le d g(r^2/d)=d\log\cosh(r/\sqrt d),
\]
with equality precisely when all \(|z_i|\) are equal (for \(r>0\)). Since a nonnegative concave function vanishing at zero is subadditive, we also have
\[
 \sum_i g(z_i^2)\ge g\!\left(\sum_i z_i^2\right)=\log\cosh r,
\]
with equality precisely when at most one coordinate is nonzero. Therefore the maximum and minimum of the modular on any sphere of radius \(r\) occur at signed diagonals and coordinate axes, respectively. The ball of radius \(\sqrt d\,c(\beta/d)\) is contained in the modular sublevel set, with exactly \(2^d\) boundary contacts. That body is contained in the ball of radius \(c(\beta)\), with exactly \(2d\) boundary contacts.

**3. Global ellipsoids and Banach–Mazur optimality.** The modular sublevel set is centrally symmetric and invariant under every signed coordinate permutation. Standard uniqueness of John and Löwner ellipsoids and this group invariance force both ellipsoids to be centered Euclidean balls, establishing their exact shapes from Step 2. For Banach–Mazur distance, suppose some positive-definite quadratic form \(Q\) achieves the multiplicative bound \(\|z\|_T^2\le z^TQz\le D^2\|z\|_T^2\) for all \(z\), after a common rescaling. Averaging \(Q\) over the signed permutation group preserves these linear inequalities and produces \(Q_0=\lambda I\). Thus no ellipsoid improves on a centered Euclidean ball; its best ratio is exactly \(c(\beta)/(\sqrt d\,c(\beta/d))\). Translating an ellipsoid cannot help for a centrally symmetric body: symmetrization of containment inequalities permits a centered one with no larger ratio.

**4. Strict level and dimension monotonicity.** Define \(h(s)=c(s)^2\), with \(h(0)=0\). Differentiating \(s=f(c(s))\) gives
\[
 h''(s)=\frac{2(\tanh t-t\operatorname{sech}^2t)}{\tanh^3t}>0,
 \qquad t=c(s)>0.
\]
Strict convexity implies \(h(s)/s\) is strictly increasing. Hence \(d h(\beta/d)=\beta[h(\beta/d)/(\beta/d)]\) strictly decreases as the integer \(d\) grows. The distortion is strictly increasing in \(d\).

To establish level monotonicity, set \(E(s)=s h'(s)/h(s)\). With \(s=f(t)\), one has \(E(s)=2f(t)/(t\tanh t)\). The ratio of the derivatives of numerator and denominator is
\[
 \frac{f'(t)}{(t\tanh t)'}
 =\frac1{1+2t/\sinh(2t)},
\]
which increases strictly on \(t>0\). The monotone form of l'Hôpital's rule (or an elementary weighted-average argument integrating those two derivatives from zero) shows that \(f(t)/(t\tanh t)\) increases strictly. Thus \(E(s)\) is strictly increasing. Differentiating the logarithm of the squared distortion gives
\[
 \frac{d}{d\beta}\log\left[\frac{h(\beta)}{d h(\beta/d)}\right]
 =\frac{E(\beta)-E(\beta/d)}\beta>0
 \quad(d>1).
\]

**5. Endpoints and limit shapes.** The expansions \(\log\cosh t=t^2/2+O(t^4)\) as \(t\to0\), \(\log\cosh t=|t|-\log2+o(1)\) as \(|t|\to\infty\), imply \(c(s)\sim\sqrt{2s}\) at zero and \(c(s)=s+\log2+o(1)\) at infinity. Substitution establishes both level limits, the finite dimension limit, and the normalized convergence to the Euclidean and cross-polytope balls. For the latter, uniform convergence on bounded sets of the rescaled modulars and their coordinatewise bounds yield Hausdorff convergence of their compact sublevel sets.

## Verification

The dependency-free script `verify_transition.py` checks the facet-reduced formulas, all predicted contacts, randomly sampled Euclidean directions for the two bounding inequalities, and strict numerical monotonicity for multiple dimensions and levels. It prints `LOGCOSH_TRANSITION_NUMERICAL_OK 7575` upon success. These are **finite numerical diagnostics only**; the proofs of all-dimensional optimality, strictness and the limit relations are Steps 1–5 above.

## Relationship to prior work

Haddad, Jiménez and Resende introduced the critical log-cosh boundary integral for the smooth-covariogram transition. Their main limiting theorem is proved under boundary smoothness assumptions; the modular integral is still meaningful on the relative interiors of polytope facets. The present determination on parallelotopes concerns exact classical ellipsoids, contact sets, and Banach–Mazur distortion throughout the level parameter and dimension, none asserted as consequences of the smooth limiting theorem. Lutwak, Yang and Zhang introduced the general Orlicz projection-body framework; this is a special explicit facet computation within that broader geometric context. Published analyses of mixed-power Musielak–Orlicz balls and other symmetric norm bodies solve distinct functionals and do not state this log-cosh profile. General theorems about invariant ellipsoids provide key methods but not the explicit level-dependent contact scales and strict profile.

## Limitations

No statement is made about smoothed-covariogram level-set convergence for polytopes; the critical functional is used as a direct facet definition. The explicit formulas rely on the parallelotope's equal-volume affine cube structure. The uniqueness and contact statements are for ellipsoids in the Euclidean affine model. Search and manuscript comparison cannot guarantee historical priority: an equivalent treatment of log-cosh Orlicz balls in specialized earlier literature remains possible. Independent mathematical audit has not been performed.

## References

- Julián Haddad, C. Hugo Jiménez, Matheus Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700 (first public October 8, 2026), https://arxiv.org/abs/2610.11700. Source for the critical boundary modular and its smooth-body context; inspected Sections 1 and 5–6 of the full preprint.
- Erwin Lutwak, Deane Yang, Gaoyong Zhang, *Orlicz projection bodies*, Advances in Mathematics 223 (2010), 220–242, DOI:10.1016/j.aim.2009.08.002. Foundational framework; abstract accessible, full paper not accessible during this research.
- Grigory Ivanov, Márton Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781. Background on distinct functional ellipsoid problems.
