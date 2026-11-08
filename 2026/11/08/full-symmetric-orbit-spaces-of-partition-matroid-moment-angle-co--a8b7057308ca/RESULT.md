# Full symmetric orbit spaces of partition-matroid moment-angle complexes

## Finding
Let \(t\ge 1\), let \(p_1,\ldots,p_t\ge1\) be integers, and let \(D_p\) denote the zero-dimensional simplicial complex with precisely \(p\) vertices and all their singleton faces. Form the partition-matroid independence complex
\[
K=D_{p_1}*D_{p_2}*\cdots*D_{p_t}.
\]
For each \(p\ge1\) put \(m_p=|\{i:p_i=p\}|\). Let \(Z_K=(D^2,S^1)^K\) be the complex moment-angle space with the natural action of the full simplicial automorphism group \(\operatorname{Aut}(K)\) by coordinate permutations. The **ordinary topological orbit space** has the homotopy type
\[
\boxed{\quad Z_K/\operatorname{Aut}(K)\simeq
\prod_{\substack{p\ge2\\m_p>0}}\operatorname{SP}^{m_p}(S^3).\quad}
\]
An empty product means a point. Here \(\operatorname{SP}^m(Y)=Y^m/S_m\) is the ordinary finite symmetric product, not a homotopy-orbit construction. In particular its rational cohomology algebra is
\[
H^*(Z_K/\operatorname{Aut}(K);\mathbb Q)
\cong\bigwedge_{\mathbb Q}(u_p:p\ge2,\ m_p>0),\qquad |u_p|=3.
\]
Thus the rational Poincaré polynomial is \((1+z^3)^d\), where \(d\) is the number of distinct block cardinalities greater than one. The homotopy-type assertion is integral (not merely rational) and retains the symmetric powers even when their rational cohomology agrees with a sphere.

## Assumptions and scope
All simplicial complexes are finite, blocks are nonempty and pairwise disjoint, and the disk and circle in the polyhedral product are the standard closed unit disk and its boundary. The group is the full group of vertex permutations preserving faces of \(K\). It is **not** the torus acting by coordinatewise phases, and the quotient is the literal orbit space, including fixed-point orbits. No freeness, genericity, or orientation assumption is imposed. The full action may have nontrivial stabilizers.

## Proof

**1. Automorphisms and the product decomposition.** A pair of vertices fails to be a face of \(K\) precisely when its two vertices lie in the same block of size at least two. Hence the graph of minimal nonfaces is a disjoint union of complete graphs of orders \(p_i\ge2\), together with isolated vertices from singleton blocks. Each component and its size are determined intrinsically by \(K\). Consequently
\[
\operatorname{Aut}(K)\cong S_{m_1}\times
\prod_{\substack{p\ge2\\m_p>0}}(S_p\wr S_{m_p}).
\]
The defining union of a polyhedral product on a simplicial join is a Cartesian product, so \(Z_K\cong\prod_{i=1}^t Z_{D_{p_i}}\), compatibly with this action. In particular, quotienting first by coordinate permutations *inside* each block and then by the permutations of equal-size blocks is exact and gives a homeomorphism
\[
Z_K/\operatorname{Aut}(K)\cong
\prod_{\substack{p\ge1\\m_p>0}}
\operatorname{SP}^{m_p}(Y_p),\qquad
Y_p:=Z_{D_p}/S_p.
\]
This requires no equivariant homotopy splitting.

