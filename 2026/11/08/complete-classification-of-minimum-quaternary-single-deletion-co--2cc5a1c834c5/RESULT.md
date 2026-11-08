# Complete classification of minimum quaternary single-deletion covering codebooks

## Finding
Let \(\Sigma=\{0,1,2,3\}\). A single-deletion covering codebook is a set \(C\subseteq\Sigma^3\) such that every ordered two-letter word in \(\Sigma^2\) occurs as a subsequence of a member of \(C\). The known minimum possible codebook size is six. The following is a complete enumeration **at that minimum**, not a new determination of the minimum size.

**Classification theorem.** There are exactly \(644\) six-word covering codebooks on the labeled alphabet. Under the action of the \(24\) alphabet permutations and global reversal of all codewords, they form exactly \(21\) equivalence classes. The class-size distribution is
\[
\#\{\text{classes of sizes }8,12,24,48\}=(1,3,9,8).
\]
Exactly \(120\) codebooks (five classes) have pairwise disjoint deletion shadows and therefore are perfect one-deletion-correcting codes; the other \(524\) (sixteen classes) are covering but not deletion-correcting. If the *shadow excess* is defined by
\[
E(C)=\sum_{w\in C}|D(w)|-16,
\]
where \(D(abc)=\{ab,ac,bc\}\) is a set, then the numbers of minimum covers with excess \(0,1,2\) are respectively \(120,336,188\), and no other excess occurs. The complete \(644\)-row catalog and one representative of each of the \(21\) classes are in `codebooks.tsv` and `orbits.tsv`.

## Assumptions and scope
The alphabet symbols are labeled and all words have length exactly three. A codebook is an unordered *set* of six distinct words, not a sequence or multiset. Deletion removes exactly one of the three positions; duplicate resulting two-letter words are counted only once. The sixteen targets are the **ordered** pairs, including \(00,11,22,33\). The symmetry group is \(S_4\times C_2\): one global alphabet permutation, optionally followed by reversal of every three-letter word. Arbitrary coordinate permutations are not asserted to preserve the deletion-cover property. The result concerns all minimum covers, not just those whose deletion shadows partition the targets.

## Proof
**Minimum.** For any word \(abc\), its deletion shadow has at most three members. Covering all \(|\Sigma^2|=16\) targets therefore requires at least \(\lceil16/3\rceil=6\) codewords. Attainability is already in the literature: the six-word codebook
\[
\{002,013,121,220,310,323\}
\]
from Chee, Ge and Ling's Table 6.1 partitions the sixteen targets exactly. Thus six is the known optimum.

**Finite exhaustive lemma.** Number the words \(abc\in\Sigma^3\) by \(i=16a+4b+c\), with \(0\le i<64\). Associate to each word the sixteen-bit integer
\[
M(abc)=2^{4a+b}\mathbin{\vert}2^{4a+c}\mathbin{\vert}2^{4b+c},
\]
where \(\vert\) denotes bitwise OR. Even if two deletions give the same ordered pair, the corresponding bit is set only once. For any six distinct words, their deletion shadows cover all targets if and only if the bitwise OR of their six masks is \(2^{16}-1\).

The supplied `enumerate.cpp` visits each increasing six-tuple of indices from \(\{0,\ldots,63\}\) at most once and tests this equality. It may skip a partial tuple only when the union already covers fewer than \(16-3r\) targets with \(r\) words left, because each remaining word covers at most three new targets. Hence **no qualifying six-tuple can be skipped**. The search space before these safe pruning tests contains exactly \(\binom{64}{6}=74{,}974{,}368\) six-subsets. Its output is the complete ordered list of \(644\) accepted codebooks.

As an independent completeness argument, `verify.py` starts with no chosen codewords and repeatedly selects an uncovered target pair. It branches over **every** three-letter word containing that target as a deletion, and uses the same rigorously justified remaining-capacity inequality to prune. Every six-word cover contains a word covering the selected target, so induction shows that some branch reaches every possible six-word cover. A cover cannot be completed with fewer than six words by the preceding minimum bound. Duplicate recursion paths are removed by storing sorted word-index tuples; no candidate is lost. The two different enumerators return precisely the same \(644\) six-sets, compared byte-for-byte after canonical index sorting.

