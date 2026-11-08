# Exact finite threshold for three distinct 2-binomial squares in binary words

## Finding

For a binary word \(w\), let \(\mathcal S_2(w)\) be the **set of distinct nonempty contiguous factors** \(uv\) of \(w\) such that \(u\) and \(v\) have the same positive length and are 2-binomially equivalent. This means that, for every binary word \(z\) of length at most two, the numbers of scattered subsequence occurrences of \(z\) in \(u\) and \(v\) agree. A factor is counted once as a literal word, no matter how often or where it occurs.

**Theorem.** The largest length of a binary word \(w\) with \(|\mathcal S_2(w)|\le3\) is exactly \(43\). Exactly four labeled binary words attain this length:

```
0010001110001011000111001011100010110001101
0100111001011100010110001110010111000111011
1011000110100011101001110001101000111000100
1101110001110100111000110100011101001110010
```

These words form one orbit under reversal and the exchange of the two alphabet symbols. The first two have distinct 2-binomial square sets exactly \(\{00,11,0101\}\); their complements have \(\{00,11,1010\}\). In particular, every binary word of length at least \(44\) contains at least four distinct 2-binomial squares.

## Assumptions and scope

Words are finite and linear (not cyclic), over the labeled alphabet \(\{0,1\}\). Factor means consecutive letters, whereas the binomial coefficients used for comparing halves count *scattered* subsequences. The empty factor is excluded, both halves of a square must be nonempty, and different literal factors remain different even if 2-binomially equivalent. The stated optimum has no additional prohibition on repeated characters, ordinary squares or cubes.

## Proof

**Reduction of the equivalence test.** Let \(u,v\) be binary words of the same length \(h\). For a word \(x\), write \(c_{01}(x)\) for the number of indexed pairs \(i<j\) with \(x_i=0\) and \(x_j=1\), and \(c_0(x)\) for its number of zeros. Then
\[
u\sim_2 v\quad\Longleftrightarrow\quad(c_0(u),c_{01}(u))=(c_0(v),c_{01}(v)).
\]
Indeed, the other length-one count is \(h-c_0\); the length-two subsequence counts for \(00\) and \(11\) are \(\binom{c_0}{2}\) and \(\binom{h-c_0}{2}\), while the count for \(10\) is \(c_0(h-c_0)-c_{01}\). Thus the displayed two-coordinate test is necessary and sufficient for all six nonempty subsequence patterns of length at most two.

**Exhaustive finite recurrence.** For a word \(w\), define \(E(w)\) to contain exactly the even-length suffixes \(uv\) of \(w\) with \(u\sim_2v\) and \(|u|=|v|\ge1\). Appending any symbol \(a\in\{0,1\}\) can introduce new factors only at the final position, hence the exact set recurrence is
\[
\mathcal S_2(wa)=\mathcal S_2(w)\cup E(wa).
\]
Starting with the empty word and an empty square set, take both possible symbol extensions at every depth, retaining an extension if and only if the union has cardinality at most three. Discarding a state with four square types is lossless, because a word containing four such factors can never lose them by extension. By induction, the retained states at depth \(n\) are **all** binary words of length \(n\) with at most three distinct 2-binomial squares, together with their exact square sets.

The fully specified recurrence is implemented in `check_bfs.py`. It yields \(1108\) retained words at length \(16\), \(64\) at length \(40\), \(32\) at \(41\), \(16\) at \(42\), \(4\) at \(43\), and **zero** at \(44\). These are all states, not random samples: each retained word is expanded by both letters. The four depth-\(43\) words are the ones displayed in the theorem. Since every longer word has a length-\(44\) prefix, none can satisfy the condition; this establishes the sharp upper bound and classification. Direct reversal/complement comparisons of the four witnesses give their single symmetry orbit.

## Verification

The complete reproducible certificate consists of two standalone Python 3 standard-library programs. From the directory containing these files, run:

```
python3 check_bfs.py
python3 check_dfs.py
```

The first program generates all retained words at every length through \(44\) by the two-coordinate subsequence signature, asserts the exact four extremizers and empty depth \(44\), and prints the layer counts. The second independently enumerates the complete six-coordinate binomial profile directly using all indexed subsequence pairs; it searches by depth-first recursion, normalizing the first letter to zero using complementation symmetry. It verifies exactly the two zero-initial extremizers at length \(43\) and the absence of any length-\(44\) extension. Both were executed and reported `BFS_PASS` and `DFS_PASS`, respectively. The latter visits \(8756\) accepted zero-initial prefix states. These exact deterministic finite exhaustions, rather than a nonexhaustive finite experiment, are the upper-bound certificate.

## Relationship to prior work

Rao, Rigo and Salimov (first public preprint 2013-10-17) introduced the relevant 2-binomial-square avoidance setting. In Section 4 of their 2015 paper, their computational Fact 1 states that no **infinite** binary word has only three different 2-binomial squares. The current result sharpens this to the exact maximum finite length and classifies every maximum word; neither figure nor the extremizers are stated in the inspected primary article. Rigo and Salimov's separate study of binomial complexity concerns equivalence classes of equal-length factors of *infinite* words, not this finite distinct-square threshold. Gabric and Shallit's study of infinite binary words with three *ordinary* squares treats a strictly different constraint: an ordinary square is always 2-binomial, but a 2-binomial square need not have equal literal halves. No theorem from those inspected materials implies the present sharp cutoff.

## Limitations

The all-length upper bound is established by a complete reproducible finite search with an explicit monotone pruning invariant, not by a short noncomputational classification. It counts distinct literal 2-binomial-square factors, not square occurrences or square equivalence classes. It does not determine the finite thresholds for four or more distinct 2-binomial squares, nor infinite-word behavior under other notions of repetition. Independent external mathematical and historical-priority review has not been performed; an unindexed earlier exact enumeration remains possible.

## References

1. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743, first public 2013-10-17; Theoretical Computer Science 572 (2015), 83–91. DOI: 10.1016/j.tcs.2015.01.029. Open author manuscript: https://orbi.uliege.be/bitstream/2268/178702/1/final.pdf.
2. M. Rigo and P. Salimov, *Another generalization of Abelian equivalence: binomial complexity of infinite words*, Theoretical Computer Science 601 (2015), 47–57. DOI: 10.1016/j.tcs.2015.07.025. Open author manuscript: https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf.
3. D. Gabric and J. Shallit, *The simplest binary word with only three squares*, RAIRO Theoretical Informatics and Applications 55 (2021), article 3. DOI: 10.1051/ita/2021001. https://www.numdam.org/articles/10.1051/ita/2021001/.
