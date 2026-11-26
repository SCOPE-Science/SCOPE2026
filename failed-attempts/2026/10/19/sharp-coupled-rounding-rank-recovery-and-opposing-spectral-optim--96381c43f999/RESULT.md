# Sharp coupled-rounding rank recovery and opposing spectral optimum for duplicate columns

## Finding
Let \(n\ge2\), \(0<p<1\), and consider the rank-one matrix \(A=p\mathbf 1_{n\times2}\). Round every entry to \(0\) or \(1\) without bias, independently **between rows** but permitting arbitrary, identically distributed dependence between the two rounded entries within each row. Write \(q=\Pr(B_{i1}=B_{i2}=1)\). The feasible range is \(\max(0,2p-1)\le q\le p\). The exact full-real-column-rank probability of the rounded matrix \(B\) is
\[
P_n(p,q)=1-2(1-p)^n-(1-2p+2q)^n+2(1-2p+q)^n.
\]
Over **all** such common-marginal row-independent rounding schemes and all \(0<p<1\), this probability has the unique maximizer \(p=2/3\), \(q=1/3\), which produces the three rows \((1,0),(0,1),(1,1)\) with equal probabilities and never produces \((0,0)\). The sharp finite-sample recovery probability is
\[
\max_{p,q}P_n(p,q)=1-3^{1-n}.
\]
By contrast, the unique scheme maximizing the limiting smallest-singular-value coefficient \(\lim_{n\to\infty}\sigma_{\min}(B)/\sqrt n\) uses \(p=1/2,q=0\), with value \(1/\sqrt2\), compared with \(1/\sqrt3\) at the finite-rank-probability optimum. At these two input-level/coupling pairs, the limiting spectral condition numbers are respectively \(1\) and \(\sqrt3\), and the rank-failure probabilities are respectively \(2^{1-n}\) and \(3^{1-n}\).

For independent entrywise stochastic rounding at the **same** \(p=2/3\), the rank-failure probability is \(2\cdot3^{-n}+(5/9)^n-2\cdot9^{-n}\). Its ratio to the optimally coupled failure probability is asymptotic to \((5/3)^n/3\). The exponential comparison is between two correctly specified schemes with the same entrywise means and independent rows; it is **not** a guarantee for arbitrary inter-row dependence or hardware implementations. At a **fixed** input level \(p\), both criteria favor the smallest feasible \(q\); the conflicting global optima arise because the input level also varies across the rank-one family.

## Assumptions and scope
Every unrounded entry equals the same real \(p\in(0,1)\), and each rounded entry is a Bernoulli random variable with mean \(p\). For each row, the joint law is arbitrary subject to both marginals being Bernoulli\((p)\). The joint distribution is identical and independent across the \(n\) rows. The parameter \(q\) fully describes this within-row law. Rank and singular values are computed over \(\mathbb R\), in exact arithmetic. The finite-sample probability and optimizer hold for each integer \(n\ge2\). The spectral assertions hold almost surely as \(n\to\infty\) along independent rows from a fixed law, with \(p,q\) fixed.

## Proof
**Parameterization.** The row atom probabilities are
\[
a=\Pr(00)=1-2p+q,\qquad b=\Pr(10)=\Pr(01)=p-q,\qquad d=\Pr(11)=q.
\]
Their nonnegativity is equivalent to \(\max(0,2p-1)\le q\le p\).

**Exact full-rank probability.** Two binary columns are linearly independent over \(\mathbb R\) exactly when at least two of the three distinct nonzero row types \(10,01,11\) appear among the \(n\) rows. Let \(E_{10},E_{01},E_{11}\) denote the events that every row is either \(00\) or the indicated single type. Rank deficiency is their union. Each pairwise or triple intersection is the all-zero matrix, of probability \(a^n\). Because \(\Pr(E_{10})=\Pr(E_{01})=(a+b)^n=(1-p)^n\) and \(\Pr(E_{11})=(a+d)^n=(1-2p+2q)^n\), inclusion-exclusion gives the stated formula.

**Global finite-sample optimizer.** The rank-deficiency probability \(F_n=1-P_n\) satisfies
\[
\frac{\partial F_n}{\partial q}=2n\big[(1-2p+2q)^{n-1}-(1-2p+q)^{n-1}\big]\ge0.
\]
For each fixed \(p\), the minimum is uniquely attained at \(q_*(p)=\max(0,2p-1)\): the derivative is strictly positive at all feasible \(q>0\), and integration from the left endpoint is strict whenever the interval has positive length. Consequently
\[
F_n(p,q_*(p))=\begin{cases}
2(1-p)^n-(1-2p)^n,&0<p\le1/2,\\
2(1-p)^n+(2p-1)^n,&1/2\le p<1.
\end{cases}
\]
The first branch decreases strictly in \(p\), since its derivative is \(2n[(1-2p)^{n-1}-(1-p)^{n-1}]<0\) in its interior. The second branch has derivative \(2n[(2p-1)^{n-1}-(1-p)^{n-1}]\), negative before \(p=2/3\), zero there, positive thereafter. This proves the unique global minimizer of failure, and substitution gives \(F_n=3^{1-n}\).

