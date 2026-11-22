# A fixed-sample spectral limit and a sharp cube-bias threshold for spherical maximal-projection uniformity testing

## Finding

For the quadratic member \(T_{n,2}\) of the maximal-projection spherical-uniformity tests defined by Borodavka and Ebner [1], fix an integer \(n\ge2\) while the ambient dimension \(d\to\infty\). Let \(W_n\) be a real symmetric \(n\times n\) random matrix with zero diagonal and independent \(N(0,1)\) entries above its diagonal. Write \(J_n\) for the all-ones matrix.

**Fixed-sample spectral limit.** Under independent uniform directions on \(\mathbb S^{d-1}\),
\[
\frac{n\sqrt d}{2}\left(T_{n,2}-\frac1n\right)
\ \xrightarrow{\mathcal D}\ \lambda_{\max}(W_n).
\]
Under the independent biased-cube directions
\[
U_{j,d}=d^{-1/2}(\xi_{1j},\ldots,\xi_{dj}),\qquad
\Pr(\xi_{kj}=1)=\frac{1+\mu_d}{2},
\]
where all signs are independent, \(0\le\mu_d\to0\), and \(\sqrt d\,\mu_d^2\to a\in[0,\infty)\), the limit instead is
\[
\frac{n\sqrt d}{2}\left(T_{n,2}-\frac1n\right)
\ \xrightarrow{\mathcal D}\
\lambda_{\max}\!\left(W_n+a(J_n-I_n)\right).
\]

**Sharp calibration boundary.** For any \(\alpha\in(0,1)\), calibrate by the exact, continuous, dimension-\(d\) Haar-null upper-\(\alpha\) critical value of \(T_{n,2}\). If \(d^{1/4}\mu_d\to c\in[0,\infty)\), the asymptotic rejection probability is
\[
\pi_n(c,\alpha)=\Pr\!\left\{
\lambda_{\max}\!\left(W_n+c^2(J_n-I_n)\right)>q_{n,\alpha}
\right\},
\]
where \(q_{n,\alpha}\) is the upper-\(\alpha\) quantile of \(\lambda_{\max}(W_n)\). If \(d^{1/4}\mu_d\to0\), the power tends to \(\alpha\). If \(d^{1/4}\mu_d\to\infty\) while \(\mu_d\to0\), it tends to one. Thus \(d^{-1/4}\) is the sharp bias scale for this test on this alternative family. Each biased-cube distribution, including \(\mu_d=0\), is mutually singular with the Haar-null law; their total-variation distance is exactly one at every finite dimension.

**Fully explicit two-observation law.** For \(n=2\), write \(z_{1-\alpha/2}=\Phi^{-1}(1-\alpha/2)\). Then
\[
\pi_2(c,\alpha)=1-\Phi(z_{1-\alpha/2}-c^2)
+\Phi(-z_{1-\alpha/2}-c^2).
\]
For \(\alpha=0.05\), the value at \(c=1\) is \(0.170075045753\ldots\), rather than the nominal \(0.05\). The curve increases strictly for \(c>0\).

## Assumptions and scope

The original quadratic statistic [1, (1.3)] is
\[
T_{n,2}=n\max_{\|v\|=1}
\left[\frac1n\sum_{j=1}^n(v^\top U_{j,d})^2-\frac1d\right]^2.
\]
The sample size \(n\) is **fixed**, the dimension \(d\ge2n\) tends to infinity, observations are independent within each dimension, and each observation lies exactly on the unit sphere. Under the cube alternative, signs are identically distributed and independent over both the coordinate and observation indices. Only nonnegative biases approaching zero are used in the asymptotic alternative theorem; replacing the bias by its absolute value yields the same pairwise inner-product law. No assertion is made for a jointly growing sample size.

All rejection probabilities concern the exact Haar-calibrated upper-tail version of the **quadratic maximal-projection** statistic; the Frobenius-norm Bingham statistic, other projection powers, and fixed-dimensional large-sample approximations are different procedures.

## Proof

**Step 1 (finite-dimensional spectral identity).** Put \(G_d=(U_{i,d}^\top U_{j,d})_{1\le i,j\le n}\) and \(S_d=n^{-1}\sum_jU_{j,d}U_{j,d}^\top\). The positive eigenvalues of \(nS_d\) are the nonzero eigenvalues of \(G_d\), and \(S_d-I_d/d\) has an eigenvalue \(-1/d\) since \(d>n\). Because \(\operatorname{tr}G_d=n\), its maximum eigenvalue is at least one. When \(d\ge2n\), \(\lambda_{\max}(G_d)/n-1/d\ge1/d\). Thus the positive leading spectral deviation dominates the absolute negative deviation, even in the presence of other small positive eigenvalues, and
\[
\boxed{T_{n,2}=\frac1n\left(\lambda_{\max}(G_d)-\frac nd\right)^2.}\tag{1}
\]

