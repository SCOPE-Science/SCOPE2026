# Motivic collapse of the four Frobenius types of pentagon-boundary degree-five del Pezzo surfaces

## Finding

Let \(k=\mathbb F_q\) be any finite field (including characteristic \(2\)), let \(Y/k\) be a smooth del Pezzo surface of degree \(5\), and suppose a reduced geometrically simple-normal-crossings anticanonical divisor \(D\subset Y\) consists of five geometric \((-1)\)-curves meeting in a pentagon. Write \(U=Y\setminus D\), \(\mathbb L=[\mathbb A^1_k]\) in \(K_0(\operatorname{Var}_k)\), and \(\mathbb E_j=[\operatorname{Spec}\mathbb F_{q^j}]\). Frobenius on the five vertices belongs to the dihedral group \(D_5\), and its four conjugacy types are identity, one-step rotations, two-step rotations, and reflections.

For *every* such pair, the exact class of the open surface in the full Grothendieck ring is
\[
\boxed{[U]=\begin{cases}\mathbb L^2+1,&\text{identity or either rotation type},\\\mathbb L^2-1+\mathbb E_2,&\text{reflection type}.\end{cases}}
\]
In particular, the three non-reflection arithmetic forms have the same motivic class even though their marked Frobenius conjugacy classes are distinct. Every one of the four types occurs over every finite field. The complete point counts and zeta functions are
\[
\#U(\mathbb F_{q^n})=q^{2n}+\varepsilon^n\quad(n\ge1),\qquad
Z(U/k,T)=\frac1{(1-q^2T)(1-\varepsilon T)},
\]
where \(\varepsilon=1\) for an identity or rotational action and \(\varepsilon=-1\) for a reflection. Moreover, for every \(\ell\ne\operatorname{char}(k)\),
\[
H_c^i(U_{\overline k},\mathbb Q_\ell)=0\ (i\ne2,4),\quad
H_c^2\cong\mathbb Q_\ell(\varepsilon),\quad
H_c^4\cong\mathbb Q_\ell(-2).
\]
Here \(\mathbb Q_\ell(\varepsilon)\) denotes the one-dimensional unramified representation on which geometric Frobenius acts by \(\varepsilon\); its sign is exactly the orientation character of the pentagon dual graph.

## Assumptions and scope

The pair \((Y,D)\) is defined over \(k\), its five components are geometrically smooth rational \((-1)\)-curves, and its only intersections are five distinct transverse nodes, with exactly two components through each node. All formulas concern the reduced complement, not arbitrary boundaries on a degree-five del Pezzo surface. The Grothendieck class is an equality in \(K_0(\operatorname{Var}_k)\), stronger than the finite-field point-count realization. The Frobenius type refers to the action on the cyclically ordered *five geometric components*, not just the conjugacy class of the complete surface.

## Proof

**1. Pentagon classification and integral lattice.** Over \(\overline k\), a degree-five del Pezzo surface is the blowup of \(\mathbb P^2\) in four points in general position. Its ten \((-1)\)-curves are the four exceptional divisors and the six lines through pairs of points. Their intersection graph is the Petersen graph. It has exactly twelve unoriented five-cycles. A five-cycle consists of five classes whose sum is \(-K_Y\), and these classes form a \(\mathbb Z\)-basis of \(\operatorname{Pic}(Y_{\overline k})\). The integral-basis fact also appears in Harpaz, Lemma 3.3.10; the included exact checker enumerates all twelve cycles and verifies each determinant is \(\pm1\) with the explicit blowup intersection form. The automorphism group of the pair over an algebraically closed field is the dihedral stabilizer of this cycle, of order ten. Hence Frobenius acts as a rotation or reflection, with the four stated \(D_5\) conjugacy classes. A twist of a split pentagon pair by any element of this constant finite group exists over every finite field (the Galois group is procyclic), establishing occurrence.

**2. Three classes for the complete degree-five surfaces.** The isomorphism class of \(Y\) over a finite field depends only on the Frobenius class in its geometric automorphism group \(S_5\). Write \(\mathbb E_j=[\operatorname{Spec}\mathbb F_{q^j}]\). In the identity case \(Y\) is a blowup of four rational plane points, so
\[
[Y]=[\mathbb P^2]+4\mathbb L=\mathbb L^2+5\mathbb L+1.
\]
For either nontrivial rotation, the element is a five-cycle in \(S_5\). Take a degree-five closed point on a smooth rational conic in \(\mathbb P^2_k\), blow it up, and contract the strict transform of the conic, which has self-intersection \(-1\) and is \(\mathbb P^1_k\). A degree-five closed point exists on a conic over every \(\mathbb F_q\); five distinct points on it satisfy the no-three-collinear condition. The resulting degree-five del Pezzo has Frobenius five-cycle, and the blowup and blowdown relations give
\[
[Y]=[\mathbb P^2]+\mathbb L\mathbb E_5-\mathbb L=\mathbb L^2+1+\mathbb L\mathbb E_5.
\]
For a reflection, its permutation in \(S_5\) has cycle type \((2,2,1)\). A blowup of \(\mathbb P^2_k\) at two distinct degree-two closed points in general position has this Frobenius type. Such points exist in general position for every \(q\): choose points on different rational lines, avoiding the finitely many incompatible choices; for \(q=2\), one may take any two distinct quadratic orbits, whose rational spanning lines differ. Consequently
\[
[Y]=[\mathbb P^2]+2\mathbb L\mathbb E_2=\mathbb L^2+\mathbb L+1+2\mathbb L\mathbb E_2.
\]
All these constructions give actual smooth surfaces, not merely rationalized classes. Equality of these forms for the same \(S_5\) Frobenius conjugacy type follows from finite-field Galois twist classification of the split degree-five surface (its geometric automorphism group is the constant \(S_5\)).

