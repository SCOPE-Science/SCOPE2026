# The tenfold isomorphism redundancy of characteristic-two cyclic-four genus-two Witt covers

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\). For each \(\lambda\in k^\times\), let \(C_\lambda\) be the smooth projective curve with function field defined by the length-two Artin–Schreier–Witt equation
\[
\wp_2(Y_0,Y_1)=(x,\lambda x^3).
\]
Here \(\wp_2=F-1\) on the ring of \(2\)-typical Witt vectors of length two. Define the rational function
\[
\mathcal J(\lambda)=\frac{(\lambda^2+\lambda+1)^5}{\lambda^6}.
\]
The following is a complete classification **of the underlying curves, without marking the cyclic order-four subgroup**:

**Theorem.** For \(\lambda,\mu\in k^\times\), the curves \(C_\lambda\) and \(C_\mu\) are geometrically isomorphic if and only if \(\mathcal J(\lambda)=\mathcal J(\mu)\). Every supersingular genus-two curve over \(k\) is isomorphic to some \(C_\lambda\). For every \(c\in k^\times\), the equation \(\mathcal J(\lambda)=c\) has precisely ten distinct nonzero solutions \(\lambda\) in \(k\), whereas \(\mathcal J(\lambda)=0\) has precisely two: the two roots of \(\lambda^2+\lambda+1\), each occurring with multiplicity five in the defining polynomial. Moreover,
\[
|\operatorname{Aut}_k(C_\lambda)|=
\begin{cases}
32,&\lambda^2+\lambda+1\ne0,\\
160,&\lambda^2+\lambda+1=0.
\end{cases}
\]
The exceptional pair both represents the unique superspecial genus-two curve \(y^2+y=t^5\); all other members are supersingular but not superspecial. In particular, the explicit parameter is generically ten-to-one on **geometric isomorphism classes** and has a two-point exceptional fiber.

## Assumptions and scope

All assertions are over an algebraically closed field \(k\) of characteristic \(2\), and \(\lambda\ne0\). The curves are nonsingular projective normalizations of the displayed affine Witt cover. Isomorphisms are not required to preserve its distinguished \(C_4\)-action, its chosen generator, its quotient coordinate, or any model over a smaller field. The function \(\mathcal J\) is an explicit classifier for geometric isomorphism classes; no assertion is made that it is a chosen scheme-theoretic coarse-moduli coordinate. The Frobenius transformation of \(\mathcal J\) is important in comparing it with traditional Igusa invariants.

## Proof

**1. Convert the Witt cover into a genus-two Artin–Schreier quintic.** For length-two Witt vectors in characteristic two, the subtraction identity is
\[
\wp_2(Y_0,Y_1)=\bigl(Y_0^2+Y_0,\;Y_1^2+Y_1+Y_0^2+Y_0^3\bigr).
\]
Put \(t=Y_0\). The first component gives \(x=t^2+t\), and the second gives
\[
Y_1^2+Y_1=\lambda(t^2+t)^3+t^2+t^3.
\]
Choose \(w\in k\) with \(w^4=\lambda\), which is unique because \(k\) is perfect. Let
\[
H(t)=w^2t^3+w^2t^2+(w+1)t,
\qquad y=Y_1+H(t).
\]
A direct characteristic-two expansion shows
\[
y^2+y=A t^5+B t^3+C t,
\quad A=\lambda,\quad B=\lambda+\lambda^{1/2}+1,\quad C=\lambda^{1/4}+1.
\tag{1}
\]
The leading term \(A\ne0\) has odd degree five; thus the smooth projective Artin–Schreier cover is of genus two with unique branch point over \(t=\infty\). The displayed Witt-to-quintic identity is independently reproduced by the exact checker below.

