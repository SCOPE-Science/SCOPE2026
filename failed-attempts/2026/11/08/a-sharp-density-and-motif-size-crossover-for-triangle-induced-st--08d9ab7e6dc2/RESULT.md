# A sharp density and motif-size crossover for triangle–induced-star covariance

## Finding
Let \(G\sim G(n,p)\) be the independent-edge random graph. Let \(T\) count unordered triangles and let \(S_r\) count induced copies of \(K_{1,r}\), each counted once by its \(r+1\) vertex set. For all integers \(r\ge3\), \(n\ge r+1\), and \(0<p<1\), put \(q=1-p\). Then
\[
\operatorname{Cov}(T,S_r)=\binom n3 p^{r+2}q^{\binom r2}\left[3\binom{n-3}{r-1}(2-(r+1)p)-(r+1)\binom{n-3}{r-2}p\right].
\]
The binomial coefficient is zero if its lower index exceeds its nonnegative upper index. If \(n=r+1\), the covariance is strictly negative. If \(n\ge r+2\), it has exactly one zero in \((0,1)\), at
\[
p_*(n,r)=\frac{6(n-r-1)}{(r+1)(3n-2r-4)},
\]
and is positive below and negative above this value. For fixed \(r\ge3\), the threshold is strictly increasing in \(n\) and converges to \(2/(r+1)\). For fixed \(n\), it is strictly decreasing as \(r\) ranges through \(3\le r\le n-2\). If \(r/n\to\rho\in(0,1)\), then \(rp_*(n,r)\to6(1-\rho)/(3-2\rho)\). At the smallest nontrivial graph order \(n=r+2\), the exact threshold is \(6/((r+1)(r+2))\).

## Assumptions and scope
There are no loops or multiple edges; each unordered potential edge is present independently with probability \(p\). An induced star requires exactly the \(r\) center-to-leaf edges and the absence of all \(\binom r2\) leaf-to-leaf edges within its selected vertex set. For \(r\ge3\), an induced star has one center. The count \(T\) does not require absence of any edges outside its triangle. All expectations use the unconditioned independent-edge distribution, not a fixed-edge model. The limits hold along integer sequences satisfying the stated constraints.

## Proof
Fix a triangle vertex set \(U\), and let \(I_U\) be its triangle indicator. For a star vertex set \(W\) and its designated center \(c\in W\), let \(J_{W,c}\) indicate that the induced subgraph on \(W\) is a star with center \(c\). For \(r\ge3\), the events \(J_{W,c}\) are pairwise disjoint as \(c\) varies, and \(S_r=\sum_W\sum_{c\in W}J_{W,c}\). Write \(b=\binom r2\), so \(\mathbb E[I_U]=p^3\) and \(\mathbb E[J_{W,c}]=p^rq^b\).

If \(|U\cap W|\le1\), the edge sets defining the two indicators are disjoint and their covariance vanishes. If \(|U\cap W|=2\), precisely one triangle edge is internal to \(W\). For the two possible centers among the shared vertices, that edge must be present, and the joint event has probability \(p^2\mathbb E[J_{W,c}]\). For each of the other \(r-1\) centers, the shared edge is forbidden, so the joint event has probability zero. Subtracting \(p^3\mathbb E[J_{W,c}]\) and summing over centers gives \(p^{r+2}q^b(2-(r+1)p)\). If \(|U\cap W|=3\), all three triangle edges lie within \(W\), while an induced star contains no triangle; hence the center-summed covariance is \(-(r+1)p^{r+3}q^b\).

There are \(3\binom{n-3}{r-1}\) choices of \(W\) sharing precisely two vertices with the fixed triangle, and \(\binom{n-3}{r-2}\) choices sharing all three. Summing over the \(\binom n3\) possible triangle sets proves the displayed covariance formula for every allowed \(n,r,p\).

