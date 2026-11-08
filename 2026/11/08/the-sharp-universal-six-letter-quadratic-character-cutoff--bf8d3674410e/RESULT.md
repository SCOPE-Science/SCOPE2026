# The sharp universal six-letter quadratic-character cutoff

## Finding

For an odd prime \(p\), let \(\chi_p(a)\) denote the Legendre symbol, and consider the six-character words

\[
\mathcal W_6(p)=\{(\chi_p(n),\chi_p(n+1),\ldots,\chi_p(n+5)):1\le n\le p-6\}.
\]

**Theorem.** For every prime \(p\ge 461\), one has \(\mathcal W_6(p)=\{-1,1\}^{6}\). At the preceding prime \(p=457\) there are precisely \(63\) distinct words, the sole missing word being \((1,1,1,1,1,1)\). Hence \(461\) is the sharp least prime after which every prime supports every possible length-six quadratic-residue/nonresidue pattern.

For example, at \(p=461\) the all-residue word begins at \(n=19\), and the all-nonresidue word begins at \(n=173\).

## Assumptions and scope

All primes are rational odd primes. The Legendre symbol is \(1\) on nonzero quadratic residues, \(-1\) on quadratic nonresidues, and \(0\) at zero. Only **ordinary non-wrapping** consecutive integers \(n,n+1,\ldots,n+5\) with \(1\le n\le p-6\) are admitted. Thus zero is never present and no cyclic wraparound is used. A universal threshold here is itself a prime \(P\) such that all primes \(p\ge P\) have complete word sets.

## Proof

Fix a sign vector \(\varepsilon=(\varepsilon_0,\ldots,\varepsilon_5)\in\{-1,1\}^6\), and write \(C_{\varepsilon}(p)\) for its number of non-wrapping occurrences. Identify the admissible starts with the elements of \(\mathbb F_p\) other than \(0,-1,-2,-3,-4,-5\). For any admissible start, the indicator of the required word is

\[
2^{-6}\prod_{j=0}^{5}(1+\varepsilon_j\chi_p(x+j)).
\]

For one of the six excluded starts, precisely one character factor is zero (because \(p>6\)), so the corresponding unnormalized product is between \(0\) and \(2^5\). Therefore

\[
64 C_{\varepsilon}(p)
=\sum_{x\in\mathbb F_p}\prod_{j=0}^{5}(1+\varepsilon_j\chi_p(x+j))-E_{\varepsilon}(p),
\qquad 0\le E_{\varepsilon}(p)\le6\cdot 2^5=192.
\]

Expanding the product yields a constant term \(p\) and one complete multiplicative-character sum for each nonempty subset \(J\subseteq\{0,\ldots,5\}\). Subsets of size one contribute zero. Every two-element subset contributes \(-1\) before its sign coefficient, by the classical quadratic-polynomial character identity; the total absolute contribution of these \(\binom62=15\) terms is at most \(15\). For a subset of cardinality \(d\ge3\), the separable polynomial \(\prod_{j\in J}(X+j)\) is not a square, and the standard Weil bound gives absolute character sum at most \((d-1)\sqrt p\). Summing over all such subsets gives

\[
\sum_{d=3}^{6}\binom6d(d-1)=20\cdot2+15\cdot3+6\cdot4+1\cdot5=114.
\]

Consequently, **uniformly over all sixty-four sign words**,

\[
64C_{\varepsilon}(p)\ge p-114\sqrt p-207.
\]

The right-hand side is positive for every real \(p\ge14000\): its derivative is \(1-57/\sqrt p>0\) in that range, and \((14000-207)^2>114^2\cdot14000\) with \(14000-207>0\). Thus every sign word occurs for every prime \(p\ge14000\).

For the remaining primes \(461\le p<14000\), the exhaustive exact-integer certificate in `artifacts/verify.py` lists all primes using the Eratosthenes sieve and, for each one, computes the quadratic-residue indicator from squares. Sliding a six-bit window over each permissible start gives the complete set of \(64\) words. All \(1564\) primes in the interval have the full set. A separate computation using Euler's criterion checks the residue classifications for \(63\) selected primes, including both boundary primes and samples spread across the range. At \(p=457\), direct complete enumeration yields exactly \(63\) words, with the all-residue word missing; at \(p=461\), it yields all \(64\). The primes \(457\) and \(461\) are consecutive (both established by the same sieve), so the universal prime cutoff is exactly \(461\).

The finite certificate is exhaustive over its explicitly bounded interval; the character-sum argument, not finite extrapolation, handles the infinite remainder.

## Verification

From the directory containing this document, execute `python3 artifacts/verify.py` with Python 3 and only its standard library. The deterministic output is recorded in `artifacts/verify_output.txt`. The program exhaustively checks all primes from \(461\) through \(13999\), counts the all-ones-pattern obstruction at \(457\), confirms the success at \(461\), checks the rational positivity certificate at \(14000\), and independently cross-checks Euler-character calculations for \(63\) primes. In the bit encoding, bit \(j\) is one precisely when the \((j+1)\)-st entry is a quadratic residue; mask \(63\) is therefore the all-residue word.

## Relationship to prior work

Wang and Fang [1] study homogeneous quadratic-residue or nonresidue progressions of small length, particularly at lengths \(3\), \(4\), and \(5\); their stated results do not determine simultaneous occurrence of all \(64\) mixed length-six patterns. Conrad [2] gives the classical general \(p/2^r+O_r(\sqrt p)\) counting framework based on Weil's bound, and the existence argument here uses that established machinery with sharper accounting of small subsets. Kiritchenko and collaborators [3] study consecutive homogeneous residue strings and associated curves; that does not settle the stated mixed-word cutoff. Buchaev and Tsfasman [4] give formulas for arbitrary mixed words of lengths \(4\) and \(5\), not the length-six case stated here. Cohen [5] treats homogeneous triples and certain quadruples. The new element is the sharp universal all-words threshold at length six, with an exhaustive small-prime certificate and a character-sum bound covering the remaining primes.

## Limitations

This result does not give closed formulas for each individual pattern count, characterize the distribution of all lengths, or cover composite moduli. The estimates above are sufficient rather than optimal for large primes. The 2026 Buchaev–Tsfasman abstract is available, but its full text could not be inspected, so an equivalent unindexed appendix or otherwise unlocated earlier statement remains an originality risk.

## References

1. X. Wang and H. Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, Journal of Mathematics (first published 2023-10-03), https://doi.org/10.1155/2023/5253261.
2. K. Conrad, *Quadratic Residue Patterns Modulo a Prime*, expository note, https://kconrad.math.uconn.edu/blurbs/ugradnumthy/QuadraticResiduePatterns.pdf (Theorem 2.1).
3. V. Kiritchenko, M. Tsfasman, S. Vlăduţ, and I. Zakharevich, *Quadratic residue patterns, algebraic curves and a K3 surface*, arXiv:2403.16326.
4. A. Buchaev and M. Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418 (abstract inspected).
5. S. D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737.
