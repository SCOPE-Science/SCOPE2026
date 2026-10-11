# Exact Bernoulli-convolution oscillation law for constant-step BSPPA on two symmetric quadratics
## Finding
Consider vanilla Bregman stochastic proximal point iteration in Euclidean geometry, with \(h(x)=\tfrac12x^2\), on the two-component finite sum
\[
f_{+}(x)=\frac{a}2(x-c)^2,\qquad f_{-}(x)=\frac{a}2(x+c)^2,
\]
where \(a>0\), \(c>0\), and each component is sampled independently with probability \(1/2\). For every constant \(\alpha>0\), define \(t=\alpha a\) and \(r=(1+t)^{-1}\). The vanilla BSPPA recursion is exactly
\[
x_{k+1}=r x_k+(1-r)c\xi_k,
\]
where \(\xi_k\in\{-1,+1\}\) are independent Rademacher variables.

The chain has the unique stationary random variable
\[
X_\infty=(1-r)c\sum_{j=0}^\infty r^j\xi_j.
\]
Hence the stationary law is a scaled Bernoulli convolution. For deterministic \(x_0\),
\[
\mathbb E[x_k^2]=r^{2k}x_0^2+c^2\frac{1-r}{1+r}(1-r^{2k}).
\]
The average objective is \(F(x)=\tfrac a2(x^2+c^2)\), so \(F\) has the unique minimizer \(0\) and
\[
\lim_{k\to\infty}\mathbb E[F(x_k)-F(0)]
=\frac{a c^2 t}{2(2+t)}.
\]

There is also a sharp support transition at \(t=1\). When \(t>1\), equivalently \(r<\tfrac12\), the support is a disjoint self-similar Cantor set. When \(t=1\), equivalently \(r=\tfrac12\), the stationary law is uniform on \([-c,c]\). When \(0<t<1\), equivalently \(r>\tfrac12\), the support is all of \([-c,c]\). In the disjoint case its Hausdorff dimension is \(\log 2/\log(1/r)\).

## Assumptions and scope
The statement concerns the vanilla BSPPA update of Traoré and Ochs, specialized to Euclidean geometry, a scalar two-term finite sum, independent uniform component sampling, and a constant positive stepsize. Both component functions are \(a\)-strongly convex but have different minimizers \(\pm c\), so this is the minimal non-interpolating symmetric instance. The finding concerns the exact law of the iterates and not a variance-reduced BSPPA variant.

All formulas hold for every \(a>0\), \(c>0\), \(\alpha>0\), and deterministic finite \(x_0\). The topology statement is about the support of the stationary probability measure; for \(r>\tfrac12\) no assertion is made here about absolute continuity or singularity of that measure.

## Proof
For a sampled sign \(\xi\in\{-1,+1\}\), write \(f_\xi(x)=\tfrac a2(x-c\xi)^2\). Euclidean BSPPA minimizes
\[
f_\xi(x)+\frac{1}{2\alpha}(x-x_k)^2.
\]
The first-order condition is
\[
a(x-c\xi)+\alpha^{-1}(x-x_k)=0,
\]
which gives
\[
x_{k+1}=\frac{x_k+\alpha a c\xi_k}{1+\alpha a}
=r x_k+(1-r)c\xi_k.
\]
Iteration yields the exact finite-time representation
\[
x_k=r^k x_0+(1-r)c\sum_{j=0}^{k-1}r^{k-1-j}\xi_j.
\]
Because \(0<r<1\), the random series defining \(X_\infty\) converges absolutely almost surely. If two chains use the same signs, their distance is multiplied by \(r\) at each step. This contractive coupling gives uniqueness of the stationary law and geometric convergence in \(W_1\); for example,
\[
W_1(\mathcal L(x_k),\mathcal L(X_\infty))\le r^k(|x_0|+c).
\]

