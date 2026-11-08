# Canonical Weierstrass-weight jumps at two branch fibers of a symmetric genus-17 Humbert–Edge family

## Finding

Let \(t\in\mathbb C\setminus\{0,1,-1\}\), and let \(C_t\subset\mathbb P^5_{\mathbb C}\) be the intersection of the four diagonal quadrics
\[
X_0^2+X_1^2+X_2^2=0,\quad
-X_0^2+X_1^2+X_3^2=0,\quad
tX_0^2+X_1^2+X_4^2=0,\quad
-tX_0^2+X_1^2+X_5^2=0.
\]
This smooth curve has genus \(17\). The reduced fibers \(R_0=C_t\cap\{X_0=0\}\) and \(R_1=C_t\cap\{X_1=0\}\) each consist of \(16\) distinct points. Define
\[
P(t)=44t^4-117t^2+44,\qquad
Q(t)=208t^8-656t^6+1527t^4-656t^2+208.
\]
At **every one of these \(32\) points**, the canonical Weierstrass weight is
\[
w_{C_t}(p)=\begin{cases}27,&P(t)Q(t)=0,\\23,&P(t)Q(t)\ne0.\end{cases}
\]
More precisely, the complete canonical vanishing sequence at either fiber is

* \(0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,24\) if \(P(t)Q(t)\ne0\);
* \(0,1,2,3,4,5,6,7,8,9,10,12,14,16,20,22,24\) if \(P(t)=0\);
* \(0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,28\) if \(Q(t)=0\).

The polynomials \(P,Q\) are squarefree and coprime, and none of their zeros lies in \(\{0,1,-1\}\). Thus this one-parameter family has precisely \(12\) distinct admissible parameter values at which the weights in both distinguished fibers jump from \(23\) to \(27\). This is a count of parameter values, not a claim of \(12\) distinct curve-isomorphism classes.

## Assumptions and scope

The ground field is \(\mathbb C\). Parameter \(t\) is arbitrary outside \(\{0,1,-1\}\); no genericity hypothesis on \(t\) is implicit. A canonical vanishing sequence at a point of a genus-\(17\) curve is the increasing list \(a_0<\cdots<a_{16}\) of valuations, in a local trivialization, of a suitably adapted basis of \(H^0(C_t,\omega_{C_t})\). Its weight is \(\sum_{i=0}^{16}(a_i-i)\). The claim concerns precisely the two branch fibers defined by \(X_0=0\) and \(X_1=0\), not the other four branch fibers or the full Weierstrass divisor.

The four coefficients of \(X_0^2\) in the defining quadrics are \(1,-1,t,-t\), which are nonzero and pairwise distinct. Their associated diagonal complete intersection is smooth: in the Jacobian matrix the four individual columns \(X_2,\ldots,X_5\) yield rank four whenever all are nonzero; at most one vanishes away from \(X_0X_1=0\), and the remaining \(X_0\) or \(X_1\) column completes the rank. At \(X_0X_1=0\) all \(X_2,\ldots,X_5\) are nonzero. Adjunction gives \(\omega_{C_t}\cong\mathcal O_{C_t}(2)\), hence genus \(17\), since \(\deg C_t=16\). Each fiber has \(16\) points by independent sign choices modulo common sign.

## Proof

**1. A basis for the canonical series.** Since \(\omega_{C_t}=\mathcal O_{C_t}(2)\), degree-two coordinate monomials span the \(17\)-dimensional canonical space. The four defining equations eliminate \(X_2^2,X_3^2,X_4^2,X_5^2\). A basis is \(X_0^2,X_1^2\) together with \(X_iX_j\) for \(0\le i<j\le5\). The latter number \(15\), so this is indeed a basis.

**2. Reduction to formal jet matrices.** At \(p\in R_0\), take \(X_1=1\), local parameter \(w=X_0/X_1\), and \(z=w^2\). The four nonzero coordinate square roots can be normalized by their constant terms to
\[
f_a(z)=\sqrt{1+az},\quad a\in\{1,-1,t,-t\}.
\]
Additionally set \(f_0(z)=1\). A nonvanishing local trivialization of \(\mathcal O(2)\) reduces the canonical basis to the five sections \(w f_a(z)\) for \(a\in\{0,1,-1,t,-t\}\) and the twelve sections \(1,z,f_af_b\) for \(a<b\) in this five-element set. The functions \(f_a\) have Taylor coefficients \([z^j]f_a=\binom{1/2}{j}a^j\); because the five slopes are distinct, the five sections \(w f_a(z)\) have an adapted valuation sequence \(1,3,5,7,9\) (a Vandermonde determinant).

**3. An involutive decomposition of the even-in-\(w\) sections.** Write \(A_{\pm}=\sqrt{1\pm z}\) and \(B_{\pm}=\sqrt{1\pm tz}\). The even-in-\(w\) part splits under \(z\mapsto-z\) into a seven-dimensional space of even functions of \(z\), with basis
\[
1,\ A_++A_-,\ B_++B_-,\ A_+A_-,\ B_+B_-,\ A_+B_++A_-B_-,\ A_+B_-+A_-B_+,
\]
and a five-dimensional space of odd functions of \(z\), with basis
\[
z,\ A_+-A_-,\ B_+-B_-,\ A_+B_+-A_-B_-,\ A_+B_--A_-B_+.
\]
These are merely invertible linear combinations of the original twelve sections. Denote the coefficient determinant of the seven even basis functions at \(z\)-degrees \(j_1,\ldots,j_7\) by \(D_E(j_1,\ldots,j_7)\), and similarly the five odd basis functions by \(D_O(j_1,\ldots,j_5)\).

