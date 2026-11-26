# Sharp reverse-isolation threshold and complete reflection complexity of a ternary morphic word

## Finding

Let \(h(0)=01\), \(h(1)=21\), and \(h(2)=0\), and let \(p=h^{\omega}(0)\) be the infinite fixed point beginning \(012102101021\cdots\). Write \(F_n(p)\) for the set of all length-\(n\) contiguous factors, and let \(\widetilde{u}\) denote the reversal of the finite word \(u\). Define the set of *reflected* factors \(Q_n=\{u\in F_n(p):\widetilde u\in F_n(p)\}\), and define the reflection complexity \(r_p(n)\) to be the number of equivalence classes of \(F_n(p)\) under the identification of a factor with its reversal whenever that reversal also occurs.

**Theorem.** The reflected sets, for lengths \(1\) through \(7\), are exactly:

| \(n\) | \(Q_n\) |
| --- | --- |
| 1 | `0`, `1`, `2` |
| 2 | `01`, `10`, `12`, `21` |
| 3 | `010`, `012`, `101`, `121`, `210` |
| 4 | `0121`, `1012`, `1210`, `2101` |
| 5 | `01210`, `10121`, `12101`, `21012` |
| 6 | `012101`, `101210` |
| 7 | `1012101` |

For every integer \(n\ge8\), one has \(Q_n=\varnothing\). The threshold \(8\) is sharp because \(Q_7\ne\varnothing\). Moreover, with \(r_p(0)=1\), the *entire* reflection-complexity sequence is

\[
r_p(n)=\begin{cases}
1,&n=0,\\
3,3,6,7,10,12,15,&n=1,2,3,4,5,6,7\text{ respectively},\\
2n+1,&n\ge8.
\end{cases}
\]

This determines not only which palindromes appear (already known), but also every distinct nonpalindromic pair of mutually reversed factors.

## Assumptions and scope

All words use the fixed, labeled alphabet \(\{0,1,2\}\); reversal is ordinary order reversal, without a letter permutation. All factors are contiguous. The one-sided infinite word is uniquely determined as the limit of \(h^k(0)\); the morphism is non-erasing and prolongable on \(0\). Every assertion about factors is over the entire infinite word, not a bounded prefix.

## Proof

**Step 1: An explicit finite factor set.** A direct sixfold substitution gives the 37-letter prefix

`0121021010210121010210121021012101021`.

Take its distinct length-eight factors; the resulting set \(\mathcal F\) contains exactly the following 17 words, in lexicographic order:

```
01021012
01210102
01210210
02101021
02101210
10102101
10121010
10121021
10210102
10210121
12101021
12102101
21010210
21012101
21012102
21021010
21021012
```

**Step 2: A finite substitution-closure certificate.** For each of these 17 words \(u\), every length-eight factor of the finite word \(h(u)\) again belongs to \(\mathcal F\). This is a finite statement about 119 windows, obtained by applying the three explicit replacement rules and comparing with the displayed sorted list. The complete independently executable check is `verify.py`, which recreates the list and tests every relevant window rather than assuming the list. No approximation or sampling is involved in this step.

**Step 3: The finite certificate covers the infinite word.** Since \(h^6(0)\) is a prefix of the infinite fixed point, \(\mathcal F\subseteq F_8(p)\). We now prove the opposite inclusion. For every finite input word \(v\) of length at least eight with \(F_8(v)\subseteq\mathcal F\), consider an arbitrary eight-letter factor \(z\) of \(h(v)\). Each letter image is nonempty, so the window \(z\) intersects images of at most eight consecutive letters of \(v\). Extend those letters within \(v\) to a length-eight block \(u\). Thus \(z\) is a length-eight factor of \(h(u)\), with \(u\in\mathcal F\); the closure certificate gives \(z\in\mathcal F\). Starting from \(v=h^6(0)\) and iterating proves \(F_8(h^k(0))\subseteq\mathcal F\) for all \(k\ge6\). Any finite factor of \(p\) occurs in some finite iterate, hence \(F_8(p)=\mathcal F\).

