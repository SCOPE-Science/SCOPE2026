# An exact three-square obstruction law for even-trace Lucas recurrences

## Finding

For positive integers \(P,B\), with \(P\) even and \(B\) odd, define
\[
U_0=0,\quad U_1=1,\quad U_{n+2}=P U_{n+1}+B U_n\quad(n\geq0).
\]
Put \(t=\nu_2(P)\geq1\) and \(a=P/2^t\), so \(a\) is odd. Every positive index has a unique expression \(n=2^s u\), where \(s\geq0\) and \(u\) is positive and odd. All inverse residues below are taken among the odd units modulo eight.

**Theorem.** The positive integer \(U_n\) is **not** representable as the sum of three integer squares precisely in the following disjoint cases.

* **Odd indices, \(s=0\).** If \(t=1\), the obstruction is \((B\equiv3\pmod8,\ n\equiv3\pmod8)\) or \((B\equiv7\pmod8,\ n\equiv7\pmod8)\). If \(t\geq2\), the obstruction is \(B\equiv7\pmod8\) and \(n\equiv3\pmod4\).
* **Even indices, \(s\geq1\).** The obstruction is exactly
\[
 t+s-1\equiv0\pmod2,\qquad u\equiv7(ac_s)^{-1}\pmod8,
\]
where
\[
 c_s\equiv
 \begin{cases}
 1\pmod8,&s=1,\\
 B+2\pmod8,&s\geq2\text{ and }t=1,\\
 B\pmod8,&s\geq2\text{ and }t\geq2.
 \end{cases}
\]

In particular, the natural density \(\delta(P,B)\) of obstructed positive indices exists, and the number of such indices at most \(N\) is \(\delta(P,B)N+O(\log(N+2))\), with an absolute implied constant. The **complete density phase diagram** is

| Parameter condition | \(\delta(P,B)\) |
|---|---|
| \(t=1\), \(B\equiv3,7\pmod8\) | \(1/6\) |
| \(t=1\), \(B\equiv1,5\pmod8\) | \(1/24\) |
| \(t\geq2\) even, \(B\equiv7\pmod8\) | \(1/3\) |
| \(t\geq2\) even, \(B\not\equiv7\pmod8\) | \(1/12\) |
| \(t\geq3\) odd, \(B\equiv7\pmod8\) | \(7/24\) |
| \(t\geq3\) odd, \(B\not\equiv7\pmod8\) | \(1/24\) |

The case \(P=2,B=1\) specializes to the previously established Pell obstruction \(n=4^{j+1}(8l+5)\), for \(j,l\geq0\); the formula above covers the entire positive two-parameter even/odd family.

## Assumptions and scope

Both recurrence parameters are positive integers, with \(2\mid P\) and \(2\nmid B\). The theorem covers all positive indices without an exceptional small-index range. Because the coefficients and initial values are nonnegative and \(P,B>0\), every \(U_n\) for \(n\geq1\) is positive. No claim is made for odd \(P\), even \(B\), or other quadratic forms. Here *three squares* allows zero and repeated integer squares.

## Proof

**1. Odd indices.** The standard integer polynomial expansion of the recurrence is
\[
 U_n=\sum_{j=0}^{\lfloor(n-1)/2\rfloor}
 {n-1-j\choose j}P^{n-1-2j}B^j.
\]
For \(n=2m+1\) the constant term in \(P\) is \(B^m\), and the coefficient of \(P^2\) is \({m+1\choose2}B^{m-1}\) when \(m\geq1\). Every higher term is divisible by \(P^4\), hence by sixteen. When \(t\geq2\), \(P^2\equiv0\pmod8\), giving \(U_{2m+1}\equiv B^m\pmod8\). Since any odd square is congruent to one modulo eight, \(B^{2j}\equiv1\) and \(B^{2j+1}\equiv B\pmod8\). Thus the only value seven occurs when \(B\equiv7\pmod8\) and \(m\) is odd, equivalently \(n\equiv3\pmod4\).

When \(t=1\), \(P^2\equiv4\pmod8\). Writing \(m=0,1,2,3\pmod4\), the respective residues of \(U_{2m+1}\) modulo eight are \(1,B+4,5,B\). This follows since \({m+1\choose2}\) is odd precisely for \(m\equiv1,2\pmod4\). The only residue seven occurs in the two specified odd-index cases. This also proves that every odd-index term has \(\nu_2(U_n)=0\).

**2. Doubling and exact even-index valuations.** Define the companion sequence \(V_0=2\), \(V_1=P\), \(V_{j+2}=PV_{j+1}+BV_j\). The characteristic roots \(\alpha,\beta\) obey \(\alpha\beta=-B\), and the standard Binet identities give
\[
 U_{2m}=U_mV_m,\qquad V_{2m}=V_m^2-2(-B)^m.
\]
In particular \(V_2=P^2+2B\), and
\[
 V_4=P^4+4P^2B+2B^2\equiv2\pmod{16},
\]
since \(P\) is even and the square of an odd integer is \(1\) or \(9\) modulo sixteen. For every \(j\geq2\), induction using the second doubling identity, together with \(B^{2^j}\equiv1\pmod{16}\), proves \(V_{2^j}\equiv2\pmod{16}\). As \(V_2\equiv2\pmod4\), it follows that
\[
 U_{2^s}=P\prod_{j=1}^{s-1}V_{2^j},\qquad
 \nu_2(U_{2^s})=t+s-1\quad(s\geq1).
\]
Dividing by this exact power of two and reducing modulo eight yields
\[
 \frac{U_{2^s}}{2^{t+s-1}}\equiv a c_s\pmod8,
\]
with the three cases for \(c_s\) in the statement. Indeed, the first factor \(V_2/2=P^2/2+B\) is congruent to \(B+2\) if \(t=1\), and to \(B\) if \(t\geq2\); every later \(V_{2^j}/2\) is one modulo eight.

