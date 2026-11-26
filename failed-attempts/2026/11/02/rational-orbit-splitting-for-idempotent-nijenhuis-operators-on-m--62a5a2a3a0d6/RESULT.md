# Rational orbit splitting for idempotent Nijenhuis operators on \(\mathfrak{sl}_2\)

## Finding

Let \(k=\mathbb F_q\) with \(q\) an odd prime power and let \(\mathfrak g=\mathfrak{sl}_2(k)\). Define the Nijenhuis torsion of a \(k\)-linear endomorphism \(N\) by
\[
\mathcal T_N(x,y)=[Nx,Ny]-N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr).
\]
Let \(\mathcal P_q\) denote the set of endomorphisms with \(N^2=N\) and \(\mathcal T_N(x,y)=0\) for all \(x,y\in\mathfrak g\). The following gives its complete \(\operatorname{PGL}_2(k)\)-conjugacy classification.

**Theorem.** There are exactly eight conjugacy orbits on \(\mathcal P_q\): the singleton orbits \(\{0\}\) and \(\{I\}\), together with three rank-one orbits and three rank-two orbits. In each of ranks one and two the three orbits have respective sizes
\[
q(q+1),\qquad \frac{q(q^2-1)}2,\qquad \frac{q(q^2-1)}2.
\]
The first orbit has a nilpotent complementary line and the latter two correspond to the two square classes of a nonzero discriminant coordinate. Their representatives are explicit below. In particular,
\[
|\mathcal P_q|=2q^2(q+1)+2.
\]
The total is a straightforward consequence of the classical projection criterion and the known subalgebra-plane count; the contribution claimed here is the **rational conjugacy-orbit spectrum**, with the square-class distinction, and its geometric organization.

Over any algebraically closed field of characteristic different from two, the underlying reduced algebraic variety of idempotent Nijenhuis operators has four disjoint smooth geometrically irreducible components: two points (ranks zero and three) and two three-dimensional components (ranks one and two). Each threefold is a Zariski-locally trivial affine \(\mathbb A^2\)-bundle over \(\mathbb P^1\). Each threefold has a smooth closed two-dimensional nilpotent-complement orbit and a single open dense semisimple-complement orbit. Over \(\mathbb F_q\), that open orbit divides into the two displayed rational square-class orbits.

## Assumptions and scope

Use the standard basis
\[
f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
e=\begin{pmatrix}0&1\\0&0\end{pmatrix}
\]
with \([h,e]=2e\), \([h,f]=-2f\), and \([e,f]=h\). Put \(\mathfrak b=kh\oplus ke\). For \(u\in k\), define the rank-one projection \(P_u\) with kernel \(\mathfrak b\) and image \(k(f+ue)\):
\[
P_u(f)=f+ue,\qquad P_u(h)=P_u(e)=0.
\]
Choose a fixed nonsquare \(\eta\in k^\times\). Complete representatives are
\[
0,\quad I,\quad P_0,\;P_1,\;P_\eta,\quad I-P_0,\;I-P_1,\;I-P_\eta.
\]
Here the two nonzero-coordinate types are distinguished by the square class of \(u\). The familiar split/nonsplit nature of the nonnilpotent image line is controlled by the square class of \(-u\), so its verbal labeling depends on whether \(-1\) is a square. All counts are for \(k\)-linear operators and \(k\)-rational \(\operatorname{PGL}_2\)-conjugacy, not semilinear conjugacy or arbitrary Nijenhuis operators.

## Proof

**1. Projector criterion.** Write \(\mathfrak g=A\oplus B\), where \(A=\operatorname{im}N\) and \(B=\ker N\), for an idempotent \(N\). Substitution of \(x=a+b\) and \(y=a'+b'\) into the torsion identity gives
\[
\mathcal T_N(x,y)=(I-N)[a,a']+N[b,b'].
\]
Thus \(N\) is Nijenhuis exactly when \(A\) and \(B\) are Lie subalgebras; this classical equivalence is not a new assertion. All lines are Lie subalgebras, so nontrivial projections require exactly that their two-dimensional image or kernel be a Lie subalgebra.

**2. Every two-dimensional Lie subalgebra is a Borel.** The bilinear form \(\langle x,y\rangle=\operatorname{tr}(xy)\) is nondegenerate on \(\mathfrak g\) when \(\operatorname{char}k\ne2\). A two-dimensional Lie subalgebra \(H\) is nonabelian: the centralizer of any nonzero traceless \(2\times2\) matrix in \(\mathfrak g\) has dimension one. If \(x,y\) span \(H\), then \(0\ne w=[x,y]\in H\). Invariance of the trace form makes \(w\) orthogonal to \(x\) and \(y\). Hence \(H=w^\perp\) and \(\operatorname{tr}(w^2)=0\), implying that \(w\) is nilpotent by Cayley–Hamilton. Therefore \(H\) is the stabilizer of the unique kernel line of \(w\), and all such \(H\) are the standard Borel conjugates. The Borel variety is \(\mathbb P^1\) and has \(q+1\) rational points.

**3. Incidence parameter space.** Fix a Borel \(H\). The complementary lines in \(\mathfrak g\) form an affine two-space: they are graphs of linear splittings of \(\mathfrak g\twoheadrightarrow\mathfrak g/H\). As \(H\) varies in \(\mathbb P^1\), these splittings form a Zariski-locally trivial affine \(\mathbb A^2\)-bundle (an affine torsor, not necessarily a vector bundle). A projection is uniquely determined by its image and kernel. Thus rank one and rank two each form this smooth geometrically irreducible threefold. Rank zero and rank three each consist of one point. The rank strata are open and closed within the reduced idempotent locus because the characteristic polynomial of an idempotent of rank \(r\) is \(t^{3-r}(t-1)^r\), distinct for \(r=0,1,2,3\) in every characteristic.

