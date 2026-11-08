# Exactly eight squarefree four-prime solutions to \(\sigma(n)=2\varphi(n)\)

## Finding
Write \(\sigma(n)\) for the sum of the positive divisors of \(n\), \(\varphi(n)\) for Euler's totient function, and \(\omega(n)\) for the number of distinct prime factors. Then, for every positive squarefree integer \(n\) with \(\omega(n)=4\),
\[
\sigma(n)=2\varphi(n)\quad\Longleftrightarrow\quad
n\in\{24871,29029,50065,58435,64285,87685,137885,140335\}.
\]
Equivalently, the eight increasing prime tuples \((p,q,r,s)\) are
\[
(5,11,23,109),\ (5,13,17,127),\ (5,13,19,71),\ (5,13,23,43),
\]
\[
(5,13,29,31),\ (5,17,19,31),\ (7,11,13,29),\ (7,11,17,19).
\]
This is an unrestricted classification, not a computational cutoff. The eight integers themselves appear in the previously published sequence A062699; the asserted contribution is proof that the list exhausts the squarefree exactly-four-prime stratum.

## Assumptions and scope
The statement ranges over **all** positive squarefree integers having exactly four distinct prime factors. It makes no claim about numbers with repeated prime factors or with other numbers of distinct prime factors. Put \(n=pqrs\) with primes \(p<q<r<s\), and let \(R(t)=(t+1)/(t-1)\) for \(t>1\). Multiplicativity gives
\[
\frac{\sigma(pqrs)}{\varphi(pqrs)}=R(p)R(q)R(r)R(s).
\]
The function \(R(t)\) is strictly decreasing and exceeds \(1\). All inequalities below are strict inequalities between rational numbers.

## Proof
**First-prime and second-prime reduction.** If \(p=2\), then the ratio is at least \(R(2)=3>2\). If \(p=3\), then \(R(3)=2\), and the remaining factors make the ratio greater than \(2\). If \(p\ge13\), the ratio is at most \(R(13)^4=(7/6)^4<2\). If \(p=11\), then \(q,r,s\ge13\) and the ratio is at most \(R(11)R(13)^3<2\). Hence \(p\in\{5,7\}\).

For \(p=5\), the case \(q=7\) is excluded because \(R(5)R(7)=2\) already. If \(q\ge23\), then \(R(5)R(23)^3<2\); if \(q=19\), the lower bounds \(r,s\ge23\) give \(R(5)R(19)R(23)^2<2\). Thus \(q\in\{11,13,17\}\). For \(p=7\), if \(q\ge17\), then \(R(7)R(17)^3<2\). If \(q=13\), then \(r,s\ge17\) and \(R(7)R(13)R(17)^2<2\). Hence \(q=11\). The only possible ordered first-two-prime pairs are therefore
\[
(p,q)\in\{(5,11),(5,13),(5,17),(7,11)\}.
\]

**Bounded third prime.** Since \(s>r\), the inequality \(R(p)R(q)R(r)^2<2\) would prevent a solution. Direct exact rational comparisons show, in the displayed order of the four pairs,
\[
R(5)R(11)R(41)^2<2,\quad R(5)R(13)R(31)^2<2,
\]
\[
R(5)R(17)R(29)^2<2,\quad R(7)R(11)R(19)^2<2.
\]
Thus respectively \(r<41,31,29,19\). Set \(A=R(p)R(q)R(r)\). Since \(1<R(s)<R(r)\), a solution requires both \(A<2\) and \(AR(r)>2\). The latter two inequalities, tested over *all primes* strictly between \(q\) and the just-proved finite bound, leave exactly
\[
\begin{array}{c|c}
(p,q)&\text{admissible }r\\\hline
(5,11)&23,29,31,37\\
(5,13)&17,19,23,29\\
(5,17)&19,23\\
(7,11)&13,17
\end{array}.
\]
This finite list has exactly twelve triples, and exhaustiveness follows from the strict monotonic bounds, not from a cutoff experiment.

**Fourth prime and primality.** For any such triple, \(AR(s)=2\) is equivalent to
\[
s=\frac{2+A}{2-A}.
\]
This determines \(s\) *uniquely*. Exact rational substitution gives the complete table
\[
\begin{array}{c|r|l}
(p,q,r)&s&\text{outcome}\\\hline
(5,11,23)&109&\text{prime}\\
(5,11,29)&55&\text{composite}\\
(5,11,31)&49&\text{composite}\\
(5,11,37)&39&\text{composite}\\
(5,13,17)&127&\text{prime}\\
(5,13,19)&71&\text{prime}\\
(5,13,23)&43&\text{prime}\\
(5,13,29)&31&\text{prime}\\
(5,17,19)&31&\text{prime}\\
(5,17,23)&169/7&\text{not integral}\\
(7,11,13)&29&\text{prime}\\
(7,11,17)&19&\text{prime}
\end{array}.
\]
Every surviving prime \(s\) exceeds \(r\). Each yields an integer \(n=pqrs\) from the asserted list, and the defining equality \(R(p)R(q)R(r)R(s)=2\) verifies sufficiency. Every other possibility has been excluded. \(\square\)

## Verification
The accompanying standalone `verify.py` uses only the Python 3 standard library and exact rational arithmetic. Run `python3 verify.py`; successful output begins `VERIFY_OK` and lists all eight integers. It checks the monotone inequalities, all twelve candidate triples, the uniquely forced fourth-prime values, primality, and direct factor-product identities. The proof above independently explains why the bounded enumeration is complete.

## Relationship to prior work
Sequence A062699, originally credited to Jason Earls on July 11, 2001, records the integers satisfying \(\sigma(n)=2\varphi(n)\) and includes all eight integers in the present statement. Broughan–Delbourgo (2013) prove that the only solutions with *at most three* distinct prime factors are \(3,35,1045\), plus general finiteness statements. Broughan–Zhou (2014) study \(\varphi(n)\mid\sigma(n)\), principally at up to three prime factors, and display \(24871\) as a four-prime example. Neither inspected paper states this exact all-four-prime squarefree classification. On squarefree arguments \(\sigma\) equals Dedekind's \(\psi\), so the equivalent equation \(\psi(n)=2\varphi(n)\) was also considered. The result is not claimed as establishing absolute historical priority over material not located or fully inspected.

## Limitations
This proof applies only to squarefree \(n\) with exactly four distinct prime factors. It does not classify all four-prime-support solutions with repeated exponents. Although prior numerical tables list the eight values, the distinction made here is a proof of **global exhaustion**, not discovery of new integer terms. Undetected earlier full classifications remain possible; independently audited validity and bibliographic priority are not asserted.

## References
1. OEIS Foundation, A062699, *Numbers k such that sigma(k) = 2*phi(k)*, https://oeis.org/A062699 (entry attributed to Jason Earls, July 11, 2001).
2. K. A. Broughan and D. Delbourgo, *On the Ratio of the Sum of Divisors and Euler's Totient Function I*, Journal of Integer Sequences 16 (2013), Article 13.8.8, https://cs.uwaterloo.ca/journals/JIS/VOL16/Broughan/broughan26.html.
3. K. A. Broughan and Q. Zhou, *On the Ratio of the Sum of Divisors and Euler's Totient Function II*, Journal of Integer Sequences 17 (2014), Article 14.9.2, https://cs.uwaterloo.ca/journals/JIS/VOL17/Broughan/bro32.html.
4. OEIS Foundation, A292390, Dedekind-psi to Euler-totient equality sequence, https://oeis.org/A292390.
