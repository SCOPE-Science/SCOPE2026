# Opposite signs of depth–leaf covariance at extremal and interior keys of random binary search trees

## Finding

**Theorem.** Let \(n\ge3\) be an integer, insert the keys \(1,\ldots,n\) in uniformly random order into an initially empty binary search tree, let \(L_n\) be its number of *internal leaves* (vertices with no children), and let \(D_{n,i}\) be the number of edges on the root-to-key-\(i\) path. Define \(C_{n,i}=\operatorname{Cov}(D_{n,i},L_n)\). Then

\[
C_{n,1}=C_{n,n}=\frac{(n+1)(n-2)}{12n(n-1)}>0.
\]

For \(n\ge4\),

\[
C_{n,2}=C_{n,n-1}=-\frac{23n^3-93n^2+130n-48}{72n(n-2)(n-1)}<0.
\]

For \(n\ge5\) and \(3\le i\le n-2\), put

\[
G(t)=-\frac{t^4+2t^3-t^2+10t+6}{18t(t-1)(t+1)(t+2)},\qquad t\ge2.
\]

Then

\[
C_{n,i}=G(i)+G(n+1-i)<0.
\]

The remaining case is \(C_{3,2}=-1/3\). Thus, **for every order at least three, the two extremal keys have strictly positive depth–leaf covariance and every other key has strictly negative covariance**. In particular,

\[
\begin{aligned}
\lim_{n\to\infty}C_{n,1}&=\frac1{12},\\
\lim_{n\to\infty}C_{n,2}&=-\frac{23}{72},\\
\lim_{n\to\infty}C_{n,i_n}&=-\frac19
\quad\text{whenever }i_n/n\to u\in(0,1).
\end{aligned}
\]

For each fixed integer \(i\ge3\), the limiting covariance is \(G(i)-1/18\) as \(n\to\infty\). All limiting statements concern *unscaled covariance*, not correlation or an independence assertion.

## Assumptions and scope

The insertion order is one uniformly random permutation; equivalently, choose independent continuous priorities \(U_1,\ldots,U_n\), and insert key \(i\) at increasing priority. We use uniform \([0,1]\) priorities since monotone transforms preserve order. A leaf means a *present key* with zero children; it does not mean an external null pointer. Every covariance is taken under this single random insertion order. The key rank \(i\) refers to key value, not arrival time. All formulas are exact for the stated finite orders, with no asymptotic approximation required.

## Proof

**1. Two exact random-permutation representations.** For each key rank \(k\), define

\[
B_k={\bf1}\{U_k>U_{k-1}\text{ if }k>1,\quad U_k>U_{k+1}\text{ if }k<n\}.
\]

In the Cartesian minimum-priority tree, a key is a leaf precisely when its priority exceeds the priorities of every existing immediate neighboring key in sorted-key order. Hence \(L_n=\sum_{k=1}^n B_k\) and, for \(n\ge2\),

\[
\mathbb E L_n=2\cdot\frac12+(n-2)\cdot\frac13=\frac{n+1}{3}.
\]

For distinct key ranks \(i,j\), let \(A_{j,i}\) denote that \(U_j\) is the minimum of the consecutive priority block between \(i\) and \(j\), endpoints included. A standard Cartesian-tree ancestor characterization, also immediate by the first inserted key in each key interval, yields

\[
D_{n,i}=\sum_{j\ne i}{\bf1}_{A_{j,i}},\qquad
\Pr(A_{j,i})=\frac1{|i-j|+1}.
\]

Consequently

\[
C_{n,i}=\sum_{j\ne i}\frac{\mathbb E[L_n\mid A_{j,i}]-\mathbb E L_n}{|i-j|+1}.
\tag{1}
\]

**2. Conditional local-maximum lemma, with all boundary terms.** By key reversal it suffices to consider \(j<i\), and write \(m=i-j+1\). Define

\[
\Delta_{n}(j,i)=\mathbb E[L_n\mid A_{j,i}]-\mathbb E L_n.
\]

For all \(n\ge3\), all \(1\le j<i\le n\), and \(m\ge2\), we claim the following exact additive rule:

\[
\Delta_n(j,i)=h_m+\mathbf1_{\{j=1\}}a_m+\mathbf1_{\{j=2\}}b_m
+\mathbf1_{\{i=n-1\}}c_m+\mathbf1_{\{i=n\}}d_m,
\tag{2}
\]

where

\[
\begin{array}{lll}
h_2=0,&h_m=-\dfrac4{3(m+1)(m+2)}&(m\ge3),\\
a_m=-\dfrac13+\dfrac1{(m+1)(m+2)},&&\\
b_m=\dfrac{m-2}{3(m+1)}+\dfrac1{(m+1)(m+2)},&&\\
c_2=-\dfrac1{12},&c_m=-\dfrac1{3(m+2)}&(m\ge3),\\
d_2=\dfrac14,&d_m=\dfrac1{3(m+1)(m+2)}&(m\ge3).
\end{array}
\]

Here \(h_m\) is the contribution in the absence of physical endpoints, while the other four terms separately replace an ordinary local-maximum probability by its endpoint counterpart. This presentation covers short intervals and the three-key tree too.

