# Entropy boundary layers for random widths of finite-dimensional norm balls

## Finding

Fix an integer \(d\ge2\), and let \(1<p<\infty\) with Hölder conjugate \(q=p/(p-1)\). Let \(K=B_p^d=\{x\in\mathbb R^d:\sum_{i=1}^{d}|x_i|^p\le1\}\). For Haar-uniform \(U\) on the Euclidean unit sphere \(S^{d-1}\), let \(W_p(U)\) denote the distance between the two supporting hyperplanes of \(K\) perpendicular to \(U\). Define

\[
W_p(U)=2\|U\|_q,\qquad s=d-1,\qquad
A_d=\frac{2\pi^{d/2}}{\Gamma(d/2)},\qquad
\kappa_s=\frac{\pi^{s/2}}{\Gamma(1+s/2)},\qquad
V_{s,q}=\frac{(2\Gamma(1+1/q))^s}{\Gamma(1+s/q)},\qquad
f_q=d^{1/q-1/2}.
\]

**Theorem (all fixed finite dimensions).** For each fixed \(q\ne2\), as \(\varepsilon\downarrow0\), all extreme-width probabilities have the following sharp equivalents:

* If \(1<q<2\), then \(W_{\min}=2\), \(W_{\max}=2f_q\), and
  \[
  \Pr\{W_p\le2+\varepsilon\}\sim
  \frac{2dV_{s,q}}{A_d}\left(\frac q2\right)^{s/q}\varepsilon^{s/q},
  \qquad
  \Pr\{W_p\ge2f_q-\varepsilon\}\sim
  \frac{2^d\kappa_s}{A_d((2-q)f_q)^{s/2}}\varepsilon^{s/2}.
  \]
* If \(2<q<\infty\), then \(W_{\min}=2f_q\), \(W_{\max}=2\), and
  \[
  \Pr\{W_p\le2f_q+\varepsilon\}\sim
  \frac{2^d\kappa_s}{A_d((q-2)f_q)^{s/2}}\varepsilon^{s/2},
  \qquad
  \Pr\{W_p\ge2-\varepsilon\}\sim
  \frac{2d\kappa_s}{A_d}\varepsilon^{s/2}.
  \]

The \(2d\) coordinate-axis directions and \(2^d\) equal-magnitude diagonal directions are, respectively, the unique types of extremizers. Each extreme event chooses among the relevant discrete directions asymptotically uniformly. After translating to a tangent chart and scaling by \(\varepsilon^{1/q}\) in the \(q<2\) axis-minimum case, its local direction is uniform on \(\{z\in\mathbb R^s:(2/q)\sum|z_i|^q\le1\}\). For the other three events, tangent scaling by \(\sqrt\varepsilon\) produces the uniform distribution on \(\{z:\|z\|_2^2\le1\}\) at a \(q>2\) axis maximum, or on \(\{z:|q-2|f_q\|z\|_2^2\le1\}\) at a diagonal extremum.

**The noncommuting Euclidean limit.** Let \(q\to2\), \(q\ne2\), in fixed dimension and define

\[
Z_q=\frac{W_p(U)-2}{2-q},\qquad
H(U)=-\sum_{i=1}^{d}U_i^2\log(U_i^2),
\]

using \(0\log0=0\). Uniformly in \(U\in S^{d-1}\),

\[
Z_q=\frac12H(U)+O_d(|q-2|).
\]

In particular \(Z_q\) converges in distribution (indeed in uniform coupling) to \(Z=H(U)/2\), supported on \([0,\tfrac12\log d]\). The squared coordinates of \(U\) have the symmetric \(\operatorname{Dirichlet}(1/2,\ldots,1/2)\) law. This limiting distribution has the sharp, different endpoint laws

\[
\boxed{\displaystyle
\Pr\{Z\le t\}\sim\frac{2d\kappa_s}{A_d}
\left(\frac{2t}{\log(1/t)}\right)^{s/2},\qquad
\Pr\{Z\ge\tfrac12\log d-t\}\sim\frac{2^d\kappa_s}{A_d}t^{s/2}
}\quad(t\downarrow0).
\]

