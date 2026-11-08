# Exact binary-power periods for every \(k\)-step Fibonacci sequence

## Finding
For every integer \(k\ge2\), let \((F_j^{(k)})_{j\ge0}\) be the integer sequence
\[
F_0^{(k)}=\cdots=F_{k-2}^{(k)}=0,\qquad F_{k-1}^{(k)}=1,
\qquad F_{j+k}^{(k)}=\sum_{i=0}^{k-1}F_{j+i}^{(k)}\quad(j\ge0).
\]
For each integer \(r\ge1\), the sequence reduced modulo \(2^r\) is purely periodic, and its **least positive period** is
\[
\boxed{\pi_k(2^r)=(k+1)2^{r-1}}.
\]
This establishes the full binary-prime-power formula stated as Conjecture 1 of OEIS A351889, including all recurrence orders, without an asymptotic assumption.

## Assumptions and scope
Here \(k\) and \(r\) are arbitrary integers satisfying \(k\ge2\) and \(r\ge1\). The initial state is exactly the impulse state with one final entry \(1\), not a generic \(k\)-step recurrence with arbitrary initial data. A period \(t\) means \(F_{j+t}^{(k)}\equiv F_j^{(k)}\pmod{2^r}\) for every \(j\ge0\). The period is the *minimal* such \(t\). No claim is made for general moduli or for arbitrary initial states.

## Proof
**1. Reduction to an order in a polynomial quotient.** Put
\[
P_k(X)=X^k-\sum_{i=0}^{k-1}X^i,\qquad
R=\mathbb Z[X]/(P_k(X)),\qquad x=X\bmod P_k.
\]
As \(P_k\) is monic, \(R\) is free of rank \(k\) over \(\mathbb Z\) with basis \(1,x,\ldots,x^{k-1}\). Define the coefficient map \(\lambda:R\to\mathbb Z\) by taking the coefficient of \(x^{k-1}\) in that basis. The relation \(x^k=\sum_{i=0}^{k-1}x^i\) and the initial values show by induction that
\[
F_j^{(k)}=\lambda(x^j)\qquad(j\ge0).
\]
The matrix \(H=(\lambda(x^{i+j}))_{0\le i,j<k}\) has entries zero when \(i+j<k-1\) and entries one when \(i+j=k-1\). After reversing its columns, \(H\) is triangular with unit diagonal, so \(\det H=\pm1\). Therefore the pairing \((a,b)\mapsto\lambda(ab)\) is nondegenerate **over every** \(\mathbb Z/2^r\mathbb Z\): if \(\lambda(x^j b)\equiv0\pmod{2^r}\) for \(0\le j<k\), then \(b\equiv0\pmod{2^rR}\).

Consequently, for any positive integer \(t\), the first \(k\) congruences \(F_{j+t}^{(k)}\equiv F_j^{(k)}\pmod{2^r}\) are equivalent to \(x^t\equiv1\pmod{2^rR}\). Since the recurrence propagates equality from its first \(k\) entries, this is equivalent to the full period condition. Moreover \(x\) is a unit in \(R\), because
\[
x\left(x^{k-1}-\sum_{i=0}^{k-2}x^i\right)=1.
\]
Thus \(\pi_k(2^r)\) is exactly the multiplicative order of the unit \(x\) in \((R/2^rR)^\times\).

**2. Exact order modulo two.** Multiplication of \(P_k(X)\) by \(X-1\) yields the integer identity
\[
(X-1)P_k(X)=X^{k+1}-2X^k+1.
\]
It follows that \(x^{k+1}\equiv1\pmod{2R}\). This order is not a proper divisor of \(k+1\): for \(1\le t<k\), the nonzero polynomial \(X^t-1\), of degree less than \(k\), cannot vanish in \(\mathbb F_2[X]/(P_k)\). At \(t=k\), the relation instead gives
\[
x^k-1=\sum_{i=1}^{k-1}x^i\not\equiv0\pmod{2R},
\]
where the right-hand polynomial is nonzero of degree less than \(k\) because \(k\ge2\). Hence the order of \(x\bmod2\) is **exactly** \(k+1\).

