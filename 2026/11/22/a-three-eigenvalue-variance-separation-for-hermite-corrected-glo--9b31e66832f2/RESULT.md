# A three-eigenvalue variance separation for Hermite-corrected global Lanczos

## Finding

**Theorem (vanishing Frobenius residual with diverging sign-probe variance).** For each integer \(N\ge 2\), let \(q=N^3\), \(n=q+2\), and define the sparse real symmetric positive-definite matrix
\[
 A_N=I_q\oplus
 \begin{pmatrix}3N/2&-N/2\\-N/2&3N/2\end{pmatrix}.
\]
For \(f(x)=1/x\), run **one full-size global Lanczos step from \(I_n\)**, and correct its trace approximation by the exact Hermite remainder using \(s\ge1\) independent probes. Write \(H_s\) for ordinary Hutchinson on \(A_N^{-1}\), and \(G_s\) for the one-step deterministic Lanczos trace plus Hutchinson applied to its Hermite remainder, both using the same number and law of probes. Put
\[
 \mu_N=\frac{N^3+3N}{N^3+2},\qquad
 \rho_N=1-\frac{2N^2}{\mu_N^2}.
\]
For **Rademacher** probes, using identical probes in the two estimators gives the exact equality of *centered random errors*, for every sample realization,
\[
 G_s-\operatorname{tr}(A_N^{-1})
 =\rho_N\bigl(H_s-\operatorname{tr}(A_N^{-1})\bigr).
\]
Consequently, with all inverse and remainder actions evaluated exactly,
\[
 \frac{\operatorname{Var}(G_s)}{\operatorname{Var}(H_s)}
 =\rho_N^2\sim4N^4,
 \qquad \operatorname{Var}(H_s)=\frac1{4sN^2}.
\]
The inflation is strict for every \(N\ge2\). In contrast, for independent standard **Gaussian** probes in each estimator the exact variance ratio is
\[
 \frac{\operatorname{Var}(G_s^{\rm Gauss})}
 {\operatorname{Var}(H_s^{\rm Gauss})}
 =\frac{\|A_N^{-1}-h_N(A_N)\|_F^2}{\|A_N^{-1}\|_F^2}
 \sim\frac5N\longrightarrow0,
\]
where \(h_N(x)=2/\mu_N-x/\mu_N^2\). Meanwhile the uncorrected one-step deterministic approximation is asymptotically accurate in **relative trace**:
\[
 \frac{\operatorname{tr}(A_N^{-1})-n/\mu_N}
 {\operatorname{tr}(A_N^{-1})}\sim\frac3{N^2}\longrightarrow0.
\]
Thus even a Hermite error matrix with asymptotically vanishing **relative Frobenius norm** and an asymptotically accurate deterministic trace can amplify Rademacher uncertainty without bound. The construction uses exactly three eigenvalues; for any two-eigenvalue SPD matrix with condition number \(\kappa\) and positive ordinary sign-probe variance, the corresponding one-node Rademacher variance ratio is at most \((\kappa-1)^2\), whereas this family has condition number \(2N\) and a ratio of order \(\kappa^4\).

## Assumptions and scope

The matrix is exactly as displayed, with real arithmetic and \(N\in\mathbb Z\), \(N\ge2\). The three distinct eigenvalues are \(1,N,2N\), with multiplicities \(N^3,1,1\), respectively; hence \(\kappa(A_N)=2N\). Each of the \(s\) probe vectors has independent coordinates and is independent across vectors, with either symmetric \(\pm1\) coordinates (sign probes) or standard Gaussian coordinates. Both estimators use the **same** probe law and sample count when compared; the exact centered-error identity couples the sign probes of the two estimators. Only the ideal exact-action stochastic correction is analyzed, not the finite-tolerance inner Krylov implementation, computational cost, or roundoff.

