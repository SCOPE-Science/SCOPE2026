# Complete nullity census and a Gaussian invertibility threshold for finite-field split-pattern matrices

## Finding
Fix a prime power \(q\) and integers \(k,m\geq1\). Consider the uniform family of symmetric matrices
\[
M=\begin{pmatrix} C&B\\B^{\mathsf T}&D\end{pmatrix},\qquad
C\in\operatorname{Sym}_k(\mathbb F_q),\quad B\in\mathbb F_q^{k\times m},\quad
D=\operatorname{diag}(d_1,\ldots,d_m).
\]
All \(\binom{k+1}{2}+km+m\) independent entries range freely over \(\mathbb F_q\), including zero. The underlying permitted off-diagonal pattern is the complete split graph with a \(k\)-vertex clique and \(m\) independent-set vertices.

Define \(\mathcal N_{k,m,q}(z)=\sum_M z^{\dim\ker M}\). For \(0\leq t\leq\min(k,s)\), define the rectangular rank number
\[
R_{k,s}(t)=\frac{\prod_{i=0}^{t-1}(q^k-q^i)(q^s-q^i)}{\prod_{i=0}^{t-1}(q^t-q^i)}.
\]
For \(0\leq r\leq d\), define the symmetric rank number
\[
H_d(r)={d\brack r}_q q^{r(r+1)/2}h_r(q),\quad
h_r(q)=\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)}),
\]
where \({d\brack r}_q\) is the Gaussian binomial coefficient, and every empty product equals one. Then **every corank multiplicity** is given by the exact polynomial
\[
\boxed{\begin{aligned}
\mathcal N_{k,m,q}(z)
={}&\sum_{s=0}^{m}\binom ms(q-1)^{m-s}q^{k(m-s)}
\sum_{t=0}^{\min(k,s)} R_{k,s}(t)\\[-2pt]
&\qquad\cdot q^{\binom{k+1}{2}-\binom{k-t+1}{2}}
\sum_{r=0}^{k-t}H_{k-t}(r)\,z^{s-t+k-t-r}.
\end{aligned}}
\]
In particular, the total number of matrices is \(\mathcal N_{k,m,q}(1)=q^{\binom{k+1}{2}+km+m}\). Writing \(p_{k,m}(q)=\Pr(M\text{ is nonsingular})\), the exact probability simplifies to
\[
\boxed{p_{k,m}(q)=\sum_{s=0}^{\min(k,m)}\binom ms q^{-s}(1-q^{-1})^{m-s}
\left[\prod_{i=0}^{s-1}(1-q^{i-k})\right]h_{k-s}(q).}
\]

Define \(h_\infty(q)=\prod_{j\geq1}(1-q^{-(2j-1)})\), which is strictly positive. For fixed \(q\), if \(k/m\to\alpha<1/q\), then \(p_{k,m}(q)\to0\); if \(k/m\to\alpha>1/q\), then \(p_{k,m}(q)\to h_\infty(q)\). In the **critical window**, for each real \(u\) and
\[
k=k_m=\left\lfloor\frac{m}{q}+u\sqrt m\right\rfloor,\qquad
\sigma_q=\frac{\sqrt{q-1}}{q},
\]
we have the sharp limiting curve
\[
\boxed{\lim_{m\to\infty}p_{k_m,m}(q)=h_\infty(q)\Phi(u/\sigma_q),}
\]
where \(\Phi\) is the standard normal cumulative distribution function. More strongly, for \(\nu_m=\dim\ker M\) and a standard normal \(Z\),
\[
\boxed{\frac{\nu_m}{\sqrt m}\ \xrightarrow{\mathrm{law}}\ (\sigma_qZ-u)_+.}
\]
Thus the critical scaled corank has a positive-part Gaussian distribution, with an atom at zero; the actual nonsingularity probability includes the additional finite-field factor \(h_\infty(q)\).

## Assumptions and scope
The formula holds for every prime power, including characteristic two, and all positive integers \(k,m\). Entries in permitted positions are independent and *may vanish*: this is an affine matrix-pattern ensemble, not the set of matrices with an exact nonzero edge support. The asymptotic statements fix \(q\) and let \(m\) grow while \(k\) varies as specified; the limiting assertions are not joint limits in \(q\). All dimensions and ranks are over \(\mathbb F_q\).

## Proof
**1. Eliminate the nonzero peripheral diagonal entries.** Let \(s\) be the number of vanishing entries among the \(m\) diagonal entries of \(D\). There are \(\binom ms(q-1)^{m-s}\) choices for their zero positions and remaining nonzero values. Permute peripheral vertices so that \(D=\operatorname{diag}(D_1,0_s)\), where \(D_1\) is invertible of dimension \(m-s\), and write \(B=(B_1\mid B_0)\). Congruence by block Gaussian elimination gives
\[
M\ \sim_{\mathrm{congruence}}\ D_1\ \oplus\
\begin{pmatrix}C-B_1D_1^{-1}B_1^{\mathsf T}&B_0\\B_0^{\mathsf T}&0_s\end{pmatrix}.
\]
For each of the \(q^{k(m-s)}\) choices of \(B_1\), the shifted upper-left symmetric block \(C'=C-B_1D_1^{-1}B_1^{\mathsf T}\) runs bijectively through the full symmetric \(k\)-matrix space as \(C\) varies. Consequently \(C'\) is uniform and independent of \(B_0\).

