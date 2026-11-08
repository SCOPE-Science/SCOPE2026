# Exponential negative-type collapse for antipodal Boolean cubes

## Finding

Let \(n=4m\) with integer \(m\ge3\), let \(h=n/2\), and put \(G_n=\mathbb F_2^n/\langle\mathbf1\rangle\), the antipodal quotient of the Boolean cube. Endow its \(N=2^{n-1}\) vertices with the graph distance
\[
d_n([x],[y])=\min\bigl(\mathrm{wt}(x-y),\,n-\mathrm{wt}(x-y)\bigr).
\]
Write \(\beta_n\) for its generalized roundness: the supremum of the real \(p>0\) for which the matrix \((d_n(a,b)^p)_{a,b\in G_n}\) is conditionally negative semidefinite. The following fully explicit two-sided bounds hold:
\[
\boxed{\frac1{2^{n+1}\log(n/2)}\le \beta_n
<\frac{2(h+1)(h-1)^2}{\binom{2h}{h}(h-3)}.}
\]
In particular, along dimensions divisible by four, the exponential decay base is exact:
\[
\boxed{\lim_{m\to\infty}\beta_{4m}^{1/(4m)}=\tfrac12.}
\]
This is a **rate theorem**, not a formula for individual critical exponents. In the equivalent Hilbert-space language, \(d_n^{p/2}\) admits an isometric Euclidean realization for all exponents in the displayed lower range, but cannot for exponents at or above the displayed upper obstruction.

## Assumptions and scope

The group is over \(\mathbb F_2\); \(\mathbf1\) is its all-ones vector; \(\mathrm{wt}\) means Hamming weight. Quotient representatives differ by \(\mathbf1\), which replaces weight \(w\) by \(n-w\), so the displayed distance is well defined. An edge on the quotient joins two classes that differ by a standard coordinate vector; this is a folded hypercube (equivalently the ordinary \((n-1)\)-cube with complementary edges added). Every distinct pair has integer distance between \(1\) and \(h\). The theorem applies only to \(n=4m\ge12\); it asserts no upper bound of this form for other parities. The logarithm is natural, and the normalization of Fourier coefficients is the unnormalized character sum.

A real symmetric kernel \(K\) is conditionally negative semidefinite if \(\sum_{a,b}u_au_bK(a,b)\le0\) for every real vector \(u\) with \(\sum_a u_a=0\). On finite abelian groups a translation-invariant kernel has this property if and only if all of its nontrivial Fourier eigenvalues are nonpositive. Schoenberg's criterion identifies negative type of \(d^p\) with Euclidean embeddability of \(d^{p/2}\). The set of admissible positive powers is an initial interval: if \(d^p\) is conditionally negative, then so is \(d^q\) for \(0<q<p\).

## Proof

**1. A parity Fourier obstruction.** Since \(n=2h\) is even, \(\chi([x])=(-1)^{\mathrm{wt}(x)}\) is a well-defined nonconstant character on \(G_n\). Its unnormalized distance-power eigenvalue is half the full-cube transform
\[
\tfrac12S_h(p),\qquad S_h(p)=\sum_{w=1}^{2h-1}(-1)^w\binom{2h}{w}\min(w,2h-w)^p.
\]
This identity is exact: every quotient class has two representatives with equal weight-parity and equal distance from the identity. Hence \(S_h(p)>0\) is sufficient to rule out negative type.

**2. Discrete Abel summation.** For \(0<p\le1\), put \(\Delta_w=(w+1)^p-w^p\) for \(w=0,\dots,h-1\); in particular \(\Delta_0=1\). Pairing opposite weight shells and applying the binomial alternating-partial-sum identity yields
\[
S_h(p)=-2\sum_{w=0}^{h-1}(-1)^w\binom{2h-1}{w}\Delta_w.
\]
Indeed \(\sum_{j=0}^w(-1)^j\binom{2h}{j}=(-1)^w\binom{2h-1}{w}\), so discrete summation by parts to the symmetric half-cube gives the identity without a boundary remainder. Since \(h\) is even, the terms with indices \(2,3\), \(4,5\), \(\ldots\), \(h-2,h-1\) can be paired:
\[
\begin{split}
S_h(p)={}&-2+2(2h-1)\Delta_1\\
&+2\sum_{\substack{2\le w\le h-2\\w\;\mathrm{even}}}
\left(\binom{2h-1}{w+1}\Delta_{w+1}-\binom{2h-1}{w}\Delta_w\right).
\end{split}
\]

**3. Positivity of paired increments.** For \(w\ge1\), the fundamental theorem of calculus gives \(\Delta_w=p\int_w^{w+1}t^{p-1}\,dt\). Pointwise comparison on adjacent unit intervals and \(0<p\le1\) show
\[
\frac{\Delta_{w+1}}{\Delta_w}\ge\left(\frac{w}{w+1}\right)^{1-p}\ge\frac w{w+1}.
\]
Writing \(B_w=\binom{2h-1}{w}\) and using \(B_{w+1}/B_w=(2h-1-w)/(w+1)\), we obtain
\[
B_{w+1}\Delta_{w+1}-B_w\Delta_w
\ge B_w\Delta_w\,
\frac{w\{2(h-w)-3\}-1}{(w+1)^2}.
\]
Every even \(w\) in the preceding sum satisfies \(2\le w\le h-2\), so \(h-w\ge2\) and the numerator is at least \(w-1>0\). In particular, keep only the final pair \(w=h-2\), whose numerator is \(h-3\). Since \(\Delta_{h-2}\ge p/(h-1)\) and
\[
2\binom{2h-1}{h-2}=\binom{2h}{h}\frac{h-1}{h+1},
\]
all other pairs are positive and therefore
\[
S_h(p)\ge -2+2(2h-1)(2^p-1)
+p\binom{2h}{h}\frac{h-3}{(h+1)(h-1)^2}.
\tag{1}
\]

