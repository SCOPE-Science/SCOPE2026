# The six-cycle quotient of the type-\(A_5\) Coxeter sphere is a Moore space

## Finding
Let \(K=\operatorname{sd}(\partial\Delta^5)\) be the barycentric subdivision of the boundary of the simplex on the six vertices \(\mathbb Z/6\mathbb Z\). Its standard type-\(A_5\) Coxeter-complex realization is a triangulated four-sphere. Let \(C_6=\langle g\rangle\) act by \(g(j)=j+1\pmod 6\). The **ordinary geometric quotient**
\[
Q=|K|/C_6
\]
has the integral homotopy type
\[
\boxed{Q\simeq M(\mathbb Z/2\mathbb Z,3)\simeq \Sigma^2\mathbb RP^2,}
\]
where \(M(\mathbb Z/2\mathbb Z,3)\) is the mapping cone of the degree-two map \(S^3\longrightarrow S^3\). In particular, \(\pi_1(Q)=\pi_2(Q)=0\), and
\[
\widetilde H_j(Q;\mathbb Z)=
\begin{cases}\mathbb Z/2\mathbb Z,&j=3,\\0,&j\ne3.\end{cases}
\]

## Assumptions and scope
The simplex is the ordinary abstract five-simplex with six labeled vertices, the cyclic action is the long six-cycle, and quotient means quotient of the **realization** rather than the abstract simplicial complex formed from vertex orbits. The subdivision is equivariant and does not alter the quotient homeomorphism type. No claim is made about other cyclic orders or other Coxeter types.

## Proof
**1. Equivariant linear model.** Map the boundary of the simplex radially from its barycenter to the unit sphere of the reduced real permutation representation
\[
V=\{(x_0,\ldots,x_5)\in\mathbb R^6:\sum x_i=0\}.
\]
This is an equivariant homeomorphism. Writing \(\zeta=e^{2\pi i/6}\), the real Fourier decomposition is
\[
V\cong\mathbb R_{\mathrm{sgn}}\oplus\mathbb C_1\oplus\mathbb C_2,
\qquad g(t,z,w)=(-t,\zeta z,\zeta^2w).
\]
The unit sphere of \(V\) is the suspension of \(S^3\subset\mathbb C^2\), with \(g\) exchanging the two suspension tips.

**2. A mapping-cone decomposition.** The normal subgroup \(H=\langle g^2\rangle\cong C_3\) fixes the suspension coordinate and acts on \(S^3\) by \((z,w)\mapsto(\omega z,\omega^2w)\), where \(\omega=\zeta^2\). Both weights are nonzero modulo three, so this action is free. Therefore
\[
S(V)/H\cong\Sigma L,\qquad L=S^3/H=L(3;1,2).
\]
The residual involution of \(C_6/H\) interchanges the suspension cones and acts on their shared equator by the involution \(\tau[z,w]=[-z,w]\), because \(g^3\) represents the nontrivial coset. Identify the upper cone with a fundamental domain. Its boundary is identified via \(\tau\), giving the actual **mapping cone**
\[
Q\cong\operatorname{Cone}(f),\qquad f:L\longrightarrow L/\tau.
\]
This uses the usual mapping-cone convention of attaching a cone over the domain to the target along \(f\).

**3. The quotient equator and induced maps.** The involution \(\tau\) on \(S^3\) changes \(z\) to \(-z\). Its quotient is homeomorphic to \(S^3\) via
\[
\Phi(z,w)=\begin{cases}(z^2/|z|,w),&z\ne0,\\(0,w),&z=0.\end{cases}
\]
This map doubles the angular coordinate of \(z\), is two-to-one away from \(z=0\), and preserves the sphere radius. It conjugates the residual \(C_3\)-action to \((u,w)\mapsto(\omega^2u,\omega^2w)\), which is free. Thus \(L/\tau\cong L(3;2,2)\) is another lens space. Both \(L\) and \(L/\tau\) have \(H_1\cong\pi_1\cong\mathbb Z/3\), \(H_3\cong\mathbb Z\), and no positive-degree homology otherwise. The map \(f_*:\pi_1(L)\to\pi_1(L/\tau)\) is an isomorphism: under the two free \(C_3\) models, the \(C_3\)-equivariant map \(\Phi\) identifies deck transformations by the same group element. The map \(f_*:H_3(L;\mathbb Z)\to H_3(L/\tau;\mathbb Z)\) is multiplication by \(2\), since \(f\) is a two-sheeted orientation-preserving map away from its codimension-two branch circle.