**Symmetries and perfectness.** The group \(S_4\times C_2\) acts on \(\Sigma^3\), preserves the covering property, and has \(48\) elements. For each enumerated codebook, `verify.py` computes all \(48\) images and chooses the lexicographically least sorted six-tuple as its orbit representative. Grouping codebooks by that representative gives \(21\) nonempty orbits with sizes \(8\) (one), \(12\) (three), \(24\) (nine), and \(48\) (eight). Their sizes sum to \(644\), and `orbits.tsv` records every representative and stabilizer order. Since each codebook's union has size sixteen, the deletion shadows are disjoint exactly when their individual cardinalities sum to sixteen, equivalently \(E(C)=0\). Tallying this integer over every entry yields the stated \(120,336,188\) distribution; the \(120\) zero-excess codebooks occupy five complete symmetry classes. No classification assumption about the shape of optimal codes enters either exhaustive method.

## Verification
From the embedded files, execute `sh reproduce.sh` with Python 3 and a C++17 compiler. It runs the pair-branching verification, compiles the lexicographic enumerator, and compares their exact \(644\)-codebook lists, in addition to checking both TSV certificates, the orbit-stabilizer sizes, and the shadow-excess distribution. The required success message is `VERIFY_OK 644 codebooks 21 orbits 120 perfect` (twice). `python3 verify.py` alone checks all statements against the included full catalog using only Python's standard library. Each proof step above is independent of probabilistic computation or numerical approximations.

## Relationship to prior work
Chee, Ge and Ling (2010) proved the spectrum of possible **sizes** of perfect length-three one-deletion-correcting codes and explicitly exhibited a six-word example for four symbols. Their result already establishes the optimum here; it does not classify all six-word *covering* codebooks or count their symmetry classes. Lenz, Rashtchian, Siegel and Yaakobi (preprint 2019, conference 2020) develop general covering-code bounds and constructions for insertions and deletions; the inspected conference paper gives no exhaustive count for four symbols and length three. The 2026 work of Xie, Sun and Ge addresses broader bounds and large-alphabet asymptotics, not an identified exact six-word classification. A public research-record search concerning odd-alphabet length-three covers describes exact **minimum sizes** for odd alphabets and does not imply the present quaternary enumeration. Equivalence of the *minimum-size question* to a previously solved case is expressly acknowledged; the classified *solution population* and perfect-versus-nonperfect split are the distinction.

## Limitations
This is a finite, exact classification at alphabet size four and word length three. It does not give the number of minimum codebooks for general alphabets, establish a new covering-number bound, or claim all deletion-covering codes are deletion-correcting. No independent scientific audit or exhaustive survey of every unpublished historical enumeration has been performed. The catalog uses the stated symmetry group only; other equivalence relations could yield different class counts. Reproducing the certificate assumes a correctly functioning Python 3 interpreter and, for the second implementation, a C++17 compiler.

## References
1. Y. M. Chee, G. Ge and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM Journal on Discrete Mathematics 24 (2010), 33–55. DOI: 10.1137/090751311. First arXiv posting 2010-08-07: https://arxiv.org/abs/1008.1343 . Full text: https://ymchee66.github.io/home/PDF/perfectdel.pdf .
2. A. Lenz, C. Rashtchian, P. H. Siegel and E. Yaakobi, *Covering Codes Using Insertions or Deletions*, arXiv:1911.09944, first posted 2019-11-22; ISIT 2020 conference text: https://yaakobi.net.technion.ac.il/files/2020/07/110_InDel_Covering_ISIT20.pdf .
3. C. Xie, Y. Sun and G. Ge, *New Bounds for Covering Codes under Insertions or Deletions*, arXiv:2606.15379 (2026): https://arxiv.org/abs/2606.15379 .
