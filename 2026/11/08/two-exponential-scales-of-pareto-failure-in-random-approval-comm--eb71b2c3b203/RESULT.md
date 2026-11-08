# Two exponential scales of Pareto failure in random approval committees

## Finding
Fix integers \(m\ge2\) and \(1\le k<m\), and let \(r=\min\{k,m-k\}\). For \(n\ge1\), independently sample every entry of an \(n\)-voter, \(m\)-candidate approval matrix from a fair Bernoulli distribution. The utility of voter \(i\) for a size-\(k\) committee \(W\) is \(u_i(W)=|W\cap A_i|\), where \(A_i\) is the voter's approved set. Write \(P_{m,k}(n)\) for the probability that **at least one** size-\(k\) committee is strictly Pareto dominated by another size-\(k\) committee. Set
\[
N_1=m(m-1),\quad N_2=\begin{cases}6\binom m4,&r\ge2,\\0,&r=1,\end{cases}\quad H=\sum_{t=3}^{r}\binom mt\binom{m-t}{t},\quad N=N_1+N_2.
\]
An empty sum equals zero. The following exact, nonasymptotic error bound holds for **all** \(m,k,n\) in this domain:
\[
\boxed{\left|P_{m,k}(n)-N_1\left(\frac34\right)^n-N_2\left(\frac{11}{16}\right)^n\right|\le
N_1\left(\frac12\right)^n+N_2\left(\frac38\right)^n+
\binom N2\left(\frac58\right)^n+H\left(\frac{21}{32}\right)^n.}
\]
Thus, for fixed \(m,k\), the two displayed contributions give the first two distinct exponential scales; the second is present precisely when \(2\le k\le m-2\). In particular, \(P_{m,k}(n)\sim m(m-1)(3/4)^n\).

There is a sharper interpretation of the second scale. Let \(Q_{m,k}(n)\) be the probability that **no candidate's approval column weakly contains another candidate's column** (including equality), but some size-\(k\) committee is Pareto dominated. If \(r\ge2\), then
\[
\boxed{\left|Q_{m,k}(n)-6\binom m4\left(\frac{11}{16}\right)^n\right|
\le N_2\left(\frac38\right)^n+\binom{N_2}{2}\left(\frac{19}{32}\right)^n+N_1N_2\left(\frac58\right)^n+H\left(\frac{21}{32}\right)^n.}
\]
Here weak containment means the two approval columns are ordered by coordinatewise comparison. For \(r=1\), \(Q_{m,k}(n)=0\). Hence the second scale measures genuine multi-candidate Pareto improvements invisible to all one-candidate replacements.

## Assumptions and scope
Candidates and voters are labeled. All \(mn\) approvals are mutually independent fair coin flips. The numbers \(m,k\) are fixed when taking \(n\to\infty\). Pareto domination requires nondecreasing utility for **every** voter and strictly increasing utility for **at least one** voter. The result concerns integral committees and additive approval utilities, not fractional committees or arbitrary correlated electorates.

For disjoint ordered candidate sets \(X,Y\) of cardinality \(t\), define \(E_{X,Y}\) by
\[
E_{X,Y}=\left\{\sum_{y\in Y}a_{iy}\ge\sum_{x\in X}a_{ix}\ \text{for all voters }i\right\},
\]
and \(E^{+}_{X,Y}\) by adding a strict inequality for at least one voter. An ordered \((X,Y)\) can arise as the deletion and addition sets of a size-\(k\) committee pair exactly when \(1\le t\le r\). Consequently, the Pareto-failure event is exactly \(\bigcup_{t=1}^r\bigcup_{|X|=|Y|=t,\,X\cap Y=\varnothing}E^+_{X,Y}\). The number of such ordered comparisons of order \(t\) is \(N_t=\binom mt\binom{m-t}t\).

