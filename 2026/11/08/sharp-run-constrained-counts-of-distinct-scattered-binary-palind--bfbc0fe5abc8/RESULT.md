# Sharp run-constrained counts of distinct scattered binary palindromes

## Finding

Let \(S(w)\) be the number of **distinct, nonempty palindromic subsequence strings** of a finite binary word \(w\); different embeddings of the same palindrome count once. Let \(M_r(n)\) maximize \(S(w)\) over binary words of length \(n\) with exactly \(r\) maximal constant-symbol runs. For each fixed integer \(k\ge1\),

\[
M_{2k+1}(n)=\frac{n^{k+1}}{2^k(k+1)^{k+1}}+O_k(n^k)
\qquad(n\longrightarrow\infty).
\]

The same run decomposition yields the sharp finite formulas

\[
M_3(n)=n+\left\lfloor\frac{n^2}{8}\right\rfloor\quad(n\ge3),
\qquad
M_4(n)=n+\left\lfloor\frac{n^2}{8}\right\rfloor\quad(n\ge4).
\]

In particular, adding a fourth run does not increase the maximum number of distinct scattered palindromes, at any admissible length.

## Assumptions and scope

The alphabet is the fixed binary alphabet \(\{0,1\}\). A subsequence (scattered subword) preserves order but need not be contiguous. A palindrome equals its reversal. A run is a maximal nonempty constant-symbol block. The maximum is taken over **exactly** the indicated number of runs. The \(O_k\) constant may depend on fixed \(k\), not on \(n\). Complementing all bits does not change \(S\), so host words may be written with an initial zero-run.

## Proof

**Full-run palindromes.** Any nonempty palindrome has an odd number of runs: its alternating run-symbol sequence is invariant under reversal and therefore starts and ends in the same symbol. Consider a word with \(2k+1\) runs,

\[
w=0^{a_1}1^{a_2}0^{a_3}\cdots0^{a_{2k+1}},\qquad a_i\ge1.
\]

A subsequence string with exactly \(2k+1\) runs must draw one nonempty constant block from *each* source run in order, because it cannot create more transitions than occur in the source. If that subsequence is palindromic, its paired block lengths agree. Conversely, every choice of positive exponents obeying these equalities embeds, using one source block per run. Thus there are exactly

\[
T(w)=a_{k+1}\prod_{i=1}^k\min(a_i,a_{2k+2-i})
\]

distinct palindromic subsequence strings with \(2k+1\) runs. This counts **strings**, not choices of positions.

**Sharp asymptotic upper bound.** Set \(x_i=\min(a_i,a_{2k+2-i})\) and \(y=a_{k+1}\). Since

\[
2\sum_{i=1}^k x_i+y\le n,
\]

the arithmetic-geometric mean inequality applied to \(2x_1,\ldots,2x_k,y\) gives

\[
T(w)=y\prod_{i=1}^k x_i
\le \frac{n^{k+1}}{2^k(k+1)^{k+1}}.
\]

A palindrome having \(2j+1\) runs is determined uniquely by its initial bit, its \(j\) paired outer positive block lengths, and its one positive central block length. Each length is at most \(n\). Consequently there are at most \(2n^{j+1}\) *possible* palindromic binary strings with \(2j+1\) runs. Any palindromic subsequence of \(w\) not counted in \(T(w)\) has at most \(2k-1\) runs, so

\[
T(w)\le S(w)\le T(w)+2\sum_{j=0}^{k-1}n^{j+1}
\le \frac{n^{k+1}}{2^k(k+1)^{k+1}}+2kn^k.
\]

This bound applies to every length-\(n\) binary word with exactly \(2k+1\) runs.

**Asymptotic attainment.** For \(n\ge2(k+1)\), set

\[
x=\left\lfloor\frac{n}{2(k+1)}\right\rfloor,\qquad
y=n-2kx.
\]

Take the \(2k+1\) run lengths to be \(x,\ldots,x,y,x,\ldots,x\), with \(k\) copies of \(x\) on each side. Every run is nonempty and the length is exactly \(n\). Its full-run contribution is

\[
x^ky=\frac{n^{k+1}}{2^k(k+1)^{k+1}}+O_k(n^k),
\]

since \(x=n/[2(k+1)]+O_k(1)\) and \(y=n/(k+1)+O_k(1)\). Combined with the preceding upper bound, this proves the displayed asymptotic formula.

