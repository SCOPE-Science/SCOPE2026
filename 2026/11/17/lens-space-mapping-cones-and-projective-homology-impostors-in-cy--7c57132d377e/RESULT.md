# Lens-space mapping cones and projective-homology impostors in cyclic Rips quotients

## Finding
For every odd prime \(p\ge5\), define the finite metric complex \(K_p=\operatorname{VR}_{\le p-1}(C_{2p})\) and let \(C_{2p}\) act by all vertex rotations. Write \(X_p=|K_p|/C_{2p}\) for the **ordinary geometric orbit space**, not a simplicial quotient with repeated vertices or a homotopy quotient. There is a natural homeomorphism
\[
X_p\cong\operatorname{Cone}(L_p)\cup_{f}L_{2p},
\]
where \(f:L_p\to L_{2p}\) is a two-fold covering between generalized lens spaces of dimension \(p-2\). The following are exact integral conclusions:
\[
\pi_1(X_p)\cong\mathbb Z/2\mathbb Z,\qquad \pi_2(X_p)\cong\mathbb Z/p\mathbb Z,
\]
\[
H_i(X_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2\mathbb Z,&i\in\{1,3,5,\ldots,p-2\},\\
0,&\text{otherwise}.
\end{cases}
\]
Thus \(X_p\) has precisely the **integral homology of** \(\mathbb{RP}^{p-1}\) but not its homotopy type, because \(\pi_2(\mathbb{RP}^{p-1})=0\). The family realizes every odd prime as a second homotopy group while keeping the same projective-space homology pattern.

## Assumptions and scope
Fix an odd prime \(p\ge5\). The vertices of the cycle are residues \(j\in\mathbb Z/(2p)\), and the distance is the minimum number of cycle edges along either direction. A simplex of \(K_p\) is any vertex set of pairwise distance at most \(p-1\); endpoints at distance exactly \(p\) are **excluded**. A generator \(t\) acts by \(j\mapsto j+1\). All quotient spaces are geometric realizations modulo the actual finite group action.

Write \(m=(p-1)/2\). Put \(E=S^{2m-1}\subset\mathbb C^m\), with a generator of \(C_{2p}\) acting on its coordinates with complex weights \(1,3,\ldots,p-2\), i.e. multiplying coordinate \(j\) by the odd-numbered root \(\exp(2\pi i(2j-1)/(2p))\), for \(1\le j\le m\). Every weight is prime to \(2p\), so the action and its index-two subgroup action are both free. Define \(L_{2p}=E/C_{2p}\), \(L_p=E/C_p\), and let \(f:L_p\to L_{2p}\) denote the canonical cover.

## Proof
**1. Cross-polytope identification.** In \(C_{2p}\), a pair is absent from the \((p-1)\)-st power precisely when its members differ by \(p\). These are the \(p\) disjoint opposite pairs \(\{j,j+p\}\). Thus every simplex of \(K_p\) chooses at most one element of each pair. Identifying the pair with \(\{+e_j,-e_j\}\), \(K_p\) is exactly the boundary complex of the \(p\)-dimensional cross-polytope. Radial normalization gives a canonical equivariant homeomorphism \(|K_p|\cong S^{p-1}\).

**2. Orthogonal action.** In the \(e_j\) basis (indexing \(j=0,\ldots,p-1\)), the generator rotates one coordinate to the next and sends the last coordinate to the negative of the first. Consequently its real linear operator \(T\) has characteristic polynomial \(\lambda^p+1\), and \(T^p=-I\). One eigenvalue is \(-1\). The remaining \(p-1\) eigenvalues occur in complex-conjugate pairs with exponents \(1,3,\ldots,p-2\) modulo \(2p\), each coprime to \(2p\) by primality of \(p\). Therefore \(S^{p-1}\) is the suspension of the invariant equator \(E=S^{p-2}\), with \(T\) exchanging the suspension poles and acting freely on \(E\).

**3. Mapping-cone quotient.** Let \(H=\langle T^2\rangle\cong C_p\). The closed northern hemisphere is \(\operatorname{Cone}(E)\). Since \(H\) preserves it and fixes its pole, the quotient is \(\operatorname{Cone}(E/H)=\operatorname{Cone}(L_p)\). Every full-group orbit meets the northern hemisphere, and two points of its equator are identified exactly when they are in the same \(C_{2p}\)-orbit. Thus only on the boundary do we impose the additional two-to-one identification \(E/H\to E/C_{2p}\), giving the stated **homeomorphism** \(X_p\cong\operatorname{Cone}(L_p)\cup_f L_{2p}\). Compactness and the Hausdorff property guarantee that the induced continuous bijection is a homeomorphism.

**4. Fundamental and second homotopy groups.** Because \(\dim E=p-2\ge3\), the free sphere quotients \(L_p\) and \(L_{2p}\) have fundamental groups \(C_p\) and \(C_{2p}\), with \(f_*\) the index-two inclusion. Van Kampen applied to the mapping cone gives \(\pi_1(X_p)=C_{2p}/C_p\cong C_2\). The residual \(C_2\) action on \(S^{p-1}/H\) is free: away from the equator it interchanges hemispheres; on the equator a fixed point would contradict freeness of \(C_{2p}\) on \(E\). Hence \(S^{p-1}/H\to X_p\) is a two-sheeted covering. Its source is \(\Sigma L_p\) and is simply connected because \(L_p\) is connected. It is therefore the universal covering. Hurewicz and suspension give \(\pi_2(X_p)\cong\pi_2(\Sigma L_p)\cong H_2(\Sigma L_p;\mathbb Z)\cong H_1(L_p;\mathbb Z)\cong C_p\).

**5. Integral homology.** The standard lens-space cellular calculation yields for \(q=p\) or \(2p\): \(H_0(L_q)=H_{p-2}(L_q)=\mathbb Z\), \(H_i(L_q)=\mathbb Z/q\) for odd \(1\le i\le p-4\), and all other positive-degree homology zero. The top-degree homology map \(f_*:\mathbb Z\to\mathbb Z\) is multiplication by two: \(f\) is an orientation-preserving double cover. On each lower odd torsion group \(f_*:C_p\to C_{2p}\) is injective. Indeed, the transfer satisfies \(\operatorname{Tr}\circ f_* =\mathrm{id}+\tau_*\), where the nontrivial deck transformation \(\tau\) on \(L_p\) is induced by a diagonal unitary rotation on \(E\). An isotopy through diagonal unitary rotations commutes with \(H\), so \(\tau_*\) is the identity. Hence transfer followed by \(f_*\) is multiplication by two, invertible on every \(p\)-torsion group. In all odd degrees \(1\le i\le p-2\), the map is injective with cokernel of order two. All even positive homology of the lens spaces vanishes. The mapping-cone long exact sequence now gives \(H_i(X_p)=C_2\) for the specified odd degrees and zero elsewhere in positive degrees; connectedness gives \(H_0=\mathbb Z\). These equal the standard integral homology groups of \(\mathbb{RP}^{p-1}\), whose universal cover is \(S^{p-1}\); for \(p\ge5\), this has zero second homotopy group and thus proves the non-equivalence.

## Verification
The bundled `verify.py` performs exact, finite checks for \(p=5,7,11\): it enumerates all \(3^p-1\) nonempty cross-polytope faces, checks the graph-power criterion for every unordered vertex pair, verifies invariance under all cyclic shifts, checks the primitive equatorial weights, constructs compatible integer mapping-cone cellular matrices, verifies each adjacent differential composition is zero, and computes reduced homology dimensions over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_p\), and \(\mathbb F_{101}\). The last test field is replaced by 103 if \(p=101\). Its recorded output is in `verification_output.txt`. These finite computations corroborate, but do **not** replace, the universal proof above; the displayed CW matrices are a compatible arithmetic model, not a computationally established equivariant CW identification for arbitrary \(p\).

