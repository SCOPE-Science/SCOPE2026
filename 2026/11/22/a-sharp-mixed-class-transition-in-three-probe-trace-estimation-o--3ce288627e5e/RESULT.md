# A sharp mixed-class transition in three-probe trace estimation on balanced bicliques

## Finding
Let \(n\ge3\) be an integer, let \(H=K_{n,n}\) be the unweighted balanced complete bipartite graph with shores \(A\) and \(B\), and let \(G_\mu=(\mu I+L_H)^{-1}\) for any real \(\mu>0\). Partition the \(2n\) vertices into exactly three nonempty, *unlabeled* classes and use one independent class-supported Rademacher quadratic-form probe per class to estimate \(\operatorname{tr}G_\mu\). Proper coloring is not imposed.

Put
\[
\kappa=\frac{n}{\mu(\mu+n)(\mu+2n)},\qquad
\theta=\left(1+\frac{\mu}{n}\right)^2,
\]
and for each integer \(s\) define
\[
H_\theta(s)=ns-s^2+(2-\theta)\left\lfloor\frac{s^2}{4}\right\rfloor.
\]
The exact minimum variance is
\[
V_*(n,\mu)=4\kappa^2\bigl[n(n-1)-M_n(\theta)\bigr],
\qquad
M_n(\theta)=
\begin{cases}
\max_{2\le s\le n-1}H_\theta(s),&1<\theta<2,\\
\lfloor n^2/4\rfloor,&\theta\ge2.
\end{cases}
\]
**Every** minimizing partition belongs to exactly the following families, up to interchanging the shores and permuting the three unlabeled classes.

1. **Mixed regime \(1<\theta<2\).** Choose any integer \(s\in\{2,\ldots,n-1\}\) maximizing \(H_\theta\). Take \(a=\lfloor s/2\rfloor\) vertices from \(A\) and \(b=\lceil s/2\rceil\) from \(B\), or interchange \(a,b\); put these \(a+b\) vertices in one mixed class, and put the unchosen vertices of \(A\) and of \(B\) in two separate pure classes. The mixed class is mandatory at every optimum. The maximizing \(s\) is unique except at exact tie parameters, when precisely two consecutive values can maximize. In particular, with \(\Delta_s=H_\theta(s+1)-H_\theta(s)\),
\[
\Delta_s=n-2s-1+(2-\theta)\left\lfloor\frac{s+1}{2}\right\rfloor,
\]
and these differences decrease strictly with \(s\); this gives all finite-size internal staircase thresholds and ties.
2. **Transition \(\theta=2\).** Choose \(s\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) and *any* nonnegative integers \(a,b\) with \(a+b=s\). Put \(a\) vertices of \(A\) and \(b\) vertices of \(B\) in one class, and the remaining vertices of each shore in its own class. Both proper and improper colorings are optimal; no other types are.
3. **Pure regime \(\theta>2\).** Keep one entire shore in one class, and split the other shore into two nonempty classes with sizes \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\). Every optimum is proper; no mixed class is optimal.

The sharp threshold separating the mandatory-mixed and all-proper regimes is therefore
\[
\boxed{\mu_c=n(\sqrt2-1).}
\]
For \(n\ge3\), the complete set of optima changes from necessarily improper for \(0<\mu<\mu_c\), to coexistence of improper and proper at \(\mu=\mu_c\), to exclusively proper for \(\mu>\mu_c\). This transition is exact for every finite \(n\), not merely asymptotic.

The number of optimal unlabeled partitions can also be recovered without enumeration. In the mixed regime it is
\[
\sum_{s\in\arg\max H_\theta}\quad
\sum_{\substack{a+b=s\\a,b\ge1\\ab=\lfloor s^2/4\rfloor}}
\binom na\binom nb.
\]
In the pure regime it equals \(\binom{n}{n/2}\) if \(n\) is even, and \(2\binom n{(n-1)/2}\) if \(n\) is odd. At \(\theta=2\), add to this pure count all mixed-class choices \(\sum_{s\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}}\sum_{a=1}^{s-1}\binom na\binom n{s-a}\), counting each distinct \(s\) once. For example, \(K_{3,3}\) has nine optimal partitions in the mixed regime, fifteen at the threshold, and six in the pure regime.

