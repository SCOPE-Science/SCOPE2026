# Optimal three-epoch radial-velocity phase design under Ornstein–Uhlenbeck noise

## Finding

**Theorem (exact finite three-epoch D-optimal design).** Fix a known orbital period \(P>0\), stationary noise scale \(\sigma>0\), and correlation time \(\tau>0\). At distinct observing times \(0\le t_1<t_2<t_3\le P\), measure
\[
Y(t)=\gamma+A\cos(\omega t)+B\sin(\omega t)+\varepsilon(t),
\qquad \omega=2\pi/P,
\]
where \(\gamma,A,B\in\mathbb R\) are unknown and \(\varepsilon\) is a zero-mean Gaussian process with known covariance \(\operatorname{Cov}(\varepsilon(s),\varepsilon(t))=\sigma^2 e^{-|t-s|/\tau}\). The unique D-optimal **pair of consecutive gaps**, maximizing the determinant of the joint Fisher information for \((\gamma,A,B)\), is
\[
 t_2-t_1=t_3-t_2=\frac{\theta_*(c)}{\omega},
 \qquad c=\frac1{\omega\tau},
\]
where \(\theta_*(c)\in(0,2\pi/3)\) is the unique solution of
\[
\frac{1+2\cos\theta}{\sin\theta}
=\frac{2c}{e^{2c\theta}-1}.
\]
The absolute starting time is arbitrary subject to all three observations lying in the chosen period. The optimum is strict modulo this common translation. The optimal phase gap is strictly increasing in \(c\), and
\[
\theta_0<\theta_*(c)<\frac{2\pi}{3},\qquad
\theta_0=1.803005921905\ldots,
\]
with \(\theta_0\) the unique root of \((1+2\cos\theta)/\sin\theta=1/\theta\) in \((0,2\pi/3)\). In the perfectly uncorrelated **limit** \(c\to\infty\), the gaps approach \(P/3\); in the long-correlation **limit** \(c\downarrow0\), they approach \(\theta_0P/(2\pi)=0.286957304895\ldots P\). The model at \(\tau=\infty\) is excluded because its covariance matrix is singular.

In the long-correlation limit, using the usual equally spaced \(P/3\) gaps instead of the optimal gaps retains only \(0.87267239617\ldots\) of the optimal Fisher determinant. This is a limiting comparison, not an assertion about other noise laws.

## Assumptions and scope

There are exactly three instantaneous scalar observations and three unknown real mean coefficients. The planetary frequency, covariance amplitude, and OU relaxation time are known; the covariance has no independent white-noise/nugget term. The three observing times may be chosen freely in one **fixed** interval of length one orbital period (endpoints allowed); the planet's mean velocity curve is sinusoidal, and the criterion is the **joint** determinant for \((\gamma,A,B)\), not marginal precision for amplitude alone. The OU correlation is a tractable idealization, not the quasi-periodic stellar-activity Gaussian process of a detailed stellar model. There are no visibility, weather, exposure-length, or calibration constraints.

## Proof

Put \(a=\omega(t_2-t_1)\), \(b=\omega(t_3-t_2)\), and \(c=(\omega\tau)^{-1}\). Thus \(a,b>0\) and \(a+b\le2\pi\). A common shift of every observation rotates the cosine/sine regression columns, leaving the Fisher determinant unchanged. Set the first phase to zero and write the design matrix and normalized covariance as
\[
X=\begin{pmatrix}1&1&0\\1&\cos a&\sin a\\1&\cos(a+b)&\sin(a+b)\end{pmatrix},\qquad
\Sigma/\sigma^2=\begin{pmatrix}1&r&rs\\r&1&s\\rs&s&1\end{pmatrix},
\]
where \(r=e^{-ca}\) and \(s=e^{-cb}\). Direct determinant expansion gives
\[
\det X=4\sin(a/2)\sin(b/2)\sin((a+b)/2),\qquad
\det\Sigma=\sigma^6(1-r^2)(1-s^2).
\]
Since \(X\) is square, \(\det(X^T\Sigma^{-1}X)=(\det X)^2/\det\Sigma\). Hence the determinant for \(a+b<2\pi\) is
\[
\mathcal D_c(a,b)=\frac{16\sin^2(a/2)\sin^2(b/2)\sin^2((a+b)/2)}{\sigma^6(1-e^{-2ca})(1-e^{-2cb})}.
\]
It vanishes as either gap tends to zero or as their sum tends to \(2\pi\). In the interior it is strictly positive.

To prove **unrestricted equality of the two optimal gaps**, maximize the positive square root and define
\[
f_c(x)=\log\sin(x/2)-\frac12\log(1-e^{-2cx}),\qquad 0<x<2\pi.
\]
Apart from an additive constant,
\[
\tfrac12\log\mathcal D_c(a,b)=f_c(a)+f_c(b)+\log\sin((a+b)/2).
\]
Differentiating twice gives
\[
f_c''(x)=-\frac1{4\sin^2(x/2)}+\frac{c^2}{2\sinh^2(cx)}<0.
\]
Indeed \(\sin(x/2)\le x/2\) and \(\sinh(cx)\ge cx\) imply \(f_c''(x)\le-1/(2x^2)<0\). For every fixed admissible total span \(a+b\), strict Jensen concavity yields a unique maximum at \(a=b\). Therefore any global optimum must have equal gaps.

