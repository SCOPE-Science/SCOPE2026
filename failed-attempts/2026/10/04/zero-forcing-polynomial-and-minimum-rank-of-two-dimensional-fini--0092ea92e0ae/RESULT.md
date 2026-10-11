# Zero forcing polynomial and minimum rank of two-dimensional finite-field total dot product graphs

## Finding

Let \(q\) be a prime power and let \(TD_2(q)\) be Badawi's total dot product graph on \(\mathbb F_q^2\setminus\{0\}\), with distinct nonzero vectors adjacent exactly when their standard dot product is zero. For \(q\ge3\), \[\mathcal Z(TD_2(q);u)=u^{(q+1)(q-2)}(u+q-1)^{q+1},\]\[Z(TD_2(q))=M(TD_2(q))=q^2-q-2,\qquad \operatorname{mr}(TD_2(q))=q+1,\]where minimum rank is over real symmetric graph-pattern matrices. Every minimum zero forcing set is exactly the complement of a projective transversal: it omits one nonzero vector from each one-dimensional subspace of \(\mathbb F_q^2\), so there are \((q-1)^{q+1}\) minimum sets. For \(q=2\), \(TD_2(2)\cong K_1\dot\cup K_2\), hence \(\mathcal Z(TD_2(2);u)=2u^2+u^3\), \(Z=M=2\), and \(\operatorname{mr}=1\).

For \(q\ge3\), the zero forcing polynomial is insensitive to the orthogonal-line type: whether the projective orthogonality involution has zero, one, or two fixed lines, all component contributions collapse to the same factorization.

## Assumptions and scope

Let
\[
V=\mathbb F_q^2,
\]
with the standard symmetric bilinear form
\[
\langle (a,b),(c,d)\rangle=ac+bd.
\]
The total dot product graph \(TD_2(q)\) has vertex set \(V\setminus\{0\}\), and distinct vertices are adjacent exactly when their dot product is zero.

The projective line set
\[
\mathbb P^1(\mathbb F_q)
\]
has \(q+1\) elements, and every line contains
\[
s=q-1
\]
nonzero vectors.

For a graph \(G\),
\[
\mathcal Z(G;u)=\sum_k z(G;k)u^k
\]
is the zero forcing polynomial,
\[
\operatorname{mr}(G)
\]
is the minimum rank over real symmetric matrices with off-diagonal pattern \(G\), and
\[
M(G)=|V(G)|-\operatorname{mr}(G).
\]

## Proof

Orthogonal complementation gives an involution
\[
L\longmapsto L^\perp
\]
on the \(q+1\) projective lines.

If
\[
L\ne L^\perp,
\]
then every nonzero vector of \(L\) is adjacent to every nonzero vector of \(L^\perp\), and no two distinct vectors within either line are adjacent. The union therefore induces
\[
K_{s,s}.
\]

If
\[
L=L^\perp,
\]
then \(L\) is isotropic and its \(s\) nonzero vectors induce
\[
K_s.
\]

There are no edges between different orthogonality orbits. Thus \(TD_2(q)\) is a disjoint union of copies of \(K_s\) indexed by fixed projective lines and copies of \(K_{s,s}\) indexed by two-cycles of orthogonal complementation. If \(h\) is the number of fixed lines and \(b\) is the number of two-cycles, then
\[
h+2b=q+1.
\tag{1}
\]

For \(s\ge2\),
\[
\mathcal Z(K_s;u)=u^{s-1}(u+s),
\tag{2}
\]
because a zero forcing set in a clique omits at most one vertex.

Likewise,
\[
\mathcal Z(K_{s,s};u)=u^{2s-2}(u+s)^2.
\tag{3}
\]
Indeed, in a balanced complete bipartite graph a zero forcing set can leave at most one white vertex in each part, and every such choice forces.

The zero forcing polynomial is multiplicative over disjoint unions. Combining (1)–(3),
\[
\begin{aligned}
\mathcal Z(TD_2(q);u)
&=
\left(u^{s-1}(u+s)\right)^h
\left(u^{2s-2}(u+s)^2\right)^b\\
&=
u^{(h+2b)(s-1)}(u+s)^{h+2b}\\
&=
u^{(q+1)(q-2)}(u+q-1)^{q+1}.
\end{aligned}
\]
Hence
\[
Z(TD_2(q))=(q+1)(q-2)=q^2-q-2.
\]

