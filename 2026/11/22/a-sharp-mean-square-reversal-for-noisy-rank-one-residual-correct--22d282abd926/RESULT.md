# A sharp mean-square reversal for noisy rank-one residual correction

## Finding

An energy-orthogonal correction can improve **every realized approximate solve** yet turn a mean-square convergent, freshly randomized Richardson iteration into a divergent one. The complete two-dimensional noise/angle phase diagram and a finite-probe version of this reversal are given below.

For every \(K>0\) and \(\delta>0\), set
\[
E_0=K\begin{pmatrix}1&1\\-1&-1\end{pmatrix},\qquad E_j=E_0+G_j,
\]
where the entries of the independent matrices \(G_j\) are independent, centered Gaussians of variance \(\delta\). Define \(A=I_2\), \(B_j=I_2-E_j\), and the raw Richardson error iteration \(e_{j+1}=E_je_j\). Its exact mean-square contraction radius is
\[
\lambda_{\rm raw}=\delta+\sqrt{\delta^2+4K^2\delta}.
\]
It is mean-square convergent from **every** deterministic initial error if and only if
\[
\boxed{0<\delta<\frac1{4K^2+2}.}
\]

For an arbitrary unit vector \(n=(\cos\theta,\sin\theta)^\top\), let \(Q=nn^\top\) and choose the digital correction space \(Z=\operatorname{range}(Q)^\perp\). The one-application residual correction of Shah–Li–Kalantzis–Xi gives the corrected iteration \(e_{j+1}=QE_je_j\). For every nonzero deterministic \(e_0\) and every \(j\ge1\),
\[
\mathbb E\|e_j\|^2=
\left((n^\top E_0e_0)^2+\delta\|e_0\|^2\right)
\left(K^2\cos^2(2\theta)+\delta\right)^{j-1}.
\]
Thus the corrected iteration converges in mean square for all initial errors **if and only if**
\[
\boxed{\gamma(\theta):=K^2\cos^2(2\theta)+\delta<1.}
\]
The sharp best and worst orientation factors are \(\delta\) and \(K^2+\delta\), respectively. Even though \(\|QE_jv\|\le\|E_jv\|\) for every sample and vector, whenever \(K>1\) and \(0<\delta<1/(4K^2+2)\), the raw iteration converges but the correction \(n=(1,0)^\top\) diverges in mean square, with arbitrarily large ratio of asymptotic factors as \(K\to\infty\) and \(\delta\) is chosen small enough.

There is also a setup-noise discontinuity in the rank-one, one-sweep probing specialization. Let the correction vector be \(Z=\operatorname{span}(Y)\), where \(Y=(E_0+G_{\rm probe})\omega\), \(\omega\ne0\) is any fixed unit probe or an independent continuously distributed random unit probe, and \(G_{\rm probe}\) has independent centered Gaussian entries of any variance \(\varepsilon>0\), independently of all solve reads. For every \(K>1\) and raw-stable \(\delta>0\), the corrected iteration has an open positive-probability set of learned spaces with \(\gamma>1\); consequently its **unconditional** expected squared error diverges from every nonzero deterministic initial error. At exact noiseless setup \(\varepsilon=0\), provided \((1,1)\omega\ne0\), the learned correction spans \((1,-1)\) and \(\gamma=\delta<1\). No assertion is made about the actual frequency of these rare events at finite horizons.

## Assumptions and scope

The matrix \(A=I_2\) is real symmetric positive definite, with one analog block. \(B_j\) is a fresh linear read operator; the programmed mean \(I_2-E_0\) is fixed. Noise in distinct solves is independent, and its four entries within a read are centered, independent, and have the same positive variance \(\delta\). Gaussianity is needed for the full-support setup-noise conclusion, not for the first two exact second-moment laws. The correction space is held fixed during the solve, learned or prescribed, with one-dimensional complement projector \(Q\). The iteration is **unit-relaxation stochastic Richardson**, not GMRES, flexible GMRES, or the authors' experimental Krylov implementation.

The variance parameter \(\delta\) is the variance of each entry **after** read averaging. Under independent equal-variance raw read entries with variance \(\tau^2\), averaged over \(D\) copies and \(S\) reads per copy with the same fixed programmed mean, it is \(\delta=\tau^2/(DS)\). The counterexample uses even \(D=S=1\).

## Proof

First \(E_0^2=0\). In the orthonormal basis \(u=(1,-1)^\top/\sqrt2\), \(v=(1,1)^\top/\sqrt2\), one has \(E_0=2Kuv^\top\). For any deterministic symmetric second-moment matrix \(C\), independence and equal coordinate variances imply the exact covariance transformation
\[
\mathcal T(C)=\mathbb E[E_jCE_j^\top]=E_0CE_0^\top+\delta\operatorname{tr}(C)I_2.
\]
In the \(u,v\) basis the diagonal moments \((a,b)=(u^\top Cu,v^\top Cv)\) obey
\[
\begin{pmatrix}a'\\b'\end{pmatrix}=
\begin{pmatrix}\delta&4K^2+\delta\\\delta&\delta\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}.
\]
Off-diagonal moments vanish after one application and never feed back into the diagonal moments. The displayed positive matrix has eigenvalues \(\delta\pm\sqrt{\delta^2+4K^2\delta}\), so Perron–Frobenius gives convergence for all starting errors exactly when its positive eigenvalue is below one. Squaring the equivalent inequality \(\sqrt{\delta^2+4K^2\delta}<1-\delta\) gives the stated sharp threshold. At or above it every nonzero initial deterministic error has nondecaying second moment, since \(\delta>0\) makes the diagonal transfer strictly positive.

