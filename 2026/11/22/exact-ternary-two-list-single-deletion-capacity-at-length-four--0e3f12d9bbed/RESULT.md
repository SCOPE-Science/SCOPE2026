# Exact ternary two-list single-deletion capacity at length four

## Finding

A **ternary length-four single-deletion code with list bound two** is a set \(C\subseteq\{0,1,2\}^4\) such that each three-letter received word is obtained by deleting exactly one position from at most two members of \(C\). The exact maximum is

\[
\boxed{\max |C|=21.}
\]

A concrete optimal code is

```
0000 0011 0022 0120 0121 0210 1001 1022 1100 1110 1111
1122 1201 2000 2002 2102 2112 2201 2211 2220 2222
```

Every three-letter word appears as a one-deletion output of **exactly two** members of this code. The code is not a union of two uniquely single-deletion-decodable codes: its pairwise-conflict graph contains a triangle on `0120`, `0121`, `0210`.

## Assumptions and scope

The alphabet is \(\Sigma=\{0,1,2\}\). All words are ordered, fixed-length strings, not multisets or cyclic words. Deletions remove precisely one symbol at an arbitrary coordinate. For a word \(w\in\Sigma^4\), let \(D(w)\subseteq\Sigma^3\) be the **set of distinct** words obtained from its four possible single-coordinate deletions; repeated outputs are counted only once. The decoding requirement is

\[
\forall y\in\Sigma^3,\qquad |\{w\in C:y\in D(w)\}|\le2.
\]

As all source words have length four, a zero-deletion read identifies its source uniquely, so the same optimum applies to a channel allowing **at most** one deletion. No claim concerns longer block lengths, larger alphabets, multiple deletions, or larger list allowances.

## Proof

**Upper bound.** Assign the following nonnegative weights to each output \(y=y_1y_2y_3\):

\[
\lambda(y)=\begin{cases}
5/8,&y_1=y_2=y_3,\\
3/8,&\text{exactly one adjacent pair agrees},\\
1/4,&\text{neither adjacent pair agrees}.
\end{cases}
\]

For each input \(w=w_1w_2w_3w_4\), assign

\[
\mu(w)=\begin{cases}
3/8,&w=aaaa,\\
1/4,&w=aabb\text{ with }a\ne b,\\
0,&\text{otherwise}.
\end{cases}
\]

For **every** \(w\in\Sigma^4\),

\[
\sum_{y\in D(w)}\lambda(y)+\mu(w)\ge1.\tag{1}
\]

This is an exhaustive ten-case equality-pattern check: the weights and deletion shadows are invariant under symbol permutation and word reversal. The table enumerates all orbits; its columns give a representative, number of labeled words, and the exact left side of (1):

| Representative | Orbit size | Left side of (1) |
|---|---:|---:|
| `0000` | 3 | \(1\) |
| `0001` | 12 | \(1\) |
| `0010` | 12 | \(5/4\) |
| `0011` | 6 | \(1\) |
| `0012` | 12 | \(1\) |
| `0101` | 6 | \(5/4\) |
| `0102` | 12 | \(9/8\) |
| `0110` | 6 | \(1\) |
| `0112` | 6 | \(1\) |
| `0120` | 6 | \(1\) |

The orbit sizes sum to \(81=3^4\), so the check covers every input. Directly counting the three constant outputs, twelve outputs with exactly one adjacent equality, and twelve others gives

\[
\sum_{y\in\Sigma^3}\lambda(y)=3(5/8)+12(3/8)+12(1/4)=75/8.
\]

Only the three constant inputs and six `aabb` inputs have nonzero \(\mu\), hence

\[
\sum_{w\in\Sigma^4}\mu(w)=3(3/8)+6(1/4)=21/8.
\]

Summing (1) over an arbitrary valid code \(C\), interchanging sums, using the two-list constraint, and using \(\mu\ge0\), yields

\[
|C|\le \sum_{y\in\Sigma^3}\lambda(y)|\{w\in C:y\in D(w)\}|+\sum_{w\in C}\mu(w)
\le 2(75/8)+21/8=171/8<22.
\]

Since \(|C|\) is integral, \(|C|\le21\).

**Lower bound.** The 21 distinct words displayed above each have their deletion shadow defined by four literal coordinate removals. Directly listing all 27 possible three-letter words and counting each word's distinct source codewords shows that every output has incidence **exactly two**. Thus the code meets the upper bound.

**Nondecomposability of this witness.** The deletion shadows of `0120`, `0121`, and `0210` pairwise intersect. Specifically, `012` is common to the first two, `021` to the second and third, and `010` and `020` to the first and third. Their triple intersection is empty, consistent with list size two. If the code were the union of two uniquely single-deletion-decodable subcodes, these three pairwise conflicting words would require three different subcode colors, which is impossible with two colors.

## Verification

The standalone standard-library Python program `verify.py` checks all \(81\) input inequalities as exact rational arithmetic, independently verifies the ten symmetry orbits and their complete coverage, computes the two weight sums, and tests the displayed 21-word code against **each of the 27 outputs**. It additionally checks the conflict triangle. Running `python3 verify.py` reproduces `verification_output.txt`. The proof itself is the explicitly tabulated exhaustive finite classification, rational summation, and witness; no floating-point optimization or opaque solver success is needed.

## Relationship to prior work

Kiah, Wei and Zeng (first public version 18 September 2026; later revised) study constant-list insertion–deletion coding bounds. Their revised preprint's Theorem 28 gives a general finite-length run-counting upper bound; at the present parameters, its choices of run cutoff yield upper bounds no smaller than \(30\), not the sharp \(21\). Lin's 22 September 2026 preprint concentrates on asymptotic **binary** list-decodable deletion codes. A separate published ternary length-four uniquely decodable result gives maximum \(11\), but this does not imply the list-two optimum: two disjoint such codes could only give a comparison of \(22\), while an arbitrary list-two code need not be their union. The present certificate proves the strict \(21\) bound and supplies a two-fold-exact, nondecomposable optimum.

## Limitations

The theorem is exact only for the stated short-block ternary model; the existence of a length-four optimum does not determine large-block rates. Originality is assessed against the identified publications and accessible records, not as a claim of exhaustive indexing. In particular, an unindexed equivalent small-parameter table remains a potential priority risk. The second preprint was only accessible in abstract form in this literature inspection; its stated results are binary. Independent validation has not been performed.

## References

1. H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395, first public version 2026-09-18; revised as *Exponentially Larger Deletion-Correcting Codes and Constant-List-Decodable Insertion-Deletion Codes*, version 2, 2026-11-01. https://arxiv.org/abs/2609.21395
2. A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, first public version 2026-09-22. https://arxiv.org/abs/2609.26650
3. *Exact ternary length-four single-deletion code size*, published mathematical result, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ternary-length-four-single-deletion-code-size--6adacbb5cb97
4. *First nondecomposable two-list single-deletion codebooks at length seven*, published mathematical result for the binary alphabet, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-nondecomposable-two-list-single-deletion-codebooks-at-leng--fcf59d2e1812