**Step 2 (Haar Gram central limit).** Realize independent Haar directions as \(U_{j,d}=Z_j/\|Z_j\|\), where the \(Z_j\)'s are independent standard Gaussian vectors in \(\mathbb R^d\). For each unordered pair \(e=\{i,j\}\), the coordinate products \(Z_{ki}Z_{kj}\), as \(k\) varies, are iid, centered, unit-variance. Products indexed by distinct unordered pairs have zero covariance, including pairs sharing one observation index. The fixed-dimensional multivariate central limit theorem, the coordinatewise law of large numbers for \(\|Z_j\|^2/d\), and Slutsky's lemma therefore yield
\[
\sqrt d\,(G_d-I_n)\ \xrightarrow{\mathcal D}\ W_n
\quad\text{(entrywise, hence jointly as a matrix).}\tag{2}
\]
The diagonal of \(G_d-I_n\) is exactly zero.

**Step 3 (biased-cube Gram central limit).** Let \(E\) index the \(\binom n2\) unordered pairs. For \(e=\{i,j\}\), set \(Y_{k,e}=\xi_{ki}\xi_{kj}-\mu_d^2\). Within each fixed dimension, the \(Y_{k,\cdot}\) are independent over \(k\), have mean zero and are uniformly bounded. Direct multiplication using independent signs gives
\[
\operatorname{Cov}(Y_{k,e},Y_{k,f})=
\begin{cases}
1-\mu_d^4,&e=f,\\
\mu_d^2-\mu_d^4,&|e\cap f|=1,\\
0,&e\cap f=\varnothing.
\end{cases}\tag{3}
\]
Since \(\mu_d\to0\), this covariance matrix converges to the identity. The triangular-array multivariate Lindeberg central limit theorem therefore shows
\[
\sqrt d\left[G_d-I_n-\mu_d^2(J_n-I_n)\right]
\ \xrightarrow{\mathcal D}\ W_n.\tag{4}
\]
For \(\sqrt d\mu_d^2\to a\), adding back the deterministic mean proves convergence of \(\sqrt d(G_d-I_n)\) to \(W_n+a(J_n-I_n)\).

**Step 4 (spectral transformation).** The largest-eigenvalue map is continuous and one-Lipschitz in operator norm. For finite \(a\), (2) or (4) gives
\[
\lambda_{\max}(G_d)=1+\frac{L_d}{\sqrt d},
\quad L_d\xrightarrow{\mathcal D}
\lambda_{\max}(W_n+a(J_n-I_n)).
\]
Expanding (1) gives
\[
\frac{n\sqrt d}{2}\left(T_{n,2}-\frac1n\right)
=L_d+O_{\Pr}(d^{-1/2}),
\]
proving both distributional limits.

**Step 5 (critical values and both sides of the threshold).** The largest eigenvalue of \(W_n\) has an atom-free distribution: for each fixed real \(t\), the event \(\lambda_{\max}(W_n)=t\) forces \(\det(W_n-tI_n)=0\), a nonzero polynomial equation in continuously distributed Gaussian entries. Its distribution also has strictly positive probability in every interval of positive real numbers, by Gaussian full support and scaling a matrix having a positive maximal eigenvalue. Hence \(q_{n,\alpha}\) is uniquely defined, positive and a continuity point. Convergence of the Haar critical values, the joint alternatives' limits, and the portmanteau theorem give the asserted local power curve.

For \(d^{1/4}\mu_d\to\infty\) with \(\mu_d\to0\), write \(a_d=\sqrt d\mu_d^2\to\infty\). The centered upper-edge matrix in (4) has bounded second moments, so is \(O_{\Pr}(1)\) in operator norm even without a finite shift limit. The all-ones Rayleigh quotient implies \(\lambda_{\max}(G_d)\ge1+(n-1)\mu_d^2+O_{\Pr}(d^{-1/2})\). Equation (1) then puts \(T_{n,2}\) above the Haar critical value with probability tending to one. If \(a_d\to0\), the limiting law is exactly the Haar law and power tends to \(\alpha\). These opposite conclusions establish the claimed scale, not a minimax rate over arbitrary alternatives.

