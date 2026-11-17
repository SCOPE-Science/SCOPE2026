# A lens-space homotopy model for the rotational quotient of the eleven-cycle independence complex

## Finding
Let \(C_{11}\) have vertices \(0,1,\ldots,10\) and edges joining cyclic neighbors. Let \(K=\operatorname{Ind}(C_{11})\), and let the cyclic group \(G=C_{11}\) act by increasing the labels by one. Then
\[
|K|/G\simeq L(11;1,4).
\]
Here the right side means the quotient of the unit sphere in \(\mathbb C^2\) by \((z,w)\mapsto(\zeta z,\zeta^4w)\), \(\zeta=e^{2\pi i/11}\). The assertion is a homotopy equivalence, **not** a homeomorphism of the given orbit spaces.

The stronger mechanism is a concrete \(G\)-equivariant homotopy equivalence to the unit sphere in the two-character representation \(\mathbb C_4\oplus\mathbb C_5\). In particular the quotient has fundamental group \(\mathbb Z/11\) and integral homology \(H_0=H_3=\mathbb Z\), \(H_1=\mathbb Z/11\), and \(H_2=0\), as follows from the homotopy classification.

## Assumptions and scope
Every face of \(K\) is a subset of cyclic labels containing no neighboring pair. Geometric realization uses barycentric coordinates \(x=(x_0,\ldots,x_{10})\), with nonnegative entries summing to one and support a face of \(K\). The orbit is the actual quotient topological space, not the simplicial complex obtained by identifying vertices. For \(j\in\mathbb Z/11\) and \(k\in\{4,5\}\) put \(\omega=\exp(2\pi i/11)\) and
\[
F_k(x)=\sum_{j=0}^{10}x_j\omega^{kj},\qquad
F(x)=\bigl(F_4(x),F_5(x)\bigr).
\]
The group generator acts on target coordinates by \(\omega^4\) and \(\omega^5\). The notation \(L(11;1,4)\) uses the group generator rescaled by the inverse of four modulo eleven. All homotopy statements are in the category of finite CW spaces.

## Proof
**1. Underlying homotopy and freeness.** The classical independence-complex recurrence for cycles (Kozlov; also Adamaszek) gives \(\operatorname{Ind}(C_{11})\simeq\Sigma^2\operatorname{Ind}(C_5)\simeq S^3\). Since eleven is prime, each nonidentity vertex rotation is transitive; a geometric fixed point would have an invariant supporting independent face. The only invariant nonempty subset is the entire vertex set, which is not independent. Thus the \(G\)-action on \(|K|\) is free.

**2. No Fourier zero.** The maximal independent faces are precisely the eleven cyclic translates of \(\{0,2,4,6,8\}\). On that representative maximal face, the real linear functional \((z,w)\mapsto\Re(w)-\Im(w)\) is strictly positive on all five corresponding Fourier vertex vectors, with a certified margin exceeding \(1/10\). Its rotated counterpart works on each translated maximal face. Therefore \(F(x)\neq0\) for every \(x\in|K|\), and
\[
f(x)=F(x)/\|F(x)\|\in S(\mathbb C_4\oplus\mathbb C_5)
\]
is well-defined, continuous, and \(G\)-equivariant.

**3. A primitive degree certificate.** The included standalone `verify.py` constructs an explicit oriented integral \(3\)-cycle \(Z\), supported on twenty-eight tetrahedra of \(K\), and checks every triangular boundary coefficient vanishes. For the regular target ray \(v=(2,3,5,7)\in\mathbb R^4\) it checks, on every tetrahedron of \(Z\), all Cramer numerators and the four-column determinant. Exactly the simplex \((0,3,7,9)\), with cycle coefficient \(+1\), meets the positive ray in its relative interior, and its four-column determinant is negative. Hence the signed degree of the normalized Fourier map on \([Z]\) is \(-1\).

This is not an unverified floating-point observation: `verify.py` bounds \(\pi\) by an exact rational Machin series, bounds the sine/cosine truncation, rounds each real Fourier coordinate to rational accuracy strictly better than \(2\times10^{-12}\), and verifies every relevant integer determinant's absolute normalized value exceeds \(1/3\). The worst-case determinant perturbation is below \(10^{-6}\), so the reported signs and the ray-count are rigorous. An explicit list of the twenty-eight tetrahedra and coefficients appears in `verify.py`.

**4. Descent to lens-space homotopy.** Since \(|K|\simeq S^3\), the degree \(-1\) map \(f:|K|\to S^3\) induces isomorphisms on all homotopy groups: this follows from the degree-isomorphism in degree three and Whitehead's theorem for simply connected CW complexes. Both source and target have free \(G\)-actions. Their quotients have universal coverings given by those spaces; the descended map is an isomorphism on \(\pi_1\cong G\) and on all higher homotopy groups. It is therefore a homotopy equivalence. The target linear sphere quotient is \(L(11;4,5)\), which becomes \(L(11;1,4)\) after replacing the cyclic generator by its third power, because \(3\cdot4\equiv1\) and \(3\cdot5\equiv4\pmod{11}\).

## Verification
Execute `python3 verify.py` using only the Python standard library. Compare its output to `verification_output.txt`. The checker enumerates all independent faces, verifies all maximal-face rotations, computes the integral boundary of the explicit \(3\)-cycle, and gives exact rational certificates for nonvanishing and the signed degree. The general homotopy arguments above are mathematical steps, not inferred from finite data. Certificate assumptions are precisely the eleven cycle labels, standard Fourier action, and the displayed target ray.

## Relationship to prior work
The classical cycle-independence homotopy computation establishes the covering complex's sphere homotopy type. A pre-existing calculation of cyclic polygon matching-space orbit spaces establishes homology, fundamental group and integral cohomology rings, including the eleven-cycle case, but explicitly leaves lens-space **homotopy equivalence** unasserted. Such algebraic invariants alone do not imply this result. The present difference is an explicit equivariant Fourier map whose degree is certified \(\pm1\).

The literature on symmetric nerves of circular arcs studies related cyclic and dihedral homology representations but is not assumed to provide this precise quotient equivalence. A published study of cyclic *nonmatching* complexes also produces representation spheres and lens spaces; those complexes forbid the existence of a large matching, whereas the present matching complex **consists** of matchings. The two face conditions are not interchangeable and neither result implies this one. Priority against unindexed, alternate formulations remains uncertain.

## Limitations
Only the eleven-cycle and the specified rotation action are classified here. The work does not assert any PL homeomorphism, any result for full dihedral symmetry, or an all-prime lens-space theorem. The normal-form lens parameter is tied to the explicit generator and is not meant as a claim of uniqueness among lens-space presentations. The same-model proof and exact checker are not independent mathematical validation. The novelty assessment is relative to inspected sources and may change upon finding an equivalent prior theorem.

## References
- A. Engström, *Complexes of Directed Trees and Independence Complexes*, first public arXiv posting 2005-08-08, https://arxiv.org/abs/math/0508148.
- M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, first public arXiv posting 2011-06-30, https://arxiv.org/abs/1106.6250.
- M. Adamaszek, H. Adams, F. Frick, C. Peterson, C. Previte-Johnson, *Nerve complexes of circular arcs*, first public arXiv posting 2014-10-16, https://arxiv.org/abs/1410.4336.