For \(n=r+1\), the first binomial coefficient vanishes while the second equals one, making the covariance negative. For \(n\ge r+2\), divide the bracket by the positive \(\binom{n-3}{r-1}\), and use
\[
\frac{\binom{n-3}{r-2}}{\binom{n-3}{r-1}}=\frac{r-1}{n-r-1}.
\]
The bracket is a strictly decreasing affine function of \(p\), positive at zero and negative at one, with the stated unique zero. Its zero is in \((0,1)\) because \(0<6(n-r-1)<(r+1)(3n-2r-4)\) for \(r\ge3\), \(n\ge r+2\).

Write \(a=n-r-1\ge1\). Then \(p_*(n,r)=6a/((r+1)(3a+r-1))\); increasing \(a\) strictly increases this expression for fixed \(r\), with limit \(2/(r+1)\). For fixed \(n\) and real \(r\in[3,n-2]\), the logarithmic derivative of \(p_*\) is
\[
-\frac1{n-r-1}-\frac1{r+1}+\frac2{3n-2r-4}<0,
\]
because \(3n-2r-4>2(n-r-1)\) for \(n>2\). This proves the rank monotonicity. The two asymptotic statements and the exact \(n=r+2\) specialization follow by direct division in the explicit rational threshold.

## Verification
Run `python check_star.py` in Python 3 (standard library only). The script checks the covariance formula against a separately constructed joint-indicator probability sum for all \(3\le n\le10\), \(2\le r<n\), and five rational probabilities. It also exactly enumerates all \(2^{\binom n2}\) labeled graphs for \(3\le n\le6\), \(2\le r<n\), and three rational probabilities, independently accumulating the two means and joint mean. Finally it checks threshold substitution and both strict signs for integers \(3\le n\le79\). The script reports `PASS 3213 exact assertions`. The tests at \(r=2\) are regression checks for an already studied special case, not a new result. The proof, not the finite tests, establishes all infinite claims.

## Relationship to prior work
Overlap decompositions of subgraph-count moments are classical. Schbath–Lacroix–Sagot (2008) use edge-overlap reasoning for coloured-motif count variance, but their motifs are defined by connectedness and vertex colours, not by an exact induced star topology paired with triangle count. Ellis–Ferry (2009/2010) derive variance of a single non-induced subgraph count in sparse independent-edge graphs. Martorana and coauthors (2020) give algorithmic general overlap/Kocay formulas for induced motif moments, including pair covariance machinery. Such formulas can in principle compute any fixed motif pair; they do not state the present closed formula or the uniform strict sign, monotone two-parameter crossover, and joint size-density scaling. The case \(r=2\) and other isolated triangle–motif covariance laws were already known; it is not claimed as new here. The contribution assessed is the all-\(r\ge3\) exact classification and its two-scale consequence, rather than the generic overlap technique.

## Limitations
The result applies only to unconditioned homogeneous \(G(n,p)\) and mixed triangle/induced-star counts. It does not establish a joint limit law or a testing procedure; correlation magnitudes and variances are not claimed. Broad older overlap formulas may imply the covariance after specialization. The exact all-size sign analysis appears unstated in the inspected material, but comprehensive historical priority is not established, and a general method yielding it with a few substitutions remains a substantive originality risk.

## References
- S. Schbath, V. Lacroix, M.-F. Sagot, “Assessing the Exceptionality of Coloured Motifs in Networks,” published 26 October 2008, https://doi.org/10.1155/2009/616234 .
- R. B. Ellis and G. Ferry, “Variance of the subgraph count for sparse Erdős–Rényi graphs,” *Discrete Applied Mathematics* (2010), https://doi.org/10.1016/j.dam.2009.11.012 ; available manuscript https://math.iit.edu/~rellis/papers/12variance.pdf .
- R. Martorana et al., “Establish the expected number of induced motifs on unlabeled graphs through analytical models,” *Applied Network Science* (2020), https://doi.org/10.1007/s41109-020-00294-y .