**3. The boundary's exact scissor class.** Let \(V\) be the finite étale Galois set of geometric components, \(E\) the finite étale set of nodes, and \(B\) the degree-ten finite étale incidence set of pairs (component,node lying on it). Every component normalizes to a projective line over its finite field of definition, since every conic over a finite field has a point. The normalization and conductor scissor identity is
\[
[D]=(\mathbb L+1)[V]-[B]+[E].
\]
For the identity: \([V]=[E]=5\) and \([B]=10\), so \([D]=5\mathbb L\). For either nontrivial rotation: \([V]=[E]=\mathbb E_5\), \([B]=2\mathbb E_5\), so \([D]=\mathbb L\mathbb E_5\). For a reflection: both vertex and edge permutations have one fixed point and two transpositions, while the ten incident flags have five transpositions (no fixed flags); thus
\[
[V]=[E]=1+2\mathbb E_2,\qquad[B]=5\mathbb E_2,
\quad [D]=\mathbb L+2+2\mathbb L\mathbb E_2-\mathbb E_2.
\]
Subtracting these three displayed divisor classes from their corresponding \([Y]\) expressions proves the two announced Grothendieck-ring equalities, with no division, motivic localization, or characteristic restriction.

**4. Point counts, zeta, and the orientation representation.** The point-count homomorphism sends \(\mathbb L\) to \(q^n\) and \(\mathbb E_2\) to \(0\) for odd \(n\), \(2\) for even \(n\), giving the stated \(q^{2n}+\varepsilon^n\) count. Taking the exponential generating function gives the zeta formula. Independently, the geometric dual graph is a circle, so \(H^1(D_{\overline k},\mathbb Q_\ell)\) has dimension one and Frobenius acts by its orientation sign. Since the five component classes are an integral Picard basis, the restriction \(H^2(Y_{\overline k},\mathbb Q_\ell)\to H^2(D_{\overline k},\mathbb Q_\ell)\) is an isomorphism (the curve-intersection matrix is unimodular). The compact-support localization sequence therefore yields \(H_c^2(U)\cong H^1(D)\) and \(H_c^4(U)\cong H^4(Y)=\mathbb Q_\ell(-2)\), with every other compact-support cohomology group zero. On a pentagon, rotations preserve and reflections reverse orientation, proving the claimed eigenvalue sign without relying on point-count extrapolation.

## Verification

Run `python3 check_pentagon.py` using standard Python 3. The program independently constructs all ten exceptional classes, enumerates the twelve geometric pentagons and their 120 oriented orderings, checks the five-cycle intersection matrices and anticanonical sums, exhaustively tests the ten dihedral permutations and their first twenty powers over five sample field sizes, checks blowup point counts, verifies the reflection's explicit affine point count over five prime fields, and checks all three *formal* Grothendieck-ring scissor identities. The actual recorded output is in `verification_output.txt` and ends in `ALL_TESTS_PASSED`. This finite testing is only corroboration; the proof above supplies all quantifiers and the characteristic-free geometric identities.

## Relationship to prior work

Harpaz (2015), Theorem 3.3.2 and Lemma 3.3.10, identifies these pentagon-boundary log K3 pairs via \(D_5\)-valued Galois classes in characteristic zero and establishes the unimodular boundary Picard basis. In particular its explicit affine models for the split and quadratic/reflection types imply their respective \(q^2+1\) and \(q^2-1\) counts in odd characteristic, and its Proposition 3.2.8 already identifies \(H_c^2\) with the orientation-sign character in characteristic zero: **none of these special cases or the known cohomology character is claimed as new**. Banwait–Fité–Loughran (2016) determine finite-field Frobenius traces of complete del Pezzo surfaces; our complete-surface counts and possible \(S_5\) Frobenius classes are therefore antecedents. Boitrel (2023) further describes degree-five del Pezzo arithmetic forms and blowup constructions over perfect fields. None of these inspected sources states the *complete class in the integral Grothendieck ring* for each pentagon boundary type or the associated comparison between the four marked arithmetic forms and their two motivic types. The contribution assessed is this exact motivic collapse and its characteristic-free cohomological realization, not the original compactification classification, the existing two affine point-count formulas, or the known degree-two compact-support cohomology character.

## Limitations

The full \(K_0(\operatorname{Var}_k)\) identities assume a finite base field and a geometrically pentagonal reduced divisor of \((-1)\)-curves; they are not claims about arbitrary log K3 surfaces or about all birational types of open del Pezzo surfaces. The sharp historical originality claim is provisional against specialist papers on finite-field cluster \(A_2\) surfaces, motivic nearby cycles, or Grothendieck classes not found in these searches. No independent audit has been carried out.

## References

1. Y. Harpaz, *Geometry and arithmetic of certain log K3 surfaces*, arXiv:1511.01285, first posted 2015-11-04; see Proposition 3.2.8, Theorem 3.3.2, Lemma 3.3.10, and Propositions 3.4.4–3.4.5; https://arxiv.org/html/1511.01285v1 .
2. B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300, first posted 2016-06-01, Section 2, https://arxiv.org/html/1606.00300v2 .
3. A. Boitrel, *Del Pezzo surfaces of degree 5 over perfect fields*, arXiv:2304.05328, 2023, https://arxiv.org/abs/2304.05328 .
