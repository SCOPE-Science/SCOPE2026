# A two-to-three-node instability transition for periodized Korobov cubature

## Finding

**Theorem (sharp boundary-cluster weight law).** Let \(N\geq 3\) be an integer, \(h=1/N\), and let \(J_2=\{0,h\}\), \(J_3=\{0,h,2h\}\) be subsets of the one-dimensional lattice of mesh \(h\). Consider the univariate, smoothness-two, unit-weight Korobov kernel
\[
K(t,u)=1+2\sum_{k=1}^{\infty}\frac{\cos(2\pi k(t-u))}{k^4},
\]
and the sine-periodization density \(\mu(u)=\frac\pi2|\sin(2\pi u)|\). Define \(\kappa(t)=\int_0^1 K(t,u)\mu(u)\,du\). The optimal unregularized kernel-integration weights on \(J_r\), \(r=2,3\), are the unique real solutions \(w^{(r)}\) of
\[
\left[K(t_i,t_j)\right]_{t_i,t_j\in J_r} w^{(r)}
=\left[\kappa(t_i)\right]_{t_i\in J_r}.
\]
Put
\[
 k_0=1+\frac{\pi^4}{45},\qquad a=\frac{2\pi^4}{3},\qquad
 b_0=\frac{\pi^2}{12}+\frac{\pi^4}{720},\qquad
 b_2=4\pi^2-\frac{\pi^4}{3}>0,
\]
\[
 A=\frac{b_0}{8k_0}+\frac{b_2}{16a}=0.0445757926701356\ldots>0.
\]
Then the two-node weights stay bounded and have limits
\[
\lim_{N\to\infty}(w^{(2)}_0,w^{(2)}_1)
=\left(\frac{b_0}{2k_0}-\frac{b_2}{4a},\frac{b_0}{2k_0}+\frac{b_2}{4a}\right),
\]
whereas the three-node weights, ordered by \(0,h,2h\), satisfy
\[
 \boxed{\quad\lim_{N\to\infty}\frac1N(w^{(3)}_0,w^{(3)}_1,w^{(3)}_2)
 =A(1,-2,1).\quad}
\]
Consequently, the middle weight is negative for all sufficiently large \(N\), the sharp bounded-data sensitivity is \(\|w^{(3)}\|_1=4AN+O(1)\), and the amplification of independent, centered, equal-variance evaluation errors satisfies
\[
 \operatorname{Var}\left(\sum_{j=0}^2w^{(3)}_j\epsilon_j\right)
 =6\sigma^2A^2N^2+O_\sigma(N),\qquad \operatorname{Var}(\epsilon_j)=\sigma^2.
\]
Thus, for this prescribed boundary-cluster family, adding a third nearby lattice node changes bounded weights into linearly diverging signed weights; this does **not** assert instability of typical random subsamples or complete lattices.

## Assumptions and scope

The quadrature is the unmodified exact kernel-integral rule on the specified, distinct lattice sites. The smoothness parameter is exactly \(\alpha=2\), the single-coordinate Korobov weight is \(\gamma=1\), and the periodization is \(x=\sin^2(\pi t)\). The actual physical integration nodes are \(\sin^2(\pi j/N)\), which are distinct for \(j=0,1,2\) when \(N\geq5\). The asymptotic claim is for integers \(N\to\infty\), so the distinctness of physical nodes holds throughout the relevant tail. The kernel Gram matrices are invertible because every Fourier coefficient is strictly positive and the sample sites are distinct modulo one. The variance assertion assumes independent observation errors with finite common variance and is a conditional noise-sensitivity identity, not a claim about the underlying deterministic integrand.

## Proof

**1. Exact kernel and kernel mean.** The Bernoulli-polynomial Fourier identity gives, for \(0\leq t\leq1\),
\[
 K(t,0)=k_0-a(t^2-2t^3+t^4).
\]
The normalized nonnegative density has Fourier expansion
\[
 \mu(t)=1-2\sum_{\ell=1}^{\infty}\frac{\cos(4\pi\ell t)}{4\ell^2-1}.
\]
Convolution with the above Korobov kernel yields
\[
 \kappa(t)=1-\frac18\sum_{\ell=1}^{\infty}
 \frac{\cos(4\pi\ell t)}{\ell^4(4\ell^2-1)}.
\]
It is even, has four continuous derivatives, and near zero obeys \(\kappa(t)=b_0+\frac12b_2t^2+O(t^4)\). Indeed, use \(\sum_{\ell\geq1}(4\ell^2-1)^{-1}=1/2\), the evaluations \(\zeta(2)=\pi^2/6\) and \(\zeta(4)=\pi^4/90\), and the partial fractions
\[
\frac1{\ell^2(4\ell^2-1)}=-\frac1{\ell^2}+\frac4{4\ell^2-1},\qquad
\frac1{\ell^4(4\ell^2-1)}=-\frac1{\ell^4}-\frac4{\ell^2}+\frac{16}{4\ell^2-1}.
\]
These give exactly \(\kappa(0)=b_0\) and \(\kappa''(0)=b_2\). Positivity of \(b_2\) follows from \(\pi^2<12\).

