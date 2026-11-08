# Frobenius incidence of the fifteen-plane boundary on Segre cubic twists

## Finding
Let \(q\) be a prime power of characteristic at least \(5\). Over \(\mathbb F_q\), let
\[
X:\quad \sum_{i=1}^{6}x_i=\sum_{i=1}^{6}x_i^3=0\subset\mathbb P^5,
\]
be the Segre cubic threefold. Its fifteen geometrically embedded planes are indexed by perfect matchings \(M\) of \(\{1,\dots,6\}\):
\[
\Pi_M=\{x_i+x_j=0\text{ for each }\{i,j\}\in M\}.
\]
Set \(B=\bigcup_M\Pi_M\), a closed reduced surface. For any permutation \(\sigma\in S_6\), denote by \((X_\sigma,B_\sigma)\) the \(\mathbb F_q\)-form obtained by descending \((X,B)\) with geometric Frobenius acting by \(\sigma\) on the six indices (equivalently, rational geometric points satisfy \(\sigma\circ\mathrm{Frob}_q(x)=x\)). All eleven conjugacy types \(\lambda\vdash6\) occur and the counts depend only on \(\lambda\).

Write \(N_m(\lambda,q)\) for the number of \(\mathbb F_q\)-rational points of \(B_\sigma\) lying on exactly \(m\) *geometric* planes. The only possible positive multiplicities are \(1,2,3,6\), and the complete table is:

