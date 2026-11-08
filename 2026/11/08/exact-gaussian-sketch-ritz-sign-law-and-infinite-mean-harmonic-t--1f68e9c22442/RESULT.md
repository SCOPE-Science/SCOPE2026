# Exact Gaussian-sketch Ritz sign law and infinite-mean harmonic tail

## Finding

**Theorem (scalar sketched Arnoldi and sketched harmonic Arnoldi).** Fix integers \(d\ge2\) and \(s\ge1\), a real symmetric positive-definite matrix \(A\in\mathbb R^{d\times d}\), and \(b\in\mathbb R^d\setminus\{0\}\). Draw \(S\in\mathbb R^{s\times d}\) with independent entries of law \(N(0,1/s)\). Set
\[
\theta_{\mathrm A}=\frac{(Sb)^\mathsf T(SAb)}{\|Sb\|_2^2},\qquad
\theta_{\mathrm H}=\frac{\|SAb\|_2^2}{(Sb)^\mathsf T(SAb)}.
\]
These are the one-dimensional sketched Arnoldi and sketched harmonic Arnoldi Ritz values, respectively. They are well-defined almost surely. Define
\[
\alpha=\frac{\|Ab\|_2}{\|b\|_2},\qquad
\rho=\frac{b^\mathsf TAb}{\|b\|_2\|Ab\|_2},\qquad
\sigma=\sqrt{1-\rho^2}.
\]
For \(0<\rho<1\), let \(T_s\) denote the standard Student variable with \(s\) degrees of freedom. The **separate marginal laws** (not a claimed common coupling) are
\[
\theta_{\mathrm A}\ \overset{\mathrm d}{=}\ \alpha\left(\rho+\frac{\sigma}{\sqrt s}T_s\right),\qquad
\theta_{\mathrm H}\ \overset{\mathrm d}{=}\ \frac{\alpha}{\rho+(\sigma/\sqrt s)T_s}.
\]
Both Ritz values have the same sign in every nonsingular sample. Their exact negative-real-axis probability is
\[
\Pr\{\theta_{\mathrm A}<0\}=\Pr\{\theta_{\mathrm H}<0\}
=\frac12 I_{\sigma^2}\left(\frac{s}{2},\frac12\right),
\]
where \(I_z(a,b)=B_z(a,b)/B(a,b)\) is the regularized incomplete beta function. For \(s=1\) this is \(\arccos(\rho)/\pi\), and for \(s=2\) it is \((1-\rho)/2\).

Let \(K>1\). Among all real SPD matrices of any dimension at least two whose spectral condition number does not exceed \(K\), and all nonzero starting vectors, the **attained sharp worst-case probability** is
\[
\boxed{p_s(K)=\frac12 I_{((K-1)/(K+1))^2}\left(\frac{s}{2},\frac12\right).}
\]
Equality holds already for \(A=\operatorname{diag}(1,K)\) and \(b=(\sqrt{K/(K+1)},\sqrt{1/(K+1)})^\mathsf T\). For fixed \(K>1\),
\[
p_s(K)\sim\frac{K+1}{2\sqrt{2\pi K s}}
\left(\frac{K-1}{K+1}\right)^s\qquad(s\to\infty).
\]
For \(K_s>1\) with \(K_s\to\infty\) and \(s/K_s\to c\in[0,\infty)\),
\[
p_s(K_s)\longrightarrow\Phi(-2\sqrt c),
\]
where \(\Phi\) is the standard normal distribution function; if instead \(s/K_s\to\infty\), the limit is zero. Thus the natural high-condition sketch dimension is proportional to condition number.

A further, qualitatively different, feature concerns harmonic Ritz magnitudes. For every finite \(s\ge1\) and every \(0<\rho<1\), the two one-sided limits exist and are equal:
\[
\boxed{
\lim_{t\to\infty}t\Pr\{\theta_{\mathrm H}>t\}
=\lim_{t\to\infty}t\Pr\{\theta_{\mathrm H}<-t\}
=\alpha\frac{\Gamma((s+1)/2)}{\sqrt\pi\,\Gamma(s/2)}\sigma^s>0.}
\]
Consequently \(\mathbb E|\theta_{\mathrm H}|=\infty\), and neither its positive nor negative part has finite expectation, **for any finite sketch dimension**, unless \(b\) is an eigenvector. For comparison, \(\theta_{\mathrm A}\) has finite mean if \(s>1\) and finite variance if \(s>2\). If \(Ab=\lambda b\), both values are deterministically \(\lambda>0\), with no negative-sign or heavy-tail effect.