The one-step global Lanczos node is the normalized Frobenius Rayleigh quotient at \(I_n\), namely \(\mu_N=\operatorname{tr}(A_N)/n\). The Hermite interpolant matches \(f\) and its first derivative at this node, so \(h_N(x)=2/\mu_N-x/\mu_N^2\). Denote \(M_N=A_N^{-1}-h_N(A_N)\). Since \(\operatorname{tr}(h_N(A_N))=n/\mu_N\), the correction \(n/\mu_N+s^{-1}\sum z_j^TM_Nz_j\) is unbiased for \(\operatorname{tr}(A_N^{-1})\).

## Proof

**Step 1: exact spectrum, trace, and remainder.** The final \(2\times2\) block has eigenvalues \(N,2N\), and its inverse is
\[
 \begin{pmatrix}3/(4N)&1/(4N)\\1/(4N)&3/(4N)\end{pmatrix}.
\]
Thus \(\operatorname{tr}(A_N)=N^3+3N\), \(\operatorname{tr}(A_N^{-1})=N^3+3/(2N)\). Direct scalar algebra gives
\[
 r_N(x):=f(x)-h_N(x)=\frac{(x-\mu_N)^2}{\mu_N^2x},
\]
so \(M_N=r_N(A_N)\) is positive semidefinite. This identity verifies the Hermite normalization and shows that the error trace equals \(\operatorname{tr}(A_N^{-1})-n/\mu_N\), without any appeal to a finite eigenvalue experiment.

**Step 2: the exact sign-probe law.** There is exactly one off-diagonal pair in both \(A_N^{-1}\) and \(M_N\). Its entries are, respectively,
\[
 (A_N^{-1})_{q+1,q+2}=\frac1{4N},\qquad
 (M_N)_{q+1,q+2}=\frac1{4N}-\frac N{2\mu_N^2}
 =\frac{\rho_N}{4N}.
\]
For a sign vector \(z\), all diagonal contributions in \(z^TBz\) are deterministically \(\operatorname{tr}(B)\). The sole random term is twice the off-diagonal entry multiplied by \(z_{q+1}z_{q+2}\). With \(\xi_j=z_{j,q+1}z_{j,q+2}\), the \(\xi_j\) are independent symmetric signs and
\[
 H_s-T_N=\frac1{2Ns}\sum_{j=1}^{s}\xi_j,
 \qquad G_s-T_N=\frac{\rho_N}{2Ns}\sum_{j=1}^{s}\xi_j,
 \quad T_N=\operatorname{tr}(A_N^{-1}).
\]
This proves the pathwise identity and the variance formulas. Since \(\mu_N\to1\), one has \(\rho_N/N^2\to-2\) and hence \(\rho_N^2/N^4\to4\). For all \(N\ge2\), \(\mu_N\le7/5\), while \(2N^2/\mu_N^2\ge 8/(7/5)^2>2\), so \(|\rho_N|>1\). The asserted inequality \(\mu_N\le7/5\) follows from \(5(N^3+3N)\le7(N^3+2)\) for integer \(N\ge2\), with equality at \(N=2\).

**Step 3: contrast with Gaussian probes and deterministic trace.** For a symmetric \(B\), the exact variance of an average of \(s\) standard-Gaussian quadratic forms is \(2\|B\|_F^2/s\). Spectral calculus yields
\[
 \|A_N^{-1}\|_F^2=N^3+\frac5{4N^2},\quad
 \|M_N\|_F^2=N^3r_N(1)^2+r_N(N)^2+r_N(2N)^2.
\]
Now \(\mu_N-1=O(N^{-2})\), so \(r_N(1)=O(N^{-4})\), whereas \(r_N(N)/N\to1\) and \(r_N(2N)/N\to2\). Therefore \(\|M_N\|_F^2\sim5N^2\), yielding the Gaussian ratio \(\sim5/N\). Finally \(n/\mu_N=(N^3+2)^2/(N^3+3N)\); subtracting from \(T_N=N^3+3/(2N)\) and dividing by \(T_N\) gives
\[
 \frac{T_N-n/\mu_N}{T_N}
 =\frac{6N^4-8N^3+3N^2+1}{(N^2+3)(2N^4+3)}
 \sim\frac3{N^2}.
\]

