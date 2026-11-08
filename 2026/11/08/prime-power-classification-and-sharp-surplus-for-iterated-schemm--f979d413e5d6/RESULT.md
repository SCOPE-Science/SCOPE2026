# Prime-power classification and sharp surplus for iterated Schemmel totient sums

## Finding
For each prime \(p\) and integer \(a\ge1\), the iterate-sum of the second Schemmel totient has the complete sign classification
\[
\begin{aligned}
D_2(2^a)&=0,\\
D_2(3^a)&=\frac{3^a-1}{2},\\
D_2(5^a)&=\frac{3\cdot5^a+1}{4},\\
D_2(p^a)&>p^a\qquad(p\ge7).
\end{aligned}
\]
In the abundant regime the sharp global surplus is
\[
\min_{p\ge7\text{ prime},\,a\ge1}\bigl(D_2(p^a)-p^a\bigr)=2,
\]
and the only minimizers are \((p,a)=(7,1),(11,1),(17,1)\). Thus **no prime power is \(D_2\)-perfect**. The primes \(2,3,5\) are deficient at every positive exponent, while every prime \(p\ge7\) is abundant at every positive exponent.

## Assumptions and scope
For every integer \(n>1\), define the second Schemmel totient
\[
L_2(n)=\prod_{p^e\parallel n}p^{e-1}(p-2),\quad L_2(1)=1,\quad L_2(0)=0.
\]
Here \(p^e\parallel n\) indicates an exact prime-power divisor. Equivalently, \(L_2(n)\) counts residues \(x\bmod n\) such that both \(x\) and \(x+1\) are units modulo \(n\). When \(n>1\), let \(R_2(n)\) be the smallest positive integer \(r\) for which \(L_2^{(r)}(n)\in\{0,1\}\), and set
\[
D_2(n)=\sum_{j=1}^{R_2(n)}L_2^{(j)}(n),\qquad D_2(1)=0.
\]
For odd \(n>1\), all iterates until the terminal \(1\) are odd and strictly decreasing. For even \(n\), the first iterate is \(0\). Thus the definitions make sense for every positive integer.

## Proof
**1. Two elementary lemmas.** The displayed Euler-product formula follows by counting at a prime power: if \(p\ge3\), exactly \(p^e-2p^{e-1}\) residues avoid both forbidden classes \(0,-1\bmod p\); if \(p=2\), none do. The Chinese remainder theorem multiplies the local counts.

For odd \(n\ge5\), every factor \(p^{e-1}(p-2)\) in the product is a positive odd integer. It equals \(1\) only when \((p,e)=(3,1)\), and equals \(3\) only when \((p,e)=(3,2)\) or \((5,1)\). The only odd \(n\ge5\) with \(L_2(n)=3\) are therefore
\[
\{5,9,15\}.
\]
All other odd \(n\ge5\) have \(L_2(n)\ge5\), since \(L_2(n)=1\) would force \(n=3\). Furthermore, \(L_2(n)\ge3\) implies \(L_2^{(2)}(n)\ge1\), because \(L_2\) maps odd integers to odd integers. Consequently
\[
D_2(n)\ge4\quad(n\ge5\text{ odd}),\qquad
D_2(n)=4\iff n\in\{5,9,15\}.
\tag{1}
\]
The reverse implication uses \(L_2(3)=1\); the forward implication follows because the first iterate is odd and at least \(3\), the second at least \(1\), and every subsequent term is nonnegative.

**2. Prime powers at \(2,3,5\).** For \(a\ge1\), \(L_2(2^a)=0\), proving the first formula. Also, the positive iterates of \(3^a\) are \(3^{a-1},3^{a-2},\ldots,1\), and hence their sum is \((3^a-1)/2\). The positive iterates of \(5^a\) are
\[
3\cdot5^{a-1},\;3\cdot5^{a-2},\;\ldots,\;3,\;1.
\]
Indeed, \(L_2(5^a)=3\cdot5^{a-1}\), \(L_2(3)=1\), and for \(j\ge1\) one has \(L_2(3\cdot5^j)=3\cdot5^{j-1}\). The geometric sum gives \(D_2(5^a)=(3\cdot5^a+1)/4\), strictly smaller than \(5^a\).

**3. Every larger prime power is abundant.** Let \(p\ge7\) be prime. If \(a=1\), the recursion for the iterate sum and (1) yield
\[
D_2(p)=p-2+D_2(p-2)\ge p+2.
\]
Equality holds exactly when \(p-2\in\{5,9,15\}\), which is equivalent to \(p\in\{7,11,17\}\).

If \(a\ge2\), write \(b=L_2(p-2)\ge3\). Since \(\gcd(p,p-2)=1\), the first two iterates satisfy
\[
L_2(p^a)=p^{a-1}(p-2),\qquad
L_2^{(2)}(p^a)=p^{a-2}(p-2)b.
\]
Their sum is at least
\[
p^{a-2}(p-2)(p+3)=p^a+(p-6)p^{a-2}.
\]
The second iterate is odd and at least \(15\), so its successor is at least \(3\) by the first lemma. Therefore
\[
D_2(p^a)-p^a\ge(p-6)p^{a-2}+3\ge4\qquad(a\ge2).
\]
Combining both exponent cases proves strict abundance and shows that the global smallest surplus \(2\) occurs only at the three stated primes to exponent one. All prime powers are now classified. \(\square\)

## Verification
The accompanying standalone standard-library script `verify.py` independently counts consecutive units directly for each \(1\le n\le500\), replays the iterate-sum definition, and tests the formulas for \(1776\) prime powers with prime \(p\le10000\) and power \(p^a\le10^7\). It additionally checks the minimum surplus and the three equality cases, and enumerates the fiber \(L_2(n)=3\) among odd \(n<100000\). Run with `python3 verify.py`. All assertions pass using exact integers. The infinite assertions follow from the proof, not from these finite tests.

## Relationship to prior work
Defant introduced and studied \(D_m\), proving that every multiple of \(3\) is \(D_m\)-deficient for \(m>1\), and that every multiple of \(5\) is \(D_m\)-deficient for \(m=2\). Thus the deficiency of the powers of \(3\) and \(5\) is **already covered**; the explicit formulas record it but are not the substantive new comparison. His Theorem 3.5 constructs infinitely many abundant prime-power rays for each even \(m\), but does not classify every prime at \(m=2\) or determine the sharp surplus. The same article asks whether further \(D_m\)-perfect numbers exist beyond the exhibited example. Harrington and Jones studied the same underlying exceptional-unit totient and the *number* of iterations on a restricted domain, rather than the *sum* of iterates. The present complete prime-power dichotomy and sharp minimum are not consequences of their stated iteration-length formulas.

## Limitations
The result concerns only \(D_2\) at prime powers, not integers with two or more distinct prime divisors, nor the functions \(D_m\) for other parameters. No additional \(D_2\)-perfect numbers are constructed; the classification excludes only the one-prime-support case. The proof is elementary and may admit an unlocated historical equivalent; literature search and registry absence do not establish absolute priority. Independent mathematical assessment is not included.

## References
1. Colin Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, Journal of Integer Sequences **18** (2015), Article 15.2.1; `https://cs.uwaterloo.ca/journals/JIS/VOL18/Defant/defant5.html`; author preprint `https://arxiv.org/abs/1506.05426`.
2. Joshua Harrington and Lenny Jones, *On the Iteration of a Function Related to Euler's \(\phi\)-Function*, Integers **10** (2010), A42, 497–515; `https://math.colgate.edu/~integers/k42/k42.pdf`.
