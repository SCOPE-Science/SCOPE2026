# Dihedral fixed spaces, lens quotients, and sphere quotients of cyclic nonmatching complexes

## Finding
Let \(C_n\) be the graph with edges \(e_i=\{i,i+1\}\), indexed by \(i\in\mathbb Z/n\mathbb Z\). A face of the \(t\)-nonmatching complex \(\operatorname{NM}_t(C_n)\) is a subset of \(E(C_n)\) not containing \(t\) pairwise disjoint edges. Fix integers \(t\ge3\), \(n\ge2t\), and write \(d=t-1\). The dihedral group \(D_n=\langle r,s\rangle\) acts on the edge labels by \(r(i)=i+1\), \(s(i)=-i\). This action is the usual symmetries of the *edge-index cycle* (a conjugate of the geometric reflection action on the underlying graph).

**Equivariant spherical model.** Put \(V=\bigoplus_{j=1}^{d}\mathbb C_j\), regarded as a real orthogonal representation of dimension \(2d\), with
\[
r(z_1,\ldots,z_d)=(\omega z_1,\omega^2 z_2,\ldots,\omega^d z_d),\qquad
s(z_1,\ldots,z_d)=(\bar z_1,\ldots,\bar z_d),
\quad \omega=e^{2\pi i/n}.
\]
There is a \(D_n\)-equivariant homeomorphism
\[
|\operatorname{NM}_t(C_n)|\cong S(V)\cong S^{2t-3}.
\]
The statement is about actual equivariant homeomorphism, not merely a homology representation.

**All subgroup fixed spaces.** For every divisor \(q\mid n\) and integer \(a\), set \(C_q=\langle r^{n/q}\rangle\) and \(D_{q,a}=\langle r^{n/q},r^a s\rangle\). Every subgroup of \(D_n\) is one of these types, including the trivial group \(C_1\). With the convention \(S^{-1}=\varnothing\),
\[
|\operatorname{NM}_t(C_n)|^{C_q}\cong S^{2\lfloor d/q\rfloor-1},\qquad
|\operatorname{NM}_t(C_n)|^{D_{q,a}}\cong S^{\lfloor d/q\rfloor-1}.
\]
In particular, the full dihedral fixed space is empty.

**Cyclic quotient and integral torsion.** The action of \(C_n\) on the sphere is free if and only if no prime divisor of \(n\) is at most \(d\). Precisely in that range,
\[
|\operatorname{NM}_t(C_n)|/C_n\cong L(n;1,2,\ldots,d).
\]
Its integral homology is \(H_0\cong H_{2d-1}\cong\mathbb Z\), \(H_{2j-1}\cong\mathbb Z/n\) for \(1\le j\le d-1\), and zero in all other degrees. Its fundamental group is \(\mathbb Z/n\).

**A contrasting dihedral quotient.** For every \(n\ge6\), independently of parity,
\[
|\operatorname{NM}_3(C_n)|/D_n\cong S^3.
\]
Thus at odd \(n\ge7\) the cyclic quotient is the non-simply-connected lens space \(L(n;1,2)\), whereas the full dihedral quotient is the three-sphere. At even \(n\), the cyclic action is not free, but the full dihedral quotient remains a three-sphere.

## Assumptions and scope
All spaces are geometric realizations; \(X^H\) denotes the *geometric* fixed-point set, not the realization of a vertex-fixed subcomplex. The cyclic/dihedral symbols refer to specified subgroups of the standard action on cycle *edge indices*. The lens-space notation is the quotient of the unit sphere of \(\mathbb C^d\) by the diagonal weights \(1,\ldots,d\). The homeomorphisms are topological and equivariant where stated; no unproved PL or smooth conjugacy is asserted. The parameter bounds ensure the corresponding cyclic polytope is full-dimensional and simplicial.