Set \(a=b=\theta\in(0,\pi)\). Up to a positive factor, maximizing \(\mathcal D_c(\theta,\theta)\) is equivalent to maximizing
\[
J_c(\theta)=\frac{\sin\theta(1-\cos\theta)}{1-e^{-2c\theta}}.
\]
Its logarithmic derivative is
\[
L_c(\theta)=\frac{1+2\cos\theta}{\sin\theta}-\frac{2c}{e^{2c\theta}-1},
\]
and its second logarithmic derivative is
\[
L_c'(\theta)=-\frac1{\sin^2\theta}-\frac1{1-\cos\theta}+\frac{c^2}{\sinh^2(c\theta)}<0.
\]
The last inequality follows from \(\sinh(c\theta)\ge c\theta\) and \(\sin\theta\le\theta\). As \(\theta\downarrow0\), \(L_c(\theta)\sim2/\theta>0\); as \(\theta\uparrow\pi\), \(L_c(\theta)\to-\infty\). Thus a unique critical point exists, and strict concavity makes it the global maximizer. At \(\theta=2\pi/3\), \(L_c<0\), so the root is smaller than \(2\pi/3\).

For fixed \(\theta>0\), \(2c/(e^{2c\theta}-1)=\theta^{-1}u/(e^u-1)\), \(u=2c\theta\), decreases strictly with \(c\). Consequently \(L_c(\theta)\) increases strictly with \(c\), while it decreases strictly with \(\theta\); the unique root \(\theta_*(c)\) therefore increases strictly with \(c\). Taking \(c\downarrow0\) and \(c\to\infty\) in the root equation gives the two stated limiting equations. Strict decrease of \(L_0(\theta)=(1+2\cos\theta)/\sin\theta-1/\theta\) follows by the same derivative bound. Finally, since \(1-e^{-2c\theta}\sim2c\theta\) as \(c\downarrow0\), the limiting determinant ratio for uniform versus optimal gaps is the square of
\[
\frac{\sin(2\pi/3)(1-\cos(2\pi/3))/(2\pi/3)}{\sin(\theta_0)(1-\cos\theta_0)/\theta_0}.
\]
This evaluates to \(0.87267239617\ldots\). All assertions hold for the entire declared continuous domain.

## Verification

A standalone companion file, `verify_design.py`, symbolically expands both required determinants in SymPy and independently optimizes the full two-gap objective using SciPy, without imposing equal gaps. It checks the root equation at eight correlation ratios, asymmetric perturbations, and thousands of interior pairs. Run from the extracted directory with `python verify_design.py`; this requires Python, NumPy, SciPy, and SymPy. Successful execution prints the symbolic checks, full-domain numerical comparisons and the limiting root. Numerical sampling supplements—but does not replace—the analytic inequalities above.

## Relationship to prior work

Lam et al. (2024) give a Fisher-information framework for planning exoplanet radial-velocity observations with general Gaussian-process noise. Their study emphasizes radial-velocity semi-amplitude precision in more realistic quasi-periodic noise, and does not state the exact global three-epoch OU joint-D-optimal phase-gap law derived here. Dette, Pepelyshev and Zhigljavsky (2013) establish universal *approximate* designs for certain periodic covariance kernels and trigonometric regression functions; these do not imply the present finite three-sample, nonperiodic OU covariance optimum. Their 2015 work develops continuous-time and mainly one-parameter correlated-regression designs rather than this saturated three-parameter finite design. Baran, Szák-Kocsis and Stehlík (2017) prove equal spacing for **two-component complex** OU observations with a different trend parameterization and criterion; the models are not equivalent. The classical \(P/3\) independent-noise design is recovered as a limiting case. No universal originality claim is inferred from unsuccessful searches.

## Limitations

This is an exact theoretical benchmark for one stationary OU noise component. Adding white instrumental noise, unknown period or covariance parameters, eccentric orbital harmonics, a quasi-periodic stellar kernel, telescope scheduling constraints, or changing the criterion to marginal precision of the velocity semi-amplitude can alter the optimum. Numerical checks are finite and do not establish the proof. Priority against uninspected finite-design literature remains provisional; no empirical validation or independent audit has been performed.

## References

1. Lam, C., Bedell, M., Zhao, L. L., Gupta, A. F., and Ballard, S. A. (2024). *gaspery: Optimized Scheduling of Radial Velocity Follow-Up Observations for Active Host Stars*. First arXiv version dated 2024-08-29. https://arxiv.org/abs/2408.16830
2. Dette, H., Pepelyshev, A., and Zhigljavsky, A. (2013). *Optimal design for linear models with correlated observations*. Annals of Statistics 41. https://arxiv.org/abs/1303.2863
3. Dette, H., Pepelyshev, A., and Zhigljavsky, A. (2016). *Optimal designs in regression with correlated errors*. Annals of Statistics 44. https://pmc.ncbi.nlm.nih.gov/articles/PMC4914140/
4. Baran, S., Szák-Kocsis, C., and Stehlík, M. (2017). *D-optimal designs for complex Ornstein-Uhlenbeck processes*. https://arxiv.org/abs/1704.05719