## Assumptions and scope
The graph has exactly two shores each of size \(n\ge3\), all cross edges are unit-conductance, the graph Laplacian is the unnormalized combinatorial one, and \(\mu>0\). Each of the three probes has independent uniform signs on its own support and zero entries elsewhere, and probes are independent across supports. One exact quadratic form is evaluated per nonempty class, with no division of the sum by three. Thus the estimator is unbiased and uses exactly three matrix-vector actions regardless of the partition. The result minimizes *variance at a fixed three-action budget*, not solver runtime, tail probabilities, or variance under correlated or repeated probes.

## Proof
**Resolvent and variance normalization.** With \(J\) the \(n\)-by-\(n\) all-ones matrix,
\[
\mu I+L_H=\begin{pmatrix}(\mu+n)I&-J\\-J&(\mu+n)I\end{pmatrix}.
\]
Direct multiplication verifies that its inverse has diagonal blocks \((\mu+n)^{-1}I+\kappa J\) and off-diagonal blocks \(\chi J\), where \(\chi=1/[\mu(\mu+2n)]\). Hence the off-diagonal Green entry is \(\kappa\) for distinct same-shore vertices and \(\chi\) for cross-shore vertices, with \(\chi^2/\kappa^2=\theta>1\). For a symmetric matrix and one class-supported Rademacher quadratic form, independent signs give variance \(4\) times the sum of squared matrix entries over unordered pairs within the class: the only surviving terms in the centered fourth moment have the same unordered pair. Independence across classes adds their variances. Dividing the total variance by \(4\kappa^2\), each same-shore collision has cost \(1\) and each cross-shore collision has cost \(\theta\). For a class containing \(a_i\) and \(b_i\) vertices from the two shores, the cost is
\[
C=\sum_{i=1}^3\left[\binom{a_i}{2}+\binom{b_i}{2}+\theta a_i b_i\right].
\]

**Strict uncrossing.** Let \(u_i=a_i+b_i\) and \(d_i=a_i-b_i\). A summand in \(4C\) equals \((1+\theta)u_i^2+(1-\theta)d_i^2-2u_i\). Suppose two distinct classes contain vertices from both shores. Order those two classes so that \(d_i\ge d_j\). Exchange one \(B\)-vertex in class \(i\) with one \(A\)-vertex in class \(j\). This preserves both class sizes, while changing \((d_i,d_j)\) to \((d_i+2,d_j-2)\). Their squared-imbalance sum increases by \(4(d_i-d_j)+8>0\). Since \(1-\theta<0\), the cost strictly falls. Thus at most one optimal class is mixed.

If exactly one class is mixed but the two other pure classes lie on the same shore, say \(A\), then the mixed class contains all \(n\) vertices of \(B\) and \(a\ge1\) vertices of \(A\). Transfer those \(a\) vertices to the smaller pure \(A\)-class of size \(p\). This increases the same-shore collision cost by \(ap\) but removes \(\theta an\) in cross-shore collisions. As \(p<n<\theta n\), it is a strict improvement, contradicting optimality. Thus every optimizer has two pure classes from opposite shores and a third class containing \(a\) vertices of \(A\) and \(b\) vertices of \(B\), allowing one of \(a,b\) to vanish for the pure case. This structural conclusion applies without any assumption of balanced class sizes.

