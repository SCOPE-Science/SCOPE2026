# Arithmetic descent of all automorphisms of a genus-nine Artin–Schreier curve

## Finding
Let \(X/\mathbb F_2\) be the smooth projective normalization of the absolutely irreducible plane curve
\[
 (x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1.
\]
For every integer \(r\geq1\), the full automorphism group of this smooth curve over \(\mathbb F_{2^r}\) is
\[
 \operatorname{Aut}_{\mathbb F_{2^r}}(X)\cong
 \begin{cases}
 C_4\times C_2,&r\text{ odd},\\
 \operatorname{Dih}(C_8)\times C_2,&r\text{ even}.
 \end{cases}
\]
These groups have respective orders \(8\) and \(32\). In particular, the full geometric automorphism group is defined over \(\mathbb F_4\), but not over \(\mathbb F_2\), and \(\mathbb F_4\) is the unique smallest finite extension of \(\mathbb F_2\) over which all geometric automorphisms are defined.

## Assumptions and scope
The ground characteristic is \(2\). Automorphisms mean automorphisms of the smooth, geometrically connected **projective normalization**, not polynomial automorphisms of the displayed affine plane model. The base field \(\mathbb F_{2^r}\) is fixed elementwise. All statements hold for every positive integer \(r\). We use as a published input the geometric full-automorphism classification for this exact curve: Tafazolian, Theorem 1.7, Proposition 3.1 and Proposition 7.2 of arXiv:2609.14830v1. That input gives genus \(9\), the unique bielliptic deck involution and a geometric group of order \(32\), with cyclic order-eight translation lifts split from that deck involution.

## Proof
Write \(k=\overline{\mathbb F}_2\) and use the following birational Artin–Schreier description established in Tafazolian's Proposition 7.2:
\[
 E:\ y^2+xy=x^3+1,\qquad
 X:\ z^2+z=f(x,y):=\frac yx+\frac{x^4+x^3+1}{x^4+x}.
\]
Let \(u\) be the deck involution \((x,y,z)\mapsto(x,y,z+1)\). The elliptic curve \(E\) is ordinary; its geometric group \(T=E[8](k)\) is cyclic of order eight. Tafazolian identifies a split lift \(C=\langle t\rangle\cong C_8\) of the translation subgroup \(T\), commuting with \(u\), and proves that the entire geometric automorphism group \(G=\operatorname{Aut}_k(X)\) has order \(32\), with exact quotient
\[
 1\longrightarrow\langle u\rangle\longrightarrow G
 \longrightarrow T\rtimes\langle[-1]\rangle\longrightarrow1.
\]
Here \([-1]\) acts on \(T\) by inversion. Thus every element of \(G\) has a unique expression \(t^i w^b u^j\), where \(0\leq i<8\) and \(b,j\in\{0,1\}\), for any fixed lift \(w\) of \([-1]\).

Let \(\rho\in\mathbb F_4\setminus\mathbb F_2\) satisfy \(\rho^2+\rho+1=0\). On the displayed elliptic curve the inverse is \(\iota(x,y)=(x,y+x)\). As \(f\circ\iota=f+1\), the formula
\[
 w(x,y,z)=(x,y+x,z+\rho)
\]
defines an involution of \(X\) lifting \(\iota\). Its conjugate under coefficient Frobenius \(\sigma:a\mapsto a^2\) is \(\sigma(w)=uw\), since \(\rho^2=\rho+1\). Also \(\sigma(u)=u\).

The point \(P=(\rho,0)\in E(\mathbb F_4)\) generates \(T\), as verified in Tafazolian's Proposition 7.2 and independently by the exact checker. Direct enumeration of \(E(\mathbb F_2)\) yields precisely \(O,(0,1),(1,0),(1,1)\); hence the Frobenius-fixed subgroup of \(T\) has order four. Because \(T\cong C_8\), and because \(\sigma\) sends \(P\) to \((\rho^2,0)\ne P\), its action on \(T\) must be multiplication by \(5\) (the unique nonidentity unit of \(\mathbb Z/8\mathbb Z\) with exactly four fixed elements). Indeed the elliptic group law gives \(5P=(\rho^2,0)\). Choose the lift \(t\) mapping to translation by \(P\). Since \(\ker(G\to\operatorname{Aut}(E,T))=\{1,u\}\), for some \(\epsilon\in\{0,1\}\),
\[
 \sigma(t)=t^5u^{\epsilon}.
\]
We do **not** need to determine \(\epsilon\). In particular, \(\sigma(t^2)=t^{10}=t^2\). For every normal-form element,
\[
 \sigma(t^i w^b u^j)=t^{5i}w^b u^{\epsilon i+b+j}.
\]
It is fixed by \(\sigma\) exactly when
\[
 4i\equiv0\pmod8,\qquad \epsilon i+b\equiv0\pmod2.
\]
The first condition forces \(i\) even; therefore the second forces \(b=0\). The \(\mathbb F_2\)-automorphism group is exactly \(\langle t^2,u\rangle\cong C_4\times C_2\), of order eight. Galois descent for smooth projective curves identifies this fixed subgroup with the automorphisms defined over \(\mathbb F_2\).

Finally, \(\sigma^2\) fixes \(u,w\) and
\[
 \sigma^2(t)=(t^5u^\epsilon)^5u^\epsilon=t^{25}u^{6\epsilon}=t
\]
because \(t^8=u^2=1\). Thus every geometric automorphism is already defined over \(\mathbb F_4\). For odd extension degree the fixed group of \(\sigma^r\) equals the fixed group of \(\sigma\); for even degree it is all \(G\). This proves the complete extension-degree classification and minimality.

## Verification
The standalone Python 3 file `verify.py` is dependency-free. Run `python3 verify.py`. It implements \(\mathbb F_4\) arithmetically, enumerates the rational elliptic points, verifies the order-eight point and its Frobenius image, and checks both possible Frobenius actions on the order-32 group presentation. The executed output was:

```text
GF4_ELLIPTIC_GROUP_OK
FROBENIUS_ORDER_TWO_OK
DESCENT_C4XC2_AND_MINIMAL_F4_OK
CERTIFICATE_OK
```

The finite computation tests the stated small exact algebra, not the full geometric automorphism theorem, which is an explicit cited published input. The proof above establishes the descent over **all** finite extensions without inferring an infinite statement from sample sizes.

## Relationship to prior work
Tafazolian (2026), Proposition 7.2, gives the same equation over \(\mathbb F_2\), and Theorem 1.7 and Proposition 3.1 determine the *geometric* automorphism group over an algebraic closure. Those results supply crucial inputs. The additional fact here is the exact Frobenius action on the geometric group and the resulting complete arithmetic descent classification, including the strict index-four difference between base-field and geometric automorphisms. Giulietti–Korchmáros (2015) classify large geometric characteristic-two automorphism groups and construct related curves; the inspected introductory and classification material does not state the arithmetic descent classification of this exact \(\mathbb F_2\)-model. Zeta-function data determine point counts but do not determine Frobenius action on the curve's automorphism group.

## Limitations
The computation uses Tafazolian's geometric automorphism theorem as an input; it is not an independent reproof of that theorem. It concerns one particularly natural genus-nine member, not all parameters in the infinite family. Comparison with all historical finite-field automorphism tables is not exhaustive; the related 2015 treatment was inspected only in accessible portions, leaving residual priority risk. No independent mathematical audit has been performed.

## References
1. S. Tafazolian, *Nakajima-extremal Artin--Schreier covers of ordinary elliptic curves in characteristic 2*, arXiv:2609.14830v1 (first public 2026-09-13), especially Theorem 1.7 and Propositions 3.1, 7.2. https://arxiv.org/abs/2609.14830
2. M. Giulietti and G. Korchmáros, *Large 2-groups of automorphisms of algebraic curves over a field of characteristic 2*, J. Algebra 427 (2015), 264–294, doi:10.1016/j.jalgebra.2014.12.019. https://doi.org/10.1016/j.jalgebra.2014.12.019
3. J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer (2009), for the standard characteristic-two elliptic group law and descent framework.
