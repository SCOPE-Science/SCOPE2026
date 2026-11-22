# A sharp no-blur-to-complete-blur transition for log-determinant variable projection

## Finding

For the smallest nonconstant periodic convolution model, a log-determinant penalty intended to remove the no-blur degeneracy can instead produce a **discontinuous global switch directly to complete contrast annihilation**, without any optimal intermediate blur. The switch has an exact determinant-weight threshold; on a nonempty interval beyond it, the nonoptimal no-blur operator remains a strict local minimizer, separated from the global minimizer by a unique interior local maximum.

Precisely, let \(\ell>0\), \(d>0\), \(B>0\), and \(w\geq0\). Define

\[
L_d=\log\frac{1+d}{d},\qquad
w_{\mathrm{jump}}=\frac{B}{(1+\ell)L_d},\qquad
w_{\mathrm{local}}=\frac{\ell B(1+d)}{(1+\ell)^2}.
\]

If

\[
\boxed{\ell(1+d)L_d>1+\ell,}
\]

then the exact set of globally minimizing blur parameters \(s\in[0,1]\) is

\[
\boxed{
\operatorname*{argmin}_{0\le s\le1}J_w(s)=
\begin{cases}
\{1\},&0\le w<w_{\mathrm{jump}},\\
\{0,1\},&w=w_{\mathrm{jump}},\\
\{0\},&w>w_{\mathrm{jump}}.
\end{cases}}
\]

Moreover, whenever \(w_{\mathrm{jump}}<w<w_{\mathrm{local}}\), the global minimizer \(s=0\) and the strict nonglobal local minimizer \(s=1\) are separated by exactly one interior critical point, which is a strict local maximum. The auxiliary-scale condition is sharp for the **positive-width metastability window**: for each \(\ell>0\), there is one \(d_*(\ell)>0\) solving \(\ell(1+d_*)\log((1+d_*)/d_*)=1+\ell\); the strict ordering \(w_{\mathrm{jump}}<w_{\mathrm{local}}\) holds exactly for \(0<d<d_*(\ell)\). At equality the strict window closes.

## Assumptions and scope

For \(s\in[0,1]\), let the two-pixel periodic convolution matrix be

\[
A_s=\frac12\begin{pmatrix}1+s&1-s\\1-s&1+s\end{pmatrix}.
\]

It has nonnegative, unit-sum kernel coefficients and orthonormal Fourier eigenvectors \(v_+=(1,1)^\top/\sqrt2\), \(v_-=(1,-1)^\top/\sqrt2\), with eigenvalues \(1\) and \(s\). The endpoint \(s=1\) is identity/no blur; \(s=0\) is equal-neighbor averaging/full removal of the alternating Fourier mode.

Given any real observed vector \(b\) with \(B=|v_-^\top b|^2>0\), let image regularization \(\ell=\lambda^2>0\), auxiliary determinant scale \(d=\gamma>0\), reconstruction and auxiliary operators both be the identity, and choose a uniform base prior on \([0,1]\). Consider the exact regularized variable-projection functional

\[
J_w(s)=\min_{x\in\mathbb R^2}
\left\{\tfrac12\|A_sx-b\|_2^2+\tfrac{\ell}{2}\|x\|_2^2\right\}
+\tfrac{w}{2}\log\det(A_s^\top A_s+dI).
\]

The quadratic inner minimization is unique for all \(s\), including singular \(A_0\). The determinant is positive for \(d>0\). This is the two-pixel specialization of the objective in Dworaczyk–Español (2026), with \(w=\beta^2\), \(\ell=\lambda^2\), and \(d=\gamma\); no claim is made about higher-dimensional blur families or nonuniform base priors.

## Proof

**Fourier reduction.** Let \(b_+=v_+^\top b\) and \(b_-=v_-^\top b\). Direct minimization in the Fourier basis gives

\[
\widehat x_+(s)=\frac{b_+}{1+\ell},\qquad
\widehat x_-(s)=\frac{s b_-}{s^2+\ell}.
\]

The constant Fourier mode contributes only a term independent of \(s\). Writing \(a=s^2\in[0,1]\), the nonconstant part is exactly

\[
F_w(a)=\frac12\left(\frac{C}{a+\ell}+w\log(a+d)\right),\qquad C=\ell B>0.
\]

