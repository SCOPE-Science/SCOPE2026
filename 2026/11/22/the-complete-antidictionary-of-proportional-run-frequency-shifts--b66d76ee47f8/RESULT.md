# The complete antidictionary of proportional-run frequency shifts

## Finding
For every integer \(k\ge1\), consider the two-sided binary coded subshift \(X_k\) whose finite language comprises all factors of concatenations of the generator words \(0^m1^{km}\), \(m\ge1\). Its complete set \(\mathcal M_k\) of *minimal absent contiguous factors* is exactly the following disjoint union:

\[
\mathcal M_k=\{01^r0:r\ge1,\ k\nmid r\}\ \cup\ \{10^m1^{km+1}:m\ge1\}\ \cup\ \{0^{m+1}1^{km}0:m\ge1\}.
\]

The number \(a_k(n)\) of these words of length \(n\) is zero for \(n<3\), and for \(n\ge3\) equals

\[
a_k(n)=\mathbf1_{k\nmid(n-2)}+2\mathbf1_{n\ge k+3,\ (k+1)\mid(n-2)}.
\]

In particular \(a_k(n)\le3\), and its exact length generating function is

\[
\sum_{n\ge0}a_k(n)z^n=\frac{z^3}{1-z}-\frac{z^{k+2}}{1-z^k}+\frac{2z^{k+3}}{1-z^{k+1}}.
\]

For every \(k\), the minimal-forbidden language is nonregular and has zero exponential growth entropy (its cumulative number of forbidden words through length \(N\) is \(O(N)\)).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), \(k\) is any positive integer, and the generator index \(m\) ranges over all positive integers. A finite word is admissible precisely when it occurs as one contiguous factor of a *finite* concatenation of the generators (equivalently, in a point of the coded shift closure). A minimal absent word is absent, while each nonempty proper contiguous factor is present. All formulas describe **contiguous** factors, not scattered subsequences or maximal-entropy-measure probabilities.

## Proof
**Admissible-run constraints.** In a concatenation of generators, every complete \(1\)-run bounded on both sides by zeros has length \(km\) for some \(m\ge1\). Its immediately preceding \(0\)-run, if complete, must have length exactly \(m\). This yields three obstructions. First, \(01^r0\) is absent if \(k\nmid r\). Second, \(10^m1^{km+1}\) is absent because the complete zero-run of length \(m\) would require a following one-run of exactly \(km\). Third, \(0^{m+1}1^{km}0\) is absent because a completed one-run of length \(km\) has a preceding zero-run of exactly \(m\), even if the observed zero-run is only a suffix of that zero-run. (A suffix cannot be longer than its containing run.)

**Each obstruction is minimal.** Deleting the first or last symbol from any word in the three families produces a factor of a generator concatenation: for the first family, the two resulting proper factors are \(1^r0\) and \(01^r\), each embeddable by enlarging the generating run. For the second family, removing the initial \(1\) gives an initial zero-run followed by an arbitrarily long (possibly unfinished) one-run, and removing the last \(1\) gives \(10^m1^{km}\), contained in \(0^a1^{ka}0^m1^{km}\) for any \(a\ge1\). For the third family, removing its initial \(0\) yields \(0^m1^{km}0\), while removing its final \(0\) yields \(0^{m+1}1^{km}\), both admissible. Every other proper contiguous subword is contained in one of these two proper factors.

**No other obstruction exists.** Let \(w\) avoid all three families. Decompose \(w\) into alternating maximal zero- and one-runs. Any one-run enclosed between zeros must have length a positive multiple of \(k\), by absence of the first family. Suppose such a run has length \(km\) and the zero-run immediately preceding it has visible length \(a\). The absence of family three implies \(a\le m\). If this zero-run is *complete in* \(w\) (preceded by a one), the absence of family two also implies \(m\le a\); hence \(a=m\). If it is the first, left-truncated zero-run of \(w\), extend it to total length \(m\). For a terminal one-run following a complete zero-run of length \(a\), the absence of family two implies its visible length is at most \(ka\); enlarge it on the right to length \(ka\). For a terminal one-run following the first left-truncated zero-run, enlarge the zero-run enough to support the visible ones. An initial one-run can be supplied with a suitable preceding full zero-run and then joined to the subsequent zero-run through a generator boundary; a final zero-run can be completed and followed by its matching one-run. This produces a concatenation of generators containing \(w\). Thus every absent word contains a member of the displayed family. Combined with minimality, the family equals the full minimal antidictionary.

**Counting and nonregularity.** The first family contributes one word at each length \(r+2\) when \(k\nmid r\). Each of the last two families has length \((k+1)m+2\), and all three families are distinct by their end symbols/initial run structure. Summation yields the stated rational series and the bound three. Intersecting \(\mathcal M_k\) with the regular language \(10^+1^+\) gives exactly \(\{10^m1^{km+1}:m\ge1\}\), which is nonregular by the pumping lemma (or intersection with a regular length-filter, since the two run lengths obey an unbounded exact linear relation). Hence \(\mathcal M_k\) is nonregular. The bounded per-length count gives growth entropy zero.

## Verification
An independently written finite-language checker enumerates all admissible binary words of lengths \(1\) through \(12\) for each \(k\in\{1,2,3,4\}\), using bounded-state generation from generator concatenations, then matches each language against avoidance of the three proposed families. The included `checker.py` reproduces this finite consistency test; the all-length theorem rests on the run-extension proof, not on finite enumeration.

## Relationship to prior work
The proportional-run coded shifts appear in C. Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity* (2026), which analyzes their entropy and intrinsic ergodicity and records forbidden gaps \(01^r0\) with \(k\nmid r\). The other two boundary-obstruction families, the complete minimality characterization, and the all-parameter exact length series are the present claim; the earlier entropy and uniqueness properties are **not** newly claimed here. Wu and Zhang's *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts* (2026) motivates counting minimal forbidden words by length. General antidictionary theory is classical; no priority claim is made for that framework.

## Limitations
This determines only the complete minimal forbidden factors of this explicitly defined family, not other frequency shifts or scattered-subsequence avoidance. The length series is an exact counting statement, not a general formula for the topological entropy or number of maximal-entropy measures; those questions are addressed in the motivating literature. Historical unindexed equivalents remain a priority uncertainty, and no independent audit has been performed.

## References
- C. Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity*, arXiv:2611.10995 (first made public 2026-11-07), https://arxiv.org/abs/2611.10995.
- Wu and Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758 (first made public 2026-11-02), https://arxiv.org/abs/2611.03758.
- M. Crochemore, F. Mignosi, A. Restivo, *Automata and Forbidden Words*, Information Processing Letters 67 (1998), 111–117, general background.
