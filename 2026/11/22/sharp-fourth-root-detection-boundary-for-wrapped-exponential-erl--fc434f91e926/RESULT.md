# Sharp fourth-root detection boundary for wrapped exponential–Erlang mixtures

## Finding

For the wrapped exponential–Erlang family, the first complex trigonometric moment identifies both interior parameters, but the exponential submodel is singular when its rate is unknown. Nevertheless, a first-moment statistic has nontrivial Gaussian local power at the sharp fourth-root mixture scale, with a matching impossibility result below this scale.

For \(m=\mathbb E e^{iT}=u+iv\), define \(D(u,v)=v^2-u(1-u)\). At any \(\theta>0\), \(0\le q<1\),
\[
D(u,v)=\frac{q^2\theta^2}{(1+\theta^2)^2},\qquad
\theta=\frac{v+\sqrt{D}}{1-u},\qquad
q=\frac{1+\theta^2}{\theta}\sqrt D.
\]
The inverse applies to every interior parameter \(q>0\); \(D=0\) characterizes the exponential submodel \(q=0\).

Given \(n\) independent angles, let \(\widehat u=n^{-1}\sum_j\cos T_j\), \(\widehat v=n^{-1}\sum_j\sin T_j\), \(\widehat D=\widehat v^2-\widehat u(1-\widehat u)\), and \(\widetilde\theta=\max\{n^{-1},\widehat v/(1-\widehat u)\}\) when \(\widehat u<1\) (set \(\widetilde\theta=1\) otherwise). Put
\[
V(\theta)=\frac{\theta^2+2}{(1+\theta^2)^2(\theta^2+4)},\qquad
S_n=\frac{\sqrt n\,\widehat D}{\sqrt{V(\widetilde\theta)}}.
\]
Under the composite wrapped-exponential null \(q=0\) at every fixed \(\theta>0\), \(S_n\Rightarrow N(0,1)\). Under \(\theta_n\to\theta_0>0\) and \(q_n=c n^{-1/4}\) for fixed \(c\ge0\),
\[
S_n\Rightarrow N(\mu,1),\qquad
\mu=\frac{c^2\theta_0^2}{(1+\theta_0^2)^2\sqrt{V(\theta_0)}}.
\]
For any \(\alpha\in(0,1)\), rejecting for \(S_n>z_{1-\alpha}\) has limiting size \(\alpha\) at each null parameter and local power \(1-\Phi(z_{1-\alpha}-\mu)\), strictly exceeding \(\alpha\) for \(c>0\). At every fixed interior alternative it is consistent. Conversely, for each \(\theta_0>0\) and \(q_n=o(n^{-1/4})\), there are wrapped-exponential null distributions with nearby rates whose \(n\)-sample total-variation distance from the alternative tends to zero. Thus no test controlling null size uniformly in a neighborhood of \(\theta_0\) can exceed asymptotic power \(\alpha\) along those alternatives. The fourth-root scale is sharp for this composite-null problem.

## Assumptions and scope

The angular origin is fixed. Data are iid within each row of any triangular array, with \(T\in[0,2\pi)\). For \(\theta>0\), let \(h_\theta\) denote an exponential density wrapped modulo \(2\pi\), and \(k_\theta\) a shape-two Gamma density wrapped at the same rate:
\[
h_\theta(t)=\frac{\theta e^{-\theta t}}{1-e^{-2\pi\theta}},\quad
k_\theta(t)=\sum_{j\ge0}\theta^2(t+2\pi j)e^{-\theta(t+2\pi j)},\quad
f_{\theta,q}=(1-q)h_\theta+q k_\theta.
\]
The model has \(\theta>0\), \(0\le q<1\); the null is \(q=0\). This is the published wrapped quasi-Lindley family under \(q=1/(1+a)\) with published \(a>0\), also the wrapped two-parameter Lindley family under \(q=b/(\theta+b)\) with published \(b>0\). Both prior parameterizations concern the same distributions. The endpoint \(q=0\) is adjoined for exponentiality testing. The exponential rate is unknown under the null.

## Proof

**Exact moment and inverse.** Wrapping preserves integer Fourier moments. For every positive integer \(r\),
\[
\mathbb E e^{irT}=(1-q)\frac\theta{\theta-ir}+q\left(\frac\theta{\theta-ir}\right)^2.
\]
Writing \(A=1+\theta^2\) gives
\[
u=\frac{\theta^2}A-\frac{2q\theta^2}{A^2},\qquad
v=\frac\theta A+\frac{q\theta(\theta^2-1)}{A^2}.
\]
Substitution gives \(D=q^2\theta^2/A^2\) and \(v+\sqrt D=\theta(1-u)\). Since \(1-u>0\), the claimed inverse follows, proving full interior identification. Differentiating this parameter-to-moment map gives determinant \(2q\theta^2/A^3\), positive for \(q>0\), zero for \(q=0\).

