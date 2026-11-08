# Exact 23-adic value spectrum and Haar measure of Perrin numbers

## Finding
Let \(R_0=3\), \(R_1=0\), \(R_2=2\), and \(R_{n+3}=R_{n+1}+R_n\) for every integer \(n\geq0\). Define \(I_k=\{R_n\bmod 23^k:n\geq0\}\), and let \(S_m\) be the number of square residues modulo \(23^m\), with \(S_0=1\), \(S_1=12\), and, for \(m\geq2\),
\[
 S_m=11\cdot23^{m-1}+S_{m-2}.
\]
Then the **exact cardinalities for every positive exponent** are
\[
 |I_1|=15,\qquad |I_2|=211,\qquad
 |I_k|=198\cdot23^{k-2}+13S_{k-3}\quad(k\geq3).
\]
In particular \(|I_3|=4567\) and \(|I_4|=104898\). The least period of the scalar Perrin sequence modulo \(23^k\) is \(22\cdot23^{k-1}\) for every \(k\geq1\). The closure \(\mathcal I\) of the nonnegative-index Perrin values in \(\mathbb Z_{23}\) has normalized additive Haar measure
\[
 \mu(\mathcal I)=\frac{9517}{25392}.
\]
More structurally, \(\mathcal I\) is a disjoint union of \(198\) complete residue balls modulo \(23^2\), and \(13\) disjoint critical images, each a translate of \(23^3\) times a unit multiple of the square set in \(\mathbb Z_{23}\).

## Assumptions and scope
The residue ring is \(\mathbb Z/23^k\mathbb Z\) and the sequence is the classical Perrin trace recurrence with indices \(n\geq0\). The modulus prime \(23\) is distinguished by the discriminant \(-23\) of \(T^3-T-1\). A square includes zero. In a full residue ball every possible higher-precision lift occurs. A critical image has only the indicated square-pattern lifts. No assertion is made about other primes.

## Proof
**1. Trace interpolation.** Put
\[
 A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad
 N=A^{22}-I_3.
\]
The characteristic polynomial is \(T^3-T-1\), so Newton's recurrence gives \(R_n=\operatorname{tr}(A^n)\). Direct integer matrix multiplication gives \(N^2\equiv0\pmod{23}\) and, for \(r=0,1,2\),
\[
 \operatorname{tr}(A^rN)\equiv\operatorname{tr}(A^rN^2)\equiv0\pmod{23},\qquad
 \operatorname{tr}(A^rN^3)\equiv0\pmod{23^2}.
\]
Because traces of \(A^rN^j\), as functions of \(r\), satisfy the Perrin recurrence, these congruences hold for every \(r\geq0\). For integer \(t\geq0\), the exact identity
\[
 R_{r+22t}=R_r+\sum_{j\geq1}\operatorname{tr}(A^rN^j)\binom tj
\]
has finitely many nonzero terms. Since \(N^2\in23M_3(\mathbb Z)\), \(N^j\in23^{\lfloor j/2\rfloor}M_3(\mathbb Z)\). After expressing \(\binom tj\) as a polynomial divided by \(j!\), the coefficient of each term with \(j\geq4\) is divisible by \(23^2\) (use \(\lfloor j/2\rfloor-\nu_{23}(j!)\geq2\)); the \(j=3\) term is also divisible by \(23^2\) by the displayed trace congruence. These coefficients tend to zero \(23\)-adically. Consequently the series extends uniquely to a restricted analytic function \(F_r:\mathbb Z_{23}\to\mathbb Z_{23}\), satisfying
\[
 F_r(t)=R_r+23g_r(t),\qquad
 g_r(t)\equiv u_rt^2+v_rt\pmod{23},
\]
where \(g_r\in\mathbb Z_{23}\langle t\rangle\), and \(u_r,v_r\in\mathbb F_{23}\) are obtained from three integer samples \(R_r,R_{r+22},R_{r+44}\). The \(22\) resulting leading coefficients \(u_r\) are all nonzero; this is certified explicitly in the accompanying finite table and verifier.