## Proof
**1. A label-preserving cyclic-polytope boundary.** Shan and Wang, Lemma 2.2, prove that \(\operatorname{NM}_t(C_n)\) is simplicially isomorphic to \(\partial C(n,2d)\) by sending the cyclically labeled edge \(e_i\) to cyclic-polytope vertex \(i\). Their proof uses the matching characterization of the minimal nonfaces and the cyclic-polytope Gale evenness description. Therefore this identification respects all cyclic shifts and reversals of the labels. The combinatorial identification alone does not yet establish a model for *geometric* fixed spaces.

**2. A dihedrally orthogonal geometric model.** Let
\[
\Phi(i)=(\omega^{i},\omega^{2i},\ldots,\omega^{di})\in\mathbb C^d,
\qquad P=\operatorname{conv}\{\Phi(i):i\in\mathbb Z/n\mathbb Z\}.
\]
The equally spaced trigonometric moment curve realizes the standard labeled cyclic polytope \(C(n,2d)\): this is the even-dimensional Carathéodory realization, discussed explicitly by Olarte and Santos, Section 2.3. Its face lattice agrees with the polynomial-moment-curve model. In particular, taking affine combinations on its boundary simplices gives a \(D_n\)-equivariant homeomorphism from the geometric realization of the nonmatching complex to \(\partial P\), since
\[
\Phi(i+1)=r\Phi(i),\qquad \Phi(-i)=s\Phi(i).
\]
Because \(n\ge2d+2\), the coordinate Fourier characters \(1,\omega^{ji},\omega^{-ji}\) for \(1\le j\le d\) are linearly independent on the \(n\) sample labels. Hence \(P\) affinely spans \(V\). Moreover \(n^{-1}\sum_i\Phi(i)=0\), a strictly positive convex combination of all vertices. Therefore \(0\) is in the interior of \(P\). Radial projection \(x\mapsto x/\|x\|\) is a homeomorphism \(\partial P\to S(V)\). Since \(D_n\) acts orthogonally, this homeomorphism is equivariant. This proves the representation-sphere assertion, including the exact topological scope.

**3. Fixed subspaces.** An element \(r^{n/q}\) acts on \(\mathbb C_j\) by multiplication by \(e^{2\pi i j/q}\), so its real fixed subspace has dimension two precisely when \(q\mid j\), and zero otherwise. Thus \(\dim_\mathbb R V^{C_q}=2\lfloor d/q\rfloor\). On each surviving \(\mathbb C_j\), the element \(r^a s\) acts by \(z\mapsto\omega^{aj}\bar z\), whose fixed set is a real line. Hence \(\dim_\mathbb R V^{D_{q,a}}=\lfloor d/q\rfloor\). Intersecting with the unit sphere gives exactly the two fixed-space formulas. The case of fixed dimension zero is empty, as specified by the \(S^{-1}\) convention.

**4. Free cyclic action and torsion.** A nonidentity power of \(r\) fixes a point of \(S(V)\) if and only if it acts trivially on at least one harmonic coordinate \(\mathbb C_j\). Such a power exists if and only if \(\gcd(n,j)>1\) for some \(1\le j\le d\); equivalently the least prime factor of \(n\) is at most \(d\). When no such prime exists the quotient is, by the *definition* of generalized lens spaces, \(L(n;1,\ldots,d)\). The standard one-cell-per-degree cellular chain complex of a lens space gives the stated integral homology and fundamental group (here \(d\ge2\), so the sphere is simply connected).

**5. The full dihedral quotient at \(t=3\).** Here \(V=\mathbb C_1\oplus\mathbb C_2\) and \(S(V)=S^3\). Every rotation belongs to \(SO(4)\). The reflection \(s\) is complex conjugation in both complex coordinates, hence has real determinant \((-1)^2=1\); thus the entire \(D_n\) action on \(S^3\) is orientation preserving and orthogonal. At each point its stabilizer is a finite subgroup of \(SO(3)\) acting on the tangent space. The local quotient is a cone on \(S^2/K\); every finite rotation subgroup \(K\le SO(3)\) has \(S^2/K\cong S^2\). Thus \(S^3/D_n\) is a closed connected topological three-manifold without boundary, including at its singular-orbit images.

