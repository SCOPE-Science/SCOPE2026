# Zero forcing polynomials and a rank transition in finite local unit graphs

## Finding

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(\mathfrak m\), residue-field order \(q=|R/\mathfrak m|\), maximal-ideal size \(s=|\mathfrak m|\), and \(N=qs\). For the unit graph \(G(R)\), whose distinct vertices are adjacent when their sum is a unit, \[\mathcal Z(G(R);u)=\binom{q}{2}s^2u^{N-2}+Nu^{N-1}+u^N.\] Thus \(Z(G(R))=N-2\), and the minimum zero forcing sets are exactly the complements of two vertices chosen from two distinct residue classes modulo \(\mathfrak m\). The polynomial recovers \(q\) and \(s\): if \(c\) is the coefficient of \(u^{N-2}\), then \(q=N^2/(N^2-2c)\) and \(s=N/q\). For real symmetric minimum rank, \(\operatorname{mr}(G(R))=2\) when \(q\) is odd or \(q=2\), while \(\operatorname{mr}(G(R))=3\) when \(q\) is even and \(q\ge4\). Consequently \(M(G(R))=Z(G(R))\) except for even residue fields of order at least \(4\), where \(Z(G(R))=M(G(R))+1\).

In particular, the zero forcing polynomial determines the unit graph up to isomorphism within the finite commutative local nonfield class, even though the real minimum-rank behavior has a sharp residue-characteristic transition.

## Assumptions and scope

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(\mathfrak m\). Put
\[
q=|R/\mathfrak m|,
\qquad
s=|\mathfrak m|,
\qquad
N=|R|=qs.
\]
For each residue \(a\in R/\mathfrak m\), let \(C_a\) be the corresponding additive coset of \(\mathfrak m\). Every \(C_a\) has cardinality \(s\).

The unit graph \(G(R)\) has vertex set \(R\), with two distinct vertices adjacent exactly when their sum is a unit.

## Proof

An element of a local ring is a unit exactly when its residue modulo \(\mathfrak m\) is nonzero. Hence, for
\[
x\in C_a,
\qquad
y\in C_b,
\]
one has
\[
x\sim y
\quad\Longleftrightarrow\quad
a+b\ne0
\quad\text{in }R/\mathfrak m.
\tag{1}
\]

If the residue characteristic is \(2\), then \(-a=a\) for every residue. Thus every \(C_a\) is independent, and two different residue classes are completely joined. Therefore
\[
G(R)\cong K_{s,s,\ldots,s}
\]
with \(q\) parts.

If the residue characteristic is odd, then \(C_0\) is independent, every nonzero \(C_a\) is a clique, \(C_a\) and \(C_{-a}\) have no edges between them, and every other pair of distinct residue classes is completely joined. Equivalently,
\[
\overline{G(R)}
\cong
K_s\;\dot\cup\;\frac{q-1}{2}K_{s,s}.
\tag{2}
\]

In either case, every residue class is a twin class: it is a false-twin class in residue characteristic \(2\), while in odd residue characteristic \(C_0\) is false-twin and each nonzero \(C_a\) is true-twin. Hence a zero forcing set cannot leave two white vertices in one residue class.

Suppose the white vertices lie in at least three distinct residue classes. In characteristic \(2\), a blue vertex in a white residue class sees all white classes except its own, hence at least two white neighbors; a blue vertex in a fully blue class sees all white classes. Thus no force is possible.

In odd residue characteristic, a blue vertex of \(C_0\) sees every white nonzero class. A blue vertex of a nonzero class \(C_a\) sees every white class except possibly \(C_{-a}\). With at least three white classes, every blue vertex therefore has either zero or at least two white neighbors. Again no force is possible.

Conversely, every profile with at most two white residue classes forces. In characteristic \(2\), if the white vertices lie in classes \(C_a,C_b\), a blue vertex of \(C_a\) sees only the white vertex of \(C_b\), and after that force the remaining white vertex is forced from \(C_b\). The one-white case is immediate.

In odd residue characteristic, for white classes \(C_a,C_b\) with both residues nonzero, a blue vertex of \(C_{-a}\) is nonadjacent to the white vertex in \(C_a\) and adjacent to the one in \(C_b\), so it performs the first force; then a blue vertex of \(C_0\) finishes. If the white classes are \(C_0,C_b\), a blue vertex of \(C_{-b}\) first forces the white vertex in \(C_0\), after which \(C_0\) forces the remaining white vertex. The one-white case is again immediate.