**Two-integer reduction.** Relative to the base partition with one class on each whole shore, whose normalized cost is \(n(n-1)\), the third-class construction decreases the cost by
\[
D(a,b)=a(n-a)+b(n-b)-\theta ab
=n(a+b)-(a+b)^2+(2-\theta)ab.
\]
Write \(s=a+b\). If \(1<\theta<2\), for fixed \(s\) the gain is strictly increasing in \(ab\), so \(a,b\) must differ by at most one, with \(ab=\lfloor s^2/4\rfloor\). The gain becomes \(H_\theta(s)\). It is enough to consider \(2\le s\le n-1\): for \(s\ge n\), the differences \(H_\theta(s+1)-H_\theta(s)\) are negative and \(H_\theta(n)=(2-\theta)\lfloor n^2/4\rfloor<\lfloor n^2/4\rfloor\); for \(s=0,1\), the gain cannot beat \(\lfloor n^2/4\rfloor\). Yet choosing \(s\) nearest to \(n/2\), with \(s\ge2\), and both \(a,b>0\) gives \(D(a,b)>\lfloor n^2/4\rfloor\). Such a choice exists for each \(n\ge3\), taking \(s=2\) when \(n=3\). Therefore an optimizer lies in the displayed range and is necessarily mixed. The exact successive difference formula follows from \(\lfloor(s+1)^2/4\rfloor-\lfloor s^2/4\rfloor=\lfloor(s+1)/2\rfloor\). Since \(0<2-\theta<1\), the successive differences strictly decrease, implying at most two consecutive maximizing \(s\)-values.

If \(\theta>2\), for all \(a,b\ge0\),
\[
D(a,b)=ns-s^2-(\theta-2)ab\le \left\lfloor\frac{n^2}{4}\right\rfloor,
\]
with equality precisely when \(ab=0\) and \(s\) is an integer nearest \(n/2\). These choices are feasible and give exactly the pure balanced-split partitions. If \(\theta=2\), the \(ab\)-penalty vanishes, so equality holds for all feasible \(a+b\) nearest \(n/2\), yielding the mixed/pure tie family. The identity \(\theta=(1+\mu/n)^2\) makes the unique transition \(\mu_c=n(\sqrt2-1)\). All claims, including equality cases and the optimizer counts, follow.

## Verification
The accompanying `verify.py` uses only Python 3 standard library fractions and enumerates every unlabeled three-class partition for \(n=3,4,5,6\) at nine exact rational values of \(\theta\), verifying both minimum costs and counts of *all* optimal partitions. It separately inverts the entire rational shifted graph Laplacian for \(n=3,4,5\) at three exact rational screenings and checks the proposed Green entries and every partition's matrix-based variance. It also checks the discrete gain identities and strict concavity for \(3\le n\le29\). The recorded test result in `VERIFY_OUTPUT.txt` contains 35,610 passed assertions. None of these finite computations is substituted for the general proof above.

## Relationship to prior work
Stathopoulos, Laeuchli and Orginos (2013), arXiv:1302.4018v1, develop distance-based/hierarchical probing for trace estimation on lattices and discuss the tradeoff between coloring and solve cost. The later general analysis of Frommer, Rinelli and Schweitzer (2023), arXiv:2308.07722v1, especially Theorem 3.3 and Lemma 3.5, gives the per-partition Rademacher variance identity, which is used here as an established fact. Neither inspected statement solves the unrestricted three-class partition optimum on a balanced complete bipartite screened resolvent. A separate published result, *Sharp two-color stochastic-probing transition on complete bipartite resolvents* (published-finding corpus record `2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895`), explicitly treats **exactly two** nonempty classes for general \(K_{m,n}\). Its formula does not determine the optimum for **exactly three** classes: indeed, on \(K_{n,n}\) its two-class optimum is the proper bipartition for all positive shifts, whereas the present three-class optimum is necessarily improper in the entire weak-screening regime. The new claim concerns this sharp shift-induced reversal at a fixed three-action budget, including the entire optimizer family and ties. This comparison does not claim absolute publication priority beyond inspected records.

## Limitations
The graph must be unweighted and balanced, have shore sizes \(n\ge3\), and use the positive screened combinatorial Laplacian inverse. The result does not optimize unbalanced bicliques, more than three probes, variable repeats per class, adaptive or dependent signs, nonquadratic trace estimators, runtime, or tail bounds. The novelty assessment is limited to inspected literature and indexed records; a specialized weighted multiway-cut theorem could imply an equivalent answer. No independent mathematical validation has occurred.

## References
1. A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018v1, publicly submitted 17 February 2013, Sections 1–2. https://arxiv.org/abs/1302.4018
2. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1, publicly submitted 15 August 2023, Theorem 3.3 and Lemma 3.5. https://arxiv.org/abs/2308.07722
3. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, published published-finding corpus record `2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895`, full `RESULT.md` statement and proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895
