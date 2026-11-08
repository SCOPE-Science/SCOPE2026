# Uniform odd-characteristic rigidity and two point-free Klein-line complements

## Finding
Let \(R=\mathbb Z[\omega]/(\omega^2+\omega+2)\). The 21 line forms below define the classical Klein reflection-line arrangement over \(R\). For **every** field \(k\) of characteristic different from two with an element \(\omega\in k\) satisfying \(\omega^2+\omega+2=0\), these forms give 21 distinct projective lines and exactly 28 ordinary triple and 21 ordinary quadruple intersection points, all rational over \(k\), with no other intersections. In particular, there are no double points, including in characteristic seven.

If \(k=\mathbb F_q\), let \(D\) be the reduced union of these lines and \(U=\mathbb P^2_k\setminus D\). For every integer \(m\ge1\),

\[
\#U(\mathbb F_{q^m})=q^{2m}-20q^m+99=(q^m-9)(q^m-11),
\]

and

\[
Z(U/k,T)=\frac{(1-qT)^{20}}{(1-T)^{99}(1-q^2T)}.
\]

In particular, \(U(\mathbb F_9)=U(\mathbb F_{11})=\varnothing\), and these are precisely the two finite fields of odd order admitting this model with no rational point in its complement. The fields \(\mathbb F_9\) and \(\mathbb F_{11}\) carry the necessary quadratic root; for example, \(\omega^2+\omega+2=0\) over \(\mathbb F_9\), and \(\omega=4\) or \(6\) over \(\mathbb F_{11}\).

## Assumptions and scope
The result concerns this fixed coefficientwise Klein model in the plane, not every combinatorially equivalent realization. Write homogeneous coordinates as \([x:y:z]\). The 21 line forms are, in published numbering, 

\[
\begin{aligned}
\ell_1&=x,&\ell_2&=y+z,&\ell_3&=\omega x+y-z,\\
\ell_4&=\omega x-y+z,&\ell_5&=-y+z,&\ell_6&=x+\omega y-z,\\
\ell_7&=\omega x-y-z,&\ell_8&=-x+y+\omega z,&\ell_9&=\omega x+y+z,\\
\ell_{10}&=-x+\omega y+z,&\ell_{11}&=-x-y+\omega z,&\ell_{12}&=x+z,\\
\ell_{13}&=-x+\omega y-z,&\ell_{14}&=x+\omega y+z,&\ell_{15}&=-x+z,\\
\ell_{16}&=x-y+\omega z,&\ell_{17}&=x+y+\omega z,&\ell_{18}&=z,\\
\ell_{19}&=-x+y,&\ell_{20}&=x+y,&\ell_{21}&=y.
\end{aligned}
\]

The root need not be a primitive element of the finite field. In characteristic seven the polynomial has a double root, and the theorem still applies. Characteristic two is expressly excluded.

## Proof
1. **Integral determinant certificate.** Represent elements of \(R\) by \(a+b\omega\), with multiplication determined by \(\omega^2=-\omega-2\). The conjugate root is \(-1-\omega\); the integral norm is
\[
N(a+b\omega)=a^2-ab+2b^2.
\]
For each unordered triple of the 21 row vectors of line coefficients, compute the corresponding \(3\times3\) determinant in \(R\). There are exactly \(\binom{21}{3}=1330\) triples. The complete histogram of determinant norms, certified by `klein21_certificate.py`, is
\[
\begin{array}{c|rrrrrrrr}
N&0&1&2&4&8&16&32&64\\\hline
\text{count}&112&169&228&271&320&156&70&4.
\end{array}
\]
The norm is positive definite, so norm zero means determinant zero in \(R\). Every nonzero determinant has norm a power of two; the identity \(d\bar d=N(d)\) therefore makes each such determinant a unit in \(R[1/2]\). Thus **no new triple concurrency can appear in any odd characteristic**.

