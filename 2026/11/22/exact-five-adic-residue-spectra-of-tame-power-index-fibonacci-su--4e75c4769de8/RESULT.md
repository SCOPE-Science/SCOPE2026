# Exact five-adic residue spectra of tame power-index Fibonacci subsequences

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Fix an integer exponent \(d\ge1\) with \(5\nmid d\). For \(k\ge1\) let \(f_d(n)=F_{n^d}\pmod{5^k}\), where \(n\ge0\), and put \(s_d=2\) if \(4\mid d\), otherwise \(s_d=4\). Write \(v_5(0)=\infty\).

**Exact image.** A nonzero residue \(y\pmod{5^k}\) occurs if and only if \(v_5(y)=da<k\) for some integer \(a\ge0\), and, when \(4\mid d\), the unit \(y/5^{da}\) is congruent to \(1\) or \(2\pmod5\). If \(4\nmid d\) there is no restriction on that unit. The zero residue always occurs. Consequently the image cardinality is
\[
N_{d,k}=1+s_d\sum_{a=0}^{\lfloor(k-1)/d\rfloor}5^{k-da-1}.
\]

**Exact fibers and least period.** The least period as a function of \(n\) modulo \(5^k\) is \(T_{d,k}=q_d5^k\), where \(q_d=4\) for odd \(d\) and \(q_d=2\) for even \(d\). In the universal interval \(0\le n<4\cdot5^k\), each nonzero represented residue of valuation \(da<k\) occurs exactly \(4\cdot5^{(d-1)a}\) times if \(4\nmid d\), or \(8\cdot5^{(d-1)a}\) times if \(4\mid d\). The residue zero occurs \(4\cdot5^{k-\lceil k/d\rceil}\) times. Counts per least period are obtained by multiplying these frequencies by \(q_d/4\).

**Five-adic closure.** For the normalized Haar probability measure \(\mu\) on \(\mathbb Z_5\), the closure \(I_d=\overline{\{F_{n^d}:n\ge0\}}^{(5)}\) consists of zero and exactly those nonzero \(y\in\mathbb Z_5\) for which \(v_5(y)\) is a multiple of \(d\), with the additional leading-unit restriction \(5^{-v_5(y)}y\equiv1,2\pmod5\) when \(4\mid d\). Its measure is
\[
\mu(I_d)=\frac{s_d/5}{1-5^{-d}}.
\]
In particular, squares of indices give the closure \(\{0\}\cup\{y:v_5(y)\text{ is even}\}\) of measure \(5/6\); for fourth-power indices the leading unit lies in \(\{1,2\}\pmod5\), and the image measure is \(125/312\).

## Assumptions and scope
Only nonnegative integer indices and integer exponents \(d\ge1\) prime to five are considered. All modular valuations of nonzero residues take values in \(\{0,\ldots,k-1\}\). The parameter \(d\) is fixed while \(k\) varies. No assertion is made for exponents divisible by five. The closure is in the ring \(\mathbb Z_5\), not in the real numbers.

## Proof
**1. Fibonacci's unit quotient.** Binet's polynomial identity gives, for every positive integer \(m\),
\[
\frac{F_m}{m}=2^{1-m}\sum_{j\ge0}\frac{5^j(m-1)(m-2)\cdots(m-2j)}{(2j+1)!}.
\]
The product is \(1\) at \(j=0\), and the finite sum terminates when \(2j+1>m\). For \(j\ge1\), \(v_5((2j+1)!)\le j-1\): check \(j=1,2\), and for \(j\ge3\) use the factorial valuation bound \(v_5((2j+1)!)\le(2j+1)/4\le j-1\). Thus every \(j\ge1\) term is in \(5\mathbb Z_5\), and
\[
\frac{F_m}{m}\equiv c_{m\bmod4}\pmod5,\qquad(c_0,c_1,c_2,c_3)=(2,1,3,4).
\]
In particular \(v_5(F_m)=v_5(m)\) for all positive \(m\).

**2. An exact index isometry.** Let \(Q=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\), so \((Q^m)_{12}=F_m\). Direct integer calculation gives
\[
Q^{20}\equiv I+5B\pmod{25},\qquad B=\begin{pmatrix}4&3\\3&1\end{pmatrix},\qquad Q^4B\equiv B\pmod5.
\]
Furthermore \(((Q^rB)_{12})_{r=0}^3\equiv(3,4,2,1)\pmod5\), all units. If \(s,t\ge0\) are distinct and \(s\equiv t\pmod4\), put \(h=v_5(s-t)\). When \(h=0\), the congruence in step 1 gives \(F_s-F_t\equiv c_{s\bmod4}(s-t)\not\equiv0\pmod5\). When \(h\ge1\), write the positive difference as \(s-t=4\cdot5^h u\), with \(5\nmid u\), exchanging \(s,t\) if necessary. Raising \(Q^{20}\) to \(5^{h-1}u\) gives \(Q^{s-t}\equiv I+5^h uB\pmod{5^{h+1}}\), and hence \(F_s-F_t\equiv5^hu(Q^tB)_{12}\not\equiv0\pmod{5^{h+1}}\). Therefore
\[
\boxed{v_5(F_s-F_t)=v_5(s-t)\quad(s\ne t,\ s\equiv t\pmod4).}
\]
This independently proves the isometry behind the arithmetic-progression equidistribution theorem of Erlebach and Vélez.

