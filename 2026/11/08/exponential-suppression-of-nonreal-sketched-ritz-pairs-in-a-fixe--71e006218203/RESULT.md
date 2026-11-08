# Exponential suppression of nonreal sketched Ritz pairs in a fixed symmetric model

## Finding
For the Gaussian sketched Rayleigh–Ritz map on the fixed positive-definite family below, the probability of a nonreal conjugate pair is exactly a one-dimensional angular integral for **every** integer sketch dimension \(s\ge3\). Writing \(h=\delta/(2\sqrt{2}t)>0\) and \(q=1+h^2\), it has the sharp asymptotic
\[
\Pr\{\text{nonreal pair}\}=\frac{q}{h\sqrt{3\pi s}}\,q^{-s/2}\bigl(1+o(1)\bigr),\qquad s\to\infty.
\]
The probability is strictly positive for every finite \(s\). Thus, at fixed spectral gap, Gaussian oversampling suppresses but does not deterministically eliminate the real-Schur two-by-two blocks arising from a symmetric original problem. The result applies equally to an arbitrarily large ambient dimension and to genuine dimension-reducing sketches.

## Assumptions and scope
Fix integers \(n\ge3\), \(s\ge3\); positive \(\alpha,\delta,t\); and \(\mu>t^2(1/\alpha+1/(\alpha+\delta))\). If \(n>3\), let \(D\) be any positive-definite real \((n-3)\)-by-\((n-3)\) matrix. Define
\[
A=\begin{pmatrix}\alpha&0&t\\0&\alpha+\delta&t\\t&t&\mu\end{pmatrix}\oplus D,
\qquad X=[e_1,e_2]\in\mathbb R^{n\times2}.
\]
For \(n=3\) the \(D\) block is absent. The Schur-complement criterion makes \(A\) positive definite. Let \(S\in\mathbb R^{s\times n}\) have independent standard normal entries and let
\[
M_s=(SX)^\dagger(SAX)\in\mathbb R^{2\times2}.
\]
Almost surely \(SX\) has full column rank; the eigenvalues of \(M_s\) are also those of the sketched, basis-whitened two-dimensional compression. Scaling every sketch entry by \(s^{-1/2}\) leaves \(M_s\) unchanged. If \(n>s\), the same statement concerns a strictly dimension-reducing sketch.

Set \(h=\delta/(2\sqrt2t)\). For \(0\le\phi\le\pi/4\) put
\[
\ell(\phi)=\frac{2h}{\cos\phi+\sqrt{\cos(2\phi)}},\qquad
u(\phi)=\frac{2h}{\cos\phi-\sqrt{\cos(2\phi)}}
\]
with \(\nu(0)=+\infty\). Then the **exact finite-sample law** is
\[
\boxed{p_s(h)=\frac1\pi\int_0^{\pi/4}\left[
(1+\ell(\phi)^2)^{-(s-1)/2}-(1+\nu(\phi)^2)^{-(s-1)/2}
\right]d\phi.}
\]
For all finite \(s\ge3\) and \(h>0\), \(0<p_s(h)<1/2\). In particular the sharp exponential decay rate is \(\lim_{s\to\infty}-s^{-1}\log p_s(h)=\tfrac12\log(1+h^2)\), with the stated explicit subexponential prefactor.

## Proof
**1. Regression reduction.** Write \(G=SX\), and let \(w=Se_3\). The columns of \(G\) and \(w\) are independent standard Gaussian vectors. Since
\[
SAX=G\operatorname{diag}(\alpha,\alpha+\delta)+w(t,t),
\]
the two-dimensional reduced matrix equals
\[
M_s=\begin{pmatrix}\alpha+t v_1&t v_1\\t v_2&\alpha+\delta+t v_2\end{pmatrix},\qquad
v=(G^TG)^{-1}G^Tw.
\]
Conditional on \(G\), the vector \(v\) is normal with covariance \((G^TG)^{-1}\). The Gram matrix \(G^TG\) is Wishart with \(s\) degrees of freedom and identity scale. Integrating its density against the conditional normal density, and applying the rank-one determinant identity, yields a rotationally invariant density proportional to \((1+\|v\|^2)^{-(s+1)/2}\). Direct polar integration fixes the constant:
\[
 f_s(v_1,v_2)=\frac{s-1}{2\pi}(1+v_1^2+v_2^2)^{-(s+1)/2}.
\]
This argument requires only \(s\ge2\), although the theorem concerns \(s\ge3\).

