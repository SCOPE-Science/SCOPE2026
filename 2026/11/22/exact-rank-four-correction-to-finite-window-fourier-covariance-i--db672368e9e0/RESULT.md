# Exact rank-four correction to finite-window Fourier covariance in a stochastic gene-switching model

## Finding

For the stationary two-state gene-transcription process described below, the covariance of **every** finite sample of at least four observations has an explicit *positive-definite circulant plus a correction of rank at most four*. In the generic nonresonant case the correction has **exact rank four**; in the exceptional nonresonant case specified below it has rank two. At exact promoter–mRNA relaxation resonance it has **exact rank four**, not two, because two exponential lag modes coalesce into a confluent exponential-polynomial mode.

Consequently the covariance matrix of the unitary discrete Fourier transform, with matrix entries \(F_{j\ell}=m^{-1/2}e^{-2\pi i j\ell/m}\), is **exactly diagonal plus rank at most four**; no large-sample approximation is invoked. This permits an exact, \(O(m\log m)\)-operation evaluation of the *covariance-matched Gaussian surrogate* likelihood using FFTs and a matrix of order at most four. It is **not** an exact likelihood for the original, generally non-Gaussian Markov process.

## Assumptions and scope

Let \(G(t)\in\{0,1\}\) be a stationary promoter, with activation rate \(a>0\) and deactivation rate \(b>0\). While \(G(t)=1\), mRNA molecules are born at Poisson rate \(k>0\), and each extant mRNA molecule independently degrades at rate \(\delta>0\). The joint process \((G,N)\) is in its stationary distribution before sampling. At \(m\ge4\) equally spaced times \(j\Delta\), \(0\le j<m\), \(\Delta>0\), observe \(Y_j=N(j\Delta)+\sigma\varepsilon_j\), where \(\varepsilon_j\) are independent unit-variance Gaussian variables independent of the reaction process and \(\sigma\ge0\).

Put
\[
 s=a+b,\quad p=\frac a{s},\quad \bar n=\frac{kp}{\delta},\quad d=\frac{kp(1-p)}{\delta+s},\quad c=kd,\quad V=\bar n+\frac c\delta.
\]
The constant \(d\) is \(\operatorname{Cov}(G(0),N(0))\) and \(V=\operatorname{Var}(N(0))\). For \(0<r<1\), define matrices indexed by \(0\le i,j<m\):
\[
 T_m(r)_{ij}=r^{|i-j|},\qquad
 P_m(r)_{ij}=\frac{r^{|i-j|}+r^{m-|i-j|}}{1-r^m}.
\]
The matrix \(P_m(r)\) is circulant and has strictly positive Fourier eigenvalues
\[
 L_\ell(r)=\frac{1-r^2}{1-2r\cos(2\pi\ell/m)+r^2},\qquad 0\le\ell<m.
\]

**Distinct relaxation rates, \(s\ne\delta\).** Let \(r=e^{-\delta\Delta}\), \(u=e^{-s\Delta}\), \(B=c/(\delta-s)\), and \(A=V-B\). Then the observed time-domain covariance and its circulant counterpart are
\[
 C_m=A T_m(r)+B T_m(u)+\sigma^2I_m,\qquad
 \mathcal P_m=A P_m(r)+B P_m(u)+\sigma^2I_m.
\]
For \(x_i(v)=v^i\) and \(y_i(v)=v^{m-i}\),
\[
 C_m-\mathcal P_m=-\frac{A}{1-r^m}(xy^{\mathsf T}+yx^{\mathsf T})\bigg|_{v=r}
 -\frac{B}{1-u^m}(xy^{\mathsf T}+yx^{\mathsf T})\bigg|_{v=u}.
\]
Here \(\operatorname{rank}(C_m-\mathcal P_m)=4\) if \(A\ne0\), whereas the rank is \(2\) if \(A=0\). Since \(c>0\), \(B\ne0\). The rank-two surface is nonempty: for \(a=b=1/2\), \(k=6\), and \(\delta=2\), one has \(V=B=3\) and \(A=0\), for every sampling interval. The diagonal Fourier eigenvalues of \(\mathcal P_m\) are \(A L_\ell(r)+B L_\ell(u)+\sigma^2\).

