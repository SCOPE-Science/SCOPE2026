# Exact minimal modular periods of the four-part elementary-symmetric partition sum

## Finding: lifting at the primes 2 and 3

Let \(a(n)\) be the sum of \(\sum_{i<j}\lambda_i\lambda_j\) over partitions \(\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\ge1\) of \(n\). A period modulo \(m\) means a positive shift valid at every index \(n\ge0\); write \(T(m)\) for the least such shift. For \(r\ge1\), the exact power-of-two period is
\[
T(2^r)=48\,2^{r-1}.
\]
At three, \(T(3)=54\), but the higher powers satisfy
\[
T(3^r)=4\,3^{r+2}\qquad(r\ge2).
\]
In particular, \(T(18)=\operatorname{lcm}(48,324)=1296\), not the conjectural shift 1246 of Ballantine, Beck and Merca. In fact \(a(1246)\equiv6\pmod{18}\), while \(a(0)=0\).

The contribution is the higher-power lift at 2 and 3, including the additional factor of two that appears at modulus 9, and the resulting correction at modulus 18. The rational generating function and the prime periods 48 and 54 are known. The periods coprime to six are also known; together with the formulas here they give periods for all moduli by the Chinese remainder theorem.

## Assumptions and scope

Exactly four positive parts are required; equal parts are allowed, and each partition is counted once. The coefficients for \(0\le n<4\) are zero. Neither a changed weight nor a changed number of parts is considered.

## Proof

**Generating function and period criterion.** Use the previously obtained generating function \(G(q)=N(q)/D(q)\), where
\[
\begin{aligned}
D(q)&=(q-1)^6(q+1)^4(q^2+1)^3(q^2+q+1)^3,\\
N(q)&=q^4(6+15q+34q^2+57q^3+95q^4+121q^5+146q^6\\
&\qquad+126q^7+106q^8+72q^9+50q^{10}+25q^{11}+11q^{12}).
\end{aligned}
\]
For direct verification, parametrize the parts as \((a+b+c+e+1,b+c+e+1,c+e+1,e+1)\) with \(a,b,c,e\ge0\). The size is \(4+a+2b+3c+4e\), and the weight expands as
\[
ab+2ac+3ae+3a+b^2+4bc+6be+6b+3c^2+9ce+9c+6e^2+12e+6.
\]
Summing each monomial with the moments \(1/(1-x), x/(1-x)^2,x(1+x)/(1-x)^3\), with \(x=q^w\) for weights \(w=1,2,3,4\), gives the displayed fraction.

In \(R=\mathbb Z[q]/(D)\) use the basis \(1,q,\ldots,q^{21}\); \(q\) is a unit since \(D(0)=1\). A shift \(t>0\) is a period modulo \(m\) exactly when \(N(q)(q^t-1)\in mR\): \((1-q^t)G\) is then a polynomial of degree below \(t\), by monic division and \(\deg N<\deg D\), and its coefficients at indices \(\ge t\) are the period differences. The periods, extended to integer shifts, form the stabilizer subgroup of \(N\) under multiplication by powers of \(q\) in \(R/mR\). Thus every period is a multiple of the least one.

**Base checks.** Modulo 2 the reduced denominator is \((q+1)^{12}(q^2+q+1)^2\): the exponent of \(q+1\) in \(D\) is 16 and the common factor with \(N\) is \((q+1)^4(q^2+q+1)\). Its order for \(q\) is \(\operatorname{lcm}(16,6)=48\). Modulo 3 the reduced denominator is \((q-1)^{10}(q+1)^4\), after canceling \((q-1)^2(q^2+1)^3\). Its order for \(q\) is \(\operatorname{lcm}(27,18)=54\). These orders follow because, over \(\mathbb F_p\), raising a prime-to-\(p\) cyclotomic order to its \(p^j\)-multiple gives multiplicity \(p^j\).

The following table records the small integral-basis certificates. An entry in the last column is a coefficient of \(N(q)(q^t-1)\) reduced modulo \(pm\), after checking every coefficient is divisible by \(m\).

| \(p\) | \(t\) | \(m\) | \(q^t-1\in mR\) needed for lift | Witness coefficient modulo \(pm\) |
|---|---:|---:|---|---|
| 2 | 48 | 2 | not needed | degree 1: 2 |
| 2 | 96 | 4 | yes | degree 1: 4 |
| 3 | 108 | 3 | yes | degree 0: 3 |

