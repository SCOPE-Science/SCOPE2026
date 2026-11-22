# Quadratic-induction Richelot strata of irreducible genus-two sextics and their first Weil spectra

## Finding
For every odd prime power \(q\), write \(k=\mathbb F_q\), and let \(\mathcal I_6(k)\) be the set of monic irreducible degree-six polynomials \(f\in k[x]\). The smooth genus-two curve \(C_f\) has affine model \(y^2=f(x)\), with two rational points above infinity.

**Theorem.** Every \(f\in\mathcal I_6(k)\) gives exactly one \(k\)-rational maximal isotropic subgroup of \(\operatorname{Jac}(C_f)[2]\). The associated polarized Richelot quotient is geometrically decomposed if and only if a nonidentity projective involution \(g\in\operatorname{PGL}_2(k)\) preserves the roots of \(f\). Such an involution, when it exists, is unique. The decomposed locus divides into the two disjoint arithmetic types below.

| Type of the unique involution | Number of monic sextics | Polarized Richelot codomain over \(k\) |
|---|---:|---|
| Two \(k\)-rational fixed points (split) | \(q^2(q-1)(q+1)^2/12\) | Product of two elliptic curves |
| Two conjugate quadratic fixed points (nonsplit) | \(q^2(q-1)^2(q+1)/12\) | Quadratic Weil restriction of an elliptic curve |

In the nonsplit type, for every integer \(r\ge0\),
\[
\#C_f(\mathbb F_{q^{2r+1}})=q^{2r+1}+1,
\qquad L_{C_f}(T)=1+b_fT^2+q^2T^4
\]
for an integer \(b_f\) satisfying the Weil bound. The restriction-of-scalars statement concerns the *principally polarized Richelot quotient*; no claim is made that the original Jacobian itself is isomorphic to a product over \(k\).

The total number in the two decomposed strata is \(q^3(q^2-1)/6\). The independent formula for fixed irreducible polynomials under projective involutions is known from Reis (2018); this numerical total and its elementary split/nonsplit refinements are supporting inputs, not claimed as novel discoveries. The distinct result assessed here is the resulting arithmetic splitting/trace classification and the exact two first-field spectra below.

For the nonsplit stratum the complete monic-model Weil-polynomial census is:

| Base field | Numerator \(L_{C_f}(T)\) | Exact monic-model count |
|---|---|---:|
| \(\mathbb F_3\) | \(1-T^2+9T^4\) | 12 |
| \(\mathbb F_5\) | \(1-5T^2+25T^4\) | 20 |
| \(\mathbb F_5\) | \(1-T^2+25T^4\) | 60 |
| \(\mathbb F_5\) | \(1+3T^2+25T^4\) | 60 |
| \(\mathbb F_5\) | \(1+7T^2+25T^4\) | 60 |

## Assumptions and scope
The characteristic is odd (including characteristic three). The polynomial must be monic, irreducible, of degree six; this implies squarefreeness over every finite field. Different monic polynomials are counted separately even when their curves are isomorphic or twists. An involution of \(\mathbb P^1\) is split if its two fixed points belong to \(k\), and nonsplit if they are conjugate over \(\mathbb F_{q^2}\). A polarized Richelot quotient means the principally polarized abelian surface obtained from the quotient by the canonical maximal isotropic subgroup, with its descended principal polarization. The Weil numerator is normalized by \(Z(C_f,T)=L_{C_f}(T)/((1-T)(1-qT))\).

## Proof
1. **Unique rational kernel.** Fix one root \(\alpha\) of \(f\). Arithmetic Frobenius acts as the six-cycle \((\alpha,\alpha^q,\ldots,\alpha^{q^5})\). A maximal Weil-isotropic subgroup of the Jacobian two-torsion corresponds to an unordered perfect matching of these six Weierstrass points. An invariant matching of a six-cycle must pair each vertex with its vertex at displacement three; the sole such matching is \(\{\{\alpha,\alpha^{q^3}\},\{\alpha^q,\alpha^{q^4}\},\{\alpha^{q^2},\alpha^{q^5}\}\}.\) In particular, the unique kernel is defined over \(k\), though the Jacobian has no nonzero rational two-torsion point.

