# Exact planar Gaussian XNysTrace risk and posterior-error calibration

## Finding

For the **unnormalized** two-probe Gaussian XNysTrace estimator of the trace of every real symmetric positive-definite \(2\times2\) matrix \(A\), let \(a,b>0\) be its eigenvalues and put
\[
 r=\frac{\sqrt b-\sqrt a}{\sqrt a+\sqrt b},\qquad
 X=\frac{\sqrt{ab}(a+b)}2,\qquad
 Y=\frac{ab}{4}(1+r^4).
\]
Then its trace-estimation variance and the expectation of its *reported squared error* \(S\) are exactly
\[
 \boxed{\operatorname{Var}(\widehat t)=X+Y,\qquad \mathbb E S=X-Y.}
\]
In particular, for every \(a,b>0\),
\[
 \boxed{1<\frac{\operatorname{Var}(\widehat t)}{\mathbb E S}\le\frac53,\qquad
 \operatorname{Var}(\widehat t)\le\frac58(a^2+b^2).}
\]
Both upper bounds are attained exactly when \(a=b\). The lower calibration ratio \(1\) is approached as the eigenvalue ratio tends to zero or infinity, but is never attained by a positive-definite matrix. The second bound compares against the **two-probe standard Gaussian** Girard–Hutchinson estimator, whose variance is \(a^2+b^2\); it is not a comparison against all probe laws or all trace estimators.

For the isotropic matrix \(A=I_2\), the true mean-square estimation error is \(5/4\) whereas \(\mathbb E S=3/4\); the expected posterior squared error is therefore \(40\%\) smaller than the true mean-square error. For \(A=\operatorname{diag}(1,4)\), these quantities are respectively \(487/81\) and \(323/81\).

## Assumptions and scope

Let \(g_1,g_2\) be independent standard real Gaussian vectors in \(\mathbb R^2\), and let \(A=A^{\mathsf T}\succ0\). For any nonzero \(g\), define its rank-one Nyström approximation
\[
 N(g)=Ag(g^{\mathsf T}Ag)^{-1}g^{\mathsf T}A.
\]
With \(j\ne i\), define the two leave-one-out estimates and their mean by
\[
 T_i=\operatorname{tr}N(g_j)+g_i^{\mathsf T}(A-N(g_j))g_i,
 \qquad \widehat t=\tfrac12(T_1+T_2).
\]
The algorithm's unnormalized posterior squared-error indicator in this two-probe case is
\[
 S=\frac{(T_1-\widehat t)^2+(T_2-\widehat t)^2}{2}
   =\frac{(T_1-T_2)^2}{4}.
\]
These definitions are exactly the basic Gaussian XNysTrace leave-one-out equations (8)–(9) of Epperly, Tropp and Webber (2023) specialized to two test vectors. This is **not** their optional residual-normalized version in Section 2.3. The two probes each require one matrix–vector product; all assertions concern exact arithmetic and the specified Gaussian input law.

## Proof

**Step 1: rank-one residual.** Orthogonal invariance permits \(A=\operatorname{diag}(a,b)\). Write \(g_i=R_i(\cos\theta_i,\sin\theta_i)^{\mathsf T}\), with independent uniform \(\theta_i\in[0,2\pi)\), independent radii satisfying \(\mathbb ER_i^2=2\), \(\mathbb ER_i^4=8\). For \(v(\theta)=(-\sin\theta,\cos\theta)^{\mathsf T}\), direct multiplication gives
\[
 A-N(g_i)=\tau(\theta_i)v(\theta_i)v(\theta_i)^{\mathsf T},
 \qquad \tau(\theta)=\frac{ab}{a\cos^2\theta+b\sin^2\theta}.
\]
Set \(\Delta=\theta_1-\theta_2\). Since \(\operatorname{tr}N(g_i)=a+b-\tau(\theta_i)\), the centered basic estimates satisfy
\[
 T_1-(a+b)=\tau(\theta_2)(R_1^2\sin^2\Delta-1),\quad
 T_2-(a+b)=\tau(\theta_1)(R_2^2\sin^2\Delta-1).
\]
For each fixed held-out approximation the independent Gaussian correction has the correct conditional mean; therefore \(\mathbb E T_i=a+b\).

**Step 2: exact angular moments.** Put \(q=\sqrt{ab}\). Since \(|r|<1\), the Poisson-kernel series, absolutely and uniformly convergent in the angle, is
\[
 \tau(\theta)=q\frac{1-r^2}{1-2r\cos2\theta+r^2}
 =q\left(1+2\sum_{k=1}^{\infty}r^k\cos(2k\theta)\right).
\]
It follows that
\[
 \mathbb E_\theta\tau=q,\qquad
 \mathbb E_\theta[\tau\cos4\theta]=qr^2,\qquad
 \mathbb E_\theta[\tau\sin4\theta]=0.
\]
For completeness, the elementary angular integral \(J(a,b)=\mathbb E_\theta[(a\cos^2\theta+b\sin^2\theta)^{-1}]=1/\sqrt{ab}\) follows from the tangent substitution on each quadrant. Differentiation under the integral (justified by \(a,b>0\)) gives \(\mathbb E_\theta[(a\cos^2\theta+b\sin^2\theta)^{-2}]=-\partial_aJ-\partial_bJ=(a+b)/[2(ab)^{3/2}]\). Consequently,
\[
 \mathbb E_\theta\tau^2=\frac{q(a+b)}2=X.
\]

