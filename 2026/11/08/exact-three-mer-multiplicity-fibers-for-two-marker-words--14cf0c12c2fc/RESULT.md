# Exact three-mer multiplicity fibers for two-marker words

## Finding
Fix any integer \(q\ge2\), an alphabet \(\Sigma=\{0,1,\ldots,q-1\}\), and a length \(n\ge8\). Let \(\mathcal W_{n,q}\) consist of all length-\(n\) words with exactly two nonzero positions. For a word \(w\), let \(\mathcal S_3(w)\) be the multiset of its \(n-2\) **contiguous** triples, including multiplicities. Two members of \(\mathcal W_{n,q}\) are equivalent when these multisets are equal.

Put \(r=q-1\). There are exactly
\[
18r+37\binom r2=\frac{r(37r-1)}2
\]
equivalence classes, independent of \(n\ge8\). At length \(n=7\), the corresponding count is \(17r+36\binom r2\), so eight is the exact stabilization threshold. More strongly, the *entire multiset of class cardinalities* is as follows. An entry `multiplicity : size` means that many distinct classes of the indicated size; entries with coincident numerical sizes are combined.

| Two nonzero symbols | Multiplicity : size of class |
|---|---|
| Equal fixed symbol \(a=a\ne0\) | \(10:1,\;1:2,\;3:(n-6),\;3:(n-5),\;1:\binom{n-6}{2}\) |
| Fixed unordered distinct symbols \(\{a,b\}\) | \(24:1,\;6:(n-6),\;6:(n-5),\;1:(n-6)(n-7)\) |

The first row occurs once per nonzero symbol (\(r\) times); the second once per unordered distinct pair (\(\binom r2\) times). In particular, for \(n\ge9\) exactly
\[
10r+24\binom r2=12r^2-2r
\]
words are uniquely determined **within** \(\mathcal W_{n,q}\) by their three-mer spectrum; at \(n=8\) this number is \(11r+24\binom r2\). These are counts of unique classes of size one, not claims about unrestricted-word uniqueness.

## Assumptions and scope
Words are linear, indexed and noncyclic. The zero symbol is distinguished, while all nonzero symbols are labeled. Exactly two *positions* are nonzero; their symbols may be equal. The three-mer observation records multiplicities and is not a set, a subsequence spectrum, or the full spectrum of all smaller lengths. No external boundary symbols are appended. The assertion is for all integers \(n\ge8\), \(q\ge2\); lengths below eight are not covered by the stabilized table.

## Proof
Every input has a unique form
\[
w=0^L a0^G b0^R,\qquad a,b\ne0,\quad L,G,R\ge0,\quad L+G+R=n-2.
\]
Associate to the three zero gaps the truncated tuple \(t=(\min\{L,2\},\min\{G,2\},\min\{R,2\})\). Every contiguous length-three factor except `000` meets at least one nonzero position and lies within two positions of it. Consequently, the complete multiplicities of **nonzero** three-mers depend only on \(t\) and the ordered symbols \((a,b)\): they are exactly the nonzero-three-mer multiplicities in
\[
0^{t_1}a0^{t_2}b0^{t_3}.
\]
The number of `000` factors is the fixed total \(n-2\) minus the sum of the other multiplicities. Thus two length-\(n\) words have equal full three-mer multisets if and only if their truncated templates have the same nonzero-three-mer signatures. The unordered set of nonzero symbols is detectable from the three-mers, so distinct sets of one or two labels never share a class.

