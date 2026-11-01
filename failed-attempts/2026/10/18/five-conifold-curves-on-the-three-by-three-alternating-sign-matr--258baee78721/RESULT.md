# Five conifold curves on the three-by-three alternating-sign-matrix toric fourfold

## Finding

Let \(P=\operatorname{ASM}_3\) be the convex hull of the seven \(3\times 3\) alternating sign matrices in the affine lattice of integer matrices with every row and column sum equal to one. Let \(X_P\) be the projective normal toric fourfold whose fan is the **normal fan** of \(P\), over any algebraically closed field \(k\). For a face \(E\subset P\), write \(V(E)\) for the closure of the torus orbit of the normal cone of \(E\).

Label the six permutation-matrix vertices by their zero-indexed row-to-column permutations \(012,021,102,120,201,210\), and the seventh vertex by \(X\), corresponding to the matrix
\[
\begin{pmatrix}0&1&0\\1&-1&1\\0&1&0\end{pmatrix}.
\]
Moreover, there is an explicit **unimodular affine equivalence** from \(P\) to the stable-set polytope of the four-cycle \(C_4=K_{2,2}\). In particular, the seven ASM vertices correspond to the empty stable set, the four singleton stable sets, and the two stable pairs of opposite vertices. Under this equivalence the entire **reduced** singular support is
\[
\operatorname{Sing}(X_P)_{\mathrm{red}}
=V([012,021])\cup V([012,102])\cup V([012,210])
 \cup V([210,120])\cup V([210,201]).
\]
These are precisely five distinct irreducible torus-invariant curves, each isomorphic to \(\mathbb P^1_k\). Their incidence graph is the tree with edge set
\[
\{012\! -\! 021,\ 012\! -\! 102,\ 012\! -\! 210,\ 210\! -\! 120,\ 210\! -\! 201\}.
\]
Thus three curves meet at the torus-fixed point for \(012\), three meet at the torus-fixed point for \(210\), and there are no other intersections of distinct listed curves. At a general point of each curve the transverse toric germ is the ordinary threefold node
\[
\operatorname{Spec} k[a,b,c,d]/(ab-cd).
\]
The singular locus is pure one-dimensional (codimension three). Moreover, the non-\(\mathbb Q\)-factorial locus agrees with this reduced singular support set-theoretically.

## Assumptions and scope

The coordinate lattice is \(M\cong\mathbb Z^4\), obtained by retaining the northwest \(2\times2\) block \((x_{11},x_{12},x_{21},x_{22})\); the remaining entries are determined integrally by the row/column-sum-one conditions. The seven vertices in this chart are
\[
\begin{array}{c|c@{\qquad}c|c}
012&(1,0,0,1)&021&(1,0,0,0)\\
102&(0,1,1,0)&120&(0,1,0,0)\\
201&(0,0,1,0)&210&(0,0,0,1)\\
X&(0,1,1,-1)&&
\end{array}.
\]
The normal-fan convention is essential: this is not a claim about the toric variety of the fan over the faces of \(P\), nor about the Birkhoff polytope. The ground field may have any characteristic; no scheme-theoretic description of the Jacobian singular subscheme is asserted.

## Proof

**1. A cross-model integral equivalence.** Use \(X=(0,1,1,-1)\) as origin and order the four vertices \(021,102,120,201\) as coordinate vectors. The matrix whose columns are their differences from \(X\) is
\[
T=\begin{pmatrix}
1&0&0&0\\
-1&0&0&-1\\
-1&0&-1&0\\
1&1&1&1
\end{pmatrix},\qquad\det T=-1.
\]
The inverse integral affine map \(v\mapsto T^{-1}(v-X)\) sends \(X\) to \(0\), sends \(021,102,120,201\) to \(e_1,e_2,e_3,e_4\), and sends \(012\) to \(e_1+e_2\) and \(210\) to \(e_3+e_4\). These are precisely the seven stable-set indicator vectors of the cycle graph whose two bipartition classes are \(\{1,2\}\) and \(\{3,4\}\). As \(T\in\operatorname{GL}_4(\mathbb Z)\), this equivalence preserves the lattice normal fan, not merely its combinatorial type.