2. **Exhaustion of the incidence classes.** For each pair of line indices \(i,j\), form the set consisting of \(i,j\) and all \(h\) for which \(\det(\ell_i,\ell_j,\ell_h)=0\). Deduplicating these pair-index sets gives exactly 28 sets of size three and 21 sets of size four. Their pairs exhaust the \(\binom{21}{2}=210\) line pairs, since
\[
28\binom{3}{2}+21\binom{4}{2}=84+126=210.
\]
For every pair there is a third line outside its concurrency class; its nonzero determinant shows the first two lines remain independent after any odd-characteristic specialization. Every two distinct classes stay distinct: coincidence of their intersection points would force an additional vanishing triple determinant, contradicting step 1. Hence the only intersections are the stated 49, with the same multiplicities in every allowed characteristic. Distinct projective lines crossing at a point have distinct tangent directions, so the intersections are ordinary. Their coordinates are rational over \(k\), being intersections of \(k\)-lines.

3. **Rational-point count.** Over \(\mathbb F_{q^m}\), each of the 21 lines contains \(q^m+1\) points. Correcting the multiple counts at the 28 triple and 21 quadruple points gives
\[
\#D(\mathbb F_{q^m})=21(q^m+1)-28(3-1)-21(4-1)=21q^m-98.
\]
Subtracting from \(\#\mathbb P^2(\mathbb F_{q^m})=q^{2m}+q^m+1\) gives the displayed complement formula.

4. **Zeta function and point-free cases.** Apply the definition \(Z(U/k,T)=\exp(\sum_{m\ge1}\#U(\mathbb F_{q^m})T^m/m)\) to the formula in step 3. For \(m=1\), the factorization \((q-9)(q-11)\) vanishes only at \(q=9\) or \(q=11\). Both fields admit the displayed Klein model, and the two point-free conclusions follow. No inference about fields of characteristic two is made.

## Verification
Run the complete executable determinant certificate with `python3 klein21_certificate.py`, and the independent exhaustive projective-plane counts with `python3 klein21_finite.py` from the same directory. The latter explicitly enumerates every projective point for field sizes 7, 9, 11 (both choices of the root), and 23. The field of order nine is represented by \(\mathbb F_3[\omega]/(\omega^2+\omega+2)\). Results and exact outputs are provided in `verification_output.txt`. These finite enumerations are supplementary checks; the determinant and incidence-class certificates prove the arbitrary-characteristic statement, while elementary inclusion-exclusion proves the all-extension arithmetic formulas.

## Relationship to prior work
Bauer and collaborators (2014, 2016) document the classical 21-line configuration with 28 triple and 21 quadruple points; their 2016 positive-characteristic discussion explicitly develops the \(\mathbb F_7\) case and notes the general requirement that the 49 points be distinct. Gévay and Pokora publish the 21 explicit equations used here and the classical 49-point incidence. Innamorati analyzes the distinguished characteristic-seven finite geometry. The finite-field statement established here is specifically the all-odd-characteristic determinant rigidity, together with the complete point-count/zeta formula and the previously unaddressed point-free \(\mathbb F_9\) and \(\mathbb F_{11}\) specializations. No novelty is claimed for the 21 lines, the complex incidence counts, or the characteristic-seven realization.

## Limitations
Historical priority is provisional: specialist finite-geometry sources may contain equivalent statements not found in the inspected primary passages. The calculation establishes ordinary reduced line crossings; it does not assert that the entire reflection-group representation has the same properties in modular characteristics. The result is for fields admitting a root of the stated quadratic and excludes characteristic two. The source-code certificate exhausts 1330 triples and 210 pairs; the mathematical reduction to this finite list and the subsequent all-extension formulas are given above.

## References
- T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Lundman, P. Pokora, T. Szemberg, *Bounded Negativity and Arrangements of Lines*, arXiv:1407.2966, first posted 2014-07-10. Section 4.1.
- T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu, T. Szemberg, *Negative Curves on Symmetric Blowups of the Projective Plane, Resurgences and Waldschmidt Constants*, arXiv:1609.08648, first posted 2016-09-27. Section 9.
- G. Gévay and P. Pokora, *Klein's Arrangements of Lines and Conics*, arXiv:2211.15309, first posted 2022-11-28. Section 2.1, explicit line equations and classical intersection list.
- S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, 2024. Section 4, characteristic-seven Klein configuration.