**Exact three-run maximum.** If \(w=0^a1^b0^c\) with \(a,b,c\ge1\), its single-run palindromic subsequences consist of all-zero strings of lengths through \(a+c\) and all-one strings of lengths through \(b\), exactly \(n=a+b+c\) strings. Its only other palindromic subsequences have three runs and take the form \(0^t1^u0^t\) with \(1\le t\le\min(a,c)\) and \(1\le u\le b\). Hence

\[
S(w)=n+b\min(a,c)\le n+\frac{b(a+c)}2\le n+\frac{n^2}{8}.
\]

Let \(t\) maximize \(t(n-2t)\) over positive integers with \(2t<n\). The maximum is \(\lfloor n^2/8\rfloor\), by completing the square and checking the nearest integers to \(n/4\). The run lengths \((t,n-2t,t)\) attain the upper bound for every \(n\ge3\).

**Exact four-run maximum.** If \(w=0^a1^b0^c1^d\), the single-run contribution is again \(n=a+b+c+d\). The only other palindromes have three runs, of either shape \(0^t1^u0^t\) or \(1^t0^u1^t\). Therefore

\[
S(w)=n+b\min(a,c)+c\min(b,d).
\]

Put \(E=b\min(a,c)+c\min(b,d)\). A four-case comparison, according to \(a\le c\) or \(a>c\) and \(b\le d\) or \(b>d\), proves

\[
2E\le(a+c)(b+d)\le\frac{n^2}{4}.
\]

For clarity, when \(a\le c,b>d\), the difference between the first right-hand side and the left is \((c-a)(b-d)\ge0\); when \(a>c,b\le d\), the left side is \(4bc\le(a+c)(b+d)\); the other two cases follow immediately from \(a\le c\) or \(b\le d\). Since \(E\) is integer, \(E\le\lfloor n^2/8\rfloor\).

Choose the same maximizing positive integer \(t\) as in the three-run case. For every \(n\ge4\) it can be chosen so \(n-2t-1\ge1\). The four positive run lengths

\[
(a,b,c,d)=(1,t,n-2t-1,t)
\]

give \(E=t+t(n-2t-1)=t(n-2t)=\lfloor n^2/8\rfloor\). Hence the four-run upper bound is attained, completing the proof.

## Verification

The accompanying standalone Python 3 script `verify.py` implements a distinct-palindromic-subsequence dynamic program and a separately coded direct subsequence-set generator. It checked the exact three-/four-run formulas and maxima on 1,365 compositions, compared direct generation with dynamic programming on 3,807 binary words, verified the full-run palindrome count where applicable, and checked 32 balanced paired-run constructions. Invoke `python3 verify.py` with no dependencies beyond the Python standard library. These finite tests are not substitutes for the uniform proof above.

## Relationship to prior work

Mahalingam and Pandoh (2021, arXiv:2108.02729) count distinct scattered palindromic subwords, establish a general Fibonacci upper bound, give extremal formulas for sufficiently large alphabet size, and discuss unrestricted extremal problems. Their investigated extremal parameter is the alphabet size, whereas this result fixes the binary alphabet and stratifies the problem by the **number of constant runs**, giving a sharp polynomial leading coefficient and exact low-run plateaus. The general Fibonacci bound is compatible with but does not determine these run-conditioned extrema. Holub and Saari (2009, *On highly palindromic words*) identify binary words through their sets of scattered palindromes and study the longest-palindrome and extension-ratio invariants, not the cardinality extremum by run count. Müllner and Ryzhikov (2019, arXiv:1901.07502) study lengths of palindromic and antipalindromic subsequences, particularly in circular words, not the number of distinct scattered palindromic subsequences conditional on run count.

## Limitations

The asymptotic formula concerns each fixed *odd* run number; it is not an exact formula for arbitrary larger lengths and does not assert uniformity as the run count grows with word length. Even-run exact maxima are proved here only for four runs. Existence of an unindexed equivalent prior result cannot be excluded by a bounded literature search. The mathematical argument and verification are supplied for independent scrutiny; no independent scientific audit has been performed.

## References

1. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729, first public version 2021-08-05. https://arxiv.org/abs/2108.02729
2. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first public version 2019-01-22. https://arxiv.org/abs/1901.07502
3. Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959. Accessible author manuscript: https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf
