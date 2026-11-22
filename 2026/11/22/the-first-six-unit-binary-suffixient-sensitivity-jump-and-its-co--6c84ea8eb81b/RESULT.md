# The first six-unit binary suffixient sensitivity jump and its complete length-fourteen extremizers

## Finding

For every nonempty binary word \(w\) and index \(i\), write \(w^{(i)}\) for the word obtained by flipping just the \(i\)-th bit. Let \(\chi(w)\) denote the minimum cardinality of a suffixient set for the terminated word \(w\texttt{\$}\). Define the one-substitution additive sensitivity

\[
A(n)=\max_{w\in\{0,1\}^n}\max_{1\le i\le n}\bigl(\chi(w^{(i)})-\chi(w)\bigr).
\]

**Finite exact theorem.** For \(1\le n\le14\), the profile is

\[
\bigl(A(1),A(2),\ldots,A(14)\bigr)
=(0,1,1,1,2,2,3,4,4,4,4,5,5,6).
\]

The first length where a substitution increases \(\chi\) by at least six is **14**. At that length precisely **16 directed pairs** attain the maximum six-unit increase, and all of them have \(\chi(w)=5\) and \(\chi(w^{(i)})=11\). The complete set of lower-measure words and allowable one-based flip positions is:

| Lower word | Flip positions |
|---|---|
| `01111000111100` | 3, 4, 10, 11 |
| `01111001111000` | 3, 4, 9, 10 |
| `10000110000111` | 3, 4, 9, 10 |
| `10000111000011` | 3, 4, 10, 11 |

For example, flipping position 11 in `01111000111100` produces `01111000110100` and raises \(\chi\) from five to eleven.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); only one substitution of a symbol by the other binary symbol is permitted, not insertion, deletion or reversal. The unique terminator `\$` is not counted in the source length, and is not substituted. All positions above are one-based. A pair \((w,w^{(i)})\) is *directed*: its increase is the target measure minus the source measure. The theorem covers all words of lengths 1 through 14 and makes no extrapolation to longer lengths or larger alphabets.

For a terminated word \(s=w\texttt{\$}\), a (possibly empty) factor \(u\) is *right-maximal* if distinct symbols \(a,b\in\{0,1,\texttt{\$}\}\) occur immediately after two occurrences of \(u\). A *right extension* is any appearing \(ua\) with right-maximal \(u\). A *supermaximal right extension* is a right extension that is not a proper suffix of any other right extension. The standard identity \(\chi(w)=|\mathcal S_r(w\texttt{\$})|\) is used throughout [1].

## Proof

**Lemma 1 (exhaustive factor characterization).** Form the finite set \(E(s)\) of all distinct right extensions in \(s\). Then

\[
\chi(w)=\left|\{e\in E(s):e\text{ is not a proper suffix of any }f\in E(s)\}\right|.
\]

This is the characterization of minimum suffixient-set size by supermaximal right extensions [1, Definitions 1–5]. Every right extension is a suffix of some inclusion-maximal right extension, and two distinct inclusion-maximal right extensions cannot be suffixes of the same prefix-ending word; choosing one occurrence-ending position for each therefore gives the minimum. The construction is finite because every right extension is a factor of \(s\).

**Lemma 2 (one-letter test).** A right extension \(e\) is a proper suffix of some other right extension if and only if there is a letter \(a\in\{0,1\}\) for which \(ae\) is a right extension. The backward implication is immediate. For the forward implication, write the longer right extension as \(ve\) and take the last letter \(a\) of the nonempty prefix \(v\). The prefix of \(ve\) excluding its last symbol has at least two different following symbols, so every suffix of that prefix also has those two following symbols. In particular, \(ae\) is a right extension. This proves that the local one-letter test is sufficient. The terminal symbol cannot be the extra preceding letter, because it occurs only once at the end of \(s\).

**Finite exhaustion.** The bundled file `verify_suffixient.cpp` implements two independently organized exact versions of Lemma 1. The first enumerates all occurrence-followers of every factor, constructs right extensions, and applies Lemma 2. The second enumerates distinct positive-length factors, explicitly scans occurrences to determine their right-maximal prefixes, and applies all-length proper-suffix comparison. It checks that both computations agree for **every** one of the \(\sum_{n=1}^{14}2^n=32{,}766\) source words.

