# A curvature sign law for one-probe functional Nyström sketches

## Finding
Let \(A\) be any finite-dimensional real symmetric positive-semidefinite matrix, let \(q\ge1\) be an integer, let \(g\) be any real column vector, and let \(f:[0,\infty)\to[0,\infty)\) be continuous, nondecreasing, satisfy \(f(0)=0\), and be strictly positive on \((0,\infty)\). Define the one-column, \(q\)-power Nyström map
\[
\mathcal N_q(B,g)=B^qg\,(g^{\mathsf T}B^{2q-1}g)^\dagger\,g^{\mathsf T}B^q,
\]
where the scalar dagger denotes its Moore–Penrose inverse, including value zero when its argument is zero. Compare the **function-after-sketch** estimate \(F=f(\mathcal N_q(A,g))\) with the **sketch-after-function** estimate \(D=\mathcal N_q(f(A),g)\), using the *same* probe.

If \(f\) is concave, then \(\operatorname{tr}F\ge\operatorname{tr}D\) for **every** \(A,g,q\). If \(f\) is convex, the inequality reverses for **every** \(A,g,q\). Both estimates are trace-underestimators: \(0\le\operatorname{tr}F,\operatorname{tr}D\le\operatorname{tr}f(A)\). Hence the curvature sign determines the pointwise ordering of their nonnegative trace deficits, without distributional assumptions or oversampling. Under strict concavity or strict convexity, inequality is strict whenever \(g\) has nonzero components in at least two distinct positive-eigenvalue eigenspaces of \(A\). A positive linear function gives equality for all inputs.

The comparison can be arbitrarily consequential. For \(A_\varepsilon=\operatorname{diag}(1,\varepsilon)\), \(q=1\), and a standard real Gaussian probe, let \(\mathcal E_F\) and \(\mathcal E_D\) denote the trace deficits. With \(f(t)=\sqrt t\),
\[
\mathbb E\mathcal E_D=\varepsilon^{1/4},\qquad
\mathbb E\mathcal E_F\sim(1+2/\pi)\varepsilon^{1/2}.
\]
With \(f(t)=t^2\),
\[
\mathbb E\mathcal E_D=\varepsilon,\qquad
\mathbb E\mathcal E_F\sim\tfrac32\varepsilon^{1/2}.
\]
Thus the mean-deficit ratio of the less favorable order to the more favorable order diverges, with exponent \(1/4\) in the concave square-root case and \(1/2\) in the convex square case. The theorem is about scalar traces, not Löwner ordering of the two rank-one approximants.

## Assumptions and scope
All matrices and probes are real, finite-dimensional, and operations use exact arithmetic. The scalar function is positive at every positive argument, monotone, continuous, and has \(f(0)=0\). The core order law requires ordinary scalar concavity or convexity, **not** operator concavity. The sketch has exactly one column and uses the same vector for both orders, with the same integer \(q\ge1\). Nonzero, deterministic probes are permitted; stochastic Gaussian probes are used only in the asymptotic examples. If the probe is orthogonal to the range of \(A\), both estimates vanish.

## Proof
Write \(A=U\operatorname{diag}(a_1,\ldots,a_n)U^{\mathsf T}\) with \(a_i\ge0\) and \(w_i=|(U^{\mathsf T}g)_i|^2\). If \(\sum_i a_i^{2q-1}w_i=0\), the positive-eigenvalue components of \(g\) all vanish. Both approximants are zero, proving the assertion in this case. Otherwise, with \(p=2q-1>0\), the nonzero eigenvalue of \(\mathcal N_q(A,g)\) is
\[
R_a=\frac{\sum_iw_ia_i^{p+1}}{\sum_iw_ia_i^p}.
\]
The nonzero eigenvalue of \(\mathcal N_q(f(A),g)\) is
\[
R_f=\frac{\sum_iw_if(a_i)^{p+1}}{\sum_iw_if(a_i)^p}.
\]
Consequently \(\operatorname{tr}F=f(R_a)\), while \(\operatorname{tr}D=R_f\). Restrict sums to positive eigenvalues with positive weights. Define probability weights \(\nu_i\propto w_i a_i^p\) and \(\mu_i\propto w_if(a_i)^p\), and let \(r_i=(a_i/f(a_i))^p\). Then \(\nu_i=\mu_i r_i/(\sum_j\mu_jr_j)\), and
\[
\sum_i\nu_if(a_i)-\sum_i\mu_if(a_i)
=\frac{\operatorname{Cov}_\mu(f(a),r)}{\mathbb E_\mu r}.
\]
For concave \(f\) with \(f(0)=0\), the ratio \(f(t)/t\) is nonincreasing; hence \(r_i\) and \(f(a_i)\) are similarly ordered. Their covariance is nonnegative, as seen by symmetrizing into \(\tfrac12\sum_{i,j}\mu_i\mu_j(f(a_i)-f(a_j))(r_i-r_j)\). Scalar Jensen gives
\[
f(R_a)=f(\mathbb E_\nu a)\ge\mathbb E_\nu f(a)\ge\mathbb E_\mu f(a)=R_f.
\]
For convex \(f\), \(r_i\) and \(f(a_i)\) are oppositely ordered, reversing the covariance step; convex Jensen reverses the other step. Strict curvature on a nontrivial interval containing the active positive eigenvalues makes the Jensen step strict. When \(f(t)=ct\) both formulas coincide.