The equality case in (2) omits one vector from each isotropic line. The equality case in (3) omits one vector from each side of every orthogonal pair. Therefore a minimum zero forcing set omits exactly one nonzero vector from every projective line. This gives
\[
(q-1)^{q+1}
\]
minimum zero forcing sets.

For minimum rank, a clique \(K_s\), \(s\ge2\), has real minimum rank \(1\), witnessed by the all-ones matrix. A balanced complete bipartite graph \(K_{s,s}\), \(s\ge2\), has real minimum rank \(2\), witnessed by
\[
\begin{pmatrix}
0&J\\
J&0
\end{pmatrix}.
\]
Rank \(1\) is impossible because a rank-one symmetric matrix with all cross-part entries nonzero would also create nonzero off-diagonal entries inside each part.

Minimum rank is additive over disjoint components because every graph-pattern matrix is block diagonal across components. Thus
\[
\operatorname{mr}(TD_2(q))
=
h+2b
=
q+1.
\]
Since \(TD_2(q)\) has \(q^2-1\) vertices,
\[
M(TD_2(q))
=
q^2-1-(q+1)
=
q^2-q-2
=
Z(TD_2(q)).
\]

For \(q=2\), the three projective lines each contain one nonzero vector. Orthogonal complementation has one fixed line and one two-cycle, giving
\[
TD_2(2)\cong K_1\dot\cup K_2.
\]
Therefore
\[
\mathcal Z(TD_2(2);u)=u(2u+u^2)=2u^2+u^3,
\]
and
\[
Z=M=2,\qquad \operatorname{mr}=1.
\]

## Verification

The accompanying `verify.py` constructs the graph directly from finite-field arithmetic for
\[
q=2,3,4,5.
\]
The \(q=4\) case uses
\[
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)
\]
rather than a prime-field shortcut.

For \(q\le4\), every vertex subset is exhaustively tested for the zero forcing property and the resulting polynomial is compared with the theorem. For all four fields, connected components are reconstructed from the direct dot-product graph and exact rational row reduction verifies the block minimum-rank witnesses.

Exact replay output:

```text
q=2: |V|=3, components=[1, 2], polynomial={2: 2, 3: 1}, witness_rank=1
q=3: |V|=8, components=[4, 4], polynomial={4: 16, 5: 32, 6: 24, 7: 8, 8: 1}, witness_rank=4
q=4: |V|=15, components=[3, 6, 6], polynomial={10: 243, 11: 405, 12: 270, 13: 90, 14: 15, 15: 1}, witness_rank=5
q=5: |V|=24, components=[4, 4, 8, 8], predicted_polynomial={18: 4096, 19: 6144, 20: 3840, 21: 1280, 22: 240, 23: 24, 24: 1}, witness_rank=6
VERIFY_OK
```

These finite checks are corroborative only. The arbitrary-prime-power proof is the projective orthogonality decomposition plus the componentwise polynomial and minimum-rank arguments.

## Relationship to prior work

Badawi introduced the total dot product graph and zero-divisor dot product graph of a commutative ring. The inspected published full text lists primary Mathematics Subject Classification \(13A15\), defines the exact graph used here, and contains no occurrence of “zero forcing” or “minimum rank.”

Abdulla and Badawi later give the full finite-field component decomposition in dimension two. In characteristic two, the total graph is one \(K_{q-1}\) together with \(q/2\) copies of \(K_{q-1,q-1}\). In odd characteristic, the number of clique components is controlled by whether \(-1\) is a square, with the remaining projective lines paired into balanced complete bipartite components. Their full text contains no occurrence of “zero forcing” or “minimum rank.”

Boyer and collaborators introduced the zero forcing polynomial and established general structural properties including multiplicativity. Those generic facts are prior coverage. The present result identifies the complete finite-field factorization, the projective-transversal minimizers, and the exact real minimum rank.

## Limitations

The theorem is for the two-dimensional total dot product graph over a finite field. It does not assert the same polynomial in dimensions \(n\ge3\), where the graph is connected and the projective orthogonality structure is substantially different.

The component decomposition itself is known from later finite-field dot-product work. The strengthened contribution is the exact zero forcing polynomial, the geometric classification of every minimum forcing set, and the matching real minimum-rank formula.

The minimum-rank statement is over real symmetric matrices.

For \(q=2\), singleton projective lines create a genuine boundary and the \(q\ge3\) factorization does not apply.

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188. Published online 1 August 2014.
2. M. Abdulla and A. Badawi, “On the Dot Product Graph of a Commutative Ring II,” *International Electronic Journal of Algebra* 28 (2020), 61–74. DOI: 10.24330/ieja.768135.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