**4. Rational orbit calculation.** The group \(G=\operatorname{PGL}_2(k)\) acts transitively on the \(q+1\) Borels. Fix \(\mathfrak b\). Its complement lines are uniquely
\[
\ell_{a,b}=k(f+ah+be),\qquad (a,b)\in k^2.
\]
For an upper triangular representative \(g=\begin{psmallmatrix}t&s\\0&1\end{psmallmatrix}\), \(t\ne0\), direct conjugation of the displayed matrices sends
\[
(a,b)\longmapsto (s+ta,\;-s^2-2sta+t^2b).
\]
Consequently the parameter \(u=b+a^2\) obeys \(u\mapsto t^2u\). Translation in \(s\) first moves \(a\) to zero, leaving precisely three rational orbits: \(u=0\); \(u\) a nonzero square; and \(u\) a nonsquare. Their sizes inside one affine complement fibre are, respectively, \(q\), \(q(q-1)/2\), and \(q(q-1)/2\). Since \(G\) has \(q+1\) Borel cosets, multiplying gives the three asserted global orbit sizes. Stabilizer orders are \(q-1\), \(2\), and \(2\). The same calculation applies to rank two by \(N\mapsto I-N\).

The discriminant interpretation follows from
\[
\det(f+ah+be)=-a^2-b=-u.
\]
The vanishing locus \(u=0\) is a smooth affine line in each complement fibre, giving the closed two-dimensional orbit. Over an algebraically closed field every nonzero \(u\) is a square, giving one open three-dimensional orbit per rank. Over \(k\) the nonzero coordinate splits into the two rational orbits. Finally each rank-one or rank-two component has \((q+1)q^2\) points and the two singleton ranks yield the total \(2q^2(q+1)+2\). This completes the classification.

## Verification

The standalone checker `check_nijenhuis.py` constructs the original \(\mathfrak{sl}_2\) bracket, directly evaluates \(N^2=N\) and the Nijenhuis torsion on basis pairs for all constructed projections, enumerates all two-dimensional subalgebras, and computes the three stabilizer-fibre orbit sizes. It independently computes all \(\operatorname{PGL}_2\)-conjugacy orbits by explicit matrix conjugation for \(q=3,5\). It exhaustively checks all \(3^9\) endomorphism matrices over \(\mathbb F_3\) against the classification; for \(q=5,7,9\), it exhaustively checks the candidate projection parameter space, not all ambient matrices. The \(q=9\) case uses the genuine degree-two extension field \(\mathbb F_3[z]/(z^2+1)\). The accompanying `verification_output.txt` records all four successful cases.

## Relationship to prior work

Cariñena, Grabowski, and Marmo already established the Nijenhuis projection criterion for two complementary Lie subalgebras (arXiv:math/0103103, Theorem 5); that step and the idea of projection contractions are prior art. Liu–Sheng–Zhou–Bai describe a broader Nijenhuis-operator framework for higher Lie products (arXiv:1601.02356), not the present finite-field rational orbit count. Mosbahi (arXiv:2609.09392, Theorem 3.1) gives a close 2026 classification of complex Nijenhuis operators for three-dimensional simple BiHom-Lie algebras, explicitly including the untwisted complex \(\mathfrak{sl}_2\) case. It does not state the arithmetic rational-orbit sizes or square-class splitting for odd finite fields. A previously published account, *Plane counts control subalgebra commutativity in dimension three*, proves that perfect three-dimensional Lie algebras have \(q+1\) subalgebra planes; it makes the unweighted total count elementary and is not evaded by a different title. Its full result does not provide the eight operator-conjugacy orbits or the two rational semisimple types. A previous classification of rank-one weight-zero Rota–Baxter operators on \(\mathfrak{sl}_2\) concerns a different operator identity.

The new assertion is restricted to the eight rational conjugacy orbits and their sizes, including the geometric-to-rational orbit splitting, rather than the already-known projection criterion, Borel count, or general complex operator parametrization. The comparison cannot establish absolute historical priority; a more general treatment of rational orbits of Lie-algebra factorisations could still subsume it.

## Limitations

The theorem excludes characteristic two and applies only to **idempotent** Nijenhuis operators on \(\mathfrak{sl}_2\), not all Nijenhuis operators or higher-rank simple Lie algebras. Geometry concerns the reduced varieties, not a claim about global reducedness of the complete defining scheme. Orbits are under \(\operatorname{PGL}_2\), not semilinear automorphisms. No independent mathematical audit has been performed; publication-priority verification remains provisional.

## References

1. J. F. Cariñena, J. Grabowski and G. Marmo, *Contractions: Nijenhuis and Saletan tensors for general algebraic structures*, arXiv:math/0103103 (first public version 2001-03-16), https://arxiv.org/abs/math/0103103.
2. J. Liu, Y. Sheng, Y. Zhou and C. Bai, *Nijenhuis operators on n-Lie algebras*, arXiv:1601.02356 (first public version 2016-01-11), https://arxiv.org/abs/1601.02356.
3. B. Mosbahi, *Classification of Nijenhuis operators on three-dimensional multiplicative simple BiHom-Lie algebras*, arXiv:2609.09392 (2026-09-08), https://arxiv.org/abs/2609.09392.
4. *Plane counts control subalgebra commutativity in dimension three*, published full result, https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c/RESULT.md.
