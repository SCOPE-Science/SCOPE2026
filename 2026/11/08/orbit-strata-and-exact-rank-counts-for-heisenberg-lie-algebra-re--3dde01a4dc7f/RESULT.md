# Orbit strata and exact rank counts for Heisenberg Lie algebra retractions

## Finding

Let \(k\) be any field and let \(H=V\oplus kz\), where \(V\) has dimension \(2n\), \(n\ge1\), with a nondegenerate alternating bilinear form \(\omega\). Equip \(H\) with the Heisenberg bracket \([v,w]=\omega(v,w)z\) and central \(z\). We classify all ordinary Lie-algebra endomorphisms \(P:H\longrightarrow H\) with \(P^2=P\), both as labeled maps and under \(\operatorname{Aut}(H)\)-conjugacy.

Every such endomorphism is either the identity or is uniquely described by an isotropic subspace \(W\le V\) of dimension \(r\), a complementary subspace \(U\) with \(V=W\oplus U\), and a functional \(\varphi\in W^*\). The associated projection \(B:V\to W\) along \(U\) satisfies \(P(v)=Bv+\varphi(Bv)z\) and \(P(z)=0\). Here \(0\le r\le n\); the map has linear rank \(r\).

Put \(Z=U^{\perp_\omega}\). The restriction \(\omega|_Z\) has an even rank \(2s\), with \(0\le s\le\lfloor r/2\rfloor\). Two nonidentity retractions are conjugate under the **full** Lie-algebra automorphism group if and only if their invariants \((r,s)\) agree. Each such pair occurs. Thus the number of conjugacy classes over any field is
\[
1+\sum_{r=0}^{n}\bigl(\lfloor r/2\rfloor+1\bigr),
\]
including the identity class.

For \(k=\mathbb F_q\), define \(G_j(q)=\prod_{i=0}^{j-1}(q^j-q^i)\), \(S_s(q)=q^{s^2}\prod_{i=1}^{s}(q^{2i}-1)\), and the Gaussian coefficient \({a\brack b}_q\), all with the usual empty-product conventions. Define
\[
I_{n,r}(q)=\frac{\prod_{i=0}^{r-1}(q^{2n-i}-q^i)}{G_r(q)}.
\]
The exact cardinality of the individual nonidentity orbit indexed by \((r,s)\) is
\[
\boxed{N_{n,r,s}(q)=I_{n,r}(q){r\brack 2s}_q
\frac{G_{2s}(q)}{S_s(q)}
q^{r(r+1)/2+2r(n-r)+r}.}
\]
In particular, all operators having rank \(r\) are counted by \(I_{n,r}(q)q^{r(2n-r+1)}\), and the complete rank polynomial is
\[
\boxed{\mathcal R_{n,q}(T)=T^{2n+1}+\sum_{r=0}^{n}
I_{n,r}(q)q^{r(2n-r+1)}T^r.}
\]
Hence the realized ranks are exactly \(0,1,\ldots,n,2n+1\); all ranks strictly between \(n\) and \(2n+1\) are absent.

The reduced variety of these endomorphisms has \(n+2\) smooth geometrically irreducible connected components: one for each nonidentity rank \(r=0,\ldots,n\), and the isolated identity. The rank-\(r\) component is an iterated affine bundle over the isotropic Grassmannian \(\operatorname{IGr}(r,V)\), of dimension
\[
2r(2n-r)+r-\binom r2.
\]
Inside this component, the orbit indexed by \(s\) has codimension \(\binom{r-2s}{2}\). These statements concern the reduced parameter variety; no assertion about nonreduced scheme structure is made.

## Assumptions and scope

The base field is arbitrary, including characteristic two, and \(n\ge1\). Endomorphisms are ordinary Lie-algebra homomorphisms, not restricted-Lie homomorphisms. Maps are labeled over \(\mathbb F_q\), and the orbit action is the full algebraic group \(\operatorname{Aut}(H)\), not merely the subgroup of inner automorphisms. The symplectic form is alternating in every characteristic. The polynomial counts each distinct linear map exactly once. No isomorphism-quotient weighting is used.

## Proof

