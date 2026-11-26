# Degree-profile classification and the first graph collision for defective tripartite Henson spectra

## Finding

Fix integers \(a,b,c\ge1\). From \(K_{a,b,c}\) with independent shores \(A,B,C\), delete exactly the edges of a bipartite pattern \(F\subseteq K_{a,b}\) between \(A\) and \(B\), obtaining \(G_F\). Name the vertices of \(G_F\) individually in the countable homogeneous \(K_4\)-free Henson graph. Let \(P_F(z)\) count complete nonalgebraic one-point types by the number of neighbors among those parameters. Write \(m=|E(F)|\) and \(d_F(v)\) for a degree in the deletion pattern. Then
\[
\begin{split}
P_F(z)&=(1+z)^{a+b}+\big((1+z)^c-1\big)\big(D_F(z)+R_F(z)\big),\\
D_F(z)&=(1+z)^a+(1+z)^b-1+z\sum_{v\in A\cup B}\big((1+z)^{d_F(v)}-1\big)-mz^2,\\
R_F(z)&=\sum_{\substack{S\subseteq A,\ T\subseteq B\\|S|,|T|\ge2,\ S\times T\subseteq E(F)}}z^{|S|+|T|}.
\end{split}
\]
The correction \(R_F\) vanishes exactly for \(C_4\)-free \(F\). If \(F\) has \(q_4(F)>0\) four-cycles, the first difference between \(P_F\) and its degree-only expression (obtained by omitting \(R_F\)) is \(c q_4(F)\) in degree five. For fixed \((a,b,c)\), two \(C_4\)-free patterns give equal polynomials exactly when their **combined** degree multisets on \(A\cup B\) agree, including zero degrees.

The reconstruction threshold below compares parameter graphs as *ordinary uncoloured graphs*, always for a common fixed triple \((a,b,c)\). For \(a+b\le4\) equal polynomials imply isomorphic parameter graphs. At \(a+b=5\) there is exactly one polynomial fibre containing two nonisomorphic parameter graphs, up to exchange of \(A,B\) and relabelling. For \((a,b)=(2,3)\), its two patterns \(F_A,F_B\) are the two-edge stars with their centers respectively in \(A\) and \(B\). Their common polynomial and total are
\[
P_{F_A}(z)=P_{F_B}(z)=(1+z)^5+\big((1+z)^c-1\big)(1+5z+6z^2+2z^3),
\qquad P_{F_A}(1)=18+14\,2^c.
\]
For \(c=1\) the polynomial is \(1+6z+15z^2+16z^3+7z^4+z^5\), giving 46 types at the first order of six parameters. All these graph pairs are connected and the sums of cubes of their parameter-graph degrees differ by six. There is a **second fibre of shore-labelled patterns** at \((2,3)\), consisting of the two complements \(K_{2,3}\setminus F_A\) and \(K_{2,3}\setminus F_B\) treated as deletion patterns. One contains a four-cycle. In this fibre the two parameter graphs are isomorphic, so it is not a second graph reconstruction failure.

## Assumptions and scope

Graphs are finite, simple and undirected except for the ambient Henson graph. A four-cycle is an ordinary copy of \(K_{2,2}\) in the bipartite deletion pattern. A type is nonalgebraic and specifies the new point's adjacencies and nonadjacencies to all individually named vertices; the polynomial only records the number of adjacencies. A shore-labelled pattern is considered up to independent permutations within each shore, with whole-shore exchange allowed when sizes agree. The graph threshold does not compare different triples of shore sizes, or arbitrary parameter graphs in the Henson graph.

## Proof

### Exact polynomial and inverse theorem

An admissible neighborhood in \(G_F\) is exactly a triangle-free subset. A triangle would create a \(K_4\) with the new point. Conversely adjoining the point with that neighborhood gives a finite \(K_4\)-free extension, realized over the fixed parameters by the extension property. Homogeneity gives exactly one complete type for each neighborhood.

Neighborhoods omitting \(C\) contribute \((1+z)^{a+b}\). Those meeting \(C\) may choose any nonempty subset of that shore. A triangle then occurs precisely if some selected cross pair between \(A\) and \(B\) survives as an edge of \(G_F\). Thus such neighborhoods contribute \(((1+z)^c-1)Q_F(z)\), where
\[
Q_F(z)=\sum_{S\subseteq A,\ T\subseteq B:\ S\times T\subseteq E(F)}z^{|S|+|T|}.
\]
Equivalently \(Q_F\) is the independence polynomial of the bipartite graph \(K_{a,b}\setminus F\). The terms where a shore is empty give \((1+z)^a+(1+z)^b-1\). The nonempty terms with a singleton shore come from choosing its vertex and then a nonempty subset of its neighbors in \(F\); each deleted edge is counted twice and so contributes a correction \(-z^2\). All remaining terms are precisely \(R_F\). A rectangle in this remainder contains a four-cycle, and each four-cycle contributes one rectangle of size \(2+2\). This proves the extinction criterion and the first correction coefficient. In particular the correction is not determined by degrees in general: on shores of size four, an eight-cycle and two disjoint four-cycles have the same degrees but distinct fourth coefficients in \(R_F\).

For fixed shores, equality of \(P_F\) is equivalent to equality of \(Q_F\), since the multiplier of \(Q_F\) is nonzero. When \(F\) is \(C_4\)-free, \(Q_F=D_F\). Its quadratic coefficient is \(\binom a2+\binom b2+m\), so \(D_F\) determines \(m\) and hence
\[
\sum_{v\in A\cup B}(1+z)^{d_F(v)}
=a+b+\frac{D_F(z)-((1+z)^a+(1+z)^b-1)+mz^2}{z}.
\]
Writing \(y=1+z\), the coefficients of this polynomial in \(y\) are the multiplicities of the degrees. Conversely the combined degree multiset determines \(m\) and \(D_F\).

