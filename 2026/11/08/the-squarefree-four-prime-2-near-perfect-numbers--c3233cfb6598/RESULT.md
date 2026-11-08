# The squarefree four-prime 2-near-perfect numbers

## Finding
A positive integer \(n\) is **2-near-perfect** if
\[\sigma(n)=2n+d_1+d_2\]
for two distinct positive proper divisors \(d_1,d_2\) of \(n\), where \(\sigma\) is the positive-divisor sum. For primes \(3\le p<q<r\), the integer \(n=2pqr\) is 2-near-perfect **if and only if**
\[
 n\in\{570,690,910,1722,1974,2002,2470,3230,4386,4510,4730,7630,9590,9730,13026\}.
\]
Each of these fifteen integers has exactly one unordered pair of omitted proper divisors. In increasing order of \(n\), the pairs are
\[(15,285),(3,345),(14,182),(14,574),(2,658),(2,26),(5,95),(1,19),\]
\[(1,731),(11,41),(1,43),(35,545),(7,685),(5,695),(1,2171).\]
This is a complete, unbounded classification of **all squarefree integers with exactly four distinct prime factors**: the odd case is impossible, and the fifteen solutions are even. No claim is made about non-squarefree integers.

## Assumptions and scope
Let \(n\) be any positive squarefree integer with exactly four distinct prime factors. If \(n\) is odd and its prime factors are \(p<q<r<s\), then \[\frac{\sigma(n)}n=\prod_{t\in\{p,q,r,s\}}(1+1/t)\le(4/3)(6/5)(8/7)(12/11)=2304/1155<2.\] Hence any 2-near-perfect \(n\) in this class must be even, so it has the form \(n=2pqr\) for distinct odd primes \(p<q<r\). Then \(n\) has sixteen positive divisors, of which precisely fifteen are proper. A pair of omitted divisors is unordered and its elements must be distinct. The family is infinite before classification. No bound on \(p,q,r\) is assumed; the proof derives one.

## Proof
Write \(D=\sigma(2pqr)-4pqr\). Multiplicativity gives
\[
 D=\bigl(3(p+1)(q+1)-4pq\bigr)r+3(p+1)(q+1)
 =Cr+B,
\]
where \(C=3p+3q+3-pq\) and \(B=3(p+1)(q+1)\). Necessarily \(D>0\). Equivalently
\[\frac{\sigma(2pqr)}{2pqr}=\frac32(1+1/p)(1+1/q)(1+1/r)>2.\]
The right side decreases strictly as any prime increases. The inequalities
\[3\cdot12\cdot14\cdot18<4\cdot11\cdot13\cdot17,\]
\[3\cdot8\cdot14\cdot18<4\cdot7\cdot13\cdot17,\qquad
 3\cdot6\cdot20\cdot24<4\cdot5\cdot19\cdot23\]
force \(p\in\{3,5,7\}\); if \(p=7\), then \(q=11\); if \(p=5\), then \(q\in\{7,11,13,17\}\). If \(p=7,q=11\), then \(D=-20r+288>0\) forces \(r<15\). If \(p=5\) and \(q\ge11\), then \(C=18-2q<0\) and \(r<9(q+1)/(q-9)\le54\).

For \(p=5,q=7\), one has \(D=4r+144\). The divisors of \(70\) are \(1,2,5,7,10,14,35,70\). Each proper divisor of \(70r\) either divides \(70\) or equals \(ar\) for a divisor \(a\mid70\). Two divisors not involving \(r\) sum to at most \(105<4r+144\); two involving \(r\) would force the prime \(r>7\) to divide \(144\), impossible. In the remaining case \(ar+b=4r+144\) with \(a,b\mid70\), whence \((a-4)r=144-b>0\). Thus \(a\ge5\), and \(r\le143\).

For \(p=3\), \(D=12r+12(q+1)\) and the divisors of \(6q\) are \(1,2,3,6,q,2q,3q,6q\). Two divisors free of \(r\) sum to at most \(9q<D\). Two divisible by \(r\) would imply \(r\mid 12(q+1)\), impossible for a prime \(r>q\ge5\): the prime \(r\) cannot divide \(12\), and if it divided \(q+1\) it would equal the even integer \(q+1>2\). Hence precisely one omitted divisor involves \(r\), say \(ar\), and the other is \(b\), where \(a,b\mid6q\). Thus
\[(a-12)r=12(q+1)-b\ge 6q+12>0,\]
so \(a>12\). For \(q\ge29\), this entails \(a\ge q\), and then
\[r\le\frac{12(q+1)-1}{q-12}<q\qquad(q\ge29),\]
contrary to \(r>q\). Thus \(q\in\{5,7,11,13,17,19,23\}\). The smallest possible \(a>12\) for these seven values is respectively \(15,14,22,13,17,19,23\). The resulting bounds on \(r\) are respectively \(23,47,14,167,43,34,26\); in particular \(r\le167\).

Combining all cases proves the **unconditional exhaustive cutoff**
\[p\in\{3,5,7\},\quad r\le167,\]
with precisely the \(q\)-ranges specified above. It remains to examine finitely many candidate prime triples, not a conjecturally adequate search range. For each prime triple, the only fifteen permitted omitted divisors are the fifteen proper divisors of \(2pqr\). The standalone `CHECKER.py` evaluates \(\sigma(n)-2n\) and every unordered pair of distinct proper divisors, using integer arithmetic and trial-division primality tests. Its exhaustive 399-triple output is `CHECKER_OUTPUT.txt`. Exactly fifteen triples pass, and each has a unique omitted pair, as displayed in the Finding. Conversely each reported pair consists of distinct proper divisors and sums to \(\sigma(n)-2n\), so all fifteen qualify.

## Verification
Run `python3 CHECKER.py` using Python 3 with no external packages. It prints the fifteen triples, each full deficit and unique omitted pair, followed by `EXACT_CERTIFICATE_OK count=15 largest=13026 tested_prime_triples=399`. The computation uses the mathematically proved finite cutoff and independently constructs the full proper divisor set for each squarefree input. The proof of the infinite classification includes the cutoff inequalities; unbounded validity does not rely on extrapolating a finite experiment. `CHECKER_OUTPUT.txt` records the actual execution output.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery and Zelinsky (first public 2023-10-02; published 2024-06-19) define 2-near-perfect numbers and classify the two-distinct-prime families \(2^k p\) and \(2^k p^2\). Their Theorems 1–2 do not cover the four-distinct-prime squarefree family \(2pqr\). The public list OEIS A341475 records individual small 2-near-perfect integers, not a proof that every admissible \(2pqr\) is in this fifteen-number set. A separately published three-prime squarefree classification for \(2pq\) does not imply the present four-prime assertion. The proof here uses no assumed completeness of any precomputed table.

## Limitations
The classification concerns all squarefree integers with exactly four distinct prime factors; odd inputs are excluded rigorously by the initial abundancy inequality. It is not a statement about nonsquarefree four-prime 2-near-perfect integers. The originality check covers the inspected primary literature, mathematical-record searches, and accessible earlier claims; independent external validation has not been performed, and equivalent unindexed literature remains a residual risk.

## References
1. V. Aryan, D. Madhavani, S. Parikh, I. Slattery and J. Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305, first posted 2023-10-02; *INTEGERS* 24 (2024), paper A61, https://arxiv.org/abs/2310.01305 and https://math.colgate.edu/~integers/y61/y61.pdf.
2. OEIS A341475, *2-near-perfect numbers*, https://oeis.org/A341475 (finite sequence table, not a complete classification of this family).
3. R. Fearon et al., *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, arXiv:2508.06651, 2025 (different prime-factor-count family).