**2. Rank the remaining rectangular coupling.** Let \(t=\operatorname{rank}B_0\), with exactly \(R_{k,s}(t)\) choices. Changes of bases in the two spaces reduce \(B_0\) to \(\begin{psmallmatrix}I_t&0\\0&0\end{psmallmatrix}\). Simultaneously eliminate the paired \(t\)-dimensional hyperbolic block by congruence. The residual form is an unrestricted symmetric form \(S\) on the \((k-t)\)-dimensional complement, together with an \((s-t)\)-dimensional zero block. Hence
\[
\dim\ker M=(s-t)+(k-t-\operatorname{rank}S).
\]
Fixing the restriction \(S\) imposes exactly \(\binom{k-t+1}{2}\) independent linear conditions on the \(\binom{k+1}{2}\) entries of \(C'\). Thus each \(S\) has exactly \(q^{\binom{k+1}{2}-\binom{k-t+1}{2}}\) lifts. The standard finite-field symmetric rank formula gives \(H_{k-t}(r)\) restrictions of rank \(r\): choose their radical, then a nondegenerate symmetric form on the quotient. Combining these disjoint cases proves the entire displayed corank polynomial, including the claimed total count.

**3. Nonsingularity.** The nullity equation forces \(s=t\leq k\), and requires the complementary symmetric form of dimension \(k-s\) to be nonsingular. A uniform \(k\)-by-\(s\) matrix has full column rank with probability \(\prod_{i=0}^{s-1}(1-q^{i-k})\); an independent uniform symmetric matrix of dimension \(k-s\) is nonsingular with probability \(h_{k-s}(q)\). Since \(s\) has the binomial law with parameters \(m\) and \(q^{-1}\), the exact probability follows.

**4. Sharp threshold and corank fluctuations.** Let \(S_m\sim\operatorname{Bin}(m,1/q)\). The binomial central limit theorem gives \((S_m-m/q)/\sqrt m\Rightarrow\sigma_qZ\). Uniformly in \(k,s\), the defect \(\min(k,s)-\operatorname{rank}B_0\) is tight: for any \(d\geq1\), a union bound over \(d\)-dimensional kernels of a uniform rectangular matrix gives \(\Pr(\text{defect}\geq d)\leq C_q q^{-d^2}\), using the Gaussian-binomial bound and transposition if necessary. Similarly, the corank of a uniform symmetric form is tight, since the expected number of its nonzero nullvectors is exactly \((q^e-1)q^{-e}<1\) in dimension \(e\). Therefore
\[
\nu_m=(S_m-k)_++O_{\mathbb P}(1).
\]
This proves the positive-part Gaussian weak limit in the critical window. For nonsingularity, on events where \(k-S_m\to+\infty\), the rectangular full-column-rank factor tends to one and \(h_{k-S_m}(q)\to h_\infty(q)\). Where \(S_m>k\), nonsingularity is impossible. The probability of the boundary band \(|S_m-k|=o(\sqrt m)\) tends to zero. Bounded convergence and the binomial central limit theorem yield \(h_\infty(q)\Phi(u/\sigma_q)\). The two off-critical limits follow from binomial concentration by the same reasoning.

## Verification
The standalone program `check.py` constructs matrices directly over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), independently performs finite-field Gaussian elimination and compares all observed nullity counts with the theorem's algebraic formula. Its captured output is `check_output.txt`. Eleven nontrivial hub/periphery combinations were exhaustively checked, as were 15 independent small-dimensional symmetric nonsingularity counts. All passed. These are bounded checks, not an exhaustive check over arbitrary dimensions or fields; the universal claim rests on the algebraic and probability proof above.

## Relationship to prior work
Barrett, van der Holst and Loewy (2005) classify finite-field graphs whose **minimum** possible symmetric matrix rank is two, with exact nonzero edge support. This does not enumerate all ranks in a random *allowed-support* split matrix pattern. Fulman and Goldstein (first arXiv version 2012) give the unrestricted symmetric finite-field rank distribution \(H_d(r)\), used here as a cited standard ingredient; their ensemble has no split-pattern zeros. Salmond, Grant, Grivell and Chan (2014 arXiv version) prove general bounds for uniformly random matrices with predetermined zeros, but do not give this symmetric split-pattern exact census or its critical-scale law. The new calculation combines a diagonal zero-count, a rectangular coupling rank, and an independent residual symmetric rank; in particular it identifies the phase boundary and the non-Gaussian critical corank law.

## Limitations
This theorem describes a particular exact zero pattern and a uniform distribution; it is not an arbitrary sparse-matrix universality theorem. The full finite characteristic-independent formula uses established symmetric-matrix rank counts. The critical-window convergence is weak convergence, not a uniform local-limit theorem or a finite-size error estimate. The argument does not establish historical uniqueness; another unindexed enumeration or an implicit specialization of a general block-matrix theorem remains possible.

## References
1. W. Barrett, H. van der Holst and R. Loewy, *Graphs whose minimal rank is two: The finite fields case*, Electronic Journal of Linear Algebra 14 (2005), 32–42. DOI: https://doi.org/10.13001/1081-3810.1175 . Publisher metadata gives 2005-01-01; printed issue is February 2005.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504v1, first posted 2012-11-02, Section 4. https://arxiv.org/abs/1211.0504 .
3. D. Salmond, A. Grant, I. Grivell and T. Chan, *On the rank of random matrices over finite fields*, arXiv:1404.3250v1, first posted 2014-04-12. https://arxiv.org/abs/1404.3250 .
