# Exact endpoint Hodge norms and separated finite peaks on complementary two-subset graphs

## Finding

For an integer \(n\ge3\), the triangular graph \(T_n=J(n,2)\) has all two-element subsets of \(\{1,\ldots,n\}\) as vertices; two vertices are adjacent when their intersection has cardinality one. For \(n\ge5\), its complementary Kneser graph \(K_n=KG(n,2)\) joins pairs of disjoint two-element subsets. Every graph considered here is finite, connected, simple and unweighted.

Equip the unoriented edge-coordinate space with the standard real \(\ell_1\) and \(\ell_\infty\) norms. Write \(Q_G\) for the Euclidean-orthogonal projection onto its cut space and \(C_G=I-Q_G\) for the complementary cycle projection. Then, for all \(n\ge3\),

\[
\|Q_{T_n}\|_{1\to1}=\frac{(n-2)(3n-1)}{n(n-1)},\qquad
\|C_{T_n}\|_{1\to1}=\frac{2(2n-5)}{n-1}.
\]

For all \(n\ge5\),

\[
\|Q_{K_n}\|_{1\to1}=\frac{2(n-3)(n+6)}{n(n-1)},\qquad
\|C_{K_n}\|_{1\to1}=\frac{3n^3-4n^2-59n+100}{n(n-3)(n-1)}.
\]

Each displayed value is also the corresponding induced \(\ell_\infty\) operator norm. On triangular graphs both norms increase strictly with \(n\), approaching \(3\) and \(4\), respectively. On the Kneser graphs, by contrast, the cut norm is globally maximal **exactly at \(n=8\) and \(n=9\)**, with value \(5/2\), while the cycle norm is globally maximal **uniquely at \(n=12\)**, with value \(1000/297\). The latter two norms tend to \(2\) and \(3\), respectively. Thus the complementary natural graph families have qualitatively different size profiles, and the two Kneser projection norms have different sharp maximizing orders.

## Assumptions and scope

Let \(B\) be any oriented vertex-by-edge incidence matrix and \(L=BB^{\mathsf T}\) the unweighted graph Laplacian. The cut projection is \(Q_G=B^{\mathsf T}L^+B\), with \(L^+\) the Moore–Penrose pseudoinverse, and \(C_G=I-Q_G\). No minimum-norm claim among arbitrary nonorthogonal projections is made. The scalar field for the edge-space norm is real; the same absolute-column-sum formulas also hold for the complex coordinate extension of these fixed real matrices.

## Proof

**1. Electrical-current reduction.** For an oriented edge \(e=(u,v)\), choose a potential \(h\) satisfying \(Lh=\delta_u-\delta_v\). Then the column \(Q_G\mathbf e_e\) has entries \(h(x)-h(y)\) on oriented edges \((x,y)\). Hence

\[
\|Q_G\mathbf e_e\|_1=\sum_{\{x,y\}\in E(G)}|h(x)-h(y)|.
\]

The symmetric group on the underlying \(n\) labels acts transitively on edges of either two-subset graph. Thus every column has the same absolute sum. The diagonal entry is \((Q_G)_{ee}=h(u)-h(v)\). Since it belongs to an orthogonal projector, it lies in \([0,1]\), and consequently

\[
\|C_G\mathbf e_e\|_1=\|Q_G\mathbf e_e\|_1+1-2(h(u)-h(v)).
\]

**2. Triangular graph.** Set \(u=\{1,2\}\), \(v=\{1,3\}\). The potential equals \(+U\) at \(u\), \(-U\) at \(v\), \(+V\) at each \(\{2,k\}\) and \(-V\) at each \(\{3,k\}\) for \(4\le k\le n\), and zero at all other vertices. For \(n\ge4\), the two nontrivial Laplacian equations are

\[
(2n-3)U-(n-3)V=1,\qquad (n+1)V-U=0.
\]

They give \(U=(n+1)/(2n(n-1))\) and \(V=1/(2n(n-1))\). Every zero-potential vertex has cancelling positive and negative neighbors. At \(n=3\), the \(V\)-orbits are absent and the sole source equation is \(3U=1\), yielding \(U=1/3\), consistent with the displayed formula. Thus the complete Laplacian system holds at every allowed order.

The complete count of graph edges with each positive absolute potential drop, where a zero multiplicity means the type is absent, is

| Absolute drop | Multiplicity in \(T_n\) |
| --- | ---: |
| \(2U\) | \(1\) |
| \(U\) | \(2(n-2)\) |
| \(U-V\) | \(2(n-3)\) |
| \(V\) | \(2(n-3)(n-2)\) |
| \(2V\) | \(n-3\) |

To see the count, start at the two endpoints, then enumerate edges from \(\{2,k\}\) and \(\{3,k\}\) to zero-potential pairs and to each other. The table partitions every edge with a nonzero potential drop; same-value edges contribute zero. Adding the drops gives

\[
\|Q_{T_n}\|_{1\to1}=4(n-2)U+2(n-3)(n-2)V
=\frac{(n-2)(3n-1)}{n(n-1)}.
\]

The diagonal is \(2U\). Applying the complementary-column identity gives the asserted cycle norm.

