# The 128 Newey classes exhaust the shortest five-letter permutation-subsequence words

## Finding

Let \(A=\{0,1,2,3,4\}\). A finite word \(w\in A^*\) is *complete* if each of the \(5!=120\) permutations of \(A\) occurs in \(w\) as a **scattered subsequence** (not necessarily as a contiguous factor). The shortest complete words have length \(19\), a previously established minimum. The complete equality-case census is:

- Exactly **\(128\)** complete words of length \(19\) up to common permutation of the five alphabet symbols; this proves that the \(128\) classes constructed by Newey in 1973 are *all* such classes.
- Exactly **\(128\cdot5!=15{,}360\)** complete length-\(19\) words on the labeled alphabet \(A\).
- Exactly **\(72\)** classes under alphabet relabeling *and reversal*: reversal fixes \(16\) relabeling classes and exchanges the other \(112\) in \(56\) pairs.
- In every class, the unique representative whose letters are renamed \(0,1,2,3,4\) in order of first appearance begins with the block `01234` and has sorted letter-occurrence multiplicities \((3,3,4,4,5)\).

For example, `0123401230412031240` is complete and has length \(19\). The complete list of all \(128\) canonical representatives is in `data/canonical_optima.txt`; their reversal-orbit partition is in `data/reversal_orbits.tsv`.

## Assumptions and scope

Words are linear, indexed finite strings over exactly five *labeled* letters. All \(120\) distinct-letter permutations must embed as subsequences. Alphabet relabeling applies the same bijection to all positions; reversal reverses the word order. No cyclic shift is included in either equivalence relation. The classification is exhaustive for exactly length \(19\). It asserts no analogous result for other alphabet sizes.

## Proof

**1. Removing repetitions and normalizing.** Consecutive equal letters can be collapsed without losing any permutation subsequence, because no target permutation repeats a letter. Thus a shortest complete word has no equal adjacent positions. Every complete word uses all five symbols. Relabel symbols in order of first occurrence to obtain a *unique* canonical word: its first symbol is `0`, and when a new symbol appears it must be the next unused digit. Every canonical word represents exactly \(5!\) labeled words, since the full alphabet is present.

**2. A sound prefix-pruning lemma.** Write \(m_s\) for the shortest length of a complete word over any given alphabet of \(s\) symbols, with \(m_0=0\). For a complete word \(w\) of length \(L\), every ordered tuple \(p\) of \(t\) distinct letters, where \(1\le t\le5\), is a subsequence of its first \(L-m_{5-t}\) positions. To see this, let the *leftmost greedy* embedding of \(p\) finish at position \(j\). For every permutation \(v\) of the complementary \(5-t\) letters, completeness yields an embedding of \(pv\). The embedding of the prefix \(p\) in that witness ends no earlier than \(j\), so \(v\) embeds after position \(j\). Consequently the suffix after \(j\) is complete on the complementary alphabet and has length at least \(m_{5-t}\). Hence \(j\le L-m_{5-t}\). The case \(t=5\) uses \(m_0=0\).

The smaller-alphabet lengths \((m_1,m_2,m_3,m_4)=(1,3,7,12)\) are classical, and are also certified by the complete finite enumerator `code/subalphabet_minima.cpp` (checking the two neighboring lengths for each nontrivial alphabet size). Thus a candidate of length \(19\) must already contain all ordered distinct-letter patterns of length \(t=1,2,3,4,5\) by depths \(7,12,16,18,19\), respectively. For a candidate of length \(18\) the corresponding deadlines are \(6,11,15,17,18\).

**3. Exact finite search.** `code/enum_greedy.cpp` enumerates *every* canonical, adjacent-repeat-free prefix, branching only to one of the already seen symbols or the next unused symbol. Its state holds, for each of the \(120\) permutations, the length of that permutation's longest leftmost-greedy matched prefix. Appending a symbol advances a state precisely when it matches the next required symbol. The state is therefore exact, not a heuristic. At each deadline from Step 2, a branch is rejected only if some ordered \(t\)-letter prefix cannot yet be embedded; by Step 2 no complete word lies below such a branch. At a terminal depth, all \(120\) states must equal \(5\). The enumerator yields zero canonical complete words at length \(18\), and exactly \(128\) at length \(19\).

