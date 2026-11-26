# Elliptic root spectra for cubic Ankeny–Brauer–Chowla polynomials

## Finding

Let \(\mathbb F_q\) be a finite field of odd characteristic different from \(7\), and let \(\varepsilon\in\{-1,1\}\). For \(u\in\mathbb F_q\), put
\[
P_{u,\varepsilon}(X)=X(X-\varepsilon)(X-u)+1,
\qquad r_{u,\varepsilon}=\#\{x\in\mathbb F_q:P_{u,\varepsilon}(x)=0\}.
\]
Define the fixed elliptic curve
\[
E:\quad Y^2=X^3+13X^2+128X,
\qquad H_q=\#E(\mathbb F_q),
\]
and the local collision count
\[
z_q=\#\left\{u\in\mathbb F_q:(u^2+u-3)^2=32\right\}.
\]
Then \(H_q\) is divisible by \(6\), \(z_q\in\{0,2,4\}\), and **the complete parameter histogram** \(N_j(q)=\#\{u:r_{u,\varepsilon}=j\}\), independent of \(\varepsilon\), is
\[
\boxed{\begin{aligned}
N_0(q)&=H_q/3,\\
N_1(q)&=q+1-(H_q+z_q)/2,\\
N_2(q)&=z_q,\\
N_3(q)&=H_q/6-1-z_q/2.
\end{aligned}}
\]
In particular, **exactly one third of the elliptic curve's rational-point count** is the number of irreducible members of either cubic family. By Hasse's bound and \(z_q\le4\), the proportions \((N_0,N_1,N_2,N_3)/q\) tend to \((1/3,1/2,0,1/6)\) with error \(O(q^{-1/2})\) as \(q\) tends to infinity through eligible odd prime powers.

## Assumptions and scope

All coefficients are interpreted in \(\mathbb F_q\). The polynomial has exact degree three and nonzero constant term. Root counts mean **distinct** field roots; for \(j=0\), a monic cubic with no field root is irreducible. The exclusions of characteristics \(2\) and \(7\) ensure the elliptic curve and discriminant quartic are nonsingular. No assertion is made for these excluded characteristics. The two choices of \(\varepsilon\) exhaust the degree-one monic polynomials \(Q(X)\in\mathbb Z[X]\) with constant term \(\pm1\) in the motivating family \(XQ(X)(X-u)+1\).

## Proof

**1. Discriminants and multiple roots.** For \(\varepsilon=1\), direct expansion of the cubic discriminant yields
\[
\Delta_1(u)=\operatorname{Disc}_X(P_{u,1})
=(u^2+u-3)^2-32.
\]
For \(\varepsilon=-1\) the analogous expression is
\[
\Delta_{-1}(u)=((u+1)^2+(u+1)-3)^2-32=\Delta_1(u+1).
\]
The discriminant, as a polynomial of its parameter, has discriminant \(-2^{14}7^3\); hence its zeros are simple in the indicated characteristics. A triple-root cubic would make both its discriminant and the derivative of the discriminant in the parameter vanish: the gradient of the general cubic discriminant vanishes on cubics with a triple root. Thus every zero of \(\Delta_\varepsilon\) produces exactly one double root and one different simple root. Both are rational over \(\mathbb F_q\), as each is the unique root with its specified multiplicity. Therefore \(N_2=z_q\), and translating the parameter does not change \(z_q\).

**2. Split versus nonsplit discriminant.** For \(\Delta_\varepsilon(u)\ne0\), the sign of Frobenius on the three roots is the quadratic character \(\chi(\Delta_\varepsilon(u))\). A nonsquare discriminant corresponds to a transposition, so exactly one root is rational; a nonzero square discriminant corresponds to an identity or a three-cycle, hence to three or zero rational roots. Let
\[
S_q=\sum_{u\in\mathbb F_q}\chi((u^2+u-3)^2-32),\qquad \chi(0)=0.
\]
There are \(q-z_q\) nondegenerate parameters, giving
\[
N_1=(q-z_q-S_q)/2.
\]
Independently, each \(x\in\mathbb F_q\setminus\{0,\varepsilon\}\) satisfies \(P_{u,\varepsilon}(x)=0\) for exactly one value
\[
u=x+\frac1{x(x-\varepsilon)}.
\]
Consequently \(\sum_u r_{u,\varepsilon}=q-2\), i.e.
\[
N_1+2N_2+3N_3=q-2.
\]
Together with \(N_0+N_1+N_2+N_3=q\), these identities give
\[
N_0=(q+2+S_q)/3,
\quad N_1=(q-z_q-S_q)/2,
\quad N_3=(q-4-3z_q+S_q)/6.
\]

**3. Elliptic identification.** The smooth genus-one quartic
\[
C:\quad Z^2=(u^2+u-3)^2-32
\]
has two rational points at infinity and thus \(\#C(\mathbb F_q)=q+2+S_q\). Put \(T=u^2+u-3\), and for affine points of \(C\) set
\[
X=2(T+Z),\qquad Y=X(2u+1).
\]
Since \((T+Z)(T-Z)=32\), we have \(X\ne0\), and
\[
Y^2=X^2(4T+13)=X^3+13X^2+128X.
\]
Conversely, for points of \(E\) with \(X\ne0\), recover
\[
u=\frac{Y/X-1}{2},\quad T=\frac{X+128/X}{4},\quad Z=X/2-T.
\]
These inverse rational maps extend to an isomorphism of smooth projective curves (the two rational quartic points at infinity correspond to the identity and \((0,0)\) on \(E\)). The Weierstrass discriminant of \(E\) is \(-2^{18}7^3\), nonzero in the allowed characteristics. Therefore \(H_q=q+2+S_q\), giving all the stated formulas.

**4. Divisibility and boundaries.** The point \((0,0)\) has order two. On \(E\), the point \(P=(4,28)\) satisfies \(2P=(4,-28)=-P\), by the tangent slope \((3\cdot4^2+26\cdot4+128)/(2\cdot28)=5\). These calculations remain valid in every characteristic other than \(2\) and \(7\); hence \(P\) has order three, and \(6\mid H_q\). The parameter quartic has distinct zeros; moreover, the roots arise in pairs from the two quadratic equations \(u^2+u-3=\pm4\sqrt2\), giving \(z_q\in\{0,2,4\}\). More explicitly, if \(2\) is nonsquare, \(z_q=0\); otherwise for any \(s\in\mathbb F_q\) with \(s^2=2\),
\[
z_q=2+\chi(13+16s)+\chi(13-16s).
\]
Changing \(s\) to \(-s\) leaves this expression unchanged. Finally \(|H_q-(q+1)|\le2\sqrt q\) gives the limiting proportions.

## Verification

The self-contained file `verify.py` recomputes the full histogram by direct polynomial evaluation and independently counts the elliptic curve's points by enumerating squares. It checks both cubic families at every odd prime at most \(97\) other than \(7\), and at the quadratic-extension sizes \(9,25,121,169,289\). In each test it verifies the exact four-part histogram, evenness of the discriminant collision count, and divisibility of the curve order by six. Execute with `python verify.py` (standard-library-only). These checks are finite sanity tests; the algebraic proof above establishes the theorem for every eligible finite field.

## Relationship to prior work

Pethő, *Common values of linear recurrences related to Ankeny–Brauer–Chowla polynomials* (arXiv:2611.17962v1, first public 13 November 2026), introduces this polynomial construction and establishes effective bounds for repeated absolute values of associated integer recurrences. The present statement concerns a different arithmetic invariant: the entire distribution of finite-field splitting types of its degree-three specializations, and the exact elliptic-curve count governing irreducible parameters. Noubissie–Tichy's *Large common values of generalized Ankeny–Brauer–Chowla recurrences* (arXiv:2606.27885) also studies repeated recurrence values, not finite-field splitting histograms. Known general facts about cubic discriminants, finite-field Frobenius and elliptic point counts are used as tools; the identification of this specific parameter family with the fixed six-torsion elliptic curve is the additional classification.

## Limitations

The theorem excludes characteristic \(2\) and \(7\); the elliptic identification degenerates there. It counts distinct roots, not multiplicity-weighted roots or roots over arbitrary extension degrees for a fixed parameter. It does not supply a closed elementary formula for \(H_q\), nor claim that elliptic curve point counts or cubic discriminant criteria are themselves new. The literature comparison is best knowledge rather than proof of global uniqueness; unindexed equivalent studies of this rational map or elliptic isogeny remain possible.

## References

1. Attila Pethő, *Common values of linear recurrences related to Ankeny–Brauer–Chowla polynomials*, arXiv:2611.17962v1 (13 November 2026), https://arxiv.org/html/2611.17962v1.
2. Armand Noubissie and Robert F. Tichy, *Large common values of generalized Ankeny–Brauer–Chowla recurrences*, arXiv:2606.27885v1 (26 June 2026), https://arxiv.org/abs/2606.27885.
3. Standard discriminant, Frobenius factorization and Hasse-bound identities for cubics and elliptic curves; see J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Springer, 2009, for elliptic curve background.
