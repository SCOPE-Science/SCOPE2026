# Sharp one-deletion code capacity for four signed ranks

## Finding

Let \(B_n\) consist of all signed permutations \(w=(w_1,\ldots,w_n)\): the absolute values are precisely \(1,\ldots,n\), and each entry has an independent positive or negative sign. For a position \(i\), let \(\delta_i(w)\) delete that entry, retain all remaining signs, and replace every surviving absolute value by its rank among the surviving absolute values. Write \(D(w)=\{\delta_i(w):1\le i\le n\}\), with multiplicities discarded. A one-deletion-correcting code is a subset \(C\subseteq B_n\) whose sets \(D(w)\), for distinct \(w\in C\), are disjoint.

**Theorem.** For the four-rank signed deletion channel,

\[
\max\{|C|:C\subseteq B_4,\ D(w)\cap D(w')=\varnothing\text{ for }w\ne w'\}=20.
\]

There exists an optimum code invariant under simultaneous negation of all signs. The simple weighted deletion-output bound given below is also exactly \(20\); thus the associated fractional shadow-packing relaxation is tight.

## Assumptions and scope

Positions are ordered and labeled; absolute ranks are unique; every sign is retained except the sign of the deleted entry. Neither the deleted rank nor its position is transmitted. The channel produces **one** unknown outcome in \(B_3\), not the entire deck as an observation. The claim concerns exactly four source ranks, not arbitrary-length signed permutations, ordinary unsigned permutations, permutations with retained absolute labels, or channels allowing sign errors.

There are \(|B_4|=2^4 4!=384\) possible sources and \(|B_3|=2^3 3!=48\) possible received words. This is a natural orientation-retaining version of rank-standardized deletion, appropriate whenever an ordered set of distinct markers carries a binary orientation attribute.

## Proof

**1. A weighted output certificate.** For \(v=(v_1,v_2,v_3)\in B_3\), assign the nonnegative integer twice-weight

\[
\lambda(v)=\begin{cases}
0,&\operatorname{sgn}(v_1)=\operatorname{sgn}(v_3)\ne\operatorname{sgn}(v_2),\\
2,&\text{all signs agree and }(|v_1|,|v_2|,|v_3|)\in\{(1,2,3),(3,2,1)\},\\
1,&\text{otherwise}.
\end{cases}
\]

There are \(12\) received words of weight \(0\) (two alternating sign patterns, each with six absolute permutations), \(4\) of weight \(2\) (two constant sign patterns, each with two monotone absolute permutations), and \(32\) of weight \(1\). Hence \(\sum_{v\in B_3}\lambda(v)=40\).

**2. Feasibility for every source.** We show

\[
\sum_{v\in D(w)}\lambda(v)\ge2\qquad\text{for every }w\in B_4.
\]

If the source signs are not constant, deleting suitable positions gives at least two distinct *nonalternating* three-sign patterns. This can be seen directly by sign-pattern type: with one sign change, delete an entry on each side of the change (using a singleton-sign deletion where necessary); with two sign changes, the patterns are, up to reversal and global sign change, `++-+` or `+--+`, whose deletions give respectively `+++` and `++-`, or `+--` and `--+`; with three changes, the pattern is `+-+-` up to negation, and its two middle-position deletions give `++-` and `+--`. The two resulting received words cannot coincide because their sign patterns differ. Each has twice-weight at least one.

If all four source signs agree, all received sign patterns are constant, and every output has twice-weight at least one. When at least two distinct outputs occur, the desired sum follows. If there is just one distinct output, the underlying unsigned permutation must be strictly monotone: indeed equality of outputs from adjacent deletion positions forces the adjacent absolute values to be consecutive, and equality of all four deletions forces a simple four-vertex path using only adjacent integer values, hence the order \((1,2,3,4)\) or \((4,3,2,1)\). Its unique received word has twice-weight two. This proves feasibility in all cases.

**3. Upper bound.** If \(C\) has pairwise disjoint deletion sets, then by the preceding inequality and nonnegative weights,

\[
2|C|\le\sum_{w\in C}\sum_{v\in D(w)}\lambda(v)
\le\sum_{v\in B_3}\lambda(v)=40,
\]

so \(|C|\le20\).

**4. Matching code.** Take the ten signed four-tuples listed here, together with their entrywise negatives:

```
(-1,-2,-3,-4)   (-1, 2, 3,-4)
(-2,-1,-4,-3)   (-2,-1, 4, 3)
(-2, 1,-4, 3)   (-3,-4,-1,-2)
(-3, 4,-1, 2)   (-3,-4, 2, 1)
(-4,-3, 1, 2)   (-4,-3,-2,-1)
```

These give twenty distinct source words. Direct deletion and sign-preserving rank standardization produce \(46\) **different** received words across the twenty decks; the only unused words of \(B_3\) are `(-3,2,-1)` and `(3,-2,1)`. To check without trusting an optimization system, for each listed tuple delete each of the four positions, rank-standardize its three surviving absolute values, and compare all resulting triples. The embedded `verify.py` performs this check and cross-checks the entire channel against independent inverse insertions. Thus all twenty deletion sets are disjoint, proving the matching lower bound.

## Verification

Run `python3 verify.py` from the directory containing this file and the embedded checker. The script uses only the Python standard library, independently generates all \(384\) sources and \(48\) recipients, reconstructs the inverse incidence relation from all \(4\) insertion positions, \(4\) inserted absolute ranks and both signs, checks every one of the \(384\) weighted source inequalities, and verifies all twenty codewords and their pairwise deletion disjointness. Its expected terminal marker is `VERIFY_OK`. The proof's weight argument is analytic and does not infer optimality from a failed optimizer search.

## Relationship to prior work

Gabrys, Yaakobi, Farnoud, Sala, Bruck and Dolecek (2014) define rank-standardized deletion for ordinary *unsigned* permutations, prove the consecutive-run characterization of identical deletion outputs, and construct asymptotically efficient codes. Their symbols do not carry independent signs, so their code bounds do not determine the present twenty-word signed capacity. The consecutive-run argument is acknowledged where used.

Galvão, Lee and Dias (2015) use signed permutations to retain marker orientation, especially for genome rearrangement models. Their results concern sorting by short signed reversals and transpositions, not recovering a source after one sign-preserving, rank-standardized deletion. Here the sign attribute changes the received alphabet and collision structure; forgetting it is a strictly coarser channel and does not yield the exact code capacity proved here.

Other available research records concern signed-successions encoding of optimal *ternary sparse-word* deletion codes and full-systematic *unsigned* permutation codes. Neither published summary states a theorem about \(B_4\) with an independent sign at every absolute rank or an exact twenty-word capacity. These comparisons are of implication and model, not keyword matching.

## Limitations

The exact answer is limited to four signed ranks. No capacity theorem or asymptotic scaling law for \(n\ge5\), no complete classification of all optimal codebooks, and no resistance to sign flips or multiple deletions are asserted. This is a finite mathematical certificate and self-review, not independent external mathematical validation. Unindexed earlier exact tabulations and the inaccessible full contents of some related research records remain historical-priority risks. The code is given explicitly and independently reproducible, but numerical enumeration is not used as a replacement for the stated upper-bound proof.

## References

1. R. Gabrys, E. Yaakobi, F. Farnoud, F. Sala, J. Bruck and L. Dolecek, "Single-Deletion-Correcting Codes over Permutations," *2014 IEEE International Symposium on Information Theory*, pp. 2764–2768, DOI: 10.1109/ISIT.2014.6875337; open copy: https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf.
2. G. R. Galvão, O. Lee and Z. Dias, "Sorting signed permutations by short operations," *Algorithms for Molecular Biology* **10**, article 12 (25 March 2015), DOI: 10.1186/s13015-015-0040-x; https://link.springer.com/article/10.1186/s13015-015-0040-x.