Every reflection \(r^a s\) fixes a unit circle: the equations \(z_j=\omega^{aj}\bar z_j\) cut out a real line in each of the two complex coordinates, whose unit sphere is \(S^1\). Reflections generate \(D_n\). Armstrong's fundamental-group theorem for orbit spaces of finite group actions on simply connected, locally suitably connected spaces therefore gives \(\pi_1(S^3/D_n)=D_n/N=1\), where \(N\) is the normal subgroup generated by elements with fixed points. The topological Poincaré theorem identifies every closed simply connected three-manifold with \(S^3\). This proves the full dihedral quotient assertion for all \(n\ge6\), without assuming that the cyclic subgroup acts freely.

## Verification
The included `verify.py` independently enumerates all forbidden \(t\)-matchings of small cycle graphs; compares the maximal allowable faces with Gale-evenness facets of cyclic polytopes; constructs geometric fixed-point orbit complexes for cyclic and dihedral subgroups and computes their reduced homology over \(\mathbb F_2\); and computes quotient barycentric flag-cell homology over \(\mathbb F_2\) and \(\mathbb F_3\) for \(t=3\). It does not use the harmonic representation to generate these finite complexes. Execute `python3 verify.py`. These finite computations are corroboration, not a proof of the unrestricted theorem or homeomorphism type. The proof relies on the explicitly stated geometric model and standard cited three-manifold theorems.

## Relationship to prior work
Shan and Wang's 2026 Lemma 2.2—and the earlier cyclic-polytope characterization it cites—already identify the **nonequivariant combinatorial** complex. Olarte and Santos explicitly describe the symmetric trigonometric realization of cyclic polytopes. Neither work states the all-subgroup geometric fixed-space classification, free-action threshold with integral lens-space quotients, or the all-length three-sphere dihedral quotient for these nonmatching complexes. Their ingredients are essential and are not claimed as new.

A prior published result titled *Dihedral orientation characters of bounded-independence spheres on cycles* treats exactly the same simplicial complex under the equivalent description \(\{S:\alpha(C_n[S])<t\}\): it determines the integral orientation character and rational homology of cyclic and full dihedral quotients. Those facts are *excluded* from the present novelty claim. They neither distinguish the lens-space integral torsion nor establish geometric fixed-point types or the full dihedral quotient homeomorphism. The present proof uses the much stronger geometric harmonic-sphere model and, in dimension three, the orbit-space fundamental-group theorem and the Poincaré theorem. The combination of established cyclic-polytope and moment-curve methods makes these conclusions accessible; priority against every unindexed treatment of this combination is not asserted.

## Limitations
The theorem is confined to \(n\ge2t\) and \(t\ge3\), with the natural action on cyclically indexed *edges*. The orientation character and rational quotient homology are known prior facts. The stated integral homology of the rotation quotient applies only when its action is free; no integral homology formula is claimed for the nonfree cyclic quotient. For \(t>3\), no homeomorphism classification of the full dihedral quotient is claimed. The harmonic representation gives equivariant topological, not necessarily smooth or PL, conjugacy. Independent validation and an exhaustive priority search across inaccessible or unindexed literature have not been performed.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621v1 (first public 2026-09-02), Lemma 2.2, https://arxiv.org/abs/2609.02621.
2. J. A. Olarte and F. Santos, *Hypersimplicial subdivisions*, Selecta Mathematica 28 (2022), article 4 (online 2021-11-03), Section 2.3, https://doi.org/10.1007/s00029-021-00722-6.
3. *Dihedral orientation characters of bounded-independence spheres on cycles*, publicly available mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-orientation-characters-of-bounded-independence-spheres--8a099ca44501.
4. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845.
5. Topological Poincaré theorem (Perelman's proof via Ricci flow); used only to identify the resulting closed simply connected three-manifold with the three-sphere.
