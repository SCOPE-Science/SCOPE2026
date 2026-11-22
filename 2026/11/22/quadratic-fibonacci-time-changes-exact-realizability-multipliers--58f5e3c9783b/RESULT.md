# Quadratic Fibonacci time changes: exact realizability multipliers

## Finding

Let \(F_0=0\), \(F_1=1\), \(F_{m+2}=F_{m+1}+F_m\), and let \(a,b,c\) be integers with \(a\ge1\), \(b,c\ge0\). Define \(u_n=F_{an^2+bn+c}\) for \(n\ge1\). A sequence is *realizable* if its terms count the fixed points of successive iterates of one map; it is *almost realizable* if a fixed positive integer multiple is realizable.

**Theorem (sharp trichotomy).** The smallest positive multiplier \(M\), if any, for which \((M u_n)_{n\ge1}\) is realizable is
\[
M_{\min}(a,b,c)=
\begin{cases}
1,&b=0\text{ and }5\mid a,\\
5,&b=0\text{ and }5\nmid a,\\
\text{nonexistent},&b\ge1.
\end{cases}
\]

More precisely, writing \(L_r=F_{r-1}+F_{r+1}\), for every prime \(p\ne5\),
\[
u_p-u_1\equiv
\begin{cases}
0& p\equiv1,4\pmod5,\\
-F_bL_{a+c}&p\equiv2,3\pmod5
\end{cases}\pmod p.
\]
For \(b\ge1\), the nonzero integer \(F_bL_{a+c}\) obstructs the prime-index Dold congruence at all but finitely many primes in the two inert residue classes, for any fixed multiplier. These primes have relative and natural prime densities \(1/2\) among primes by the prime-number theorem for arithmetic progressions.

## Assumptions and scope

All coefficient parameters are **integers**, \(a\ge1\), \(b,c\ge0\), and all sequence indices satisfy \(n\ge1\); Fibonacci numbers use the normalization above. The least multiplier refers to exact realizability, not only the Dold divisibility condition. The result is a complete classification of this natural family of positive-leading-coefficient, nonnegative-coefficient quadratic time changes. It does not claim the same for general polynomials or negative coefficients.

## Proof

**1. Frobenius and the exact prime-index obstruction.** Let
\[
Q=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad Q^2=Q+I,\quad \det Q=-1.
\]
The upper-right entry of \(Q^t\) is \(F_t\) for every nonnegative integer \(t\). For a prime \(p\ne5\), the characteristic polynomial \(X^2-X-1\) has distinct roots over \(\mathbf F_{p^2}\), so Frobenius acts on the pair either trivially, when \(p\equiv1,4\pmod5\), or by transposition, when \(p\equiv2,3\pmod5\). In the first case \(Q^p=Q\pmod p\); in the second, \(Q^p=I-Q=-Q^{-1}\pmod p\). (For \(p=2\) this is verified directly by \(Q^2=I+Q\) modulo two.) In both cases \(Q^{p^2}=Q\pmod p\). Thus
\[
Q^{ap^2+bp+c}\equiv
\begin{cases}
Q^{a+b+c},&p\equiv1,4\pmod5,\\
(-1)^bQ^{a-b+c},&p\equiv2,3\pmod5
\end{cases}\pmod p.
\]
The inverse is integral and exists over every residue ring, so negative exponents in the intermediate matrix identity are legitimate. Applying the Fibonacci–Lucas identity valid for integer indices,
\[
F_{r+s}-(-1)^sF_{r-s}=F_sL_r,
\]
with \(r=a+c\), \(s=b\), proves the stated exact defect.

For \(b\ge1\), \(F_bL_{a+c}\) is a fixed positive integer, since \(a+c\ge1\). Any hypothetical multiplier \(M\ge1\) must satisfy \(p\mid M(u_p-u_1)\) for every prime \(p\). Dirichlet's theorem gives infinitely many primes congruent to either two or three modulo five; only finitely many divide \(MF_bL_{a+c}\). Hence no fixed multiplier is possible for \(b\ge1\).

**2. Full Dold divisibility when \(b=0\).** For an integer sequence \((v_n)\), the Dold conditions \(n\mid\sum_{d\mid n}\mu(n/d)v_d\) follow if, for every prime \(p\), \(k\ge1\), and \(m\ge1\) coprime to \(p\),
\[
v_{mp^k}\equiv v_{mp^{k-1}}\pmod{p^k}.
\]
Indeed, group the terms in the Möbius transform at \(mp^k\) in pairs according to whether the divisor contains \(p^k\) or \(p^{k-1}\), and then use coprimality for each prime-power divisor of the transform index.

For every \(p\ne5\), the eigenvalues of \(Q\) lie in \(\mathbf F_{p^2}^{\times}\), so \(Q^{p^2-1}=I\pmod p\). Matrix binomial lifting gives \(Q^{p^{k-1}(p^2-1)}=I\pmod{p^k}\) for all \(k\ge1\). The two Fibonacci arguments in the prime-power comparison for \(v_n=F_{an^2+c}\) differ by
\[
a m^2p^{2k-2}(p^2-1),
\]
which is divisible by \(p^{k-1}(p^2-1)\); hence the comparison holds without a multiplier at all primes except possibly five.

