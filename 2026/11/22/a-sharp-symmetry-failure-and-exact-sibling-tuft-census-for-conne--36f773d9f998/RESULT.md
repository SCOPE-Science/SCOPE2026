# A sharp symmetry failure and exact sibling–tuft census for connected threshold graphs

## Finding
For each connected unlabeled threshold graph \(G\) of order \(n\ge2\), let \(s(G)\) be the largest number of *other* vertices sharing the closed neighborhood of a vertex, and let \(t(G)\) be the largest number of degree-one neighbors of one vertex. For nonnegative integers \(p,q\), write
\[
C_{p,q}(z)=\sum_{n\ge2}z^n\#\{G:\lvert V(G)\rvert=n,\ s(G)\le p,\ t(G)\le q\}.
\]
Define the finite polynomials \(B_m(z)=\sum_{j=1}^{m}z^j\) and \(D_m(z)=\sum_{j=2}^{m}z^j\), with empty sums equal to zero, and put
\[
\begin{aligned}
U_p&=zB_p+\frac{z^2B_{p+1}}{1-z},
&V_p&=\frac{zB_{p+1}}{1-z},\\
W_{p,q}&=zB_q+\frac{zD_{p+1}}{1-z},
&R_{p,q}&=\mathbf 1_{p\ge1,\,q\ge1}z^2+zD_p+zD_q+\frac{z^2D_{p+1}}{1-z}.
\end{aligned}
\]
Then the **complete joint cumulative enumerator** is the following rational function for every \(p,q\ge0\):
\[
\boxed{C_{p,q}(z)=R_{p,q}(z)+\frac{U_p(z)W_{p,q}(z)}{1-V_p(z)}.}
\]
The exact distribution at \((s,t)=(p,q)\) is recovered by the mixed difference \(C_{p,q}-C_{p-1,q}-C_{p,q-1}+C_{p-1,q-1}\), with negative subscripts interpreted as zero.

The symmetry of the sibling and tuft statistics on **all** connected unlabeled graphs does not survive restriction to connected threshold graphs. The smallest asymmetric order is exactly four: the joint enumerator at that order is
\[
\boxed{P_4(u,v)=u^3+u+uv+v^3.}
\]
More strongly, if \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) are Fibonacci numbers, for every \(n\ge3\) the number of connected unlabeled threshold graphs with no siblings is \(F_{n-2}\), whereas the number with no leaves is \(2^{n-3}\). Thus the marginal symmetry defect is exactly
\[
\boxed{2^{n-3}-F_{n-2}>0\quad(n\ge4),}
\]
and the number of leafless graphs exceeds the number of siblingless graphs by an exponentially growing amount. In particular, no connected threshold graph with \(n\ge3\) has both statistics zero.

## Assumptions and scope
All graphs are finite, simple, connected, and counted **up to isomorphism**, not by vertex labelings. A threshold graph is obtained by starting from one vertex and repeatedly adding an isolated or universal vertex. The standard unique canonical creation word of a connected threshold graph of order \(n\ge2\) starts with \(0\), ends with \(1\), and records these two operations. It has a unique decomposition
\[
0^{a_1}1^{b_1}\cdots0^{a_r}1^{b_r},\qquad r\ge1,\quad a_i,b_i\ge1.
\]
The convention at \(n=2\) is included: \(K_2\) has \(s=t=1\). For a series \(C_{p,q}\), \(z\) marks the number of vertices; \(p,q\) are fixed nonnegative integer bounds. None of the claims concerns labelled graph counts or independent events in a random labelled graph.

## Proof
**Step 1: evaluate the two parameters from the canonical word.** Each maximal consecutive \(1\)-block forms a true-twin class, since all its vertices have identical closed neighborhoods. Different \(1\)-blocks are separated by a \(0\)-vertex which distinguishes them. All vertices of a \(0\)-block are pairwise nonadjacent, so no two of them are true twins. A \(0\)-vertex is in a true-twin class with a \(1\)-block only in the exceptional first block \(a_1=1\), where the initial vertex and the first \(b_1\) universal vertices share their closed neighborhood. Consequently,
\[
\boxed{s(G)=\max\bigl\{b_1-1+\mathbf1_{a_1=1},\ b_2-1,\ldots,b_r-1\bigr\}.}
\]
Each vertex in the final \(0\)-block has exactly \(b_r\) neighbors. Each vertex in an earlier \(0\)-block has at least one additional universal neighbor. A \(1\)-vertex has degree at least two except in \(K_2\), where both vertices have degree one and the same answer follows. Hence
\[
\boxed{t(G)=\begin{cases}a_r,&b_r=1,\\0,&b_r\ge2.\end{cases}}
\]
This is also an exact characterization of which graphs have positive tuft number.

