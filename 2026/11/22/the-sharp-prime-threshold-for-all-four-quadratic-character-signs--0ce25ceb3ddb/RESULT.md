# The sharp prime threshold for all four quadratic-character signs following a nonzero square

## Finding
Let \(p\ge5\) be prime, let \(\chi_p\) be the Legendre symbol with \(\chi_p(0)=0\), and for \(x\in\mathbb F_p^\times\) consider the four-sign word
\[
W_p(x)=\bigl(\chi_p(x^2+1),\chi_p(x^2+2),\chi_p(x^2+3),\chi_p(x^2+4)\bigr).
\]
Only \(x\) with all four coordinates nonzero contribute a word in \(\{-1,1\}^4\). Every one of the sixteen words occurs **if and only if**
\[
p\notin E=\{5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61, 71, 73, 89, 97, 103, 113, 137, 149, 193\}.
\]
Consequently all sixteen occur for every prime \(p\ge197\). This is sharp as a *universal prime cutoff*: the largest exceptional prime is \(193\), where the only missing word is \((+1,+1,+1,+1)\). At \(p=5\), no admissible nonzero square starts a four-sign word.

Equivalently, every prescribed sequence of four quadratic-residue/nonresidue signs immediately after a **nonzero quadratic residue** is attainable modulo every prime \(p\ge197\). Unlike a statement about arbitrary starting residues, this fixes the multiplicative class of the starting term.

## Assumptions and scope
All arithmetic is in \(\mathbb F_p\); the four shifts may cross the usual integer-representative boundary modulo \(p\). The starting square is required to be nonzero: \(x=0\) is excluded. A coordinate equal to zero is not called either a quadratic residue or a nonresidue. The classification covers every prime \(p\ge5\), each of the sixteen mixed sign words, and no extension fields or words of other lengths. The characteristic bound \(p\ge5\) ensures that shifts \(1,2,3,4\) are distinct nonzero residues.

## Proof
**1. Indicator expansion.** For a prescribed \(\boldsymbol\varepsilon=(\varepsilon_1,\ldots,\varepsilon_4)\in\{\pm1\}^4\), let \(N_p^\times(\boldsymbol\varepsilon)\) be the number of *nonzero* inputs \(x\) having exactly this word. Define the nonnegative integer
\[
T_p(\boldsymbol\varepsilon)=\sum_{x\in\mathbb F_p}\prod_{j=1}^4\bigl(1+\varepsilon_j\chi_p(x^2+j)\bigr).
\]
For an input with no zero argument, the summand is \(16\) when its word matches, otherwise zero. At a zero argument, exactly one of the four factors is \(1\), since the shifts are pairwise distinct; the other factors belong to \(\{0,2\}\). Thus each such exceptional summand is between \(0\) and \(8\). Each quadratic \(x^2+j\) has at most two roots, so at most eight inputs have any zero argument. Finally, \(x=0\) adds at most \(16\). Therefore
\[
16N_p^\times(\boldsymbol\varepsilon)\ \ge\ T_p(\boldsymbol\varepsilon)-80.
\]
This inequality remains true if the same zero-input exceptional contribution is counted twice; the upper bound is deliberately conservative.

**2. Weil character-sum bound.** Expanding the four factors gives \(T_p=p+\sum_{\varnothing\ne S\subseteq\{1,2,3,4\}}\bigl(\prod_{j\in S}\varepsilon_j\bigr)H_p(S)\), with
\[
H_p(S)=\sum_{x\in\mathbb F_p}\chi_p\Bigl(\prod_{j\in S}(x^2+j)\Bigr).
\]
For \(p\ge5\), every polynomial \(\prod_{j\in S}(X^2+j)\) is squarefree: each factor has nonzero discriminant, distinct factors have no common root, and its degree is \(2|S|\). In particular it is not a square in \(\overline{\mathbb F}_p[X]\). The standard Weil bound for a nontrivial quadratic character of a squarefree polynomial of degree \(d\) yields \(|H_p(S)|\le(d-1)\sqrt p=(2|S|-1)\sqrt p\). Consequently,
\[
T_p(\boldsymbol\varepsilon)\ge p-\Bigl(\sum_{s=1}^4\binom4s(2s-1)\Bigr)\sqrt p=p-49\sqrt p,
\]
and hence
\[
16N_p^\times(\boldsymbol\varepsilon)\ge p-49\sqrt p-80.
\]
The right side is strictly positive for all real \(p\ge2579\): writing \(u=\sqrt p\), its value increases with \(u>49/2\), and its value at \(p=2579\) is positive. Thus every word occurs for every prime \(p\ge2579\), without any computational hypothesis.