**4. Exact determinant identities and exhaustion of possible jumps.** Taylor expansion with \(\binom{1/2}{j}\) gives the following four polynomial identities (the standalone script `VERIFY.py` recomputes them using exact rational arithmetic):
\[
D_O(1,3,5,7,9)=\frac{t^6(t-1)^4(t+1)^4P(t)}{8589934592},
\]
\[
D_O(1,3,5,7,11)=\frac{3t^6(t-1)^4(t+1)^4(t^2+1)(156t^4-401t^2+156)}{68719476736},
\]
\[
D_E(0,2,4,6,8,10,12)=\frac{t^9(t-1)^8(t+1)^8Q(t)}{9223372036854775808},
\]
\[
D_E(0,2,4,6,8,10,14)=\frac{t^9(t-1)^8(t+1)^8(t^2+1)(3056t^8-9808t^6+21653t^4-9808t^2+3056)}{73786976294838206464}.
\]
Direct Euclidean polynomial gcd computations (also replayed by `VERIFY.py`) show \(\gcd(P,Q)=1\), and \(P\) is coprime to the nontrivial factor of the second odd determinant, while \(Q\) is coprime to the nontrivial factor of the fourth determinant. The factors \(t\) and \(t\pm1\) never vanish in the scope. Accordingly, the odd-in-\(z\) five-section valuations in \(z\) are \(1,3,5,7,9\), except at \(P(t)=0\), where the final valuation is \(11\). The even-in-\(z\) seven-section valuations are \(0,2,4,6,8,10,12\), except at \(Q(t)=0\), where the final valuation is \(14\). In each case the nonvanishing replacement determinant proves the first six or four jet rows have maximal rank and prevents a larger jump. No simultaneous jump is possible because \(P,Q\) are coprime.

**5. Conversion to canonical weights and the other fiber.** A function with \(z\)-order \(j\) has \(w\)-order \(2j\). Interlacing these orders with the five odd-in-\(w\) valuations \(1,3,5,7,9\) yields the three asserted canonical vanishing sequences. Their weights, computed by subtracting \(0+\cdots+16=136\), are respectively \(23,27,27\). At \(p\in R_1\), normalize \(X_0=1\), take \(w=X_1/X_0\), and obtain the same square-root analysis with slope set \(\{0,\pm1,\pm 1/t\}\) up to nonzero scalar rescaling. The equations \(t^4P(1/t)=P(t)\) and \(t^8Q(1/t)=Q(t)\) give identical vanishing sequences. The permutation of signs of nonzero homogeneous coordinates acts transitively on each of \(R_0,R_1\), so the calculation applies to all \(32\) points.

Finally, \(\gcd(P,P')=\gcd(Q,Q')=1\), \(\gcd(P,Q)=1\), and \(P(0)P(1)P(-1)Q(0)Q(1)Q(-1)\ne0\). Thus \(P\) and \(Q\) contribute four and eight distinct admissible values respectively.

## Verification

Run `python VERIFY.py` with SymPy version 1.12 or later. The script reconstructs formal square-root coefficients, calculates all four determinants from the claimed bases, proves their symbolic identities by exact simplification, checks polynomial gcds, squarefreeness, admissibility and reciprocity, and checks the stated weight sums. The included `VERIFY_OUTPUT.txt` records `ALL_CHECKS_PASSED`. No floating-point sampling is used. The symbolic identities are finite exact certificates of the critical steps in the algebraic argument; neither a bounded numerical experiment nor a claimed independent formal certification.

## Relationship to prior work

Hidalgo and Leyton-Álvarez (first public preprint 2014, updated 2018) prove a general lower bound for weights at fixed/hyperosculating points on generalized Fermat curves and prove equality on a dense open subset of the full moduli space. Their general lower bound specializes to \(21\) in type \((2,5)\). That theorem does not assert the weights \(23\) and \(27\) or the exact two-polynomial jump locus on the present extra-symmetric one-parameter family. Castorena and Frías-Medina investigate the same genus-\(17\) Humbert–Edge objects via Kummer surfaces and theta characteristics but do not provide this canonical jet stratification. Karagiannis computes general canonical algebra and representation structures, without determining this locus. The present statement concerns new closed jet determinants and the resulting Weierstrass-weight jump stratification, not the pre-existing construction of the curves, their genus, or the general lower-bound theorem.

## Limitations

This result only concerns the \(32\) points over the two distinguished quotient branch values. It does not classify weights over the other four branch values or all Weierstrass points. The parameter count does not count isomorphism classes. Novelty is provisional against potentially unlocated specialized Humbert–Edge and Weierstrass literature; full priority verification by an independent expert remains outstanding. The exact arithmetic script validates the displayed determinant and polynomial identities, not an independently formalized proof of every geometric statement.

## References

1. R. A. Hidalgo and M. Leyton-Álvarez, *The hyperosculating points of the generalized Fermat curves*, arXiv:1409.6258v1 (public 2014-09-22), https://arxiv.org/abs/1409.6258.
2. R. A. Hidalgo and M. Leyton-Álvarez, *Weierstrass weight of the hyperosculating points of generalized Fermat curves*, arXiv:1809.05428 (2018), https://arxiv.org/abs/1809.05428.
3. A. Castorena and J. B. Frías-Medina, *Geometric aspects on Humbert-Edge curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, Glasgow Math. J. 65 (2023), 612–624, https://doi.org/10.1017/S0017089523000174.
4. K. Karagiannis, *Representations on canonical models of generalized Fermat curves and their syzygies*, Quart. J. Math. 76 (2025), 95–107, https://doi.org/10.1093/qmath/haae064; first online 2024-12-23.