## Proof
**1. The per-voter exchange probabilities.** For each fixed disjoint \(X,Y\), both sides of the inequality are independent \(\operatorname{Binomial}(t,1/2)\) random variables. By symmetry, the one-voter probability of nonnegative difference is
\[
\rho_t=\frac12+\frac12\Pr\{\operatorname{Bin}(t,1/2)=\operatorname{Bin}'(t,1/2)\}=\frac12+\frac{\binom{2t}t}{2\cdot4^t}.
\]
The central-binomial identity follows from Vandermonde's identity. Therefore \(\Pr(E_{X,Y})=\rho_t^n\), and the probability of equality for *all* voters is \((\binom{2t}t/4^t)^n\). In particular, \(\rho_1=3/4\), \(\rho_2=11/16\), and \(\rho_3=21/32\). Moreover, for \(e_t=\binom{2t}t/4^t\),
\[
\frac{e_{t+1}}{e_t}=\frac{2t+1}{2t+2}<1,
\]
so \(\rho_t\le21/32\) for all \(t\ge3\).

**2. Fixed finite overlap lemma.** For any two distinct ordered exchange events with sizes at most two, their *single-voter* joint probability is at most \(5/8\). Indeed, the support of both comparisons involves at most eight labeled candidate coordinates, and independence allows embedding into eight fair bits. Enumerate all 256 binary rows and all ordered disjoint pairs \((X,Y)\) of sizes 1 and 2. The maximum number of rows satisfying two distinct inequalities, classified by their respective sizes, is **160, 160 and 152** for \((1,1)\), \((1,2)\), and \((2,2)\), respectively. This is a complete exhaustive check of the fixed lemma, not a large-\(n\) experiment: the 56 one-set and 420 two-set comparisons and all their distinct pairs are enumerated in the included `verify_pareto_rates.py`. In particular the size-2-versus-size-2 joint probability is at most \(152/256=19/32\). For \(n\) independent voters the respective intersections have probabilities bounded by the \(n\)th powers of those values.

**3. First two exponential fronts.** Let \(L\) be the union of the non-strict events of sizes one and two. The elementary two-term Bonferroni bounds imply
\[
\left|\Pr(L)-N_1\rho_1^n-N_2\rho_2^n\right|\le \binom{N_1+N_2}{2}\left(\frac58\right)^n.
\]
The union of strict events of these orders is contained in \(L\); the difference is bounded by the total probabilities of the all-voter equalities, \(N_1(1/2)^n+N_2(3/8)^n\). Exchanges of orders \(t\ge3\) contribute at most \(H(21/32)^n\) by the union bound. Combining these three bounds proves the first displayed estimate. Since \(21/32<11/16<3/4\) and \(5/8<11/16\), the coefficients of the two leading exponentials are exact.

**4. No-local-containment (second-front) law.** The absence of all ordered single-candidate weak containments is exactly the complement of the union of all non-strict \(t=1\) events. On this complement, a Pareto failure must have an exchange of size at least two. The union of all \(t=2\) non-strict events has probability \(N_2(11/16)^n\) up to a pairwise overlap error of \(\binom{N_2}{2}(19/32)^n\). Removing all-voter ties costs at most \(N_2(3/8)^n\). Intersections with any \(t=1\) event cost at most \(N_1N_2(5/8)^n\). Orders at least three cost at most \(H(21/32)^n\). Their sum proves the second estimate. If \(r=1\), only single-candidate exchanges are possible and the exceptional event is empty.

**5. Genuine nonlocal witness.** With five voters and four candidates, take the four candidate-approval columns, written as voter-bit masks with the first voter in the least significant bit, to be \((3,5,10,28)\). All four columns are pairwise incomparable under containment. At committee size two, \(W=\{1,2\}\) gives utilities \((1,1,1,1,0)\), while \(W'=\{0,3\}\) gives \((1,1,1,1,1)\). Thus a size-two exchange is strictly Pareto improving even though no one-candidate swap weakly improves every voter.

## Verification
Run `python3 verify_pareto_rates.py` using Python 3 standard library only. The program checks all candidate-event pairs of orders at most two on eight labeled bits, independently compares the direct committee-Pareto definition to the oriented-exchange description on 14,336 finite approval profiles, tests the displayed finite-\(n\) error envelope with exact rational arithmetic, and checks the five-voter nonlocal witness. It prints `ALL EXACT CHECKS PASSED` on success. The eight-bit computation is an exhaustive certificate for the fixed overlap lemma, not a finite-data surrogate for the quantified result; the all-\(n\) conclusion is derived by probability identities and Bonferroni/union bounds.

## Relationship to prior work
Schünke (2026) investigates the structure, committee monotonicity and reconfiguration of Pareto-optimal approval committees, and introduces a *Single Dominance Only* (SDO) characterization for particular restricted profile domains. The present theorem instead quantifies how often one-candidate domination versus genuinely multi-candidate domination occurs in the unrestricted independent fair-coin model, with explicit decay exponents and a finite error. Becker, Boehmer, Frank and Glessen (2026) investigate fractional Pareto optimality, a strictly stronger axiom, and characterize its structural properties; no fractional dominance is considered here. Aziz, Lang and Monnot's committee-testing work addresses decision complexity rather than this probabilistic event. These distinctions do not constitute a claim of exhaustive literature coverage.

## Limitations
The approval probability is exactly \(1/2\), approvals are independent over voter-candidate cells, and the asymptotics hold only for fixed \(m,k\). For finite small \(n\) the explicit error may be numerically loose. The result does not show that *a particular committee-selection rule* is efficient, does not establish connectedness for every approval profile, and does not classify fractional Pareto efficiency. The finite overlap enumeration is small and exactly reproducible but is a computer-assisted lemma rather than a handwritten case table. Previously unindexed equivalent probability calculations remain an originality risk.

## References
1. Joshua Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490v1, first publicly posted May 28, 2026, https://arxiv.org/abs/2605.30490.
2. Patrick Becker, Niclas Boehmer, Fabian Frank, Lara Glessen, *Fractional Pareto-Optimality in Multiwinner Voting*, arXiv:2606.11160, first publicly posted June 9, 2026, https://arxiv.org/abs/2606.11160.
3. Haris Aziz, Jérôme Lang and Jérôme Monnot, *Computing and Testing Pareto Optimal Committees*, arXiv:1803.06644, March 2018, https://arxiv.org/abs/1803.06644.