**Step 2: enumerate one or several alternating blocks.** For \(s(G)\le p\), the first alternating block \(0^{a_1}1^{b_1}\) can have \(a_1=1\) and \(1\le b_1\le p\), or \(a_1\ge2\) and \(1\le b_1\le p+1\). Its series is \(U_p\). Every internal alternating block has \(a\ge1\) and \(1\le b\le p+1\), so its series is \(V_p\). A final block (when at least two blocks are present) has \(b=1\) and \(1\le a\le q\), or \(2\le b\le p+1\) and unrestricted \(a\ge1\), giving \(W_{p,q}\).

When there is only one alternating block, the first-block exceptional condition and the last-block tuft condition must both be enforced. Its four disjoint possibilities are \((a,b)=(1,1)\) with \(p,q\ge1\); \(a=1,2\le b\le p\); \(2\le a\le q,b=1\); and \(a\ge2,2\le b\le p+1\). Their combined series is precisely \(R_{p,q}\). For at least two alternating blocks the generating series is \(U_p(1+V_p+V_p^2+\cdots)W_{p,q}\). This proves the rational formula and, by coefficientwise mixed differences, the complete exact joint distribution.

**Step 3: sharp asymmetry.** For \(n\ge3\), a connected canonical word has \(t=0\) exactly when its final two bits are \(11\); its other \(n-3\) free bits give \(2^{n-3}\) graphs. By the sibling formula \(s=0\) exactly when the word begins \(00\), ends \(1\), and contains no adjacent \(1\)'s. The number of these words is \(F_{n-2}\), by the standard two-state Fibonacci recurrence. For orders two and three, the polynomials are respectively \(uv\) and \(u^2+v^2\); at order four, direct application of the word formulas gives \(u^3+u+uv+v^3\), which is asymmetric. For \(n\ge4\), \(F_{n-2}<2^{n-3}\) by the recurrence (or comparison with unrestricted binary strings), and the marginal difference tends to infinity exponentially. Since \(s=0\) forces every \(1\)-block to have length one, the last block also has length one, so \(t\ge1\). This establishes the final structural assertion.

## Verification
The companion `verification.py` contains an independent direct graph construction and a second, run-based computation of \((s,t)\). It enumerates every connected canonical word of orders \(2\) through \(12\), checks that the words give distinct degree multisets, recomputes the two statistics directly from adjacency, and checks every cumulative coefficient \([z^n]C_{p,q}(z)\) for \(0\le p,q\le6\). The recorded replay produced `CUMULATIVE_COMPARISONS 539` and `VERIFY_OK`. The proof above, not this finite verification, establishes the all-order formula.

## Relationship to prior work
Fürnsinn, Gangl and Rubey proved that the sibling number and tuft number have symmetric joint distribution over all connected unlabeled simple graphs and also over the connected chordal subclass. The present theorem addresses the **different**, stricter class of connected threshold graphs (which are chordal), where the equality fails: a symmetry of a superset's distribution does not imply a symmetry of the restricted distribution. Their paper develops an enumerative species proof and notes that finding a bijection remains open; it does not give the threshold-graph joint law. Banerjee and Mehatari describe the canonical threshold creation words and their uniqueness; this well-known representation is used here, not claimed as new. The contribution here is the joint cumulative rational enumeration and the exact sharp symmetry defect, not the underlying word encoding or the global equidistribution.

## Limitations
This result does not refute the global connected-graph or chordal-graph symmetry. It does not construct a bijection for those families. It concerns unlabeled connected threshold graphs only. The rational series formula is parameter-wise (for fixed finite integer bounds) and is not an assertion of a single rational series in all four marker variables. No independent mathematical audit has been performed. Historical priority may be affected by unindexed graph-statistic or threshold-word enumeration results; no claim is made that a literature search proves uniqueness of the theorem.

## References
1. F. Fürnsinn, M. Gangl and M. Rubey, *Unexpectedly, a Symmetry on Unlabeled Graphs*, arXiv:2505.03665 (first public version 2025-05-06); *Electronic Journal of Combinatorics* 33(4), P4.32 (2026), https://arxiv.org/abs/2505.03665 and https://doi.org/10.37236/15312.
2. A. Banerjee and R. Mehatari, *On the normalized spectrum of threshold graphs*, arXiv:1610.08816 (2016), https://arxiv.org/abs/1610.08816. See the introduction for canonical binary strings and run decomposition.
3. I. Sciriha and S. Farrugia, *On the Spectrum of Threshold Graphs*, *International Scholarly Research Notices* (2012), article 108509, https://doi.org/10.5402/2011/108509, for structural background on nested split/threshold graphs.
