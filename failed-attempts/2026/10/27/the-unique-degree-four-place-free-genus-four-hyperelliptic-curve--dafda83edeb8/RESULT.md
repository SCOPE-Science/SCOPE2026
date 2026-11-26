# The unique degree-four-place-free genus-four hyperelliptic curve over \(\mathbb F_3\) and an infinite sharp closed-point threshold

## Finding

Write \(B_r(C)\) for the number of Frobenius orbits of cardinality exactly \(r\) on a smooth, projective, geometrically connected curve \(C/\mathbb F_q\). Let \(\rho(q,g)\) be the smallest integer \(R\) such that every genus-\(g\) curve over \(\mathbb F_q\) has at least one closed point of degree \(r\) for every integer \(r\ge R\).

**Theorem.** Among all smooth, projective, geometrically connected **hyperelliptic** genus-four curves over \(\mathbb F_3\), precisely one \(\mathbb F_3\)-isomorphism class has \(B_4=0\). It is represented by
\[
C:\quad y^2=x^9-x.
\]
The curve has \(\#C(\mathbb F_9)=\#C(\mathbb F_{81})=10\), and therefore \(B_4(C)=0\).

**Companion consequence.** For every odd prime power \(q\), the smooth hyperelliptic curve
\[
C_q:\quad y^2=x^{q^2}-x
\]
has genus \(g=(q^2-1)/2\), satisfies \(B_4(C_q)=0\), and makes the known universal closed-point upper bound sharp:
\[
\boxed{\rho\!\left(q,\frac{q^2-1}{2}\right)=5.}
\]
In particular, \(\rho(3,4)=5\). The genus-four uniqueness theorem is restricted to **hyperelliptic** curves; no classification of the nonhyperelliptic locus is asserted.

## Assumptions and scope

Every field appearing in the theorem is finite of odd characteristic. The genus is the geometric genus of the smooth projective model. A closed point of degree \(r\) is a Frobenius orbit of cardinality \(r\), and
\[
\#C(\mathbb F_{q^n})=\sum_{d\mid n}dB_d(C),\qquad
4B_4(C)=\#C(\mathbb F_{q^4})-\#C(\mathbb F_{q^2}).
\]
Hyperelliptic means there is a degree-two morphism to a genus-zero curve over the ground field. Over a finite field the genus-zero quotient is \(\mathbb P^1\). The classification is of genuine ground-field isomorphism classes, not merely normalized polynomial presentations.

## Proof

### 1. A genus-dependent universal upper bound

Aubry–Herbaut–Monaldi [1, Proposition 2.2], based on Aubry–Haloui–Lachaud [2], prove that for any smooth genus-\(g\) curve over \(\mathbb F_q\), each integer \(r\ge2\) satisfying
\[
(q^{r/4}-1)^2\ge2g
\]
is the degree of at least one closed point. For \(g=(q^2-1)/2\), this holds for every \(r\ge5\) and every odd \(q\ge3\): at \(q=3\), \(3^{5/4}>1+\sqrt8\); at \(q\ge5\), \(q^{1/4}\ge5^{1/4}>6/5\ge1+1/q\), hence \(q^{5/4}>q+1>1+\sqrt{q^2-1}\). Increasing \(r\) only strengthens the inequality. Thus
\[
\rho\!\left(q,\frac{q^2-1}{2}\right)\le5.
\]
This upper bound is **prior work**; only its sharpness in the stated new range is asserted here.

### 2. A degree-four obstruction over every odd finite field

The derivative of \(x^{q^2}-x\) is \(-1\). Hence the polynomial is squarefree of odd degree \(q^2\), and the normalization of \(C_q\) is smooth, geometrically connected, and hyperelliptic of genus \((q^2-1)/2\), with one rational point at infinity.

Take \(x\in\mathbb F_{q^4}\) and put \(z=x^{q^2}-x\). If \(x\in\mathbb F_{q^2}\), then \(z=0\) and the only affine point above \(x\) is \((x,0)\). Otherwise \(z\ne0\), and
\[
z^{q^2}=x^{q^4}-x^{q^2}=x-x^{q^2}=-z,
\qquad z^{q^2-1}=-1.
\]
Since \(q\) is odd, \((q^2+1)/2\) is odd. Therefore
\[
z^{(q^4-1)/2}=\left(z^{q^2-1}\right)^{(q^2+1)/2}=-1,
\]
so \(z\) is a nonsquare in \(\mathbb F_{q^4}\). It has no square root \(y\). Consequently
\[
C_q(\mathbb F_{q^4})=C_q(\mathbb F_{q^2}),\qquad
\#C_q(\mathbb F_{q^4})=q^2+1,
\qquad B_4(C_q)=0.
\]
This implies \(\rho(q,(q^2-1)/2)\ge5\), and Step 1 gives equality. At \(q=3\), this is the displayed genus-four witness.

### 3. Exhaustion of hyperelliptic genus-four presentations over \(\mathbb F_3\)

A hyperelliptic involution is defined over \(\mathbb F_3\), and its genus-zero quotient is \(\mathbb P^1\) because finite fields have trivial Brauer group. Choose a rational point of this quotient as infinity. By the odd-characteristic double-cover normal form, every genus-four hyperelliptic curve over \(\mathbb F_3\) is isomorphic to the smooth projective model of
\[
y^2=a f(x),\qquad a\in\{1,2\},\qquad
f\in\mathbb F_3[x]\ \text{monic, squarefree,}\quad \deg(f)\in\{9,10\}.
\]
The factors \(a=1\) and \(a=2\) are both squares in \(\mathbb F_9\) and \(\mathbb F_{81}\). Thus, for purposes of the difference \(N_4-N_2\), it suffices to inspect \(a=1\). For each monic coefficient vector \((c_0,\ldots,c_{d-1})\in\{0,1,2\}^d\), set \(f=x^d+\sum_{j<d}c_jx^j\). Retain it precisely when \(\gcd(f,f')=1\). For \(n\in\{2,4\}\), compute
\[
N_n(f)=3^n+\varepsilon_d+\sum_{x\in\mathbb F_{3^n}}\chi_n(f(x)),\qquad
\varepsilon_9=1,\quad\varepsilon_{10}=2,
\]
where \(\chi_n(0)=0\), \(\chi_n(u)=1\) for nonzero squares and \(-1\) otherwise. Finally compute \(B_4=(N_4-N_2)/4\). This is an exhaustive, finite, exact specification, not a random search.

The supplied standalone verifier `verify.cpp` implements this enumeration with integer polynomial operations and the quotient fields
\[
\mathbb F_9=\mathbb F_3[u]/(u^2+1),\qquad
\mathbb F_{81}=\mathbb F_3[v]/(v^4+v+2).
\]
The two moduli are verified irreducible: the quadratic has no \(\mathbb F_3\)-root, and the quartic has no root in \(\mathbb F_9\), which excludes both linear and quadratic factors. Coefficients are traversed by all base-three integers from zero through \(3^d-1\), so no monic polynomial is omitted. The resulting exact counts are:

| Degree of \(f\) | Monic squarefree forms | Forms with \(B_4=0\) | Minimum \(B_4\) |
| --- | ---: | ---: | ---: |
| \(9\) | 13,122 | 1 | 0 |
| \(10\) | 39,366 | 0 | 2 |

The unique degree-nine vanishing form has coefficients \((c_0,\ldots,c_8)=(0,2,0,0,0,0,0,0,0)\), namely \(f=x^9-x\), and \(N_2=N_4=10\). The squarefree totals also independently agree with \(3^d-3^{d-1}\) for \(d=9,10\). Both quadratic-twist choices give the same vanishing condition. Finally the two twists of this particular equation are isomorphic over \(\mathbb F_3\): substituting \(x\mapsto-x\) interchanges \(f(x)\) and \(2f(x)\). Hence **exactly one ground-field isomorphism class** in the entire hyperelliptic genus-four locus is degree-four-place-free.

## Verification

Compile the standalone enumeration source with a standard C++17 compiler, for example `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. Its terminal line is `VERIFY_OK`; it prints the squarefree counts, the two minimum values, and the unique zero form. The separate Python source `check_witness.py` uses its own base-three representation of \(\mathbb F_{81}\), verifies the field power identities, and obtains `WITNESS_VERIFY_OK N2=10 N4=10 B4=0`. Both files are supplied, self-contained, and require no proprietary dependencies. The universal statement is proved symbolically in Steps 1–2; the finite exhaustive computer proof is used only for the uniqueness classification over \(\mathbb F_3\).

## Relationship to prior work

Aubry–Herbaut–Monaldi [1] define \(\rho(q,g)\), determine its exact values for genera one through three, and record the universal upper bound used in Step 1. They do not give the asserted hyperelliptic genus-four uniqueness classification or the infinite sharp family. The original threshold question is credited there to Tsfasman–Vlăduț–Nogin [3]. Lario's Diophantine-stability tables [4] classify curves of genera at most three and provide genus-four candidates in certain quadratic-extension settings, including \(\mathbb F_9/\mathbb F_3\), but do not display the degree-four-point classification for \(\mathbb F_{81}/\mathbb F_3\). Aubry–Herbaut–Monaldi's later quadratic-extension work [5] treats different maximality criteria and supplies no equivalent genus-four enumeration in the examined sections. The equation \(y^2=x^9-x\) occurs in other geometric contexts; the equation itself is **not** asserted to be newly invented. The purported new statements are the exact closed-point property, the uniqueness among hyperelliptic genus-four curves over \(\mathbb F_3\), and the sharp infinite threshold family. Published databases or unindexed work could contain stronger implicit coverage; this is the main residual originality risk.

## Limitations

No classification is claimed for nonhyperelliptic genus-four curves over \(\mathbb F_3\); they may also lack degree-four points. The uniqueness classification uses an exhaustive finite computation rather than a conceptual rigidity theorem. It does not assert uniqueness over every odd finite field or for arbitrary genera. No independent external validation has been performed. Known upper bounds and old table entries remain attributed to the primary literature. The numerical and uniqueness conclusions have been checked with the supplied programs, not with an external proof assistant.

## References

1. Y. Aubry, F. Herbaut and J. Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218v1 (first made public 17 October 2023), especially §§1–2, 6, Proposition 2.2. https://arxiv.org/abs/2310.11218
2. Y. Aubry, S. Haloui and G. Lachaud, *On the number of points on abelian and Jacobian varieties over finite fields*, Acta Arith. 160 (2013), 201–242, as cited in [1].
3. M. Tsfasman, S. Vlăduț and D. Nogin, *Algebraic Geometric Codes: Basic Notions*, Problem 3.2.13, as cited in [1].
4. J.-C. Lario, *Curves over Finite Fields with Diophantine Stability*, https://web.mat.upc.edu/joan.carles.lario/DS.html (accessed 24 October 2026).
5. Y. Aubry, F. Herbaut and J. Monaldi, *Maximal curves with respect to quadratic extensions over finite fields*, arXiv:2506.08603 (first made public 2025), https://arxiv.org/abs/2506.08603.
