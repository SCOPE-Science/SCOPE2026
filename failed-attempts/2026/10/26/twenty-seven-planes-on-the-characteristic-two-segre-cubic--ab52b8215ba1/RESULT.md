# Twenty-seven planes on the characteristic-two Segre cubic

## Finding
Let \(\mathcal S\) be the integral Segre cubic threefold in \(\mathbb P^5\), defined by
\[
\sum_{i=1}^{6}X_i=0,\qquad \sum_{i=1}^{6}X_i^3=0.
\]
In characteristic \(2\), its fiber is the cone over the smooth cubic surface
\[
C:\quad \sum_{i=1}^{5}X_i=\sum_{i=1}^{5}X_i^3=0\quad\subset\mathbb P^4.
\]
It has one singular point, an isolated multiplicity-three cone vertex. It contains exactly \(27\) geometric projective planes, all passing through the vertex. Exactly \(15\) of them are defined over \(\mathbb F_2\); the other \(12\) form six conjugate pairs defined over \(\mathbb F_4\). In contrast, the characteristic-zero Segre cubic has \(15\) planes. Hence its plane-incidence geometry acquires twelve extra geometric planes upon reduction modulo \(2\).

The cubic surface \(C\) is the unique smooth \(\mathbb F_2\)-cubic surface with automorphism group \(S_6\), and is isomorphic over \(\mathbb F_4\) to the Fermat cubic surface. Consequently, for every integer \(m\ge1\), writing \(q=2^m\),
\[
\#\mathcal S(\mathbb F_q)=q^3+(6+(-1)^m)q^2+q+1.
\]
The assertion concerns geometric planes as reduced subvarieties, *not* a determination of the full scheme structure of the relative Hilbert scheme of planes.

## Assumptions and scope
All projective varieties are defined by the displayed homogeneous equations. The special-fiber assertion is over any characteristic-two field; finite-field counts refer to the actual standard integral model over \(\mathbb F_2\), not to arbitrary twists. A geometric plane is a linear \(\mathbb P^2\) over an algebraic closure. The comparison in characteristic zero uses the classical \(15\)-plane theorem for the standard Segre cubic.

## Proof
**Cone decomposition.** In characteristic \(2\), set \(e=(1,1,1,1,1,1)\) in the five-dimensional vector space \(H=\{\sum X_i=0\}\). Let \(W=H\cap\{X_6=0\}\). Since \(e_6=1\), one has the direct sum \(H=W\oplus ke\). For \(w\in W\) and scalar \(t\), the characteristic-two binomial expansion gives
\[
\sum_{i=1}^{6}(w_i+t)^3
=\sum_i w_i^3+t\sum_i w_i^2+t^2\sum_iw_i,
\]
where the \(t^3\)-term is \(6t^3=0\). Since \(\sum_iw_i=0\) and \(\sum_iw_i^2=(\sum_iw_i)^2=0\), the cubic is independent of \(t\). Thus \(\mathcal S_{\mathbb F_2}\) is the projective cone over \(C\subset\mathbb P(W)\), with vertex \([e]\).

**Singular locus and multiplicity.** The gradient of the cubic in the hyperplane \(H\) vanishes precisely when the ambient gradient \((X_1^2,\ldots,X_6^2)\) is proportional to \((1,\ldots,1)\). Over any field of characteristic two, after extending to an algebraic closure this forces all six coordinates equal, giving exactly \([e]\). In the slice \(W\) all five coordinates similarly would have to be equal, incompatible with their zero sum unless all are zero (because \(5=1\) in characteristic two). Therefore \(C\) is smooth. The affine equation at the vertex is exactly the homogeneous cubic defining \(C\), so the vertex has multiplicity \(3\), and its projectivized tangent cone is smooth.

**Planes.** Projection from \([e]\) onto \(\mathbb P(W)\) sends any plane not through \([e]\) isomorphically onto a plane in \(C\), which is impossible for a smooth cubic surface in \(\mathbb P^3\). A plane through \([e]\) is exactly the join of \([e]\) with a line on \(C\). The classical 27-line theorem for a smooth cubic surface in any characteristic therefore gives precisely \(27\) geometric planes.

**Specialization of the classical planes.** Each partition of the six indices into three unordered pairs \(\{a,b\},\{c,d\},\{e,f\}\) gives one of the fifteen classical Segre planes with equations \(X_a+X_b=X_c+X_d=X_e+X_f=0\). Upon reduction modulo \(2\), these become \(X_a=X_b\), \(X_c=X_d\), \(X_e=X_f\); the fifteen partitions still define fifteen distinct planes. Thus all fifteen classical planes survive as distinct special-fiber planes and the other twelve are genuinely additional geometric planes.