**2. Complete facet description.** In the dual lattice \(N=M^\vee\cong\mathbb Z^4\), the eight outward primitive facet normals \(n_i\), supporting constants \(c_i\) in \(\langle n_i,x\rangle\le c_i\), and sets of incident vertices are as follows. The first six vertex labels denote permutation matrices, and \(X\) denotes the exceptional ASM.

| Facet | \(n_i\) | \(c_i\) | Incident vertices |
|---|---|---:|---|
| \(0\) | \((1,1,0,0)\) | \(1\) | \(012,021,102,120,X\) |
| \(1\) | \((1,0,1,0)\) | \(1\) | \(012,021,102,201,X\) |
| \(2\) | \((0,0,-1,0)\) | \(0\) | \(012,021,120,210\) |
| \(3\) | \((0,-1,0,0)\) | \(0\) | \(012,021,201,210\) |
| \(4\) | \((0,1,0,1)\) | \(1\) | \(012,102,120,210\) |
| \(5\) | \((0,0,1,1)\) | \(1\) | \(012,102,201,210\) |
| \(6\) | \((-1,-1,-1,-1)\) | \(-1\) | \(021,120,201,210,X\) |
| \(7\) | \((-1,0,0,0)\) | \(0\) | \(102,120,201,210,X\) |

Each row is checked directly against all seven vertices; its incident vertices affinely span dimension three. These are all the facets: Striker's facet theorem gives \(4((3-2)^2+1)=8\), and independently the exact enumeration of all affine-independent four-vertex supports in the companion checker returns precisely these eight. Thus there are no unlisted rays in any normal cone.

**3. Exhaustive face and lattice analysis.** Every nonempty face is the intersection of the facets containing it. Intersecting the eight explicit vertex-support sets yields the face counts \((f_0,f_1,f_2,f_3)=(7,17,18,8)\). For any face \(F\) of dimension \(d\), its normal cone is generated by exactly the normals of the facets containing \(F\) and has dimension \(4-d\). A cone with exactly \(4-d\) primitive rays is smooth precisely when the gcd of its maximal minors in a \((4-d)\)-by-\(4\) ray matrix is one. This is the saturated-lattice basis criterion, valid for every \(d\).

The complete exact check gives the following table.

| Face dimension \(d\) | Total faces | Smooth normal cones | Nonsmooth normal cones |
|---|---:|---:|---:|
| \(0\) | \(7\) | \(1\) | \(6\) |
| \(1\) | \(17\) | \(12\) | \(5\) |
| \(2\) | \(18\) | \(18\) | \(0\) |
| \(3\) | \(8\) | \(8\) | \(0\) |

All five nonsmooth edge cones have four extremal rays in rank three; the other twelve edge cones have three saturated primitive generators. The eight faces of dimension three and all eighteen of dimension two likewise have smooth cones. Only the vertex \(X\) has a smooth maximal cone. The other six vertices lie on at least one of the five nonsmooth edges below. Therefore no isolated singular torus-fixed points or other singular orbit closures are left over.

Explicitly the twelve *smooth* edges are
\[
\begin{split}
&[201,X], [021,X], [021,120], [102,210], [120,X], [102,201],\\
&[012,201], [021,210], [012,120], [021,201], [102,120], [102,X].
\end{split}
\]
Together with the five nonsmooth edges these exhaust all seventeen edges, and the attached exact-arithmetic checker provides a reproducible finite proof of all the face intersections and lattice gcd assertions.

**4. Transverse type on every nonsmooth edge.** The four active facets at the five edges, in the order of the table above, are:
\[
\begin{array}{c|c|c}
\text{edge}&\text{active normals}&\text{primitive relation}\\\hline
[012,021]&n_0,n_1,n_2,n_3&n_0+n_3=n_1+n_2\\
[012,102]&n_0,n_1,n_4,n_5&n_0+n_5=n_1+n_4\\
[012,210]&n_2,n_3,n_4,n_5&n_2+n_5=n_3+n_4\\
[210,120]&n_2,n_4,n_6,n_7&n_2+n_7=n_4+n_6\\
[210,201]&n_3,n_5,n_6,n_7&n_3+n_7=n_5+n_6
\end{array}.
\]
For each row, all four triples of the listed rays are saturated in their rank-three span: the gcd of each triple's \(3\times3\) minors in \(\mathbb Z^4\) is \(1\). Thus an integral change of basis identifies the cone with the cone over a unit lattice square. The toric affine variety of that cone is the ordinary threefold determinantal node \(ab-cd=0\). Along the associated one-dimensional torus orbit, this is the generic transverse singularity; it is singular in every characteristic.

