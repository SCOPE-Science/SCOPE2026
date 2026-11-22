# A sharp \(3k+1\) threshold for reconstructing palindromes from contiguous-factor counts

## Finding

**Sharp reconstruction theorem.** Fix an integer \(k\ge 1\) and a finite labeled alphabet \(\Sigma\) with at least two symbols. The **\(k\)-Abelian fingerprint** of a word \(w\) is the collection of multiplicities \(\operatorname{occ}_w(x)\) of every nonempty **contiguous** factor \(x\) of length at most \(k\), with occurrences counted at their start positions. Restrict both the source word and its potential reconstructions to ordinary linear palindromes, i.e. \(w=w^R\).

For every positive length \(n\le 3k\), the fingerprint distinguishes every palindrome of length \(n\) from every other palindrome of the same length. This is sharp: for each \(k\ge1\), the two distinct binary palindromes

\[
U_k=0^k1\,0^{k-1}1\,0^k,\qquad V_k=0^{k-1}1\,0^{k+1}1\,0^{k-1}
\]

both have length \(3k+1\) and identical \(k\)-Abelian fingerprints. Therefore, **for every alphabet containing two distinct symbols, the first length admitting two distinct fingerprint-equivalent palindromes is exactly \(3k+1\)**.

An explicit reconstruction procedure for the entire uniqueness range reads the common \((k-1)\)-letter prefix and the parity-selected central factor; at worst it determines one remaining mirrored letter pair from the single-letter counts.

## Assumptions and scope

The alphabet is finite, labeled, and contains at least two letters; \(k\) and \(n\) are positive integers. All words are linear, indexed, and have unrestricted letter multiplicities. Factor counts include overlapping occurrences and all lengths \(1,2,\ldots,\min(k,n)\); they are *not* scattered-subsequence counts, cyclic factor counts, or merely the set of distinct factors. The injectivity assertion holds for any nonempty alphabet, including a singleton; sharpness requires at least two symbols. Only reconstruction **within the palindromic source family** is asserted.

