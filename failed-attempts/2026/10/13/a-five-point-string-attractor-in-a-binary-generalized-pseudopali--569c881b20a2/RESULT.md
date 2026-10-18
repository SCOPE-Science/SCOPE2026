# A five-point string attractor in a binary generalized pseudopalindromic prefix

## Finding

There is a binary generalized pseudostandard word with a pseudopalindromic prefix whose minimum *full* string-attractor size is five. Specifically, applying the directive pair \(\Delta=\mathtt{10111}\), \(\Theta=\mathtt{EEERE}\) gives the length-\(44\) word
\[
W=\mathtt{10011010011011001011001100101100100110100110},
\qquad \gamma(W)=5.
\]
A zero-based minimum attractor is \(\Gamma=\{9,16,23,33,39\}\). This is a counterexample to the upper-bound-four conjecture about binary generalized pseudostandard pseudopalindromic prefixes explicitly stated by Dvořáková and Hendrychová in Section 7 of [1].

## Assumptions and scope

The alphabet is \(\{0,1\}\). Write \(R(x)\) for reversal and \(E(x)\) for reversal followed by exchanging \(0\) with \(1\). For \(\theta\in\{R,E\}\), define \(x^\theta\) as the shortest word beginning with \(x\) fixed by \(\theta\). Equivalently, if \(z\) is the longest suffix of \(x\) fixed by \(\theta\), write \(x=uz\) and set \(x^\theta=uz\theta(u)\). The empty suffix is allowed. Define \(w_0=\varepsilon\) and \(w_i=(w_{i-1}\delta_i)^{\vartheta_i}\), with the five prescribed directive pairs. The finite directive can be extended arbitrarily to an infinite one; hence the generated \(w_5\) is a pseudopalindromic prefix of an infinite generalized pseudostandard sequence in the sense of [1, Definition 3].

For a finite nonempty word \(x\), a *full string attractor* \(\Gamma\subseteq\{0,\ldots,|x|-1\}\) meets an occurrence of every distinct nonempty factor of \(x\). More precisely, for a factor \(f\), put
\[
S_x(f)=\bigcup_{i:\,x[i:i+|f|]=f}\{i,i+1,\ldots,i+|f|-1\}.
\]
Then \(\Gamma\) is an attractor exactly when \(\Gamma\cap S_x(f)\ne\varnothing\) for every nonempty factor \(f\). Let \(\gamma(x)\) be the minimum cardinality of such a set.

## Proof

**Closure construction.** Direct application of the longest fixed-suffix rule gives these five successive output lengths and longest fixed-suffix lengths:

| Step | Directive letter | Antimorphism | Longest fixed-suffix length | Output length |
|---:|:---:|:---:|---:|---:|
| 1 | `1` | `E` | 0 | 2 |
| 2 | `0` | `E` | 0 | 6 |
| 3 | `1` | `E` | 2 | 12 |
| 4 | `1` | `R` | 3 | 23 |
| 5 | `1` | `E` | 4 | 44 |

The resulting prefixes are `10`, `100110`, `100110100110`, `10011010011011001011001`, and the displayed \(W\). Every fixed-suffix maximum, closure equality and complete prefix is independently recalculated by the accompanying standard-library checker.

**Lower bound.** In the following table the positions are zero-based; the listed factor occurrences are **all** occurrences in \(W\):

| Factor | Start positions | All positions belonging to its occurrences |
|:---|:---|:---|
| `1010` | 4, 36 | 4–7, 36–39 |
| `11011` | 9 | 9–13 |
| `00100` | 30 | 30–34 |
| `110011` | 18 | 18–23 |
| `0101` | 15, 25 | 15–18, 25–28 |
| `001100` | 20 | 20–25 |