For the digital correction, \(C_Z=Z(Z^\top A Z)^{-1}Z^\top\) is the orthogonal projector onto \(Z\) because \(A=I_2\). Its complementary projector is \(Q\). The exact one-solve error identity is
\[
I_2-M_Z(B_j)A=(I_2-C_ZA)(I_2-B_jA)=QE_j.
\]
Thus the first corrected error equals \(n\,[n^\top E_je_0]\). Every subsequent step multiplies its scalar coefficient by the independent random scalar \(n^\top E_jn\). Since \(n^\top E_0n=K\cos(2\theta)\) and the fresh scalar fluctuation has variance \(\delta\), the independent product law yields the claimed exact second-moment formula. Its first prefactor is strictly positive for every nonzero \(e_0\) because \(\delta>0\). The phase diagram and sharp best/worst angles follow from \(0\le\cos^2(2\theta)\le1\). The samplewise projector inequality is elementary Euclidean orthogonality and does not compare products at different times.

For the learned-space statement, fix any unit probe \(\omega\). The Gaussian vector \((E_0+G_{\rm probe})\omega\) is a nondegenerate two-dimensional Gaussian: its covariance is \(\varepsilon I_2\). Hence its direction assigns strictly positive probability to every open arc. Because \(K>1\), there is an open arc of complementary directions near \(n=(1,0)^\top\) on which \(K^2\cos^2(2\theta)+\delta>1+c\) for some \(c>0\). Conditional on the learned direction, the already-proved exact moment formula applies, with its first prefactor bounded below by \(\delta\|e_0\|^2\). Integrating over this arc gives a strictly positive constant times \((1+c)^{j-1}\), proving unconditional mean-square divergence. With noiseless setup and \((1,1)\omega\ne0\), the probe image is the line spanned by \(u\), whose orthogonal complement is \(v\), so \(\cos(2\theta)=0\) and \(\gamma=\delta\). This uses only the single-sweep, single-vector probing construction, not any assertion that other probing configurations share the phenomenon.

For a rational concrete witness choose \(K=2\), \(\delta=1/100\), and \(n=(1,0)^\top\). The raw mean-square factor is \(\lambda_{\rm raw}=(1+\sqrt{1601})/100\approx0.410125\), whereas the corrected factor is exactly \(401/100=4.01\). The raw noise threshold is \(1/18\), so the witness is strictly inside the stable raw regime.

## Verification

`verify.py` is a standalone SymPy/NumPy diagnostic. Run `python verify.py`. It checks the nilpotent factorization, the exact quadratic covariance transformation, the moment-transfer eigenvalue, sharp rational witness, and stochastic scalar variance against independent Gaussian samples across ninety parameter/angle settings. These finite tests support reproducibility; the universal convergence and positive-probability claims follow from the algebraic and Gaussian-support proofs above.

## Relationship to prior work

Shah, Li, Kalantzis and Xi (arXiv:2611.17251v1, Sections 2.2–3.2) define the programmed-mean/read-fluctuation model, the low-rank energy projection, and its pointwise error identity. They explicitly do **not** claim a complete convergence guarantee for their implementation. The exact rank-one covariance spectrum, sharp stability reversal, and full-support setup-probe consequence here concern a specific stationary Richardson specialization. This neither contradicts the proven pointwise error reduction nor establishes failure of their FGMRES implementation.

Nabben and Rooch (arXiv:2604.21648v1) study compatible transfer operators, deterministic nonsymmetric two-grid convergence, and the role of normality; their abstract and relevant theorem sections do not state this iid-read, fixed-setup 2D moment classification. Earlier work on deflation projections and stochastic multiplicative-noise stability provides broad techniques but not, in the materials examined, this particular sharp construction. The novelty comparison remains qualified by incomplete access to a related older nonsymmetric-deflation full text and possible unindexed equivalent examples.

## Limitations

The chosen programmed mean is strongly nonnormal; it is not guaranteed to be typical of a particular analog device, and the projection is not necessarily the optimizer of the proposed learned-space design. The setup-noise divergence is an infinite-horizon **unconditional mean-square** statement, possibly driven by extremely rare orientations; it does not imply frequent or finite-time practical failure, nor almost-sure divergence. The source does not analyze stationary Richardson as its primary tested solver. This result does not cover general SPD matrices, correlated read noise, finite-precision digital computation, additional probe sweeps, adaptive correction updates, or GMRES convergence.

## References

- Shikhar Shah, Rui Peng Li, Vassilis Kalantzis, Yuanzhe Xi, *Noise-Adaptive Analog–Digital Preconditioning*, arXiv:2611.17251v1, first posted 2026-11-12. https://arxiv.org/html/2611.17251v1
- Reinhard Nabben, Ludwig Rooch, *Optimal transfer operators for nonsymmetric two-grid methods*, arXiv:2604.21648v1, 2026-04-23. https://arxiv.org/html/2604.21648v1
- Luis García Ramos, René Kehl, Reinhard Nabben, *Projections, Deflation, and Multigrid for Nonsymmetric Matrices*, SIAM J. Matrix Anal. Appl. 41 (2020), 83–105. https://doi.org/10.1137/18M1180268 (abstract examined; complete article not accessed).