### Exhaustion at the first collision threshold

Take \(a\le b\). If \(a=1\), the pattern is fixed up to relabelling by its edge count, which is recovered from the quadratic coefficient of \(Q_F\) after removing the known empty-shore contribution. For \((a,b)=(2,2)\), all edge counts except two have one pattern up to the allowed permutations. At two edges, a matching and a star are the only choices, and only the star contributes a mixed cubic term. The two orientations of the star are exchanged by swapping the equally sized shores.

It remains to check \((a,b)=(2,3)\). Regard \(B\) as the three columns of the deletion matrix. Up to row exchange, let \(u\ge v\) count columns with an edge only in the respective rows, and let \(w\) count double columns; there are \(3-u-v-w\) empty columns. Every triple of nonnegative integers satisfying these constraints specifies exactly one pattern up to relabelling. Subtract the empty-shore contribution from \(Q_F\); the remaining mixed contribution is
\[
H(z)=z\big((1+z)^{u+w}+(1+z)^{v+w}-2\big)+z^2\big((1+z)^w-1\big).
\]
The two summands count selections of one and two rows, respectively. The complete list is

| \(m\) | \((u,v,w)\) | \(H(z)\) |
|---|---|---|
| 0 | \((0,0,0)\) | \(0\) |
| 1 | \((1,0,0)\) | \(z^2\) |
| 2 | \((1,1,0)\) | \(2z^2\) |
| 2 | \((2,0,0),(0,0,1)\) | \(2z^2+z^3\) |
| 3 | \((2,1,0)\) | \(3z^2+z^3\) |
| 3 | \((1,0,1)\) | \(3z^2+2z^3\) |
| 3 | \((3,0,0)\) | \(3z^2+3z^3+z^4\) |
| 4 | \((1,1,1)\) | \(4z^2+3z^3\) |
| 4 | \((2,0,1),(0,0,2)\) | \(4z^2+4z^3+z^4\) |
| 5 | \((1,0,2)\) | \(5z^2+6z^3+2z^4\) |
| 6 | \((0,0,3)\) | \(6z^2+9z^3+5z^4+z^5\) |

The collision at two deletions consists of the stated stars. Take \(E(F_A)=\{a_0b_0,a_0b_1\}\) and \(E(F_B)=\{a_0b_0,a_1b_0\}\). In \(G_{F_A}\) the degrees on \(A\cup B\) are \(c+1\) three times, \(c+2\) once, and \(c+3\) once; in \(G_{F_B}\) they are \(c\) once and \(c+2\) four times. Degrees on \(C\) equal five in both graphs. Thus the difference of cube sums is \(3(c+1)^3+(c+3)^3-3(c+2)^3-c^3=6\) for every \(c\). Connectivity holds since \(C\) is nonempty and adjacent to all of \(A\cup B\). The common polynomial follows by adding the empty-shore contribution to \(2z^2+z^3\) and using the factorization above.

At four deletions, the patterns are complements of these two patterns in \(K_{2,3}\). The surviving graphs on \(A\cup B\) are therefore the original two-edge stars, each isomorphic to \(P_3\sqcup 2K_1\) once colours are forgotten. Joining either to the independent shore \(C\) preserves that isomorphism. This concludes the all-pattern classification at the threshold for every \(c\ge1\).

## Verification

The classification through \(a+b=5\) is exhausted by the table and the cases with a singleton shore or two equal shores of size two. The accompanying `verify_degree_collapse.py` independently enumerates triangle-free neighborhoods for small patterns and checks the first four-cycle correction. Its polynomial-fibre test is restricted to \(C_4\)-free patterns, so it corroborates the two-deletion witness but does not certify the full table or the distinction between pattern and graph fibres. See `VERIFICATION.md` for the scope of the finite checks.

## Relationship to prior work and limitations

The Henson extension criterion and the clique-free-subset polynomial interpretation are standard and already used in *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*. For the complete cross-edge case (no deletions), *Finite-jet reconstruction of complete multipartite Henson type spectra* concerns recovering shore sizes rather than recovering a deleted-edge degree multiset with the shores fixed. *Forest defects in multipartite clique-avoidance* analyzes homotopy type, not the polynomial of graded subset counts. The fact that every biclique of a \(C_4\)-free bipartite graph is a star is not a novelty claim. The distinct *Sharp six-vertex reconstruction failure for one-point type polynomials over 2-trees* gives a different pair in a different restricted class; its six-vertex common polynomial ends at degree four and totals 44, rather than 46. The fixed-shore theorem here gives no global first collision across unrelated decompositions or graph classes. Historical priority beyond the compared sources is not asserted.

## References

1. G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, §3, https://arxiv.org/abs/1401.1570.
2. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650.
3. *Finite-jet reconstruction of complete multipartite Henson type spectra*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-finite-jet-reconstruction-of-complete-multipartite-henson-type-s--5d62697fc5af.
4. *Forest defects in multipartite clique-avoidance: a shape-invariant sphere-wedge law and an integral persistence transition*, https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-forest-defects-in-multipartite-clique-avoidance-a-shape-invarian--636cc79caa35.
5. *Sharp six-vertex reconstruction failure for one-point type polynomials over 2-trees*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-six-vertex-reconstruction-failure-for-one-point-type-polyn--a112196b9f8b.
