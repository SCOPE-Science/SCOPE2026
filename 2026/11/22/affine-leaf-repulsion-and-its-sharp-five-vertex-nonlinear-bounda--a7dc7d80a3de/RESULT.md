# Affine leaf repulsion and its sharp five-vertex nonlinear boundary

## Finding

**Theorem (complete finite leaf-survival law and first sign reversal).** Start with the edge joining vertices \(0\) and \(1\). At each size \(t\ge2\), vertex \(t\) arrives and joins an existing vertex chosen with probability proportional to \(f(k)\), where \(k\) is its ordinary undirected degree. There are two conclusions.

**Affine case.** If \(f(k)=ck+d\), where \(c\ge0\) and \(w=c+d>0\), then the entire vector of indicators that **distinct** vertices are leaves at **arbitrary individually chosen finite observation sizes** is negatively associated. In fact, for distinct monitored vertices \(i\) with chosen observation sizes \(H_i\) at least their birth sizes, put
\[
b_i=\begin{cases}2,&i=0,1,\\i+1,&i\ge2,\end{cases}
\qquad W_t=2c(t-1)+dt,\qquad
m_t=\#\{i:b_i\le t<H_i\}.
\]
For a finite monitored set \(S\), the exact joint survival probability is
\[
\Pr\{i\text{ is a leaf at size }H_i\text{ for all }i\in S\}
=\prod_{t=2}^{\max_i H_i-1}\left(1-\frac{w m_t}{W_t}\right).
\]
The empty product is one. These probabilities determine the entire finite-dimensional Boolean law by inclusion-exclusion. For a sum \(X\) of \(r\ge1\) such indicators and every \(u\ge0\),
\[
\Pr\{|X-\mathbb EX|\ge u\}\le2\exp(-2u^2/r).
\]

**Sharp first nonlinear breakdown.** For **every** strictly positive degree kernel \(f\), all distinct leaf-indicator covariances through size four are nonpositive. Size five is the earliest at which positive covariance can occur. Indeed, fix \(f(1)=f(2)=1\), \(f(3)=g>0\) (arbitrary positive continuation at higher degrees). At size five, the indicators for vertices \(2\) and \(3\) have covariance
\[
\operatorname{Cov}(L_2,L_3)
=\frac{g^2-8g-41}{72(g+3)^2}.
\]
This covariance is positive **exactly** when \(g>4+\sqrt{57}\), is zero at equality and is negative below it. In that family, all other potentially positive pairs have the same sign boundary: pairs \((0,3)\) and \((1,3)\) have half the displayed covariance, while all pairs not containing vertex \(3\) are strictly negatively correlated, apart from the deterministic newest leaf.

## Assumptions and scope

The process is a growing **undirected** tree, with one edge and two degree-one vertices initially; parent weights are normalized anew at each step. The affine condition \(c\ge0,\ c+d>0\) ensures that all positive-integer-degree weights are strictly positive and the normalizers are deterministic. The leaf observation sizes \(H_i\) are deterministic integers; each distinct vertex occurs at most once in the monitored vector. No assertion of negative association is made for repeated observations of the same vertex, nor for arbitrary nonlinear weights.

The first-public initiating source is Hartle and Krapivsky's study of preferential-attachment leaf statistics, publicly available on **2026-02-01**. The theorem here concerns the finite **labeled vertex leaf-status law**, not the limiting empirical degree/leafdegree distribution studied there.

## Proof