**2. A complete geometric isomorphism criterion for the quintics.** Consider any two curves
\[
D_{A,B,C}: y^2+y=A t^5+B t^3+C t,
\qquad D_{A',B',C'}: y'^2+y'=A't'^5+B't'^3+C't',
\tag{2}
\]
where \(A,A'\in k^\times\) and the other coefficients are arbitrary. Each hyperelliptic double cover has a unique branch point, at infinity. Therefore any geometric isomorphism induces \(t'=a t+b\), with \(a\in k^\times\), \(b\in k\), and must have \(y'=y+h(t)\). Pole comparison forces \(h\) to be a polynomial of degree at most two. Comparing the fifth and third-degree coefficients, which cannot be affected by \(h^2+h\), yields the necessary conditions
\[
A'a^5=A,\qquad B'a^3=B.
\tag{3}
\]
Conversely assume (3), and put
\[
\begin{aligned}
\delta_4&=A'a^4b,\\
\delta_2&=B'a^2b,\\
\delta_1&=A'ab^4+B'ab^2+C'a+C,\\
\delta_0&=A'b^5+B'b^3+C'b.
\end{aligned}
\]
Then \(D_{A',B',C'}(a t+b)-D_{A,B,C}(t)=\delta_4t^4+\delta_2t^2+\delta_1t+\delta_0\), with subtraction understood as addition in characteristic two. For \(h(t)=u t^2+v t+s\), the equality \(h^2+h=\sum\delta_i t^i\) is equivalent to
\[
u^2=\delta_4,\qquad v^2+u=\delta_2,\qquad v=\delta_1,\qquad s^2+s=\delta_0.
\]
Eliminating \(u,v\) leaves precisely
\[
\delta_1^4+\delta_2^2+\delta_4=0.\tag{4}
\]
As a polynomial in \(b\), the left side has degree \(16\), leading coefficient \((A'a)^4\ne0\), and formal derivative \(A'a^4\ne0\). Thus (4) has exactly sixteen distinct roots in \(k\). For any such root, take \(v=\delta_1\), \(u=\delta_2+\delta_1^2\), and choose either of the two solutions of \(s^2+s=\delta_0\). This explicitly constructs the isomorphism. Hence (3) is also sufficient.

When \(B=B'=0\), equation (3) has five possible values of \(a\). When exactly one of \(B,B'\) vanishes, it has none. When \(BB'\ne0\), equation (3) is soluble if and only if
\[
\frac{B^5}{A^3}=\frac{(B')^5}{(A')^3};\tag{5}
\]
indeed the condition follows by taking powers, and the converse follows from \(\gcd(3,5)=1\) (one may take \(a=(A/A')^2/(B/B')^3\)). Thus (5) characterizes geometric isomorphism in all cases, allowing zero numerators.

**3. The rational parameter classifier and exact fibers.** For (1), squaring the invariant in (5) gives
\[
\left(\frac{B^5}{A^3}\right)^2=\frac{(\lambda^2+\lambda+1)^5}{\lambda^6}=\mathcal J(\lambda).
\]
Squaring is injective over \(k\); hence criterion (5) is exactly equality of \(\mathcal J\). For a prescribed \(c\in k\), the parameter equation is
\[
F_c(L):=(L^2+L+1)^5+cL^6=0.\tag{6}
\]
It has degree ten and constant coefficient one, so all its ten roots counted with multiplicity are nonzero. Its derivative in characteristic two is
\[
F'_c(L)=(L^2+L+1)^4.
\]
If \(c\ne0\), a common root of \(F_c\) and \(F'_c\) would satisfy \(L^2+L+1=0\) and \(cL^6=0\), an impossibility. Thus all ten roots are distinct. For \(c=0\), (6) has exactly the two distinct roots of \(L^2+L+1\), each with multiplicity five. In particular \(\mathcal J:k^\times\to k\) is surjective on geometric points, and its fibers have precisely the claimed sizes. The separability claim concerns this explicit rational classifier, not any fixed coarse-moduli scheme structure.

**4. Completeness and automorphism jump.** The general classification of supersingular genus-two curves over an algebraically closed field of characteristic two gives either \(y^2+y=t^5\), or a model \(y^2+y=D(t^5+t^3)\) with \(D\in k^\times\); see Brock–Howe, Lemma 2.1. In the latter normal form the invariant (5) is \(D^2\), while it is zero for the special curve. Surjectivity in Step 3 therefore proves that every supersingular genus-two curve occurs in this Witt family. To count all automorphisms using Step 2, set \(A'=A\), \(B'=B\), \(C'=C\). If \(B\ne0\), then \(a^5=a^3=1\) forces \(a=1\); there are sixteen permissible \(b\)'s and two choices for the constant in \(h\), hence \(32\) automorphisms. If \(B=0\), there are five fifth roots for \(a\), giving \(5\cdot16\cdot2=160\) automorphisms. Finally, \(B=0\) is equivalent to \(\lambda^2+\lambda+1=0\). The identification of the latter curve as superspecial, and of the others as non-superspecial supersingular curves, is the standard genus-two classification in characteristic two; alternatively it follows from the normal forms and Brock–Howe, Lemma 2.1.

## Verification

The standalone standard-library Python 3 program `verify_witt_moduli.py` verifies exactly (over polynomial rings with coefficients in \(\mathbb F_2\)) the Witt-to-quintic identity in Step 1 and the degree/derivative identities in Step 3. It independently checks the rational classifier and the two special parameters over \(\mathbb F_{256}\). Executing the package program prints:

```
EXACT_WITT_TO_QUINTIC_IDENTITY_OK
DEGREE_TEN_SEPARABLE_FIBER_IDENTITY_OK
FINITE_FIELD_F256_CLASSIFIER_AND_SPECIAL_FIBER_OK
CERTIFICATE_OK
```

The finite-field samples are not used to assert global root counts or geometric classification; those conclusions follow from the preceding polynomial and isomorphism proofs.

## Relationship to prior work

Kazemifard–Tafazolian (2026), Theorem 5.7, constructs the genus-two, cyclic-four Witt family and explicitly does not assert uniqueness of its parameter. The present result **does not** reprove the existence or the group classification of its marked cyclic covers. It solves the distinct question of when the *underlying unmarked curves* are isomorphic, identifies the exact size of every parameter fiber, and locates the exceptional full-automorphism jump.

Brock–Howe (2020), Lemma 2.1, classifies arbitrary supersingular genus-two curves by Igusa data and gives normal forms and automorphism group orders. This stronger general theorem is essential comparison literature. It does **not** state the rational function \(\mathcal J(\lambda)\), its ten-to-one parameter redundancy, or the exceptional two-point fiber for the specific Witt parameter of the later paper. The direct proof here derives those facts from the Witt equation and an explicit degree-sixteen isomorphism equation; the classical normal-form theorem is used only for the exhaustion of all supersingular genus-two isomorphism classes and the superspecial label. For the traditional invariant \(I=J_8^5/J_{10}^4\), one obtains \(I=\mathcal J(\lambda)^4\); the Frobenius power must not be confused with a separable map of coarse-moduli schemes. Earlier supersingular-normal-form and zeta-function classifications (e.g. Scholten–Zhu; Maisner–Nart) concern the broader ambient moduli, not this explicit Witt parameter map.

## Limitations

The result classifies underlying curves over algebraically closed fields only. It does not classify Witt presentations as **marked pairs** \((C_\lambda,C_4)\), identify isomorphisms over arbitrary finite subfields, provide a scheme-level moduli morphism, or describe the Galois/monodromy group of polynomial (6). Historical priority of the concrete rational parameter map cannot be certified exhaustively by a literature search. There is no independent mathematical audit.

## References

1. A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702, first public 2026-10-03, Theorem 5.7 and Section 5.3. https://arxiv.org/abs/2610.04702
2. B. W. Brock and E. W. Howe, *Purely inseparable Richelot isogenies*, arXiv:2002.02122, 2020, Section 2 and Lemma 2.1. https://arxiv.org/abs/2002.02122
3. J. Scholten and H. J. Zhu, *Families of supersingular curves in characteristic 2*, Mathematical Research Letters **9** (2002), 639–650. https://doi.org/10.4310/MRL.2002.v9.n5.a7
4. D. Maisner and E. Nart, *Zeta functions of supersingular curves of genus 2*, arXiv:math/0408383, 2004. https://arxiv.org/abs/math/0408383