**3. Finite exact classification.** It remains to check the finite set of primes \(5\le p<2579\). The attached standalone `verify_square_index_patterns.py` computes these primes by an integer sieve (exactly \(373\)), and for each prime computes the full sixteen-bit presence mask twice: first by enumerating \(1\le x<p\) and using Euler's criterion, and independently by constructing the set of nonzero squares and enumerating each distinct square origin. It requires full equality of all \(373\) masks and verifies the complete exceptional-prime list. The numbers of missing words, in the same order as \(E\), are
\[
16,14,12,13,12,9,6,6,6,3,6,1,3,3,2,1,2,2,2,1,1,2,1,1.
\]
It also verifies that the only absent word at \(193\) is the all-positive word, while all sixteen occur at \(197\). The two algorithms have different enumerations and distinct character-evaluation methods. The finite exhaustive check plus the uniform infinite bound gives the asserted classification.

## Verification
Run `python3 verify_square_index_patterns.py` using standard Python 3. The deterministic checker prints `PASS`, enumerates all \(373\) primes below \(2579\), compares \(5,968\) independently computed word-presence bits, validates the twenty-four exceptional primes and their missing-word counts, and prints a SHA-256 fingerprint of the complete ordered prime-to-mask census: `ae46170c708cc49792a01577a3ce855d0f2c54dda0f6a570596d42045a6d44aa`. The checker has been run successfully. Exhaustive finite enumeration applies only below the analytic cutoff; the Weil argument is needed for the infinite range.

## Relationship to prior work
Wang and Fang (2023), *The Distribution Properties of Consecutive Quadratic Residue Sequences*, study arithmetic-progression runs of uniform residue status with fixed step, with precise formulas and estimates in selected cases. Their full accessible article (definitions, Theorems 8, 10, 11, conclusions and references) does not give this restricted-start, **all mixed words**, sharp exceptional-prime table. Wang and Li (2023) study triples of consecutive residues/nonresidues and are similarly distinct.

An existing sharp six-word universality theorem establishes all sixty-four unrestricted nonwrapping quadratic-sign words for primes \(p\ge461\). It implies eventual existence of our five-term \((+,\varepsilon_1,\ldots,\varepsilon_4)\) words for such large primes, but not universality at \(197\le p<461\) or this complete exception list. The six-word result also excludes wraparound starts. Buchaev and Tsfasman (arXiv:2607.17418) provide general finite-field count formulas for length-four/five sign words in terms of curve traces; the accessible abstract does not state our sharp prime threshold. Its primary full text was not accessed, so unrecognized implicit coverage is an originality risk.

The character-indicator expansion, the Weil bound, and simple sieve enumeration are established tools, not claimed as original. The proposed contribution is the complete prime classification for a natural multiplicatively restricted family of sign words, including the exact last obstruction.

## Limitations
The proof gives no simple symbolic formula for word multiplicities at individual primes; it settles existence and the complete exception set. The analytic bound is nonoptimal on a finite interval, which is bridged by exact enumeration. No claim is made for characteristic two or three, nonprime finite fields, arbitrary shift patterns, or longer words. The 2026 paper with general five-pattern character formulas was known by abstract but unavailable in full text, leaving a specific bibliographic priority risk. Independent mathematical and originality audits have not been performed.

## References
1. Xiao Wang and Hao Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, Journal of Mathematics (2023), article 5253261; first published 2023-10-03. https://doi.org/10.1155/2023/5253261
2. Xiao Wang and Ai Hua Li, *Distribution Properties and Applications of Consecutive Quadratic Residues*, Acta Mathematica Sinica, Chinese Series 66 (2023), 389–398. https://doi.org/10.12386/A20210160
3. André Weil, *On Some Exponential Sums*, Proc. Natl. Acad. Sci. USA 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204
4. Abdulkadyr Buchaev and Michael Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418 (2026). https://arxiv.org/abs/2607.17418
