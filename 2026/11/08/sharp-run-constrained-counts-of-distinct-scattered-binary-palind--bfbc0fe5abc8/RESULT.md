# Sharp three–four-run plateau for distinct scattered binary palindromes

## Finding

For a finite binary word w, let S(w) count distinct nonempty palindromic subsequence **strings** (not embeddings), and let M_r(n) be the maximum of S(w) over all binary words of length n with exactly r nonempty maximal constant-symbol runs. Then

\[
M_3(n)=n+\left\lfloor\frac{n^2}{8}\right\rfloor\quad(n\ge3),\qquad
M_4(n)=n+\left\lfloor\frac{n^2}{8}\right\rfloor\quad(n\ge4).
\]

Thus the additional fourth run does not increase this exact extremal count for any admissible length. This equality is the new assertion. The more general odd-run asymptotic coefficient, including the binary case, was already established by the stronger all-alphabet run-bounded theorem dated October 25, 2026, cited below; **no originality is claimed for that asymptotic result**.

## Scope and definitions

The alphabet is {0,1}. A subsequence need not be consecutive, but retains order. Identical resulting strings are counted once. A run is a maximal nonempty constant-symbol block. Both r and length n are exact; complementing all bits does not affect S(w). The statement applies to n≥r only, and says nothing about the finite maximum with five or more runs.

## Proof

Every palindrome has an odd number of runs, because a palindromic run-symbol sequence cannot have two unequal neighboring middle runs. For a three-run host 0^a1^b0^c (a,b,c≥1), the monochromatic subsequences give exactly a+b+c=n different strings. The other palindromes are exactly 0^t1^u0^t, with 1≤t≤min(a,c), 1≤u≤b. Therefore
\[
S(0^a1^b0^c)=n+b\min(a,c).
\]
Since b min(a,c)≤b(a+c)/2≤n²/8, the integer excess is at most floor(n²/8). Choosing (a,b,c)=(t,n−2t,t), where t is a positive integer maximizing t(n−2t), attains floor(n²/8) for every n≥3, proving the three-run formula.

For four positive runs, write w=0^a1^b0^c1^d. Its monochromatic palindromes again total n. Every nonconstant palindromic subsequence has three runs, either 0^t1^u0^t (possible for 1≤t≤min(a,c), 1≤u≤b) or 1^t0^u1^t (possible for 1≤t≤min(b,d), 1≤u≤c). These two string forms are disjoint. Thus, exactly,
\[
S(w)=n+E,\quad E=b\min(a,c)+c\min(b,d).
\]
We show 2E≤(a+c)(b+d) by the four exhaustive cases. If a≤c and b≤d, then 2E=2ab+2bc=2b(a+c)≤(a+c)(b+d). If a≤c and b>d, then 2E=2ab+2cd, and (a+c)(b+d)−2E=(c−a)(b−d)≥0. If a>c and b≤d, then 2E=4bc≤(a+c)(b+d). If a>c and b>d, then 2E=2bc+2cd=2c(b+d)≤(a+c)(b+d). By AM–GM, (a+c)(b+d)≤n²/4. Hence E≤floor(n²/8).

Choose t maximizing t(n−2t), with 1≤t and n−2t−1≥1 (a maximizer with this property exists for every n≥4). The positive four-run lengths (a,b,c,d)=(1,t,n−2t−1,t) give E=t+t(n−2t−1)=t(n−2t)=floor(n²/8). This proves M4(n) and the exact plateau for every n≥4. The argument counts different subsequence strings, and handles all integer boundaries without taking a limit.

## Verification and limitations

The existing standard-library `verify.py` directly compares distinct subsequence sets with an independently implemented interval dynamic program for short words and exhaustively checks three- and four-run compositions of short lengths. These finite checks corroborate rather than establish the infinite theorem: the four-case inequality and integer witness do that. We do not assert uniqueness of finite extremizers, exact maxima for r≥5, or any alphabet beyond binary.

## Relationship to published results

The October 25 theorem *Universal run-bounded asymptotics and rigidity for scattered palindromes* establishes the sharp asymptotic leading coefficient n^(k+1)/[2^k(k+1)^(k+1)] for every fixed run budget 2k+1 and every alphabet q≥2. In particular it subsumes the originally submitted odd-run asymptotic; that claim is not reproduced here as a new finding. Its quantitative leading-order result does not determine the exact four-run integer maximum or the all-length three/four plateau. The October 26 *Scattered palindrome spectrum and sharp cubic growth for five-run binary words* establishes the five-run exact spectrum and the weaker four-run O(n²) growth, but not this exact finite-length plateau. Mahalingam and Pandoh, *Counting scattered palindromes in a finite word* (arXiv:2108.02729), develop the invariant and general Fibonacci/alphabet-size results; their inspected theorem statements do not imply the four-run equality.

References:
- https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-universal-run-bounded-asymptotics-and-rigidity-for-scattered-pal--24ceac73bbf9
- https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-scattered-palindrome-spectrum-and-sharp-cubic-growth-for-five-ru--4f4e17853929
- https://arxiv.org/abs/2108.02729

Priority remains qualified by possible unindexed earlier special-case computations. No external scientific certification is asserted.