**Step 3: the non-independent leave-one-out terms.** Conditional on the other Gaussian vector, the centered Gaussian quadratic form has variance \(2\tau^2\); hence \(\operatorname{Var}(T_i)=2X\). For their covariance, integrate first over the independent radii. The product of centered terms becomes
\[
 (2\sin^2\Delta-1)^2=\cos^2(2\Delta)
   =\tfrac12[1+\cos(4\theta_1-4\theta_2)].
\]
Independence of \(\theta_1,\theta_2\) and the Fourier coefficients from Step 2 yield
\[
 \operatorname{Cov}(T_1,T_2)
 =\mathbb E[\tau(\theta_1)\tau(\theta_2)\cos^2(2\Delta)]
 =\frac{q^2}{2}(1+r^4)=2Y.
\]
Consequently, \(\operatorname{Var}((T_1+T_2)/2)=(2X+2Y)/2=X+Y\), and \(\mathbb E[(T_1-T_2)^2/4]=(2X-2Y)/4=X-Y\). These identities prove the exact formulas.

**Step 4: the two sharp global boundaries.** Let \(t=\sqrt{b/a}>0\), so that \(r=(t-1)/(t+1)\). Direct polynomial factorization gives
\[
 \frac58(1+t^4)-\frac{X+Y}{a^2}
 =\frac{(t-1)^2(5t^6+26t^5+57t^4+80t^3+57t^2+26t+5)}{8(t+1)^4}\ge0
\]
and
\[
 \frac{X-4Y}{a^2}
 =\frac{t(t-1)^2(t^4+2t^3+10t^2+2t+1)}{2(t+1)^4}\ge0.
\]
All displayed polynomial coefficients are positive, with equality in either factorization exactly at \(t=1\). Since \(X,Y>0\), \(X-Y>0\) follows also from \(X\ge4Y\), and
\[
 1<\frac{X+Y}{X-Y}\le\frac{5}{3}.
\]
Finally, as \(t\to0\) or \(t\to\infty\), \(Y/X\to0\), proving the claimed strict lower limit. This finishes all quantified cases.

## Verification

The standalone `verify.py` checks the two sharp factorization identities and rational benchmarks with exact symbolic arithmetic; it independently integrates the angular moments at five positive-definite spectra with absolute discrepancy below \(2\cdot10^{-10}\); and it evaluates the original, unsimplified two leave-one-out formulas on \(180000\) independently sampled Gaussian probe pairs for each of five spectra using a fixed seed. It compares empirical mean-square error and posterior squared-error average to the two exact expressions. See `verification_output.txt` for the recorded direct execution and `VERIFICATION.md` for commands and scope. Numerical tests corroborate but do not replace Steps 1–4.

## Relationship to prior work

Epperly, Tropp and Webber (2023), *XTrace: Making the most of every sample in stochastic trace estimation*, introduce the exact basic XNysTrace estimator in equations (7)–(9), prove general upper bounds for its variance in Proposition 5 and Section 5.3, and relate the expected posterior squared error to the correlation between its exchangeable basic estimates in Proposition 2 and Section 5.6. Their published treatment does **not** state the present complete two-dimensional Gaussian spectral variance, exact covariance, sharp \(5/3\) posterior-underestimation constant, or \(5/8\) comparator constant. The general identity in their Proposition 2 is fully credited; its correlation input is evaluated here by an independent nontrivial Fourier calculation.

Persson, Cortinovis and Kressner (2021) study Nyström++ with a distinct fixed-split architecture and provide probabilistic trace-estimation guarantees; their method is not the exchangeable two-probe estimator considered here. The classical Gaussian quadratic-form variance \(2\operatorname{tr}(A^2)\) establishes the baseline comparison. The exact first moment of a planar one-column Nyström residual, when known, does not determine the cross-probe covariance required here. Literature and database comparison provides evidence against direct coverage, not a proof of publication uniqueness.

## Limitations

The theorem concerns only real \(2\times2\) positive-definite matrices, independent **standard Gaussian** test vectors and the **unnormalized** original estimator. It does not extend the sharp constants to larger dimensions, complex matrices, arbitrary probe laws or the modified normalized estimator. In fact two generic matrix–vector products in dimension two already determine \(A\), so a different reconstruction estimator can be exact; also the optional residual-normalized XNysTrace is exact in this special full-rank setting. The value of these formulas is an exact small-budget covariance and posterior-calibration diagnostic for the baseline variant, **not** an optimal information-theoretic algorithm or a claim that two-dimensional stochastic estimation is necessary. A more general specialist result might imply the formulas. The full text of a later, potentially relevant source, E. N. Epperly, *Make the Most of What You Have: Resource-Efficient Randomized Algorithms for Matrix Computations* (2025 dissertation, arXiv:2512.15929), was not accessible for an exact comparison; only its metadata and abstract were available. Independent mathematical and publication-precedence evaluation has not been performed.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825, first public version January 19, 2023; https://arxiv.org/abs/2301.07825 ; open full text https://ar5iv.labs.arxiv.org/html/2301.07825 . In particular equations (7)–(9), Proposition 2 and Section 5.3.
2. D. Persson, A. Cortinovis, and D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659, first public version September 22, 2021; https://arxiv.org/abs/2109.10659 ; open full text https://ar5iv.labs.arxiv.org/html/2109.10659 .
3. E. N. Epperly, *Make the Most of What You Have: Resource-Efficient Randomized Algorithms for Matrix Computations*, doctoral dissertation (2025), arXiv:2512.15929, https://arxiv.org/abs/2512.15929 . Relevant-source risk only: full text was not inspected.
