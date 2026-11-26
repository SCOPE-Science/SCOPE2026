# Endpoint cut–cycle norms of complete multipartite graphs and a maximizing-edge reversal

## Finding
Let \(r\ge3\), let \(n_1,\ldots,n_r\) be positive integers, put \(N=\sum_i n_i\), and give the edges of the unweighted complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) any orientation. Let \(B\) be its vertex–edge incidence matrix, \(L=BB^{\mathsf T}\), and consider the canonical Euclidean-orthogonal cut and cycle projections on the *real* edge-coordinate space:
\[
Q=B^{\mathsf T}L^+B,\qquad P=I-Q.
\]
Here \(L^+\) is the Moore–Penrose pseudoinverse. For each admissible part size \(a\) define
\[
F_N(a)=\frac{N^2-2N+2-a^2}{N(N-a)},\qquad
H_N(a)=\frac{(N-2)^2-a^2}{N(N-a)}.
\]
For **every** edge joining distinct parts of sizes \(a,b\), the absolute column sums of \(Q\) and \(P\) are exactly
\[
\sum_{f\in E}|Q_{fe}|=F_N(a)+F_N(b),\qquad
\sum_{f\in E}|P_{fe}|=1+H_N(a)+H_N(b).
\]
Consequently the induced \(\ell_1\) and \(\ell_\infty\) operator norms are equal and satisfy
\[
\boxed{\|Q\|_1=\|Q\|_\infty=F_N(n_{(1)})+F_N(n_{(2)})},
\]
where \(n_{(1)}\ge n_{(2)}\ge\cdots\ge n_{(r)}\) are the part sizes in nonincreasing order, and
\[
\boxed{\|P\|_1=\|P\|_\infty
 =1+\max_{1\le i<j\le r}\{H_N(n_i)+H_N(n_j)\}}.
\]
Thus the cut norm always has a maximizing edge between **two largest parts**, whereas the cycle norm need not.

In fact, for each integer \(k\ge3\) the graph \(K_{k,2,1}\) exhibits a strict *maximizing-edge reversal*: the cut norm is maximized only on edges joining the \(k\)- and \(2\)-vertex parts; the cycle norm only on edges joining the \(2\)- and \(1\)-vertex parts. Their exact values are
\[
\boxed{\|Q\|=\frac{7k^2+21k+8}{3(k+1)(k+3)},\qquad
\|P\|=\frac{k(3k+7)}{(k+1)(k+3)}}.
\]
The loss in the cut column sum on replacing the largest part by the singleton equals the gain in the cycle column sum from the same replacement:
\[
\big[F_N(k)+F_N(2)\big]-\big[F_N(2)+F_N(1)\big]
=\big[1+H_N(2)+H_N(1)\big]-\big[1+H_N(k)+H_N(2)\big]
=\frac{k-1}{3(k+3)}>0,\qquad N=k+3.
\]
These norms are for the *specified orthogonal projections*; no optimization over arbitrary nonorthogonal projections is asserted.

## Assumptions and scope
The graph is finite, connected, simple, complete multipartite, and has at least three nonempty vertex parts. Every graph edge has unit weight. The edge-coordinate space is real \(\mathbb R^{E}\), carrying either \(\ell_1\) or \(\ell_\infty\). The projections \(Q,P\) are orthogonal with respect to the *Euclidean* inner product, not the endpoint Banach norms. The induced norms do not depend on the chosen edge orientations because orientation changes conjugate the matrices by diagonal sign matrices. Every distinct pair of parts has edges, so each pair of part-size scores is a realizable edge type.

## Proof
**1. The potential for one edge.** Partition the real vertex-vector space into the orthogonal sum of within-part zero-sum subspaces and the subspace of part-constant vectors. The Laplacian has eigenvalue \(N-n_i\) on the within-part zero-sum subspace for part \(i\), eigenvalue \(N\) on the global-mean-zero part-constant subspace, and eigenvalue zero on constants. This follows directly from
\[
(Lz)_v=(N-n_i)z_v-\sum_{w\notin V_i}z_w\quad(v\in V_i).
\]
Fix an edge \(e=(u,v)\) from a part of size \(a\) to a different part of size \(b\). Put \(\alpha=(N-a)^{-1}\) and \(\beta=(N-b)^{-1}\). The uniquely determined mean-zero potential \(h=L^+(\delta_u-\delta_v)\) has the following five values:
\[
\begin{array}{c|c}
\text{vertex category}&h\\ \hline
u& (N-1)\alpha/N\\
V_a\setminus\{u\}&-\alpha/N\\
v&-(N-1)\beta/N\\
V_b\setminus\{v\}&\beta/N\\
V\setminus(V_a\cup V_b)&0.
\end{array}
\]
Indeed, the mean of the displayed values is zero and applying \(L\) produces \(\delta_u-\delta_v\). Alternatively this follows by the preceding eigenspace decomposition. Therefore each entry of column \(e\) of \(Q\) is the signed difference of these potentials across the corresponding edge.

