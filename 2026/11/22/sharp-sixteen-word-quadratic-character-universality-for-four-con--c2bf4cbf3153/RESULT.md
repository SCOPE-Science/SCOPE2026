# Sharp sixteen-word quadratic-character universality for four consecutive Gaussian norms

## Finding
For an odd prime \(p\), write \(\chi_p\) for the Legendre symbol, with \(\chi_p(0)=0\), and put \(F_j(X)=(X+j)^2+1\) for \(j\in\{0,1,2,3\}\). Call a sign word \(\varepsilon\in\{-1,1\}^4\) *realized* if there is \(x\in\mathbb F_p\) satisfying \(\chi_p(F_j(x))=\varepsilon_j\) for every \(j\).

**Theorem.** All sixteen sign words are realized if and only if the odd prime \(p\) does not belong to
\[
\mathcal E=\{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61\}.
\]
In particular, every prime \(p\ge67\) realizes all sixteen words, and the threshold is sharp: at \(p=61\) the word \((+1,-1,-1,+1)\) is absent. The condition is not monotone below the cutoff: \(p=59\) already realizes every word.

## Assumptions and scope
The variable \(x\) ranges over all residue classes modulo an **odd prime**, not an interval of positive integers. A vanishing \(F_j(x)\) realizes neither sign and is excluded automatically. A word specifies the ordered signs of four successive Gaussian integer norms \(N(x+j+i)=F_j(x)\). This theorem concerns existence of all sixteen words, not an exact formula for their individual multiplicities or the corresponding question over composite moduli.

## Proof
Fix \(p>13\). Each \(F_j\) has derivative \(2(X+j)\), and this derivative cannot vanish at a root of \(F_j\) when \(p\) is odd, so \(F_j\) is separable. If \(F_i(x)=F_j(x)=0\) with \(i\ne j\), subtraction gives \((i-j)(2x+i+j)=0\). Because \(0<|i-j|\le3<p\), one has \(2x=-i-j\), and substitution gives \((i-j)^2+4=0\pmod p\). Its possible integer values are \(5,8,13\), impossible for \(p>13\). Thus the four polynomials are pairwise coprime and every nonempty subproduct \(F_I=\prod_{j\in I}F_j\) is squarefree of degree \(2|I|\); in particular none is a square over the algebraic closure.

For \(\varepsilon\in\{-1,1\}^4\) put
\[
P_\varepsilon(x)=\prod_{j=0}^{3}\bigl(1+\varepsilon_j\chi_p(F_j(x))\bigr),\qquad
N_\varepsilon=\#\{x\in\mathbb F_p: \chi_p(F_j(x))=\varepsilon_j\ \forall j\}.
\]
If all four norm values are nonzero, \(P_\varepsilon(x)=16\) at precisely the realizing \(x\), and \(0\) otherwise. At a zero of any norm, \(0\le P_\varepsilon(x)\le8\). There are at most eight such \(x\), so
\[
16N_\varepsilon\ \ge\ \sum_{x\in\mathbb F_p}P_\varepsilon(x)-64.
\]
Expanding the product, the empty subset contributes \(p\). For every nonempty \(I\subseteq\{0,1,2,3\}\), the standard quadratic-character Weil bound for a squarefree polynomial of degree \(2|I|\) yields
\[
\left|\sum_{x\in\mathbb F_p}\chi_p(F_I(x))\right|\le(2|I|-1)\sqrt p.
\]
Consequently,
\[
16N_\varepsilon\ge p-\Bigl(4\cdot1+6\cdot3+4\cdot5+1\cdot7\Bigr)\sqrt p-64
=p-49\sqrt p-64.
\]
The right side is positive whenever \(p\ge2529\). Therefore every word occurs for all primes in that infinite range, uniformly over \(\varepsilon\).

For the remaining odd primes \(p<2529\), a finite exhaustive computation independently forms all sixteen counts in two ways. First it forms the nonzero quadratic-residue set \(\{r^2\bmod p:1\le r<p\}\); second it uses Euler's criterion \(a^{(p-1)/2}\equiv\pm1\pmod p\) at each nonzero norm. Both independently enumerate every \(x\in\{0,\ldots,p-1\}\), construct its four-bit sign mask, and discard zero norms. The two complete histograms agree for each of the 368 odd primes below \(2529\). The only primes with a zero histogram entry are precisely the sixteen primes in \(\mathcal E\) above. At \(61\), only mask \(1001\), the word \((+1,-1,-1,+1)\), is absent. At \(59\) and \(67\), all sixteen masks occur. Taken with the infinite bound, this proves both the exceptional-prime classification and the optimal universal threshold.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It enumerates all 368 odd primes below \(2529\) using an integer sieve and every residue class for each prime. It calculates the word histograms by both quadratic-residue lookup and Euler's criterion and checks equality, the complete exception set, and the sharp boundary. The deterministic digest of the ordered prime histograms is `194838fb1badf1f21c7f2a978cef964c71d50b13656a9a1537bd30f09ea254aa` (SHA-256). This finite verification proves the finite range by exhaustive enumeration only; the Weil estimate above proves the infinite range.

## Relationship to prior work
Liu and Meng (2023) analyze quadratic-residue triples of the form \(a,a+a^{-1},a-a^{-1}\) and obtain Gauss-sum identities. Wang and Fang (2023) analyze consecutive residue/nonresidue arithmetic progressions of *linear* arguments. Their character-sum techniques motivate studying a different natural sequence, the quadratic Gaussian norms \((x+j)^2+1\), whose four ordered signs need not form a linear progression in the character arguments. Neither inspected article supplies this exact sixteen-word exceptional-prime set or the sharp cutoff; the proof uses the standard quadratic-character bound together with a complete finite census. The character indicator method and Weil's inequality are classical and are not presented as original.

## Limitations
The result concerns four fixed consecutive Gaussian norms only. It gives the full existence spectrum in the prime parameter, not closed expressions for individual word frequencies, higher word lengths, or composite moduli. Its small-prime classification depends on a finite exhaustive computation, included in a standalone script; no claim is made that a symbolic argument characterizes the sixteen exceptional primes individually. The discovery of unindexed equivalent work remains possible. This is a mathematical proof with finite computation, not independent external certification.

## References
- Xiaoge Liu and Yuanyuan Meng, “On the quadratic residues and their distribution properties,” *Open Mathematics* **21** (2023), article 20230123, first public September 26, 2023. https://doi.org/10.1515/math-2023-0123
- Xiao Wang and Hao Fang, “The Distribution Properties of Consecutive Quadratic Residue Sequences,” *Journal of Mathematics* (2023), article 5253261, first published October 3, 2023. https://doi.org/10.1155/2023/5253261
- A. Weil, classical bound for multiplicative character sums of squarefree polynomials over finite fields (standard theorem, used as stated in the proof).
