# Divisor classes and cyclic singularities of the order-sixty-one Klein quartic quotient

## Finding
Let \(X\subset\mathbb P^4_{\mathbb C}\) be the smooth Klein quartic threefold cut out by
\[
 F=x_0^3x_1+x_1^3x_2+x_2^3x_3+x_3^3x_4+x_4^3x_0.
\]
Write \(\zeta\) for a primitive \(61\)-st root of unity and set
\[
 G=\left\langle\operatorname{diag}(\zeta,\zeta^{58},\zeta^9,\zeta^{34},\zeta^{20})\right\rangle,
 \qquad Y=X/G.
\]
The normal projective threefold \(Y\) has precisely five singular points, each analytically of cyclic quotient type \(\frac1{61}(8,19,33)\), with minimal log discrepancy \(22/61\) and canonical Cartier index \(61\). These singularities are klt and noncanonical.

More precisely, the natural equivariant hyperplane/character basis identifies
\[
 \operatorname{Cl}(Y)\simeq\mathbb Z\oplus\mathbb Z/61,
 \qquad\operatorname{Pic}(Y)=61\mathbb Z\oplus\{0\}.
\]
The five local divisor-class groups are each \(\mathbb Z/61\), and the image of the global-to-local map is the \(\mathbb F_{61}\)-linear span of
\[
 (1,1,1,1,1),\qquad(1,58,9,34,20).
\]
Thus \(\operatorname{Cl}(Y)/\operatorname{Pic}(Y)\simeq(\mathbb Z/61)^2\): although five singularities have local class groups of order \(61\), precisely two independent local class directions globalize.

Additionally, \(Y\) is a \(\mathbb Q\)-Fano threefold with \((-K_Y)^3=4/61\), its smooth-locus fundamental group is \(\mathbb Z/61\), and
\[
 H^*(Y,\mathbb Q)\simeq\mathbb Q[u]/(u^4),\qquad \deg u=2.
\]

## Assumptions and scope
The base field is \(\mathbb C\); the quotient is the coarse projective variety, not the quotient stack. Coordinates run over \(\mathbb Z/5\), and the five singular points are images of the coordinate points \(e_j\). The divisor-class identifications use the standard linearization on \(\mathcal O_X(1)\) and the chosen generator of \(G\). The minimal log discrepancy is computed at each closed singular point. Rational cohomology is singular cohomology of the underlying complex analytic space. All asserted equalities are exact.

## Proof
**Fixed points and local quotient types.** Put \(a=(1,58,9,34,20)\in(\mathbb Z/61)^5\). The identities \(3a_j+a_{j+1}=0\) show \(F\) is invariant. The entries of \(a\) are distinct, and \(61\) is prime. Consequently every nonidentity element of \(G\) has the same five fixed points on \(\mathbb P^4\), namely the coordinate points; all five lie on \(X\). In the chart \(x_j=1\), the partial derivative of \(F\) with respect to \(x_{j+1}\) is \(1\) at \(e_j\). The remaining variables \(x_{j+2},x_{j+3},x_{j+4}\) therefore give analytic parameters on \(X\), of weights
\[
 a_{j+2}-a_j,\ a_{j+3}-a_j,\ a_{j+4}-a_j
 \equiv (-3)^j(8,33,19)\pmod {61}.
\]
Replacing the generator by its \((-3)^j\)-th power and permuting the parameters yields the common type \(\frac1{61}(8,19,33)\). Each coordinate chart is smooth and its quotient singularity is nontrivial because all three local weights are nonzero and no nonidentity element is a pseudoreflection. Away from those five points, the quotient is étale and smooth. This proves the complete singularity basket.

**Discrepancies.** In the toric lattice \(N=\mathbb Z^3+\frac1{61}(8,19,33)\mathbb Z\), the minimal log discrepancy at the quotient origin is the smaller of \(3\) and the \(60\) ages
\[
 \frac{(8k\bmod61)+(19k\bmod61)+(33k\bmod61)}{61},
 \quad 1\le k\le60,
\]
where residues are chosen in \(\{1,\ldots,60\}\). Exact exhaustive enumeration has minimum \(22/61\), reached at \(k=39\) with residues \((7,9,6)\). This is positive but less than one, so the quotient is klt and noncanonical. The sum of weights is \(60\not\equiv0\pmod {61}\), so the local canonical index is exactly \(61\).

**Global class groups and descent.** Let \(U=X\setminus\{e_0,\ldots,e_4\}\), \(V=U/G=Y_{\mathrm{sm}}\). The finite map \(U\to V\) is a free étale \(G\)-torsor. Since \(X\) is a smooth quartic threefold, the Grothendieck–Lefschetz theorem gives \(\operatorname{Pic}(X)=\mathbb Z[\mathcal O_X(1)]\). Removing finitely many points from the smooth threefold preserves its Picard group and its invertible regular functions, so
\[
 \operatorname{Pic}(U)=\mathbb Z,\qquad\mathcal O(U)^*=\mathbb C^*.
\]
Descent identifies \(\operatorname{Pic}(V)\) with the equivariant Picard group \(\operatorname{Pic}^G(U)\). The standard hyperplane linearization gives a lift of its generator, while the kernel is the character group \(\operatorname{Hom}(G,\mathbb C^*)=\mathbb Z/61\). (Equivalently, the obstruction group \(H^2(G,\mathbb C^*)\) vanishes because \(G\) is cyclic and \(\mathbb C^*\) is divisible.) Hence
\[
 \operatorname{Pic}(V)\simeq\mathbb Z\oplus\mathbb Z/61.
\]
Since the complement of \(V\) in normal \(Y\) has codimension three, restriction identifies \(\operatorname{Cl}(Y)=\operatorname{Pic}(V)\).

