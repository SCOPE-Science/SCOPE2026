# Two variance peaks in future phylogenetic diversity: a sharp two-block clade threshold

## Finding
Under independent, homogeneous species survival, the variance of rooted future phylogenetic diversity need not be unimodal as the shared extinction probability varies. The simplest two-block competition between the survival of one taxon and that of a clade of \(m\) taxa has two distinct local variance maxima for a suitable choice of positive block lengths if and only if \(m\ge 7\). Moreover, a rooted eight-taxon tree with every edge strictly positive realizes exactly two local variance maxima.

The cutoff concerns the **two-block class** defined below; no minimum across arbitrary rooted phylogenetic trees is asserted.

## Assumptions and scope
Let every taxon survive independently with common probability \(p\in(0,1)\), and write \(q=1-p\). Rooted phylogenetic diversity of the survivor set means the total length of the union of all root-to-surviving-leaf paths (the empty set has diversity zero).

For the two-block model, the root has a pendant edge of length \(a>0\) leading to taxon \(0\), and an edge of length \(b>0\) leading to a clade \(B\) with \(m\ge1\) taxa. The edges below the latter edge have length zero **only in this reduced two-block model**. With independent survival indicators \(X_0,X_1,\ldots,X_m\), the random rooted diversity is
\[
Y=aX_0+b\mathbf{1}\{X_1+\cdots+X_m>0\},
\qquad V_m(q)=\operatorname{Var}(Y)
=a^2q(1-q)+b^2q^m(1-q^m).
\]
A variance peak is a strict local maximum inside \(0<q<1\), equivalently inside \(0<p<1\).

For a strictly positive-edge example, take eight taxa: a root pendant edge of length \(1\) to taxon \(0\), one root edge of length \(4/5\) to a seven-leaf star, and each of the seven star pendant edges of length \(\delta=1/10000\). Every edge has positive length.

## Proof
Put \(t=b^2/a^2>0\). A normalized derivative of the two-block variance is
\[
F_{m,t}(q)=1-2q+mtq^{m-1}(1-2q^m).
\]
For \(m=1\), this has its only zero at \(q=1/2\). For \(m\ge2\), \(F_{m,t}(q)>0\) for \(0<q\le1/2\) and \(F_{m,t}(q)<0\) for \(q_m\le q<1\), where \(q_m=2^{-1/m}\). Every critical point therefore occurs in \((1/2,q_m)\), where
\[
F_{m,t}(q)=0\quad\Longleftrightarrow\quad
t=h_m(q):=\frac{2q-1}{mq^{m-1}(1-2q^m)}.
\]
The derivative of \(h_m\) has the sign of
\[
H_m(q)=(m-1)-2(m-2)q-(4m-2)q^m+(8m-8)q^{m+1}.
\]
For \(2\le m\le6\), \(H_m(q)>0\) throughout \([1/2,1]\). One exact certificate expands \(H_m(a+(b-a)s)\) in the degree-\(m+1\) Bernstein basis \(\binom{m+1}{j}s^j(1-s)^{m+1-j}\), for \(s\in[0,1]\). Every coefficient is positive, with the following **minimum coefficient** in each stated interval:

| \(m\) | \(q\)-interval | Smallest Bernstein coefficient |
|---|---|---|
| 2 | \([1/2,1]\) | \(1/2\) |
| 3 | \([1/2,1]\) | \(9/16\) |
| 4 | \([1/2,1]\) | \(2/5\) |
| 5 | \([1/2,1]\) | \(1/8\) |
| 6 | \([1/2,2/3]\) | \(167/2187\) |
| 6 | \([2/3,3/4]\) | \(341/5103\) |
| 6 | \([3/4,1]\) | \(217/512\) |

The exact coefficients and transformation are recomputed by the accompanying standard-library verifier. Consequently \(h_m\) increases from zero to infinity and intersects every \(t>0\) exactly once. Hence the variance has exactly one strict local maximum for all \(1\le m\le6\).

