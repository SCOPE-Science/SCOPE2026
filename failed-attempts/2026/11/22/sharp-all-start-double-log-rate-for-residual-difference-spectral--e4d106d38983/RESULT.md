# Sharp all-start double-log rate for residual-difference spectral steps on two-mode systems

## Finding
Let \(A\in\mathbb R^{m\times n}\) have full column rank, \(m\ge n\), and suppose \(A^{\mathsf T}A\) has exactly two distinct positive eigenvalues \(0<b<a\), with arbitrary multiplicities. For a consistent system \(Ax=b_{\mathrm{data}}\), initialize at any \(x_0\), define \(r_k=b_{\mathrm{data}}-Ax_k\), and use one residual Rayleigh step followed by the residual-difference (RD) steps specified below. If \(r_0\) has a nonzero component in each squared-singular-value eigenspace, the iteration never terminates in finite exact arithmetic, but satisfies
\[
\boxed{\lim_{k\to\infty}\frac1k\log\log\left(\frac{\|r_0\|_2}{\|r_k\|_2}\right)=\frac12\log2.}
\]
More strongly, constants \(c,C>0\), depending on the system and initialization, give for all sufficiently large \(k\)
\[
\exp(-C2^{k/2})\le\frac{\|r_k\|_2}{\|r_0\|_2}\le\exp(-c2^{k/2}).
\]
If \(r_0=0\), the system is already solved; if \(r_0\ne0\) lies in a single eigenspace, the initial Rayleigh step terminates exactly. Unlike the matched-initialized delayed long/BB1 step, this short/RD rule has **no exceptional mixed-data geometric orbit** under its specified warm start.

## Assumptions and scope
The system is real, consistent and of full column rank; the residual is always in \(\operatorname{range}(A)\), even when \(m>n\). Put \(B=AA^{\mathsf T}\). For \(r_k\ne0\) set \(x_{k+1}=x_k+\alpha_kA^{\mathsf T}r_k\), so \(r_{k+1}=(I-\alpha_kB)r_k\). The initial step is
\[
\alpha_0=\frac{r_0^{\mathsf T}r_0}{r_0^{\mathsf T}Br_0}.
\]
For every \(k\ge1\) use the residual-difference rule
\[
\alpha_k=\frac{\|r_k-r_{k-1}\|_2^2}{\|A^{\mathsf T}(r_k-r_{k-1})\|_2^2}
=\frac{r_{k-1}^{\mathsf T}B^2r_{k-1}}{r_{k-1}^{\mathsf T}B^3r_{k-1}}.
\]
These equalities are valid before termination, using \(r_k-r_{k-1}=-\alpha_{k-1}Br_{k-1}\). Multiplicities may exceed one. The limit is an \(R\)-type sharp double-logarithmic rate, *not* a claim that consecutive norms contract or that each ratio tends to zero.

## Proof
**1. Normalize and reduce to two scalar energies.** Scaling \(B\) by \(b^-1\) scales every step by \(b\) and leaves the residual path unchanged. Thus take spectral levels \(L=a/b>1\) and \(1\). Let \(P_L,P_1\) be the two orthogonal projectors on \(\operatorname{range}(A)\) and write \(u_k=\|P_Lr_k\|_2\), \(v_k=\|P_1r_k\|_2\). If \(u_0v_0>0\), put \(e_k=u_k^2/v_k^2>0\). The first Rayleigh step has high/low multipliers \(-(L-1)/(Le_0+1)\) and \((L-1)e_0/(Le_0+1)\), respectively. Hence \(e_1=e_0^-1\) and \(u_1v_1>0\).

**2. Short-step recurrence and the absence of a balanced exception.** For \(k\ge1\), the preceding residual has ratio \(e_{k-1}\), and therefore
\[
\alpha_k=\frac{L^2e_{k-1}+1}{L^3e_{k-1}+1}.
\]
Writing \(t_k=L^2e_k\), its high- and low-mode multipliers are respectively
\[
-\frac{L-1}{1+Lt_{k-1}},\qquad \frac{(L-1)t_{k-1}}{1+Lt_{k-1}}.
\]
They never vanish for finite positive \(t_{k-1}\), so neither eigenspace disappears. Their squared ratio gives the **exact** recursion
\[
 t_{k+1}=\frac{t_k}{t_{k-1}^2},\qquad k\ge1.
\]
Let \(z_k=\log t_k\). Then \(z_{k+1}=z_k-2z_{k-1}\). Warm-starting forces \(t_0=L^2e_0\), \(t_1=L^2/e_0\), so \(t_0t_1=L^4>1\). In particular \((z_0,z_1)\ne(0,0)\). There is no nonzero bounded solution of this recurrence: its characteristic roots have modulus \(\sqrt2>1\), hence
\[
 z_j=Q(\sqrt2)^j\cos(j\theta-\delta),\quad Q>0,\quad \theta=\arccos\left(\frac{1}{2\sqrt2}\right).
\]

