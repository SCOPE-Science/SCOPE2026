# Complete strong \(M\)-equivalence census on the balanced quaternary double-occurrence layer

## Finding
Let \(\Sigma=\{0,1,2,3\}\), and let \(\mathcal W\) be the set of all indexed length-eight words having exactly two occurrences of each letter. For a word \(w\), let \(I(w)\) be its vector of numbers of scattered occurrences of every injective pattern (every pattern using each alphabet letter at most once). Then equality of \(I(w)\) partitions the \(2{,}520\) words of \(\mathcal W\) into exactly \(2{,}346\) classes, with the complete multiplicity distribution

\[
\boxed{\#\{\text{classes of size }1\}=2184,\quad
\#\{\text{classes of size }2\}=156,\quad
\#\{\text{classes of size }4\}=6.}
\]

No other class size occurs. Moreover, two words of \(\mathcal W\) have equal observations if and only if one can be obtained from the other by a sequence of local exchanges \(abba\leftrightarrow baab\), with distinct letters \(a,b\). Every class is a cube of zero, one, or two independent exchanges. The six four-word classes are exactly the classes comprising two consecutive exchangeable four-letter blocks using disjoint pairs of letters. The largest possible ambiguity is four, and the exact zero-error reconstruction-code size for this observation on \(\mathcal W\) is \(2{,}346\).

For example, the four members of one maximum fiber are `01102332`, `01103223`, `10012332` and `10013223`. The six lexicographically smallest representatives of the size-four fibers are `01102332`, `02201331`, `03301221`, `12210330`, `13310220` and `23320110`.

## Assumptions and scope
Words are literal indexed linear words, not necklaces, rotation classes or words modulo symbol relabeling. Scattered occurrences are indexed by strictly increasing position tuples. An injective pattern is any word of length at most four over \(\Sigma\) with no letter repeated. The empty and one-letter patterns have constant multiplicities within \(\mathcal W\), so the sixty patterns of lengths two through four suffice to test equality. The result concerns exactly four labeled letters, each occurring exactly twice; it asserts nothing about other composition layers or unrestricted words.

The equality of these observations is precisely *strong Parikh-matrix equivalence*, equivalence under the Parikh matrices for every alphabet ordering, by Teh's 2015 Theorem 3.3. The name describes an established equivalence relation; no new definition of strong equivalence is asserted.

## Proof
**1. Finite domain and observation.** There are exactly \(8!/(2!)^4=2520\) elements of \(\mathcal W\). For each of the sixty injective patterns of lengths two, three or four, compute its exact scattered count by the integer recurrence \(d_0=1\), \(d_j=0\) initially for \(j>0\), and for each letter \(c\) scanned left to right, update in decreasing order \(d_{j+1}\gets d_{j+1}+d_j\) when the pattern's \((j+1)\)-st letter equals \(c\). This counts all increasing position tuples, not merely contiguous factors. `check_scattered.py` recursively generates all allowed words and groups the resulting complete sixty-coordinate vectors. Its exact dictionary census returns \(2184\) singleton vectors, \(156\) vectors with two preimages, and \(6\) vectors with four preimages; its assertions check that these account for all \(2520\) words and precisely \(2346\) vectors.

**2. Structural lower inclusion.** For distinct letters \(a,b\), the two four-letter blocks \(abba\) and \(baab\) have the same counts of every injective scattered pattern; in either block the only nonconstant two-letter observations are \(\#ab=\#ba=2\), while observations involving a third letter vanish. Concatenation preserves equality of complete injective scattered-pattern vectors by partitioning each occurrence at the block boundaries. Thus local replacements in an arbitrary surrounding word preserve the observation. This is also the special case with empty interior of Teh's established rule SE.

Each exchangeable length-four block uses both occurrences of its two letters, so different exchangeable blocks in a word are necessarily disjoint and involve disjoint letter pairs. This can also be checked directly: within a block \(abba\) neither the two endpoint occurrences of \(a\) nor the two adjacent middle occurrences of \(b\) can simultaneously fit the required endpoint or middle roles of a distinct overlapping exchange block. Since the words have length eight, at most two independently exchangeable blocks can occur. Each rewrite component is therefore a cube of dimension zero, one or two.

**3. Exact rewrite-component census.** Count undirected exchange edges by choosing a starting position (five choices), the unordered pair of exchanged letters (six choices), and the order of the remaining four letters (six choices); the resulting count is \(5\cdot6\cdot6=180\) edges. Four-element components consist of two disjoint exchange blocks and correspond to choosing the unordered pair for the first block (six choices), giving exactly six four-cycles. Therefore, writing \(c_j\) for the number of rewrite components of size \(j\), edge counting gives \(c_2+4c_4=180\) and thus \(c_2=156\); vertex counting gives \(c_1+2c_2+4c_4=2520\), thus \(c_1=2184\). Hence the rewrite graph has \(2346\) components. `check_rewrites.py` independently reconstructs all \(2520\) graph vertices, the \(180\) edges, and their connected components, confirming the analytic census.

**4. No additional strong-equivalence collisions.** Every rewrite component lies inside a complete observation fiber by Step 2. The independently calculated number of observation fibers in Step 1 equals the \(2346\) rewrite components from Step 3. Thus each fiber is exactly one component, and the characterization and spectrum follow. `check_independent.py` separately enumerates scattered occurrences using combinations of position indices instead of dynamic programming; it verifies direct set equality of every observation fiber and its rewrite component, including all \(2346\) classes. This completes the finite proof without assuming an unproved general rewriting theorem.

## Verification
Run each included program from its directory using Python 3's standard library:

```sh
python3 check_scattered.py
python3 check_rewrites.py
python3 check_independent.py
```

`check_scattered.py` implements an integer subsequence-count dynamic program; `check_rewrites.py` constructs the local-exchange graph without computing those counts; `check_independent.py` implements a second observation calculation by direct enumeration of position subsets and compares every observation fiber with the rewrite component containing its words. Their successful assertions yield respectively \((2184,156,6)\), \((2184,156,6)\), and equality of all \(2346\) partitions. The algorithm is exhaustive because the domain is completely generated as the \(8!/(2!)^4\) multiset permutations and all injective patterns of lengths two through four are checked. No sampling, randomization, external data, solver assumption or timeout inference is involved.

## Relationship to prior work
Teh's *Parikh Matrices and Strong M-Equivalence* (first publicly posted January 29, 2015; arXiv:1501.07354) supplies the definition, injective-pattern characterization (Theorem 3.3), and sound rule SE (Proposition 3.8). It proves rewrite completeness only for specified **ternary** layers with low counts of an ordered three-letter pattern (Theorem 4.2), and exhibits broader exceptions to elementary-rewrite completeness. It does not give the balanced **quaternary** eight-letter exact ambiguity spectrum or a completeness proof for this composition layer. Poovanandran and Teh (2017, arXiv:1702.03647) study stronger transformations for **ternary** words; these neither tabulate nor imply the quaternary fixed-composition census. Relevant research-index comparisons about Parikh matrices, scattered decks and fixed-content spectra do not state this quaternary injective-pattern fiber classification. The local rule and general definition are credited as prior work; the new claim is the exact finite-layer classification and counts.

## Limitations
This is an exact finite classification, not a theorem for all alphabet sizes or arbitrary content vectors. The enumeration exhaustiveness and independent implementations can be checked from the included programs, but this is not a formal proof-assistant certificate or an independent external audit. Published-work searches may miss unindexed tables or earlier equivalents; absence from searches does not prove historical priority. No assertion is made that rule SE is complete outside this fixed composition layer.

## References
- Wen Chean Teh, *Parikh Matrices and Strong M-Equivalence*, arXiv:1501.07354 (initial version 2015-01-29), https://arxiv.org/abs/1501.07354 and https://arxiv.org/pdf/1501.07354.
- Ghajendran Poovanandran and Wen Chean Teh, *Strong \(2\cdot t\) and Strong \(3\cdot t\) Transformations for Strong M-Equivalence*, arXiv:1702.03647 (2017-02-13), https://arxiv.org/pdf/1702.03647.
- Wen Chean Teh, *Order of weak M-relation and Parikh matrices*, *Theoretical Computer Science* (2018), https://doi.org/10.1016/j.tcs.2018.04.042 (abstract/available metadata consulted; full text not obtained).