| Frobenius cycle type \(\lambda\) | \(N_1\) | \(N_2\) | \(N_3\) | \(N_6\) |
|:--|--:|--:|--:|--:|
| \((6)\) | \(q(q+1)\) | \(0\) | \(0\) | \(1\) |
| \((5,1)\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \((4,2)\) | \(q(q+1)\) | \(q-2\) | \(1\) | \(2\) |
| \((4,1,1)\) | \(q(q+1)\) | \(q\) | \(1\) | \(0\) |
| \((3,3)\) | \(3q(q+1)\) | \(0\) | \(0\) | \(1\) |
| \((3,2,1)\) | \(0\) | \(0\) | \(1\) | \(1\) |
| \((3,1,1,1)\) | \(0\) | \(0\) | \(3\) | \(1\) |
| \((2,2,2)\) | \(7q^2-11q+6\) | \(9q-12\) | \(3\) | \(4\) |
| \((2,2,1,1)\) | \(3q^2-3q-2\) | \(5q-2\) | \(3\) | \(2\) |
| \((2,1,1,1,1)\) | \(3(q-2)(q+1)\) | \(9q-12\) | \(7\) | \(4\) |
| \((1,1,1,1,1,1)\) | \(15(q-2)(q-3)\) | \(45(q-2)\) | \(15\) | \(10\) |

In particular, the twist of type \((5,1)\) has **no rational point on its entire fifteen-plane boundary**, over any such \(\mathbb F_q\), although this boundary is nonempty and geometrically a union of planes. All its closed points have degree divisible by \(5\), and its first points arise over \(\mathbb F_{q^5}\). Their complete zeta function is
\[
Z(B_\sigma/\mathbb F_q,T)
=\frac{(1-q^5T^5)^6}{(1-q^{10}T^5)^3(1-T^5)^5}
\qquad(\lambda=(5,1)).
\]
For every cycle type \(\lambda\), the table also determines the full zeta function by applying it with \((\sigma^n,q^n)\) for every \(n\ge1\).

## Assumptions and scope
The characteristic assumption is \(p=\operatorname{char}(\mathbb F_q)\ge5\). The result concerns the specific marked \(S_6\)-forms obtained from the permutation action on coordinates; these are defined over every finite field via finite-field Galois descent. The incidence is with *all fifteen geometric planes*, including planes not individually defined over \(\mathbb F_q\). Counting rational planes rather than points lying on geometric planes gives a different invariant. The table does not count points on the whole cubic threefold outside the boundary.

## Proof
**1. Incidence support.** A nonzero projective vector \((x_1,\dots,x_6)\) lies in \(\Pi_M\) exactly when each pair of \(M\) matches two opposite entries. If the number of zero entries is \(2s\), the zero entries can be paired in \((2s-1)!!\) ways. For each nonzero class \(\{a,-a\}\), the numbers of entries equal to \(a\) and \(-a\) must coincide, say both equal \(r_a\); they can be paired in \(r_a!\) ways. Thus the number of containing planes is
\[
(2s-1)!!\prod_{\{a,-a\}}r_a!,\qquad
s+\sum r_a=3,
\]
where \((-1)!!=1\). Its possible positive values are precisely \(1,2,3,6\). This is a geometric statement over the algebraic closure, not just a finite-field experiment.

**2. Linear intersection formula.** For a nonempty subset \(I\) of the fifteen matchings, make a graph \(G_I\) with six vertices and all edges belonging to any matching in \(I\). The equations of \(L_I=\bigcap_{M\in I}\Pi_M\) are \(x_u+x_v=0\) on each graph edge. In odd characteristic, one free scalar survives for each bipartite connected component; a nonbipartite component forces all its coordinates to zero. Let \(b(I)\) be the number of bipartite components. Hence the vector-space dimension of \(L_I\) is \(b(I)\) and its projective dimension is \(b(I)-1\) when \(b(I)>0\). Every \(L_I\) lies on \(X\), because already each \(\Pi_M\) does. The formula is independent of the characteristic apart from excluding \(2\).

**3. Frobenius saturation.** For a permutation \(\sigma\), put \(\widehat I=\bigcup_{j\ge0}\sigma^j I\), a finite, \(\sigma\)-stable set of matchings. A point fixed by twisted Frobenius and lying in \(L_I\) necessarily lies in \(L_{\widehat I}\); the reverse inclusion is immediate. The latter is a descended projective linear space of dimension \(b(\widehat I)-1\). By finite-field descent of projective spaces (or Lang's theorem), it has exactly
\[
P_{b(\widehat I)}(q)=1+q+\cdots+q^{b(\widehat I)-1}
\]
rational points when \(b(\widehat I)>0\), and none otherwise. Thus, with \(S_k=\sum_{|I|=k}P_{b(\widehat I)}(q)\), double counting \(k\)-subsets of the incidence set gives \(S_k=\sum_m\binom mk N_m\). Binomial inversion yields the exact formula
\[
N_m=\sum_{k=m}^{15}(-1)^{k-m}\binom km
\sum_{\substack{I\subset\mathcal M\\ |I|=k}}P_{b(\widehat I)}(q).
\tag{*}
\]
There are only \(2^{15}-1=32767\) nonempty subsets. Evaluating (*) symbolically for a representative of each of the eleven partitions of \(6\) gives every row in the displayed table. The standalone `verify_incidence.py` enumerates the exact graph components and computes binomial inversion over \(\mathbb Z[q]\), asserting all forty-four polynomial entries; no numerical interpolation or finite-field extrapolation is involved.

**4. Degree-five descent and zeta function.** A \(5\)-cycle on the six indices permutes the fifteen matchings as three orbits of length \(5\). The set of planes through any rational boundary point is Frobenius stable. Its cardinality would therefore have to be a positive multiple of \(5\), contradicting the incidence values \(1,2,3,6\). This proves emptiness of the rational boundary independently of the table computation. For \(5\nmid n\), \(\sigma^n\) remains a \(5\)-cycle and \(B_\sigma(\mathbb F_{q^n})=\varnothing\). For \(5\mid n\), the planes all split and the split table gives
\[
\#B_\sigma(\mathbb F_{q^n})=15q^{2n}-30q^n+25.
\]
Exponentiating \(\sum_{n\ge1}\#B_\sigma(\mathbb F_{q^n})T^n/n\) proves the stated rational zeta function. The positive split count at \(n=5\) proves that degree \(5\) is the smallest extension where the boundary acquires points.

## Verification
Run `python3 verify_incidence.py` in the directory containing this file. It asserts every polynomial and prints `VERIFY_SEGRE_BOUNDARY_OK 11 FROBENIUS TYPES`. Independently, `python3 verify_direct.py` constructs \(\mathbb F_{25}\) and \(\mathbb F_{125}\) with explicit irreducible polynomials, enumerates the fifteen-plane union point-by-point, and tests twisted Frobenius on the geometric points for five involution/order-three conjugacy types over \(\mathbb F_5\). It prints `VERIFY_SEGRE_DIRECT_OK F25_F125`. These direct computations reproduce, for example, the totals \(166,86,98,91,4\) in the five tested classes. The all-characteristics proof is the graph/intersection argument above, not the finite-field examples.

## Relationship to prior work
The Segre cubic, its ten nodes and its fifteen planes are classical, and none of those objects or incidence relations is claimed as newly discovered. Avilov's *On forms of the Segre cubic* (2018, Section 2, especially Lemma 2.4 and Proposition 2.11) studies Galois forms, their automorphisms and fixed nodes/planes. Cheltsov–Tschinkel–Zhang's *Equivariant geometry of the Segre cubic and the Burkhardt quartic* (first posted August 29, 2023; Sections 2.4 and 6) analyzes the \(S_6\) action and equivariant birational geometry. Neither inspected treatment gives the eleven rational-point incidence polynomials for the union of the fifteen planes or the exceptional fifth-degree point obstruction. The claim here is the arithmetic stratification of that *closed union*, not the known configuration, nor the point count of the \(\mathcal M_{0,6}\)-type open complement. Earlier finite-field formulas for the whole Segre cubic in all eleven twist types do not distinguish boundary points by the number of geometric planes through them. Likewise, earlier Frobenius counts of the ten nodes, fifteen planes, and sixty node–plane incidence flags do not determine the positive-dimensional plane-intersection strata classified here.

## Limitations
The formula does not classify other forms arising from unrelated geometric varieties, nor does it determine the rational-point counts of the ambient cubic threefold. The exact polynomial identities are finite combinatorial identities with a complete symbolic verifier; the verifier is not a substitute for the mathematical justification of descent and graph components. Although the cited primary sources do not explicitly cover the displayed stratification, an earlier equivalent computation in the classical arithmetic of Segre configurations remains a historical-priority risk.

## References
- I. Cheltsov, Y. Tschinkel, Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, arXiv:2308.15271, version 1 submitted 2023-08-29; especially Sections 2.4 and 6. https://arxiv.org/abs/2308.15271
- A. Avilov, *On forms of the Segre cubic*, arXiv:1812.11363, 2018; especially Section 2, Lemma 2.4, Proposition 2.11. https://arxiv.org/abs/1812.11363
- I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, in *From Classical to Modern Algebraic Geometry*, 2016, for the classical ten-node/fifteen-plane configuration (background only).
