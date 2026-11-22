# Universal high-noise staircase for optimal parallel threshold localization

## Finding
Let \(k\ge3\) be fixed and let \(X\) be uniform on \([0,1]\). Before seeing any outcomes, choose \(k\) real thresholds \(t_1,\ldots,t_k\in[0,1]\), repetitions permitted. Query whether \(X\) exceeds each threshold; independently flip each correct binary response with probability \(p\in(0,1/2)\). Decode by the posterior mean, and let \(R_k(t,p)\) be its Bayes mean-squared error. Put \(\varepsilon=1-2p\), and let \(R_k^*(p)\) be the minimum over **all** fixed nonadaptive threshold vectors, without any symmetry restriction. Every global minimizer, in increasing order, satisfies as \(\varepsilon\downarrow0\)
\[
t_{(i)}=\frac12+\frac{2i-k-1}{4}\varepsilon^2+o_k(\varepsilon^2),\qquad i=1,\ldots,k.
\]
In particular, **every** globally optimal vector has distinct thresholds for sufficiently small positive \(\varepsilon\), and successive optimal spacings are asymptotic to \(\varepsilon^2/2\). If \(R_k^{\rm rep}(p)\) is the risk from repeating the midpoint \(k\) times, then the exact sharp leading advantage is
\[
\boxed{R_k^{\rm rep}(p)-R_k^*(p)=\frac{k(k^2-1)}{96}\varepsilon^6+o_k(\varepsilon^6).}
\]
For example, three unrestricted optimal thresholds approach \(1/2-\varepsilon^2/2\), \(1/2\), and \(1/2+\varepsilon^2/2\) up to \(o(\varepsilon^2)\), with risk improvement \(\varepsilon^6/4+o(\varepsilon^6)\). The displayed statements are asymptotic, **not** claims of exact optimal locations at a fixed nonzero noise contrast.

## Assumptions and scope
The number of questions \(k\) is fixed before taking the high-noise limit, with \(k\ge3\). The prior is exactly uniform. Responses are conditionally independent and identically binary-symmetric; the bit flip probability is constant, independent of position and query. The only admissible query sets are upper threshold half-intervals; thresholds may be placed anywhere in the closed unit interval and may coincide. All thresholds are determined in parallel, before any response. Estimation is by the exact posterior conditional mean for squared error. No adaptive, entropy-loss, arbitrary measurable query-set, or growing-\(k\) result is asserted. The primary mathematical object is the global stochastic optimization of Bayes risk over fixed threshold locations.

## Proof
**1. Exact finite-dimensional risk.** Write \(Z=X-1/2\), \(s_i(x)=2\mathbf1_{\{x\ge t_i\}}-1\), and let the observed signs \(Y_i\in\{-1,1\}\) satisfy
\[
\Pr(Y_i=y_i\mid X=x)=\frac{1+\varepsilon y_i s_i(x)}2.
\]
Given an outcome vector \(y\), put \(P_y=\mathbb E[\mathbf1_{\{Y=y\}}]\) and \(M_y=\mathbb E[Z\mathbf1_{\{Y=y\}}]\). Since \(P_y>0\) for \(0\le\varepsilon<1\), the law of total variance gives
\[
R_k(t,p)=\frac1{12}-J_k(t,\varepsilon),\qquad J_k(t,\varepsilon)=\sum_{y\in\{-1,1\}^k}\frac{M_y^2}{P_y}.
\]
This expression is continuous on the compact threshold cube, so a global risk minimizer exists for every \(0<\varepsilon<1\).