**3. Tame power lifting.** Fix \(a\ge0\) and a residue \(r\pmod4\). Write \(n=5^a u\) with \(5\nmid u\), requiring \(n\equiv r\pmod4\); by the Chinese remainder theorem, \(u\) can vary through any prescribed unit residue modulo any power of five. If two such indices have units \(u,v\equiv u_0\pmod5\), then their powers have the same residue modulo four. The isometry in step 2 and the factorization \(u^d-v^d=(u-v)\sum_{j=0}^{d-1}u^{d-1-j}v^j\), whose second factor is congruent to \(du_0^{d-1}\not\equiv0\pmod5\), show
\[
v_5\!\left(\frac{F_{(5^a u)^d}-F_{(5^a v)^d}}{5^{da}}\right)=v_5(u-v).
\]
The normalized image function is therefore an isometry on each unit ball \(u_0+5\mathbb Z_5\), and it maps that ball *onto* the complete ball specified by its output modulo five: at every finite depth the isometry injects two finite sets of equal size, so it is surjective. By step 1 this output is \(c_\rho u_0^d\pmod5\), where \(\rho\equiv n^d\pmod4\).

**4. Leading-unit classes and multiplicities.** If \(d\) is odd, the map \(u_0\mapsto u_0^d\) permutes \(\mathbb F_5^\times\), since \(\gcd(d,4)=1\). Each of the four residue classes of \(n\pmod4\) thus contributes one unit root for each chosen output unit class. If \(d\equiv2\pmod4\), even \(n\) gives \(\rho=0\), multiplier \(c_0=2\), whereas odd \(n\) gives \(\rho=1\), multiplier \(c_1=1\). Squares and twice squares partition \(\mathbb F_5^\times\). There are two square roots in the appropriate parity, and two index classes modulo four of that parity, so again four roots. If \(4\mid d\), every unit \(u_0^d\equiv1\pmod5\), hence only the two output unit classes \(1\) and \(2\) occur, each with four roots in each of the two relevant index classes modulo four, giving eight roots. For a nonzero output of valuation \(da<k\), each such root modulo \(5^{k-da}\) has precisely \(5^{(d-1)a}\) lifts to a choice of \(n\pmod{5^k}\); this proves all nonzero multiplicities. The zero fiber consists precisely of indices divisible by \(5^{\lceil k/d\rceil}\), giving its stated size. Summing the allowed leading-unit shells proves the image-count formula.

**5. Minimal periods and closure.** The index shift \(4\cdot5^k\) is a period for every exponent, since the resulting powers are congruent modulo \(4\cdot5^k\). For even \(d\), the shorter shift \(2\cdot5^k\) is a period because it preserves parity and the two powers are congruent both modulo four and modulo \(5^k\), so step 2 applies. Conversely, any positive period \(t\) must satisfy \(5\mid t\), by comparing \(n=0\) with \(n=t\), using the exact valuation of step 1. Comparing \(n=1\) with \(n=1+t\) modulo five shows \(4\mid t\) when \(d\) is odd, and \(2\mid t\) when \(d\) is even: otherwise the leading multiplier \(c_{(1+t)^d\bmod4}\) differs from \(c_1=1\). In these permitted cases the index isometry at \(n=1\) and \(5\nmid d\) imply \(k\le v_5(F_{(1+t)^d}-F_1)=v_5((1+t)^d-1)=v_5(t)\). This proves the exact least period. Finally, the finite image criteria at every depth are compatible and the allowed shells accumulate only at zero, proving the asserted five-adic closure and its geometric-series Haar measure.

## Verification
Run `python3 verify.py`. The standalone checker independently constructs Fibonacci periods by recurrence, evaluates the power-index samples modulo the period, and checks the complete predicted output-frequency table, claimed periods and absence of shorter periods in tested small cases. It additionally checks the exact matrices and residue slopes from proof step 2. Its 70 test scenarios cover exponents not divisible by five through 18 at depths one through four, plus ten selected exponent tests at depth five. Finite checks support but do not replace the infinite proofs above.

## Relationship to prior work
Erlebach and Vélez [1], Theorem 2, prove that every ordinary index progression \(F_{r+4j}\) represents each residue modulo \(5^k\) exactly once. This is the closest and strongest underlying result. It does not specify the image of *power-index restrictions*: an arbitrary bijective isometry need not have an evident power-class image without the leading-unit compatibility and local lifting established here. Medina and Rowland [2] record the classical \(v_5(F_n)=v_5(n)\) formula; this predicts only allowable valuations, not whether every compatible unit is attained. Moss and Ward [3] study dynamical realizability of the *same power-index subsequences*, not their complete five-adic residue spectra. OEIS A054783 [4] records the square-index sequence, not all-depth residue image and fiber laws. The theorem is a direct development of these established tools; it does not claim a new five-adic analytic framework, and an implicit equivalent in earlier work remains possible.

## Limitations
The classification excludes \(5\mid d\), where the local power map is not an isometry and the present unit-lifting argument fails. No assertion about numerical first occurrences, archimedean distributions, or results over other primes is made. The priority comparison remains qualified by possible implicit derivations from classical five-adic Fibonacci equidistribution; computational checks alone cannot settle priority or infinite correctness. The older 1983 publication is cited by year and issue without fabricating a day-specific public-release date.

## References
[1] L. Erlebach and W. Y. Vélez, *Equiprobability in the Fibonacci Sequence*, Fibonacci Quarterly 21(3) (August 1983), 189–191. https://www.fq.math.ca/Scanned/21-3/erlebach.pdf

[2] L. A. Medina and E. Rowland, *\(p\)-regularity of the \(p\)-adic valuation of the Fibonacci sequence*, arXiv:0910.2907v1, first posted 15 October 2009; Theorem 1.2. https://arxiv.org/abs/0910.2907

[3] P. Moss and T. Ward, *Fibonacci along even powers is (almost) realizable*, arXiv:2011.13068v1, first posted 26 November 2020; Theorem 2 and Corollary 3. https://arxiv.org/html/2011.13068v1

[4] OEIS A054783, *\((n^2)\)-th Fibonacci number*. https://oeis.org/A054783