The trace-underestimator statement follows independently: each approximation has rank at most one and its nonzero eigenvalue cannot exceed the maximal eigenvalue of its input matrix (it is a weighted mean of input eigenvalues). Since \(f\) is increasing, \(f(R_a)\le f(\max_i a_i)\le\sum_i f(a_i)\), and similarly \(R_f\le\max_i f(a_i)\le\sum_i f(a_i)\).

For the asymptotic examples, let \(u=g_1/g_2\), a standard Cauchy random variable. The nonzero eigenvalue of \(\mathcal N_1(A_\varepsilon,g)\) is \(\lambda_\varepsilon=(u^2+\varepsilon^2)/(u^2+\varepsilon)\). For every fixed \(\alpha>0\), substitution \(u=\sqrt\varepsilon\,v\), symmetry, and dominated convergence yield
\[
\mathbb E[1-\lambda_\varepsilon^\alpha]
\sim C_\alpha\sqrt\varepsilon,\qquad
C_\alpha=\frac2\pi\int_0^\infty\left[1-\left(\frac{v^2}{1+v^2}\right)^\alpha\right]dv
=\frac2{\sqrt\pi}\frac{\Gamma(\alpha+1/2)}{\Gamma(\alpha)}.
\]
The integrand is bounded near zero and decays as \(O(v^{-2})\) at infinity. Integration by parts followed by the beta integral gives the gamma expression. In particular, \(C_{1/2}=2/\pi\) and \(C_2=3/2\). The trace deficit of \(F\) equals \(\varepsilon^\alpha+1-\lambda_\varepsilon^\alpha\). For the direct method, the input matrix is \(\operatorname{diag}(1,s)\) with \(s=\varepsilon^\alpha\). Its rank-one Nyström trace deficit is \(s(g_1^2+g_2^2)/(g_1^2+sg_2^2)\); angular integration over the uniform Gaussian direction gives expectation \(\sqrt s\) *exactly*. This proves both claimed comparisons.

## Verification
Run `python3 verify.py` using Python 3 and NumPy (see `requirements.txt`). The verifier compares actual dense-matrix rank-one Nyström constructions with spectral formulas, checks thousands of pointwise inequalities for concave and convex functions over positive and rank-deficient spectra, checks exact-rational test cases, and numerically integrates the asymptotic constants. The proof of the universal inequality and infinite limiting laws is analytic; finite experiments are only consistency tests. The captured output is in `verification_output.txt`.

## Relationship to prior work
Persson and Kressner (2022, journal publication 2023) define function-after-Nyström and compare it numerically with direct Nyström of the matrix function, giving norm error bounds under operator monotonicity. Their formulas (3) and (18), and sections 3–4, provide the two algorithms used here but not the universal same-probe **curvature-sign comparison for one-column sketches**. Gittens and Mahoney (first arXiv release 2013; journal 2016) study ordinary Nyström approximation and its trace-norm behavior, not a convexity-controlled comparison of two function/sketch orders. The exact \(\sqrt\varepsilon\) mean-error fact for ordinary one-column Nyström is already represented in the relevant pre-existing numerical linear algebra literature and is used here as background; the new statement is the all-spectra, all-probes order law and its convex/concave reversal. A previous finite-dimensional Gaussian Nyström residual distribution can recover some isolated special-case expectations; it does not assert the same-probe functional curvature dichotomy.

## Limitations
No ordering of the approximation matrices in Löwner order is claimed: for a nonlinear \(f\), their ranges can differ, so the rank-one matrices may be incomparable even when their traces are ordered. No matrix rank beyond one, different probes, arbitrary nonmonotone functions, complex Gaussian law, finite-precision guarantees, or relative error bound in operator/Frobenius norms is established. The large-gap example is a two-dimensional exact-arithmetic limit, not a generic-spectrum rate theorem. No independent external validation has been performed.

## References
1. D. Persson and D. Kressner, “Randomized low-rank approximation of monotone matrix functions,” arXiv:2209.11023 (first public release 2022-09-22), *SIAM Journal on Matrix Analysis and Applications* 44 (2023), 894–918. https://arxiv.org/abs/2209.11023 ; https://doi.org/10.1137/22M1523923 .
2. A. Gittens and M. W. Mahoney, “Revisiting the Nyström Method for Improved Large-Scale Machine Learning,” arXiv:1303.1849 (first public release 2013-03-07), *JMLR* 17 (2016), 1–65. https://arxiv.org/abs/1303.1849 .