**2. Sum the absolute edge differences.** Since \(r\ge3\), both \((N-1)\alpha-\beta\) and \((N-1)\beta-\alpha\) are nonnegative. The five types of edges with nonzero differences and their total absolute contributions, all divided by \(N\), are:
\[
\begin{array}{c|l}
\text{type}&\text{numerator of total absolute contribution}\\ \hline
\{u,v\}&(N-1)(\alpha+\beta)\\
\{u,V_b\setminus\{v\}\}&(b-1)((N-1)\alpha-\beta)\\
\{V_a\setminus\{u\},v\}&(a-1)((N-1)\beta-\alpha)\\
\{V_a\setminus\{u\},V_b\setminus\{v\}\}&(a-1)(b-1)(\alpha+\beta)\\
\text{edges to all remaining vertices}&(N-a-b)[(N+a-2)\alpha+(N+b-2)\beta].
\end{array}
\]
All other edge differences vanish. Grouping the \(\alpha\) and \(\beta\) terms yields
\[
\|Q\mathbf e_e\|_1
=\frac{N^2-2N+2-a^2}{N(N-a)}+
 \frac{N^2-2N+2-b^2}{N(N-b)}=F_N(a)+F_N(b).
\]
The diagonal entry is the effective resistance
\[
Q_{ee}=h_u-h_v=\frac{N-1}{N}\left(\frac1{N-a}+\frac1{N-b}\right).
\]
Because \(Q\) is an orthogonal projection, \(0\le Q_{ee}\le1\). For \(P=I-Q\), only this one diagonal entry differs from the negated \(Q\)-column. Hence
\[
\|P\mathbf e_e\|_1=1+\|Q\mathbf e_e\|_1-2Q_{ee}
=1+H_N(a)+H_N(b).
\]
This establishes both exact column formulas, including singleton parts. Matrix symmetry gives equality of the induced \(\ell_1\) and \(\ell_\infty\) norms.

**3. Why the cut norm selects the largest parts.** For distinct part sizes \(a\ge b\), direct subtraction gives
\[
F_N(a)-F_N(b)=\frac{a-b}{N}
\left(1-\frac{2(N-1)}{(N-a)(N-b)}\right).
\]
Because there is at least one further nonempty part, \(a+b\le N-1\). Set \(x=N-a\), \(y=N-b\). Then \(x,y\ge2\), \(x+y\ge N+1\), and
\[
xy-2(N-1)=(x-2)(y-2)+2(x+y-N-1)\ge0.
\]
Thus \(F_N(a)\ge F_N(b)\) whenever two actual part sizes satisfy \(a\ge b\). The two largest sizes maximize their sum. Note that the inequality may be an equality at boundary configurations; no uniqueness of maximizing cut edges is claimed for general part lists.

**4. The opposite response for cycle columns.** The cycle score satisfies the related but stronger threshold
\[
H_N(a)-H_N(b)=\frac{a-b}{N}
\left(1-\frac{4(N-1)}{(N-a)(N-b)}\right).
\]
It therefore need not be ordered by part size. For the part sizes \((k,2,1)\) with \(k\ge3\), direct substitutions and cancellation give
\[
F_N(k)>F_N(2)>F_N(1),\qquad
H_N(2)\ge H_N(1)>H_N(k),\quad N=k+3,
\]
where equality \(H_N(2)=H_N(1)\) occurs only when \(k=3\). In particular the maximizing *part-pair* is unique in each case: \((k,2)\) for \(Q\) and \((2,1)\) for \(P\). Substituting these pairs into the column formulas gives the two displayed rational norms. The strict matched margins follow from
\[
F_N(k)-F_N(1)=H_N(1)-H_N(k)=\frac{k-1}{3(k+3)}.
\]
This completes the proof for all permitted part sizes and all \(k\ge3\).

## Verification
The standalone Python 3 program `verify_multipartite.py` uses only the standard library and may be executed as `python verify_multipartite.py`. It rebuilds the graph Laplacian, inverts a grounded minor with exact rational Gaussian elimination, reconstructs *every* cut and cycle column, and compares its actual absolute column sum with the claimed part-score formula. It exhausts all unordered integer part-size partitions for \(3\le N\le9\), having at least two parts (86 graphs, 1,572 columns), and independently evaluates the strict part-score rankings and two rational norm formulas for \(3\le k\le40\). The output was `COMPLETE_MULTIPARTITE_CERTIFICATE_OK partitions=86 columns=1572 family_cases=38`. These finite checks support the calculations but the general proof is the four analytical steps above.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii [1,2] establish the functional-analytic meaning of cycle spaces inside edge \(\ell_1\) and study invariant/minimal projections. The 2023 source computes and studies orthogonal and other projections on discrete tori and Hamming graphs; those graph products and their projection problems do not entail the edge-column formulas or top-part/reversal phenomena for arbitrary complete multipartite graphs. The 2018 source focuses on graph transportation spaces, complemented subspaces, diamonds, and Laakso graphs. The presently stated norms are specifically for canonical **Euclidean-orthogonal** projections, not minimum norms over all projections, so related optimized-projection results require separate comparison.

Published calculations of coordinate suppression on cactus transportation-space bases concern maps on a *quotient*, not the orthogonal cut/cycle projections treated here. Graphical-zonotope and symmetric-edge-polytope invariants of complete multipartite graphs likewise do not determine these operator norms. More general Laplacian pseudoinverse or effective-resistance identities can recover single diagonal entries but do not alone supply the full absolute column sums, their maximizing part types, and the strict reversal family.

## Limitations
The statement assumes unit edge weights and real edge coordinates, and concerns the canonical Euclidean-orthogonal cut/cycle projections. It does not establish optimality among nonorthogonal projections, give results for arbitrary weighted multipartite graphs, or assert any corresponding behavior for arbitrary graphs. General multipartite cycle-norm maximizers are specified through the exact part-score maximization rather than a single size-order classification. Bibliographic searches and inspections are finite; specialized network or Banach-space literature may contain an equivalent formula not identified here. Independent mathematical audit has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, first arXiv version 2023-05-21, arXiv:2305.12582, https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz Free Spaces on Finite Metric Spaces*, first arXiv version 2018-07-10, arXiv:1807.03814, https://arxiv.org/abs/1807.03814.