For a short replay of the table, write \(D(q)=q^{22}+\sum_{i=0}^{21}d_iq^i\). Starting with the basis vector of \(1\) or \(N\), iterate \(v'_i=v_{i-1}-d_i v_{21}\), with \(v_{-1}=0\), modulo \(pm\) for \(t\) steps and subtract the starting vector. These are exactly the remainders of \(q^t-1\) and \(N(q)(q^t-1)\); check the former modulo \(m\) where needed. This verifies the finite certificates without factoring large polynomials.

**Lifting from 4 or 3.** If \(q^t=1+p^e C\) in \(R\), where \(e\ge2\) for \(p=2\) or \(e\ge1\) for \(p=3\), the binomial theorem gives
\[
(q^{t p^s}-1)/p^{e+s}\equiv C\pmod{pR}\qquad(s\ge0).
\]
Indeed in each squaring or cubing the higher binomial terms are divisible by at least one further power of \(p\) after the division. An additional positive exponent factor \(u\) prime to \(p\) multiplies the reduced class by \(u\). Thus when \(NC\notin pR\), multiplication by \(N\) has exact divisibility \(p^{e+s}\) for shifts \(t p^s u\).

For \(p=2\), the table shows that 96 is a period modulo 4 and 48 is not. Since every period is divisible by 48, the least period modulo 4 is 96. Apply the lift with \((t,e)=(96,2)\) and its degree-one witness. For \(r\ge2\), any period must be a multiple of 96, and the lift shows its multiplier must be divisible by \(2^{r-2}\), which also suffices. This gives the asserted formula including the base modulus 2.

For \(p=3\), a period at a higher power is a multiple of 54. If it is not a multiple of 4, then \(t\equiv2\pmod4\) and, since \(N\equiv-12\pmod{q^2+1}\), one has \(N(q)(q^t-1)\equiv24\pmod{q^2+1}\). The remainder does not vanish modulo 9. The quotient by \(q^2+1\) is available in \(R\) because that polynomial divides \(D\); this rules out every multiple of 54 not divisible by 108. Now apply the lift with \((t,e)=(108,1)\) and the constant-coefficient witness. The multiplier of 108 must be divisible by \(3^{r-1}\), which also suffices. This proves the separate ternary branch.

**Composite consequence.** The CRT makes \(T(18)=\operatorname{lcm}(T(2),T(9))\). The coefficient recurrence \(a(n)=N_n-\sum_{j=1}^{\min(n,22)}d_ja(n-j)\), with \(N_n=[q^n]N\), gives \(a(1246)\equiv6\pmod{18}\). Pure periodicity makes this an obstruction also to an eventual period of length 1246, by translating the two indices by sufficiently large multiples of 1296. For general \(m\), the CRT combines the formulas here with the known coprime-to-six formula: for the coprime-to-six factor \(b>1\) the least period is \(12b\) if \(5\nmid b\) and \(60b\) otherwise; a factor of modulus 1 contributes period 1.

## Verification and prior work

The included `artifacts/verify_periods.py` verifies the generating-function identity and the modular certificates using exact integer arithmetic. It also compares against direct partition enumeration and checks sample least periods and table witnesses. The argument for all exponents is the binomial lift, not extrapolation from those tests.

- C. Ballantine, G. Beck, M. Merca, *Partitions and elementary symmetric polynomials: an experimental approach*, [arXiv:2408.13346](https://arxiv.org/abs/2408.13346), [journal DOI](https://doi.org/10.1007/s11139-024-01001-6). The introductory table proposes the periods; Theorem 2 proves the shifts 48, 54 and 96 modulo 2, 3 and 4.
- *Exact prime periods of the second-symmetric four-part partition statistic*, [Resultary finding](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-prime-periods-of-the-second-symmetric-four-part-partition--9727064bcc24). Gives the same generating function and the exact prime periods, including 48 and 54.
- *Exact minimal periods of a four-part weighted partition statistic at moduli coprime to six*, [Resultary finding](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-minimal-periods-of-a-four-part-weighted-partition-statisti--30a02e351eb2). Gives the coprime-to-six formula and the same generating function. Neither the generating function nor those periods are claimed as new here.
