# A signed fourth-power Mertens law for truncated Möbius shifts over the binary polynomial ring

## Finding
Let \(a\in\mathbb F_2[t]\) be any fixed nonzero polynomial and \(\mathcal P\) the set of monic irreducible polynomials. For \(M\ge1\), define \(\omega_M(f)=\#\{P\in\mathcal P:P\mid f,\ \deg P\le M\}\), and \(\mu_M(f)=\mu(f)^2(-1)^{\omega_M(f)}\), where \(\mu\) is the polynomial Möbius function. All averages below are over monic polynomials of exactly degree \(N\).

Put \(Q_P=2^{\deg P}\) and
\[
L_P(a)=\begin{cases}1-4/Q_P+2/Q_P^2,&v_P(a)=0,\\1-2/Q_P^2,&v_P(a)=1,\\1-1/Q_P^2,&v_P(a)\ge2.\end{cases}
\]
Let \(D_M=2\sum_{\deg P\le M}\deg P\). For all integers \(M\ge1\), \(N\ge D_M\), and \(N>\deg a\), the exact local approximation obeys
\[
\left|2^{-N}\sum_{\substack{f\text{ monic}\\\deg f=N}}\mu_M(f)\mu_M(f+a)-\prod_{\deg P\le M}L_P(a)\right|\le\frac{2^{1-M}}{M+1}.
\]
Define the nonzero real constant
\[
\kappa_a=e^{-4\gamma}\prod_{P\in\mathcal P}\frac{L_P(a)}{(1-Q_P^{-1})^4},
\]
where the correction product converges absolutely in the sense that the sum of absolute deviations of its factors from one is finite. Uniformly for \(N\ge D_M\), \(N>\deg a\) and \(M\to\infty\),
\[
2^{-N}\sum_{\substack{f\text{ monic}\\\deg f=N}}\mu_M(f)\mu_M(f+a)=\frac{\kappa_a}{M^4}\left(1-\frac2M+\frac7{3M^2}+O_a(M^{-3})\right).
\]
Moreover \(\kappa_a<0\) precisely when \(a\) has exactly one distinct root in \(\mathbb F_2\); otherwise \(\kappa_a>0\). In particular, the leading signed correlation has exact fourth-power decay, and the first two relative correction coefficients are independent of the nonzero shift.

## Assumptions and scope
The coefficient field is exactly \(\mathbb F_2\). The shift \(a\) is nonzero and fixed. Every \(N\) is an integer exceeding \(\deg a\), so that \(f+a\) remains monic of degree \(N\). The cutoff \(M\) may vary with \(N\), subject to the explicit Chinese-remainder capacity bound \(N\ge D_M\). No assertion is made beyond this window. The Euler constant \(\gamma\) is the usual Euler–Mascheroni constant.

## Proof
**1. Local squarefree signed expectation.** Fix \(P\in\mathcal P\), with \(Q=Q_P\), and consider the local function on residues modulo \(P^2\) which is zero when \(P^2\) divides either \(f\) or \(f+a\), and otherwise is \((-1)^{\mathbf1_{P\mid f}+\mathbf1_{P\mid f+a}}\). If \(P\nmid a\), the classes \(0,-a\) are distinct modulo \(P\), so the mean is \(1-4/Q+2/Q^2\). If \(v_P(a)=1\), the residue classes with \(P\nmid f\) contribute \(1-1/Q\), and those in which \(f\) and \(f+a\) are each divisible exactly once by \(P\) contribute \(1/Q-2/Q^2\), for total \(1-2/Q^2\). If \(v_P(a)\ge2\), the two numbers are congruent modulo \(P^2\); outside the zero residue both signs cancel, yielding \(1-1/Q^2\). These computations prove all three formulas for \(L_P(a)\).

**2. Exact finite-level CRT formula.** Let \(\widetilde\mu_M(f)\) be the product of the local signed-squarefree indicators over all \(P\) with \(\deg P\le M\), without imposing squarefreeness at larger primes. Its value depends only on \(f\) modulo \(B_M=\prod_{\deg P\le M}P^2\), and \(\deg B_M=D_M\). Each residue class modulo \(B_M\) occurs exactly \(2^{N-D_M}\) times among monic degree-\(N\) polynomials whenever \(N\ge D_M\). By the Chinese remainder theorem and Step 1,
\[
2^{-N}\sum_{\deg f=N\atop f\text{ monic}}\widetilde\mu_M(f)\widetilde\mu_M(f+a)=\prod_{\deg P\le M}L_P(a).
\]
For an irreducible \(P\) of degree \(d>M\), the fraction of monic degree-\(N\) polynomials divisible by \(P^2\) is \(2^{-2d}\) if \(2d\le N\) and zero otherwise. The same applies to \(f+a\), which is also monic of degree \(N\). Hence, denoting by \(I_2(d)\) the number of monic irreducibles of degree \(d\), the discrepancy in the preceding normalized correlation is bounded by
\[
2\sum_{d>M}I_2(d)2^{-2d}\le2\sum_{d>M}\frac{2^{-d}}d\le\frac{2^{1-M}}{M+1}.
\]
The first inequality is a union bound: outside these large-square events, the two products agree, and both have absolute value at most one. The second uses \(dI_2(d)\le2^d\). This proves the displayed finite-level inequality.

**3. Precise binary Mertens product.** Write \(V_M=\prod_{\deg P\le M}(1-Q_P^{-1})\). The elementary prime-polynomial identity \(\sum_{d\mid n}dI_2(d)=2^n\), obtained by logarithmically differentiating the unique-factorization Euler series, gives
\[
-\log V_M=\sum_{d\le M}I_2(d)\sum_{k\ge1}\frac{2^{-dk}}k=H_M+R_M,
\]
where \(H_M=\sum_{n\le M}1/n\) and \(R_M\) comprises the terms with \(dk>M\). In those terms \(k\ge2\), so \(d\le dk/2\); therefore
\[
0\le R_M\le\sum_{n>M}\frac{2^{-n}}n\sum_{d\le n/2}dI_2(d)
\le\sum_{n>M}\frac{2^{-n}}n\sum_{d\le n/2}2^d
=O(2^{-M/2}/M).
\]
Consequently \(V_M=e^{-H_M}(1+O(2^{-M/2}/M))\).

**4. Euler-product convergence and expansion.** For all but finitely many \(P\), the fixed shift has \(P\nmid a\), and the quotient \(L_P(a)/(1-Q_P^{-1})^4\) equals \(1+O(Q_P^{-2})\). As \(\sum_PQ_P^{-2}<\infty\), the correction product converges absolutely and is nonzero; none of its local factors is zero. Its tail from \(\deg P>M\) is \(1+O_a(2^{-M}/M)\). Thus Step 2 and the preceding Mertens formula yield
\[
2^{-N}\sum_{\deg f=N\atop f\text{ monic}}\mu_M(f)\mu_M(f+a)=\kappa_a e^{4\gamma-4H_M}+O_a(2^{-M/2}M^{-4})+O(2^{-M}/M).
\]
Since \(H_M=\log M+\gamma+1/(2M)-1/(12M^2)+O(M^{-4})\), the exponential factor is
\[
e^{4\gamma-4H_M}=M^{-4}\left(1-\frac2M+\frac7{3M^2}+O(M^{-3})\right).
\]
Both exponentially small errors are absorbed into the stated \(O_a(M^{-7})\) absolute remainder. This proves the full asymptotic.

**5. Exact sign.** For \(\deg P\ge2\), one has \(Q_P\ge4\), whence each of the three local factors \(L_P(a)\) is strictly positive. For the only two degree-one primes \(t\) and \(t+1\), one has \(L_P(a)=-1/2\) when \(P\nmid a\), and \(L_P(a)=1/2\) or \(3/4\) when \(P\mid a\). Accordingly \(\kappa_a\) is negative exactly when precisely one of these two linear factors divides \(a\), i.e. when the shift has exactly one root in \(\mathbb F_2\). This completes the proof.

## Verification
The accompanying standalone `verify.py` uses exact polynomial arithmetic and exact rational fractions. It independently enumerates all monic degree-eleven inputs at cutoff two for four distinct shifts, checks the local residue-product identity and the large-square union-bound error, and reports `VERIFY_OK`. These finite checks are supporting evidence only; the proof above establishes all infinitely many admissible degrees and cutoffs.

## Relationship to prior work
Chatterjee (2026) studies the two-point Chowla problem for this specific truncated Möbius function over polynomial rings by bivariate Erdős–Kac methods. The present result uses a different explicit local-squarefree CRT reduction to obtain a sharp, signed asymptotic and its first two universal corrections over the binary field, with a sign determined by the shift's two linear factors. Darbar and Mukhopadhyay (2024) develop general correlation principles for multiplicative functions over polynomial rings under an odd-characteristic setup and present different truncated-Liouville applications. Carmon (2015) proves characteristic-two Möbius correlation results in the large-field, fixed-degree regime, rather than the fixed binary field and growing-degree truncated regime considered here. A broader correlation identity or sieve treatment may imply aspects of the present calculation without presenting this signed constant explicitly; no claim of proven uniqueness is made.

## Limitations
The result requires \(N\ge D_M\) and fixed nonzero \(a\). It does not supply a Chowla theorem in the full range of cutoffs, does not treat untruncated Möbius correlation, and does not extend its signed constant uniformly to other field sizes. The identity is proved analytically; the executable enumerations cover only finite cases. Novelty judgments remain subject to potential implicit earlier coverage, and no independent mathematical validation has been performed.

## References
1. A. Chatterjee, *Chowla Conjecture for the truncated Möbius function over* \(\mathbb F_q[t]\), arXiv:2610.06471 (first public version, 2026-10-05), https://arxiv.org/abs/2610.06471.
2. P. Darbar and A. Mukhopadhyay, *Correlation of multiplicative functions over* \(\mathbb F_q[x]\): *A pretentious approach*, Mathematika 70 (2024), DOI:10.1112/mtk.12227, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/mtk.12227.
3. D. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, Philosophical Transactions A 373 (2015), DOI:10.1098/rsta.2014.0311, https://pmc.ncbi.nlm.nih.gov/articles/PMC4375379/.