**5. Components and incidence.** In a normal toric variety, the singular support is the union of orbit closures for nonsmooth cones. A normal cone of an edge of a four-dimensional polytope has dimension three, so its orbit closure is a projective one-dimensional normal toric variety, hence \(\mathbb P^1\). The five nonsmooth edges are inclusion-maximal among nonsmooth faces, so their orbit closures are precisely the five irreducible components of the reduced singular support. Two invariant edge curves intersect only at fixed points of common endpoints. Their edge-incidence graph is exactly the stated tree. Finally, all nonsmooth cones here are nonsimplicial, and all simplicial cones are smooth; hence the non-\(\mathbb Q\)-factorial locus coincides set-theoretically with the singular locus.

## Verification

Run `python3 VERIFY_COMPUTATION.py` from this directory. The script uses only the Python standard library and exact integer/fraction arithmetic. It exhausts every independent four-vertex supporting hyperplane; derives all \(8\) facets and their face intersections; verifies the \((7,17,18,8)\) face vector; tests smoothness using saturated-lattice minor gcds; isolates the five nonsmooth edges and checks the four-ray square relation and saturated triples for each. Its expected terminal marker is `VERIFY_OK`.

The finite enumeration is exhaustive for the specified seven-vertex polytope, not an extrapolation to other matrix sizes. The algebraic geometry then follows from the standard toric orbit-cone correspondence and the explicitly certified normal cones.

## Relationship to prior work

Striker [1] defines the alternating-sign-matrix polytope, gives its inequality description and face-lattice method, and proves the facet-count theorem used here. Behrend--Knight [2] establish the integral-polytope and higher-spin lattice-point context, including special results for size three. Mészáros--Morales--Striker [3] study specified faces and their descriptions as order and flow polytopes. The new claim concerns the **integral identification with the stable-set polytope of the four-cycle and the normal-fan toric fourfold's complete singular curves and their transverse analytic types**; it is not a new enumeration of alternating sign matrices, facets or lattice points.

The unimodular equivalence to the four-cycle stable-set polytope is explicitly accounted for here: the statement can equally be read as a classification for that normal-fan toric fourfold. Thus an independent established classification for that graph would imply the toric portion of the claim, and the distinguishing element would be the explicit integral ASM--graph correspondence. The Birkhoff polytope of permutation matrices is a proper subpolytope with a different facet structure; a singularity classification for its toric variety does not imply the present result. The earlier works' methods offer necessary combinatorial background, but none of the inspected relevant sections provides the asserted toric singular-locus classification.

## Limitations

No classification for \(\operatorname{ASM}_n\) with \(n>3\) is claimed. The theorem classifies the reduced singular *support*; it does not compute the nonreduced Jacobian singular scheme or complete analytic germs at the two triple-intersection fixed points. The conifold statement applies transversely at general points of each curve. Standard toric correspondence is used for the implication from cone smoothness to singular support. Equivalent coverage implicit in unlocated literature cannot be excluded absolutely.

## References

[1] Jessica Striker, *The Alternating Sign Matrix Polytope*, arXiv:0705.0998 (first posted 2007-05-07), Electron. J. Combin. **16** (2009), R41. https://arxiv.org/abs/0705.0998

[2] Roger E. Behrend and Vincent A. Knight, *Higher Spin Alternating Sign Matrices*, arXiv:0708.2522 (first posted 2007-08-20), Electron. J. Combin. **14** (2007), R83. https://arxiv.org/html/0708.2522v2

[3] Karola Mészáros, Alejandro H. Morales, and Jessica Striker, *On Flow Polytopes, Order Polytopes, and Certain Faces of the Alternating Sign Matrix Polytope*, arXiv:1510.03357 (first posted 2015-10-12), Discrete Comput. Geom. **62** (2019), 128–163. https://arxiv.org/abs/1510.03357