The support sets for the first four factors are pairwise disjoint. Therefore any four-point attractor must put exactly one point in each of these four sets. The support for `0101` intersects the first three support sets nowhere and intersects the fourth only at position \(18\). Thus the point selected from the fourth set must be \(18\). However, the support for `001100` also misses the first three sets and intersects the fourth only at \(\{20,21,22,23\}\). The fourth point would have to lie in that disjoint set as well, a contradiction. Therefore \(\gamma(W)\ge5\). This is an elementary six-factor certificate, not an inference from optimization failure.

**Upper bound.** Take \(\Gamma=\{9,16,23,33,39\}\). The maximum length of a consecutive run of positions avoiding \(\Gamma\), including the two boundary runs, is \(9\). Thus every occurrence of every factor of length at least \(10\) crosses \(\Gamma\). It remains to verify only factor lengths \(1,\ldots,9\). The following exact counts give, at each length, (i) the number of all distinct factors of \(W\), and (ii) the number with at least one occurrence crossing \(\Gamma\):

| Length | All factors | Factors crossing an attractor position |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 4 | 4 |
| 3 | 6 | 6 |
| 4 | 10 | 10 |
| 5 | 14 | 14 |
| 6 | 18 | 18 |
| 7 | 22 | 22 |
| 8 | 25 | 25 |
| 9 | 28 | 28 |

The checker enumerates the actual factor sets and asserts equality, rather than merely comparing counts. Thus \(\Gamma\) is a full string attractor and \(\gamma(W)\le5\). Together with the lower bound, \(\gamma(W)=5\).

## Verification

Run the included `verify.py` with Python 3 and no external packages. It independently generates all five closures by checking **every** candidate suffix length; verifies the exact word, every occurrence in the six-factor lower certificate, the disjoint-support contradiction, and all \(1{,}200\) possible four-point selections forced by the first four factors. It also verifies the proposed five-set against **every** distinct factor of lengths \(1\) through \(9\). The bound on unmarked runs treats all longer factors. No probabilistic or numerical-optimization assumptions are needed.

## Relationship to prior work

Dvořáková and Hendrychová [1] define binary generalized pseudostandard sequences through alternating choices of palindromic and antipalindromic closure (their Definition 3). In Section 7 they conjecture that every pseudopalindromic prefix in this class has a string attractor with at most four positions. The present explicitly constructed prefix, with \(\gamma(W)=5\), directly negates that universal conjecture; it does not reprove their positive theorems for special subclasses. Earlier exact results on Thue–Morse prefixes [2, 3] and on factors of Thue–Morse [4] concern narrower fixed languages and do not establish a universal bound for arbitrary generalized pseudostandard prefixes. In particular, the five-position phenomenon for some Thue–Morse *factors* in [4] does not supply this specific pseudopalindromic-closure counterexample.

## Limitations

The theorem identifies one explicit length-\(44\) counterexample. It does **not** claim that \(44\) is the smallest possible counterexample length, that five is the maximum size for all generalized pseudostandard pseudopalindromic prefixes, or that this word represents an entire classification. The upper witness is verified by finite exhaustive factor enumeration, which is conclusive for the given finite word but does not establish properties of other words. Literature searches cannot exclude all unindexed earlier equivalents.

## References

[1] Ľ. Dvořáková and V. Hendrychová, *String attractors of Rote sequences*, arXiv:2308.00850, first publicly posted 2023-08-01; final public version v5, 2024-09-15. Definition 3 and Section 7. Published in *Discrete Mathematics & Theoretical Computer Science* 26:3 (2024), DOI:10.46298/dmtcs.12385.

[2] K. Kutsukake, T. Matsumoto, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *On repetitiveness measures of Thue–Morse words*, arXiv:2005.09524v3 (2020), Theorem 3.3.

[3] L. Schaeffer and J. Shallit, *String attractors for automatic sequences*, arXiv:2012.06840v6 (2024), Sections 2–4.

[4] F. Dolce, *String attractors for factors of the Thue–Morse word*, *Combinatorics on Words*, LNCS 13899 (2023), 117–129, DOI:10.1007/978-3-031-33180-0_9, Theorem 1 and Example 5.