**Step 6 (exact two-observation distributions).** For \(n=2\), write \(r=U_{1,d}^\top U_{2,d}\). The Gram eigenvalues are \(1\pm|r|\); hence (1) becomes
\[
T_{2,2}=\frac12\left(1+|r|-\frac2d\right)^2,\qquad d\ge4.\tag{5}
\]
Under the Haar null, \(r^2\sim\operatorname{Beta}(1/2,(d-1)/2)\). Let
\[
b_{d,\alpha}=
\sqrt{F^{-1}_{\operatorname{Beta}(1/2,(d-1)/2)}(1-\alpha)}.
\]
Under the biased-cube alternative, all products \(\xi_{k1}\xi_{k2}\) are independent signs of mean \(\mu_d^2\), and therefore \(r=(2K-d)/d\) for \(K\sim\operatorname{Binomial}(d,(1+\mu_d^2)/2)\). Consequently the **exact finite-dimensional power**, with strict rejection at the Haar critical value, is
\[
\boxed{\Pr\big\{|2K-d|>d\,b_{d,\alpha}\big\}.}\tag{6}
\]
At the local scale \(d^{1/4}\mu_d\to c\), the binomial central limit theorem gives \(\sqrt d\,r\Rightarrow N(c^2,1)\); also \(\sqrt d\,b_{d,\alpha}\to z_{1-\alpha/2}\). Equations (5)–(6) yield the explicit power formula. Its derivative for \(c>0\) is \(2c[\phi(z-c^2)-\phi(z+c^2)]>0\), with \(z=z_{1-\alpha/2}>0\), proving strict increase.

## Verification

A standalone Python checker (`checker.py`) evaluates the exact spectral identity for several dimensions and random unit-vector configurations, exhaustively enumerates the required edge-product moments for up to five independent biased signs, checks the two-observation exact Beta and binomial formulas, and checks numerical finite-dimensional powers against the derived limit. It reported **751 passed deterministic assertions**, including a supplementary empirical Gram-covariance check. The finite simulations do **not** serve as proof of either central limit theorem; Steps 2–5 do.

At \(\alpha=0.05\) and \(\mu_d=d^{-1/4}\), the exact \(n=2\) power from (6) equals approximately \(0.191249632842\) at \(d=64\), \(0.175465797543\) at \(d=256\), \(0.167714211421\) at \(d=1024\), and \(0.171808101289\) at \(d=4096\). Lattice oscillations are expected. The continuous limit is \(0.170075045753\). The code requires NumPy and SciPy; it uses fixed random seeds for supplementary checks.

## Relationship to prior work

Borodavka and Ebner [1, Eq. (1.3) and Section 1] define the maximal-projection statistic and its quadratic spectral representation. Their Theorem 2.1 treats large sample size with a fixed sphere dimension. Their conclusion explicitly discusses the still-relevant problem of consistency rates for the quadratic member, with high-dimensional Bingham studies as related literature. The present result keeps \(n\) fixed and allows \(d\to\infty\), establishing a *deformed finite-dimensional Gaussian Gram eigenvalue law* and a *non-rotational, singular cube-alternative detection boundary*, with an exact two-point finite-sample law.

Cutting, Paindaveine and Verdebout [2] establish high-dimensional detection results for the **Bingham Frobenius-norm statistic**, with both dimension and sample size diverging and with rotationally symmetric alternatives, so their theorems do not imply the fixed-\(n\) **operator-norm** and independent-sign alternative result here. High-dimensional Rayleigh tests [3] concern the first power, rather than the second. The matrix central limit theorem used in Steps 2–3 is classical; no claim is made that its generic form is new. The specific exact test-calibration consequences and power law are the contribution assessed here.

## Limitations

The result is restricted to fixed \(n\), the quadratic maximal-projection statistic, and the stated biased product-cube alternatives. It does not establish universal powerlessness of rotation-invariant tests, a minimax lower bound, or any claim about the usual regime \(n\to\infty\). The cube distribution is discrete and therefore singular relative to Haar, so total-variation separation is not a statement that every test is unable to distinguish it; it highlights the loss of information in this particular statistic. The exact finite-dimensional upper-tail law is derived only for \(n=2\). Earlier fixed-sample high-dimensional Gram-limit techniques may in principle subsume part of the probabilistic argument, and independent assessment of historical priority remains necessary. No independent audit has been performed.

## References

[1] Jaroslav Borodavka and Bruno Ebner, *A general maximal projection approach to uniformity testing on the hypersphere*, first submitted 9 January 2023, arXiv:2301.03482v1, https://arxiv.org/pdf/2301.03482. Journal version: *Bernoulli* 32 (2026), 996–1019, https://doi.org/10.3150/25-BEJ1889.

[2] Christine Cutting, Davy Paindaveine and Thomas Verdebout, *Testing uniformity on high-dimensional spheres: The non-null behaviour of the Bingham test*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 58 (2022), 567–602, https://doi.org/10.1214/21-AIHP1168; author preprint https://dipot.ulb.ac.be/dspace/bitstream/2013/320587/3/Paper.pdf.

[3] Christine Cutting, Davy Paindaveine and Thomas Verdebout, *Testing uniformity on high-dimensional spheres against monotone rotationally symmetric alternatives*, *Annals of Statistics* 45 (2017), 1024–1058, https://doi.org/10.1214/16-AOS1473; https://arxiv.org/abs/1502.02120.
