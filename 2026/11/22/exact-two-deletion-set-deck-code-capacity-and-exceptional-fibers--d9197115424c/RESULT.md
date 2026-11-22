# Exact two-deletion set-deck code capacity and exceptional fibers in \(S_6\)

## Finding
For the 720 permutations of six distinct ranked symbols, observe the **entire set** of distinct standardized permutations obtainable by retaining any four positions, with multiplicities discarded. This full-deck observation has precisely 714 distinct possible values: 710 have one source, two have two sources, and two have three sources. All nontrivial inverse fibers are listed below. Consequently a codebook that is uniquely decodable from its entire two-deletion set-deck has at most **714** codewords, and exactly **36** labeled codebooks attain this bound. The exception fibers form two orbits under the usual reversal/complement/inverse permutation symmetries; no permutation with at most one descent is ambiguous.

## Assumptions and scope
Write \(S_6\) for permutations of the labeled values \(1,\ldots,6\). For a sequence of four distinct numbers \(a\), define \(\operatorname{std}(a)\in S_4\) by replacing its entries with their relative ranks, starting at 1. For \(p\in S_6\), its **two-deletion set-deck** is
\[
D(p)=\left\{\operatorname{std}(p_{i_1},p_{i_2},p_{i_3},p_{i_4}):1\le i_1<i_2<i_3<i_4\le6\right\}.
\]
The observation is the complete unordered *set* of patterns, not a single received trace and not the multiset retaining the frequency of each pattern. A full-set code \(\mathcal C\subseteq S_6\) is uniquely decodable if distinct elements of \(\mathcal C\) have distinct decks. Codebooks are subsets of the fixed labeled \(S_6\); they are not identified under symmetry.

The **entire** non-singleton fiber list is the following, with each permutation shown as a six-digit word:

- Three sources: `132465`, `132546`, `213546` (deck of five patterns).
- Two sources: `241635`, `315264` (deck of ten patterns).
- Two sources: `462513`, `536142` (deck of ten patterns).
- Three sources: `564231`, `645231`, `645312` (deck of five patterns).

All other 710 permutations have singleton fibers, including all 58 permutations with at most one descent.

## Proof
The following is a finite exhaustive proof whose complete search domain, test, expected output and two independent observation implementations appear in `verify.py`.

There are exactly \(6!=720\) possible input permutations and exactly \(\binom64=15\) ordered-position subsets of size four. There are only \(4!=24\) possible observed rank patterns. Thus a deck may be represented without loss by a 24-bit integer: bit \(j\) is one exactly when the \(j\)-th lexicographically ordered element of \(S_4\) occurs as a four-position subsequence. The checker enumerates *all* 720 inputs and all 15 position choices, groups the inputs by the exact resulting bitsets, and asserts the complete four-fiber list above. The first calculation standardizes every selected four-tuple by sorting its values. A second calculation instead loops over each candidate pattern from \(S_4\) and tests the six pairwise-order relations for every four-position selection. These procedures do not share the standardization calculation; they yield exactly the same 24-bit deck for every one of the 720 inputs.

The verified histogram of inverse fiber cardinalities is
\[
\#\{d:|D^{-1}(d)|=1\}=710,\quad
\#\{d:|D^{-1}(d)|=2\}=2,\quad
\#\{d:|D^{-1}(d)|=3\}=2,
\]
and no other cardinality occurs. Indeed, the displayed four non-singleton classes contain ten inputs, and the remaining 710 each yield a different deck. The two independent exact computations and assertions of every exceptional class make this a terminating, completely specified enumeration, not an inference from a sample.

A deck-injective codebook can select at most one source from each of the 714 fibers. Conversely, selecting one element from each fiber is deck-injective, yielding the sharp capacity 714. In every maximum codebook the 710 singleton sources are forced. The four exceptional fibers offer independent choices of sizes 3, 2, 2 and 3, hence exactly \(3\cdot2\cdot2\cdot3=36\) distinct maximum codebooks. Reversing positions and complementing values both exchange the first and fourth fibers and exchange the second and third; inversion preserves each fiber as a set. These identities are checked explicitly. The 58 permutations with zero or one descent occur in no exceptional fiber, giving the stated restricted-source property.

## Verification
Run `python3 verify.py` from this directory using Python 3 and the standard library. Its assertions verify both deck constructions for every source, the exact fiber histogram, all exceptional class members, the codebook count, symmetry exchanges and the one-descent assertion. The expected terminal line is:

`VERIFY_OK sources=720 distinct_decks=714 singleton=710 doubleton=2 tripleton=2 optimal_dictionaries=36 one_descent_singletons=58`

No external dataset or software packages are necessary. The embedded code is an exhaustive finite proof of the specific six-symbol classification. It does not purport to prove a theorem for unbounded blocklength.

## Relationship to prior work
Smith [1, Proposition 3.1] already gives the colliding pair `132465`, `132546` and identifies the multiset-versus-set distinction. Raykova [2] establishes the general two-deletion set-reconstruction threshold of seven, so the existence of *some* ambiguity at six and reconstruction from all sets at greater lengths are **not** claimed as new. Neither paper's inspected two-deletion discussion supplies the four full fibers, the 714-profile census or the 36 maximum full-deck codebooks. The 2014 permutation deletion-code study [3] is a coding-theoretic motivation but uses a different observation model. The published two-deletion permutation-pattern sphere study [4] counts a single source's *distinct outputs* at length seven, not equality of complete decks across length-six sources. These comparisons are about mathematical implications, not merely titles.

## Limitations
The claimed exact code capacity concerns access to an entire set of all distinct double-deletion outputs. It is **not** a correction guarantee from any one adversarially chosen deletion trace, and the 714 figure must not be confused with a conventional one-trace deletion-correcting code bound. The result is a finite classification for six symbols; the previously known reconstruction threshold for larger permutations is not reproved here. Earlier unindexed classifications, particularly the full 2005 dissertation behind [1], could reduce originality; that dissertation's detailed contents were not available for a full comparison. Independently reproducing a computer enumeration does not constitute an external mathematical audit.

## References
[1] Rebecca Smith, “Permutation Reconstruction,” *Electronic Journal of Combinatorics* 13 (2006), #N11, published June 30, 2006. https://doi.org/10.37236/1149

[2] Mariana Raykova, “Permutation Reconstruction from Minors,” *Electronic Journal of Combinatorics* 13 (2006), #R66, published August 3, 2006. https://doi.org/10.37236/1092

[3] Ryan Gabrys et al., “Single-Deletion-Correcting Codes over Permutations,” ISIT 2014, https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf

[4] “Complete two-deletion permutation-pattern sphere spectrum at the first prolific length,” public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-two-deletion-permutation-pattern-sphere-spectrum-at-the--5cf589273ff1

[5] Rebecca N. Smith, “Combinatorial Algorithms Involving Pattern Containing and Avoiding Permutations,” doctoral dissertation, University of Florida, 2005, https://ufdc.ufl.edu/UFE0009783/00001 (full material not accessed).
