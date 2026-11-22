# A sharp golden-ratio bound for failure of square hyponormality on one-fork trees

## Finding

Let \(\mathcal F_{r,m}\) be the rooted directed tree formed by a stem of \(r\geq0\) edges leading to one fork, followed by \(m\geq2\) pairwise disjoint infinite rays, where \(m\) may also be countably infinite. For a bounded weighted shift \(S\) on \(\ell^2(\mathcal F_{r,m})\), put
\[
\Delta(S)=\left\|\left(S^{*2}S^2-S^2S^{*2}\right)_{-}\right\|,
\qquad A_-:=\max\{-A,0\}\quad(A=A^*).
\]
Among all hyponormal contractions on this fixed tree,
\[
\boxed{\sup_{S\text{ hyponormal},\ \|S\|\leq1}\Delta(S)=
\begin{cases}
0,&r=0,\\[2pt]
(\sqrt5-2)/4,&r\geq1.
\end{cases}}
\]
The positive bound is attained by a shift with **strictly positive weights on every edge**, for every \(r\geq1\) and each permitted \(m\), including countably infinite branching. In particular, for arbitrary bounded hyponormal shifts on these trees, \(\Delta(S)\leq (\sqrt5-2)\|S\|^4/4\), and the constant cannot be reduced if the fork has a parent.

The distinction between a root fork and a non-root fork measures quantitatively the qualitative breakdown of power hyponormality: a single backward edge above an otherwise identical fork permits a sharp negative spectral defect in the self-commutator of the square.

## Assumptions and scope

All Hilbert spaces are complex. A weighted shift on a directed tree acts by \(Se_v=\sum_{w\in\operatorname{Chi}(v)}\lambda_w e_w\), where the series is square-summable for each vertex. Hyponormal means \(S^*S-SS^*\geq0\). We make **no** uniform lower bound assumption on the weights; zero weights are allowed in the upper bound. Sharp examples have all weights positive. The fork has exactly \(m\) children, each initiating an infinite, unbranched ray. The stem is finite and unbranched. The result is not asserted for trees with two or more forks.

Write \(u\) for the fork. If \(r\geq1\), let \(a\) denote the weight on its incoming edge. For ray \(j\), write \(b_j\) for the weight from \(u\) to its first vertex and \(d_{j,n}\) for the weight from ray vertex \(n\) to \(n+1\). Phases can be removed by a diagonal unitary, so the proof uses their absolute values. Set \(X_j=|d_{j,1}|^2\), \(s=\sum_j |b_j|^2\), and \(b=(b_j)_j\). After normalizing \(\|S\|\leq1\), we have \(0\leq X_j\leq1\) and \(s\leq1\).

## Proof

**1. Local operator blocks.** For any weighted shift \(R\) on a directed forest, the supports of \(Re_v\) for distinct vertices are disjoint. Consequently \(R^*R\) is diagonal and \(RR^*\) is a direct sum, over parents, of rank-one matrices on their child sets. On a child set with incoming vector \(c\), the self-commutator block is \(\operatorname{diag}(\|Re_w\|^2)-cc^*\). This description applies equally to \(R=S\) and \(R=S^2\), the latter regarded as a shift on the two-step forest. A block \(\operatorname{diag}(z_j)-cc^*\) with \(z_j>0\) is positive exactly when \(\sum_j|c_j|^2/z_j\leq1\). Zero diagonal coordinates are treated by continuity, or directly by positivity forcing their corresponding incoming coefficients to vanish.

Hyponormality of \(S\) therefore yields
\[
\sum_{j:X_j>0}\frac{|b_j|^2}{X_j}\leq1,
\qquad |a|^2\leq s\quad(r\geq1),
\qquad |d_{j,n+1}|\geq|d_{j,n}|.
\]
In particular \(b_j=0\) whenever \(X_j=0\). The stem weights are nondecreasing toward the fork, and all are at most \(\sqrt{s}\).

The two-step forest has at most two branching parents: the original fork, and its immediate predecessor if one exists. At the original fork its grandchildren block is nonnegative, because the incoming coefficients are \(b_jd_{j,1}\), the grandchildren outgoing two-step weights have moduli \(|d_{j,2}d_{j,3}|\geq X_j\), and hence
\[
\sum_j\frac{|b_jd_{j,1}|^2}{|d_{j,2}d_{j,3}|^2}
\leq\sum_{j:X_j>0}\frac{|b_j|^2}{X_j}\leq1.
\]
The one-child blocks along rays are nonnegative by monotonicity. The one-child blocks on the stem are also nonnegative, including the junction: Cauchy--Schwarz gives
\[
s^2\leq\left(\sum_j|b_j|^2X_j\right)
\left(\sum_{j:X_j>0}\frac{|b_j|^2}{X_j}\right)
\leq\sum_j|b_j|^2X_j,
\]
so the outgoing squared norm \(\|S^2e_u\|^2\) dominates every incoming two-step squared stem weight. The adjacent stem block follows from \(|a|^2\leq s\), and earlier blocks from monotonicity.

If \(r=0\), there is no other branching parent and hence \(S^2\) is hyponormal. If \(r\geq1\), the **only possibly nonpositive** block, indexed by the first vertices of the rays, is
\[
D=\operatorname{diag}(|d_{j,1}d_{j,2}|^2)-|a|^2bb^*
\ \geq\ \operatorname{diag}(X_j^2)-sbb^*.
\]
This is an operator inequality on \(\ell^2\) of the ray index set; it remains valid for countably many rays.