**Arithmetic and symmetry.** Permutations of the six coordinates preserve \(H\), its one-dimensional subspace \(ke\), and the cubic; they give a faithful projective action of \(S_6\) on \(C\). For instance, a three-cycle acts nontrivially, and its normal closure excludes a nontrivial normal kernel. By the uniqueness and maximality theorem for smooth cubic surfaces over \(\mathbb F_2\) [Vikulova, Theorem 1.3], \(C\) is the unique \(\mathbb F_2\) surface with this symmetry; over \(\mathbb F_4\) it becomes the Fermat cubic [Vikulova, Corollary 1.7]. All \(27\) lines of that Hermitian Fermat cubic are defined over \(\mathbb F_4\). The accompanying exact coefficient-level line enumeration checks all \(35\) projective lines in \(\mathbb P^3(\mathbb F_2)\) and finds exactly \(15\) contained in \(C\); over \(\mathbb F_4\), it finds exactly \(27\). Therefore the remaining \(12\) geometric lines form six conjugate pairs over \(\mathbb F_4\), and the same is true of their cone planes.

Finally, every point of \(\mathbb P^3(\mathbb F_2)\) lies on \(C\), since \(a^3=a\) for \(a\in\mathbb F_2\); thus \(\#C(\mathbb F_2)=15\). The \(27\) lines defined over \(\mathbb F_4\) span the rank-7 geometric Picard group, so the eigenvalues of Frobenius on that group square to \(1\). The smooth cubic-surface point-count formula gives \(15=2^2+2\operatorname{Tr}(\mathrm{Frob}|\mathrm{Pic})+1\), hence trace \(5\). The seven eigenvalues are therefore six \(+1\)'s and one \(-1\), yielding
\[
\#C(\mathbb F_{2^m})=q^2+(6+(-1)^m)q+1.
\]
Each \(\mathbb F_q\)-point of the base contributes \(q\) nonvertex rational points on the cone, while the vertex contributes one. Multiplication by \(q\) and addition of \(1\) proves the displayed cone point-count formula.

## Verification
Run `python verify.py` with the Python standard library. It enumerates all points and lines of \(\mathbb P^3\) over \(\mathbb F_2\) and \(\mathbb F_4\), using exact arithmetic (the \(\mathbb F_4\) modulus is \(u^2+u+1\)). A line is counted only when all four coefficients of the binary cubic obtained by restricting the defining equation vanish; testing its rational points alone is not substituted for containment. It outputs `q 2 base_points 15 lines 15`, `q 4 base_points 45 lines 27`, and `VERIFY_OK`. The general cone and Picard arguments are proofs, not inferred from finite tests.

## Relationship to prior work
Cheltsov–Tschinkel–Zhang (2023, arXiv:2308.15271) treat group actions on the classical Segre cubic in characteristic zero. Dolgachev (2015, arXiv:1501.06432) describes the 15 classical Segre planes; Eklund (2018) also explains their appearance in Heisenberg quartic geometry. Vikulova (2023, arXiv:2312.17032) determines the unique maximally \(S_6\)-symmetric smooth cubic surface over \(\mathbb F_2\) and its quadratic extension to the Fermat surface, but does not identify it as the base of a special Segre-cubic fiber or classify that fiber's planes. The new comparison is the specific characteristic-two cone degeneration and 15-to-27 plane jump, with field-of-definition stratification and zeta-count consequence.

## Limitations
The finding does not classify scheme-theoretic infinitesimal structures of the Hilbert scheme of planes or deformations of individual planes. It does not assert analogous behavior at primes other than \(2\). Classical literature not indexed in available searches could contain an equivalent reduction observation. Arithmetic formulas concern this integral model only.

## References
- I. Cheltsov, Yu. Tschinkel, Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, arXiv:2308.15271 (first posted 2023-08-29), https://arxiv.org/abs/2308.15271.
- A. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2*, arXiv:2312.17032 (first posted 2023-12-28), https://arxiv.org/abs/2312.17032; Theorems 1.3–1.5, Corollary 1.7.
- I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432 (2015), Section 2, https://arxiv.org/abs/1501.06432.
- D. Eklund, *Curves on Heisenberg invariant quartic surfaces in projective 3-space*, European Journal of Mathematics 4 (2018), Section 2.4, https://doi.org/10.1007/s40879-018-0216-2.