**3. Odd-multiplier rigidity.** For any positive integer \(k\) and odd \(u\), the quotient \(U_{ku}/U_k\) is an integer, equal to the index-\(u\) Lucas polynomial of parameters \((V_k,(-B)^k)\). For \(k=2^s\) with \(s\geq1\), the second parameter is \(B^{2^s}\equiv1\pmod8\), while the first is \(V_{2^s}\equiv2\) or \(-2\pmod8\) (and is \(2\pmod8\) for \(s\geq2\)). The polynomial recurrence \(W_0=0\), \(W_1=1\), \(W_{j+2}=TW_{j+1}-W_j\) has \(W_u(2)=u\) and \(W_u(-2)=(-1)^{u-1}u=u\) for odd \(u\). Hence
\[
 \frac{U_{2^s u}}{U_{2^s}}\equiv u\pmod8.
\]
The quotient is odd, so this proves both the valuation and odd-unit congruence
\[
 \nu_2(U_{2^s u})=t+s-1,\qquad
 \frac{U_{2^s u}}{2^{t+s-1}}\equiv a c_s u\pmod8.
\]

**4. Legendre's criterion.** A positive integer is not a sum of three squares exactly when its two-adic valuation is even and the remaining odd part is seven modulo eight. Applying this criterion to the odd-index and even-index formulas proves the stated complete disjoint classification.

**5. Exact densities and error.** At each fixed \(s\geq1\) with \(t+s-1\) even, the even-index condition selects exactly one arithmetic progression modulo \(2^{s+3}\), of density \(2^{-s-3}\). If \(t\) is even, the permitted exponents are \(s=1,3,5,\ldots\), whose densities sum to \(1/12\). If \(t\) is odd, the permitted exponents are \(s=2,4,6,\ldots\), giving \(1/24\). The odd-index part adds density \(1/8\) in the specified cases when \(t=1\), density \(1/4\) in the specified cases when \(t\geq2\), and otherwise zero. This gives exactly the six displayed parameter cases and five distinct density values. In counting indices at most \(N\), each nonempty progression contributes its exact expected count with error at most one; only \(O(\log(N+2))\) exponents occur. This proves the uniform counting error and completes the proof.

## Verification

The accompanying standalone `check.py` compares the stated criterion against the definition of forbidden numbers (even two-adic valuation and odd part seven modulo eight) computed by a direct recurrence. Its independent exact-integer loop tests 22,680 parameter-index pairs. A second, fixed-width modular recurrence tests 1,664,000 pairs for even \(P\leq128\), odd \(B\leq129\), and \(1\leq n\leq400\). In this range no computed term has two-adic valuation as high as the modulus exponent twenty-four. Both methods passed; five independent dyadic-prefix censuses at height \(2^{14}\) agree with the five density regimes to within the proved logarithmic counting error, and rational arithmetic verifies that all five density values arise. Reproduce with `python check.py`. These finite computations corroborate the proof but cannot establish the unbounded index result.

## Relationship to prior work

Sobolewski, first publicly circulated on 20 February 2022, proves a general structural description (Theorem 5.4) of three-square obstructions for nondegenerate first-kind Lucas sequences with odd recurrence coefficient, and works out the classical Pell case \((P,B)=(2,1)\) explicitly (Example 5.1). The present result does not claim the general structural theorem or its Pell instance: it derives explicit residues, a sharp parameter-dependent complete classification, and exact natural densities for **every** positive even \(P\) and positive odd \(B\). Latushkin and Ushakov (2012) classify the classical Fibonacci and Lucas numbers, rather than this two-parameter family. The proof uses familiar Lucas identities and Legendre's theorem, but resolves the uniform residue behavior of the whole family. It is possible that equivalent identities or classifications occur in other references; novelty beyond the inspected sources has not been independently certified.

## Limitations

The criterion addresses existence, not the number of representations as three squares. It requires positive even \(P\) and positive odd \(B\). The error term is logarithmic and not claimed optimal for each fixed pair. The independent validation status remains unperformed. The priority comparison includes the complete accessible Sobolewski article and directly relevant older work, but does not exclude unindexed or inaccessible equivalent statements.

## References

1. B. Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits*, arXiv:2202.09922, first version 20 February 2022; *The Ramanujan Journal* 61 (2023), 1151–1195, DOI: 10.1007/s11139-023-00710-8. Theorem 5.4 and Example 5.1.
2. Ya. A. Latushkin and V. N. Ushakov, *On the Representation of Fibonacci and Lucas Numbers as the Sum of Three Squares*, *Mathematical Notes* 91 (2012), 663–670, DOI: 10.1134/S0001434612050070.
3. Legendre's three-square theorem (classical criterion for \(4^a(8b+7)\)).