**1. Deterministic normalization and a hidden independent occupancy process.** At size \(t\), the sum of all ordinary degrees is \(2(t-1)\), hence the total affine attachment weight is
\[
W_t=2c(t-1)+dt.
\]
Each current leaf has ordinary degree one and weight \(w=c+d\). Construct independent categorical variables \(J_t\), one for each \(t\ge2\), with
\[
\Pr(J_t=i)=w/W_t\quad(0\le i<t),\qquad
\Pr(J_t=*)=c(t-2)/W_t.
\]
These define genuine probabilities since \(W_t-tw=c(t-2)\ge0\). Start with leaf set \(\{0,1\}\). At step \(t\), erase \(J_t\) from the leaf set if it is a currently present leaf, then insert the new vertex \(t\). Choosing a particular current leaf has probability \(w/W_t\), exactly as in the original attachment tree. The probability of choosing no current leaf is correspondingly \(1-|\mathcal L_t|w/W_t\), again the same as in the true process. Thus **the entire leaf-set history**, including all different observation times, has the same law as this independently driven construction. In particular, vertex \(i\) remains a leaf at time \(H_i\) precisely when no \(J_t=i\) occurs for \(b_i\le t<H_i\). Independence across \(t\) yields the displayed joint-survival product.

For any prescribed zero-one outcomes on the monitored vertices, use inclusion-exclusion over the vertices required to have outcome zero. This obtains the exact joint probability from the all-one probabilities and establishes completeness of the finite law.

**2. Negative association, proved from elementary one-hot facts.** A finite zero-one vector with at most one nonzero coordinate is negatively associated: for disjoint coordinate sets \(A,B\), an increasing function restricted to the one-hot support is a constant plus nonnegative multiples of the single-coordinate indicators, so the covariance of two such functions equals a negative product of nonnegative sums. Independence preserves negative association when families are concatenated (condition on one family and apply the inequality successively). Coordinatewise nondecreasing functions of disjoint coordinate blocks preserve it; if **all** functions are nonincreasing, the same statement follows by negating both test functions. Applying these closure properties to
\[
Y_{t,i}=\mathbf1\{J_t=i\},\qquad
L_i=\mathbf1\Big\{\sum_{t=b_i}^{H_i-1}Y_{t,i}=0\Big\}
\]
proves negative association of every finite collection \((L_i)_{i\in S}\). The coordinate blocks indexed by distinct \(i\) are disjoint, even when observation intervals overlap in calendar time. Each \(Y_{t,\cdot}\) is one-hot (possibly all zero), and different \(t\) are independent.

In particular, for two monitored vertices with overlapping active intervals, the ratio of their joint leaf probability to the product of marginal probabilities is
\[
\prod_{t\text{ in the overlap}}
\frac{1-2w/W_t}{(1-w/W_t)^2}<1.
\]
The inequality is strict whenever the overlap is nonempty (and equality holds when the active intervals are disjoint). For the concentration inequality, negative association bounds the moment generating function of \(X\), for either sign of its argument, by that of independent Bernoulli variables with the same marginal means. Applying the bounded-Bernoulli exponential-moment bound and optimizing the exponent gives the displayed two-sided Hoeffding estimate.

**3. Universal nonpositivity through four vertices.** Rescale any positive kernel so that \(f(1)=1\), and write \(b=f(2)>0\). At size three, exactly one of the two seed vertices is still a leaf; the new vertex is a certain leaf. Their only nonzero pair covariance is \(-1/4\). Directly conditioning on the parent of the fourth vertex gives, at size four,
\[
\operatorname{Cov}(L_0,L_1)=-\frac{(b+1)^2}{4(b+2)^2},\qquad
\operatorname{Cov}(L_0,L_2)=\operatorname{Cov}(L_1,L_2)=-\frac1{2(b+2)^2}.
\]
The newest vertex \(3\) is a leaf with probability one, and all its covariances vanish. Thus arbitrary positive higher-degree values of \(f\) cannot yield positive leaf covariance before five vertices.