Represent a class by \((m,b)\): \(\mathcal O_X(m)\) with its standard linearization twisted by \(\zeta^b\). At \(e_j\), the induced action on its fiber is \(\zeta^{b-ma_j}\). Descent to a line bundle on the coarse quotient is equivalent to trivial stabilizer action on all fibers. Thus \((m,b)\) is Cartier on \(Y\) precisely when
\[
 b-ma_j\equiv0\pmod {61}\quad\text{for every }j.
\]
Since \(a_0\ne a_1\), these five congruences are equivalent to \(m\equiv b\equiv0\pmod {61}\). Consequently \(\operatorname{Pic}(Y)=61\mathbb Z\oplus\{0\}\). The local class at the \(j\)-th point is the residue \(b-ma_j\). Therefore the exact image of \(\operatorname{Cl}(Y)\to\bigoplus_j\operatorname{Cl}(\mathcal O_{Y,p_j})\) is the span of the all-ones vector and \(a\) as stated; they are linearly independent.

**Canonical class, volume, topology.** The group acts freely in codimension one. Thus for the quotient map \(\pi:X\to Y\), \(\pi^*K_Y=K_X=-H\). The normal, projective quotient is \(\mathbb Q\)-factorial; \(-K_Y\) is ample, its Cartier index is \(61\), and
\[
 (-K_Y)^3=\frac{H^3}{\deg\pi}=\frac4{61}.
\]
By Lefschetz, \(X\) is simply connected. Removing five points in complex dimension three does not change its fundamental group, and the étale covering \(U\to V\) has deck group \(G\); hence \(\pi_1(V)=G\).

The Chern-class calculation
\[
 c(TX)=\frac{(1+H)^5}{1+4H},\qquad \int_Xc_3(TX)=-14\cdot4=-56
\]
gives \(\dim H^3(X,\mathbb Q)=60\), with four one-dimensional even cohomology groups. Each nontrivial \(g^k\) fixes precisely the five coordinate points, all with nondegenerate complex-linear fixed action. The topological Lefschetz formula yields \(L(g^k)=5\). Its trace on the four even groups is \(4\), so \(\operatorname{Tr}(g^k\mid H^3(X,\mathbb Q))=-1\). Averaging the character over the \(61\) elements gives \(H^3(X,\mathbb Q)^G=0\). Rational cohomology of a finite topological quotient is the invariant cohomology. Thus \(H^*(Y,\mathbb Q)\) has one copy of \(\mathbb Q\) in each degree \(0,2,4,6\) and nothing else; powers of an ample rational divisor generate these groups, establishing \(\mathbb Q[u]/(u^4)\).

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library. It exhaustively checks the five defining-form characters, every nonidentity power's distinct eigenweights, all five tangent representations, all \(60\) toric age candidates, the precise two-dimensional local-character image and its kernel among all \(61^2\) possible residues, the adjunction Chern numbers, and the averaged Lefschetz trace. Execute \(\texttt{python verify.py}\); a successful run prints \(\texttt{VERIFY_OK}\). The finite checker supports, but does not replace, the cited Lefschetz, equivariant descent, and quotient-singularity theorems.

## Relationship to prior work
Zhu (2026, Example 3.1(12)) provides the displayed Klein quartic equation, the order-\(61\) diagonal automorphism, and its full ambient automorphism group. González-Aguilera, Liendo, Montero and Villaflor Loyola (2022 preprint, 2024 journal) prove the automorphism and extremal-Hodge structure results, including the cyclotomic action on middle cohomology. Thus the vanishing of invariant middle cohomology is compatible with and implicit in earlier spectral results, and is not by itself claimed as a new contribution. The present result instead explicitly calculates the quotient's five noncanonical cyclic singularities, the uniform minimal log discrepancy, and especially the global Weil/Cartier distinction and the rank-two image in the five local class groups. General cyclic quotient and descent theorems are standard tools, not claimed as new.

## Limitations
The result applies to this specific order-\(61\) subgroup of the automorphism group and to the coarse quotient, not to the quotient by the full order-\(305\) group, other quartic threefolds, or an integral-cohomology computation. The displayed rational-cohomology consequence is mostly implicit in previously known middle-cohomology representations. A specialist historical search might uncover an earlier implicit quotient-divisor calculation, and no independent mathematical audit has been performed.

## References
1. Zigang Zhu, *Automorphism groups of smooth quartic threefolds*, arXiv:2610.39627v1 (first posted 2026-10-29), Example 3.1(12), Section 3.2 and Theorem 1.1. https://arxiv.org/html/2610.39627v1
2. Víctor González-Aguilera, Alvaro Liendo, Pedro Montero, Roberto Villaflor Loyola, *On a Torelli Principle for Automorphisms of Klein Hypersurfaces*, arXiv:2212.13308 (2022 preprint; Trans. Amer. Math. Soc. 377, 2024), Theorem B and Sections 4–5. https://arxiv.org/pdf/2212.13308
3. Miles Reid, *Young person's guide to canonical singularities*, Proceedings of Symposia in Pure Mathematics 46 (1987), for the age and canonical-singularity criterion.
4. Standard Grothendieck–Lefschetz, cyclic-group equivariant descent and topological Lefschetz fixed-point theorems are used as stated in the proof.