For every \(m\ge7\), the signs of \(H_m\) at \(1/2\), \(7/10\), and \(q_m\) are respectively positive, negative, positive. Indeed,
\[
H_m(1/2)=1-2^{1-m}>0,\quad H_m(q_m)=m(2q_m-1)>0,
\]
\[
5H_m(7/10)=9-2m+(8m-18)(7/10)^m<0.
\]
The last inequality holds at \(m=7\), and for larger integers follows because \((8m-18)(7/10)^m/(2m-9)\) strictly decreases. By Descartes' rule of signs, \(H_m\), whose coefficients in ascending positive degrees have signs \(+,-,-,+\), has at most two positive roots, counted with multiplicity. Thus it has exactly two distinct roots in \((1/2,q_m)\), defining one local maximum and one local minimum of \(h_m\). Choose \(t\) strictly between their values. The equation \(h_m(q)=t\) has exactly three roots, giving two strict local maxima of \(V_m\). This completes the if-and-only-if classification in the two-block model.

Now give every leaf of the seven-taxon clade the strictly positive pendant length \(\delta=1/10000\), while retaining \(a=1\) and \(b=4/5\). Independence and the clade-indicator covariance give
\[
V_\delta(q)=(1+7\delta^2)q(1-q)+\frac{16}{25}q^7(1-q^7)+\frac{56}{5}\delta q^7(1-q).
\]
Its derivative is
\[
V_\delta'(q)=(1+7\delta^2)(1-2q)+\frac{112}{25}q^6(1-2q^7)
+\frac{56}{5}\delta q^6(7-8q).
\]
At \(q=1/2,3/5,7/10,9/10\), these derivative values have exact signs \(+,-,+,-\). Therefore there is a critical point in each of the three disjoint intervening intervals, yielding at least two strict local maxima. The derivative has precisely three sign changes among its nonzero monomial coefficients (in ascending degree: \(+,-,+,-,-\)), so Descartes' rule bounds its number of positive roots by three. Hence there are **exactly** three positive critical points and exactly two strict local maxima for this positive-edge eight-taxon tree.

## Verification
Run `python3 verify_variance.py` using the Python standard library. It recomputes all seven positive Bernstein coefficient bounds exactly using \(`fractions.Fraction`\), checks the all-\(m\) sign lemma and its first 94 integer instances, reconstructs the complete eight-taxon probability distribution by enumerating all \(2^8=256\) survivor subsets, matches its exact variance polynomial to the closed formula, and verifies exact derivative signs and the three-sign-change root bound. No numerical root-finding is needed for the proof.

For orientation only, the positive-edge example has local maxima at approximately \(p=0.4111284\) and \(p=0.1675300\), with an intervening local minimum near \(p=0.3629086\); these decimals are not used as certificates.

## Relationship to prior work
Faller, Pardi and Steel (arXiv:0708.0425, 2 August 2007), in their Lemma 1.1, already give the general exact covariance and variance formula for future rooted phylogenetic diversity under independent extinction. Their Section 2 uses a structurally similar one-taxon-plus-clade tree as an asymptotic normality counterexample. Those foundational formulas and that tree shape are **not** claimed as new. The present claim concerns the exact phase geometry of variance as the **common survival probability varies**, the seven-member clade cutoff in a two-block model, and an explicit all-positive-edge example exhibiting two variance peaks; the inspected sections do not establish those results.

Nipperess and Matsen (arXiv:1208.6552, 31 August 2012; published 2013) give exact mean and variance formulas for phylogenetic diversity under fixed-count rarefaction rather than independent equal-probability extinction. This is a different sampling measure and does not imply the asserted bimodality classification. The risk-curve result follows from additional polynomial and sign analysis, not from the earlier variance formula alone.

## Limitations
The seven-taxon clade cutoff is **not** a universal smallest-leaf theorem for all positively weighted phylogenetic trees. It is a complete classification of the specified two-block model, coupled with a strictly positive eight-tip realization. No claim about real-world extinction-rate calibration, optimal protection, nonindependent losses, or uniqueness of the eight-leaf topology is made. Other unindexed literature may contain related variance-shape results; independent review has not been performed.

## References
1. Faller, B., Pardi, F., and Steel, M. (2007 preprint; 2008 journal). *Distribution of phylogenetic diversity under random extinction*. arXiv:0708.0425 (first public 2007-08-02), https://arxiv.org/abs/0708.0425 ; DOI:10.1016/j.jtbi.2007.11.034.
2. Nipperess, D. A., and Matsen IV, F. A. (2012 preprint; 2013 journal). *The mean and variance of phylogenetic diversity under rarefaction*. arXiv:1208.6552, https://arxiv.org/abs/1208.6552 ; DOI:10.1111/2041-210X.12042.
3. Faith, D. P. (1992). *Conservation evaluation and phylogenetic diversity*. Biological Conservation 61:1–10. DOI:10.1016/0006-3207(92)91201-3.