**1. Normal form and all solutions.** As \([H,H]=kz\), an endomorphism has \(P(z)=cz\) and \(P(v)=Bv+\psi(v)z\), with \(B\in\operatorname{End}(V)\), \(\psi\in V^*\). Preserving brackets is equivalent to \(\omega(Bv,Bw)=c\omega(v,w)\) for all \(v,w\). The idempotence condition gives \(B^2=B\), \(c^2=c\), and \(\psi B+c\psi=\psi\). Since \(k\) is a field, \(c=0\) or \(1\). If \(c=1\), nondegeneracy makes \(B\) invertible and idempotence forces \(B=1_V\); the functional equation then gives \(\psi=0\), hence \(P=1_H\). If \(c=0\), the bracket condition states that \(\operatorname{im}B=W\) is totally isotropic and the remaining condition is \(\psi=\psi B\). Every idempotent \(B\) is projection onto \(W\) along a complement \(U\). Each \(\psi\) is uniquely the extension of a functional \(\varphi\in W^*\) by zero on \(U\). Conversely all such data satisfy both original identities. Thus every nonidentity map has rank \(r=\dim W\le n\).

**2. Conjugacy invariant.** Any Lie automorphism acts by \(z\mapsto cz\), \(v\mapsto Av+\alpha(v)z\), with \(c\ne0\), \(\omega(Av,Aw)=c\omega(v,w)\), and arbitrary \(\alpha\in V^*\). Taking \(A=1_V\), conjugation by the central shear \(v\mapsto v+\alpha(v)z\), \(z\mapsto z\), changes the functional of a map with \(P(z)=0\) by the precise formula \(\psi\mapsto\psi+\alpha B\). Since \(\psi=\psi B\), choosing \(\alpha|_W=-\varphi\) kills the functional. Equivalently, the image graph \(\{w+\varphi(w)z:w\in W\}\) is flattened. This leaves \(B\) and \(U\) intact. Thus conjugacy reduces to symplectic-similitude equivalence of the complementary pair \((W,U)\).

For \(Z=U^{\perp_\omega}\), the pairing \(W\times Z\to k\) is perfect: if \(w\in W\) annihilates \(Z\), then \(w\in Z^\perp=U\), hence \(w=0\). Both spaces have dimension \(r\), so the pairing is nondegenerate. Also \(W\cap Z=0\): any vector in their intersection annihilates \(W\) (as \(W\) is isotropic) and \(U\) (as it is in \(Z\)), hence all of \(V\). Therefore \(W\oplus Z\) is a nondegenerate symplectic \(2r\)-space. Fixing dual bases for \(W\) and \(Z\), the restricted form has matrix \(\Omega\), which is alternating. Changes of the basis of \(W\) induce congruence transformations of \(\Omega\). Alternating forms on an \(r\)-space over any field are congruent precisely when their ranks match, and every even rank \(2s\le r\) occurs. An isometry of the two nondegenerate subspaces \(W\oplus Z\) that matches their marked summands extends to \(V\) by a symplectic isometry of their orthogonal complements. Hence this rank completely classifies the full-automorphism orbits. Since \(U=Z^\perp\), the marked \(Z\) recovers the kernel. This also proves existence of each \((r,s)\) via an alternating form on a chosen dual complement.

**3. Counting isotropic images.** The number of ordered isotropic \(r\)-frames is \(\prod_{i=0}^{r-1}(q^{2n-i}-q^i)\): at the next step the vector belongs to the orthogonal complement of the previously selected isotropic span but not to that span. Each isotropic \(r\)-space contains \(G_r(q)\) ordered bases. Dividing gives \(I_{n,r}(q)\).

**4. Counting kernels with a fixed alternating invariant.** Fix \(W\) and a symplectic Witt decomposition \(V=W\oplus H_0\oplus W^*\), with \(\dim H_0=2(n-r)\). Every complement \(Z\) to \(W\) that pairs perfectly with \(W\) is the graph over the distinguished \(W^*\) of two maps: \(A:W^*\to W\) and \(L:W^*\to H_0\). The restricted alternating form is \(A-A^\mathsf T+L^\mathsf T J_0L\), up to a conventional overall sign, where \(J_0\) represents \(\omega|_{H_0}\). The linear map \(A\mapsto A-A^\mathsf T\) onto alternating matrices is surjective in all characteristics, including characteristic two, and has kernel dimension \(r(r+1)/2\). Thus for *each fixed alternating matrix* there are exactly \(q^{r(r+1)/2+2r(n-r)}\) choices of \(Z\), and hence of \(U=Z^\perp\). There are \({r\brack 2s}_q G_{2s}(q)/S_s(q)\) alternating matrices of rank \(2s\): first choose their \((r-2s)\)-dimensional radical, then choose a nondegenerate alternating form on the quotient, counted by the indicated general-linear/symplectic group quotient. The \(\varphi\in W^*\) add \(q^r\) choices. Multiplying by \(I_{n,r}(q)\) proves the orbit formula. Summing over all alternating matrices (there are \(q^{\binom r2}\)) yields \(I_{n,r}(q)q^{r(2n-r+1)}\), and adjoining the identity proves the rank polynomial.

