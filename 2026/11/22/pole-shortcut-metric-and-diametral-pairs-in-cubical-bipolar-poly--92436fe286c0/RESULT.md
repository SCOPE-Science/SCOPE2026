# Pole-shortcut metric and diametral pairs in cubical bipolar polytopes

## Finding

For every integer \(n\ge 1\), let \(Q_n=[-1,1]^n\) and let \(P_n\) be any convex geometric realization of the bipolar polytope \(W(\mathcal F(Q_n))\), in which the vertices correspond to **all** faces of \(Q_n\), including the empty face. Such realizations exist by the cube case of Pavlík's geometric realization theorem [1]. Let \(G_n\) be the one-skeleton of \(P_n\).

Represent each nonempty face by a word \(u\in\{-1,0,+1\}^n\), with zero denoting a free coordinate, and represent the empty face by \(\bot\). For a pair of nonempty words \(u,v\), let \(a,b,c,e\) denote, respectively, the counts of coordinates with opposite fixed signs, exactly one zero, two zeros, and identical nonzero signs. Thus \(a+b+c+e=n\). Put \(f(u)=\#\{i:u_i=0\}\). The complete graph metric is

\[
\operatorname{dist}_{G_n}(u,v)=b+\min\{2a,2c+2\},\qquad
\operatorname{dist}_{G_n}(\bot,u)=f(u)+1.
\]

In particular, \(G_n\) is self-centered and

\[
\operatorname{rad}(G_n)=\operatorname{diam}(G_n)=n+1.
\]

Exactly the pairs \(\{\bot,0^n\}\) and the pairs of nonempty words with \(e=0\), \(a=c+1\) are diametral. Their number is

\[
M_n=1+\frac12\sum_{c=0}^{\lfloor(n-1)/2\rfloor}
\frac{n!\,2^{c+1}4^{n-2c-1}}{(c+1)!\,c!\,(n-2c-1)!}.
\]

The exact unordered, distinct-pair graph-distance enumerator \(D_n(z)=\sum_{\{u,v\}\subset V(G_n)}z^{\operatorname{dist}(u,v)}\) is

\[
D_n(z)=z(2+z)^n+\frac12\left[
\sum_{a+b+c+e=n}
\frac{n!\,2^{a+e}4^b}{a!\,b!\,c!\,e!}
 z^{b+\min\{2a,2c+2\}}-3^n\right].
\]

The polytope has \(3^n+1\) vertices and \(2n3^{n-1}+2^n\) edges. If \(U,V\) are independent uniform nonempty-face vertices (sampling with replacement), then

\[
0\le \frac{2n}{3}+2-\mathbb E\operatorname{dist}_{G_n}(U,V)
\le 2(n+1)\left(\frac{6+2\sqrt2}{9}\right)^n.
\]

Thus the mean distance is asymptotically \(2n/3+2\) with exponentially small error, even though the direct coordinatewise route has mean length \(8n/9\). This difference is caused by shortest paths passing through the empty-face pole.

## Assumptions and scope

The claim concerns the unweighted **edge-graph distance**, not Euclidean distance between a particular realization's vertices. The result holds for every convex realization with the combinatorial face lattice of \(W(\mathcal F(Q_n))\); it uses only that combinatorial type. The empty face is a vertex of the bipolar polytope, not a face of its underlying cube. All graph edges have unit length, and a distance enumerator sums over unordered pairs of distinct graph vertices. The two randomly sampled vertices in the expectation statement can coincide.

## Proof

**1. Edges and the elementary graph.** Pavlík [1, Definitions 4.1 and Theorem 4.5] identifies the vertices of \(W(\mathcal F(Q_n))\) with the elements of the face lattice of \(Q_n\), and its nonempty faces with intervals in that lattice. An interval is an edge precisely when its endpoints form a cover relation (its rank difference is one). Every nonempty cube face has a unique ternary encoding. Among nonempty faces, the cover relations change a single coordinate between zero and one of the two signs. Hence the induced subgraph on nonempty faces is the Cartesian product of \(n\) three-vertex paths \((-1)-0-(+1)\). The empty face is adjacent precisely to the \(2^n\) cube vertices (words with no zeros).

**2. Shortest paths.** In the Cartesian product, the shortest route between \(u,v\) has length \(2a+b\). From \(u\) to the empty-face vertex \(\bot\), any route must reach a word with no zeros and use the final incident edge, and all \(f(u)\) zeros can be fixed individually; hence the distance is \(f(u)+1\). A route between two nonempty words that visits \(\bot\) is at least \(f(u)+f(v)+2=b+2c+2\), and equality is attained by separately fixing all zeros. Consequently the global shortest distance is the minimum of these two routes, as claimed. No path can gain by visiting \(\bot\) more than once.

**3. Radius, diameter, and diametral pairs.** Since \(a+b+c+e=n\), the two candidate lengths become \(n+a-c-e\) and \(n+c-a-e+2\). If they were both greater than \(n+1\), one would require simultaneously \(a-c-e\ge2\) and \(a-c+e\le0\), an impossibility. Equality of their minimum with \(n+1\) holds precisely when \(e=0\), \(a=c+1\). The distance from the empty-face vertex to a word is at most \(n+1\), with equality only at the all-zero word.

To see that every vertex has eccentricity \(n+1\), the two poles \(\bot,0^n\) see one another at that distance. Given any other ternary word \(u\), choose a coordinate where \(u\) is fixed, and construct \(v\) by reversing its sign there, fixing all free coordinates of \(u\) to arbitrary signs, and making every other fixed coordinate of \(u\) free. This gives \(a=1,b=n-1,c=e=0\), hence distance \(n+1\). Thus all vertices have eccentricity \(n+1\). For the diameter-pair count, choose \(c\) both-free coordinates, \(c+1\) oppositely fixed coordinates, and the remaining \(n-2c-1\) one-free coordinates. Their ordered count is the multinomial summand, with \(2^{c+1}\) opposite-sign choices and \(4^{n-2c-1}\) one-free choices. Divide by two to pass to unordered pairs and add the single pole pair.

**4. Exact distance distribution and edge count.** For two ordered ternary words, each coordinate has \(2\) identical-fixed possibilities, \(2\) opposite-fixed possibilities, \(4\) one-free possibilities, and \(1\) both-free possibility. The multinomial expansion therefore counts every ordered pair with its correct distance. Subtract the \(3^n\) diagonal pairs and divide by two. There are \(\binom nf2^{n-f}\) nonempty faces with \(f\) zero coordinates, each at distance \(f+1\) from \(\bot\), contributing \(z(2+z)^n\). This proves the distance enumerator. For the edge count, the Cartesian path product has \(2n3^{n-1}\) edges and the empty-face pole supplies \(2^n\) more.

**5. Mean-distance law.** For independent uniform ternary words, the types at different coordinates are independent and satisfy \(\mathbb P(a\text{-type})=2/9\), \(\mathbb P(c\text{-type})=1/9\), \(\mathbb P(b\text{-type})=4/9\). Since \(f(U)+f(V)+2=b+2c+2\), the distance formula gives

\[
\operatorname{dist}(U,V)=f(U)+f(V)+2-2(C-A+1)_+,
\]

where \(A,C\) are the random opposite-fixed and both-free counts and \(x_+=\max\{0,x\}\). Because \(\mathbb E(f(U)+f(V)+2)=2n/3+2\), the difference is nonnegative. It is bounded by \(2(n+1)\mathbb P(A-C\le0)\). By the exponential Markov bound at \(t=(\log2)/2\),

\[
\mathbb P(A-C\le0)\le
\mathbb E e^{-t(A-C)}=
\left(\frac{6+2e^{-t}+e^t}{9}\right)^n
=\left(\frac{6+2\sqrt2}{9}\right)^n.
\]

This proves the stated exponential estimate; in particular it is not based on finite experiments.

## Verification

The included standalone \(\texttt{check\_metric.py}\) independently builds the Hasse-cover graph for \(1\le n\le6\), runs breadth-first search from **every vertex**, and compares all shortest-path distances with the closed formula. It additionally checks the diameter, eccentricities, edge count, full distance enumerator, and exact diametral-pair count against independently generated multinomial expressions. The observed diametral-pair counts at dimensions \(1,2,3,4,5,6\) are \(2,9,55,353,2281,14785\). These finite checks are supplementary: the proof above applies to all positive integers \(n\).

To reproduce, run \(\texttt{python3 check\_metric.py}\) with a standard Python 3 installation; no third-party packages are needed.

## Relationship to prior work

Pavlík's [1] construction and its cube realization, including the fact that the bipolar polytope's vertices are the cube faces and its faces are intervals, are antecedents, not discoveries here. [1, Sections 4--5] does not state the graph metric, self-centeredness, diametral-pair classification, or distance enumerator. Savvidou [2] studies interval-poset constructions arising in cubical barycentric subdivisions and proves face-vector and cubical \(h\)-vector formulas, but not the shortest-path metric for the *augmented* cube-face Hasse graph. Standard face-lattice/Hasse-diagram material [3] provides the underlying coordinate model, not the claimed all-distance classification. The new content is the exact pole-shortcut metric and its enumerative and probabilistic consequences, rather than the pre-existing combinatorial model.

## Limitations

The theorem is specific to the bipolar polytope associated with a cube (and any combinatorially equivalent realization). It is not a general theorem for arbitrary face lattices, nor a statement about Euclidean metric geometry. The literature comparison is provisional: a historical treatment of the same Hasse graph under another name might contain equivalent formulas. Independent mathematical validation has not been performed.

## References

[1] J. Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1, publicly submitted 2026-11-10, especially Definitions 4.1, Lemmas 4.2--4.3, Theorems 4.5 and 5.8. https://arxiv.org/abs/2611.13896

[2] C. Savvidou, *Face numbers of cubical barycentric subdivisions*, arXiv:1005.4156v2, 2010, especially Section 2.3 and Proposition 3.1. https://arxiv.org/abs/1005.4156

[3] G. Pineda-Villavicencio, *Polytopes and Graphs*, Cambridge University Press, Section 2.3 (face lattices and their Hasse diagrams), 2024. https://doi.org/10.1017/9781009257794
