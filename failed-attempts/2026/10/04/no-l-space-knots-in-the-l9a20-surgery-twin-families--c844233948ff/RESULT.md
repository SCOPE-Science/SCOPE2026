# No L-space knots in the L9a20 surgery-twin families
## Finding
Let \(K_m\) and \(J_n\) denote the two twist families constructed from the two-component link `L9a20` in Kegel--Schmalian Theorem 2.13:
\[
K_m=L9a20(*,1/m),\qquad J_n=L9a20(1/n,*).
\]
For every nonzero integer \(m\) and every nonzero integer \(n\), neither \(K_m\) nor \(J_n\) is an L-space knot.

More precisely, for \(|m|\ge3\), the normalized Alexander polynomial of \(K_m\) has a coefficient of absolute value \(7\). For the four remaining nonzero parameters
\[
m=-2,-1,1,2,
\]
the maximum absolute Alexander coefficient is, respectively,
\[
7,\ 13,\ 9,\ 7.
\]
For \(n\ge4\) or \(n\le-5\), the normalized Alexander polynomial of \(J_n\) has a coefficient of absolute value \(7\). For the seven remaining nonzero parameters
\[
n=-4,-3,-2,-1,1,2,3,
\]
the maximum absolute Alexander coefficient is, respectively,
\[
7,\ 7,\ 5,\ 13,\ 9,\ 7,\ 7.
\]

Thus every nonzero member of both surgery-twin families violates the Alexander-polynomial coefficient constraint for L-space knots.

## Assumptions and scope
An L-space knot means a knot in \(S^3\) admitting a positive Dehn surgery to an L-space. A standard consequence of Ozsváth--Szabó knot Floer theory is that the normalized Alexander polynomial of an L-space knot has all nonzero coefficients equal to \(1\) or \(-1\), with alternating signs.

The families \(K_m\) and \(J_n\) are exactly those of Kegel--Schmalian Theorem 2.13. Their source link has two unknotted components of linking number one. The theorem uses explicit Alexander polynomials obtained by the Baker--Motegi/Torres specialization method to distinguish twist-family members and establish multiple surgery descriptions.

The parameters \(m=0\) and \(n=0\) are excluded because Theorem 2.13 is stated for nonzero family parameters and the present classification concerns precisely that family.

## Proof
Kegel and Schmalian compute
\[
\Delta_{K_m}(t)\doteq
t^{4m+2}-t^{4m+1}-3t^{3m+2}+4t^{3m+1}-t^{3m}
+3t^{2m+2}-7t^{2m+1}+3t^{2m}
-t^{m+2}+4t^{m+1}-3t^m-t+1
\]
and
\[
\Delta_{J_n}(t)\doteq
t^{2n+4}-3t^{2n+3}+3t^{2n+2}-t^{2n+1}
-t^{n+4}+4t^{n+3}-7t^{n+2}+4t^{n+1}-t^n
-t^3+3t^2-3t+1,
\]
where \(\doteq\) means equality up to multiplication by a unit \(\pm t^k\).

The source observes that, after normalization, all thirteen displayed exponents for \(K_m\) are strictly ordered when \(|m|\ge3\). Hence no cancellation can affect the coefficient \(-7\), so the normalized polynomial has a coefficient of absolute value \(7\).

For \(m=-2,-1,1,2\), direct collection of coincident exponents gives maximum absolute coefficients
\[
7,\ 13,\ 9,\ 7.
\]
Therefore every \(K_m\) with \(m\ne0\) has a nonzero Alexander coefficient of absolute value greater than \(1\).

Likewise, the source observes that the thirteen exponents in the normalized expression for \(J_n\) are strictly ordered when \(n\ge4\) or \(n\le-5\). The coefficient \(-7\) therefore survives unchanged throughout those ranges.

For the remaining values \(n=-4,-3,-2,-1,1,2,3\), collecting coincident exponents gives maximum absolute coefficients
\[
7,\ 7,\ 5,\ 13,\ 9,\ 7,\ 7.
\]
Thus every \(J_n\) with \(n\ne0\) has a nonzero Alexander coefficient of absolute value greater than \(1\).

Ozsváth--Szabó's L-space-knot Alexander-polynomial constraint now excludes every one of these knots from the L-space-knot class.

## Verification
The current full text of Kegel--Schmalian was inspected at the definition of `L9a20`, Lemma 2.12, Theorem 2.13, and the displayed one-variable Alexander-polynomial formulas. The source itself separates the same infinite parameter ranges from the finite exceptional set because exponent collisions occur only in the exceptional parameters.

The L-space-knot coefficient obstruction was checked against published accounts deriving it from Ozsváth--Szabó knot Floer theory. In particular, Krčatovich records the staircase consequence for knots admitting positive L-space surgery, and the standard formulation says every nonzero Alexander coefficient is \(1\) or \(-1\).

The bundled verifier expands the published formulas, exactly checks all eleven exceptional parameters, and samples the non-collision ranges through absolute parameter \(500\). It prints:

`VERIFY_OK K_exceptional=4 J_exceptional=7 sampled_K=996 sampled_J=993 all_have_coefficient_abs_gt_1=true`

The finite range sampling is not the infinite proof. The infinite proof is the symbolic exponent-order split above, together with the source's monotonicity observation.

## Relationship to prior work
Kegel--Schmalian Theorem 2.13 constructs the families \(K_m\) and \(J_n\), proves the knots are distinct, and uses their Alexander polynomials to distinguish the twist-family members. The paper separately proves a positive result for hyperbolic L-space knots: infinitely many integer slopes are strongly characterising. It does not classify whether the knots in its negative surgery-twin construction are L-space knots.

Baker--Motegi study when twist families can contain L-space knots, including the delicate linking-number-one case relevant here, but their general theorems do not force the complete zero-member classification for this specific `L9a20` family.

The present finding closes that interface exactly: the entire nonzero `L9a20` surgery-twin construction lies outside the L-space-knot class. Targeted literature searches using the family name, both family notations, the `L9a20` identifier, Alexander coefficients, and L-space terminology did not locate this complete parameter classification.

## Limitations
This result does not determine whether the knots \(K_m\) or \(J_n\) are hyperbolic, fibered, or strongly quasipositive, and it does not classify their knot Floer complexes.

The argument is an obstruction only: having all Alexander coefficients in \(\{-1,0,1\}\) would not by itself prove that a knot is an L-space knot.

The calculation is specific to the `L9a20` families in Theorem 2.13. It does not assert that other families of knots with multiple surgery descriptions avoid L-space knots.

## References
1. M. Kegel and M. Schmalian, *Unique Surgery Descriptions along Knots*, arXiv:2508.18521v1, first posted 2025-08-25.
2. K. L. Baker and K. Motegi, *Twist families of L-space knots, their genera, and Seifert surgeries*, Communications in Analysis and Geometry 27 (2019), 743--790; arXiv:1506.04455.
3. D. Krčatovich, *A restriction on the Alexander polynomials of L-space knots*, Pacific Journal of Mathematics 297 (2018), 117--138, DOI `10.2140/pjm.2018.297.117`.
4. P. Ozsváth and Z. Szabó, *On knot Floer homology and lens space surgeries*, Topology 44 (2005), 1281--1300, DOI `10.1016/j.top.2005.05.001`.