For each \(n\), it then evaluates the difference \(\chi(w^{(i)})-\chi(w)\) for all \(n2^n\) directed bit flips. Every pair is covered because the bit-mask loops visit all source masks and all bit indices. The finite search consists of \(\sum_{n=1}^{14}n2^n=425{,}986\) directed substitutions. The maximal differences are, in increasing length order, exactly the values in the finding. Thus the first six-unit jump cannot occur earlier than length fourteen, and it does occur there.

For length fourteen the verifier prints **all** pairs having increase six. Its 16 output lines have exactly the four lower words and their indicated flip-position sets. Every line reports the low and high values five and eleven. Completeness of both the upper bound and the optimizer classification follows from visiting every binary source and every allowable substitution, not from sampling.

**Additional independent witness check.** The bundled `verify_positions.py` constructs right extensions for four distinct representative source/target pairs and tests **every** subset of the fifteen positions of each terminated word. For the lower words it obtains a minimum of five positions (four minimum sets in each example); for their chosen upper words it obtains eleven (two minimum sets each). This checks the measure directly through the defining suffix-coverage property, rather than exclusively through the supermaximal-extension formula. Its verification is supplementary; full finite completeness is supplied by the C++ enumeration.

## Verification

Compile with `g++ -std=c++17 -O2 verify_suffixient.cpp -o verify_suffixient` and run `./verify_suffixient`, or use a compatible C++17 compiler. Run `python3 verify_positions.py` separately. The exact output for both is included in `verify_suffixient.out` and `verify_positions.out`. The C++ program aborts if its two independent finite measure computations disagree on any source word; the output contains the complete length profile and all sixteen extremal directed pairs. The separate Python check exhausts all possible position sets on its displayed witnesses. Both verifiers were executed from the packaged source and their outputs compared byte-for-byte with the included outputs.

## Relationship to prior work

Fujimaru, Navarro, Romana and Urbina [1] introduce and study the exact same measure and its edit sensitivity, obtaining an asymptotic lower bound of order \(\sqrt n\) under a single substitution. Their general result, construction and proof do not supply the *finite binary* sensitivity values through length fourteen, the first occurrence of a six-unit increase, or the classification of every equality case. The present theorem is a finite exact refinement of that sensitivity question, **not** a new asymptotic bound. Cenzato, Olivares and Prezza [2] analyze how to test suffixient and minimum suffixient sets, without this binary substitution-sensitivity census. Köppl and Kucherov [3] develop online maintenance algorithms for smallest suffixient sets, rather than this finite extremal profile.

## Limitations

The result is a fully finite exhaustive theorem; the listing is a computer-assisted proof with an independently cross-checked measurement routine. It does not assert any closed formula or universal threshold beyond fourteen, and does not imply a universal multiplicative bound on edit sensitivity. The exact equality classification concerns directed increases and does not count reversed directed edges as new positive examples. Historical priority may be affected by an unindexed equivalent enumeration, even though no equivalent result was found in the inspected primary sources.

## References

1. H. Fujimaru, G. Navarro, G. Romana, C. Urbina, *Smallest Suffixient Sets: Effectiveness, Resilience, and Calculation*, arXiv:2506.05638 (first public version 2025-06-05), especially Definitions 1–5 and Section 4. https://arxiv.org/html/2506.05638v7
2. D. Cenzato, F. Olivares, N. Prezza, *Testing Suffixient Sets*, arXiv:2506.08225 (first public version 2025-06-09), especially Sections 2–3. https://arxiv.org/html/2506.08225v2
3. D. Köppl, G. Kucherov, *Smallest Suffixient Set Maintenance in Near-Real-Time*, MFCS 2026, Article 86, DOI 10.4230/LIPIcs.MFCS.2026.86. https://drops.dagstuhl.de/storage/00lipics/lipics-vol386-mfcs2026/html/LIPIcs.MFCS.2026.86/LIPIcs.MFCS.2026.86.html