**Step 4: Sharp reverse isolation.** Direct comparison of each of the 17 explicit words with its reversed spelling shows \(\mathcal F\cap\widetilde{\mathcal F}=\varnothing\). Suppose, for contradiction, that a factor \(w\) of length \(n\ge8\) and its reversal both appear in \(p\). Choose any length-eight subword \(v\) of \(w\). Then \(v\) occurs in \(w\), and \(\widetilde v\) occurs in \(\widetilde w\), contradicting the disjointness of \(F_8(p)\) and its reversal. Therefore \(Q_n=\varnothing\) for all \(n\ge8\).

**Step 5: All shorter lengths.** Each finite factor of length \(n<8\) can be extended rightwards inside the infinite word to a length-eight factor. Consequently \(F_n(p)\) is exactly the set of length-\(n\) subwords of the 17 words in \(\mathcal F\). Exhaustive set comparison yields the reflected sets in the theorem. The following table also records \(P_n\), the number of palindromic factors of length \(n\):

| \(n\) | \(|F_n(p)|\) | \(|Q_n|\) | \(P_n\) | \(r_p(n)\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 3 | 3 | 3 |
| 2 | 5 | 4 | 0 | 3 |
| 3 | 7 | 5 | 3 | 6 |
| 4 | 9 | 4 | 0 | 7 |
| 5 | 11 | 4 | 2 | 10 |
| 6 | 13 | 2 | 0 | 12 |
| 7 | 15 | 1 | 1 | 15 |
| 8 | 17 | 0 | 0 | 17 |

For any language of factors, reversing pairs of nonpalindromic factors into two-element classes gives

\[
r_p(n)=|F_n(p)|-\frac{|Q_n|-P_n}{2}.
\]

The short values now follow from the table. For \(n\ge8\), the just-proved \(Q_n=\varnothing\) yields \(r_p(n)=|F_n(p)|\). Finally, Currie, Ochem, Rampersad and Shallit prove \(|F_n(p)|=2n+1\) for every \(n\ge1\) [1, Theorem 1]. This published factor-complexity theorem supplies the closed numerical expression in the last line. The empty word supplies \(r_p(0)=1\). This completes the proof.

## Verification

Run `python3 verify.py` using only the Python standard library. It reconstructs \(h^6(0)\), checks the complete 17-word set, tests each of the 119 substitution-closure windows, checks the exact reflected sets and palindromic counts through length eight, and recomputes the reflection-complexity table. It additionally checks stabilization of length-eight factors through five further substitution iterates, as a redundant finite consistency test. Successful output begins `VERIFY_OK`. The infinite part follows from the proved substitution-closure induction, not from the longer-prefix checks. The numerical formula for high lengths uses [1, Theorem 1] and is not re-proved computationally.

## Relationship to prior work

The 2022 primary analysis of this same word [1] proves its factor complexity \(2n+1\), and its Theorem 6 already provides the complete list of its nine palindromic factors. Neither result alone determines the nonpalindromic reverse pairs, which are present at lengths two through six. Palindrome enumeration is therefore credited as prior work, not offered as an independent discovery here. Its other inspected results about avoided factors also do not list a reflection complexity spectrum.

The 2024 reflection-complexity theory [2, Theorem 11] shows that a uniformly recurrent sequence lacking reversal closure has no *sufficiently long* reflected factors. It does not specify the least such length for this word or enumerate the exceptional reflected factors. The new content here is the exact sharp threshold eight and the full numerical reflection complexity at *every* length, supported by an explicit finite substitution-closure certificate. No claim of independent verification or guaranteed bibliographic uniqueness is made.

## Limitations

The result applies only to the indicated morphism and ordinary, letter-preserving reversal. It is not a classification of all ternary morphic words. It depends on the published factor-complexity result [1] for the closed form \(2n+1\) at arbitrary lengths. Although checked against the identified primary sources and relevant research records, an unindexed equivalent reverse-pair computation remains a bibliographic possibility. No independent scientific audit has been performed.

## References

[1] J. Currie, P. Ochem, N. Rampersad and J. Shallit, *Properties of a Ternary Infinite Word*, arXiv:2206.01776 (first public version June 3, 2022), especially Theorems 1, 6 and 14. https://arxiv.org/abs/2206.01776

[2] J.-P. Allouche, D. Campbell, S. Li, J. Shallit and M. Stipulanti, *The Reflection Complexity of Sequences over Finite Alphabets*, arXiv:2406.09302 (first public version June 13, 2024), especially Theorem 11. https://arxiv.org/abs/2406.09302