**2. Sharp scalar majorant.** Put
\[
\alpha=\frac{\sqrt5-1}{4},\qquad
\delta=\frac{\sqrt5-2}{4},\qquad
\sigma=\frac{1+\sqrt5}{4}.
\]
For every \(0\leq x\leq1\), the following identity proves the inequality indicated:
\[
\left(\frac2\sigma-\frac{x}{\sigma^2}\right)(x^2+\delta)-x
=\frac{(1-x)(x-\alpha)^2}{\sigma^2}\geq0,
\quad\text{so}\quad
\frac{x}{x^2+\delta}\leq\frac2\sigma-\frac{x}{\sigma^2}.
\]
For completeness, let \(\mu=\sum_{X_j>0}|b_j|^2/X_j\leq1\). If \(\mu=0\), then \(b=0\) and \(D\geq0\). Otherwise set \(p_j=|b_j|^2/(\mu X_j)\); these are nonnegative and sum to one. With \(\rho=\sum_j p_jX_j\), we have \(s=\mu\rho\). The scalar inequality gives
\[
\begin{aligned}
s\sum_j\frac{|b_j|^2}{X_j^2+\delta}
&=\mu^2\rho\sum_jp_j\frac{X_j}{X_j^2+\delta}\\
&\leq\mu^2\rho\left(\frac2\sigma-\frac\rho{\sigma^2}\right)\\
&\leq1-\left(1-\frac\rho\sigma\right)^2\leq1.
\end{aligned}
\]
By the rank-one positivity criterion, \(\operatorname{diag}(X_j^2+\delta)-sbb^*\geq0\). Thus \(D\geq-\delta I\) and \(\Delta(S)\leq\delta\). The proof uses no finite-dimensional enumeration and remains valid for countable index sets.

**3. Exact sharpness and branch-number independence.** Let \(q=(5-\sqrt5)/10\). Set \(X_1=\alpha\) and \(X_j=1\) for \(j\geq2\). Choose strictly positive masses \(p_j\) summing to one with \(p_1=q\). For finite \(m\), take \(p_j=(1-q)/(m-1)\) when \(j\geq2\); for countably infinite \(m\), take \(p_j=(1-q)2^{-(j-1)}\) for \(j\geq2\). Set \(b_j=\sqrt{p_jX_j}\), every ray weight equal to \(\sqrt{X_j}\), and every stem weight equal to \(\sqrt\sigma\). Since
\[
\sum_j\frac{b_j^2}{X_j}=1,
\qquad \sum_jb_j^2=q\alpha+(1-q)=\sigma,
\]
the resulting norm-one shift is hyponormal. Here the potentially negative block is exactly \(D=\operatorname{diag}(X_j^2)-\sigma bb^*\).

Both terms where the scalar majorant becomes equality (\(x=\alpha\) and \(x=1\)) occur with the precise probabilities giving \(\rho=\sigma\). Therefore
\[
\sigma\sum_j\frac{|b_j|^2}{X_j^2+\delta}=1.
\]
The nonzero vector with coordinates \(b_j/(X_j^2+\delta)\) lies in the kernel of \(D+\delta I\). The previously proved lower bound forces \(\min\sigma(D)=-\delta\). Thus \(\Delta(S)=\delta\), with every edge weight strictly positive. Scaling proves the unnormalized statement. \(\square\)

## Verification

The symbolic certificate has only one nonstandard algebraic step: the exact cubic factorization in Step 2. The accompanying standalone `verify.py` checks it in the quadratic number field \(\mathbb Q(\sqrt5)\), verifies exactly that the two-ray extremizer has eigenvalue \(-\delta\), and executes 8,000 finite-coordinate secular-inequality spot checks. Run with `python3 verify.py` using Python 3.10+ and SymPy. These checks do not replace the proof or certify all infinite shifts.

## Relationship to prior work

Jabłoński--Jung--Stochel introduced one-fork weighted shifts and displayed bounded hyponormal shifts whose squares fail hyponormality, in particular Example 5.3.2 of the work below. Pikul's backward-extension results characterize hyponormality of powers using local ratios, and his 2023 manuscript characterizes forests for which hyponormality forces power hyponormality. Those qualitative criteria imply the **possibility** of failure at a non-root fork, but the inspected statements and examples do not give the sharp norm-one self-commutator defect, the golden-ratio constant, or its independence of the number of rays. The present statement is a quantitative extremal result, not a claim to have discovered the qualitative counterexample or the local hyponormality criterion.

## Limitations

This result concerns one-fork rooted trees, not arbitrary directed forests or trees with iterated branching. The defect is that of the **square**, not of all powers and not a distance to the set of power-hyponormal operators. The supporting random experiments alone cannot prove any universal claim. Absence of an identical result from indexed searches is not a proof of historical priority, and independently established priority or independent mathematical validation is not claimed.

## References

1. P. Pikul, *Weighted shifts on directed forests and hyponormality*, preprint first public 15 July 2023, arXiv:2307.07777, especially Section 5, Theorems 5.2 and 5.4. https://arxiv.org/abs/2307.07777
2. P. Pikul, *Backward extensions of weighted shifts on directed trees*, arXiv:2109.05970, first public 13 September 2021, especially Theorems 4.1 and 4.8. https://arxiv.org/abs/2109.05970
3. Z. Jabłoński, I. B. Jung, J. Stochel, *Weighted shifts on directed trees*, arXiv:0911.3821, first public 19 November 2009, especially Section 5.3, Example 5.3.2. https://arxiv.org/abs/0911.3821