**2. Exact nonreal region.** Let \(u=(v_1+v_2)/\sqrt2\) and \(b=(v_1-v_2)/\sqrt2\). The characteristic discriminant is exactly
\[
\Delta_s=(\operatorname{tr}M_s)^2-4\det M_s
=\delta^2-2\sqrt2\,\delta t\,b+2t^2u^2.
\]
Hence \(\Delta_s<0\) if and only if
\[
 b>h+\frac{u^2}{4h}.
\]
The event is a nonempty open parabola region. It is contained in \(\{b>0\}\), which has probability \(1/2\) by symmetry; both it and its complement contain nonempty open sets. Therefore \(0<p_s(h)<1/2\). Integrating the bivariate density gives the alternative exact form
\[
p_s(h)=\frac{s-1}{2\pi}\int_{\mathbb R}\int_{h+u^2/(4h)}^\infty
(1+u^2+b^2)^{-(s+1)/2}\,db\,du.
\]

**3. Angular quadrature.** Use polar coordinates \(u=r\cos\theta\), \(b=r\sin\theta\). The quadratic inequality in \(r\) has an admissible interval only if \(\pi/4<\theta<3\pi/4\). Writing \(\theta=\pi/2+\phi\), its two roots are \(\ell(|\phi|)\) and \(\nu(|\phi|)\). The radial antiderivative is
\[
\int r(1+r^2)^{-(s+1)/2}\,dr=-\frac{(1+r^2)^{-(s-1)/2}}{s-1}.
\]
Symmetry about \(\theta=\pi/2\) proves the one-dimensional formula with its stated endpoint convention.

**4. Sharp large-sketch asymptotics.** In the parabola integral substitute \(b=h+u^2/(4h)+c\), then \(u=U/\sqrt s\), \(c=C/s\). With \(q=1+h^2\), the quantity in the density is exactly
\[
1+u^2+b^2=q+\frac{3U^2/2+2hC}{s}
+\frac{(U^2/(4h)+C)^2}{s^2}.
\]
For fixed \(U\in\mathbb R\), \(C\ge0\), the scaled integrand tends to \(\exp[-(3U^2/2+2hC)/(2q)]\). Dominated convergence is justified, for all \(s\ge5\), by the integrable majorant \((1+(3U^2/2+2hC)/(5q))^{-5/2}\): the expression \((1+z/s)^{-s/2}\) decreases in \(s>0\) for every \(z\ge0\). Thus
\[
\lim_{s\to\infty}\sqrt{s}\,q^{s/2}p_s(h)
=\frac{q^{-1/2}}{2\pi}\int_{\mathbb R}\int_0^\infty
\exp\!\left[-\frac{3U^2/2+2hC}{2q}\right]dC\,dU
=\frac{q}{h\sqrt{3\pi}}.
\]
This proves the asymptotic and logarithmic rate.

## Verification
The accompanying standard-library script `verify_srr.py` checks the discriminant identity using exact rational inputs, verifies a full-rank deterministic three-row complex-pair example, evaluates the angular quadrature, compares it with independently generated Gaussian sketches, and examines convergence to the proved prefactor. Execute with `python3 verify_srr.py` from the extracted file directory. The finite checks support the derivation; the infinite-dimensional quantifiers in \(s\) rest on the analytic proof above.

For example, with \(\alpha=\delta=t=1\), \(\mu=2\), and
\[
 S=\begin{pmatrix}1&0&1\\0&1&-1\\0&0&1\end{pmatrix},
\]
we obtain the positive-definite matrix \(A=\left(\begin{smallmatrix}1&0&1\\0&2&1\\1&1&2\end{smallmatrix}\right)\) and \(M_s=\left(\begin{smallmatrix}2&1\\-1&1\end{smallmatrix}\right)\), with discriminant \(-3\). Its positive-probability Gaussian neighborhood yields a nonreal pair. For this family \(h=1/(2\sqrt2)\), and the quadrature gives \(p_3(h)\approx0.1924501\).

## Relationship to prior work
Nakatsukasa and Tropp introduce sketched Rayleigh–Ritz and explicitly note in their symmetric-case discussion that nonsymmetric reduced matrices can have nonreal eigenvalues. Liu and Liu develop a real Schur treatment of those nonreal blocks. The present result quantifies the **exact fixed-matrix Gaussian probability for all sketch row counts** and its exponential oversampling asymptotic in a minimal, structurally motivated coupled model. Shao studies a different square complex-Gaussian randomized Petrov–Galerkin projection and convergence of randomized Ritz pairs, not this real, oversampled nonreal-pair distribution.

## Limitations
The exact probability and prefactor apply to a two-vector trial subspace with a single coupled out-of-subspace direction and independent real Gaussian sketches. The other ambient directions may be arbitrary uncoupled positive-definite modes but cannot interact with the two trial vectors. No claim is made for all symmetric positive-definite matrices, structured/oblivious sparse sketches, finite-precision rounding, or the unconditional monotonicity of \(p_s(h)\) at small \(s\). The family is a model for Schur-block occurrence, not a convergence theorem for a full eigensolver.

## References
- J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261, first public 2026-10-15. https://arxiv.org/abs/2610.22261
- Y. Nakatsukasa and J. A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183–1214, Section 6.8. https://doi.org/10.1137/23M1565413
- N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037, 2026. https://arxiv.org/abs/2604.01037