Write \(\operatorname{occ}_w(x)=\#\{i:w[i\ldots i+|x|-1]=x\}\), using zero-based positions. Reversal is denoted \(w^R\), and the empty word by \(\varepsilon\).

## Proof

**1. Prefix recovery.** For \(n\le k\), the fingerprint includes the multiplicity of the entire \(n\)-letter word, so reconstruction is immediate. Assume \(n>k\). For \(k\ge2\), every \((k-1)\)-letter word \(u\) satisfies

\[
\operatorname{occ}_w(u)-\sum_{a\in\Sigma}\operatorname{occ}_w(au)
=\begin{cases}1&\text{if }u\text{ is the prefix of }w,\\0&\text{otherwise.}\end{cases}
\]

Indeed, every noninitial occurrence of \(u\) has precisely one preceding letter. Hence the fingerprint determines the prefix \(P\) of length \(k-1\). For \(k=1\), set \(P=\varepsilon\). Palindromicity also determines the matching reversed suffix \(P^R\).

**2. Central-factor recovery by parity.** Choose

\[
j=\begin{cases}k&\text{when }n\equiv k\pmod2,\\k-1&\text{otherwise.}\end{cases}
\]

Then \(n-j\) is even and \(j\le k\). If \(j=0\), the central factor is the known empty word; this is possible only when \(k=1\) and \(n\) is even. Otherwise the centered length-\(j\) factor \(C\) starts at \(s=(n-j)/2\), and \(C=C^R\). In a palindrome, reversal pairs all noncentral occurrences of any palindrome \(j\)-factor. Thus its total multiplicity is even except for the unique centered factor \(C\), whose multiplicity is odd. The fingerprint therefore identifies \(C\) as the **unique** palindromic length-\(j\) word having odd multiplicity. This statement also accounts for repetitions of the same factor away from the center, because such occurrences occur in reversal pairs.

**3. Coverage and the last pair.** The first \(k-1\) positions (when they exist) and their mirrors are given by \(P,P^R\); the central \(j\) positions are given by \(C\). Their only possible unassigned positions on the left are from index \(k-1\) through \(s-1\). Since \(n\le3k\), parity gives \(s\le k\): if \(j=k\) then \(s\le k\), while if \(j=k-1\) the parity restriction forces \(n\le3k-1\), again giving \(s\le k\). Consequently there are either no unknown positions or exactly one unknown position and its distinct mirror. If two remain, their letters agree by palindromicity; subtracting the already determined letter counts from the length-one factor counts leaves precisely two copies of that letter. In either case, the entire palindrome is uniquely reconstructed. This includes \(k=1\), where the empty central factor requires no parity readout.

**4. Sharp counterexamples.** In each of \(U_k,V_k\), the two occurrences of \(1\) have distance at least \(k\); each is at least \(k-1\) positions from either end. Hence for every \(1\le j\le k\), no contiguous \(j\)-factor contains both ones. For each offset \(r\in\{0,\ldots,j-1\}\), the factor \(0^r1\,0^{j-r-1}\) appears exactly twice, once around each occurrence of \(1\). Every other \(j\)-factor is \(0^j\), appearing \(3k+2-3j\) times in either word. Thus the full fingerprints agree. Both words are palindromes and they are distinct (their first \(1\)'s appear at indices \(k\) and \(k-1\)). This proves noninjectivity at length \(3k+1\), and completes the theorem.

## Verification

The infinite statements follow from the four symbolic steps above, not from finite experiments. Two separately implemented reproducibility scripts provide finite cross-checks:

- `check_exhaustive.py` groups **all** palindromes by their actual factor-count fingerprints. It verifies injectivity through length \(3k\) and noninjectivity at length \(3k+1\) for binary alphabets with \(1\le k\le7\), ternary alphabets with \(1\le k\le4\), and four-letter alphabets with \(1\le k\le3\).
- `check_decoder.py` independently reconstructs every palindrome in those uniqueness ranges from its measured factor counts, implementing central parity, prefix extraction, and the mirrored-pair completion step.

Run `python check_exhaustive.py` and `python check_decoder.py` under Python 3 with only the standard library. Both scripts were executed successfully. The finite tests are checks, not a substitute for the universal proof.

## Relationship to prior work

The framework of \(k\)-Abelian equivalence and its prefix-plus-factor characterization were developed in Huova–Karhumäki (2011) and Karhumäki–Saarela–Zamboni (2013). The latter's Theorem 2.6 classifies shortest ambiguous **unrestricted** words at length \(2k\); it neither restricts sources to ordinary palindromes nor establishes the present sharp \(3k+1\) threshold. Karhumäki–Puzynina (2014) and Cassaigne–Karhumäki–Puzynina (2018) address \(k\)-Abelian palindromic rich/poor factors, using the distinct condition that a word be equivalent to its own reversal, rather than injectivity among words already fixed by reversal. The available 2016 presentation of that work discusses the latter rich/poor questions, not this reconstruction threshold. Karhumäki–Puzynina–Rao–Whiteland (2016) study unrestricted equivalence classes using switchings and de Bruijn graphs, without a palindromic uniqueness claim.

A previously recorded special-case classification identifies the first \(3\)-Abelian ambiguity of ordinary palindromes at length ten and enumerates all its fibers. The present result goes beyond that fixed-order census: it establishes the **sharp threshold for every positive order \(k\)** and supplies a uniform constructive reconstruction proof. A published exact three-mer census for sparse-marker words applies only at factor length three, not uniformly to arbitrary factor length.

## Limitations

The theorem does not characterize all fibers at or beyond length \(3k+1\), nor does it claim unique reconstruction of arbitrary nonpalindromic words. The fingerprint is a complete multiset of contiguous factors of **all** lengths at most \(k\); weakening the observations may invalidate the threshold. The scientific originality judgment is based on documented searches and examined primary sources rather than a guarantee of uniqueness in all literature. The full 2014 proceedings article was not accessible; a closely related presentation and its abstract were examined. Older unindexed statements remain a residual originality risk. No independent audit has been performed.

## References

- M. Huova and J. Karhumäki, *Observations and Problems on k-abelian avoidability*, arXiv:1104.4273v1, first public 2011-04-21, https://arxiv.org/abs/1104.4273.
- J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, first public 2013-01-22, https://arxiv.org/abs/1301.5104.
- J. Karhumäki, S. Puzynina, M. Rao, and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319v1, first public 2016-05-11, https://arxiv.org/abs/1605.03319.
- J. Karhumäki and S. Puzynina, *On k-Abelian Palindromic Rich and Poor Words*, DLT 2014, doi:10.1007/978-3-319-09698-8_17 (abstract and related presentation inspected).
- J. Cassaigne, J. Karhumäki, and S. Puzynina, *On k-abelian palindromes*, *Information and Computation* 260 (2018), 89–98, doi:10.1016/j.ic.2018.04.001; related scientific presentation at https://www.cirm-math.fr/ProgWeebly/Renc1429/Puzynina.pdf.