At the lower endpoint, conditioning on \(Z\le t\) and dividing the coordinate-axis tangent displacement by \(\sqrt{2t/\log(1/t)}\) gives the uniform unit Euclidean \(s\)-ball limit; at the upper endpoint, conditioning on \(Z\ge\tfrac12\log d-t\) and dividing diagonal tangent displacement by \(\sqrt t\) gives the same marked limit. Thus the fixed-\(q<2\) lower tail has exponent \(s/q\), whereas first taking the Euclidean limit yields a logarithmically corrected exponent \(s/2\).

## Assumptions and scope

All random directions use normalized rotation-invariant surface measure, not cone measure on a non-Euclidean sphere or a random affine line. The width is the **full** projection length, not the support-function half-width. The dimension is fixed in each limit. The Hölder exponents satisfy \(1<p,q<\infty\); the exactly Euclidean case \(q=2\) has deterministic width \(2\) and is excluded from the fixed-\(q\) tails. Every asymptotic constant and exponent above depends only on \(d,q\) as displayed. No joint \(d\to\infty\) assertion is made.

## Proof

**Support and extremizers.** Hölder duality gives \(\sup_{x\in B_p^d}\langle x,u\rangle=\|u\|_q\), so central symmetry gives the stated width. The strict power-mean inequalities on \(S^{d-1}\) imply \(1\le\|u\|_q\le f_q\) when \(q<2\), and \(f_q\le\|u\|_q\le1\) when \(q>2\). In each case, equality at the value \(1\) occurs only at the \(2d\) signed coordinate vectors, while equality at \(f_q\) occurs only when all coordinate magnitudes equal \(d^{-1/2}\). This also proves that no other near-extremal regions contribute.

**Axis contact.** In a chart about the positive first coordinate axis write \(u=(\sqrt{1-\|z\|_2^2},z)\), \(z\in\mathbb R^s\). Its spherical area element is \((1-\|z\|_2^2)^{-1/2}dz=(1+O(\|z\|_2^2))dz\). Direct expansion of the defining norm, uniformly over the directions of \(z\), gives

\[
W_p(u)-2=\frac2q\sum_{j=1}^{s}|z_j|^q-\|z\|_2^2+o\!\left(\|z\|_2^q+\|z\|_2^2\right).
\]

For \(q<2\), the leading term is \((2/q)\sum|z_j|^q\), uniformly because the \(\ell_q\) and Euclidean norms are equivalent on \(\mathbb R^s\). The corresponding tangent sublevel region has volume \(V_{s,q}(q\varepsilon/2)^{s/q}\). For \(q>2\), the leading width *deficit* is \(\|z\|_2^2\), so its tangent sublevel region has volume \(\kappa_s\varepsilon^{s/2}\). Multiply by the \(2d\) disjoint axis charts and divide by \(A_d\). The same uniform expansions and rescaled Lebesgue-density convergence give the marked limits.

**Diagonal contact.** Fix a signed diagonal \(a\) with \(a_i=\pm d^{-1/2}\). Write \(u=\sqrt{1-\|z\|_2^2}\,a+z\), where \(z\perp a\). All coordinates of \(a\) are nonzero, so the \(q\)-norm is smooth nearby. Its spherical gradient vanishes and its tangent Hessian is exactly \((q-2)f_q I_s\). Consequently

\[
W_p(u)=2f_q+(q-2)f_q\|z\|_2^2+O_{d,q}(\|z\|_2^3).
\]

The induced area element is \((1+O(\|z\|_2^2))dz\). Integration over the local radius \(\sqrt{\varepsilon/(|q-2|f_q)}\), followed by multiplication by \(2^d\), proves both diagonal coefficients and their uniform-ball marks.

**Euclidean-parameter expansion.** Put \(t_i=u_i^2\), so \(\sum t_i=1\). For \(\delta=2-q\),
\[
\|u\|_{2-\delta}=\left(\sum_i t_i^{1-\delta/2}\right)^{1/(2-\delta)}.
\]
Because \(x^a\log^k x\) is uniformly bounded on \(0\le x\le1\) for \(a\) in a fixed neighborhood of \(1\) and \(k=1,2\), Taylor's formula is uniform on the entire closed simplex. Thus \(\log\|u\|_{2-\delta}=\delta H(u)/4+O_d(\delta^2)\), proving \(Z_q=H(u)/2+O_d(|\delta|)\). The Dirichlet law follows by dividing independent standard Gaussian squares by their sum.