**4. Exact five-vertex calculation.** Now choose \(f(1)=f(2)=1\) and \(f(3)=g>0\). When vertex \(3\) arrives, each of the three existing vertices is equally likely as its parent. Conditional on that parent being (i) the degree-two center, (ii) the other old leaf, or (iii) vertex \(2\), each with probability \(1/3\), the survival probabilities of vertices \(2\) and \(3\) after vertex \(4\) arrives can be read off from the resulting degree patterns. The resulting exact values are
\[
\Pr(L_2=1)=\frac{7g+17}{12(g+3)},\quad
\Pr(L_3=1)=\frac{5g+13}{6(g+3)},\quad
\Pr(L_2=L_3=1)=\frac{3g+5}{6(g+3)}.
\]
Subtracting the product of the marginals yields \((g^2-8g-41)/(72(g+3)^2)\), whose unique positive zero is \(4+\sqrt{57}\). A similar two-stage conditioning yields the remaining five-vertex pair covariances:
\[
\begin{aligned}
\operatorname{Cov}(L_0,L_1)&=-\frac{(7g+17)^2}{576(g+3)^2},\\
\operatorname{Cov}(L_0,L_2)&=\operatorname{Cov}(L_1,L_2)=-\frac{g^2+46g+145}{288(g+3)^2},\\
\operatorname{Cov}(L_0,L_3)&=\operatorname{Cov}(L_1,L_3)=\frac{g^2-8g-41}{144(g+3)^2}.
\end{aligned}
\]
Again the newest vertex \(4\) is a certain leaf. This proves the claimed complete sign boundary.

## Verification

The standalone `check.py` exactly enumerates degree-vector probabilities over **every parent choice** for sizes up to seven in four affine parameter settings. It verifies all all-leaf probabilities and their pair covariances against the independent-category formula. It also uses symbolic arithmetic to compute and simplify every five-vertex covariance for the nonlinear family and checks the transition across the algebraic threshold. Run `python3 check.py` with Python 3 and SymPy installed; the replayed run returned **1,272 exact assertions passed**. These finite checks support the written identities; the infinite-size negative-association conclusion follows from the preceding analytic argument, not the checker.

## Relationship to prior work

The 2026 Hartle–Krapivsky work characterizes degree/leafdegree empirical statistics of degree-proportional preferential-attachment trees, not the labeled vector of leaf-survival events across arbitrary observation times. Their November 2025 paper treats random recursive trees and leafdegree-driven attachment instead. Bryc, Minda and Sethuraman establish large deviations for **total** leaf counts, not joint survival across labeled vertices. A study of young-age preferential attachment establishes pairwise nonpositive leaf covariances when parental choices have deterministic age-dependent probabilities; it does not cover history-dependent degree weights or arbitrary joint monotone events. Dubhashi and Ranjan prove negative association for independent ball allocations; that generic result is **fully acknowledged**. The new structural step is the exact identification of the **degree-reinforced affine tree leaf process** with an independent allocation system, together with a sharp first-size and weight threshold at which that property can fail outside the affine class.

## Limitations

No negative-association statement is asserted for all nonlinear attachment rules or for multiple observation times assigned to the same vertex. The five-vertex threshold is specific to the natural family with first two degree weights equal; the universal statement concerns **only** the earliest possible tree size. The Hoeffding bound need not be sharp. The finite checker cannot establish claims at arbitrary sizes without the analytic proof. No exhaustive historical-priority guarantee is claimed; a previously unlocated degree-weighted occupancy representation would affect originality.

## References

1. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1, 2026-02-01. https://arxiv.org/html/2602.01021v1
2. H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085v1, 2025-11-06. https://arxiv.org/html/2511.04085v1
3. W. Bryc, D. Minda and S. Sethuraman, *Large deviations for the leaves in some random trees*, arXiv:0809.4741, 2008. https://arxiv.org/abs/0809.4741
4. *Trees grown under young-age preferential attachment*, *Journal of Applied Probability* 57 (2020), 911–927, DOI:10.1017/jpr.2020.49. https://doi.org/10.1017/jpr.2020.49
5. D. Dubhashi and D. Ranjan, *Balls and Bins: A Study in Negative Dependence*, BRICS Report Series 3(25) (1996), DOI:10.7146/brics.v3i25.20006. https://www.brics.dk/RS/96/25/BRICS-RS-96-25.pdf