Therefore the minimum zero forcing sets are exactly the complements of one vertex from each of two distinct residue classes. Their number is
\[
\binom{q}{2}s^2.
\]
Every set of size \(N-1\) is zero forcing because the graph has no isolated vertices, and the whole vertex set is zero forcing. Hence
\[
\mathcal Z(G(R);u)
=
\binom{q}{2}s^2u^{N-2}+Nu^{N-1}+u^N.
\tag{3}
\]

Equation (3) also reconstructs the local size parameters. If
\[
c=\binom{q}{2}s^2,
\]
then
\[
N^2-2c
=
q^2s^2-q(q-1)s^2
=
qs^2,
\]
so
\[
q=\frac{N^2}{N^2-2c},
\qquad
s=\frac Nq.
\tag{4}
\]
Thus the polynomial determines the residue-field order and maximal-ideal size, and hence the unit-graph isomorphism type inside this local class.

It remains to determine real minimum rank.

Assume first that \(q\) is odd. Pair the nonzero residue classes as \(a,-a\). Choose distinct positive real numbers \(t_1,\ldots,t_{(q-1)/2}\), assign parameters \(t_a=t_j\), \(t_{-a}=-t_j\), and put \(t_0=0\). Assign every vertex in \(C_a\) the vector
\[
v_a=(1,t_a)\in\mathbb R^2
\]
and use the symmetric bilinear form with matrix
\[
H=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
Then
\[
v_a^{\mathsf T}Hv_b=t_a+t_b,
\]
which vanishes exactly for \(a=b=0\) or for opposite nonzero residue classes. This is precisely the off-diagonal zero pattern in (2), so it gives a graph-pattern matrix of rank \(2\). Since (3) gives \(Z=N-2\) and \(M\le Z\), one has \(\operatorname{mr}\ge2\). Therefore
\[
\operatorname{mr}(G(R))=2
\]
for odd \(q\).

If \(q=2\), then \(G(R)=K_{s,s}\), whose adjacency matrix has rank \(2\). Thus the same conclusion holds.

Now suppose \(q\) is even and \(q\ge4\). Because \(R\) is a finite local nonfield, \(\mathfrak m\ne\mathfrak m^2\): otherwise nilpotence of the maximal ideal would force \(\mathfrak m=0\). Hence \(\mathfrak m/\mathfrak m^2\) is a nonzero vector space over \(R/\mathfrak m\), and therefore
\[
s=|\mathfrak m|\ge q\ge4.
\tag{5}
\]

A rank-two real symmetric graph-pattern matrix for the complete \(q\)-partite graph would factor through a nondegenerate symmetric bilinear form on \(\mathbb R^2\). Inside each part, at least three nonzero representing vectors are pairwise orthogonal. In dimension two they must all lie on one isotropic line: if two were independent, a third vector orthogonal to both would be zero. Different parts require different isotropic lines, since vertices from different parts are adjacent. But a nondegenerate symmetric bilinear form on \(\mathbb R^2\) has at most two isotropic lines. Since \(q\ge4\), rank two is impossible.

For the matching upper bound, choose distinct real numbers \(t_1,\ldots,t_q\), assign every vertex in the \(j\)-th part the vector
\[
w_j=(1,t_j,t_j^2),
\]
and use
\[
B=
\begin{pmatrix}
0&0&1\\
0&-2&0\\
1&0&0
\end{pmatrix}.
\]
Then
\[
w_i^{\mathsf T}Bw_j=(t_i-t_j)^2,
\]
which vanishes exactly within a part and is nonzero across distinct parts. Three distinct vectors \(w_j\) already span \(\mathbb R^3\), so the resulting matrix has rank \(3\). Therefore
\[
\operatorname{mr}(G(R))=3
\]
when \(q\) is even and \(q\ge4\).

Combining this with \(M=N-\operatorname{mr}\) proves
\[
M(G(R))=
\begin{cases}
N-2,&q\text{ odd or }q=2,\\
N-3,&q\text{ even and }q\ge4.
\end{cases}
\]
Thus \(Z=M\) except in the even residue-field orders at least \(4\), where \(Z=M+1\).

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

It constructs the unit graphs of
\[
\mathbb Z/4\mathbb Z,
\qquad
\mathbb Z/8\mathbb Z,
\qquad
\mathbb Z/9\mathbb Z
\]
directly from the condition that the sum be coprime to the modulus. It also constructs the unit graph of the dual-number ring
\[
\mathbb F_4[\varepsilon]/(\varepsilon^2)
\]
directly from its residue-field coordinate.

For all four graphs, every vertex subset is exhaustively tested, and the complete zero forcing polynomial is compared with (3). The largest exhaustive case has \(16\) vertices and therefore \(65536\) subsets.

The checker independently builds the rank-two witnesses for odd residue fields and for \(q=2\), the rank-three witness for \(q=4\), and verifies their graph patterns and exact rational ranks. It also tests the two-white-class forcing rule and the parameter-recovery formula on additional abstract local parameter pairs.

Exact replay output:

```text
Z/4Z: q=2, s=2, polynomial={2: 4, 3: 4, 4: 1}
Z/8Z: q=2, s=4, polynomial={6: 16, 7: 8, 8: 1}
Z/9Z: q=3, s=3, polynomial={7: 27, 8: 9, 9: 1}
F4[e]/(e^2): q=4, s=4, polynomial={14: 96, 15: 16, 16: 1}
rank witness q=2, s=2: rank=2
rank witness q=2, s=4: rank=2
rank witness q=3, s=3: rank=2
rank witness q=5, s=5: rank=2
rank witness q=4, s=4: rank=3
PROFILE_AND_RECOVERY_OK
VERIFY_OK
```

The finite checks corroborate the arbitrary-ring proof. The rank-two impossibility for even \(q\ge4\) is the bilinear-form argument above, not a finite search.

## Relationship to prior work

Ashrafi, Maimani, Pournaki, and Yassemi introduced the general unit graph of a ring and studied connectedness, chromatic index, diameter, girth, and planarity. Su, Noguchi, and Zhou subsequently studied finite commutative unit graphs of small genus; their full text has primary Mathematics Subject Classification \(13A99\) and records publication on 9 September 2014. Their paper does not contain “zero forcing,” “minimum rank,” or “maximum nullity.”

A recent dominant-metric study gives the same residue-coset decomposition for finite local unit graphs and proves a different one-vertex-per-fiber deletion theorem for dominating resolving sets. Its full text contains no zero-forcing or minimum-rank result.

Boyer and collaborators prove the zero forcing polynomial of a complete multipartite graph. Consequently, the characteristic-two branch of (3), viewed only as a graph-theoretic complete-multipartite calculation, is prior coverage. Barrett, van der Holst, and Loewy characterize real graphs of minimum rank at most two; their theorem broadly covers the low-rank structure behind the odd-characteristic branch and explains why complements built from one clique and complete bipartite components admit rank two.

The strengthened content here is the local-ring-wide forcing classification across both residue-characteristic regimes, the fact that the same three-term polynomial recovers \(q\) and \(|\mathfrak m|\), and the sharp maximum-nullity transition: the forcing number stays \(N-2\) in every local nonfield, while real minimum rank jumps from \(2\) to \(3\) exactly for even residue fields of order at least \(4\).

## Limitations

The theorem excludes fields. The proof of the two-white-fiber classification uses \(|\mathfrak m|\ge2\), so field fibers require a separate boundary analysis.

The polynomial determines \(q\) and \(|\mathfrak m|\), not the local ring isomorphism type. Different finite local rings can share these two parameters and therefore have isomorphic unit graphs.

The characteristic-two polynomial is a specialization of the known complete-multipartite formula; it is not claimed as standalone novelty.

The minimum-rank statement is over real symmetric graph-pattern matrices.

## References

1. H. Su, K. Noguchi, and Y. Zhou, “Finite commutative rings with higher genus unit graphs,” *Journal of Algebra and Its Applications* 14 (2015), 1550002. DOI: 10.1142/S0219498815500024. Published 9 September 2014. Primary MSC \(13A99\), \(05C25\).
2. N. Ashrafi, H. R. Maimani, M. R. Pournaki, and S. Yassemi, “Unit Graphs Associated with Rings,” *Communications in Algebra* 38 (2010), 2851–2871. DOI: 10.1080/00927870903095574.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
4. W. Barrett, H. van der Holst, and R. Loewy, “Graphs whose minimal rank is two,” *Electronic Journal of Linear Algebra* 11 (2004), 258–280. DOI: 10.13001/1081-3810.1137.
5. H. Almotairi, “Dominant Metric Dimension of Unit Graphs of Finite Commutative Rings,” *Journal of Mathematics* (2026). DOI: 10.1155/jom/6300309.
6. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