**2. The single-block quotient.** Clearly \(Y_1=D^2\). Fix \(p\ge2\). A point of \(Z_{D_p}\) is a tuple of \(p\) disk coordinates of which at most one lies in the open disk. After passage to unordered coordinates, the locus having one marked disk coordinate is
\(B=D^2\times\operatorname{SP}^{p-1}(S^1)\); the locus with all coordinates on the circle is \(A=\operatorname{SP}^{p}(S^1)\). Their boundary identification is the multiplication-of-multisets map
\[
\mu:C=S^1\times\operatorname{SP}^{p-1}(S^1)\longrightarrow A,
\quad (w,\{z_1,\ldots,z_{p-1}\})\longmapsto\{w,z_1,\ldots,z_{p-1}\}.
\]
The other map \(C\hookrightarrow B\) is the boundary inclusion on the disk factor. Therefore the square \(C\xrightarrow{\mu}A\), \(C\hookrightarrow B\), with its common image in \(Y_p\), is a strict pushout. To check this even when boundary entries repeat, note that the pushout is a continuous bijection onto the orbit-space subset of \(\operatorname{SP}^p(D^2)\); it is compact with Hausdorff target. Thus it is a homeomorphism. Since \(C\hookrightarrow B\) is a cofibration, it is also a homotopy pushout.

**3. Homotopy calculation of \(Y_p\).** Morton's disk-bundle description of finite symmetric products of the circle says that the map
\[
\pi_q:\operatorname{SP}^q(S^1)\longrightarrow S^1,
\qquad\{z_1,\ldots,z_q\}\longmapsto \prod_{j=1}^q z_j
\]
is a homotopy equivalence for every \(q\ge1\). For completeness, one can prove this without assuming a fiber calculation: the radial deformation retraction \(S^1\hookrightarrow\mathbb C^\times\) induces a homotopy equivalence of symmetric products, and the unordered roots-to-coefficients map identifies \(\operatorname{SP}^q(\mathbb C^\times)\) homeomorphically with \(\mathbb C^{q-1}\times\mathbb C^\times\). The product of roots is the last polynomial coefficient up to the sign \((-1)^q\); projection to that nonzero coefficient is a homotopy equivalence. The restricted product map \(\pi_q\) therefore is a homotopy equivalence, independently of the bundle interpretation. In the pushout, \(A\simeq S^1\), \(B\simeq S^1\), and \(C\simeq S^1\times S^1\). Choose the first factor of \(C\) to be \(w\) and the second to be \(\pi_{p-1}\). On fundamental groups, the attaching maps to \(A,B\) are respectively
\[
(a,b)\longmapsto a+b,\qquad (a,b)\longmapsto b.
\]
By van Kampen, the pushout is simply connected: the first boundary generator kills the generator of \(\pi_1(A)\), and the second identifies and then kills the generator of \(\pi_1(B)\). The Mayer--Vietoris sequence has its critical degree-one map
\[
H_1(C;\mathbb Z)\longrightarrow H_1(A;\mathbb Z)\oplus H_1(B;\mathbb Z),
\qquad\begin{pmatrix}1&1\\0&-1\end{pmatrix},
\]
whose determinant is \(-1\). Since \(H_2(C;\mathbb Z)\cong\mathbb Z\), while \(A\) and \(B\) have no positive homology above degree one, it follows that
\[
\widetilde H_j(Y_p;\mathbb Z)\cong
\begin{cases}\mathbb Z,&j=3,\\0,&j\ne3.\end{cases}
\]
The orbit space is a simply connected space of CW homotopy type. The Hurewicz theorem supplies a map \(S^3\to Y_p\) representing a generator of \(H_3\); this is a homology equivalence and hence a homotopy equivalence by the simply-connected homology Whitehead theorem. Therefore \(Y_p\simeq S^3\) for all \(p\ge2\). Note that this conclusion is a homotopy equivalence, **not a claimed homeomorphism** for general \(p\).