**3. Kneser graph.** Set \(u=\{1,2\}\), \(v=\{3,4\}\). Write \(+U\) at \(u\), \(-U\) at \(v\); put \(-W\) at \(\{1,k\},\{2,k\}\) and \(+W\) at \(\{3,k\},\{4,k\}\), for \(5\le k\le n\); put zero elsewhere. The degree is \(d=(n-2)(n-3)/2\). Direct adjacency counting yields

\[
(d+1)U-2(n-4)W=1,\qquad U-(d+n-5)W=0.
\]

All other Laplacian equations hold by pairwise cancellation: at a mixed pair there are equally many \(+W\) and \(-W\) neighbors; at a pair lying completely outside \(\{1,2,3,4\}\), the \(+U\), \(-U\) and outer neighbors cancel. Therefore the following is an exact solution, not an approximation:

\[
U=\frac{2(n+1)}{n(n-3)(n-1)},\qquad
W=\frac4{n(n-4)(n-3)(n-1)}.
\]

For \(n\ge5\), \(U>W>0\). The nonzero edge-drop counts are

| Absolute drop | Multiplicity in \(K_n\) |
| --- | ---: |
| \(2U\) | \(1\) |
| \(U-W\) | \(4(n-4)\) |
| \(U\) | \((n-4)(n-5)\) |
| \(W\) | \(2(n-4)[(n-5)(n-6)+4]\) |
| \(2W\) | \(4(n-4)(n-5)\) |

For example, the \(2W\) edges join one \(\{1,k\}\) or \(\{2,k\}\) pair to one \(\{3,l\}\) or \(\{4,l\}\) pair with \(k\ne l\), giving the stated factor. The \(W\) edges join outer-pair vertices to either a mixed pair or a disjoint outside pair. When \(n=5\), two drop magnitudes coincide numerically; they remain distinct combinatorial classes and must both be counted. Summing the entries gives

\[
\|Q_{K_n}\|_{1\to1}
=(n-2)(n-3)U+2(n-3)(n-4)^2W
=\frac{2(n-3)(n+6)}{n(n-1)}.
\]

The diagonal equals \(2U\), so the complementary-column identity gives the cycle formula.

**4. Exact maximizing orders.** Direct subtraction of consecutive expressions yields

\[
\|Q_{T_{n+1}}\|_{1\to1}-\|Q_{T_n}\|_{1\to1}
=\frac4{(n-1)(n+1)}>0,
\]

\[
\|C_{T_{n+1}}\|_{1\to1}-\|C_{T_n}\|_{1\to1}
=\frac6{n(n-1)}>0.
\]

For Kneser graphs the differences are

\[
\|Q_{K_{n+1}}\|_{1\to1}-\|Q_{K_n}\|_{1\to1}
=-\frac{8(n-8)}{n(n-1)(n+1)}
\]

and

\[
\|C_{K_{n+1}}\|_{1\to1}-\|C_{K_n}\|_{1\to1}
=-\frac{8[n(n-11)(n-4)-40]}{n(n-3)(n-2)(n-1)(n+1)}.
\]

Every denominator is strictly positive on the stated domain. The cut difference is positive for \(5\le n\le7\), zero at \(n=8\), and negative thereafter, giving exactly two maximizers. For the cycle difference, \(n(n-11)(n-4)-40<0\) at every \(5\le n\le11\), while it is positive at every \(n\ge12\), establishing the unique maximizer. Direct substitution yields the values above. The limits follow from the leading coefficients of the rational functions. As both projections are symmetric, the \(\ell_\infty\) norms equal their \(\ell_1\) norms.

## Verification

The accompanying `verify_2subset.py` uses only the Python standard library. It builds incidence matrices from the two-subset definitions, inverts grounded graph Laplacians over exact rational numbers, and checks **all 753 edge columns** of the two projectors on the ten graphs \(T_3,\ldots,T_8\) and \(K_5,\ldots,K_8\). It independently counts every nonzero potential-drop type for 32 graph-size instances from \(5\) through \(20\). These tests passed. The universal claims and global maximizing orders are established by the preceding all-parameter proof, not by a finite census.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii's public 2023 study establishes the cut/cycle projection framework and computes canonical or optimal projection norms for tori and Hamming graphs; its original paper is an anchor for this calculation. Schild, Rao and Srivastava's 2017 analysis identifies the absolute transfer-current norm as a natural electrical-flow localization quantity and gives general bounds, without these exact two-subset graph expressions. The present theorem concerns the **edge-incidence Hodge projectors**, not primitive idempotents of the Johnson association scheme acting on vertex functions. Generic effective-resistance identities and the relation between complementary column norms are standard or previously documented, not claimed new. The additional exact formulas and their sharply different integer-order maxima are the asserted contribution.

## Limitations

Only canonical orthogonal projections on the indicated unweighted families are studied; no claim is made about optimal nonorthogonal projections or arbitrary Johnson/Kneser parameters. The public-literature comparison is necessarily finite and cannot prove absolute novelty. Verification is analytical plus exact finite cross-checking, not independent mathematical certification.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, first publicly submitted May 21, 2023, arXiv:2305.12582; author-hosted complete text: https://denka.web.illinois.edu/CycleSpaces.pdf. Primary MSC 46B04.
2. A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, first publicly submitted August 4, 2017, arXiv:1708.01632, https://arxiv.org/pdf/1708.01632.
3. *Triangular Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/TriangularGraph.html (graph-definition and complement terminology only).
