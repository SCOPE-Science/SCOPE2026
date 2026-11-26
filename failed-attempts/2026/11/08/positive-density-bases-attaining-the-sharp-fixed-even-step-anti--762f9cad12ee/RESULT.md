# Positive-density bases attaining the sharp fixed-even-step anti-Niven bound

## Finding
For any base \(b\ge2\), write \(s_b(n)\) for the sum of the ordinary base-\(b\) digits of the positive integer \(n\). Call \(n\) **\(b\)-anti-Niven** when \(\gcd(n,s_b(n))=1\). A length-\(\ell\) progression with difference \(d\) means \(N,N+d,\ldots,N+(\ell-1)d\), with \(N,d\) positive integers.

**Theorem.** Fix an even integer \(d\ge4\) and an odd prime \(p\ge5\) for which \(p\nmid d\). Define
\[
H=\prod_{r=1}^{p-1}(p+rd),\qquad C=p+(p-1)d+2.
\]
Let \(b>C\) be an **odd** integer with these three properties:

1. \(p\mid b-1\).
2. For every prime \(q<p\) with \(q\nmid d\), we have \(q\nmid b-1\).
3. \(\gcd(b-1,H)=1\).

Then the maximum possible length of a \(b\)-anti-Niven progression having common difference **exactly** \(d\) is \(p-1\). Furthermore infinitely many distinct starting integers \(N\) attain this length.

More precisely, set \(R=b-C\), and for \(0\le j\le p-2\) define
\[
h_j=p+(p-1-j)d,\qquad s_j=b-1-h_j.
\]
Let \(\mathcal P\) consist of all prime factors of \(\prod_{j=0}^{p-2}s_j\) that do not divide \(b\). Put
\[
L=\mathop{\mathrm{lcm}}_{q\in\mathcal P}(q-1),
\]
with \(L=1\) if \(\mathcal P\) is empty. For **each** integer \(t\ge1\), the explicit start
\[
N_t=b^{1+tL}+R
\]
has the required property:
\[
\gcd\bigl(N_t+jd,s_b(N_t+jd)\bigr)=1\qquad(0\le j\le p-2).
\]

**Positive-density corollary.** Let \(\mathcal Q\) be the set consisting of all odd primes below \(p\) and all prime factors of \(H\), and put \(Q=\prod_{q\in\mathcal Q}q\). There is a unique residue class \(B\pmod{2pQ}\) satisfying
\[
B\equiv1\pmod{2p},\qquad B\equiv2\pmod Q.
\]
Every positive base \(b\equiv B\pmod{2pQ}\) above \(C\) satisfies the theorem; the set of these bases has natural density \(1/(2pQ)\). In addition, every sufficiently large base of the form \(b=2^u p^a+1\), with \(u,a\ge1\), satisfies the theorem.

For example, choose \(d=4\), \(p=5\), \(b=41\). The four terms
\[
41^{991}+18,\quad 41^{991}+22,\quad41^{991}+26,\quad41^{991}+30
\]
have digit sums \(19,23,27,31\), respectively, and each term is coprime to its own digit sum. No length-five progression with step \(4\) in base \(41\) can have this property.

## Assumptions and scope
All numbers and products in the theorem are ordinary integers. The quantifiers are: for **every** even \(d\ge4\) and **every** odd prime \(p\ge5\) coprime to \(d\), the conclusion holds for **all** odd bases \(b\) satisfying the displayed explicit hypotheses. The density is a natural density among **all** positive integer bases, not a claim about density of good starting integers within a fixed base. The assertion of infinitude concerns distinct \(N_t\) for a fixed admissible \((b,d,p)\). No bound independent of \(b,d,p\) is asserted for the smallest starting integer.

## Proof
**Step 1: digit-sum profile.** Since \(b>C\), the integer \(R=b-C\) is positive. For \(0\le j\le p-2\), the integer \(R+jd\) satisfies \(0<R+jd<b\): indeed its maximum is \(b-p-d-2\). Thus its base-\(b\) representation consists of a single low digit. Because \(1+tL\ge2\), the number \(N_t+jd=b^{1+tL}+R+jd\) consists of two nonoverlapping nonzero digits, and hence
\[
\begin{aligned}
s_b(N_t+jd)&=1+R+jd\\
&=1+b-C+jd\\
&=b-1-\bigl[p+(p-1-j)d\bigr]\\
&=s_j.
\end{aligned}
\]
The inequalities on \(R+jd\) also show \(1\le s_j<b\). In fact the chosen excess in \(C\) gives \(s_j\ge2\).

**Step 2: simultaneously avoid the digit-sum prime factors.** Fix \(j\), and let \(q\) be any prime divisor of \(s_j\). If \(q\mid b\), then \(b^{1+tL}\equiv b\equiv0\pmod q\). If \(q\nmid b\), then \(q\in\mathcal P\), so \(q-1\mid L\), and Fermat's little theorem gives
\[
b^{1+tL}\equiv b\pmod q.
\]
In either case,
\[
N_t+jd=b^{1+tL}+R+jd
\equiv b+(s_j-1)\equiv b-1\pmod q.
\]
Were \(q\) to divide both \(N_t+jd\) and \(s_j\), it would divide \(b-1\) and thus, from \(s_j=(b-1)-h_j\), would divide \(h_j\). This contradicts \(\gcd(b-1,H)=1\), because every \(h_j\) is among the factors of \(H\). Therefore no prime can divide both numbers, proving \(\gcd(N_t+jd,s_j)=1\) for each \(j\). The starts \(N_t\) strictly increase with \(t\), so there are infinitely many.