**4. Symmetric products and the claimed type.** If \(f:Y\to Y'\) is a homotopy equivalence, applying \(f\) in every coordinate induces a homotopy equivalence \(\operatorname{SP}^m(f)\) for every \(m\), because the inverse maps and homotopies are coordinatewise and commute with permutations. Thus \(\operatorname{SP}^{m_p}(Y_p)\simeq\operatorname{SP}^{m_p}(S^3)\). The factor \(\operatorname{SP}^{m_1}(D^2)\) is contractible by simultaneous radial contraction. Combining these with Step 1 proves the homotopy-type formula.

**5. Rational ring.** For a finite group acting cellularly, the rational cohomology of the ordinary orbit space is the invariant ring. For \((S^3)^m\), that ring starts as the exterior algebra on \(m\) degree-three generators, permuted by \(S_m\). Its invariants consist only of the unit and the sum of the generators: for exterior degree at least two, a transposition of two chosen factors fixes an index subset while negating its wedge product, so every invariant coefficient must vanish. Hence each \(\operatorname{SP}^m(S^3)\) has rational cohomology ring \(\mathbb Q\oplus\mathbb Q[-3]\), with square zero. Applying the Künneth theorem gives the stated exterior algebra and Poincaré polynomial.

## Verification
The accompanying Python script `verify.py` checks the determinant and homological indexing of the integral attaching matrix, enumerates automorphisms of small partition-matroid complexes against the wreath-product order formula, tests all exterior-degree invariant ranks for multiplicities up to ten, and checks the Künneth Betti vector for up to seven distinct sizes. Its recorded output is `verification_output.txt`. The proof in Steps 1--5 applies to all finite block profiles and is not inferred from the finite checks.

## Relationship to prior work
Buchstaber and Panov's original moment-angle construction supplies the polyhedral-product framework. Morton's 1967 theorem on symmetric products of the circle supplies the key disk-bundle lemma in Step 3. Both are established ingredients, not proposed new results. Yu's quotient constructions and Limonchenko--Solomadin's later homotopy-colimit methods treat quotients by subgroups of the coordinate **torus**, rather than by the full finite group of coordinate permutations. Bahri--Bendersky--Cohen--Gitler use symmetric products to study cohomology of polyhedral products, but do not state the present homotopy type of the finite automorphism orbit space for partition-matroid complexes in the inspected material. The precise combination of the one-interior-point pushout, the block automorphism group, and the finite symmetric-product output is the present claim.

## Limitations
No homeomorphism with a product of symmetric powers of three-spheres is claimed, only homotopy equivalence. The statement concerns ordinary orbit spaces, not Borel homotopy quotients, and assumes every block is a discrete simplicial complex. The rational ring description suppresses integral information retained in finite symmetric powers of \(S^3\). A full publication-priority search, especially among very recent work on permutation symmetries of polyhedral products, remains a residual risk. The original 1967 Morton article was available as a bibliographic abstract; its key homotopy-equivalence conclusion is independently derived using polynomial coefficients in Step 3. The earliest precisely day-dated online framework source used here was posted 1999-12-24; the older Morton publication is recorded as April 1967 without inventing a day.

## References
1. V. Buchstaber and T. Panov, *Torus actions, equivariant moment-angle complexes, and coordinate subspace arrangements*, arXiv:math/9912199, first publicly posted 1999-12-24, https://arxiv.org/abs/math/9912199.
2. H. R. Morton, *Symmetric products of the circle*, Proceedings of the Cambridge Philosophical Society **63** (1967), 349–352, doi:10.1017/S0305004100041256. Product-map bundle proof also discussed at https://ncatlab.org/nlab/show/symmetric+product+of+circles.
3. L. Yu, *On Hochster’s formula for a class of quotient spaces of moment-angle complexes*, arXiv:1406.7392, https://arxiv.org/abs/1406.7392.
4. A. Bahri, M. Bendersky, F. R. Cohen and S. Gitler, *Symmetric Products and a Cartan-type formula for polyhedral products*, arXiv:2305.14212, https://arxiv.org/abs/2305.14212.
5. I. Limonchenko and G. Solomadin, *On the homotopy decomposition for the quotient of a moment-angle complex and its applications*, arXiv:2202.13899, https://arxiv.org/abs/2202.13899.