## Relationship to prior work
Adamaszek (2011), arXiv:1104.0433, determines the **nonequivariant** homotopy type of clique complexes of powers of cycles, including the cross-polytope sphere at the last noncontractible stage. Adamaszek and Adams (2015), arXiv:1503.03669, develop winding-fraction classifications and integral homology classes for critical cyclic Vietoris–Rips complexes (in particular Proposition 8.4 of its later version). Both are stronger than a mere Betti-number calculation for the covering complex, but neither inspected theorem computes the **ordinary rotation orbit space**, its lens-space mapping cone, its integral homology, or its second homotopy group. General textbook computations of lens spaces are explicitly used as a proof ingredient, not claimed as new. The novel proposed synthesis is the precise geometric orbit-space identification and its contrasting homology and homotopy across all odd primes.

## Limitations
The theorem concerns odd prime parameters and the complete rotation subgroup at the last noncontractible scale. The ordinary quotient need not be a manifold; the theorem does not classify its integral cohomology ring, action on higher homotopy groups, or analogous composite-parameter quotients. The algebraic homology calculation uses standard lens-space facts and transfer; no finite enumeration is used as a proof of the infinite family. Search evidence cannot rule out equivalent unindexed literature. Independent mathematical validation and definitive priority assessment are outstanding.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, first posted 2011-04-03, arXiv:1104.0433, https://arxiv.org/abs/1104.0433 (especially §§6–7).
2. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, first posted 2015-03-12, arXiv:1503.03669, https://arxiv.org/abs/1503.03669 (especially §§4, 8 and Proposition 8.4).
3. Standard lens-space cell-structure, transfer, mapping-cone exact sequence, and Hurewicz theorems, as in A. Hatcher, *Algebraic Topology*, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