The signs are independent and centered, so cross terms vanish. Therefore
\[
\mathbb E[x_k^2]
=r^{2k}x_0^2+(1-r)^2c^2\sum_{j=0}^{k-1}r^{2j}
=r^{2k}x_0^2+c^2\frac{1-r}{1+r}(1-r^{2k}).
\]
Since \((1-r)/(1+r)=t/(2+t)\), the stated objective-error floor follows from \(F(x)-F(0)=\tfrac a2x^2\).

For the support, the two affine maps are
\[
T_-(x)=rx-(1-r)c,\qquad T_+(x)=rx+(1-r)c.
\]
On \([-c,c]\), their images are
\[
T_-([-c,c])=[-c,c(2r-1)],\qquad
T_+([-c,c])=[c(1-2r),c].
\]
If \(r<\tfrac12\), these images are disjoint and the invariant attractor is the usual two-map self-similar Cantor set; the open-set condition gives dimension \(\log 2/\log(1/r)\). If \(r>\tfrac12\), the two images overlap and their union is exactly \([-c,c]\), so uniqueness of the compact IFS attractor makes the support that full interval. If \(r=\tfrac12\), then
\[
X_\infty=c\sum_{j=0}^\infty\frac{\xi_j}{2^{j+1}},
\]
which is the centered binary expansion of a uniform random variable on \([-c,c]\).

## Verification
The standalone checker `verify_stationary_law.py` evaluates the closed-form second moment and objective floor for multiple parameter values, verifies the algebraic equivalence between the threshold \(r=\tfrac12\) and \(\alpha a=1\), and checks the first-level support geometry. A seeded Monte Carlo replay is included only as a numerical sanity check; it is not used as proof. Its stored output is `verification_output.txt` and reports `VERIFY_OK`.

## Relationship to prior work
Traoré and Ochs introduce BSPPA and, for vanilla BSPPA, explicitly discuss the need for vanishing stepsizes in the non-interpolating setting and the oscillatory behavior observed under a constant stepsize. The present finding specializes their vanilla update to the smallest symmetric non-interpolating quadratic instance and resolves that qualitative oscillation exactly as a Bernoulli-convolution Markov chain.

Earlier work of Traoré, Apidopoulos, Salzo, and Villa develops variance-reduced stochastic proximal point methods and emphasizes the role of persistent variance for vanilla SPPA. Bianchi, Hachem, and Salim study constant-step stochastic forward-backward/proximal iterations through homogeneous Feller Markov chains and invariant measures. Those general frameworks motivate invariant-measure analysis, but the inspected statements do not supply the explicit two-quadratic stationary series, exact optimization-error floor, or the \(\alpha a=1\) support transition derived here. The support calculation itself is elementary from the two affine maps and does not rely on a novelty claim about Bernoulli convolutions as probability measures.

## Limitations
This is an exact model result for one-dimensional symmetric equal-curvature quadratics with uniform two-point sampling. Unequal curvatures, unequal sampling probabilities, higher-dimensional noncommuting Hessians, and Bregman kernels other than the Euclidean quadratic can lead to different affine or nonlinear invariant laws. For \(0<\alpha a<1\), only the support is claimed to be the full interval; no claim is made about whether the Bernoulli-convolution measure has a density for a particular parameter.

A residual literature risk remains that an older stochastic-proximal example, under different terminology, may have written down the same two-map Bernoulli-convolution specialization. The closest full-text and database checks found general invariant-measure theory and SPPA variance analyses rather than this exact algorithm-specific law.

## References
1. C. Traoré and P. Ochs, *Bregman Stochastic Proximal Point Algorithm with Variance Reduction*, arXiv:2510.16655v1, 2025.
2. C. Traoré, V. Apidopoulos, S. Salzo, and S. Villa, *Variance Reduction Techniques for Stochastic Proximal Point Algorithms*, Journal of Optimization Theory and Applications 203 (2024), 1910–1939, doi:10.1007/s10957-024-02502-6.
3. P. Bianchi, W. Hachem, and A. Salim, *A Constant Step Forward-Backward Algorithm Involving Random Maximal Monotone Operators*, Journal of Convex Analysis 26 (2019), 397–436; arXiv:1702.04144v3.