**2. Two-site stability.** Set \(K_1=K(h,0)\). For the two-site rule, adding and subtracting the equations yields
\[
 w^{(2)}_0+w^{(2)}_1=\frac{\kappa(0)+\kappa(h)}{k_0+K_1},\qquad
 w^{(2)}_0-w^{(2)}_1=\frac{\kappa(0)-\kappa(h)}{k_0-K_1}.
\]
Since \(k_0-K_1=ah^2+O(h^3)\), the first quotient tends to \(b_0/k_0\) and the second to \(-b_2/(2a)\). The asserted finite limits follow.

**3. Three-site singular amplification.** Write \(K_2=K(2h,0)\), \(u=(w^{(3)}_0+w^{(3)}_2)/2\), and \(v=w^{(3)}_1\). Averaging the outer equations and retaining the central equation gives
\[
(k_0+K_2)u+K_1v=\frac{\kappa(0)+\kappa(2h)}2,\qquad
2K_1u+k_0v=\kappa(h).
\]
The determinant of this two-by-two system is
\[
\Delta_h=k_0(k_0+K_2)-2K_1^2=8k_0a h^3+O(h^4).
\]
The numerator of \(u\) is
\[
 \frac{k_0}{2}(\kappa(0)+\kappa(2h))-K_1\kappa(h)
 =\left(\frac{k_0b_2}{2}+ab_0\right)h^2+O(h^3).
\]
Therefore \(u=A/h+O(1)\) with precisely the positive constant stated in the theorem; the central equation gives \(v=-2A/h+O(1)\). Subtracting the two outer equations yields
\[
 (k_0-K_2)(w^{(3)}_0-w^{(3)}_2)=\kappa(0)-\kappa(2h),
\]
so \(w^{(3)}_0-w^{(3)}_2\to-b_2/(2a)\) and both outer weights equal \(A/h+O(1)\). This establishes the vector limit and eventual signs.

**4. Exact amplification.** The operator norm of the quadrature functional on arbitrary bounded nodal perturbations is the sum of absolute weights, giving \(4AN+O(1)\). Independent centered errors have variance exactly \(\sigma^2\sum_{j=0}^{2}(w^{(3)}_j)^2\), giving \(6\sigma^2A^2N^2+O_\sigma(N)\). No distributional assumption beyond independence, centering and common finite variance is required.

## Verification

The accompanying `verify.py` reconstructs the kernel and kernel-mean series independently, solves the two- and three-site Gram systems at increasing mesh resolutions with high-precision arithmetic, checks the exact Fourier/Bernoulli identities, and verifies convergence to the declared asymptotic coefficients. Computation illustrates the analytic limit; it does not replace the proof. For example, at \(N=128\) the computed middle three-site weight is approximately \(-11.531322\), versus the leading prediction \(-2AN\approx-11.411403\).

## Relationship to prior work

Bartel, Gilbert, Griebel, Kuo and Sloan introduce periodized kernel-integral weights and the subsampled solve \(K_Jw_J=\kappa_J\), and discuss conditioning and asymptotic positivity. Their convergence results treat properly selected full/subsampled designs, not the particular collapsing three-site sequence here. Published results on full-lattice Korobov positivity likewise treat all \(N\) nodes, not a fixed three-node cluster. General warnings about clustered kernel interpolation do not by themselves supply the exact signed-vector constant, the protected two-node comparison, or the noise-variance coefficient proved here.

## Limitations

This concerns a deliberately unfavorable deterministic subset, not a representative random subset or the construction's claimed high-probability regime. It does not disprove any existing smooth-integrand convergence guarantee, and does not address regularized kernel solves, fixed positive separation, other smoothness parameters or higher dimensions. The stochastic amplification statement pertains to added independent evaluation noise, not the intrinsic deterministic quadrature error. Historical originality is assessed relative to the explicitly checked sources, not certified exhaustively.

## References

1. F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (public release 2026-10-01), https://arxiv.org/abs/2610.01113. Open preprint: https://ins.uni-bonn.de/media/public/publication-media/2604.pdf?pk=1973, esp. equations (4), (6), (13), (15), (16), (28) and Section 7.2.
2. *Quantified asymptotic positivity for higher-order periodized Korobov quadrature*, published published-finding corpus record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-quantified-asymptotic-positivity-for-higher-order-periodized-kor--feb80935de99.
3. *A roughness threshold and exact noise tails for colliding-node kernel quadrature*, published published-finding corpus record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-roughness-threshold-and-exact-noise-tails-for-colliding-node-k--841cfe0433d1.
