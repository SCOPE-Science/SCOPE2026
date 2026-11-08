# Cartier stratification of a cyclic genus-four double-elliptic family in characteristics five and seven

## Finding

Let \(k=\overline{\mathbf F}_p\), with \(p\in\{5,7\}\), and let \(t\in k\) satisfy \(t^2\ne1\). Define a projective complete-intersection curve \(C_t\subset\mathbf P^3_k\) by
\[
 P=y^2z-x^3-z^3=0,\qquad Q=w^2-x(y+tz)=0.
\]
Let \(E\colon y^2z=x^3+z^3\), let \(\pi:C_t\to E\) be the map forgetting \(w\), and let \(P_t=\operatorname{Prym}(C_t/E)\). Every \(C_t\) is a smooth non-hyperelliptic genus-four curve, the elliptic quotient is \(E\), and the Prym \(P_t\) has dimension three. The geometric Jacobian and Prym \(p\)-ranks \(f\) and \(a\)-numbers are exactly as follows (the statements count coefficient parameters, not isomorphism classes).

| Characteristic | Condition on the parameter | \((f(J(C_t)),a(J(C_t)))\) | \((f(P_t),a(P_t))\) |
| --- | --- | --- | --- |
| \(5\) | \(t^2\ne1,2\) | \((1,3)\) | \((1,2)\) |
| \(5\) | \(t^2=2\) | \((0,4)\) | \((0,3)\) |
| \(7\) | \(t^2\ne1\), \(t(t^2-2)(3t^2-2)\ne0\) | \((3,1)\) | \((2,1)\) |
| \(7\) | \(t^2=2\) or \(t^2=3\) | \((2,2)\) | \((1,2)\) |
| \(7\) | \(t=0\) | \((1,3)\) | \((0,3)\) |

In characteristic seven, **the Prym is superspecial at the unique geometric coefficient value \(t=0\)**, whereas the elliptic quotient is ordinary and the full genus-four Jacobian is not superspecial. In characteristic five, there are exactly two geometric coefficient values \(t^2=2\) making the full Jacobian (and Prym) superspecial. Every stratum listed is nonempty. In particular, the characteristic-seven Prym has no \(p\)-rank-one/\(a\)-number-one stratum in this family.

## Assumptions and scope

All invariants are computed over the algebraic closure \(k\). For a smooth curve \(X/k\), its \(p\)-rank is \(f(J(X))=\dim_{\mathbf F_p}J(X)[p](k)\) and its \(a\)-number is \(a(J(X))=\dim_k\operatorname{Hom}(\alpha_p,J(X)[p])\). We use the same definitions for an abelian variety such as \(P_t\). An abelian threefold with \(a=3\) is superspecial. The arithmetic classification concerns the explicit one-parameter family and its distinguished degree-two elliptic quotient, not every genus-four curve or every possible Prym. We do not classify the parameters up to curve isomorphism or determine complete Newton polygons beyond what the displayed invariants imply.

## Proof

**Smoothness, degree, and genus.** The cubic \(E\) is smooth in characteristics five and seven because the discriminant of \(y^2=x^3+1\) is nonzero. The quadratic on \(E\), \(q=x(y+tz)\), vanishes on the divisor \((x=0)\cap E\), consisting of \((0:1:0)\) and \((0:\pm1:1)\), and on \((y+tz=0)\cap E\), consisting of three points whose \(x\)-coordinates satisfy \(x^3=t^2-1\). The latter are distinct when \(t^2\ne1\) since \(p\ne3\); the two sets are disjoint under the same assumption, and the intersections are transverse. Thus \(q\) has six simple zeros on \(E\); the induced quadratic cover is separable, geometrically connected, and simply ramified there. Its projective model is smooth by the transverse-intersection criterion for these complete intersections. Riemann–Hurwitz yields \(2g(C_t)-2=2(2g(E)-2)+6=6\), so \(g(C_t)=4\). The canonical complete-intersection embedding of type \((2,3)\) makes it non-hyperelliptic. The Prym's dimension is \(g(C_t)-g(E)=3\). To explain the cyclic symmetry, choose \(\eta\in k\) of order six and put \(\zeta=\eta^2\); then \( (x:y:z:w)\mapsto(\zeta x:y:z:\eta w)\) preserves both equations and has order six, with the double-cover involution as its cube.

**Hasse–Witt calculation.** For the ordered exponent vectors
\[
 e_1=(1,1,1,2),\quad e_2=(1,1,2,1),\quad e_3=(1,2,0,1),\quad e_4=(2,1,1,1),
\]
the standard complete-intersection coefficient formula (Ogasawara--Ohashi--Sakata--Harashita, Lemma 2.10) gives the \((i,j)\) entry of the Hasse–Witt matrix as the coefficient of
\[
 x^{pe_{i1}-e_{j1}}y^{pe_{i2}-e_{j2}}z^{pe_{i3}-e_{j3}}w^{pe_{i4}-e_{j4}}
\]
in \((PQ)^{p-1}\). Direct multinomial expansion, reduced in the indicated characteristic, yields the **whole** four-by-four matrices
\[
 M_5(t)=\operatorname{diag}(0,0,0,t^2-2),
\]
\[
 M_7(t)=\operatorname{diag}(3,3t^3-2t,0,t^3-2t).
\]
The coefficient calculation can be reconstructed as follows: expand \(P^{p-1}\) by choosing \(a\) factors \(y^2z\), \(b\) factors \(-x^3\), and \(c=p-1-a-b\) factors \(-z^3\). Expand \(Q^{p-1}\) with \(d\) factors \(w^2\), \(e\) factors \(-xy\), and \(h=p-1-d-e\) factors \(-txz\). The monomial is \(x^{3b+e+h}y^{2a+e}z^{a+3c+h}w^{2d}\) with \(t\)-degree \(h\); its coefficient is the product of the two multinomial coefficients times \((-1)^{b+c+e+h}\). Match these four exponents to the target exponents for each \((i,j)\), sum the matching coefficients, and reduce modulo \(p\). Both independent verification programs included with this note reconstruct all sixteen entries in each characteristic.