**4. Explicit upper bound.** Define
\[
u_h=\frac{2(h+1)(h-1)^2}{\binom{2h}{h}(h-3)}.
\]
For every even \(h\ge6\), one has \(0<u_h<1\). A completely elementary verification uses the central-binomial lower estimate \(\binom{2h}{h}\ge(h+1)2^{h-1}\) (true at \(h=6\), then preserved by the ratio \((4h+2)/(h+1)>3\)); also \(2^h(h-3)>4(h-1)^2\) at \(h=6\) and thereafter by its increasing quotient. Substitution \(p=u_h\) in (1) gives \(S_h(u_h)\ge2(2h-1)(2^{u_h}-1)>0\). The parity Fourier eigenvalue is therefore positive. By continuity it stays positive on an interval below \(u_h\); since admissible exponents form an initial interval, \(\beta_n<u_h\).

**5. Uniform lower bound.** Set \(N=|G_n|=2^{n-1}\) and \(\ell_n=(4N\log h)^{-1}\). For positive \(p\le\ell_n\), let \(D_p=(d_n(a,b)^p)\) and \(D_0=J-I\), where \(J\) is the all-ones matrix. The difference \(E_p=D_p-D_0\) has zero diagonal and off-diagonal entries satisfying
\[
0\le (E_p)_{a,b}\le h^p-1\le e^{1/(4N)}-1\le\frac{1}{2N}.
\]
The last inequality follows from \(e^t-1\le2t\) for \(0\le t\le1/2\). Therefore \(\|E_p\|_2\le\|E_p\|_{\infty}<1/2\), because \(E_p\) is symmetric and each of its \(N\) rows contains at most \(N-1\) off-diagonal entries. On the zero-sum space \(D_0=-I\), whence
\[
u^TD_pu\le-\tfrac12\|u\|_2^2
\]
for every real zero-sum vector \(u\). Thus negative type is strict for the full interval \(0<p\le\ell_n\), in particular \(\beta_n\ge\ell_n=1/(2^{n+1}\log h)\).

**6. Exact exponential base.** Stirling's estimate \(\binom{2h}{h}\sim4^h/(\sqrt{\pi h})\) makes the upper bound \(u_h\sim2\sqrt\pi\,h^{5/2}4^{-h}\); the lower bound is \((2\cdot4^h\log h)^{-1}\). Taking \((2h)\)-th roots of both inequalities and letting \(h\to\infty\) through even integers proves \(\lim_{m\to\infty}\beta_{4m}^{1/(4m)}=1/2\).

## Verification

The standalone file `folded_cube_rate_check.py` uses Python 3 standard-library combinatorics and rational expressions. Run `python3 folded_cube_rate_check.py` to reproduce the finite checks. It verifies the full-cube/Abel-sum identity for \(n=4,6,\ldots,20\) at three positive powers, an independent exact \(p=1\) binomial identity, all paired-positivity arithmetic over a wide bounded range, the upper obstruction for \(n=12,16,20,24,28\), and an independent direct quotient-character computation for the first two of those dimensions. The exact analytic inequalities above, not the finite experiments, establish the infinite statement.

## Relationship to prior work

Wang et al. (2011) define folded hypercubes and analyze their crossing numbers; they do not assert powered negative-type exponents. Sánchez (2011) supplies general finite-metric negative-type/critical-exponent machinery, and Murugan (2011) investigates generalized roundness of vertex-transitive graphs and Hamming cube subsets. Aalipour et al. (2015) study graph distance spectra, including the **halved** cube, which is not the antipodal quotient considered here. Their inspected statements do not establish the exponential upper rate or the matching exponential base for this family. Standard finite-group Fourier diagonalization and binomial identities are used openly, not presented as new. A broad distance-regular association-scheme theorem may imply some ingredients; a bounded literature comparison cannot establish absolute publication priority.

## Limitations

Only dimensions divisible by four and at least twelve are treated. The theorem does not identify \(\beta_n\) exactly, prove the polynomial factor in its asymptotic, classify which Fourier character first changes sign, or give an optimal uniform bound for other dimensions. Numerical checks cover finitely many dimensions and do not independently prove any infinite assertion. The originality comparison is bounded and does not replace exhaustive historical review or independent verification.

## References

1. H. Wang, Y. Yang, Y. Zhou, W. Zheng, G. Wang, *The crossing number of folded hypercubes*, arXiv:1101.3386v1, first public 2011-01-18, https://arxiv.org/abs/1101.3386.
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2011-08-02, https://arxiv.org/abs/1108.0451.
3. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1, first public 2011-12-23, https://arxiv.org/abs/1112.5657.
4. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196v1, first public 2015-09-03, https://arxiv.org/abs/1509.01196.
