# Laplacian spectrum and tree complexity of the dihedral noncyclic graph

## Finding

Let \(D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) with \(n\ge3\), and let \(\mathcal N(D_{2n})\) be its noncyclic graph on \(D_{2n}\setminus\operatorname{Cyc}(D_{2n})\), where distinct vertices are adjacent when they generate a noncyclic subgroup. Then \[\mathcal N(D_{2n})\cong K_n\vee \overline{K_{n-1}},\] its Laplacian spectrum is \[\{0^{(1)},\ n^{(n-2)},\ (2n-1)^{(n)}\},\] its number of spanning trees is \[\tau(\mathcal N(D_{2n}))=n^{n-2}(2n-1)^{n-1},\] and its Kirchhoff index is \[\operatorname{Kf}(\mathcal N(D_{2n}))=3n-5+\frac{2}{n}.\]

Thus the noncyclic graph of every dihedral group has an exact complete-split model, and two global Laplacian invariants follow in closed form for the whole family.

## Assumptions and scope

Let
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\qquad n\ge3.
\]
For a group \(G\), define
\[
\operatorname{Cyc}(G)=\{x\in G:\langle x,y\rangle\text{ is cyclic for every }y\in G\}.
\]
The noncyclic graph \(\mathcal N(G)\) has vertex set \(G\setminus\operatorname{Cyc}(G)\) and joins distinct \(x,y\) exactly when \(\langle x,y\rangle\) is noncyclic.

The Laplacian spectrum lists eigenvalues with multiplicity. The spanning-tree number is denoted \(\tau\), and the Kirchhoff index is
\[
\operatorname{Kf}(X)=|V(X)|\sum_{\lambda\ne0}\lambda^{-1}
\]
for a connected graph \(X\), where the sum ranges over nonzero Laplacian eigenvalues with multiplicity.

## Proof

First,
\[
\operatorname{Cyc}(D_{2n})=\{1\}.
\]
Indeed, every nonidentity rotation \(r^a\) together with any reflection \(s\) generates a noncyclic dihedral subgroup (or, in the order-two rotation case, a noncyclic Klein four subgroup). Likewise, every reflection together with a nontrivial rotation generates a noncyclic subgroup. Hence no nonidentity element lies in the cyclicizer.

The vertices therefore split into the \(n-1\) nonidentity rotations and the \(n\) reflections. Any two rotations generate a subgroup of \(\langle r\rangle\), hence are nonadjacent in the noncyclic graph. A rotation and a reflection generate a noncyclic subgroup, hence are adjacent. Finally, two distinct reflections cannot generate a cyclic group: each has order two, and a cyclic group has at most one element of order two. Thus the reflections form a clique. Therefore
\[
\mathcal N(D_{2n})\cong K_n\vee\overline{K_{n-1}}.
\tag{1}
\]

Put \(N=2n-1\). For a join \(K_n\vee\overline{K_{n-1}}\), vectors supported on the independent side with coordinate sum zero have Laplacian eigenvalue \(n\), giving multiplicity \(n-2\). Vectors supported on the clique side with coordinate sum zero have eigenvalue \(N\), giving multiplicity \(n-1\). The remaining two-dimensional space of vectors constant on each side contributes eigenvalues \(0\) and \(N\). Hence
\[
\operatorname{Spec}_L(\mathcal N(D_{2n}))=
\{0^{(1)},\ n^{(n-2)},\ (2n-1)^{(n)}\}.
\tag{2}
\]

By the Matrix-Tree Theorem,
\[
\tau(\mathcal N(D_{2n}))
=\frac1{2n-1}n^{n-2}(2n-1)^n
=n^{n-2}(2n-1)^{n-1}.
\]

The spectral formula for the Kirchhoff index gives
\[
\operatorname{Kf}(\mathcal N(D_{2n}))
=(2n-1)\left(\frac{n-2}{n}+\frac{n}{2n-1}\right)
=3n-5+\frac2n.
\]

## Verification

The standalone checker constructs \(D_{2n}\) from the presentation, computes generated subgroups directly, verifies that the cyclicizer is exactly \(\{1\}\), builds the noncyclic graph, and checks the complete-split decomposition.

For \(3\le n\le8\), it computes the exact Laplacian spectrum, a Matrix-Tree cofactor determinant, and the Kirchhoff-index spectral sum.

Exact output:

```text
n=3 vertices=5 spectrum=0^1,3^1,5^3 trees=75 Kf=14/3
n=4 vertices=7 spectrum=0^1,4^2,7^4 trees=5488 Kf=15/2
n=5 vertices=9 spectrum=0^1,5^3,9^5 trees=820125 Kf=52/5
n=6 vertices=11 spectrum=0^1,6^4,11^6 trees=208722096 Kf=40/3
n=7 vertices=13 spectrum=0^1,7^5,13^7 trees=81124178863 Kf=114/7
n=8 vertices=15 spectrum=0^1,8^6,15^8 trees=44789760000000 Kf=77/4
VERIFY_OK
```

The finite calculations are corroborative only. The arbitrary-\(n\) result follows from the structural decomposition (1).

## Relationship to prior work

Abdollahi and Mohammadi Hassanabadi introduced the noncyclic graph and studied structural group-theoretic consequences, with primary classification in finite group theory.

Ma, Wei, and Zhong later studied the complementary cyclic graph in full detail for dihedral groups. Their Theorem 28 shows that distinct reflections have no cyclic-graph edge and that nonidentity rotations form the nontrivial cyclic part; equivalently, after deleting the identity, the complementary noncyclic graph has the complete-split structure in (1).

Targeted searches for the dihedral noncyclic graph together with “Laplacian spectrum,” “spanning tree,” “tree number,” and “Kirchhoff index” did not locate the formulas (2) or the two consequences above. Papers on the Laplacian spectrum of the **noncommuting** graph of a dihedral group concern a different adjacency relation and do not imply this result.

## Limitations

The theorem concerns the noncyclic graph, not the cyclic graph or noncommuting graph.

No corresponding claim is made for generalized quaternion, semidihedral, or arbitrary metacyclic groups.

The checker covers only \(3\le n\le8\); it is not used as an infinite proof.

## References

1. A. Abdollahi and A. Mohammadi Hassanabadi, “Noncyclic Graph of a Group,” *Communications in Algebra* 35 (2007), 2057–2081. DOI: 10.1080/00927870701302081.
2. X. L. Ma, H. Q. Wei, and G. Zhong, “The Cyclic Graph of a Finite Group,” *Algebra* 2013 (2013), Article 107265. DOI: 10.1155/2013/107265.
