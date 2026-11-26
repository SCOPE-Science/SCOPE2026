# Reciprocal-Student poles in one-vector Gaussian-sketched harmonic Ritz extraction

## Finding
Fix a real symmetric positive-definite matrix \(A\in\mathbb R^{n\times n}\), \(n\ge2\), and a nonzero deterministic vector \(v\in\mathbb R^n\). For any integer \(s\ge1\), draw an \(s\times n\) matrix \(S\) with independent standard real Gaussian entries. The one-vector *sketched harmonic Ritz value* \(\widehat\vartheta\) is defined by
\[
(SAv)^{\mathsf T}S(Av-\widehat\vartheta v)=0,
\qquad
\widehat\vartheta=\frac{\|SAv\|^2}{(SAv)^{\mathsf T}Sv}
\]
where the second expression is valid with probability one if \(v\) is not an eigenvector. Set
\[
\mu=\frac{v^{\mathsf T}Av}{\|Av\|^2},\qquad
\sigma=\frac{\sqrt{\|v\|^2\|Av\|^2-(v^{\mathsf T}Av)^2}}{\|Av\|^2}.
\]
If \(v\) is not an eigenvector, then \(\mu,\sigma>0\), and the following is an *exact identity in law*:
\[
\boxed{\widehat\vartheta^{-1}\ \stackrel{d}{=}\ \mu+\frac{\sigma}{\sqrt{s}}T_s},
\]
where \(T_s\) has Student's \(t\) distribution with \(s\) degrees of freedom. In particular, the original unsketched harmonic Ritz value is \(\vartheta_0=1/\mu>0\), but the sketched value can have either sign. Precisely,
\[
\Pr\{\widehat\vartheta<0\}=F_{t_s}(-\mu\sqrt{s}/\sigma)>0.
\]
For every finite \(s\), define
\[
c_s=\frac{\Gamma((s+1)/2)}{\sigma\sqrt\pi\,\Gamma(s/2)}
\left(1+\frac{\mu^2}{\sigma^2}\right)^{-(s+1)/2}>0.
\]
The two *one-sided* tails satisfy
\[
\boxed{\lim_{t\to\infty}t\Pr\{\widehat\vartheta>t\}
=\lim_{t\to\infty}t\Pr\{\widehat\vartheta<-t\}=c_s}.
\]
Therefore, for every real \(p>0\),
\[
\boxed{\mathbb E|\widehat\vartheta|^p<\infty\quad\Longleftrightarrow\quad 0<p<1}.
\]
Both positive and negative parts have infinite first moment: the signed expectation is undefined, not merely large. These conclusions persist upon conditioning on *any nonempty finite interval of nonzero sketch norms* \(a\le\|SAv\|\le b\), \(0<a<b<\infty\): norm-only screening of the one-column sketch does not remove the pole.

If \(v\) is an eigenvector with eigenvalue \(\lambda>0\), the exceptional case has \(\sigma=0\) and \(\widehat\vartheta=\lambda\) almost surely.

## Assumptions and scope
All matrices and vectors are real, and calculations use exact arithmetic. The Gaussian sketch is oblivious and has independent centered unit-variance entries; scaling every entry by a common nonzero constant does not change the result. The one-dimensional trial space may be \(\operatorname{span}\{v\}=\mathcal K_1(A,v)\). The result treats the scalar harmonic projection and not all eigenvalues of a multi-vector sketched pencil. No subspace-embedding event is imposed; such events can exclude rare sign-changing sketches.

## Proof
Write \(u=Av\), \(\mu=(u^{\mathsf T}v)/\|u\|^2\), and \(w=v-\mu u\). Then \(u^{\mathsf T}w=0\). For a non-eigenvector \(v\), \(w\ne0\). Gaussian rotational invariance implies that \(X=Su/\|u\|\) and \(Y=Sw/\|w\|\) are independent standard \(s\)-dimensional Gaussian vectors. The harmonic equation and the orthogonal decomposition give
\[
\widehat\vartheta^{-1}=
\frac{(Su)^{\mathsf T}Sv}{\|Su\|^2}
=\mu+\frac{\|w\|}{\|u\|}\frac{X^{\mathsf T}Y}{\|X\|^2}.
\]
Conditional on \(X\), the scalar \(X^{\mathsf T}Y/\|X\|\) is standard normal with a distribution independent of \(X\). Hence it is independent of \(\|X\|^2\sim\chi^2_s\), establishing the Student identity with \(\sigma=\|w\|/\|u\|\). Because \(A\) is positive definite, \(\mu>0\), and the Gaussian geometry gives \(\sigma>0\) exactly when \(Av\) and \(v\) are nonparallel.