**Equal relaxation rates, \(s=\delta\).** Let \(r=e^{-\delta\Delta}\) and \(K=c\Delta>0\). Then
\[
 C_m=V T_m(r)+K r\partial_r T_m(r)+\sigma^2 I_m,
 \qquad \mathcal P_m=V P_m(r)+K r\partial_r P_m(r)+\sigma^2 I_m.
\]
Define \(x_i=r^i\), \(\tilde x_i=ir^i\), \(y_i=r^{m-i}\), \(\tilde y_i=(m-i)r^{m-i}\) and let \(U\) be the matrix with these four columns. With \(h=V+Km r^m/(1-r^m)\), put
\[
 H=-\frac1{1-r^m}\begin{pmatrix}
 0&0&h&K\\0&0&K&0\\h&K&0&0\\K&0&0&0
 \end{pmatrix}.
\]
Then **exactly** \(C_m=\mathcal P_m+UHU^{\mathsf T}\), with \(\operatorname{rank}(UHU^{\mathsf T})=4\) for every \(m\ge4\). The diagonal Fourier eigenvalues of \(\mathcal P_m\) are \(V L_\ell(r)+K r\partial_r L_\ell(r)+\sigma^2\).

In both cases \(C_m\) and \(\mathcal P_m\) are positive definite. The latter is an explicit *periodization of the genuine covariance sequence*, not an arbitrary nearest-circulant fit.

## Proof

**1. Stationary moments and temporal covariance.** The promoter stationary mean and covariance are \(p\) and \(p(1-p)e^{-s|t|}\). Generator moment equations give
\[
 0=kp-\delta\mathbb EN,\quad
 0= a\mathbb EN+kp-(s+\delta)\mathbb E[GN],\quad
 0=2k\mathbb E[GN]+kp-2\delta\mathbb E[N^2]+\delta\mathbb EN.
\]
These yield \(\mathbb EN=\bar n\), \(\operatorname{Cov}(G,N)=d\) and \(\operatorname{Var}(N)=V\). For \(t\ge0\), the Markov property gives \(\operatorname{Cov}(N(0),G(t))=de^{-st}\). Applying the generator to the second coordinate and solving the linear inhomogeneous equation for \(\operatorname{Cov}(N(0),N(t))\) yields
\[
 \gamma(t)=V e^{-\delta t}+c\frac{e^{-st}-e^{-\delta t}}{\delta-s}\quad(s\ne\delta),
 \qquad
 \gamma(t)=(V+ct)e^{-\delta t}\quad(s=\delta).
\]
Stationarity and independent observation noise therefore give the two stated expressions for \(C_m\), including the resonant limit at equality.

**2. Exact finite-window periodization.** Write \(d_{ij}=|i-j|\). Direct subtraction gives the elementary identity
\[
 T_m(r)_{ij}-P_m(r)_{ij}=-\frac{r^{i}r^{m-j}+r^{m-i}r^j}{1-r^m},
\]
which holds at all boundaries including \(i=j\). Linear combination proves the nonresonant formula. Differentiate this identity in \(r\), multiply by \(r\), and use the product rule to prove the resonant formula \(C_m-\mathcal P_m=UHU^{\mathsf T}\) exactly; the contribution from differentiating \((1-r^m)^{-1}\) accounts for the term \(Km r^m/(1-r^m)\) inside \(h\).

**3. Sharp rank.** For unequal rates the four possible columns are proportional to exponential sequences with bases \(r,r^{-1},u,u^{-1}\). All four bases are distinct, since \(0<r,u<1\) and \(r\ne u\), and their first four rows form a nonsingular Vandermonde matrix. The two symmetric exchange blocks have nonzero determinants whenever their coefficients \(A,B\) are nonzero; thus rank is four, dropping to exactly two if \(A=0\). At resonance the four columns are exponential-polynomial sequences with bases \(r,r^{-1}\), each of multiplicity two. Their first four rows are a nonsingular confluent Vandermonde matrix for \(0<r<1\). The unscaled symmetric coefficient matrix in \(H\) has determinant \(K^4>0\). Hence rank is exactly four even at resonance. No numerical truncation or large-\(m\) argument enters.

**4. Positivity and Fourier likelihood.** The continuous-time centered mRNA covariance has strictly positive power spectrum
\[
 S_N(\omega)=\frac{2\delta\bar n}{\delta^2+\omega^2}
 +\frac{2s k^2p(1-p)}{(\delta^2+\omega^2)(s^2+\omega^2)}.
\]
Sampling and aliasing preserve strict positivity at every discrete Fourier frequency; adding \(\sigma^2\) preserves it. The Fourier eigenvalues of the periodization \(\mathcal P_m\) are the discrete spectral values and hence strictly positive. The original finite covariance \(C_m\) is likewise strictly positive definite as the principal covariance block of a process with a strictly positive spectral density.

