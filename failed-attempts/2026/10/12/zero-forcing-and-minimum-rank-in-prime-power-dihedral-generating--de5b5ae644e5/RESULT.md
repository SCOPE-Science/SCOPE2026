# Zero forcing and minimum rank in prime-power dihedral generating graphs

## Finding

Let \(p\) be an odd prime, \(k\ge1\), \(n=p^k\), and \(D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\). Let \(\Gamma(D_{2n})\) be the full generating graph on all group elements, where distinct vertices are adjacent when they generate \(D_{2n}\). Put \(m=p^{k-1}\). Then \[\Gamma(D_{2n})\cong mK_1\dot\cup K_{(p-1)m,m,\ldots,m},\]where the active complete multipartite component has \(p+1\) parts, one of size \((p-1)m\) and \(p\) of size \(m\). Its zero forcing polynomial is \[\mathcal Z(\Gamma(D_{2n});u)=C_{p,k}u^{2p^k-2}+(2p-1)p^{k-1}u^{2p^k-1}+u^{2p^k},\]where \(C_{p,1}=p(p-1)\) and, for \(k\ge2\), \[C_{p,k}=\frac32p(p-1)p^{2k-2}.\] Hence \(Z(\Gamma(D_{2n}))=2p^k-2\). Over real symmetric graph-pattern matrices, \[\operatorname{mr}(\Gamma(D_{2n}))=\begin{cases}2,&k=1,\\3,&k\ge2,\end{cases}\qquad M(\Gamma(D_{2n}))=\begin{cases}2p-2,&k=1,\\2p^k-3,&k\ge2.\end{cases}\]Thus \(M=Z\) exactly at the prime-order rotation boundary \(k=1\), while \(Z=M+1\) for every \(k\ge2\).

The minimum zero forcing sets also admit a complete description. When \(k=1\), they are exactly the complements of one generating rotation and one reflection. When \(k\ge2\), they are exactly the complements of two active vertices lying in different multipartite classes.

## Assumptions and scope

Let
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle
\]
have order \(2n\), with
\[
n=p^k,\qquad p\text{ odd prime},\qquad k\ge1.
\]

The generating graph \(\Gamma(D_{2n})\) has vertex set \(D_{2n}\), with two distinct elements adjacent exactly when they generate the whole group.

The archive ownership source used here defines the generating graph of a finite group and has primary Mathematics Subject Classification \(20D06\). The exact dihedral structural source is later supporting literature.

## Proof

Write the rotations as
\[
r^i,\qquad 0\le i<n,
\]
and the reflections as
\[
sr^j,\qquad 0\le j<n.
\]

Two rotations never generate the noncyclic group. A rotation and a reflection generate \(D_{2n}\) exactly when the rotation generates \(\langle r\rangle\):
\[
\langle r^i,sr^j\rangle=D_{2n}
\quad\Longleftrightarrow\quad
\gcd(i,n)=1.
\tag{1}
\]
Two reflections generate \(D_{2n}\) exactly when their product generates \(\langle r\rangle\):
\[
\langle sr^i,sr^j\rangle=D_{2n}
\quad\Longleftrightarrow\quad
\gcd(i-j,n)=1.
\tag{2}
\]

Put
\[
m=p^{k-1}.
\]
There are
\[
n-\varphi(n)=m
\]
rotations with nonunit exponent, and by (1) all of them are isolated. The generating rotations form an independent set
\[
A
\]
of size
\[
|A|=\varphi(n)=(p-1)m,
\]
joined to every reflection.

By (2), two reflections are adjacent exactly when their exponents are distinct modulo \(p\). Hence the reflections split into \(p\) independent sets
\[
B_0,\ldots,B_{p-1},
\qquad
|B_i|=m,
\]
with every pair of distinct \(B_i,B_j\) completely joined. Therefore
\[
\Gamma(D_{2n})
\cong
mK_1\dot\cup K_{(p-1)m,m,\ldots,m}.
\tag{3}
\]