The reciprocal variable \(R=\widehat\vartheta^{-1}\) has the continuous, everywhere positive density
\[
f_R(r)=\frac{\Gamma((s+1)/2)}{\sigma\sqrt\pi\,\Gamma(s/2)}
\left(1+\frac{(r-\mu)^2}{\sigma^2}\right)^{-(s+1)/2}.
\]
In particular, \(f_R(0)=c_s>0\). For \(t>0\), exactly
\[
\Pr\{\widehat\vartheta>t\}=\int_0^{1/t}f_R(r)\,dr,\qquad
\Pr\{\widehat\vartheta<-t\}=\int_{-1/t}^0 f_R(r)\,dr.
\]
Continuity at zero yields both limits. The positive-moment layer-cake identity \(\mathbb E|\widehat\vartheta|^p=p\int_0^\infty t^{p-1}\Pr\{|\widehat\vartheta|>t\}\,dt\) yields finiteness precisely for \(p<1\). The separate one-sided lower tails show divergence of positive and negative first moments.

For the norm-screening statement, condition on any fixed value \(r=\|Su\|\in[a,b]\). The orthogonal Gaussian component \(Sw\) remains independent; therefore \(R\), conditioned on \(\|Su\|=r\), has law \(N(\mu,\|w\|^2/r^2)\), with a strictly positive density at zero. The event \(a\le\|Su\|\le b\) has positive probability for all \(0<a<b<\infty\); mixing these positive conditional densities produces a positive finite density at zero and the same \(t^{-1}\) tail and moment boundary. In one dimension, retaining the sole singular direction under an ordinary sketch-norm cutoff leaves this pole mechanism intact.

If \(w=0\), then \(Sv=\mu Su\) identically and \(\widehat\vartheta=1/\mu=\lambda\), proving the exceptional case.

## Verification
The standalone file `verify.py` generates fresh standard Gaussian sketches and reconstructs the harmonic quotient directly, checking its pathwise representation, the Student negative-sign probability, density normalization, the sharp tail constants, and strict positivity of the conditional zero-density under norm screening. All reported tests passed. The infinitely many moment statements and asymptotic tails follow from the displayed analytic density, *not* from simulation.

For \(A=\operatorname{diag}(1,4)\) and \(v=(1,1)^{\mathsf T}/\sqrt2\), the parameters are exactly \(\mu=5/17\) and \(\sigma=3/17\). Thus \(\widehat\vartheta=17/(5+3Z/\sqrt{W})\) with independent \(Z\sim N(0,1)\), \(W\sim\chi_s^2\), while the unsketched value is \(17/5\). The verifier includes this reproducible example.

## Relationship to prior work
Burke, Güttel and Soodhalter (arXiv:2311.14206, Section 3.5) define the sketched harmonic Ritz pencil and motivate its use in restarted GMRES with deflation. Their singular-value stabilization concerns the sketched trial vectors. The exact reciprocal-Student distribution, its signed pole tails, and failure of norm-only screening are the present claim, not part of the cited algorithm definition. Güttel and Schweitzer (arXiv:2208.11447) study sketched Krylov projection for matrix functions. Palitta, Schweitzer and Simoncini (arXiv:2306.06481) analyze outlying sketched Ritz values in matrix-function algorithms; these are distinct from the harmonic Ritz distribution here. Analogous inverse-pole phenomena occur in Gaussian-sketched Galerkin corrections, but their error bounds do not automatically identify this eigenvalue law or its conditional norm-screening behavior.

## Limitations
This is a one-vector, real-Gaussian, finite-dimensional result. It does not show that GMRES-SDR diverges, or that its actually selected multi-vector deflation space has infinite error. Selection, regularization, acceptance of a certified two-dimensional embedding, or other safeguards can change the distribution. The unconditional infinite moment arises from arbitrarily rare near-zero cross inner products; high-probability analyses remain compatible with it. Prior equivalent expressions using ratios of Gaussian quadratic forms may exist; originality beyond this explicit numerical-method application is not independently certified.

## References
- L. Burke, S. Güttel, K. M. Soodhalter, *GMRES with Randomized Sketching and Deflated Restarting*, arXiv:2311.14206, first preprint 2023-11-23, Section 3.5. https://arxiv.org/abs/2311.14206
- S. Güttel, M. Schweitzer, *Randomized Sketching for Krylov Approximations of Large-Scale Matrix Functions*, arXiv:2208.11447 (2022). https://arxiv.org/abs/2208.11447
- D. Palitta, M. Schweitzer, V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, arXiv:2306.06481 (2023). https://arxiv.org/abs/2306.06481