**Entropy boundary layers.** Near an axis, writing \(z=rv\), \(\|v\|_2=1\), gives uniformly in \(v\)
\[
H(u)=r^2\log(1/r^2)+r^2\left(1-\sum_{j=1}^{s}v_j^2\log v_j^2\right)+O(r^4).
\]
The term in parentheses is bounded for fixed \(s\), so \(H\le2t\) is asymptotically the Euclidean tangent ball with squared radius \(2t/\log(1/t)\). Multiplication by \(2d\kappa_s/A_d\) yields the first limit. Near a diagonal, the entropy Hessian on the tangent sphere is \(-4I_s\), giving \(H(u)=\log d-2\|z\|_2^2+O_d(\|z\|_2^3)\). Hence \(Z\ge\log d/2-t\) is asymptotically the tangent ball of squared radius \(t\). Its \(2^d\) charts give the second limit. Uniform chart rescaling and convergence of the area density establish both conditional marked limits.

## Verification

A standalone finite diagnostic script `check.py` evaluates the exact dual-norm width and the analytic coefficients in several dimensions and exponents. It tests both axis and diagonal local expansions, inverts the exact angular width in dimension two to compare endpoint probabilities, and tests the Euclidean-parameter entropy expansion and its two local forms. The script is executable with Python, NumPy, and SciPy and has no external data dependencies. Its finite numerical tests are not a proof of any limiting statement; the argument above supplies those limits.

## Relationship to prior work

Barthe, Guédon, Mendelson, and Naor (first public arXiv version, March 29, 2005) studied \(\ell_p\)-ball geometry using probabilistic representations and spherical norm moments. Their results motivate this directional-support problem, but do not assert the displayed fixed-dimensional near-extreme width laws or the Euclidean-parameter entropy endpoint laws. Gorbunov, Vorontsova, and Gasnikov (first arXiv version, April 10, 2018) investigated expectations and concentration of Euclidean-spherical \(q\)-norms, rather than exact fixed-dimensional endpoint probabilities. Kaufmann (June 2021) studied sharp large deviations of the length of random one-dimensional projections in an asymptotic \(d\to\infty\) regime; its Section 3.3 verifies the support-width identification but not the fixed-\(d\), \(\varepsilon\to0\) or \(q\to2\) laws here.

Related geometric and functional-analytic results concerning random chords in norm balls, covariance of projection-width powers, and entropy first variations of hyperplane-section volumes concern different random experiments or functionals, and do not directly imply these precise width distributions. Historical priority cannot be certified solely by the inspected sources.

## Limitations

All asymptotics are pointwise in fixed dimension; the fixed-\(q\) extreme-width estimates are not uniform as \(q\to2\). The normalized Euclidean limit is a different order of limits, not a uniform crossover formula valid for every joint relationship between \(q-2\) and \(\varepsilon\). The theorem does not cover the nonsmooth endpoint bodies at \(p=1,\infty\), anisotropic coordinate weights, or random hyperplane section volumes. The mathematical proof has not received an independent audit, and undiscovered prior formulations remain a possibility.

## References

1. F. Barthe, O. Guédon, S. Mendelson, A. Naor, *A probabilistic approach to the geometry of the \(\ell_p^n\)-ball*, Ann. Probab. 33 (2005), 480–513. First arXiv posting March 29, 2005. https://arxiv.org/abs/math/0503650
2. E. Gorbunov, E. Vorontsova, A. Gasnikov, *On the upper bound for the mathematical expectation of the norm of a vector uniformly distributed on the sphere and the phenomenon of concentration of uniform measure on the sphere*, arXiv:1804.03722 (first posting April 10, 2018). https://arxiv.org/abs/1804.03722
3. T. Kaufmann, *Sharp asymptotics for \(q\)-norms of random vectors in high-dimensional \(\ell_p^n\)-balls*, Modern Stochastics: Theory and Applications 8 (2021), 239–274. https://doi.org/10.15559/21-VMSTA182