**4. Independent-state enumeration and postprocessing.** `code/enum_subseq.cpp` performs the same complete canonical traversal but independently maintains explicit bitsets of all *present* distinct-letter subsequences of lengths \(1\) through \(5\); appending a symbol adds a pattern if its shorter prefix was already present and the symbol is new to that pattern. Its deadline tests use the cardinalities of these independently computed languages, rather than the greedy-permutation states. It yields exactly the same sorted list of \(128\) length-\(19\) representatives and none of length \(18\). Direct testing of every displayed representative against all \(120\) permutations independently checks that every leaf retained is complete.

No shorter complete word can exist: if one had length less than \(18\), it could be shortened by collapsing adjacent repetitions and then extended without adjacent repetitions to length \(18\), preserving all embedded permutations, contradicting the length-\(18\) census. Thus the \(128\) candidates are indeed shortest. Since alphabet relabeling acts freely, the labeled count is \(128\cdot 120\). The canonical output list shows that all \(128\) words start with `01234` and have the stated multiplicities. Under reversal followed by first-appearance normalization, the exhaustive list is invariant and the resulting involution has \(16\) fixed points and \(56\) two-element orbits. This gives \(72\) classes under relabeling and reversal.

Every finite-search boundary, generated object, recurrence and result is specified in the three C++ sources and checked using the standalone `tools/verify.py`. The finite calculation is exhaustive because Steps 1 and 2 justify its complete search space and every discarded subtree; the row counts alone, without these justifications, would not be a proof.

## Verification

Run `python3 tools/verify.py` in a directory containing the supplied files and a C++17 compiler. The verifier builds both independent-state C++ programs; for lengths \(18\) and \(19\), it checks that the resulting sorted canonical lists are respectively empty and byte-for-byte identical to the \(128\)-line supplied census. It independently checks the smaller-alphabet cutoffs, direct embedding of all \(120\) target permutations in each candidate, the multiplicity constraints and the complete \(72\)-row reversal-orbit table. Expected final output is `VERIFY_OK`. All checks passed from the supplied file set.

## Relationship to prior work

Newey's March 1973 technical report proved the minimum length \(19\) for five symbols and, in Section 9 (printed page 12), reported that his more general construction produces \(128\) equivalence classes, while explicitly leaving open whether these are all of them. **Those \(128\) constructed examples and the minimum length are prior work.** The contribution here is the matching upper bound \(128\) for *all* complete length-\(19\) words and the consequent complete classification. Newey also completely classified the nine four-symbol optima; that is not a new result here. Radomirović (2012) gives completeness techniques and improved constructions, not this five-symbol equality-case exhaustion. Engen and Vatter (2018) survey known shortest lengths and broader permutation-containment problems, not this census. OEIS A062714 records the minimum-length sequence, not the present equality-class count.

## Limitations

The proof is a finite exhaustive theorem at alphabet size five, not a formula for larger alphabets. The upper bound is a transparent exhaustive computation with mathematical completeness arguments, not a purely handwritten classification. The possible existence of a less visible later publication containing the exact same exhaustion remains a historical-priority risk. The 1973 report gives only the month March, not a verified publication day; the `first_public_date` metadata therefore uses the earliest *exact-calendar-day-verified* public primary source in this package, Radomirović's article published 2012-11-22, while explicitly acknowledging the earlier month-dated 1973 source. No independent scientific audit has been performed.

## References

1. Malcolm Newey, *Notes on a Problem Involving Permutations as Subsequences*, Stanford technical report STAN-CS-73-340, March 1973, especially Sections 5, 7 and 9. [Archived full text](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1973/CS-TR-73-340.pdf).
2. Saša Radomirović, *A Construction of Short Sequences Containing All Permutations of a Set as Subsequences*, *Electronic Journal of Combinatorics* **19**(4), P31, published 2012-11-22. [DOI](https://doi.org/10.37236/2859).
3. Michael Engen and Vincent Vatter, *Containing All Permutations*, arXiv:1810.08252, first posted 2018-10-18, Section 4. [Preprint](https://arxiv.org/abs/1810.08252).
4. OEIS [A062714](https://oeis.org/A062714), minimum lengths of complete permutation-subsequence words, and [A351468](https://oeis.org/A351468), Newey's construction.