**2. Each branch is a quadratic image.** The derivative \(g'_r(t)\equiv2u_rt+v_r\pmod{23}\) has one simple zero. Hensel's lemma applied to the restricted analytic derivative produces a unique critical point \(c_r\in\mathbb Z_{23}\). Taylor division at this point yields
\[
 g_r(t)-g_r(c_r)=u_r(t-c_r)^2(1+23H_r(t)),\qquad H_r\in\mathbb Z_{23}\langle t\rangle,
\]
where \(u_r\) now denotes any fixed unit lift of the indicated nonzero class. The square root \(w_r(t)=\sqrt{1+23H_r(t)}\in1+23\mathbb Z_{23}\langle t\rangle\) exists. The transformation \(t\mapsto(t-c_r)w_r(t)\) is an isometry and a bijection of \(\mathbb Z_{23}\): for any two inputs its divided difference is a unit congruent to \(1\) modulo \(23\), and the map is a translation modulo \(23\). Hence
\[
 F_r(\mathbb Z_{23})=F_r(c_r)+23u_r(\mathbb Z_{23})^2.
\]
Exactly one of the \(12\) value classes of each branch modulo \(23^2\) is critical. Each of the other \(11\) classes contains a simple input, so the inverse-function form of Hensel's lemma makes all higher lifts of that class attainable.

**3. Complete finite overlap certificate at precision \(23^2\).** For each \(0\leq r<22\), write \(a_r=R_r\bmod529\). Compute \(u_r,v_r\) from
\[
 q_r\equiv \frac{R_{r+44}-2R_{r+22}+R_r}{2}\pmod{529},\qquad
 b_r\equiv R_{r+22}-R_r-q_r\pmod{529},\qquad
 u_r\equiv q_r/23,\quad v_r\equiv b_r/23\pmod{23}.
\]
The divisions are well-defined: both numerators are divisible by \(23\). The branch's residue classes are precisely
\[
 \big\{a_r+23(u_rt^2+v_rt)\bmod529:0\leq t<23\big\}.
\]
Its critical value comes from \(t\equiv-v_r(2u_r)^{-1}\pmod{23}\). The following table groups branches by their common residue modulo \(23\); the last column counts targets modulo \(529\) for which *every* representing branch is critical (each such target is represented by exactly one branch).

| Residue modulo \(23\) | Branch indices \(r\) | Union classes modulo \(529\) | Critical-only classes |
|---|---|---:|---:|
| 0 | 1 | 12 | 1 |
| 1 | 20 | 12 | 1 |
| 2 | 2,4,19 | 22 | 2 |
| 3 | 0,3 | 17 | 0 |
| 4 | 17 | 12 | 1 |
| 5 | 5,6,14 | 20 | 0 |
| 6 | 12 | 12 | 1 |
| 7 | 7 | 12 | 1 |
| 10 | 8 | 12 | 1 |
| 12 | 9 | 12 | 1 |
| 16 | 13 | 12 | 1 |
| 17 | 10 | 12 | 1 |
| 20 | 18 | 12 | 1 |
| 21 | 16 | 12 | 1 |
| 22 | 11,15,21 | 20 | 0 |

The table involves only \(22\) triples modulo \(529\); the accompanying standalone verifier recomputes them from the recurrence and independently checks each set and critical-only multiplicity. It gives \(211\) residue classes at precision \(529\), of which \(198\) have at least one simple representation and \(13\) are critical-only, all in distinct classes.

**4. Exact higher images and Haar measure.** Every simple class gives all \(23^{k-2}\) lifts modulo \(23^k\). A critical-only target is covered by a single quadratic branch, with all its inputs congruent to the critical point modulo \(23\). Its image is a translate of \(23^3u_r(\mathbb Z_{23})^2\), so for \(k\geq3\) it gives precisely \(S_{k-3}\) classes. This proves the stated formula. The square-count recursion follows by dividing the squares into those represented by units (\(11\cdot23^{m-1}\) classes) and those with square roots divisible by \(23\) (\(S_{m-2}\) classes).

The complete residue balls have measure \(198/529\). The square set in \(\mathbb Z_{23}\) has measure \(23/48\), because its unit portion has measure \(11/23\) and its nonunit portion is a scaled copy by \(23^2\). The thirteen critical pieces contribute \(13\cdot23^{-3}\cdot23/48=13/25392\). Thus the total measure is \(198/529+13/25392=9517/25392\).

**5. Least period.** The recurrence modulo \(23\) has least scalar period \(22\), checked directly from its first \(22\) values and the first following triple. From the restricted analytic formula, \(F_r(t)\bmod23^k\) depends only on \(t\bmod23^{k-1}\), giving period \(22\cdot23^{k-1}\). To see minimality, any period is divisible by \(22\). If its quotient by \(22\) has \(23\)-valuation \(h<k-1\), then for an input with \(g_r'(t)\) a unit, the change in \(g_r\) after shifting by that quotient has exact valuation \(h\), contradicting periodicity. For \(h=0\) choose two inputs modulo \(23\): a nonconstant quadratic over \(\mathbb F_{23}\) cannot have a nonzero additive period. Therefore the given period is least.

## Verification
Run `python3 verify_perrin23.py`. It verifies the matrix divisibilities, all \(22\) quadratic seed polynomials, the \(15\) grouped residue classes, the \(198+13\) structural split, and the entire independently generated recurrence periods and image sizes through \(23^4\) (up to \(267674\) consecutive terms). Reported output ends with `VERIFY_OK base_rows=22 base_groups=15 full_lift_classes=198 quadratic_classes=13 prime_power_levels=4`. This is a finite certificate for the finite table and numerical examples, not a substitute for the analytic steps proved above.

## Relationship to prior work
The classical Perrin sequence and its trace representation are well established. OEIS A001608 supplies the recurrence and references, and OEIS A104217 records scalar periods for many moduli, including \(22\) at modulus \(23\). The Perrin primality literature classifies signatures of particular indices, especially at the discriminant prime. None of the inspected complete relevant web texts evaluates the all-prime-power image cardinalities, distinguishes \(198\) unrestricted residue balls from \(13\) ramified square branches, or supplies the resulting Haar measure. Period data alone do not imply this image formula. Historical priority is not independently certified; in particular an exhaustive inspection of the original Adams–Shanks publications was not possible.

## Limitations
The theorem is confined to the single ramified prime \(23\) for the Perrin trace recurrence. It does not classify images for other primes or different third-order recurrence initial conditions. The finite verifier checks levels only through \(23^4\); the unlimited-exponent conclusion uses the restricted-analytic and finite-overlap arguments. No independent mathematical review has been performed.

## References
1. OEIS Foundation, *A001608: Perrin sequence*, https://oeis.org/A001608 (accessed November 2026).
2. Anthony C. Robin, *A104217: Period of Perrin sequence mod n*, OEIS, entry dated 2005-03-14, https://oeis.org/A104217.
3. Dana Jacobsen, *Perrin Primality Tests*, 2016-08-08, https://ntheory.org/primality/perrin.html (includes historical discussion and references to Adams–Shanks 1982).
4. William Adams and Daniel Shanks, *Strong primality tests that are not sufficient*, Mathematics of Computation, 1982 (historical primary source; full text not inspected for this comparison).
