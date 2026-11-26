# The marked trigonal descent of a cyclic Hermitian quotient in characteristic eleven

Let \(C/\mathbb F_{11}\) be the smooth canonical curve
\[
y^2z=x^3+z^3,\qquad w^2=xy.
\]
Its canonical trigonal map is \(t=w/x\). Let \(G\) be its trigonal normal closure. The following identifies the **marked cover**, not merely the isomorphism class of its geometric curve.

* The cover \(G\to\mathbb P^1_t\) is regular \(S_3\)-Galois of degree six. Its only branch divisor is \(4t^{12}-27=0\), with transposition inertia and twelve simple geometric values. The fiber at infinity is unramified and split over \(\mathbb F_{11}\). The sign quotient is the genus-five curve \(v^2=4t^{12}-27\).
* Over \(k_2=\mathbb F_{121}\), set \(H:A^{12}+B^{12}=1\) (the affine Fermat model of the Hermitian curve), take \(i\in k_2\) with \(i^2=-1\) and pick \(\zeta\in k_2\) primitive of order three. Then
  \[
  G_{k_2}=H/\langle (A,B)\longmapsto(iA,i^{-1}B)\rangle,\qquad t=4AB.
  \]
  The \(\mathbb F_{11}\)-descent on this quotient is the semilinear action conjugating constants and interchanging \(A,B\). In particular this is a specified trigonal descent of a known kind of maximal quotient, not a claim of a new unmarked genus-thirteen maximal curve.
* The finite unramified Frobenius counts for the marked \(S_3\)-cover (identity, transposition, 3-cycle) are \((0,5,4)\) over \(\mathbb F_{11}\) and \((61,0,48)\) over \(\mathbb F_{121}\). There are respectively 2 and 12 finite rational branch parameters, with three rational points of \(G\) above each; infinity contributes six in either field.