**Rank and \(a\)-number.** Frobenius on \(H^1(C_t,\mathcal O_{C_t})\) is semilinear with the displayed diagonal matrix. Every nonzero diagonal coordinate survives every iterate, and each zero coordinate is killed, so the stable Frobenius rank, hence the Jacobian \(p\)-rank, equals the number of nonzero diagonal entries. The Cartier \(a\)-number is the nullity, namely four minus that number. For \(p=5\) the only possible zero of the final entry on the smooth base is \(t^2=2\). For \(p=7\), the two nonconstant entries vanish on the respective sets \(\{t=0\}\cup\{t^2=3\}\) and \(\{t=0\}\cup\{t^2=2\}\). Their common zero is only \(t=0\); both quadratic zero sets are separable, disjoint, and avoid \(t^2=1\). This proves the Jacobian rows with exact quantifiers.

**Prym invariants.** The quotient elliptic curve \(E\) has Hasse invariant equal to the coefficient of \(x^{p-1}\) in \((x^3+1)^{(p-1)/2}\). This is zero when \(p=5\) and equal to \(3\ne0\) when \(p=7\); therefore \((f(E),a(E))=(0,1)\) and \((1,0)\), respectively. The norm map and pullback for the ramified degree-two cover give an isogeny \(E\times P_t\to J(C_t)\) whose kernel is killed by a power of two. Since \(p\) is odd, this induces an isomorphism on the \(p\)-divisible groups, so both \(p\)-ranks and \(a\)-numbers add. Subtract the elliptic pair from the Jacobian pair to obtain each Prym row. At \(p=7,t=0\), \((f(P_t),a(P_t))=(0,3)\), so \(P_t\) is superspecial, whereas \(E\) is ordinary and \(J(C_t)\) has \(p\)-rank one.

## Verification

The self-contained scripts `verify_multinomial.py` and `verify_expansion.py` use independent exact modular arithmetic implementations: a multinomial coefficient enumeration and a five-variable sparse polynomial multiplication. Run `python3 verify_multinomial.py` and `python3 verify_expansion.py` from the directory containing the scripts. Both check the full sixteen-entry matrices, not selected minors, at both primes. Their expected terminal markers are `VERIFY_MULTINOMIAL_PASS` and `VERIFY_EXPANSION_PASS`. Their proof role is finite exact coefficient identity verification; the geometric and Prym deductions above remain mathematical arguments independent of a particular software run.

## Relationship to prior work

Ogasawara, Ohashi, Sakata and Harashita (arXiv:2403.08139, first posted March 12, 2024) establish the general genus-four double-elliptic model, the transversality criterion, and the Hasse–Witt coefficient formula used here. Their Table 1 and Section 4.3 **already** report the unique genus-four superspecial isomorphism class in characteristic five (known earlier from Fuhrmann–Garcia–Torres) and the absence of any superspecial genus-four curve in characteristic seven (known earlier from Kudo–Harashita). This note does **not** claim those results as new. The same source explicitly points to Prym superspeciality as a separate question in its conclusion. Its stated algorithms and superspecial classification do not give the displayed full parameter-by-parameter \(p\)-rank and \(a\)-number stratification, nor do they imply the characteristic-seven superspecial-Prym locus over an ordinary elliptic quotient without an additional computation. Results on superspecial hyperelliptic genus-four curves concern a different geometric class. The mathematical contribution here is the evaluated cyclic family's full Hasse–Witt and Prym stratification, not the standard general coefficient algorithm.

## Limitations

Parameter counts are counts in \(k\), not geometric isomorphism-class counts. The two characteristic-five exceptional values may represent the known single superspecial genus-four isomorphism class; no contrary assertion is made. The characteristic-seven Jacobians are never superspecial, consistently with the established global nonexistence theorem. Full Newton polygons and automorphism group classifications are not asserted. The literature comparison cannot exclude an unindexed earlier evaluation of the same cyclic family. No independent mathematical or priority audit is claimed.

## References

1. T. Ogasawara, R. Ohashi, K. Sakata, S. Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139, version 1 first publicly submitted 2024-03-12; v2, Sections 2.2, 2.4, 4.3, 5. https://arxiv.org/html/2403.08139v2
2. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, Finite Fields and Their Applications 45 (2017), 131–169; referenced in [1], Section 4.3.
3. R. Fuhrmann, A. Garcia, F. Torres, *On maximal curves*, Journal of Number Theory 67 (1997), 29–51; referenced in [1], Section 4.3.
4. M. Kudo, T. Nakagawa, T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing a cyclic group of order six*, arXiv:2210.14822 (2022); a different hyperelliptic genus-four setting.
