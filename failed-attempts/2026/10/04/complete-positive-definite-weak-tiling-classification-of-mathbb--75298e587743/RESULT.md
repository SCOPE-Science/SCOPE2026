# Complete positive-definite weak-tiling classification of \((\mathbb Z/2\mathbb Z)^3\)
## Finding
Let
\[
G=(\mathbb Z/2\mathbb Z)^3.
\]
A nonempty subset \(A\subset G\) pd-tiles \(G\) weakly if and only if
\[
|A|\in\{1,2,4,8\}.
\]
For each of these four cardinalities every subset is a translational tile. Consequently every positive-definite weak tile of \(G\) is a translational tile, so \(G\) is pd-flat.

## Assumptions and scope
A set \(A\subset G\) pd-tiles \(G\) weakly when there is a function \(h:G\to\mathbb R\) satisfying
\[
h\ge0,\qquad h(0)=1,\qquad 1_A*h=1_G,\qquad \widehat h\ge0.
\]
The Fourier transform is the unnormalized character sum. The claim concerns all nonempty subsets of the eight-element group \(G\); it makes no assertion for other elementary abelian groups.

## Proof
Assume first that \(A\) pd-tiles weakly with witness \(h\). Summing the convolution identity over \(G\) gives
\[
|A|\sum_{x\in G}h(x)=8,
\]
so
\[
\sum_{x\in G}h(x)=\frac{8}{|A|}.
\]
The standard support obstruction for positive-definite weak tiling is
\[
(A-A)\cap\operatorname{supp}h=\{0\}.
\]

Suppose \(5\le |A|\le7\). For every \(x\in G\), both \(A\) and \(A+x\) contain more than half of \(G\), hence they intersect. Therefore \(x\in A-A\), so \(A-A=G\). The support obstruction forces \(h=\delta_0\), but then \(1_A*h=1_A\ne1_G\), a contradiction.

It remains to exclude \(|A|=3\). Translate \(A\) so that \(0\in A\); translation preserves the property in question. Then
\[
A=\{0,a,b\}
\]
with \(a,b\) linearly independent. Hence
\[
S=A-A=\{0,a,b,a+b\}
\]
is a two-dimensional subspace. The support obstruction gives \(h(x)=0\) for every \(x\in S\setminus\{0\}\). Let \(\chi\) be the nontrivial real character with kernel \(S\). Thus \(\chi=1\) on \(S\) and \(\chi=-1\) on its complementary coset. Since \(h(0)=1\) and \(\sum h=8/3\),
\[
\widehat h(\chi)
=1-\sum_{x\notin S}h(x)
=1-\left(\frac83-1\right)
=-\frac23<0,
\]
contradicting \(\widehat h\ge0\). Therefore a pd-weak tile can have only cardinality \(1,2,4\), or \(8\).

Conversely, every subset of these four cardinalities tiles. Cardinalities \(1\) and \(8\) are immediate. If \(|A|=2\), translate to \(A=\{0,d\}\) with \(d\ne0\), and choose a two-dimensional subspace \(H\) not containing \(d\); then
\[
G=A\oplus H.
\]
If \(|A|=4\), translate so \(0\in A\). When \(A\) spans a two-dimensional subspace, it equals that subspace and tiles with any complementary line. Otherwise
\[
A=\{0,a,b,c\}
\]
for a basis \(a,b,c\) of \(G\). Put \(t=a+b+c\). Then
\[
A+t=\{a+b+c,b+c,a+c,a+b\}=G\setminus A,
\]
so
\[
G=A\oplus\{0,t\}.
\]

Finally, a translational tiling \(A\oplus B=G\), after translating \(B\) so that \(0\in B\), yields an explicit pd-weak witness
\[
h=\frac{1_B*1_{-B}}{|B|}.
\]
Indeed \(h\ge0\), \(h(0)=1\),
\[
\widehat h=\frac{|\widehat{1_B}|^2}{|B|}\ge0,
\]
and
\[
1_A*h=\frac{(1_A*1_B)*1_{-B}}{|B|}=1_G.
\]
Thus the four allowed cardinalities are exactly the pd-weak tiling cardinalities.

## Verification
The accompanying `verify.py` enumerates all \(255\) nonempty subsets of \(G\). It checks exactly, using bitwise addition in \((\mathbb Z/2\mathbb Z)^3\), that every subset of cardinality \(1,2,4\), or \(8\) is a translational tile; every subset of cardinality \(5,6\), or \(7\) has full difference set; and every three-point subset translates to a two-dimensional difference subspace with the Fourier obstruction \(-2/3\). The script prints `VERIFY_OK`.

The computation is exhaustive for this finite group, while the proof above explains the structural reason for every case.

## Relationship to prior work
Kiss, Matolcsi, Matolcsi, and Somlai introduced pd-weak tiling and the notion of a pd-flat finite abelian group. They proved pd-flatness for elementary \(p\)-groups in dimensions \(1\) and \(2\), and for dimension \(3\) stated pd-flatness as a conjectural direction while proving only a partial structural result. The present theorem settles the first three-dimensional prime case, \(p=2\), completely and gives the stronger cardinality classification of every pd-weak tile in that group.

Later work on weak tiling supplies examples showing that weak tiling without the positive-definiteness restriction can behave differently, and recent work on cyclic groups of order \(pq\) proves tile/weak-tile equivalences in a different class of groups. Neither inspected direction contains the eight-element elementary abelian classification proved here.

## Limitations
The argument exploits the special cardinality and character geometry of \((\mathbb Z/2\mathbb Z)^3\). It does not settle pd-flatness for \((\mathbb Z/p\mathbb Z)^3\) when \(p\) is odd, nor does it classify general weak tiles without positive definiteness. Targeted searches found no prior statement of the exact eight-element classification, but differently phrased or non-indexed literature remains a residual originality risk.

## References
1. G. Kiss, D. Matolcsi, M. Matolcsi, and G. Somlai, “Tiling and weak tiling in \((\mathbb Z_p)^d\),” *Sampling Theory, Signal Processing, and Data Analysis* 22 (2024), Article 1. arXiv:2212.05513. DOI: 10.1007/s43670-023-00073-7.
2. G. Kiss, I. Londner, M. Matolcsi, and G. Somlai, “A lonely weak tile,” arXiv:2410.04948.
3. M. Kadir and K. Fan, “Tiles and weak tiles in \(\mathbb Z_{pq}\),” arXiv:2607.02149.
