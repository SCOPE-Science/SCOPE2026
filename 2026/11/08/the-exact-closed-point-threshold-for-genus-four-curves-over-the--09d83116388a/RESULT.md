# The exact closed-point threshold for genus-four curves over the ternary field

## Finding
Let \(X\) range over all smooth, projective, geometrically connected curves of genus \(4\) over \(\mathbb F_3\). Let \(B_r(X)\) be the number of closed points of degree \(r\), and set
\[
\rho(3,4)=\min\{m\ge1: B_r(X)>0\text{ for every such }X\text{ and every }r\ge m\}.
\]
Then **\(\rho(3,4)=5\)**. Thus every such curve has a closed point of every degree at least five, and this cannot be improved to degree four.

## Assumptions and scope
All fields are finite fields of characteristic three, all curves are smooth, projective, geometrically connected, and genus is geometric genus. The curve used for the lower bound is the smooth projective completion of the affine hyperelliptic model
\[
C:\qquad y^2=x^9-x\quad\text{over }\mathbb F_3.
\]
The point-count argument uses extensions \(\mathbb F_9\subset\mathbb F_{81}\). No assertion is made about smaller degrees, nor about rational points of other varieties.

## Proof
**1. The genus-four witness is smooth.** The polynomial \(f(x)=x^9-x\) has derivative \(f'(x)=-1\) in characteristic three, hence is squarefree. Since its degree is nine and the characteristic is not two, the smooth projective hyperelliptic curve \(y^2=f(x)\) has genus \((9-1)/2=4\) and one rational point at infinity.

**2. It has no closed points of degree four.** For \(x\in\mathbb F_9\), one has \(x^9-x=0\); there is exactly one affine point \((x,0)\) above each such \(x\). Thus \(\#C(\mathbb F_9)=9+1=10\). Now let \(x\in\mathbb F_{81}\setminus\mathbb F_9\), and set \(v=x^9-x\ne0\). Since \(x^{81}=x\),
\[
v^9=x^{81}-x^9=x-x^9=-v,
\qquad v^8=-1,
\qquad v^{40}=(-1)^5=-1.
\]
A nonzero element of \(\mathbb F_{81}\) is a square exactly when its fortieth power is \(1\). Consequently \(v\) is a nonsquare and no \(y\in\mathbb F_{81}\) can satisfy \(y^2=v\). Only the nine affine points above \(\mathbb F_9\), plus infinity, remain: \(\#C(\mathbb F_{81})=10\). Because the divisors of \(4\) are \(1,2,4\), Möbius inversion gives
\[
4B_4(C)=\#C(\mathbb F_{81})-\#C(\mathbb F_9)=0.
\]
Therefore \(\rho(3,4)\ge5\).

**3. Degree five and every larger degree are universal.** Proposition 2.2 of Aubry–Herbaut–Monaldi gives the following consequence of a lower bound for closed points: whenever \(r\ge2\) and \((q^{r/4}-1)^2\ge2g\), every smooth, projective, geometrically connected genus-\(g\) curve over \(\mathbb F_q\) has \(B_r>0\). For \(q=3\) and \(g=4\), the condition holds at \(r=5\), since
\[
3^{5/4}>\frac{39}{10}>1+\sqrt 8.
\]
Both strict inequalities follow exactly from \(39^4<3^5\cdot10^4\) and \(29^2>8\cdot10^2\). The condition is monotone in \(r\), hence holds for every \(r\ge5\). Thus \(\rho(3,4)\le5\), proving the equality.

## Verification
The self-contained `verify_rho34.py` checks arithmetic in the field \(\mathbb F_3[u]/(u^4+u-1)\), confirms the nine-element fixed subfield, tests the nonsquare identity for all \(72\) remaining field elements, and checks the exact rational inequalities underlying the universal bound. Run `python verify_rho34.py` in the directory containing this document. Expected final line: `RHO_3_4_EXACT_WITNESS_AND_BOUND_PASS 10 10`. The general bound is used as a published theorem; the finite computation is corroboration of the explicit lower-bound proof, not a proof by extrapolation.

## Relationship to prior work
Aubry, Herbaut, and Monaldi established general closed-point bounds and exact threshold tables for genera one through three; their 2023 preprint does not give the value for genus four and \(q=3\). The upper bound used here is an existing theorem, not a new inequality. The equation \(y^2=x^9-x\) is of classical hyperelliptic/finite-field type; no novelty is claimed for the equation itself. The contribution is the combination of its exact extension-degree obstruction with the known universal bound to pin down the natural threshold. Xarles's 2020 census pertains to curves over \(\mathbb F_2\), so it does not decide \(\rho(3,4)\). Lario's finite-field Diophantine-stability lists were also compared, but those lists do not directly state the present closed-point threshold.

## Limitations
The result proves only the exact value of \(\rho(3,4)\); it is not a census of genus-four curves over \(\mathbb F_3\). The point-count proof does not require classification of such curves. A mathematically equivalent formulation may occur in unindexed literature on hyperelliptic curves or finite-field places. No independent audit or novelty certification has been performed.

## References
1. Y. Aubry, F. Herbaut, and J. Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218v1 (first public October 17, 2023), especially Proposition 2.2 and the definition of \(\rho(q,g)\). https://arxiv.org/html/2310.11218v1
2. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822v1 (July 15, 2020); relevant for comparison of field, genus, and prior census coverage only. https://arxiv.org/pdf/2007.07822
3. J. C. Lario, *Curves over Finite Fields with Diophantine Stability* (online data tables; date not asserted). https://web.mat.upc.edu/joan.carles.lario/DS.html