**3. Exact lifting through the powers of two.** Let \(u=x^k-1\in R\). The identity above gives
\[
A:=x^{k+1}=1+2u.
\]
We have \(u\not\equiv0\pmod{2R}\) by step 2. Also \(u+1=x^k\) is a unit; therefore
\[
v:=u(u+1)=ux^k\not\equiv0\pmod{2R}.
\]
Squaring gives \(A^2=1+4v\). By induction, for every integer \(s\ge1\),
\[
A^{2^s}=1+2^{s+1}v_s,
\qquad v_1=v,\qquad v_{s+1}=v_s+2^s v_s^2,
\qquad v_s\equiv v\not\equiv0\pmod{2R}.
\]
Thus \(A^{2^s}-1\) is divisible by \(2^{s+1}\) **but not** by \(2^{s+2}\) as an element of the free \(\mathbb Z\)-module \(R\). The case \(s=0\) has exact valuation one since \(A-1=2u\) with \(u\bmod2\ne0\). It follows that the order of \(A\) modulo \(2^rR\) is precisely \(2^{r-1}\): for \(r=1\) the order is one; for \(r\ge2\) the positive power \(2^{r-1}\) annihilates it and the previous power \(2^{r-2}\) does not.

**4. Minimality of the claimed period.** Any exponent for which \(x^t\equiv1\pmod{2^rR}\) must, after reduction modulo two, be a multiple of \(k+1\). Write \(t=(k+1)q\). Then \(x^t=A^q\), whose order condition is exactly \(2^{r-1}\mid q\). The least positive such exponent is \((k+1)2^{r-1}\), establishing the displayed formula. \(\square\)

## Verification
The attached executable `check.py` implements two finite checks for each \(2\le k\le30\) and \(1\le r\le8\). First it iterates the length-\(k\) recurrence state modulo \(2^r\), returning the earliest state recurrence, and compares it with \((k+1)2^{r-1}\). Second it independently multiplies and exponentiates polynomials in \((\mathbb Z/2^r\mathbb Z)[X]/(P_k)\), checking that the claimed power equals \(1\), with the preceding power of two excluded when applicable. The console output in `verification_output.txt` records 232 checked parameter pairs. These finite checks are corroboration, not the source of the universal result; steps 1–4 prove it for all parameters.

## Relationship to prior work
OEIS A351889 records the order-\(k\) Pisano-period table and explicitly lists the displayed power-of-two formula as **Conjecture 1** (OEIS record author date: 2022-02-24). Its known special cases for \(k=2,3,4\) cite earlier Fibonacci, Tribonacci and Tetranacci literature. Tongron and Kerdmongkon (2022) prove periodicity for arbitrary \(k\)-step Fibonacci *functions*, and give selected explicit periods only for orders \(2,3,4\) under additional conditions; that does not provide the all-order, all-binary-power minimal-period law here. The similarly titled paper of Taşcı and Özkan Kızılırmak (2018) concerns the order-two weighted recurrence \(G_{n+1}=kG_n+G_{n-1}\), **not** a \(k\)-step recurrence, so its prime-power period formulas cannot directly imply this theorem. Lü and Wang (2006) examine Wall numbers of \(k\)-step recurrences, but only their abstract and bibliographic entry were available for comparison; that source remains a possible overlap risk. The theorem is based on the elementary polynomial identity above and an exact \(2\)-adic lift.

## Limitations
The proof treats only the standard impulse-initialized order-\(k\) sequence and moduli \(2^r\). Some other initial vectors can have strictly smaller periods. It does not prove analogous prime-power formulas for odd primes nor general moduli. Earlier unindexed or unavailable proofs of the exact formula cannot be excluded by literature searching alone; in particular, the full text of Lü and Wang (2006) was unavailable for a decisive comparison. Independent assessment of originality and correctness remains outstanding.

## References
1. Chai Wah Wu, OEIS A351889, *Period of n-step Fibonacci numbers mod k*, author date 2022-02-24; see Formula, Conjecture 1. https://oeis.org/A351889
2. Yanapat Tongron and Supattra Kerdmongkon, *Periods of k-step Fibonacci functions modulo m*, Songklanakarin Journal of Science and Technology 44(2) (2022), 323–331. https://sjst.psu.ac.th/article/2785/PaperPDF/download
3. Dursun Taşcı and Gül Özkan Kızılırmak, *Pisano Periods for the k-Fibonacci and k-Lucas Sequences mod 2^n*, Gazi University Journal of Science 31(1) (2018), 213–220. https://dergipark.org.tr/en/download/article-file/433129
4. Kebo Lü and Jun Wang, *K-step Fibonacci sequence modulo m*, Utilitas Mathematica 71 (2006), 169–177. Abstract available at https://utilitasmathematica.com/index.php/Index/article/view/410