**3. Uniform large excursions of both signs.** Since \(\pi/3<\theta<\pi/2\), the four circle points \(0,\theta,2\theta,3\theta\) have largest circular gap \(\max(\theta,2\pi-3\theta)<\pi\). By compactness, there is a fixed \(\eta>0\) such that any four successive cosines in the preceding formula include one at least \(\eta\) and another at most \(-\eta\), regardless of the phase. Hence every sufficiently late block of four \(z_j\) includes both a positive and a negative value of magnitude at least \(\eta Q(\sqrt2)^j\), where \(j\) denotes the first index in that block. Also \(|z_j|\le Q(\sqrt2)^j\).

**4. Convert ratio excursions to a sharp norm exponent.** For \(k\ge1\), the two multiplier logarithms are
\[
\log\left|1-L\alpha_k\right|=\log(L-1)-\log(1+Le^{z_{k-1}}),
\]
\[
\log\left|1-\alpha_k\right|=\log(L-1)+z_{k-1}-\log(1+Le^{z_{k-1}}).
\]
Uniformly in \(z\in\mathbb R\), the first right-hand side differs from \(-[z]_+\) by at most a constant depending on \(L\), and the second differs from \(-[-z]_+\) by at most such a constant. Summing the logarithms gives, for \(k\to\infty\),
\[
-\log(u_k/u_0)=\sum_{j=0}^{k-2}[z_j]_++O_L(k),\qquad
-\log(v_k/v_0)=\sum_{j=0}^{k-2}[-z_j]_++O_L(k),
\]
where the first (Rayleigh) step merely changes the bounded remainder. The upper bounds \(|z_j|\le Q2^{j/2}\) make both sums \(O(2^{k/2})\). The four-index sign-excursion property applied to the last four terms gives lower bounds \(\Omega(2^{k/2})\) for **each** sum. Since \(O(k)=o(2^{k/2})\), positive constants \(c_s,C_s\) exist such that each nonzero mode norm lies between \(e^{-C_s2^{k/2}}\) and \(e^{-c_s2^{k/2}}\) times its initial norm. Orthogonality yields the same two-sided estimate for the whole residual. Taking logarithms twice proves the limit. Finally, on a single active eigenspace \(\alpha_0\) is exactly the inverse eigenvalue, giving immediate termination. \(\square\)

## Verification
The standalone `verify.py` recomputes the actual residual-difference updates with independent exact rational arithmetic, then checks the short-step spectral formula, nonvanishing, and the ratio recurrence on several rational two-level systems with both balanced and imbalanced starts. It also verifies the warm-start identity and the characteristic recurrence. These are reproducible finite checks, not a substitute for the analytic infinite-iteration proof.

## Relationship to prior work
The RD update and its equivalence to the short BB2 secant step are already in Xu [1]; its treatment analyzes the delayed long/DR scheme on the two-mode model and reports numerical RD experiments, without the stated sharp all-start RD double-log law. Early BB theory [2,3] already proves qualitative two-dimensional superlinear properties; neither BB2 formulas nor generic \(R\)-superlinearity are claimed as new. Yang and Yuan [4] study sharp uniform worst-case BB rates. The published alternating-long/short two-mode analysis [5] proves the same exponential *order* for a different sequence that explicitly alternates BB1 and BB2; the present finding establishes it for Xu's **unmixed RD/BB2** iteration with its one-step RSHK initialization. A separate published two-mode BB1 result [6] obtains a finer log-periodic profile for the long rule, not the present short rule. An equivalent derivation may exist in unindexed early BB analyses and remains a priority risk.

## Limitations
Only exact arithmetic, consistent full-column-rank systems with precisely two positive squared singular levels, and the specified Rayleigh warm start are covered. There is no asserted dimension-independent constant \(c\), no result for three or more distinct nonzero singular levels, no claim about inconsistent systems or noisy observations, and no Q-superlinear assertion for individual consecutive steps. The exact \(R\)-rate can be destroyed by finite-precision rounding after very small residuals. The mathematical result has not received independent audit.

## References
[1] X. Xu, *Two-point residual step size gradient methods for linear systems*, arXiv:2611.02743v1 (first public 2026-11-02), https://arxiv.org/html/2611.02743v1.

[2] J. Barzilai and J. M. Borwein, *Two-Point Step Size Gradient Methods*, IMA Journal of Numerical Analysis **8** (1988), 141–148, https://doi.org/10.1093/imanum/8.1.141.

[3] Y.-H. Dai, *A New Analysis on the Barzilai-Borwein Gradient Method*, Journal of the Operations Research Society of China **1** (2013), 187–198, https://doi.org/10.1007/s40305-013-0007-x.

[4] S. Yang and Y.-X. Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai–Borwein Method in \(\mathbb R^d\) and Hilbert Spaces*, arXiv:2608.07839, https://arxiv.org/abs/2608.07839.

[5] *Alternating long–short spectral steps eliminate the balanced two-mode slowdown*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-alternating-long-short-spectral-steps-eliminate-the-balanced-two--0e04302e58f6.

[6] *A universal log-periodic gradient envelope for two-mode Barzilai–Borwein descent*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-universal-log-periodic-gradient-envelope-for-two-mode-barzilai--80f835ec743a.