For \(n\ge8\), the truncated tuples realized by words of length \(n\) are **exactly** the \(3^3-2^3=19\) triples in \(\{0,1,2\}^3\) with at least one entry equal to two. Necessity follows from \(L+G+R=n-2\ge6\). For sufficiency, choose the truncated gap values and distribute the remaining \(n-2-(t_1+t_2+t_3)\) zeros among the coordinates equal to two. If exactly \(k\ge1\) coordinates equal two, the number of lifts is
\[
\binom{n-2-(t_1+t_2+t_3)+k-1}{k-1}.
\]
For a fixed symbol \(a=b\), enumerate these 19 short signatures. Exactly one collision occurs, between \((0,2,1)\) and \((1,2,0)\), giving 18 classes. For fixed distinct symbols \(a,b\), enumerate the 38 templates (19 for each of the orders \((a,b)\), \((b,a)\)). Exactly one collision occurs, between the two templates \((2,2,2)\) with opposite symbol orders, giving 37 classes. There are no other collisions. For \(n=7\), the all-two truncated triple is the only one of the 19 that cannot be realized: the equal-symbol family therefore has 17 classes, while the distinct-symbol family has 36, establishing the sharp threshold. This is a finite set of exact integer-vector comparisons, reproduced in the accompanying standalone verifier; it does not rely on a nonexhaustive sample.

For completeness, grouping the 19 (respectively 38) templates by their vector signature and summing the lift-count formula yields the two class-size rows in the theorem. Each lift count is a polynomial in \(n\) of degree at most two, and the signature grouping is independent of \(n\). The verifier computes and checks the complete signature grouping at \(n=8,9,10\). Equality of the resulting polynomial values at these three distinct integers proves the table for all \(n\ge8\), not merely those tested lengths. The aggregate word counts provide an internal check: the first row contributes \(\binom n2\), and the second contributes \(n(n-1)\), as required for one fixed repeated symbol or two possible orders of distinct symbols, respectively.

The class count follows by multiplying the 18 and 37 classes by the possible symbol choices. The singleton formulas follow by observing that the quadratic class has size one only for \(n=8\) in the equal-symbol case; all other size entries beyond the displayed singleton groups exceed one for \(n\ge9\).

## Verification
Run `python verify.py` using Python 3.8+; it requires only the standard library. The program performs all 57 truncated-template comparisons, checks their class-size expressions using exact integers, verifies the word-count identities, and independently enumerates all source words for \(q=2,3,4,5\) and \(8\le n\le15\) using the actual length-three sliding windows. It reports `VERIFY_OK templates=57 direct_words=15120 alphabet_sizes=4 n=8..15`. The finite 57-template comparison is exhaustive **for the proved reduction**; the 15,120 direct word tests are supplemental regression checks, not the basis of the infinite proof.

## Relationship to prior work
Maňuch's *Characterization of a Word by Its Subwords* defines factor spectra with multiplicity and addresses general uniqueness thresholds, without supplying this fixed-two-nonzero fiber distribution. Karhumäki, Saarela and Zamboni introduce \(k\)-Abelian equivalence and global complexity results; the present measurement is specifically a **proper contiguous three-mer multiset**, not a full \(3\)-Abelian equivalence relation, and the present theorem enumerates all fibers in a sparse input shell. General de Bruijn/Euler-trail reconstruction principles explain the importance of multiplicity spectra, but they do not themselves give the 18/37 classes and their cardinalities. The previously known binary adjacent-pair multispectrum counts and unrestricted binary three-mer *singleton* counts also do not imply this exact restricted, arbitrary-alphabet class-size distribution.

## Limitations
The claim is restricted to a fixed distinguished zero, exactly two nonzero positions, length-three windows and \(n\ge8\). It does not identify uniqueness among **all** words, permit missing/noisy reads, or settle general higher-weight, longer-window reconstruction. Novelty is assessed against examined accessible literature and indexed findings, not independently certified priority; unindexed equivalent treatments may exist. The theorem is a combinatorial idealization, not a direct statement of experimental sequencing performance.

## References
1. J. Maňuch, *Characterization of a Word by Its Subwords*, DLT-era manuscript (submitted 2002), https://www.cs.ubc.ca/~jmanuch/conference/abstracts/DLT2000.pdf .
2. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a Generalization of Abelian Equivalence and Complexity of Infinite Words*, first arXiv submission 2013-01-22, https://arxiv.org/abs/1301.5104 .
3. P. A. Pevzner, *DNA Physical Mapping and Alternating Eulerian Cycles in Colored Graphs*, Algorithmica (1995), https://doi.org/10.1007/BF01188582 .
