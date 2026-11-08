# Sharp isolated-cluster variance ordering in diameter-three site percolation

## Finding
Let \(n\ge4\), and let \(D_{a,b}\) denote the tree whose two adjacent hubs have respectively \(a,b\ge0\) pendant leaves, with \(a+b=n-2\). Thus \(D_{0,n-2}\) is the star, and every tree on \(n\) vertices of diameter at most three is one of these trees. Retain each vertex independently with probability \(1/2\); let \(Z_{a,b}\) count isolated retained vertices in the induced subgraph. Define \(A=2^{-(a+2)}\) and \(B=2^{-(b+2)}\). Then
\[
\operatorname{Var}(Z_{a,b})=\frac{a^2+b^2+2a+2b}{16}
+\left(1+\frac{b-a}{2}\right)A
+\left(1+\frac{a-b}{2}\right)B-(A+B)^2.
\]
For every pair of integers \(1\le a\le b\), writing \(d=b-a\), the outward transfer is quantitatively strict:
\[
\operatorname{Var}(Z_{a-1,b+1})-\operatorname{Var}(Z_{a,b})>\frac{d+1}{8}.
\]
Consequently among all \(n\)-vertex trees of diameter at most three, the unique variance minimizer up to isomorphism is \(D_{\lfloor(n-2)/2\rfloor,\lceil(n-2)/2\rceil}\), and the unique maximizer is the star \(D_{0,n-2}\). Their respective variances are asymptotic to \(n^2/32\) and \(n^2/16\), so the maximal-to-minimal ratio converges to \(2\).

An auxiliary exact distributional identity is available. If \(t\) is an indeterminate and \(g(t)=(1+t)/2\), then the probability generating polynomial is
\[
\mathbb E[t^{Z_{a,b}}]=\frac14\left[g(t)^{a+b}
+g(t)^a\bigl(1-2^{-b}+2^{-b}t\bigr)
+g(t)^b\bigl(1-2^{-a}+2^{-a}t\bigr)+1\right].
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and labelled only to specify independent sampling; results are invariant under isomorphism. The two hubs are adjacent, the \(a\) and \(b\) leaves adjacent to only their respective hub. A hub with zero designated leaves is permitted, so stars are included. Every vertex is retained independently with probability exactly \(1/2\), and an isolated vertex means a *retained* vertex of degree zero in the induced retained subgraph; deleted vertices do not contribute. No claim is made for general trees of diameter greater than three or for other retention probabilities.

## Proof
Let \(X,Y\) be the independent retention indicators of the two hubs, and let \(L_a,L_b\) be independent binomial variables with parameters \((a,1/2)\), \((b,1/2)\), counting retained pendant vertices. The four equally likely hub states give
\[
Z_{a,b}=\begin{cases}
L_a+L_b,&(X,Y)=(0,0),\\
L_a+\mathbf1_{\{L_b=0\}},&(X,Y)=(0,1),\\
L_b+\mathbf1_{\{L_a=0\}},&(X,Y)=(1,0),\\
0,&(X,Y)=(1,1).
\end{cases}
\]
In the second and third cases the two summands are independent. This proves the generating polynomial. Taking moments gives, with \(N=a+b\),
\[
\mathbb EZ_{a,b}=N/4+A+B,
\quad
\mathbb EZ_{a,b}^2=(N^2+a^2+b^2+2N)/16+(b+1)A+(a+1)B.
\]
Subtracting the square of the mean proves the displayed variance expression.

For \(1\le a\le b\), put \(d=b-a\), \(A=2^{-(a+2)}\), \(B=2^{-(b+2)}\). Under the transfer \((a,b)\mapsto(a-1,b+1)\), the exponential terms become \(2A,B/2\). Substitution and cancellation yield the **exact transfer identity**
\[
\Delta=\frac{d+1}{8}+\left(3+\frac d2\right)A
+\left(\frac d4-1\right)B-3A^2+\frac34B^2.
\]
Here \(0<B\le A\le1/8\). If \(0\le d\le4\), the potentially negative term has coefficient \(d/4-1\le0\), and replacing \(B\) by \(A\) in this term gives the lower bound
\[
\Delta-\frac{d+1}{8}\ge A\left(2+\frac{3d}{4}-3A\right)+\frac34B^2>0.
\]
If \(d\ge4\), both the \(B\)-linear and \(B^2\) terms are nonnegative and
\[
\Delta-\frac{d+1}{8}\ge A\left(3+\frac d2-3A\right)>0.
\]
Thus making the pendant counts more unequal strictly increases variance. Repeated inward balancing proves the unique minimizer; repeated outward transfers give the star as unique maximizer. As \(n\to\infty\), the exponential terms are negligible at balance, so the quadratic leading term gives \(n^2/32\). At the star, \(a=0\), \(b=n-2\), the leading terms give \(n^2/16\); all remaining terms are of order at most \(n\), yielding the ratio \(2\).

## Verification
The standard-library Python file `verify.py` independently enumerates all vertex-retention masks for every \(D_{a,b}\) through \(12\) vertices. It compares exact rational second moments with both the closed formula and a separate pair-covariance computation; it also checks the transfer identity and inequality on a finite two-parameter grid and the extremizers through \(120\) vertices. Execute `python3 verify.py` from the extracted package directory. The observed output was `VERIFY_OK 5263`. These finite checks do not prove the all-size statement; the case split and transfer identity above do.

## Relationship to prior work
Diskin and Krivelevich's *Site Percolation on Pseudo-Random Graphs* (public preprint July 28, 2021) concerns vertex-retained induced graphs, especially component transitions in regular pseudorandom hosts. Its assumptions exclude the high-degree-inhomogeneous double-star family, and its theorems do not optimize isolated-vertex variance over tree structure. General indicator covariance identities and the four-state conditioning principle are elementary and are **not** claimed to be original. The mathematical contribution asserted here is the explicit **strict all-order variance rearrangement theorem** and complete diameter-at-most-three extremal classification at retention probability \(1/2\).

## Limitations
The theorem is restricted to diameter-at-most-three trees and equal one-half vertex-retention probability; neither a result for all trees nor a non-half probability extension follows. The asymptotic ratio refers only to this tree family. Finite verification supplements but never replaces the symbolic proof. Although available literature comparisons did not reveal a published equivalent, an older implicit result or more general extremal theorem may exist; independent historical-priority review has not been performed.

## References
1. S. Diskin and M. Krivelevich, *Site Percolation on Pseudo-Random Graphs*, preprint first posted 2021-07-28, https://arxiv.org/abs/2107.13326; *Random Structures & Algorithms* 63 (2023), 406–441, https://doi.org/10.1002/rsa.21141.
2. See `verify.py` for independently reproducible exact rational checks specific to the statements here.
