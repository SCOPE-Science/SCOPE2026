# The exact prime slice of a factorial square-product obstruction set

## Finding
For a positive integer \(v\), let \(s(v)\) denote its squarefree part, namely the unique squarefree positive integer \(d\) for which \(v=d w^2\) with \(w\) a positive integer. Consider the set defined by Yudin in the study of square products of distinct factorials:
\[
\mathcal R=\{a\ge 1:\ a\text{ is squarefree, and }s(ac!)\ge a\text{ for every integer }c\ge0\}.
\]
The prime members are **exactly**
\[
\boxed{\mathcal R\cap\mathcal P=\{p:p\text{ prime and }p\ge13\}.}
\]
The structural input is a sharp eventual threshold for factorial squarefree parts:
\[
\boxed{s(c!)\ge c^2\quad\text{for every integer }c\ge12.}
\]
The threshold cannot be lowered: \(s(11!)=77<121\). This is the first integer from which the inequality holds without exception, not an assertion of equality at the threshold.

## Assumptions and scope
Factorials include \(0!=1\); \(s(1)=1\). The quantifier over \(c\) in the definition of \(\mathcal R\) is unrestricted. The classification covers all rational primes, not general squarefree integers. We use the classical prime-gap theorem of Nagura: for every real \(x>25\) there is a prime \(q\) with \(x<q<6x/5\). The established prime-gap theorem is an external mathematical premise, cited below.

## Proof
**Lemma (factorial squarefree parts).** For every integer \(c\ge12\), one has \(s(c!)\ge c^2\), whereas \(s(11!)=77<11^2\).

For \(c\ge51\), apply Nagura's theorem successively at the real numbers \(c/2\), \(3c/5\), and \(18c/25\). There are primes in the three disjoint open intervals
\[
(c/2,3c/5),\qquad(3c/5,18c/25),\qquad(18c/25,108c/125).
\]
Every endpoint on the left exceeds \(25\) (the smallest is \(c/2>25\)). Each of these primes lies strictly between \(c/2\) and \(c\); hence its exponent in \(c!\) is exactly one. The three primes are distinct and their product divides \(s(c!)\), so
\[
s(c!) > \frac c2\cdot\frac{3c}{5}\cdot\frac{18c}{25}
=\frac{27}{125}c^3>c^2,
\]
where the last inequality follows from \(c\ge51>125/27\). For \(12\le c\le50\), the explicit finite test in the bundled verifier calculates the exponents of each prime in \(c!\) by Legendre's formula and checks the inequality in exact integer arithmetic. Its independently specified range includes both endpoints. It also verifies \(s(11!)=77\). This proves the lemma for all integers \(c\ge12\).

Now take any prime \(p\ge13\). If \(0\le c<p\), then \(p\) does not divide \(c!\), hence \(s(pc!)=p\,s(c!)\ge p\). If \(c\ge p\), write \(d=s(c!)\). The lemma gives \(d\ge c^2\ge p^2\). Since \(d\) is squarefree, multiplication by the prime \(p\) either adds the prime to the squarefree part or removes it:
\[
s(pc!)=\begin{cases}pd,&p\nmid d,\\d/p,&p\mid d.\end{cases}
\]
In both cases \(s(pc!)\ge p\). The two ranges cover every integer \(c\ge0\), so \(p\in\mathcal R\).

Conversely the five smaller primes admit the explicit witnesses \((p,c,s(pc!))\):
\[
(2,2,1),\quad (3,3,2),\quad (5,6,1),\quad (7,7,5),\quad(11,11,7).
\]
In each case \(s(pc!)<p\); therefore none belongs to \(\mathcal R\). These are all primes smaller than \(13\), completing the classification. \(\square\)

## Verification
Run the bundled standard-library-only checker with `python3 verification/check.py`. It performs complete prime-exponent arithmetic for \(12\le c\le50\), checks the five explicit exclusions, verifies the factorial squarefree-part formula by independent factorization for small inputs, and tests numerous larger values of \(c\) and primes. The finite checks do not establish the infinite statement; Nagura's prime interval theorem and the proof above supply the infinite range.

## Relationship to prior work
Yudin (arXiv:2610.01899v1, §7.1, October 1, 2026) introduces the same set \(\mathcal R\), proves that it has positive lower density, and relates its elements to obstructions for certain five-factor square products of factorials. His proof uses the asymptotic exponential growth of \(s(c!)\). The present contribution identifies exactly the prime members of that already-defined set, through the sharp uniform quadratic lower threshold. This does not assert that all composite squarefree members are classified, nor does it improve Yudin's positive-density theorem. Nagura's 1952 prime-gap theorem is used as a prior result, not claimed as new. OEIS A055204 tabulates \(s(c!)\), including the finite initial values, and is explicitly acknowledged as prior data; the new assertion is their uniform all-index cutoff and the ensuing prime slice of \(\mathcal R\).

## Limitations
Only the prime slice is classified; membership of general squarefree composites and the density of \(\mathcal R\) are not determined here. The proof invokes the published Nagura theorem and a reproducible finite certificate for \(12\le c\le50\). No new quantitative estimate for the frequency of products of five or six factorials is asserted. Exhaustive web and database searches cannot exclude an unindexed historically equivalent observation; independent assessment of novelty remains advisable.

## References
1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1 (first posted October 1, 2026), especially §7.1, https://arxiv.org/html/2610.01899v1.
2. J. Nagura, *On the interval containing at least one prime number*, Proceedings of the Japan Academy **28** (1952), 177–181, DOI 10.3792/pja/1195570997.
3. OEIS Foundation, A055204, *Squarefree part of n!: n! divided by its largest square divisor*, https://oeis.org/A055204.
