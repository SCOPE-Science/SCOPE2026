# A maximal genus-thirteen \(S_3\)-Galois closure of a superspecial genus-four trigonal curve

## Finding
Let \(k=\mathbb F_{11}\). Let \(G\) be the smooth projective curve whose function field is the splitting field over \(k(t)\) of
\[
F(U)=U^3-t^4U^2+1.
\]
Then \(G\to\mathbb P^1_k\) is a geometrically connected regular \(S_3\)-Galois cover of degree six, branched at precisely the twelve simple roots of \(4t^{12}-27\), with inertia of order two at each branch value and no ramification over infinity. The curve has genus thirteen and
\[
\#G(\mathbb F_{11})=12,\qquad \#G(\mathbb F_{121})=408=121+1+26\cdot11.
\]
In particular it is maximal over \(\mathbb F_{121}\), and its Hasse–Weil numerator over \(\mathbb F_{11}\) is
\[
L_G(T)=(1+11T^2)^{13},\qquad \#\operatorname{Jac}(G)(\mathbb F_{11})=12^{13}=106993205379072.
\]
The cubic quotient by a transposition is the canonical trigonal map of the distinguished superspecial genus-four double-elliptic curve \(C\) given by \(y^2z=x^3+z^3\), \(w^2=xy\); the quadratic sign quotient has genus five and equation \(v^2=4t^{12}-27\).

## Assumptions and scope
All curves and point counts are over \(k=\mathbb F_{11}\) or its quadratic extension, with the smooth projective normalization understood wherever a function-field presentation is used. In characteristic eleven, the elliptic plane cubic \(E:y^2z=x^3+z^3\) is smooth. Its intersection with the conic \(xy=0\) comprises six distinct geometric points: the point at infinity, the two points with \(x=0\), and the three points with \(y=0\). Accordingly the double cover \(C\to E\), defined by \(w^2=xy\), is smooth, connected, and of genus four by Riemann–Hurwitz. Its model and its status as the characteristic-eleven superspecial curve with unique degree-two elliptic quotient appear in Ogasawara–Ohashi–Sakata–Harashita (2024). The earlier superspecial genus-four census is due to Kudo–Harashita (2017); neither attribution is claimed as new.

## Proof
**Trigonal map and discriminant.** On the open set where \(xz\ne0\), put \(u=x/z\) and \(t=w/x\). The quadratic equation gives \(y/z=t^2u\), while the cubic becomes \(u^3-t^4u^2+1=0\). This is the degree-three function-field extension associated with the pencil of generators on the canonical quadric cone \(w^2=xy\). There are three simple poles of \(t\) on \(C\), namely \([0:1:0:0]\) and \([0:\pm1:1:0]\), all rational over \(k\), establishing degree three, geometric irreducibility, and no ramification over infinity. The cubic discriminant is exactly \(\Delta(t)=4t^{12}-27\). Its derivative is \(48t^{11}=4t^{11}\) in characteristic eleven, hence \(\Delta\) has twelve simple nonzero geometric zeros and is not a square in \(\overline{k}(t)\). An irreducible separable cubic with nonsquare discriminant has splitting-field Galois group \(S_3\). Thus its normal closure has no constant-field extension and defines a geometrically connected \(S_3\)-cover. At each discriminant zero inertia has order two; there are three ramification points, each of index two, over that branch value. There is no other ramification.

**Genus.** Applying the tame Riemann–Hurwitz formula to the degree-six map yields
\[
2g(G)-2=6(-2)+12\cdot3=24,
\]
so \(g(G)=13\). The index-two subgroup \(A_3\) has sign-quotient function field \(k(t,\sqrt{\Delta(t)})\). Since the degree-twelve branch polynomial is squarefree, its smooth hyperelliptic model \(Y:v^2=4t^{12}-27\) has genus five.

**Exact Frobenius fibers.** Work in \(\mathbb F_{121}=\mathbb F_{11}[i]\), \(i^2=-1\). The norm of \(t\) is \(t^{12}\in\mathbb F_{11}\). Therefore for any \(t\in\mathbb F_{121}\), the discriminant \(4t^{12}-27\) lies in \(\mathbb F_{11}\) and is a square in \(\mathbb F_{121}\). Exactly twelve \(t\)-values have zero discriminant, since the norm map on nonzero elements has kernel of order twelve and \(27/4=4\) in \(\mathbb F_{11}\). For the other values, the separable cubic consequently has either zero roots (irreducible cubic) or three distinct roots over \(\mathbb F_{121}\): there cannot be exactly one simple root and an irreducible quadratic factor.