**4. Integral and homotopy conclusions.** The mapping-cone long exact homology sequence for \(f\) now gives \(H_4(Q)=0\), \(H_3(Q)=\operatorname{coker}(\mathbb Z\xrightarrow{\times2}\mathbb Z)=\mathbb Z/2\), \(H_2(Q)=0\), and \(H_1(Q)=0\). Van Kampen gives \(\pi_1(Q)=\pi_1(L/\tau)/\langle\langle f_*\pi_1(L)\rangle\rangle=1\); Hurewicz then gives \(\pi_2(Q)=0\) and \(\pi_3(Q)\cong\mathbb Z/2\). Represent the nonzero element of \(\pi_3(Q)\) by \(S^3\to Q\). Its double is nullhomotopic, so this map extends to the cofiber of degree two, \(M(\mathbb Z/2,3)\). The extension induces an isomorphism on all integral homology groups. Both spaces are simply connected CW complexes, so the homological Whitehead theorem yields the asserted homotopy equivalence.

## Verification
A standalone finite-cell verifier constructs all nonempty chains of nonempty proper subsets of the six-set, takes their simultaneous cyclic-rotation orbits, and forms the exact signed quotient boundaries in each dimension. The quotient cell counts are \((12,91,260,300,120)\) in dimensions zero through four; all integral consecutive boundary compositions vanish. Over \(\mathbb F_2\) its Betti vector is \((1,0,0,1,1)\), while over each of \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) it is \((1,0,0,0,0)\). These are separate finite consistency checks of the **same topological object**, not a substitute for the integer mapping-cone argument. Run `python verify_cyclic6.py`; expected output is in `VERIFIER_OUTPUT.txt`.

## Relationship to prior work
The type-\(A\) Coxeter-complex and subgroup-quotient cellular framework appear in Babson and Reiner (2004), especially their Sections 2.1, 2.3 and 4.1. Their quotient face-poset construction distinguishes flags from naive vertex-orbit complexes. An explicit May 2016 discussion by Reiner concerns correct double-coset incidences, rather than the present homotopy computation. Donau (2012) computes prime-cyclic partition-lattice quotients, a different complex and different stabilizer situation. These sources provide context or general methods; the specific order-six quotient and Moore-space identification were not located in the inspected material.

## Limitations
The statement concerns precisely the ordinary quotient of the six-vertex Coxeter sphere under the specified cyclic group. It does not give a classification for other orders. The literature check cannot exclude equivalent results hidden in unindexed or inaccessible works. The embedded verifier tests exact finite boundary identities and several fields; the infinite and integral homotopy assertions rest on the fully explicit mapping-cone proof, not on sampling primes.

## References
1. E. Babson and V. Reiner, *Coxeter-like complexes*, Discrete Mathematics and Theoretical Computer Science 6 (2004), 223–252, https://doi.org/10.46298/dmtcs.312 ; full text https://www.maths.tcd.ie/EMIS/journals/DMTCS/pdfpapers/dm060205.pdf .
2. V. Reiner, response to *Quotient of Coxeter complex in terms of double cosets?*, MathOverflow, May 11, 2016, https://mathoverflow.net/questions/238519/quotient-of-coxeter-complex-in-terms-of-double-cosets .
3. R. Donau, *Quotients of the topology of the partition lattice which are not homotopy equivalent to wedges of spheres*, arXiv:1202.4368 (2012), https://arxiv.org/abs/1202.4368 .
4. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), for mapping cones, Hurewicz and Whitehead theorems.
