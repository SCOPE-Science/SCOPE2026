# A wild normalization jump for Hauser's Calyx

## Finding
For an algebraically closed field \(k\), put \(X=\operatorname{Spec}R\) with
\[
R=k[x,y,z]/(x^2+y^2z^3-z^4).
\]
The normalizations and conductors of this fixed integral surface change sharply in characteristic \(2\):

* If \(\operatorname{char}k\ne2\), the integral closure of \(R\) is \(S=k[y,z,t]/(t^2+y^2z-z^2)\), embedded via \(x=zt\). This is a normal surface with one rational double point of type \(A_3\). Its conductor, viewed as an ideal of \(R\), is \((z,x)\); as a module over \(A=k[y,z]\), \(S/R\cong A/(z)\).
* If \(\operatorname{char}k=2\), the integral closure is \(S=k[y,t]\), embedded via \(z=t^2\) and \(x=t^4+yt^3\). Its conductor in \(R\) is \((yz,x+z^2)\), and \(S/R\cong A/(yz)\). In this case the normalization is smooth; the reduced nonnormal locus is the union of \(V(x,z)\) and \(V(y,x+z^2)\).

The second component exists only in characteristic \(2\). In particular, the generic point of that extra component has a purely inseparable degree-two preimage on the normalization.

## Assumptions and scope
The base field is algebraically closed. The statement concerns the affine model displayed above, rather than a projective compactification, arbitrary deformations or stable reduction. In this result the conductor is \(\{r\in R:rS\subseteq R\}\), and the normalization quotient is considered as an \(A\)-module. The singular locus means the reduced support of the Jacobian singular scheme, not a claim of scheme-theoretic equality.

## Proof
Write \(A=k[y,z]\). If the characteristic is not two, the polynomial \(t^2+y^2z-z^2\) defines a domain \(S\), and \(x=zt\) satisfies the Calyx equation. As an \(A\)-module,
\[
S=A\oplus tA,\qquad R=A\oplus ztA.
\]
The fraction fields agree because \(t=x/z\) away from \(z=0\). This proves that \(S\) is a finite birational extension, with quotient \(S/R\cong (A/zA)t\). The only common zero of the three derivatives of the defining equation of \(S\) is the origin. Since \(S\) is a hypersurface of dimension two, it is Cohen--Macaulay and regular in codimension one, hence normal. Writing \(u=z-y^2/2\) gives
\[
t^2+y^2z-z^2=t^2-u^2+y^4/4,
\]
so the origin is an \(A_3\) surface singularity (over any characteristic other than two). Multiplication of \(r=a+ztb\) by \(t\) lies in \(R\) precisely when \(z\mid a\), since \(t^2=z^2-y^2z\in A\). Thus \((R:S)=zS=(z,x)R\). The derivatives of the Calyx equation show that its reduced singular locus is \(V(x,z)\).

If the characteristic is two, set \(w=x+z^2\), yielding \(R=A[w]/(w^2+y^2z^3)\). This is a domain: the valuation of \(y^2z^3\) at \(z=0\) is odd, hence this element is not a square in \(k(y,z)\). Put \(t=w/(yz)\) in the common fraction field. The relation gives \(t^2=z\) and \(w=yt^3\). Conversely, \(t\) is integral over \(R\), and
\[
S=k[y,t]=A\oplus tA,\qquad R=A\oplus yztA.
\]
Thus \(S\) is a finite birational normal extension and consequently the full integral closure. The quotient is \((A/(yz))t\). Multiplication of \(a+yztb\) by \(t\) belongs to \(R\) exactly when \(yz\mid a\), so
\[
(R:S)=yzS=(yz,w)R=(yz,x+z^2)R.
\]
Here \(F_x=F_y=0\) identically and \(F_z=y^2z^2\), where \(F=x^2+y^2z^3-z^4\). The reduced singular support is therefore \(V(z,x)\cup V(y,x+z^2)\). On the second component \(y=0\), the normalization restricts to \(z=t^2\), a radicial degree-two map. The two branches of the reduced nonnormal locus meet at the origin. This completes the proof.

## Verification
A standalone Python/SymPy checker (`verify.py`) verifies the integral identities behind both normalization presentations, the characteristic-two parametrization, the coordinate change to \(A_3\), and conductor-generator multiplication. Its recorded output is `verify_output.txt`. The proof of normality, the conductor equality and the singular-support statement are algebraic arguments above, not conclusions drawn from finite sampling.

## Relationship to prior work
Hauser introduced the Calyx as a sequence of contractions from a smooth surface and explicitly described its connection to the Calypso \(t^2+y^2z=z^2\). This source is acknowledged, and the characteristic-different-from-two normalization is an immediate algebraic consequence. The additional result is the complete **characteristic-two** normalization, conductor quotient, and second nonnormal component in the *same integral equation*. Neither the dated manuscript's relevant example section nor the publicly accessible accompanying gallery describes these wild-characteristic assertions. This is a limited literature comparison, not a claim of absolute historical priority.

## Limitations
No stable model, global resolution of a projective completion, or independent external audit is asserted. The first public appearance of the exact equation predates or coincides with Hauser's dated 2006 manuscript; a separately authenticated earliest web-posting date was not established. Search non-hits cannot establish priority, and unindexed sources may contain an equivalent wild-characteristic calculation.

## References
1. H. Hauser, *Desingularization of Ideals and Varieties*, publicly accessible primary manuscript dated September 27, 2006, opening example and characteristic-zero scope, https://homepage.univie.ac.at/herwig.hauser/Publications/DESINGULARIZATION.pdf .
2. H. Hauser, *Gallery of Singular Algebraic Surfaces*, Calyx and Calypso descriptions, https://www.imaginary.org/gallery/herwig-hauser-classic .
3. E. Faber and H. Hauser, *Today's Menu: Geometry and Resolution of Singular Algebraic Surfaces*, Bull. AMS 47 (2010), 373--417, DOI:10.1090/S0273-0979-10-01295-4 (related characteristic-zero framework).
