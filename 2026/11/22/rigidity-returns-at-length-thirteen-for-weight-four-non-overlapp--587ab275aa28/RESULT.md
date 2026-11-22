# Rigidity returns at length thirteen for weight-four non-overlapping binary codes

## Finding

Let \(M_4(n)\) denote the maximum size of a binary length-\(n\) code, all words of Hamming weight \(4\), with no nonempty proper prefix of any selected word equal to a suffix of another selected word, including the same word. At the first length after the known strict necklace-packing deficit at length \(12\), the bound is attained again:

\[
M_4(13)=\frac{1}{13}\binom{13}{4}=55.
\]

**Rigidity:** There are exactly **two** maximum codebooks as sets of labeled linear words. One is

\[
\mathcal C=\{w\in\{0,1\}^{13}:\operatorname{wt}(w)=4,\ \operatorname{pos}_1(w)=(1,a,b,c),\ 1<a<b<c,\ a\le4,\ b\le7,\ c\le10\},
\]

and the other is its coordinate reversal. Thus not merely the optimum size but the complete maximizing family is determined.

## Assumptions and scope

Positions are numbered \(1\) through \(13\). A proper overlap has length \(k\) with \(1\le k\le12\), and overlap prohibition applies to ordered pairs of codewords, including equal words. Two words belong to the same oriented necklace if one is a cyclic rotation of the other. Rotation and reversal are **not** quotient operations on codebooks: the assertion of exactly two counts distinct subsets of \(\{0,1\}^{13}\) as distinct. Words with a proper border are inadmissible. No statement for length other than \(13\) is asserted.

## Proof

**Necklace upper bound.** Since \(13\) is prime and a weight-four word is nonconstant, all \(\binom{13}{4}=715\) such words lie in primitive orbits of length \(13\), yielding exactly \(55\) necklaces. Any codeword must be unbordered. Two distinct cyclic rotations of one word cannot both be selected: an appropriate nonzero rotation equates a proper prefix of one with a suffix of the other. Therefore a code has at most one representative from each of the \(55\) necklaces, proving \(M_4(13)\le55\).

**Explicit attainment.** In \(\mathcal C\), a proper prefix of length \(k\) contains strictly more than \(4k/13\) ones: for \(k\le12\), the possible jump thresholds occur at \(k=4,7,10\), requiring the second, third and fourth ones to occur by positions \(4,7,10\), respectively. Conversely, the three position bounds make this strict inequality true at every proper prefix length. A suffix of length \(k\) in a word of \(\mathcal C\) contains strictly fewer than \(4k/13\) ones, since its complementary prefix of length \(13-k\) contains strictly more than \(4(13-k)/13\) ones. Hence no prefix can equal any suffix of the same length, even between different codewords. Counting the admissible triples \((a,b,c)\) with \(1<a<b<c\), \(a\le4\), \(b\le7\), \(c\le10\) gives exactly \(55\), independently rechecked by `verify.py`; thus the upper bound is attained.

**Reduction to one orientation.** For any nonempty non-overlapping code of binary words, each word must begin and end with opposite symbols: equal endpoints cause a forbidden length-one self-overlap. The starting symbols of distinct codewords must agree, because if one begins with \(0\) and another with \(1\), the suffix of the latter is \(0\), contradicting the length-one rule. Therefore a maximizing code has either every word beginning with \(1\) and ending with \(0\), or the reversed orientation. Word reversal swaps the two orientations and preserves compatibility.

**Exhaustive rigidity certificate.** In the first orientation, enumerate all length-\(13\), weight-four words with starting symbol \(1\), final symbol \(0\), and no nonempty proper border. There are exactly \(89\). Their \(55\) necklace groups have sizes distributed as \(24\) singleton groups, \(28\) two-element groups and \(3\) three-element groups. Any code of size \(55\) must select **exactly one** word from every group. Starting with the singleton groups, reject a candidate in a different group whenever it has a forbidden prefix–suffix overlap with a forced word. Repeat this unit-forcing rule. The attached 55-row `forcing.tsv` provides an explicit sequence of the groups and their unique remaining representatives: the first row of each step is forced by prior steps, and all groups end selected without a branch. `verify.py` regenerates the entire \(715\)-word universe, every rotation group, all \(89\) candidates, every proper overlap, and checks the 55 certificate steps and final codebook. This is an exhaustive, finite branch-free forcing proof, not an inference from a sample. In particular there can be no second maximizing codebook with the same orientation. Reversal gives the exactly one maximizing codebook in the opposite orientation.

## Verification

Put `RESULT.md`, `verify.py`, and `forcing.tsv` in one directory, then run `python3 verify.py` with Python 3.9 or later. The standalone checker uses only the standard library. It regenerates the complete candidates and groups rather than trusting certificate counts, exhaustively checks the forbidden overlaps, proves all groups are forced from a unique seed, compares the result with the threshold construction, and independently replays each line of `forcing.tsv`. Its expected terminal result is `VERIFY_OK 55 unique_oriented_optimum 1 nodes 1`. Only finite length \(13\) is certified; the computation is exhaustive for this length.

## Relationship to prior work

Bilotta–Pergola–Pinzani (arXiv:1112.3168, first publicly posted 2011-12-14) develop Dyck-path constructions of cross-bifix-free binary sets. Chee–Kiah–Purkayastha–Wang (arXiv:1209.0236) and Blackburn (arXiv:1303.1026) give general constructions and upper bounds, with no classification of maximum fixed-weight-four codebooks at length \(13\) in the inspected sections. The strict-prefix-density construction above should **not** be considered independently novel; the contribution assessed here is the *complete rigidity* of the weight-four length-thirteen optimum.

The closest published fixed-weight-four calculations, *First primitive-necklace packing deficit for constant-weight-four non-overlapping binary codes* and *The first four-one non-overlapping necklace deficit occurs at length twelve*, establish the exact finite values only through \(n=12\), including a strict loss of one necklace at that length. Their statements and limitations do not imply that full packing resumes at \(13\), much less that exactly two codebooks attain it. Conversely, a standard primitive-necklace upper bound and a single achieving construction do not imply rigidity: excluding all other transversals requires the forcing proof.

## Limitations

The rigidity proof is a fully enumerated finite theorem, not a general-length classification. No assertion of priority beyond the identified inspected literature is made; obscure or unindexed earlier treatments of length-thirteen fixed-weight cross-bifix-free codes remain possible. Counts and uniqueness are guaranteed by a reproducible exhaustive finite certificate, not by an independent mathematical audit.

## References

1. S. Bilotta, E. Pergola and R. Pinzani, *A new approach to cross-bifix-free sets*, arXiv:1112.3168v1 (2011-12-14). https://arxiv.org/abs/1112.3168
2. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (2012). https://arxiv.org/abs/1209.0236
3. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (2013). https://arxiv.org/abs/1303.1026
4. *First primitive-necklace packing deficit for constant-weight-four non-overlapping binary codes*, publicly indexed result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-first-primitive-necklace-packing-deficit-for-constant-weight-fou--03fc08f0d34c
5. *The first four-one non-overlapping necklace deficit occurs at length twelve*, publicly indexed result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-first-four-one-non-overlapping-necklace-deficit-occurs-at-le--75674e0f29dd