We verify (2) directly. Conditional on \(A_{j,i}\), the minimum priority \(X=U_j\) has the \(\mathrm{Beta}(1,m)\) law, with \(\mathbb EX=1/(m+1)\) and \(\mathbb EX^2=2/((m+1)(m+2))\). Given \(X=x\), the other \(m-1\) block priorities are independent uniform random variables on \((x,1)\); priorities outside the block remain independent uniform variables on \((0,1)\). Only local maxima in positions \(j-1,j,j+1,i,i+1\) can change their expectations; all remaining triples have the same relative-order law as unconditionally. If \(m\ge3\), provided these five positions are ordinary interior locations, their changes in expected local-maximum indicators, in that order, are

\[
\frac16-\frac1{(m+1)(m+2)},\quad -\frac13,\quad
\frac16,\quad \frac1{6(m+1)},\quad
-\frac1{6(m+1)}-\frac1{3(m+1)(m+2)}.
\]

Their sum is \(h_m\). For \(m=2\), the four affected interior positions \(j-1,j,i,i+1\) instead have changes \(1/12,-1/3,1/3,-1/12\), summing to \(h_2=0\). If \(j=1\), there is no position \(j-1\) and the endpoint \(j\) has baseline probability \(1/2\) rather than \(1/3\); this gives \(a_m\). If \(j=2\), the \(j-1\) position has only one neighbor, giving \(b_m\). The symmetric replacements at \(i=n-1\) and \(i=n\) give \(c_m,d_m\). Each replacement concerns a different local-maximum site, so their corrections add even when two physical ends occur simultaneously. These calculations establish (2) for every allowed interval.

**3. Exact summation.** Substitute (2) into (1), reflecting the key order to handle \(j>i\). One only needs telescoping rational sums, including

\[
\sum_{m=3}^{t}\frac1{m(m+1)(m+2)}
=\frac1{24}-\frac1{2(t+1)(t+2)},\qquad
\sum_{m=3}^{t}\frac1{m(m+2)}=\frac7{24}-\frac1{2(t+1)}-\frac1{2(t+2)}.
\]

For a target key separated from both physical endpoints by at least two ranks, the contribution of ancestors strictly on a given side whose available interval has length \(t\) simplifies to

\[
G(t)=-\frac{t^4+2t^3-t^2+10t+6}{18t(t-1)(t+1)(t+2)}.
\]

Summing the left and right contributions yields \(G(i)+G(n+1-i)\). At a key one rank from an endpoint, the altered adjacent boundary term gives the displayed formula for \(C_{n,2}\) when \(n\ge4\). At the extremal key, summation gives \((n+1)(n-2)/(12n(n-1))\). Direct use of (2) at \(n=3\) gives the remaining covariance \(-1/3\). The independently reproducible exact finite checks below also test every term of (2), not just the final expressions.

**4. Strict signs and limits.** For \(t\ge3\), the numerator \(t^4+2t^3-t^2+10t+6\) is positive, so \(G(t)<0\). For \(n\ge4\), the cubic \(23n^3-93n^2+130n-48\) is positive: it equals \(456\) at \(n=4\), and its derivative \(69n^2-186n+130\) has negative discriminant and positive leading coefficient. The extremal-key expression is positive for every \(n\ge3\); the three-key interior case is negative. Finally \(G(t)\to-1/18\) as \(t\to\infty\), yielding all limiting claims. This completes the proof.

## Verification

The included standard-library-only file `verify.py` can be run with `python3 verify.py`. It independently constructs every BST from every insertion permutation for each size \(3\le n\le8\), computes depths by actual parent-child links and leaves by actual zero-child counts, and compares with the priority-record and local-maximum representations. It also exhaustively checks all conditional interval-minimum expectation identities (2). Exact rational arithmetic checks the analytic covariance formulas and the conditional-sum reconstruction at every key rank for all sizes \(3\le n\le120\), including every sign. Its observed output was:

`VERIFY_OK 423989 exact assertions; exhaustive n<=8; all ranks n<=120`

These finite checks corroborate the algebra; the proof above, not finite enumeration, establishes the claim for all \(n\ge3\).

## Relationship to prior work

Aguech, Amri, and Sulzbach (2017, arXiv:1707.00165) study key-rank depths, weighted depths, and related paths in the same uniform BST model. Their ancestor-event formulation (Section 4.1) supports the depth representation but does not give these mixed depth–leaf covariances or the universal sign split. Devroye (1991) gives the local-maximum/leaf-counter representation and Gaussian leaf fluctuations; his Theorem 2 does not provide the rank-indexed mixed covariance. Desmarais, Holmgren, and Wagner (2021, arXiv:2110.15050) give covariance matrices for counts of differently colored leaves in preferential-attachment trees, including binary search trees, but no fixed-key depth–total-leaf dependence theorem. The present theorem concerns the interaction between a single query's search depth and global leaf abundance, not the separate marginal results.

## Limitations

The signs are specific to *uniform random insertion order*, an internal-leaf count, and ordinary (unweighted) depths. They need not hold for biased permutations, other tree models, weighted depths, or conditional sampling. This is a covariance theorem only: it does not assert pairwise independence or a joint central limit theorem. Earlier work may contain an equivalent implicit mixed-moment formula; no general claim of priority in all unpublished sources is made.

## References

- R. Aguech, A. Amri and H. Sulzbach, *On weighted depths in random binary search trees*, arXiv:1707.00165v1, first public 2017-07-01. https://arxiv.org/abs/1707.00165
- L. Devroye, *Limit laws for local counters in random binary search trees*, Random Structures & Algorithms **2** (1991), 303–315. https://luc.devroye.org/devroye_1991_limit_law_counter_random_binary_search_tree.pdf
- C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1, first public 2021-10-28. https://arxiv.org/abs/2110.15050