## Assumptions and scope

All matrices and Gaussian sketches are real, the sketch is unconditioned, and computations are exact. Neither a successful subspace embedding nor a restarted algorithm is assumed; conditioning on an embedding event changes the laws. The spectral condition number is the largest eigenvalue divided by the smallest. Expressions at \(\rho=1\) use the deterministic eigenvector case, rather than formulas that divide by \(\sigma\). The case \(K=1\) likewise has zero failure probability. Values \(\theta_{\mathrm A}\) and \(\theta_{\mathrm H}\) are the uncorrected one-vector projected quantities from the source definitions, not similarity-restored Ritz values.

## Proof

**Gaussian reduction.** Put \(U=\sqrt s\,Sb/\|b\|_2\) and \(V=\sqrt s\,SAb/\|Ab\|_2\). Since each row of \(S\) is isotropic Gaussian, the pairs of corresponding entries have unit variances and correlation \(\rho\). For \(\rho<1\) one may therefore write \(V=\rho U+\sigma Z\), where \(U,Z\) are independent standard Gaussian vectors in \(\mathbb R^s\). It follows that
\[
\theta_{\mathrm A}=\alpha\left(\rho+\sigma\frac{U^\mathsf TZ}{\|U\|_2^2}\right).
\]
Conditionally on \(U\), the scalar \(U^\mathsf TZ/\|U\|_2\) is standard normal with a conditional law independent of \(U\). It is thus independent of the chi variable \(\|U\|_2\). Their ratio is \(T_s/\sqrt s\), giving the first marginal identity. Reversing the Gaussian regression yields \(U=\rho V+\sigma Z'\) with \(V,Z'\) independent standard Gaussians. Hence
\[
\frac1{\theta_{\mathrm H}}=\frac1\alpha\left(\rho+\sigma\frac{V^\mathsf TZ'}{\|V\|_2^2}\right),
\]
proving the second marginal identity. Because \(\|SAb\|_2^2\) and \(\|Sb\|_2^2\) are positive almost surely, both signs coincide with that of \((Sb)^\mathsf T(SAb)\). The zero-denominator event has probability zero by the continuous conditional Gaussian law. The standard Student survival formula then gives the incomplete-beta expression: at threshold \(\sqrt s\rho/\sigma\), the beta argument is \(s/(s+s\rho^2/\sigma^2)=\sigma^2\).

**Sharp uniform condition-number bound.** Write \(\mu=\lambda_{\min}(A)\), \(L=\lambda_{\max}(A)\) and \(m=b^\mathsf TAb/\|b\|_2^2\). The elementary scalar inequality \((\lambda-\mu)(L-\lambda)\ge0\) for spectral values \(\lambda\in[\mu,L]\) yields
\[
\frac{\|Ab\|_2^2}{\|b\|_2^2}\le(\mu+L)m-\mu L,
\quad\text{and}\quad
\rho^2\ge\frac{m^2}{(\mu+L)m-\mu L}
\ge\frac{4\mu L}{(\mu+L)^2}.
\]
The last inequality follows by minimizing over \(m\in[\mu,L]\), with the unique interior minimizer \(m=2\mu L/(\mu+L)\) when \(\mu<L\). The stated diagonal two-eigenvalue example attains equality. As \(\Pr\{\theta<0\}=\tfrac12 I_{1-\rho^2}(s/2,1/2)\) decreases with \(\rho\), the spectral-angle bound proves both the universal inequality and attainment.

**Asymptotic rates.** Fix \(K>1\), set \(z=((K-1)/(K+1))^2\in(0,1)\), and write \(a=s/2\). Endpoint Laplace asymptotics give \(B_z(a,1/2)\sim z^a(1-z)^{-1/2}/a\); the beta normalization is \(B(a,1/2)\sim\sqrt\pi/\sqrt a\). Combining and using \(\sqrt{1-z}=2\sqrt K/(K+1)\) gives the displayed sharp prefactor. For varying \(K_s\to\infty\), the Student threshold satisfies
\[
\sqrt s\frac{2\sqrt{K_s}}{K_s-1}=2\sqrt{\frac{s}{K_s}}\frac{K_s}{K_s-1},
\]
so the Student central limit theorem gives \(\Phi(-2\sqrt c)\) for finite \(c\). When \(s/K_s\to\infty\), the thresholds tend to infinity and tightness of \(T_s\) gives zero.

**Harmonic tails.** Let \(X=\rho+(\sigma/\sqrt s)T_s\). Its continuous density at zero is positive and equals
\[
f_X(0)=\frac{\Gamma((s+1)/2)}{\sqrt\pi\,\Gamma(s/2)}\sigma^s.
\]
By the reciprocal marginal formula, \(\Pr\{\theta_{\mathrm H}>t\}=\Pr\{0<X<\alpha/t\}\sim\alpha f_X(0)/t\). Similarly, \(\Pr\{\theta_{\mathrm H}<-t\}=\Pr\{-\alpha/t<X<0\}\sim\alpha f_X(0)/t\). Integrating either one-sided survival tail shows the corresponding expectation is infinite. The Student moment threshold yields the final comparison for Arnoldi.

## Verification

Running the supplied standalone \(\texttt{verify.py}\) with Python 3 prints `VERIFY_OK` after exact-formula extremizer spot checks on numerical grids, Gaussian-sketch simulations for five sketch/condition pairs (40,000 independent samples each), equality of Ritz signs, and analytic tail-density identity checks for seventeen sketch dimensions. These computations check finite instances and numeric identities; all universal and asymptotic claims follow from the proof above, not from simulations. The reference sketch family has entries \(N(0,1/s)\). Simulation tolerance is specified in the checker, with a fixed seed for reproducibility.

## Relationship to prior work

Güttel, Liu and Nyman [1], Section 2.2, equations (11) and (13), define the sketched Arnoldi and sketched harmonic Arnoldi projections. Their Section 5.3 studies sufficient embedding conditions ensuring harmonic Ritz values remain in the right half-plane; it does not supply the unconditional Gaussian distribution, exact worst-case sign probability, or reciprocal-tail law established here. Güttel and Schweitzer [2], Remark 2.6, already observe that sketched Ritz values may have negative real parts even when the original matrix is Hermitian/positive real; the qualitative possibility is not claimed as new. Grigori, Kressner, Shao and Simunec [3] propose a similarity-restoring modification that can avoid the uncorrected-projection issue, but their corrected Ritz values are not the random variables studied here. The available comparison with Palitta, Schweitzer and Simoncini [4] likewise concerns numerical effects of sketched/truncated Krylov approximations rather than these sharp scalar Gaussian laws. The derivation uses standard Student, beta, sample-covariance and elementary spectral-angle facts. General results on moments of Gaussian quadratic-form ratios, including Roberts [5], form relevant background to the infinite-mean phenomenon. The contribution assessed here is the joint method-specific sharp spectral-conditioning failure frontier and harmonic tail coefficient, not a new statistical distribution or a general discovery that arbitrary Gaussian ratios can lack means. The abstract of [5] was accessible, but its full text was not materially inspected: the extent of its exact coverage remains a priority risk. A literature search cannot establish historical uniqueness.

## Limitations

Only the first one-dimensional Arnoldi/harmonic projection is analyzed, with real Gaussian sketches of finite size, SPD input, and exact arithmetic. No general statement follows for longer Krylov projections, complex sketches, nonnormal matrices, or the fully safeguarded/restarted algorithms. The probabilities are unconditional and may be smaller if sketches failing an embedding check are rejected. No finite-precision overflow statement is made. The harmonic infinite-mean claim does not imply that every numerical run is unstable, nor does it apply to similarity-corrected projections. Historical priority has not been independently established.

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354 (first public version July 11, 2026). https://arxiv.org/abs/2607.10354
2. S. Güttel, M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447 (2022). https://arxiv.org/abs/2208.11447
3. L. Grigori, D. Kressner, N. Shao, I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248 (2026). https://arxiv.org/abs/2601.10248
4. D. Palitta, M. Schweitzer, V. Simoncini, *Sketched and truncated polynomial Krylov methods: Evaluation of matrix functions*, arXiv:2306.06481 (2023). https://arxiv.org/abs/2306.06481
5. L. A. Roberts, *On the Existence of Moments of Ratios of Quadratic Forms*, *Econometric Theory* 11 (1995), 750–774. https://doi.org/10.1017/S0266466600009725