**Asymptotic spectral comparison.** The strong law for the four row types yields, entrywise and hence in operator norm,
\[
\frac1n B^{\mathsf T}B\longrightarrow\begin{pmatrix}p&q\\q&p\end{pmatrix}\quad\text{almost surely}.
\]
Its eigenvalues are \(p+q\) and \(p-q\), so continuity of eigenvalues gives
\[
\frac{\sigma_{\min}(B)}{\sqrt n}\to\sqrt{p-q},\qquad
\frac{\sigma_{\max}(B)}{\sqrt n}\to\sqrt{p+q}.
\]
The constraints force \(p-q\le\min\{p,1-p\}\le1/2\), with equality only at \(p=1/2,q=0\). Therefore that scheme uniquely maximizes the limiting smallest singular value; it has limit Gram matrix \(I_2/2\). The full-rank-probability optimal scheme instead has limiting Gram matrix with diagonal \(2/3\) and off-diagonal \(1/3\), whose eigenvalues are \(1\) and \(1/3\). This proves both spectral thresholds and condition numbers. The finite failure values follow by substitution in the exact probability formula.

**Independent-entry benchmark.** Independent rounding has \(q=p^2\). At \(p=2/3\), the atom probabilities are \(a=1/9\), \(b=2/9\), \(d=4/9\), giving the stated exact failure expression. Dividing by \(3^{1-n}\), the leading term \((5/9)^n\) yields the exponential comparison.

## Verification
A standalone Python 3 standard-library script, `verify_rounding.py`, enumerates exact-rational multinomial probabilities for the four possible row types and checks the inclusion-exclusion formula across integers \(2\le n\le8\) and seven rational rounding means with several feasible couplings. It compares all 210 rational cases exactly, tests closed-form benchmark probabilities, and prints `VERIFY_OK`. Run with `python3 verify_rounding.py`. The analytic optimization, strong-law limit and exponential comparison follow from the proof, not from enumeration. The recorded output appears in `verification_output.txt`.

## Relationship to prior work
Dexter, Boutsikas, Ma, Ipsen and Drineas [1] establish the role of independent-entry stochastic rounding in regularizing tall-and-thin matrices, and specifically examine an all-\(1/2\), rank-one, two-column input (Section 4.1 and Appendix A). Their stochastic-rounding model assumes all entrywise errors are independent (Section 2.2); their matrix-perturbation theorem therefore does not imply the stated optimal within-row dependence design, exact finite-sample law, or its competing spectral optimum. The finite-rank statement is a constrained exact occupancy calculation; familiar D-optimal and E-optimal design objectives motivate but do not by themselves establish the finite-\(n\) stochastic-rounding optimizer [2]. The published rank-two DNA coverage-depth result [3] optimizes repeated sampling of fixed code columns over finite-field projective classes, not common-marginal coupled stochastic rounding of duplicated real columns. General rank thresholds for sparse random matrices [4] consider prescribed sparse degree sequences instead of this exact two-column parameterized law.

## Limitations
Changing \(p\) changes the input matrix: the comparison over \(p\) is a phase diagram across input levels, not a claim that a rounding algorithm can freely choose the input values. This result does not address independent rounding of heterogeneous matrix entries, arbitrary cross-row dependencies, more than two columns, floating-point hardware, or rank/condition-number optimization beyond the stated iid-row family. The spectral results are asymptotic rather than finite-\(n\) tail bounds. The finite formula is obtained with elementary inclusion-exclusion; while a targeted literature comparison found no identical full optimization statement, equivalent finite occupancy or design-theoretic formulations may exist. The result does not establish that maximizing exact full-rank probability is universally the best regularization objective.

## References
1. G. Dexter, C. Boutsikas, L. Ma, I. C. F. Ipsen and P. Drineas, *Stochastic Rounding Implicitly Regularizes Tall-and-Thin Matrices*, arXiv:2403.12278v1 (first submitted 18 March 2024), especially Sections 2.2 and 4.1 of the open-access v3 text: https://arxiv.org/html/2403.12278v3.
2. Classical D- and E-optimal experimental design criteria; cited here for motivation and terminology, not as a novelty certificate.
3. *Exact rank-two optimum for DNA coverage depth*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-rank-two-optimum-for-dna-coverage-depth--db2f9e82bdf9.
4. A. Coja-Oghlan, A. A. Ergür, P. Gao, S. Hetterich and M. Rolvien, *The Rank of Sparse Random Matrices*, SODA 2020, DOI: 10.1137/1.9781611975994.35.