Consequently \(g(G)=13\), \(\#G(\mathbb F_{11})=12\), \(\#G(\mathbb F_{121})=408\); the last count is also forced by the Hermitian quotient description. The Weil numerator over \(\mathbb F_{11}\) is \((1+11T^2)^{13}\); the rational Jacobian order is \(12^{13}=106993205379072\).

## Proof of the marked trigonal description

The superspecial bielliptic starting model is the characteristic-eleven model in Ogasawara–Ohashi–Sakata–Harashita, §4.4. Its geometric connectedness also follows from the double cover of the smooth elliptic cubic: the section \(xy\) has six simple zeros, namely the point at infinity, the two affine points with \(x=0\), and the three with \(y=0\). On \(xz\ne0\), write \(u=x/z\); then \(y/z=t^2u\), and \(u^3-t^4u^2+1=0\). The variable \(t\) parametrizes the rulings of the canonical cone \(w^2=xy\). At the two affine points with \(x=0\), \(x\) has order two on the double cover while \(w\) has order one, giving simple poles of \(t\). At the elliptic point at infinity use the chart \(y=1\): \(x\) is a parameter and \(z\) has order three there; again upstairs \(x\) has order two and \(w\) order one. These are all poles and all three are rational. Thus the degree of \(t\) is three and infinity splits unramified in the cubic subcover. The same calculation over an algebraic closure gives geometric irreducibility of the cubic.

The discriminant \(4t^{12}-27\) has twelve distinct roots (its derivative is \(4t^{11}\) in this characteristic) and is not a square over \(\overline{\mathbb F}_{11}(t)\). The geometric splitting group is thus \(S_3\); as the arithmetic group is also contained in \(S_3\), the cover is regular. A unit discriminant gives unramified roots. At a simple discriminant zero the cubic has a double root and a distinct simple root. The simple factor separates locally, and the remaining quadratic has discriminant of valuation one, so inertia is a transposition. The local splitting at infinity remains complete in the normal closure. Thus tame Riemann–Hurwitz gives \(2g-2=-12+12\cdot3\). The discriminant square-root field is the fixed field of \(A_3\), giving the stated sign quotient and its genus by the twelve simple branch points.

## Hermitian identification and descent

In the function field of \(H\), put \(X=-A^4\), \(Y=-B^4\) and \(t=4AB\). Then \(X^3+Y^3=-1\), and \(3XY=t^4\) since \(4^4=3\) in \(\mathbb F_{11}\). For \(j=0,1,2\) put \(r_j=\zeta^jX+\zeta^{-j}Y\). These are the three distinct generic roots of the reciprocal cubic \(r^3-t^4r+1\); this follows by cubing and subtracting \(3XYr_j\). Conversely \(X=\frac13\sum_j\zeta^{-j}r_j\) and \(Y=\frac13\sum_j\zeta^jr_j\). Thus \(k_2(t,X,Y)\) is the splitting field after extension of constants. It is also the invariant field for the displayed order-four diagonal group: the three generators are invariant, and adjoining \(A\) (satisfying a fourth-power equation) recovers \(B=t/(4A)\), so the invariant extension has degree exactly four.

Conjugation on \(k_2\) sends \(\zeta\) and \(i\) to their inverses. Combine it with swapping \(A,B\); it normalizes the order-four group, fixes \(t\), and fixes each \(r_j\) individually. The fixed field on the quotient is therefore exactly \(\mathbb F_{11}(t,r_0,r_1,r_2)\), the original reciprocal splitting field, rather than an unspecified form of the quotient. The cubic subcover is fixed by the involution interchanging the other two roots. In particular the known Hermitian maximality passes to this quotient over \(k_2\), independently of the fiber computation.

## Finite splitting certificate

The distinct-root histograms in increasing root count (0,1,2,3) are \((4,5,2,0)\) and \((48,0,12,61)\), respectively. To reproduce, build the histogram of the map \(u\mapsto u+u^{-2}\) on nonzero field elements, and for every \(t\) look up the count at \(t^4\). Use residues modulo 11 for the first field and pairs \(a+bi\), \(i^2=-1\), for the second. Exact pseudocode is:

```
count = default_zero_dictionary()
for u in field:
    if u != 0: count[u + (u.inverse())**2] += 1
hist = [0, 0, 0, 0]
for t in field: hist[count[t**4]] += 1
```

The fiber sizes of \(t\mapsto t^4\) on the nonzero image are 2 and 4 respectively; the second field has 12 branch values since \(t^{12}\) is its norm and \(27/4=4\). In the first field \(t^{12}=t^2\), so the two branch values are \(\pm2\). The distinct simple and double roots at a rational branch parameter are rational (equivalently the linear gcd with the derivative has rational coefficients and the third root is then rational). The local quadratic is totally ramified, so the decomposition group equals inertia and the branch fiber has three rational points. Away from the branch points the permutation type is determined by the number of roots, giving the claimed counts. Fully split fibers give six rational points, and nonsplit unramified fibers none; hence \(6+3\cdot2=12\) and \(6+3\cdot12+6\cdot61=408\). Maximality over \(k_2\) implies the \(\mathbb F_{11}\) Weil eigenvalues square to \(-11\); trace zero forces equal multiplicities. This proves the numerator and the Jacobian order.

## Prior coverage and scope

Montanucci–Zini, *On the spectrum of genera of quotients of the Hermitian curve*, [arXiv:1703.10592](https://arxiv.org/abs/1703.10592), Table 11, already list the genus-thirteen \(C_4\) quotient of \(H_{11}\) for a generator of type (B1). The diagonal generator here is of that type (the three distinct eigenpoints lie off the curve and form a self-polar triangle). The genus, existence of such a maximal curve, and its \(\mathbb F_{121}\) point total are therefore not claimed as new. The comparison to general Hermitian quotient constructions, including *Explicit plane models for all Galois quotients of the Hermitian curve*, [arXiv:2611.14073](https://arxiv.org/abs/2611.14073), concerns the unmarked quotient. The present identification specifies the actual map \(t=4AB\) realizing the normal closure of the known genus-four trigonal map, its descent and marked splitting. It gives neither a classification of Hermitian descents nor historical-priority certification.

The starting superspecial genus-four object is from T. Ogasawara, R. Ohashi, K. Sakata and S. Harashita, [arXiv:2403.08139](https://arxiv.org/abs/2403.08139), §4.4; the earlier genus-four census is M. Kudo and S. Harashita, [arXiv:1702.05313](https://arxiv.org/abs/1702.05313).