**Step 4: the two-eigenvalue barrier.** If an SPD matrix has only values \(0<a<b\), write \(A=aI+(b-a)P\) for its spectral projection \(P\), and set \(\mu=\operatorname{tr}(A)/n\). Since \(A^{-1}=a^{-1}I+(b^{-1}-a^{-1})P\), the off-diagonal part of \(A^{-1}-h(A)\) is exactly \((1-ab/\mu^2)\) times the off-diagonal part of \(A^{-1}\). Whenever the ordinary sign-probe variance is nonzero, the corrected-to-ordinary ratio therefore is \((1-ab/\mu^2)^2\). Because \(\mu\in[a,b]\) and \(\kappa=b/a\), its value is bounded by \((\kappa-1)^2\). The three-eigenvalue family above, with \(\kappa=2N\), has ratio asymptotic to \(\kappa^4/4\), so it is not a two-eigenvalue reformulation.

## Verification

The standalone `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. Execute `python3 verify.py`. It checks the block inverse, the global Lanczos node, the Hermite remainder, the complete binomial sign-probe distribution for sample counts \(1,2,4,7\), exact variances, Gaussian Frobenius identities, deterministic trace discrepancy and finite two-spectrum comparisons. It also checks the rational expressions at larger parameters. The reported run passed 2,501 exact-rational assertions. No finite test is offered as proof of a universal quantifier or asymptotic limit: those follow from the identities above.

## Relationship to prior work

Rinelli, Simunec and Vermeiren (2026), arXiv:2611.18864, introduce full-size global Lanczos with stochastic correction; their equations (2.13), (3.3), and (4.1)–(4.3) identify the Hermite remainder and its Gaussian/Rademacher variances. Their Section 4 discusses reductions of the Frobenius error and the possibility of improved stochastic estimation. The present theorem establishes a contrasting, explicit asymptotic *separation* between the two probe laws for that specific one-node correction. The previously studied two-eigenvalue inverse-trace variance relation is reproduced directly in Step 4 and does not yield the three-eigenvalue quartic conditioning law.

Gambhir, Stathopoulos and Orginos (2016), arXiv:1603.05988, show that Hermitian spectral deflation can increase Hutchinson variance. That general warning uses a spectral-deflation control, not a global-Lanczos Hermite tangent, and does not entail the exact distributional identity or the simultaneous Gaussian/Rademacher asymptotics here. Hallman and Troester (2021), arXiv:2103.10516, study multilevel/Chebyshev trace estimators, rather than the particular tangent remainder and three-eigenvalue family.

## Limitations

This is an exact-arithmetic, ideal-inner-action result for one full-size Lanczos step and the inverse function only. It does not say all Hermite-corrected estimators are worse, does not establish poor relative trace accuracy of the final estimator, does not compare equal wall-clock costs, and makes no claim about XTrace, XNysTrace, other Lanczos step counts, or finite-tolerance inner approximations. The relative Frobenius reduction is asymptotic in a growing dimension and growing condition number; it is not an absolute small-error guarantee. Gaussian correction has lower *relative-to-Gaussian-baseline variance* on this family but may have higher absolute variance than the sign-probe correction. Historical priority is not independently certified.

## References

1. Michele Rinelli, Igor Simunec, Robbe Vermeiren, *Global Lanczos with stochastic error correction for trace estimation of matrix functions*, arXiv:2611.18864v1, publicly released 2026-11-13. https://arxiv.org/abs/2611.18864
2. Arjun Singh Gambhir, Andreas Stathopoulos, Kostas Orginos, *Deflation as a Method of Variance Reduction for Estimating the Trace of a Matrix Inverse*, arXiv:1603.05988. https://arxiv.org/abs/1603.05988
3. Eric Hallman, Devon Troester, *A Multilevel Approach to Stochastic Trace Estimation*, arXiv:2103.10516. https://arxiv.org/abs/2103.10516