**Null variance.** The gradient of \(D\) is \(g=(2u-1,2v)\). Under \(q=0\), \(u=\theta^2/A\), \(v=\theta/A\); thus \(\|g\|=1\). If \(\Sigma=\operatorname{Cov}(\cos T,\sin T)\), then the second moment \(\mathbb E e^{2iT}=\theta/(\theta-2i)\) and the identities for squared trigonometric functions give
\[
g^\mathsf T\Sigma g=\frac{\theta^2+2}{(1+\theta^2)^2(\theta^2+4)}=V(\theta)>0.
\]
The bounded two-vector CLT and smooth delta method yield \(\sqrt n\widehat D\Rightarrow N(0,V(\theta))\). Also \(\widetilde\theta\to\theta\), so Slutsky proves the stated calibration.

**Local and fixed alternatives.** For \(\theta_n\to\theta_0\), \(q_n=c n^{-1/4}\), the exact identity gives \(\sqrt n D(u_n,v_n)\to c^2\theta_0^2/(1+\theta_0^2)^2\). Bounded triangular-array vector CLT and a first-order Taylor expansion yield asymptotic Gaussian centered fluctuation with variance \(V(\theta_0)\), since the limiting law of each observation is the wrapped exponential at \(\theta_0\). The rate estimate is consistent for \(\theta_0\) in this limit, giving the stated \(N(\mu,1)\). For fixed \(q>0\), the strong law gives \(\widehat D\to D>0\); the denominator converges to a positive constant, establishing consistency.

**Sharp unknown-rate lower bound.** Direct differentiation, either before or after wrapping, gives the exact density tangent identity
\[
k_\theta-h_\theta=-\theta\partial_\theta h_\theta,\qquad
f_{\theta,q}=h_\theta-q\theta\partial_\theta h_\theta.
\]
Taylor expansion of \(h_{\theta(1-q)}\) on a compact positive-rate neighborhood of \(\theta_0\) thus yields \(\sup_{0\le t<2\pi}|f_{\theta,q}(t)-h_{\theta(1-q)}(t)|\le Cq^2\). Wrapped exponential densities are uniformly bounded away from zero on that neighborhood. Hence squared one-observation Hellinger distance is \(O(q^4)\); squared Hellinger distance between the corresponding \(n\)-fold product laws is \(O(nq^4)\). Total variation tends to zero when \(nq_n^4\to0\), equivalently \(q_n=o(n^{-1/4})\). Choosing null rate \(\theta_0(1-q_n)\) proves the composite-null lower bound for any test with size \(\le\alpha+o(1)\) uniformly on a neighborhood of \(\theta_0\).

## Verification

The standalone `checker.py` (standard library only) verifies 1,732 assertions across rational parameter grids, including exact rational discriminants, inverse formulas and the variance computed from second Fourier moments. Run `python checker.py`. The symbolic polynomial identity, Jacobian and bounded-CLT/Hellinger arguments were reconstructed analytically. Finite assertions support but do not replace universal proofs.

## Relationship to prior work

Bhattacharjee's 2020 wrapped quasi-Lindley paper derives the corrected density, mixing representation and integer characteristic function. Bhattacharjee, Ahmed and Das's wrapped two-parameter Lindley paper treats the same family under another parameterization; it derives trigonometric moments and numerically estimates parameters by maximum likelihood. Both are directly credited. The 2024 review catalogs both names. Their inspected full texts do not supply the composite-null first-moment calibrated fourth-root test and corresponding Hellinger impossibility bound. An abstract nonregular-mixture theorem might anticipate the fourth-root rate; novelty is assessed for the combined exact model-specific inversion, statistic, noncentrality and lower bound, not for mixture formulas already published.

## Limitations

The origin is known and fixed. Independence of observations is essential. The lower bound assumes null size controlled uniformly over nearby positive rates and concerns only this two-component family. There is no claim of an optimal local power constant, exact finite-sample size, generality to rotated origins or dependent data, or independently verified historical priority.

## References

1. S. Bhattacharjee, *Exploration of some distributional properties, parameter estimates and applications of the wrapped quasi Lindley distribution*, J. Math. Comput. Sci. 10 (2020), 2390–2407, posted 2020-09-09. DOI https://doi.org/10.28919/jmcs/4888; full text https://scik.org/jmcs/article/10-6-p2390/jmcs-10-6-p2390.pdf.
2. S. Bhattacharjee, I. Ahmed, K. K. Das, *Wrapped Two-Parameter Lindley Distribution for Modelling Circular Data*, Thailand Statistician 19(1) (2021), 81–94, publicly posted 2020-12-28. https://ph02.tci-thaijo.org/index.php/thaistat/article/view/242815; full text https://ph02.tci-thaijo.org/index.php/thaistat/article/download/242815/164679/842820.
3. Bell and Nadarajah, *A Review of Wrapped Distributions for Circular Data*, Mathematics 12 (2024), 2440. DOI https://doi.org/10.3390/math12162440.