Let \(E=C_m-\mathcal P_m=UHU^{\mathsf T}\), taking two columns when \(A=0\). The matrix determinant lemma and Woodbury identity give
\[
 \det C_m=\det\mathcal P_m\det(I+H U^{\mathsf T}\mathcal P_m^{-1}U),
\]
\[
 C_m^{-1}=\mathcal P_m^{-1}-\mathcal P_m^{-1}U
 (I+H U^{\mathsf T}\mathcal P_m^{-1}U)^{-1}H U^{\mathsf T}\mathcal P_m^{-1}.
\]
These identities apply because both covariance matrices are positive definite. FFT diagonalization of \(\mathcal P_m\), a fixed number of FFT applications, and at most a \(4\times4\) solve yield \(\log\det C_m\) and quadratic forms exactly (up to numerical arithmetic) in \(O(m\log m)\) operations. The same cost applies to the corresponding covariance-matched Gaussian *surrogate* negative log-likelihood, not the true non-Gaussian transcription likelihood.

## Verification

Run `python3 checker.py` using Python 3 standard-library modules. The included checker verifies exact fractional-arithmetic identities and rank statements on six-point two-exponential and resonant examples, and independently sums the unperiodized time-domain covariance to evaluate selected finite-window Fourier cross-covariances. The universal theorem is proved above; its computational tests are finite spot checks only.

For the rates \(a=b=1/2\), \(k=30\), \(\delta=\Delta=1\), \(\sigma=0.1\), and a **stationary** sampling window with \(m=240\), the promoter and mRNA relaxations coincide. The exact lag covariance is
\[
 \gamma(j\Delta)=e^{-|j|}\left(\frac{255}{2}+\frac{225}{2}|j|\right).
\]
The normalized modulus of the covariance between the unitary Fourier coefficients at bins \(0\) and \(16\) is approximately \(0.0053053656\), not zero. This is a direct calculation from the finite Toeplitz covariance and illustrates why exact diagonal covariance is false at finite sample length. It is not claimed to be the covariance of the **transiently initialized** trajectories studied numerically in the initiating work.

## Relationship to prior work

Fang, Sun, Zhang and Khammash (2026) use the same telegraph reactions and Gaussian observation noise for frequency-domain reaction-network identification; their proposed fast likelihood in Algorithm 1 uses a **diagonal** Fourier covariance estimated by Monte Carlo. Their experimental trajectories are not initialized at stationarity. The present statement gives a distinct exact stationary, finite-window covariance correction and sharp rank classification, including the relaxation-rate equality used in their numerical parameter choice. It makes no claim of proving their Gaussian approximation or of analyzing their transient initial condition.

General Fourier/Whittle covariance corrections and low-numerical-rank likelihood approximations predate this calculation. In particular Geoga (2024) develops spectral-domain diagonal-plus-approximately-low-rank representations for broad stationary Toeplitz families and discusses exact finite-sample Fourier covariances. The novelty asserted here is **not** the Whittle idea or low-rank linear algebra: it is the exact, uniformly rank-four (or explicit rank-two exceptional) covariance-matched correction for this biochemical switching model, with a sharp confluent result at promoter–degradation resonance and its direct reaction-parameter formulas.

## Limitations

The result requires stationarity before the observation window, homogeneous positive rates, linear mRNA degradation, a two-state promoter, equally spaced measurements, and independent additive noise. It describes exact **second moments** only; the mRNA count process and its finite Fourier transform are generally not jointly Gaussian, so the corrected Gaussian density is only a surrogate and does not establish statistically improved inference over the initiating algorithm. Numerical floating-point stability when the two relaxation rates nearly coincide requires using the analytic resonant limit or stabilized divided differences. The exact-rank statement is about the explicitly defined periodized circulant, not the uniqueness or minimal rank among *all possible* circulant comparisons. General classical exact decompositions of exponential Toeplitz kernels may overlap algebraically; an equivalent model-specific result could be unindexed.

## References

1. Z. Fang, W. Sun, X. Zhang, M. Khammash, *Accelerating reaction network identification via frequency-domain analysis*, arXiv:2611.07684v1 (first publicly submitted 2026-11-05). https://arxiv.org/abs/2611.07684
2. C. J. Geoga, *Fast Machine-Precision Spectral Likelihoods for Stationary Time Series*, arXiv:2404.16583 (first publicly submitted 2024-04-25); SIAM Journal on Scientific Computing **47** (2025), A472–A496. https://arxiv.org/abs/2404.16583
3. *Pathway dynamics can delineate the sources of transcriptional noise in gene expression*, eLife (2021), https://doi.org/10.7554/eLife.69324 (background on the two-state transcription model, not an originality claim).