2. **The determinant/involution criterion.** Form the three monic quadratic factors over \(\mathbb F_{q^3}\), one for each pair. The classical Richelot criterion says that the codomain is geometrically decomposed precisely when the determinant of their three homogeneous coefficient vectors vanishes (equivalently the three quadratics lie in a common pencil). Since these factors have disjoint roots, a two-dimensional pencil containing them has no base point and defines a separable morphism \(\mathbb P^1\to\mathbb P^1\) of degree two; in odd characteristic its deck transformation is a projective involution interchanging the members of each pair. Conversely, the fibers of the quotient map of any involution form a pencil. This transformation is unique because it is prescribed on three distinct roots. As Frobenius preserves all three pairs, it fixes the transformation, so \(g\in\operatorname{PGL}_2(k)\). Conversely a nontrivial \(k\)-rational involution preserving an irreducible six-root orbit must commute with its six-cycle; its nontrivial permutation is the displacement-three involution, and so gives the required matching. Distinct involutions cannot double-count the same monic polynomial.

3. **Split type.** A split involution has rational coordinates \(x\mapsto-x\). The six-root divisor is stable precisely when its monic sextic in this coordinate is \(f(x)=h(x^2)\), with \(h\) monic irreducible cubic and each degree-three root of \(h\) a nonsquare in \(\mathbb F_{q^3}\). For each involution, the number of choices is \(((q^3-1)-(q-1))/(2\cdot3)=(q^3-q)/6\). The lifted involution \((x,y)\mapsto(-x,y)\) and its product with the hyperelliptic involution are both defined over \(k\). Their genus-one quotients provide a \(k\)-split elliptic-product polarized Richelot codomain.

4. **Nonsplit type.** A nonsplit involution has rational coordinates \(x\mapsto d/x\) with a nonsquare \(d\in k^*\). Its quotient coordinate is \(t=x+d/x\). Above any degree-three point \(t\), the quadratic \(x^2-tx+d\) is irreducible over \(\mathbb F_{q^3}\) exactly when \(\chi_{q^3}(t^2-4d)=-1\). Since \(d\) remains a nonsquare in every odd extension, the discriminant has no zeros there, and the standard conic character sum \(\sum_t\chi_{q^n}(t^2-4d)=-1\) gives \((q^n+1)/2\) nonsquare values for \(n=1,3\). Removing degree-one parameters and dividing by three, the number of degree-three parameters per involution is \((q^3-q)/6\).

5. **Exact coefficient masses.** For odd \(q\), the group \(\operatorname{PGL}_2(k)\) has \(q(q+1)/2\) split involutions and \(q(q-1)/2\) nonsplit involutions. Their centralizers have orders \(2(q-1)\) and \(2(q+1)\), respectively. Because the preserving involution is unique, multiplication by \((q^3-q)/6\) gives the two displayed cardinalities. This matches the invariant-polynomial formula in Reis (2018), Theorem 1.4, and is acknowledged as prior-covered arithmetic enumeration.