**2. Uniform weak-contrast expansion.** For a subset \(S\subseteq\{1,\ldots,k\}\), set \(y_S=\prod_{i\in S}y_i\), \(a_S=\mathbb E\prod_{i\in S}s_i(X)\), and \(b_S=\mathbb E[Z\prod_{i\in S}s_i(X)]\). Expansion of the independent likelihood gives the **exact** Walsh identities
\[
2^kP_y=1+\sum_{S\ne\varnothing}\varepsilon^{|S|}y_Sa_S,
\qquad 2^kM_y=\sum_{S\ne\varnothing}\varepsilon^{|S|}y_Sb_S.
\]
Summing over signs and expanding the positive denominator uniformly on the threshold cube, \(J_k\) is even analytic in \(\varepsilon\) near zero:
\[
J_k(t,\varepsilon)=\varepsilon^2A_2(t)+\varepsilon^4A_4(t)+\varepsilon^6H_k(t,\varepsilon),
\qquad A_2(t)=\sum_i[t_i(1-t_i)]^2.
\]
For fixed \(k\), the remainder \(H_k\) is uniformly bounded and locally Lipschitz in \(t\), with its Lipschitz constant independent of sufficiently small \(\varepsilon\): each Walsh moment is an integral of a bounded step-function product and changes by at most a constant times \(\|t-t'\|_1\), and each outcome denominator remains uniformly bounded away from zero. Odd powers vanish because changing the sign of \(\varepsilon\) simply flips every observed answer label.

**3. The first threshold-separation term.** Let \(t_i=1/2+d_i\). Set \(c_i=b_{\{i\}}=1/4-d_i^2\). Orthogonality of the Walsh monomials gives, for the fourth-order coefficient,
\[
\begin{aligned}
A_4={}&\sum_{i<j}b_{ij}^2-2\sum_{i<j}(c_i a_j+c_j a_i)b_{ij}
 +(\sum_i c_i^2)(\sum_i a_i^2)\\
&+2(\sum_i c_i a_i)^2-2\sum_i c_i^2a_i^2
 -2\sum_{i<j}c_i c_j a_{ij}.
\end{aligned}
\]
Here the subscripts \(i,j\) mean the corresponding one- or two-element subsets. Direct integration yields \(a_i=-2d_i\), \(a_{ij}=1-2|d_i-d_j|\), and \(b_{ij}=O(\|d\|^2)\) uniformly near the midpoint cluster. Therefore
\[
A_2(t)-A_2(\tfrac12\mathbf1)=-\frac12\sum_i d_i^2+\sum_i d_i^4,
\]
\[
A_4(t)-A_4(\tfrac12\mathbf1)=\frac14\sum_{i<j}|d_i-d_j|+O_k(\|d\|^2).
\]
The Lipschitz remainder from step 2 gives the useful **difference expansion**
\[
J_k(t,\varepsilon)-J_k(\tfrac12\mathbf1,\varepsilon)
=-\frac{\varepsilon^2}{2}\sum_i d_i^2
+\frac{\varepsilon^4}{4}\sum_{i<j}|d_i-d_j|
+O_k(\varepsilon^2\|d\|^4+\varepsilon^4\|d\|^2+\varepsilon^6\|d\|)
\]
for \(\|d\|\) small.

**4. All global optimizers enter the quadratic window.** Uniformly on the compact cube, \(J_k/\varepsilon^2\to A_2\). The function \(A_2\) is uniquely maximized when **every** threshold equals \(1/2\). Hence every maximizing threshold vector tends to the midpoint cluster. For such a vector, its excess information over the repeated-midpoint design is nonnegative. The difference expansion consequently implies, with constants depending only on fixed \(k\),
\[
0\le -c_k\varepsilon^2\|d\|^2+C_k\varepsilon^4\|d\|,
\]
for sufficiently small positive contrast, and therefore \(\|d\|=O_k(\varepsilon^2)\).

**5. Limiting optimization and sharp value.** Write \(d_i=\varepsilon^2u_i\) for any global optimizer. Step 4 bounds \(u\), and step 3 gives uniformly on bounded \(u\)-sets
\[
\varepsilon^{-6}\{J_k(\tfrac12\mathbf1+\varepsilon^2u,\varepsilon)-J_k(\tfrac12\mathbf1,\varepsilon)\}
=F_k(u)+o_k(1),\quad F_k(u)=\frac14\sum_{i<j}|u_i-u_j|-\frac12\sum_i u_i^2.
\]
Sorting \(u_1\le\cdots\le u_k\) gives the **exact square completion**
\[
F_k(u)=\frac12\sum_{i=1}^kv_i^2-\frac12\sum_{i=1}^k(u_i-v_i)^2,
\qquad v_i=\frac{2i-k-1}{4}.
\]
Thus the unique sorted maximizer is \((v_1,\ldots,v_k)\), and its value is \(\frac12\sum_i v_i^2=k(k^2-1)/96\). A trial vector with these scaled offsets supplies the matching lower bound; every convergent subsequence of sorted global optimizers must converge to this unique maximizer. Consequently the full sorted sequence has the asserted expansion and the risk gap has the asserted sharp coefficient. Since \(v_i-v_{i-1}=1/2>0\), the optimal finite-contrast thresholds are distinct for all sufficiently small positive contrasts. This completes the proof.

## Verification
The standalone `verify.py` computes \(J_k\) from exact rational cell integrals for one through five queries and checks the high-noise clustered design against replication, label permutation, and rational perturbations of its predicted offsets. It passes 40 nontrivial rational comparisons. Run `python3 verify.py` with Python 3.9 or later; no third-party packages are required. The finite checks are supplementary; the arbitrary-fixed-\(k\) limit follows from the uniform expansion and square completion above.

## Relationship to prior work
Variani, Lahouel, Bar-Hen and Jedynak (2015) study asymptotic mean-square localization under nonadaptive dyadic-bit questions and bit repetition, not an unrestricted fixed-length upper-threshold grid at vanishing channel contrast. Zhou and Hero (2019/2020) derive finite-blocklength bounds for resolution-exceedance probabilities and second-order large-query asymptotics, not a fixed-\(k\) Bayes quadratic-loss optimizer as \(p\to1/2\). A published two-query analysis, *Noise-calibrated thresholds for two parallel binary location queries* (2026), establishes exact placement within a **reflection-symmetric two-question** family; its small-contrast expansion matches the \(k=2\) consistency check here, but two questions alone cannot imply the unrestricted any-fixed-\(k\ge3\) sorted staircase or the degree-three budget law. The present theorem concerns the opposite asymptotic regime from coding-theoretic long-horizon estimates: fixed query budget and vanishing per-bit information.

## Limitations
Only leading asymptotics at fixed \(k\) are established; uniqueness of the exact finite-contrast optimizer, global monotonicity of optimal spacings as noise changes, and rates uniform in growing \(k\) remain open. For fixed positive contrast, the staircase is an approximation, not an exact optimizer. Distinct optimal thresholds are guaranteed only for sufficiently high noise (depending on \(k\)). The result does not cover adaptive location questions, arbitrary measurable sets, correlated or measurement-dependent bit noise, different priors, or other loss functions. An undiscovered equivalent weak-channel design theorem remains a historical-priority risk; literature searching is not a formal novelty certificate.

## References
1. E. Variani, K. Lahouel, A. Bar-Hen, B. Jedynak, *Non-Adaptive Policies for 20 Questions Target Localization*, arXiv:1504.05996 (first public 2015-04-22), https://arxiv.org/html/1504.05996v3 .
2. L. Zhou, A. Hero, *Resolution Limits for the Noisy Non-Adaptive 20 Questions Problem*, arXiv:1909.12954 (first public 2019-09-27); later version arXiv:2004.07231 (2020-04-15), full HTML: https://ar5iv.labs.arxiv.org/html/2004.07231 .
3. *Noise-calibrated thresholds for two parallel binary location queries*, publicly available result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-noise-calibrated-thresholds-for-two-parallel-binary-location-que--dedce94eaa8e/RESULT.md .
4. D. Dereniowski, A. Łukasiewicz, P. Uznański, *Noisy (Binary) Searching: Simple, Fast and Correct*, arXiv:2107.05753 (2021-07-12), https://arxiv.org/abs/2107.05753 .