At \(p=5\), \(Q^5=3I\pmod5\), hence \(Q^{20}=I\pmod5\), and lifting yields \(Q^{20\cdot5^{k-1}}=I\pmod{5^k}\). For \(k\ge2\), the argument difference \(24am^2 5^{2k-2}\) is divisible by \(20\cdot5^{k-1}\), and therefore the unscaled comparison holds. For \(k=1\), that argument difference is divisible by 20 whenever \(5\mid a\). For arbitrary \(a\), multiplication of the sequence by five makes the first-level Dold comparison trivial modulo five. Thus \((F_{an^2+c})\) satisfies all Dold conditions if \(5\mid a\), and \((5F_{an^2+c})\) always satisfies them.

**3. Sharp multiplier at the ramified prime.** Modulo five, the characteristic polynomial of \(Q\) is \((X-3)^2\). Put \(N=Q-3I\). Then \(N^2=0\pmod5\), and for every integer \(t\ge1\),
\[
Q^t=3^tI+t3^{t-1}N\pmod5.
\]
Because \(25a+c\equiv a+c\pmod4\),
\[
Q^{25a+c}-Q^{a+c}\equiv24a\,3^{a+c-1}N\pmod5.
\]
Its upper-right entry equals \(-a3^{a+c-1}\pmod5\), which is nonzero when \(5\nmid a\). The prime-index Dold condition at \(n=5\) then forces \(5\mid M\). This shows the multipliers proved sufficient above are the least possible.

**4. Positivity of every orbit count.** Let \(v_n=F_{an^2+c}\). Its Möbius transform \(B_n=\sum_{d\mid n}\mu(n/d)v_d\) satisfies \(B_1=v_1>0\), and \(B_2=v_2-v_1>0\), because \(a\ge1\) and Fibonacci numbers are strictly increasing from index two onward. For every \(n\ge3\), every proper divisor \(d\mid n\) has \(d\le\lfloor n/2\rfloor\). The addition formula \(F_{u+v}\ge F_uF_{v+1}\) for integers \(u\ge1,v\ge0\), together with \(a(n^2-\lfloor n/2\rfloor^2)\ge2n\) and \(F_{2n+1}\ge2^n>n-1\), gives
\[
v_n>(n-1)v_{\lfloor n/2\rfloor}\ge\sum_{\substack{d\mid n\\d<n}}v_d.
\]
Consequently \(B_n>0\) for every \(n\ge1\). When the Dold congruence holds, \(MB_n/n\) is a nonnegative integer and supplies the exact number of disjoint cycles of length \(n\), producing a map with \(Mu_n\) fixed points for every iterate. This establishes realizability in both \(b=0\) cases and concludes the classification.

## Verification

The accompanying `verify.py` independently computes modular Fibonacci numbers by fast doubling, enumerates primes and checks the three-parameter prime-index identity, checks prime-power Dold lift congruences for a range of coefficients and moduli, and verifies positive integral Möbius orbit counts for multiple quadratic parameters. It also checks the exact fifth-prime obstruction and its dependence on divisibility of the leading coefficient. Execute `python3 verify.py`. Finite computations do not replace the prime-power lifting, Dirichlet, and positivity proofs.

## Relationship to prior work

Moss and Ward [1], first publicly available on 26 November 2020, established almost realizability of \(F_{n^{2k}}\) with multiplier five and the negative obstruction for odd powers. Luca and Ward [2] proved a broad monomial-subsequence theorem for linearly recurrent sequences; applying that theorem to shifted or indexed recurrences already provides some sufficiency information for the \(b=0\) branch, so positivity of that branch alone is not claimed to be new. A later study [3] establishes non-almost-realizability for the different family \(F_{(n+h)^{2k}}\) when \(h>0\): its quadratic specialization corresponds to the constrained subfamily \(a=1,b=2h,c=h^2\). It does not contain the full three-parameter characterization, the factorization \(F_bL_{a+c}\), or the sharp unscaled-versus-five threshold for arbitrary leading coefficients. The present synthesis supplies these simultaneously, with exact necessary and sufficient conditions. Searches of associated mathematical records and relevant full texts did not reveal the complete classification; searches are not a proof of bibliographic uniqueness.

## Limitations

The result applies to nonnegative quadratic coefficients with strictly positive leading coefficient and to Fibonacci initial conditions exactly as specified. No conclusion is asserted for negative coefficients, arbitrary Lucas sequences, or higher polynomial degrees. The prime-density assertion uses the classical prime-number theorem in arithmetic progressions; mere infinitude only needs Dirichlet's theorem. The computational checks are finite and no independent mathematical audit has been performed. Equivalent work outside the inspected material may exist.

## References

[1] P. Moss and T. Ward, *Fibonacci along even powers is (almost) realizable*, arXiv:2011.13068v1, first posted 26 November 2020, Theorem 2 and Corollary 3. https://arxiv.org/abs/2011.13068

[2] F. Luca and T. Ward, *On (almost) realizable subsequences of linearly recurrent sequences*, arXiv:2204.02711v1, first posted 6 April 2022; *Journal of Integer Sequences* 26 (2023), Article 23.4.6, Theorems 1 and 3. https://cs.uwaterloo.ca/journals/JIS/VOL26/Ward/ward9.pdf

[3] *Positive translations destroy almost-realizability of even-power Fibonacci samples*, publicly indexed mathematical result (2026), full RESULT.md inspected. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-positive-translations-destroy-almost-realizability-of-even-power--bd4c6c314992