6. **Arithmetic descent and odd-degree point counts.** In nonsplit coordinates, the root pairs are \(\{u,d/u\}\), whence monicity forces \(f(0)=d^3\) and \(x^6f(d/x)=d^3f(x)\). Over \(\mathbb F_{q^2}\) the involution of \(C_f\) lifts to \(\sigma(x,y)=(d/x,\sqrt{d^3}\,y/x^3)\). Its Frobenius conjugate is \(\iota\sigma\), where \(\iota(x,y)=(x,-y)\); on the Jacobian, \(\iota\) acts as minus the identity. The two elliptic eigenspace quotients of \(\sigma\) are therefore exchanged by Frobenius, rather than individually descending over \(k\). The polarized Richelot quotient descends as \(\operatorname{Res}_{\mathbb F_{q^2}/k}(E)\) for an elliptic curve \(E/\mathbb F_{q^2}\), and its Weil numerator has the indicated even form. Independently, for every odd \(n\), set \(Q=q^n\). The map \(u\mapsto d/u\) has no fixed point in \(\mathbb F_Q^*\), and \(\chi_Q(f(d/u))=\chi_Q(d^3)\chi_Q(f(u))=-\chi_Q(f(u))\). Thus the nonzero terms of \(\sum_{u\in\mathbb F_Q}\chi_Q(f(u))\) cancel in pairs and its zero term is \(-1\). Including the two rational points above infinity yields \(\#C_f(\mathbb F_Q)=Q+1\).

7. **First-field Weil spectra.** The exact finite exhaustive certificate consists of the supplied standard-library Python programs. They enumerate all \(p^6\) monic sextic coefficient vectors for each \(p\in\{3,5\}\), apply the exact Rabin irreducibility test \(x^{p^6}\equiv x\pmod f\) together with the degree-two and degree-three gcd exclusions, enumerate all \(p^2\) normalized projective involutions, and identify the nonsplit invariance class by an exact degree-six binary-form transformation. In explicit \(\mathbb F_{p^2}\) arithmetic they calculate \(N_2=\#C_f(\mathbb F_{p^2})\), from which \(b_f=(N_2-p^2-1)/2\). The calculations test every one of the 12 and 200 nonsplit models and give the displayed complete histograms. A separate \(\mathbb F_{p^3}\) character-sum checker verifies \(N_1=p+1\) and \(N_3=p^3+1\) for each model. These are genuine exhaustive finite proofs for \(p=3,5\), while the universal assertion rests on Steps 1–6.

## Verification
Place `check_richelot.py`, `check_trace.py`, and `check_weil_spectra.py` in one directory. Run `python3 check_richelot.py`, `python3 check_trace.py`, `python3 check_weil_spectra.py`. All use only the Python standard library. The first verifies total irreducible sextic counts, unique involution counts and split/nonsplit masses for \(p=3,5\); the second verifies odd-extension point counts in degrees one and three; and the third checks the complete degree-two Weil-coefficient histograms. Each program performs exact modular arithmetic and raises an assertion on failure.

## Relationship to prior work
Reis, *On the existence and number of invariant polynomials* (first public version 2018-11-06), Theorems 1.3 and 1.4, already determines the counts of irreducible polynomials invariant under projective involutions and excludes noncyclic stabilizers in degree six. Thus neither the number of invariant sextics nor its split/nonsplit elementary group partition is claimed original. Katsura–Takashima (2020, 2021) establish the geometrically decomposed Richelot/involution characterization. Magma's Richelot documentation distinguishes elliptic products and quadratic Weil restrictions. The new combined arithmetic claim specifies exactly which case arises from a six-cycle branch divisor, establishes the universal odd-extension trace cancellation, and determines the complete marked-model Weil spectra for \(q=3,5\). Earlier Frobenius matching-cycle tables describe the fifteen kernels but do not determine this codomain/trace stratification. Previously studied nonsplit Rosenhain families have rational branch points and do not cover irreducible sextics. The exact spectral tables and their complete proof go beyond the previously found fixed-polynomial formulas.

## Limitations
No classification by \(k\)-isomorphism or geometric isomorphism is asserted. A geometric decomposition of the *Richelot codomain* is not the same as an isomorphism of the original Jacobian to a product. The nonsplit codomain can be simple over \(k\) as an unpolarized abelian surface; no claim of unconditional simplicity is made. Outside the nonsplit sublocus there may be other curves with odd-degree balanced point counts, so no converse to the point-count condition is asserted. The finite exact spectra are restricted to \(q=3,5\); no uniform formula for \(b_f\)-frequencies is claimed for larger fields. Generic irreducible sextics have a rational Richelot kernel whose codomain remains a genus-two Jacobian. An earlier general invariant-polynomial theorem fully accounts for the stated polynomial counts; remaining originality concerns arithmetic quotient splitting and finite Weil spectra. Equivalent older classifications in unindexed genus-two finite-field tables remain a priority risk; independent validation has not been performed.

## References
1. Lucas Reis, *On the existence and number of invariant polynomials*, arXiv:1811.02537 (first submitted 2018-11-06), Theorems 1.3–1.4, on invariant irreducible polynomials.
2. Toshiyuki Katsura and Katsuyuki Takashima, *Counting Richelot isogenies between superspecial abelian surfaces*, arXiv:2003.00633 (2020-03-02), especially Propositions 4.3 and 4.5 on involutions and decomposed quotients; the enumeration in that paper is for superspecial curves.
3. Toshiyuki Katsura and Katsuyuki Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936 (2021-08-16), criterion in Section 3.
4. Magma computational algebra system, *Richelot Isogenies* handbook, https://magma.maths.usyd.edu.au/magma/handbook/text/1615, especially kernel descriptions and the product/Weil restriction distinction.
5. Hung Dang and Diep Nguyen, *Exact Stratification and Affine Mass Formulas for Split Richelot Data over Finite Fields*, arXiv:2607.03376 (2026); treats triples of individually rational quadratics, unlike the irreducible-sextic cubic-algebra case here.