**5. Geometry.** For fixed \(r\), the isotropic Grassmannian of possible \(W\) is smooth and geometrically irreducible, of dimension \(r(2n-r)-\binom r2\). The space of complements \(U\) is an affine-bundle torsor of relative dimension \(r(2n-r)\), while the extensions of \(\varphi\) are a rank-\(r\) vector bundle. Consequently the fixed-rank component is smooth irreducible with the claimed dimension. Rank of an idempotent operator is locally constant in algebraic families; therefore these disjoint fixed-rank loci and the identity are open and closed in the reduced solution variety, giving exactly \(n+2\) components. The condition \(\operatorname{rank}\omega|_Z=2s\) has codimension \(\binom{r-2s}{2}\) in the affine space of alternating matrices, establishing the orbit codimension.

## Verification

The reproducibility file `verify.py` enumerates all \(3\times3\) linear maps for \(n=1\) over \(\mathbb F_2\) and \(\mathbb F_3\), tests \(P^2=P\) and the **original** Lie-homomorphism equation on basis vectors, and compares the exact \((r,s)\) distributions with the formula. For \(n=2\) over \(\mathbb F_2\), it enumerates all quotient idempotents, verifies isotropy and the original matrix identities of all allowed lifts, and compares each symplectic restriction-rank stratum. The output in `verification_output.txt` ends `HEISENBERG_IDEMPOTENT_RETRACTION_ORBIT_COUNTS_OK`.

The independently checked distributions are \((0,0):1,(1,0):12,(3,\mathrm{identity}):1\) at \((n,q)=(1,2)\), \((0,0):1,(1,0):36,(3,\mathrm{identity}):1\) at \((1,3)\), and \((0,0):1,(1,0):240,(2,0):480,(2,1):480,(5,\mathrm{identity}):1\) at \((2,2)\). The code represents the second orbit parameter by the actual alternating rank \(2s\), not by \(s\). Finite experiments support the proof but cannot establish all dimensions or all fields on their own.

## Relationship to prior work

Carlson, Friedlander, and Pevtsova (`arXiv:1207.5898`, subsequently available as `arXiv:1408.3913`) identify the maximal elementary subalgebra variety of a restricted Heisenberg Lie algebra with a Lagrangian Grassmannian; the inspected Proposition 2.2 concerns **subalgebras**, not idempotent endomorphisms, complementary kernels, or full-automorphism orbit multiplicities. Rojas (`arXiv:1206.5867`) uses the standard Heisenberg symplectic bracket and studies minimal faithful representations, not this retraction count. Cerqua and Facchini (`arXiv:2301.02627`, Section 6, Proposition 15) discuss the general decomposition principle for idempotent endomorphisms in a pre-Lie context; such a principle does not supply the alternating-rank orbit stratification or finite-field counts. These connections motivate the present question but do not independently verify historical novelty.

The closest inspected public mathematical finding records concern Heisenberg subalgebra commutativity counts and fixed-point-free automorphisms; their asserted invariants do not imply the labeled retraction orbits. Generic Grassmannian and alternating-form enumeration are standard ingredients; originality, if established, concerns their **combined exact application to retractions**, including the kernel invariant. A broader previously published retraction theorem could still subsume this result.

## Limitations

This result treats ordinary Lie-algebra idempotent endomorphisms of Heisenberg algebras and their reduced geometric parameter varieties, not arbitrary endomorphisms, restricted-Lie endomorphisms, nonreduced equation schemes, or endomorphisms of Heisenberg groups. The component and orbit formulas are not independently externally certified. Priority is a best-knowledge comparison against the inspected literature and research-record queries; it is not a proof that no stronger theorem exists.

## References

1. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Elementary subalgebras of Lie algebras*, `arXiv:1207.5898` (first submitted 2012-07-25); inspected expanded full text `arXiv:1408.3913`, especially §2 and Proposition 2.2. https://arxiv.org/abs/1207.5898 ; https://arxiv.org/pdf/1408.3913
2. Á. Rojas, *Minimal Faithful Representation of the Heisenberg Lie Algebra with Abelian Factor*, `arXiv:1206.5867` (first submitted 2012-06-26), especially the introduction and the defining Heisenberg bracket. https://arxiv.org/abs/1206.5867
3. A. Cerqua and A. Facchini, *Pre-Lie algebras, their multiplicative lattice, and idempotent endomorphisms*, `arXiv:2301.02627` (2023), §6, Proposition 15. https://arxiv.org/abs/2301.02627