**Step 3: sharp upper bound.** Since \(p\mid b-1\), the positional expansion identity gives \(s_b(n)\equiv n\pmod p\) for every positive integer \(n\). Because \(p\nmid d\), any \(p\) consecutive terms \(N,N+d,\ldots,N+(p-1)d\) contain exactly one multiple of \(p\). Its digit sum is also divisible by \(p\), so it cannot be anti-Niven. Consequently no anti-Niven progression with step \(d\) has length \(p\) or greater. Step 2 constructs length \(p-1\), establishing the exact maximum. The no-smaller-prime condition ensures that \(p\) is the first available obstruction of this type; it is not used separately in the construction.

**Step 4: a positive-density set of admissible bases.** Each factor \(p+rd\) of \(H\) is odd since \(p\) is odd and \(d\) is even, and is not divisible by \(p\) since \(1\le r\le p-1\) and \(p\nmid d\). Consequently \(\gcd(Q,2p)=1\). The Chinese remainder theorem gives the unique class \(B\) in the statement. Every base in it is odd, has \(p\mid b-1\), and has \(q\nmid b-1\) for each odd \(q<p\) or each prime factor \(q\) of \(H\). The prime \(2\) divides \(d\) and cannot violate the no-smaller-prime condition; also \(H\) is odd. Thus all three hypotheses hold. A fixed residue class modulo \(2pQ\) has natural density \(1/(2pQ)\), and deleting finitely many bases \(b\le C\) does not change that density. Finally, if \(b-1=2^u p^a\), then no prime below \(p\) failing to divide \(d\) divides \(b-1\), and \(\gcd(b-1,H)=1\), since \(H\) is odd and prime to \(p\). This proves the explicit prime-power subfamily.

**Step 5: explicit example.** For \((b,d,p)=(41,4,5)\), one gets \(C=23\), \(R=18\), \((h_0,h_1,h_2,h_3)=(21,17,13,9)\), and \((s_0,s_1,s_2,s_3)=(19,23,27,31)\). Their prime factors have \(q-1\) dividing \(990\), so the exponent \(991\) is permitted. The preceding argument gives all four gcds equal to one. Because \(5\mid40\) and \(5\nmid4\), the upper-bound argument excludes five terms.

## Verification
The accompanying standard-library file `verify.py` independently computes the required digit sums and gcds, both by modular prime-factor checks and, in small cases, by constructing the full integers. Execute `python3 verify.py` in a directory containing the extracted file. Its tested output is:

```
VERIFY_OK structured_cases=236 direct_full_cases=6 sieve_cases=741 max_length=12 example_base41_sums=[19, 23, 27, 31] exponent=991
```

The finite computations check 236 members of the prime-power-base family for various even steps and primes, 741 additional admissible bases satisfying the sieve hypotheses, six full big-integer cases, and the displayed base-\(41\) example. They are not proofs of the infinite quantifiers; Steps 1–4 establish those.

## Relationship to prior work
Blau, Harrington, Lohrey, Sosis, and Wong introduced systematic fixed-step anti-Niven progression questions. Their 2023 publicly available preprint proves an upper bound of \(p-1\) when \(p\) is the least prime factor of \(b-1\) not dividing \(d\) (Theorem 2.5), proves sharpness for common differences \(1\) and \(2\) (Theorems 3.2 and 3.3), and formulates a conjecture for arbitrary even differences in odd bases (Conjecture 4.3). Their progression-existence theorem with a freely chosen difference does **not** yield a prescribed difference. The contribution here is the explicit sharp construction for **every fixed even step \(d\ge4\)** on a **positive-density set of odd bases**, including a natural two-parameter prime-power family. The general conjecture for every admissible odd base is not claimed.

Harrington, Litman, and Wong's 2023 work on **Niven**, rather than anti-Niven, numbers addresses divisibility of a digit sum rather than coprimality; it does not cover the present fixed-step anti-Niven theorem. The full 2023 preprint was inspected for overlapping statements and construction hypotheses; the later 2026 journal record could be identified but the complete journal text was not independently inspected. Additional indexing and priority review remain worthwhile.

## Limitations
The theorem assumes \(d\) even, \(p\ge5\) prime with \(p\nmid d\), \(b>C\), and the explicit coprimality restrictions. It does not settle the proposed sharpness for **all** odd bases in Conjecture 4.3; it does not treat odd common differences. The base-family density refers to bases, not starting points. The constructed starting numbers may be extremely large. Finite experiments are corroboration, not exhaustive mathematical certification. Priority relative to all possibly unindexed literature has not been independently established.

## References
1. R. Blau, J. Harrington, S. Lohrey, E. Sosis, and T. W. H. Wong, *Arithmetic Progressions of Integers that are Relatively Prime to their Digital Sums*, arXiv:2308.05228v1 (first public posting 2023-08-09), Theorems 2.4, 2.5, 3.2, 3.3 and Conjecture 4.3; https://arxiv.org/abs/2308.05228. Later journal DOI: 10.1216/rmj.2026.56.13.
2. J. Harrington, D. Litman, and T. W. H. Wong, *Every Arithmetic Progression Contains Infinitely Many b-Niven Numbers*, arXiv:2303.06534 (2023); https://arxiv.org/abs/2303.06534.
3. Fermat's little theorem and the Chinese remainder theorem (classical).