Let \(H\) denote the active complete multipartite component. Every zero forcing set of the full graph must contain all \(m\) isolated vertices.

In a complete multipartite graph, two white vertices in the same part can never be separated by a first force, because they are false twins. Thus a zero forcing set leaves at most one white vertex in each part.

If three or more white vertices lie in distinct parts, every blue vertex sees at least two white neighbors, so no first force exists. Hence a zero forcing set leaves at most two active vertices white.

Now suppose exactly two active vertices are white and lie in distinct parts. If at least one of those two parts has another blue vertex, that blue vertex is nonadjacent to the white vertex in its own part and adjacent to the other white vertex, so it forces the latter. The remaining white vertex is then forced in one further step. Conversely, if both white vertices lie in singleton parts, neither part contains such a blue vertex and every blue vertex sees both whites, so the coloring stalls.

When \(k=1\), the part \(A\) has size \(p-1\ge2\), while the \(p\) reflection parts are singletons. Thus the minimum zero forcing sets are exactly the complements of one vertex of \(A\) and one reflection. Their number is
\[
p(p-1).
\tag{4}
\]

When \(k\ge2\), every part has size at least \(3\), so every pair of white vertices in distinct parts is forceable. The number of such pairs is
\[
|A|\sum_i|B_i|
+
\sum_{i<j}|B_i||B_j|.
\]
Using
\[
|A|=(p-1)m,\qquad |B_i|=m,
\]
this is
\[
p(p-1)m^2+\binom p2m^2
=
\frac32p(p-1)m^2.
\tag{5}
\]

The active component has
\[
(2p-1)m
\]
vertices. Every active set missing exactly one vertex is zero forcing, while a full active set is zero forcing. Multiplying by the compulsory factor from the \(m\) isolates gives
\[
\mathcal Z(\Gamma(D_{2n});u)
=
C_{p,k}u^{2p^k-2}
+
(2p-1)p^{k-1}u^{2p^k-1}
+
u^{2p^k},
\]
with \(C_{p,k}\) given by (4) and (5). Hence
\[
Z(\Gamma(D_{2n}))=2p^k-2.
\]

It remains to determine real symmetric minimum rank. Isolated vertices can be represented by zero rows and columns, so they do not increase minimum rank.