**Secant-ratio lemma.** For fixed \(\ell,d>0\), define for \(0\le a<1\)

\[
\tau(a)=\frac{1-a}{(1+\ell)(a+\ell)\log((1+d)/(a+d))},
\]

extended continuously by \(\tau(1)=(1+d)/(1+\ell)^2\). Then \(\tau\) has no interior local minimum and

\[
\min_{a\in[0,1]}\tau(a)=\min\left\{
\frac{1}{\ell(1+\ell)L_d},\ \frac{1+d}{(1+\ell)^2}\right\}.
\]

To prove this, put \(H(a)=\log((1+d)/(a+d))\) and

\[
T(a)=\frac{(1-a)(a+\ell)}{(1+\ell)(a+d)}-H(a).
\]

Multiplication by strictly positive factors shows \(\operatorname{sgn}\tau'(a)=\operatorname{sgn}T(a)\) for \(0<a<1\), while

\[
T(1)=0,\qquad
T'(a)=\frac{(1-a)(a+2d-\ell)}{(1+\ell)(a+d)^2}.
\]

If \(\ell\le2d\), then \(T\) increases to zero and \(\tau\) decreases. If \(\ell\ge1+2d\), then \(T\) decreases to zero and \(\tau\) increases. In the remaining case, \(T\) first decreases, then increases to zero, being strictly negative on the final increasing branch; any zero of \(T\) on the preceding branch crosses from positive to negative, so any interior extremum of \(\tau\) is a strict maximum. The continuous endpoint values therefore give the global minimum. If \(\tau(0)<\tau(1)\), the endpoint \(a=0\) is its *only* minimum, with strict inequality \(\tau(a)>\tau(0)\) for \(0<a\le1\).

**Exact global transition.** For \(0\le a<1\), subtraction yields

\[
F_w(a)-F_w(1)=\frac12\log\frac{1+d}{a+d}\left(C\tau(a)-w\right).
\]

The stated inequality \(\ell(1+d)L_d>1+\ell\) is equivalent to \(\tau(0)<\tau(1)\). Consequently \(C\tau(0)=w_{\mathrm{jump}}\) is the sharp global comparison threshold against the identity. If \(w<w_{\mathrm{jump}}\), the difference is strictly positive for every \(a<1\), giving the unique minimizer \(a=1\). At equality, \(F_w(0)=F_w(1)\) and all interior values are strictly larger. If \(w>w_{\mathrm{jump}}\), write

\[
F_w(a)-F_w(0)=\left[F_{w_{\mathrm{jump}}}(a)-F_{w_{\mathrm{jump}}}(0)\right]
+\frac{w-w_{\mathrm{jump}}}{2}\log\frac{a+d}{d}.
\]

Both terms are nonnegative for all \(a\in[0,1]\), and the second is strictly positive for \(a>0\). Thus \(a=0\) becomes the unique global minimizer at every larger weight. Since \(s\mapsto a=s^2\) is a bijection of \([0,1]\), this proves the claimed blur classification.

**Metastable no-blur basin and unique barrier.** Direct differentiation gives

\[
2F_w'(a)=\frac{w(a+\ell)^2-C(a+d)}{(a+\ell)^2(a+d)}.
\]

At \(a=1\), its sign is that of \(w-w_{\mathrm{local}}\). Hence \(a=1\) is a strict one-sided local minimizer when \(w<w_{\mathrm{local}}\). Since at \(w=w_{\mathrm{jump}}\), \(a=0\) is a global minimizer, the right derivative there is nonnegative; increasing \(w\) makes that derivative strictly positive. Thus in the open interval \(w_{\mathrm{jump}}<w<w_{\mathrm{local}}\), the upward-opening quadratic numerator of \(F'_w\) is positive at zero and negative at one, with exactly one root in \((0,1)\). The derivative changes from positive to negative at that root, which is the unique interior local maximum. The endpoint \(a=0\) is the unique global minimizer, while \(a=1\) remains strictly locally minimizing.

**Sharp auxiliary-scale boundary.** For \(d>0\), the function \(M(d)=(1+d)\log(1+1/d)\) has derivative \(M'(d)=\log(1+1/d)-1/d<0\) and limits \(M(0+)=+\infty\), \(M(+\infty)=1\). Since \((1+\ell)/\ell>1\), exactly one \(d_*(\ell)\) satisfies \(M(d_*)=(1+\ell)/\ell\). This is precisely the boundary between the strict endpoint-threshold ordering \(w_{\mathrm{jump}}<w_{\mathrm{local}}\) and the opposite ordering; at equality the metastability interval has zero width.

The reconstructed nonconstant Fourier coefficient jumps from \(b_-/(1+\ell)\) before the transition to zero after it, providing an exact contrast-loss statement.

## Verification

A standalone Python 3 standard-library checker `verify.py` tests exact rational reductions of the Tikhonov inner minimization and derivative identity, supplementary secant inequalities on a broad parameter grid using high-precision `decimal` logarithms, the global-minimizer comparisons for the explicit transition example, and the unique-barrier sign test. Running `python3 verify.py` in the extracted package gives `PASS` and 4,556 finite assertions. These finite tests are not substituted for the all-parameter proof above.

As an exact-parameter illustrative instance, take \(\ell=1\), \(d=1/100\), \(B=1\). Then \(w_{\mathrm{jump}}=1/(2\log101)\approx0.10833953\), whereas \(w_{\mathrm{local}}=101/400=0.2525\). At \(w=1/5\), full blur is uniquely globally optimal, but identity remains a strict local minimum; the separating local maximum lies at \(a\approx0.35982457\).

## Relationship to prior work

Dworaczyk and Español (2026, Section 3.1, especially Proposition 5) introduce the log-determinant penalized variable-projection functional and give a sufficient *local* exclusion test for the no-blur limit under simultaneous Fourier diagonalization. Their formula for the reduced Fourier objective supplies the starting point here; it is not new. The theorem above treats the smallest actual nonnegative convolution family and instead determines the *global* optimum for every determinant weight in a sharp auxiliary-scale regime, including the previously unquantified discontinuity, complete frequency annihilation, and an explicit interval of deceptive local stability.

Wipf and Zhang (2014) analyze variational-Bayesian versus joint MAP blind-deconvolution penalties, blur-norm dependence and local-minimum mechanisms for a distinct image-prior family. Levin et al. (2011) address approximate marginal-likelihood optimization, and Mbakam et al. (2024) study stochastic semiblind marginal-likelihood estimation. Their general mechanisms do not give the displayed particular two-pixel endpoint threshold. This does not assert universal priority; unrelated or unindexed equivalent results might exist.

## Limitations

The result is confined to a two-pixel periodic positive blur kernel with one varying Fourier magnitude, quadratic image regularization, uniform base prior, a positive auxiliary scale and exact global optimization. It does not imply a bang-bang classification for natural higher-dimensional point-spread families; it does not claim the log-determinant prior always overblurs. For \(d\ge d_*(\ell)\), no complete global-minimizer classification is claimed. The theorem is deterministic and exact-arithmetic; computational optimization algorithms may become trapped in the nonoptimal no-blur local minimum. Independent validation has not been performed.

## References

1. J. T. Dworaczyk and M. I. Español, *Marginalization-Based Regularization for Separable Nonlinear Least Squares Problems with Applications to Semi-Blind Deblurring*, arXiv:2611.04846v1 (first public 2026-11-03), Sections 2–3 and Proposition 5. https://arxiv.org/html/2611.04846v1
2. D. Wipf and H. Zhang, *Revisiting Bayesian Blind Deconvolution*, Journal of Machine Learning Research 15 (2014), 3595–3634; arXiv:1305.2362. https://arxiv.org/abs/1305.2362
3. A. Levin, Y. Weiss, F. Durand and W. T. Freeman, *Efficient Marginal Likelihood Optimization in Blind Deconvolution*, CVPR (2011), 2657–2664. https://dspace.mit.edu/entities/publication/c8a2c704-3a49-413c-b253-83ab3edcfd4e
4. C. K. Mbakam, M. Pereyra and J.-F. Giovannelli, *Marginal Likelihood Estimation in Semiblind Image Deconvolution: A Stochastic Approximation Approach*, SIAM Journal on Imaging Sciences 17 (2024), 1206–1254. https://doi.org/10.1137/23M1584496
