# A doubly suspended lens universal cover for singular type-\(B_{2p}\) Coxeter quotients

## Finding
For every odd prime \(p\ge3\), the ordinary Coxeter-element quotient \(X_p=|\Sigma(B_{2p})|/\langle c\rangle\) has a universal fourfold covering of the explicit homeomorphism type
\[
\widetilde X_p\cong \Sigma^2L^{2p-3}\bigl(p;1,3,\ldots,2p-1\text{ with }p\text{ omitted}\bigr),
\]
with the remaining weights reduced modulo \(p\). In particular
\[
\pi_1(X_p)\cong C_4,\qquad \pi_2(X_p)=0,\qquad \pi_3(X_p)\cong C_p,
\]
and the deck action on the third homotopy group is trivial. The full integral homology of the *ordinary geometric quotient* is
\[
H_k(X_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,2p-1,\\
\mathbb Z/4,&k=1,\\
\mathbb Z/(4p),&3\le k\le2p-3\text{ and }k\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]
The homology calculation by itself is covered in principle by Kawasaki's general weighted-lens formulas; the stated geometric universal-cover description and resulting low homotopy information are the distinguishing structural conclusions here.

## Assumptions and scope
The prime \(p\) is odd and at least three. The type-\(B_{2p}\) Coxeter complex is the unit-sphere triangulation of the coordinate/sign reflection arrangement in \(\mathbb R^{2p}\), hence has geometric realization \(S^{2p-1}\). Its Coxeter element is the orthogonal signed cycle
\[
c(e_i)=e_{i+1}\quad(1\le i<2p),\qquad c(e_{2p})=-e_1.
\]
The quotient is the orbit space of this *actual geometric action*, not a Borel construction. The notation \(L^{2p-3}(p;A_p)\) means the quotient of \(S^{2p-3}\subset\mathbb C^{p-1}\) by a generator of \(C_p\) acting in the listed character weights, all coprime to \(p\). Suspensions are ordinary unreduced suspensions; for this connected lens space the iterated suspension coincides up to pointed homeomorphism with the join \(S^1*L\).

## Proof
**1. Character weights and stabilizers.** Since \(c^{2p}=-I\), it has order \(4p\) and characteristic polynomial \(t^{2p}+1\). Regard the real representation as the underlying real space of \(p\) complex character lines with eigenweights \(1,3,\ldots,2p-1\) modulo \(4p\). This follows by pairing conjugate roots of \(t^{2p}+1\); the paired weights are the listed odd residues strictly between zero and \(2p\). Exactly one is divisible by \(p\), namely weight \(p\), and no listed weight is even. Every nontrivial point stabilizer is therefore contained in the unique subgroup \(P=\langle c^4\rangle\cong C_p\), and the entire subgroup \(P\) fixes the weight-\(p\) complex axis. The complement of that axis has no nonzero fixed vectors for any nonidentity element of \(P\).

**2. Universal cover as a double suspension.** Write the representation as \(U\oplus V\), where \(U\cong\mathbb C\) is the weight-\(p\) line and \(V\cong\mathbb C^{p-1}\) is its orthogonal complement. Equivariant radial coordinates give a homeomorphism of spheres
\[
S(U\oplus V)\cong S(U)*S(V),
\]
with \(P\) acting trivially on \(S(U)\cong S^1\) and freely on \(S(V)\cong S^{2p-3}\). Therefore
\[
S^{2p-1}/P\cong S^1*(S(V)/P)
\cong\Sigma^2L^{2p-3}(p;A_p).
\]
The connected lens factor makes this join simply connected (indeed 2-connected): its reduced homology begins in degree three, and a double suspension of a connected CW complex has no homotopy in degrees one or two. The residual group \(\langle c\rangle/P\cong C_4\) acts freely on \(S^{2p-1}/P\): a hypothetical fixed orbit by a nonidentity coset would give a fixed vector for a power of \(c\) outside \(P\), contrary to Step 1. Thus this explicit fourfold covering is universal and \(\pi_1(X_p)\cong C_4\).

**3. First nontrivial higher homotopy and monodromy.** A dimension-\((2p-3)\) ordinary lens space has \(H_1\cong C_p\) and integral homology \(C_p\) in every lower positive odd degree. Suspension shifts reduced homology by two. Hence \(H_3(S^{2p-1}/P;\mathbb Z)\cong C_p\), whereas its first two reduced homology groups vanish. By Hurewicz for the 2-connected cover,
\[\pi_2(X_p)=0,\quad \pi_3(X_p)\cong C_p.\]
The diagonal torus of the character-line decomposition is path connected, commutes with the cyclic action and contains \(c\). Its induced maps on the intermediate quotient are homotopic to the identity, so the residual deck action on \(\pi_3\) is trivial.

**4. Integral homology and torsion exponents.** At the prime \(p\), transfer/averaging for the residual free \(C_4\)-action identifies localized homology of \(X_p\) with the invariant homology of \(S^{2p-1}/P\). The torus isotopy makes that action trivial on homology; thus the \(p\)-primary positive-degree homology is \(C_p\) in odd degrees \(3,5,\ldots,2p-3\), and zero elsewhere except the integral top class. At the prime two, instead take \(Q=\langle c^p\rangle\cong C_4\). Every nonidentity element of \(Q\) acts without fixed points because all character weights are odd. Consequently \(S^{2p-1}/Q\) is an ordinary dimension-\((2p-1)\) lens space, having \(C_4\) homology in each odd degree \(1,3,\ldots,2p-3\). Its remaining quotient by \(P\) has the same two-local homology by averaging, again with trivial induced action by torus isotopy. At primes other than \(2,p\), averaging for the full group identifies homology with that of the sphere. Combining primary pieces of finitely generated abelian groups yields \(C_4\) in degree one and \(C_{4p}\) in all subsequent odd degrees below the top; orientations of the original orthogonal action are positive, so the top integral homology is \(\mathbb Z\). This proves the displayed formula.

## Verification
The self-contained script `verify_b6.py` constructs a simplicial product/join model for the type-\(B_6\) example, using three twelve-cycles and cyclic weights \((1,3,5)\). It constructs the ordinary quotient cellular boundary operators, checks all consecutive compositions vanish, and performs exact finite-field Gaussian elimination for characteristics two, three, five and seven. The calculated mod-two Betti numbers are all one in degrees zero through five; the mod-three Betti numbers are one precisely in degrees zero, three, four and five; mod-five and mod-seven Betti numbers are one only in degrees zero and five. These agree with the integral prediction through universal coefficients. The script verifies the smallest odd-prime instance but does **not** certify the infinite theorem, its integral exponents or the universal-cover homeomorphism; these rest on the proof above.

## Relationship to prior work
The sphere realization and action of the finite Coxeter group are classical, recalled for example by Petersen (2016); the general theory of Coxeter elements is treated by Reiner, Ripoll and Stump (2014). Kawasaki (1973) computed cohomology for twisted projective spaces and lens complexes; Bahri, Franz and Ray (2011 preprint, 2014 journal) explicitly reproduce the general weighted-lens-space cohomology formulas. Accordingly **neither the weighted-lens description nor the homology groups alone are claimed original here**. The additional statement identifies this Coxeter family’s universal cover geometrically as a specific double suspension, with nontrivial order-\(p\) third homotopy and a trivial fourfold deck action. The existing generic weighted-lens cohomology results do not state this covering-homeomorphism and 3-type for the Coxeter family. Bari and Hunsicker (2019) consider orbifold lens spectra, not this low homotopy calculation. This is a specialized geometric structural refinement rather than a general theory of all weighted-lens spaces.

## Limitations
This result does not identify the complete homotopy type of \(X_p\) (the asserted complete homotopy description is only for its universal cover). The general weighted-lens cohomology part is known and cannot establish novelty by itself. Kawasaki’s original 1973 full text was unavailable during source inspection; the exact cohomological content was checked in the full, openly available Bahri–Franz–Ray exposition (Section 2), which specifically attributes it to Kawasaki. The possibility of an unindexed prior statement of this universal-cover specialization remains a publication-priority risk.

## References
1. A. Bahri, M. Franz and N. Ray, *Weighted projective spaces and iterated Thom spaces*, arXiv:1109.2359v1 (first posted 2011-09-11), Section 2 (notably Definition 2.3 and equation (2.16)); https://arxiv.org/abs/1109.2359.
2. V. Reiner, V. Ripoll and C. Stump, *On non-conjugate Coxeter elements in well-generated reflection groups*, arXiv:1404.5522v1 (2014-04-22); https://arxiv.org/abs/1404.5522.
3. T. K. Petersen, *A two-sided analogue of the Coxeter complex*, arXiv:1607.00086v1 (2016-07-01); https://arxiv.org/abs/1607.00086.
4. T. Kawasaki, *Cohomology of twisted projective spaces and lens complexes*, Math. Ann. 206 (1973), 243–248; https://doi.org/10.1007/BF01429212.
5. F. Bari and E. Hunsicker, *Isospectrality for Orbifold Lens Spaces*, DOI 10.4153/S0008414X19000178 (2019); https://doi.org/10.4153/S0008414X19000178.