Exhaustive exact field arithmetic (standalone `verify.py`) gives the following *complete* number of \(t\)-values sorted by the number of **distinct roots** of \(F(U)\) in the indicated field:

| Field | 0 roots | 1 root | 2 roots | 3 roots |
|---|---:|---:|---:|---:|
| \(\mathbb F_{11}\) | 4 | 5 | 2 | 0 |
| \(\mathbb F_{121}\) | 48 | 0 | 12 | 61 |

An unramified fully split cubic fiber contributes six rational points to the Galois closure, and an unramified nonsplit cubic fiber contributes none. At each of the twelve simple-discriminant points, the cubic has one rational double root and one distinct rational root; tame inertia is a transposition and the decomposition group equals inertia, so the normal-closure fiber consists of three rational points. At infinity all three poles of \(t\) on \(C\) are rational and unramified, giving six rational points on \(G\). Hence
\[
\#G(\mathbb F_{121})=6\cdot61+3\cdot12+6=408.
\]
Over \(\mathbb F_{11}\), the only split ramified parameters are \(t=\pm2\), and no finite unramified cubic splits completely. The same fiber argument gives \(\#G(\mathbb F_{11})=2\cdot3+6=12\).

**Zeta numerator.** The genus-thirteen Hasse–Weil bound over \(\mathbb F_{121}\) is \(122+2\cdot13\cdot11=408\), so equality proves maximality and makes every quadratic-Frobenius eigenvalue equal to \(-11\). Every eigenvalue \(\alpha\) of arithmetic Frobenius over \(\mathbb F_{11}\) therefore obeys \(\alpha^2=-11\). The rational-point count \(12=11+1\) forces zero trace, so the two square roots of \(-11\) have multiplicity thirteen each, proving \(L_G(T)=(1+11T^2)^{13}\). Evaluating at \(T=1\) yields the stated Jacobian order.

## Verification
The standalone Python 3 script `verify.py` implements \(\mathbb F_{11}\) and \(\mathbb F_{121}\) using pairs \(a+bi\) with \(i^2=-1\), exhausts every field parameter and every cubic root, and separately enumerates the genus-four cubic quotient \(C\) and the genus-five sign quotient \(Y\). It verifies the respective point counts \((12,210)\) and \((12,232)\), both root-pattern tables, and the number \(408\) for the normal closure. The output ends in `GENUS13_S3_MAXIMAL_F121_VERIFIED`. The counts are exhaustive for the finite fields stated, not empirical samples. Riemann–Hurwitz, separable cubic Galois theory, and the Weil bound are used as mathematical deductions rather than inferred from code.

## Relationship to prior work
Kudo–Harashita (arXiv:1702.05313, first posted 2017-02-17) enumerate the characteristic-eleven superspecial genus-four curves and give maximal genus-four examples. Kudo–Harashita–Senda (arXiv:1709.03627, first posted 2017-09-11) determine their automorphism groups and finite-field forms. Ogasawara–Ohashi–Sakata–Harashita (arXiv:2403.08139, first posted 2024-03-12), Section 4.4, identify the displayed canonical bielliptic model and its unique elliptic quotient. These results supply the genus-four starting object, **not** the degree-six trigonal normal closure, its twelve-point ramification scheme, its genus-thirteen maximality, or the exact nonabelian covering-field Frobenius spectrum. Known maximality of a genus-four curve alone does not imply maximality of its non-Galois cubic map's normal closure: the discriminant genus-five quotient also matters. The result uses both components and an independent complete fiber count.

## Limitations
This establishes a single specified \(S_3\)-cover and its arithmetic, not a classification of all maximal genus-thirteen curves, its full geometric automorphism group, or uniqueness of this covering type. The 2017 and 2024 sources are credited for the genus-four curve. Priority searches cannot rule out every older unindexed expression of this exact normal closure; no independent validation has been performed.

## References
1. M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313 (2017), https://arxiv.org/abs/1702.05313.
2. M. Kudo, S. Harashita, and H. Senda, *Automorphism groups of superspecial curves of genus 4 over F11*, arXiv:1709.03627 (2017), https://arxiv.org/abs/1709.03627.
3. T. Ogasawara, R. Ohashi, K. Sakata, and S. Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139 (2024), https://arxiv.org/abs/2403.08139.
