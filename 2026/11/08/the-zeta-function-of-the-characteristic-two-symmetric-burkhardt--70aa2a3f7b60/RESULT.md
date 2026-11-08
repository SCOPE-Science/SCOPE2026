# The zeta function of the characteristic-two symmetric Burkhardt twist

## Finding
Let \(\sigma_i\) be the elementary symmetric polynomial of degree \(i\) in six homogeneous coordinates. For the quartic threefold
\[
X=\{\sigma_1=\sigma_4=0\}\subset\mathbb P^5_{\mathbb F_2},
\]
write \(q=2^m\), \(m\ge1\). Then
\[
\#X(\mathbb F_q)=\begin{cases}
1+q^3+11q-4q^2,&m\text{ odd},\\
1+q^3-29q+16q^2,&m\text{ even}.
\end{cases}
\]
Consequently,
\[
Z(X/\mathbb F_2,T)=
\frac{(1-2T)^9(1+2T)^{20}}{(1-T)(1-8T)(1-4T)^6(1+4T)^{10}}.
\]
Every \(\mathbb F_2\)-point of \(X\) is singular; in particular, its smooth locus has no \(\mathbb F_2\)-point.

## Assumptions and scope
The equations define the coefficientwise symmetric six-coordinate model, not the standard five-coordinate equation \(B:y_0(y_0^3+y_1^3+y_2^3+y_3^3+y_4^3)+3y_1y_2y_3y_4=0\). The symmetric model is a nontrivial form over \(\mathbb F_2\), but becomes isomorphic to \(B\) over \(\mathbb F_4\), which contains the primitive cube roots of unity. The asserted counts hold for all positive extension degrees, rather than merely the fields enumerated below.

## Proof
**1. Published quadratic splitting and geometric input.** Bruin--Nasserden identify the six-coordinate model \(V(\sigma_1,\sigma_4)\) as a twist of their standard Burkhardt equation and state that these models are isomorphic over fields containing a primitive cube root of unity (their discussion after Proposition 2.8). Hence \(X_{\mathbb F_4}\cong B_{\mathbb F_4}\). Their Theorem 2.2 and Corollary 2.3 provide, at cardinality four, respectively
\[
Z(X/\mathbb F_4,T)=\frac{(1-4T)^{29}}{(1-T)(1-16T)^{16}(1-64T)},
\]
\[
Z(\widetilde X/\mathbb F_4,T)=\frac{1}{(1-T)(1-4T)^{61}(1-16T)^{61}(1-64T)},
\]
where \(\widetilde X\) is obtained by blowing up the 45 ordinary nodes. All geometric nodes and their exceptional smooth quadrics are defined and split over \(\mathbb F_4\).

**2. Restriction on the descent spectrum.** The smooth projective threefold \(\widetilde X\) has pure \(\ell\)-adic cohomology for \(\ell\ne2\). Deligne's weight bounds applied to its displayed zeta function give only even cohomology: ranks \(1,61,61,1\) in degrees \(0,2,4,6\), and the \(\mathbb F_4\)-Frobenius eigenvalues on the two middle spaces are all \(4\) and \(16\), respectively. Thus \(\mathbb F_2\)-Frobenius has eigenvalues only \(\pm2\) on degree two and \(\pm4\) on degree four. For the exceptional quadrics and the zero-dimensional node scheme, the \(H^0\)-terms cancel under the blow-down comparison; their remaining Frobenius eigenvalues are likewise only \(\pm2\) and \(\pm4\), since all nodes and rulings split over \(\mathbb F_4\). Consequently there are integers \(a,b\) such that for every \(m\ge1\), setting \(q=2^m\),
\[
\#X(\mathbb F_q)=1+q^3-qA_m+q^2B_m,
\quad A_m=\begin{cases}a,&m\text{ odd},\\29,&m\text{ even},\end{cases}
\quad B_m=\begin{cases}b,&m\text{ odd},\\16,&m\text{ even}.\end{cases}
\]
The even values follow from the first displayed zeta function over \(\mathbb F_4\).

**3. Determination of the two unknown traces.** Exact exhaustive evaluation of \(\sigma_4\) under \(\sigma_1=0\), on normalized projective representatives over \(\mathbb F_2\) and \(\mathbb F_8=\mathbb F_2[t]/(t^3+t+1)\), gives
\[
\#X(\mathbb F_2)=15,\qquad\#X(\mathbb F_8)=345.
\]
Substitution yields \(-2a+4b=6\) and \(-8a+64b=-168\), whence \(a=-11\), \(b=-4\). These determine all extension counts, as asserted. On the numerator (weight-two) side the positive/negative eigenvalue multiplicities are \(9,20\); on the denominator (weight-four) side they are \(6,10\), yielding the stated zeta function.

**4. Absence of smooth base-field points.** A nonzero six-tuple over \(\mathbb F_2\) satisfying \(\sigma_1=0\) has Hamming weight \(2,4\), or \(6\). Since \(\sigma_4=\binom{w}{4}\pmod2\), exactly the fifteen weight-two tuples lie on \(X\). At each, every ambient partial derivative \(\partial\sigma_4/\partial x_i=\sigma_3(x_0,\ldots,\widehat{x_i},\ldots,x_5)\) vanishes. Hence these are singular on the hyperplane, and none is smooth.

## Verification
Run `python3 burkhardt_twist_verifier.py` with Python's standard library. It implements \(\mathbb F_{2^m}\) as a polynomial quotient by irreducible polynomials of degrees one through four, enumerates every projective point through first-nonzero-coordinate normalization, and independently evaluates \(\sigma_4\) by elementary-symmetric recursion and explicit four-element subsets for extensions of degrees at most three. Observed counts for \(m=1,2,3,4\) are \(15,205,345,7729\), respectively. Counts for the standard Burkhardt model, computed separately, are \(23,205,761,7729\). The two extra degrees are cross-checks; the all-extension theorem follows from the comparison of zeta functions and Frobenius weights, not extrapolation.

## Relationship to prior work
The six-coordinate symmetric Burkhardt equation and its classical geometry are longstanding; Ren--Sam--Sturmfels analyze Burkhardt moduli in characteristic zero. Bruin--Nasserden prove the standard model's zeta formula over fields of characteristic different from three and explicitly distinguish the symmetric twist. Their standard-model count at \(\mathbb F_2\) is \(23\), whereas the present symmetric twist has \(15\). Thus their formula cannot simply be substituted for the twist: the new determination is the quadratic-descent sign distribution, fixed here by exact odd-degree point counts. Bruin--Filatov's later general study of twists explicitly excludes characteristic two. These sources are acknowledged rather than claimed as new.

## Limitations
The zeta function does not assert an independent classification of all twists, rationality of the symmetric form, or a new classification of the 45 classical nodes. Independent validation of the present arithmetic derivation is not claimed. The full historical priority of the explicit symmetric-twist formula is not certified by these comparisons.

## References
- Q. Ren, S. V. Sam, and B. Sturmfels, *Tropicalization of classical moduli spaces*, first arXiv submission 2013-03-05, arXiv:1303.1132; Sections 1 and 3.
- N. Bruin and B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006 (2017); Theorem 2.2, Corollary 2.3, and the discussion following Proposition 2.8.
- N. Bruin and E. Filatov, *Twists of the Burkhardt Quartic Threefold*, arXiv:2207.04393 (2022), characteristic restrictions stated in the abstract.
