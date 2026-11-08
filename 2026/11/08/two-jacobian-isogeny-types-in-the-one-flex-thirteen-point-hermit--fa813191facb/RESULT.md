# Two Jacobian isogeny types in the one-flex, thirteen-point Hermitian-relative quartic stratum

## Finding

Let \(k=\mathbb F_9=\mathbb F_3[\iota]/(\iota^2+1)\). For nonzero \(c\in k\), put
\[
 C_c=V(x^3z-cxy^3+cxz^3-yz^3)\subset\mathbb P^2_k.
\]
Among the eight values of \(c\in k^\times\), precisely \(c=-1,1+\iota,1-\iota\) give **thirteen \(k\)-rational points and exactly one \(k\)-rational inflexion**, where an inflexion means contact order four with the tangent line. These curves are smooth of genus three. Set \(P_c(T)=\det(1-T\operatorname{Frob}_9\mid H^1_{\mathrm{\acute et}}(C_{c,\bar k},\mathbb Q_\ell))\) for any \(\ell\ne3\). Their complete Weil numerators are
\[
\begin{aligned}
P_{-1}(T)&=(1-3T+9T^2)(1+3T+9T^2)^2\\
 &=1+3T+18T^2+27T^3+162T^4+243T^5+729T^6,\\
P_{1+\iota}(T)=P_{1-\iota}(T)
 &=(1+3T+9T^2)(1-9T^2+81T^4)\\
 &=1+3T-27T^3+243T^5+729T^6.
\end{aligned}
\]
Consequently \(\#\operatorname{Jac}(C_{-1})(k)=1183=7\cdot13^2\), while \(\#\operatorname{Jac}(C_{1\pm\iota})(k)=949=13\cdot73\). All three Jacobians are supersingular. The first is \(k\)-isogenous to a product of three elliptic curves (one of trace \(+3\), two of trace \(-3\)); the latter two are each \(k\)-isogenous to an elliptic curve of trace \(-3\) times a **simple abelian surface**. Thus even the joint rational-point/inflexion profile does not determine Jacobian isogeny decomposition in this natural, complete three-parameter stratum.

## Assumptions and scope

The base field is the *specific* field of nine elements in characteristic three, with \(\iota^2=-1=2\). All parameter choices are made in the displayed normal-form family; no assertion classifies arbitrary quartics or their abstract \(k\)-isomorphism classes. The three curves share the published rational-point/inflexion type \((13,1)\). The assertion concerns the numerator of the Hasse–Weil zeta function over \(k\), not the geometric zeta function after passing to an algebraic closure.

## Proof

**1. Smoothness, genus, and rational inflexions.** Write \(F=x^3z-cxy^3+cxz^3-yz^3\). In characteristic three,
\[
(F_x,F_y,F_z)=(c(z^3-y^3),-z^3,x^3).
\]
All three derivatives cannot vanish at a projective point when \(c\ne0\). A smooth plane quartic has genus three. At infinity \(z=0\), the equation is \(-cxy^3=0\), giving exactly \([1:0:0]\) and \([0:1:0]\); both tangent lines have contact order three, not four.

On the affine chart \(z=1\), a point \((X,Y)\) satisfies \(X^3-cX(Y^3-1)-Y=0\). Its tangent line may be parametrized by \((x,y)=(X+t,Y+at)\), where \(a=c(1-Y^3)\). Direct substitution, using the characteristic-three binomial identity, gives exactly
\[
F(X+t,Y+at,1)=(1-cXa^3)t^3-ca^3t^4.
\]
Therefore the affine rational inflexions are exactly the solutions for which \(1-cXa^3=0\). Exact enumeration for all eight \(c\ne0\), using \(\iota^2=2\) and coordinates \(a+b\iota\), gives the following complete table:

| \(c\) | \(\#C_c(k)\) | \(\#\) rational inflexions |
|---|---:|---:|
| \(1\) | 16 | 0 |
| \(-1\) | 13 | 1 |
| \(\iota\) | 10 | 2 |
| \(1+\iota\) | 13 | 1 |
| \(2+\iota\) | 7 | 0 |
| \(-\iota\) | 10 | 2 |
| \(1-\iota\) | 13 | 1 |
| \(2-\iota\) | 7 | 0 |

The inflexions of the three distinguished curves in the integer encoding \(a+b\iota\leftrightarrow a+3b\) are, respectively, \((1,0),(7,6),(4,3)\) for \(c=2,4,7\). These counts also agree with the relevant three-parameter type of Homma–Kim's classification, but the verification here does not assume their counting theorem.

**2. Complete point-count certificates in the first three extensions.** For \(r=1,2,3\) use explicit fields \(k_r=\mathbb F_{9^r}\) described by
\[
 k_1=k,\quad k_2=k[v]/(v^2-(1+\iota)),\quad
 k_3=k[u]/(u^3-u-1).
\]
The element \(1+\iota\) is not a square in \(k\), and \(s^3-s\in\iota\mathbb F_3\) for every \(s\in k\), so both polynomials are irreducible. Thus each construction is the claimed field, with its canonical embedded copy of \(k\).

For each \(y\in k_r\), enumerate the solutions to the cubic
\[
 x^3-c(y^3-1)x=y.
\]
The map on the left is additive over \(\mathbb F_3\), hence each fiber has cardinality \(0\), \(1\), or \(3\). The exhaustive fiber histograms \((n_0,n_1,n_3)\), where \(n_j\) counts \(y\)'s with exactly \(j\) solutions, are:

| \(r\) | \(c\) | \((n_0,n_1,n_3)\) | \(2+n_1+3n_3\) |
|---:|---|---|---:|
| 1 | \(-1,1+\iota,1-\iota\) | \((2,5,2)\) each | 13 |
| 2 | \(-1\) | \((18,41,22)\) | 109 |
| 2 | \(1\pm\iota\) | \((30,41,10)\) each | 73 |
| 3 | \(-1,1+\iota,1-\iota\) | \((261,365,103)\) each | 676 |

The leading \(2\) counts the two points at infinity. Each fiber is checked against *every* field element \(x\), so these are exhaustive finite proofs, not sampled experiments or extrapolations. The standalone `VERIFY.py` reconstructs each field by integral polynomial arithmetic, independently checks all nonzero elements satisfy \(a^{9^r-1}=1\), enumerates all pairs, and reproduces the tangent-contact test. Its check includes every \(c\in k^\times\) for the base-field census.

**3. Reconstructing the unique Weil polynomials.** Put \(s_r=9^r+1-\#C_c(k_r)\), the \(r\)-th power sum of the six Frobenius eigenvalues. If \(P_c(T)=1+a_1T+\cdots+a_6T^6\), Newton's identities give
\[
 a_1=-s_1,\qquad a_2=(s_1^2-s_2)/2,\qquad
 a_3=-(s_3+a_1s_2+a_2s_1)/3.
\]
For a genus-three curve over a field of size nine, the Weil functional equation forces \(a_{6-j}=9^{3-j}a_j\) for \(0\le j\le3\), so these first three extension counts determine the *entire* degree-six polynomial. Substitution yields \((a_1,a_2,a_3)=(3,18,27)\) for \(c=-1\) and \((3,0,-27)\) for \(c=1\pm\iota\). Expanding the factorizations in the finding confirms all six coefficients.

**4. Isogeny decomposition.** For an abelian variety over a finite field, its order is the value of its Frobenius characteristic polynomial at one; hence the orders are 1183 and 949. The reciprocal characteristic polynomial of the four-dimensional factor is
\[
 Q(X)=X^4-9X^2+81.
\]
It is irreducible over \(\mathbb Q\): if \(Q=(X^2+aX+b)(X^2-aX+d)\) over \(\mathbb Q\), then \(bd=81\), \(a(d-b)=0\), and \(b+d-a^2=-9\). If \(a=0\), then \(b,d\) would solve \(Z^2+9Z+81=0\), whose discriminant is \(-243\). Otherwise \(b=d=\pm9\), requiring \(a^2=27\) or \(-9\). Both are impossible over \(\mathbb Q\). The simple-isogeny-factor decomposition theorem for abelian varieties over finite fields therefore gives a simple abelian surface for this quartic factor, alongside the elliptic factor. For \(c=-1\), all factors are quadratic, so the Jacobian is a product of three elliptic isogeny factors.

Each reciprocal Frobenius factor is \(9\Phi_3(X/3)\), \(9\Phi_6(X/3)\), or \(81\Phi_{12}(X/3)\), respectively. Thus every normalized eigenvalue is a root of unity; equivalently each Jacobian is supersingular.

## Verification

Run `python3 VERIFY.py` with the ordinary Python standard library. The executable computes all field products directly, checks field orders, all base-field types and tangent-contact tests, all 81/729-point-extension fibers, both Weil polynomials and their factorizations, and the two Jacobian orders. A successful execution ends with `VERIFY_OK`. The extension-degree-three computation checks all 531,441 affine pairs separately for each of the three distinguished coefficients; its finiteness is explicit. The irreducibility argument for \(Q\) and the Weil functional equation are proved in the text, not inferred from machine output.

## Relationship to prior work

Homma–Kim (arXiv:2610.09672v1, October 7, 2026), Sections 3–4 and Theorem 46, classify Hermitian-relative curves by the numbers of rational points and rational inflexions. In particular their type \((q+\sqrt q+1,1)\) has \(\sqrt q\) parameters, giving three at \(q=9\). The result here **uses that naturally defined stratum**, but determines extra arithmetic geometry not included in that classification: its complete Weil numerators and the elliptic-product-versus-simple-surface isogeny boundary. Homma–Kim (arXiv:2402.14192, 2024), Section 2, show that all these curves are geometrically Hermitian twists and constrain the normalized Frobenius eigenvalues to be roots of unity; this does not specify which two arithmetic factorizations occur in the thirteen-point one-flex stratum. Meagher–Top (2010), *Twists of Genus Three Curves over Finite Fields*, discusses Jacobian Frobenius for many quartic twists, but its Sections 7 and 8 explicitly exclude characteristic three for the Dyck–Fermat and Klein twist calculations, and therefore do not directly cover these \(\mathbb F_9\) cases.

Earlier exact Weil numerators for the distinct *one-rational-point* Hermitian-relative quartic family \(X^4+\eta Y^4+Y^3Z+YZ^3=0\) do not cover these thirteen-point curves: the former have base-field count one and a Jacobian Weil numerator \((1-3T+9T^2)^3\). In particular, knowing that family-wide result neither fixes the present three numerators nor gives the mixed elliptic/simple-surface decomposition.

## Limitations

The isogenies are over \(\mathbb F_9\), not asserted as isomorphisms of principally polarized abelian varieties; the result does not classify the full rational Jacobian groups, automorphism groups, or all Hermitian-relative quartic twist classes. The three-parameter classification is confined to the chosen published normal form. The existence of general theory for characteristic-three unitary twists makes an unlocated equivalent Frobenius table a residual historical-priority risk. The verification is exact but has not been independently audited.

## References

1. M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, arXiv:2610.09672v1, first submitted October 7, 2026. https://arxiv.org/html/2610.09672v1
2. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192, 2024. https://arxiv.org/abs/2402.14192
3. S. Meagher and J. Top, *Twists of Genus Three Curves over Finite Fields*, 2010, Sections 3, 7 and 8. https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf
4. Classical Newton identities, Weil functional equation, and isogeny classification of abelian varieties over finite fields; the only numerical inputs here are certified by `VERIFY.py`.