Assume first \(k=1\). The active graph is
\[
K_{p-1,1,\ldots,1}.
\]
Use the symmetric bilinear form
\[
B=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
Assign \((1,0)\) to every vertex in the \((p-1)\)-vertex part and \((1,1)\) to every singleton reflection part. Inner products vanish exactly inside the nontrivial part and are nonzero on every edge. This gives rank at most \(2\). A connected graph has real symmetric minimum rank \(1\) only when it is complete, while the active graph is not complete. Therefore
\[
\operatorname{mr}(\Gamma(D_{2p}))=2.
\]

Now assume \(k\ge2\). Use the Lorentz form
\[
B=\operatorname{diag}(1,1,-1).
\]
For the \(p+1\) multipartite classes choose distinct integers \(t\) and assign every vertex in class \(t\) the vector
\[
v_t=(1-t^2,\,2t,\,1+t^2).
\]
Then
\[
v_t^{\mathsf T}Bv_t=0
\]
and, for \(t\ne u\),
\[
v_t^{\mathsf T}Bv_u=-2(t-u)^2\ne0.
\]
Thus the associated symmetric matrix has exactly the required off-diagonal graph pattern and rank \(3\).

Rank \(2\) is impossible. Indeed, in any rank-two symmetric factorization with a nonsingular bilinear form on \(\mathbb R^2\), the at least three vertices in one multipartite part must lie on one isotropic line: if two were linearly independent, a third vector orthogonal to both would be zero, contradicting its nonzero adjacencies outside the part. A nondegenerate symmetric form on \(\mathbb R^2\) has at most two isotropic lines, but here there are \(p+1\ge4\) multipartite parts. Two parts would therefore share an isotropic line, making all cross products between them zero, contradicting their complete adjacency. Hence
\[
\operatorname{mr}(\Gamma(D_{2p^k}))=3
\qquad(k\ge2).
\]

Since the graph has \(2p^k\) vertices,
\[
M=2p^k-\operatorname{mr},
\]
which gives the stated maximum-nullity formulas and the strict gap
\[
Z=M+1
\]
for every \(k\ge2\).

## Verification

The accompanying `verify.py` constructs the dihedral generating graph directly from the two-generator criteria (1) and (2).

For
\[
(p,k)=(3,1),(5,1),(3,2),
\]
it exhaustively enumerates every vertex subset and reproduces the entire zero forcing polynomial.

For larger representative cases
\[
(3,3),(5,2),(7,2),
\]
it verifies the isolated-rotation count, multipartite class sizes, all one-white and cross-part two-white forcing profiles, and a three-white stalled profile.

The rank-two and rank-three witnesses are checked entry-by-entry against the graph pattern, and their ranks are computed by exact rational row reduction.

Exact replay output:

```text
p=3, k=1, order=6, polynomial={4: 6, 5: 5, 6: 1}, witness_rank=2
p=5, k=1, order=10, polynomial={8: 20, 9: 9, 10: 1}, witness_rank=2
p=3, k=2, order=18, polynomial={16: 81, 17: 15, 18: 1}, witness_rank=3
p=3, k=3, structural_profiles_ok, witness_rank=3
p=5, k=2, structural_profiles_ok, witness_rank=3
p=7, k=2, structural_profiles_ok, witness_rank=3
VERIFY_OK
```

The finite computations corroborate the proof but do not replace the arbitrary-prime-power argument.

## Relationship to prior work

Lucchini, Maróti, and Roney-Dougal use the generating graph of a finite group as a group-theoretic invariant. Their paper was first published online on 26 September 2016 and lists primary Mathematics Subject Classification \(20D06\).

Reddy and Samant later analyze the generating graph of every finite dihedral group. Their full public preprint describes the rotation/reflection decomposition, the unit-difference adjacency among reflections, and the prime-power equitable classes; it determines adjacency and Laplacian spectra and graph indices. A full-text search found no occurrence of “zero forcing.”

General zero forcing theory already covers the standard inequality
\[
M(G)\le Z(G),
\]
and zero forcing numbers for complete multipartite graphs are part of the broader literature. The strengthened content here is the complete zero forcing polynomial of the full dihedral generating graph including its compulsory isolated vertices, the exact classification of all minimum sets, and the sharp real minimum-rank transition
\[
2\longrightarrow3
\]
between \(k=1\) and \(k\ge2\), producing a natural infinite family with \(Z=M+1\).

Targeted searches under “generating graph,” “dihedral,” “prime power,” “zero forcing polynomial,” “maximum nullity,” “minimum rank,” and complete-multipartite aliases did not locate this combined statement.

## Limitations

The theorem assumes that \(p\) is odd and \(n=p^k\). The case \(p=2\) belongs to the two-generated finite \(2\)-group regime and has broader prior coverage.

For general composite \(n\) with at least two distinct prime factors, the reflection subgraph is a unitary Cayley graph rather than a single complete multipartite graph of the form used here.

The minimum-rank statement uses real symmetric graph-pattern matrices.

The complete-multipartite zero forcing number itself is not claimed as standalone novelty. The contribution is the full generating-graph polynomial, the exact minimizer classification with the prime boundary, and the minimum-rank/nullity comparison on the dihedral prime-power family.

## References

1. A. Lucchini, A. Maróti, and C. M. Roney-Dougal, “On the generating graph of a simple group,” *Journal of the Australian Mathematical Society* 103 (2017), 91–103. DOI: 10.1017/S1446788716000458. First published online 26 September 2016.
2. A. Satyanarayana Reddy and K. Samant, “Generating Graphs of Finite Dihedral Groups,” arXiv:2307.11802, first posted 21 July 2023; *Results in Mathematics* (2023). DOI: 10.1007/s00025-023-01963-x.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910; *Discrete Applied Mathematics* 258 (2019), 35–48.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
