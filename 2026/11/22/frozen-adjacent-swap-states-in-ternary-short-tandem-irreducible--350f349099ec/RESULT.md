# Frozen adjacent-swap states in ternary short-tandem-irreducible words

## Finding

Let \(\mathcal I_n\) be the indexed words of length \(n\ge 3\) over the labeled alphabet \(\{0,1,2\}\) containing neither an adjacent pair \(aa\) nor an adjacent repetition \(abab\). Join distinct words in \(\mathcal I_n\) when swapping one pair of **adjacent positions** of the first yields the second. A word is *frozen* if it is isolated in this restricted graph. With Fibonacci numbers \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), the exact frozen count is

\[
Z_n=\begin{cases}6F_{(n-1)/2},&n\ge3\text{ odd},\\0,&n\ge4\text{ even}.\end{cases}
\]

Equivalently,

\[
\sum_{n\ge3} Z_n z^n=\frac{6z^3}{1-z^2-z^4}.
\]

The result is a structural characterization, not just a sequence: the maximal sign runs of a frozen word are exactly an initial singleton, zero or more internal runs of length two or four, and a final singleton, with alternating signs between runs. In particular every odd-length restricted graph has multiple isolated vertices, so no Hamiltonian adjacent-swap Gray listing exists at any odd length \(n\ge3\). The absence of frozen vertices for even lengths does **not** imply connectivity or Hamiltonicity.

## Assumptions and scope

All words are linear, indexed, and over exactly three labeled symbols. Swaps exchange positions \(i\) and \(i+1\), never nonadjacent positions. Both the source and the output must avoid \(aa\) and \(abab\). This counts isolated vertices only, not components, edge counts, or largest independent sets. The small boundaries are \(Z_1=3\) if one separately defines an isolated one-symbol word, and \(Z_2=0\); the theorem and displayed series start at \(n=3\).

## Proof

**Sign encoding.** Regard letters as elements of \(\mathbb Z/3\mathbb Z\). For a proper word \(w=(w_1,\ldots,w_n)\), write \(s_j=w_{j+1}-w_j\in\{+1,-1\}\) for \(1\le j<n\). The first symbol and the sign sequence reconstruct the word uniquely. The factor \(abab\) occurs if and only if three consecutive signs alternate, namely \((+,-,+)\) or \((-,+,-)\): the first two increments sum to zero and the next two also sum to zero. Consequently every *interior* maximal sign run in an admissible sequence has length at least two. The first and last runs may have length one.

**Local swap lemma.** At a word endpoint, exchanging its first two (or last two) letters keeps adjacent letters distinct exactly when the first two (or last two) signs are equal. In that case precisely those two signs change sign. At an interior position, a swap keeps neighboring letters distinct exactly when the three signs spanning its four-letter neighborhood are equal; then exactly those three signs change sign. These claims follow by testing the two new cross-boundary adjacencies in \(\mathbb Z/3\mathbb Z\). For a swap to be *legal* the resulting sign sequence must additionally contain no alternating triple.

**Endpoint runs.** If the first maximal sign run has length two, flip its first two signs: they now match the next run if present and introduce no alternating triple. If its length is three, flip all its first three signs by the interior adjacent swap; these also match the next run if present. If its length is four or more, flip its first two signs; the remaining next two original signs are equal, so the new boundary cannot contain an alternating triple. Thus some legal move exists whenever the first run has length at least two. By reversal the same holds for the last run. This includes the single-run case. Frozen words therefore must have initial and terminal runs of length one.

**Interior runs.** Consider an interior maximal run of sign \(t\), bounded on each side by a sign \(-t\). Its length cannot equal one by admissibility. If its length is three, flip the entire run; all altered signs then match their bordering signs, and no alternating triple is introduced. If the length is at least five, flip the first three signs; those now match the left border, while the next two original signs are both \(t\), so again no alternating triple is introduced. Conversely, a length-two run has no three-equal-sign interior-swap site. A length-four run has only two such sites. Flipping its first three signs creates \((-t,t,-t)\) at the right border; flipping its last three creates the same alternating triple at the left border. Hence neither site is legal. With endpoint singleton runs, no endpoint swap is proper, and all interior candidate swaps lie in maximal sign runs. This proves the stated necessary and sufficient characterization.

**Exact census.** The total number of signs is \(n-1\). The two endpoint singletons contribute two signs; the internal run lengths contribute a sequence of parts from \(\{2,4\}\). Hence \(n-1=2+2k\) with \(k\ge0\). The number of ordered compositions of \(k\) with parts one and two, including the empty composition at \(k=0\), is \(F_{k+1}\). There are independently three choices of first letter and two choices of first sign. Therefore \(Z_{2k+3}=6F_{k+1}\), while no frozen words have even length. Summing the Fibonacci series yields \(6z^3/(1-z^2-z^4)\).

For each odd length there are at least six frozen words, whereas \(\mathcal I_n\) contains other words (for example the cyclic run \(012012\ldots\)), so a Hamiltonian listing by the permitted swaps is impossible.

## Verification

`checker.py` enumerates every allowable sign sequence for sign lengths two through eighteen, constructs a word, directly tests all adjacent swaps against **both** forbidden factors, and checks the run characterization and Fibonacci count. It also independently enumerates every original ternary word through length eleven. All these bounded checks passed. They corroborate the local-swap proof; they do not replace its all-length argument.

For example, at lengths \(3,5,7,9,11,13\), the frozen counts are respectively \(6,6,12,18,30,48\); at every even length \(4,6,8,10,12\), the count is zero.

## Relationship to prior work

Chee, Chrisnata, Kiah and Nguyen (2018) give encoding/ranking methods and a Fibonacci-type recurrence for the *number of all* short-tandem-irreducible ternary words, not the isolated vertices of an adjacent-swap graph. Adamson, Flaherty, Potapov and Spirakis (2023/2024) analyze unrestricted transposition graphs of fixed-Parikh words; the constraint that both endpoints avoid \(aa\) and \(abab\) is absent. Fuchs and collaborators (2025) analyze color swaps on proper graph colorings, including paths; their path observation requires only adjacent symbols to remain unequal. That condition is strictly weaker than requiring preservation of the length-four square avoidance: `0102101` has proper adjacent swaps producing `0120101` and `0101201`, but both outputs contain \(abab\), so the source is frozen in the present graph although it is movable in the proper-coloring graph. Thus neither the unconstrained graph result nor the proper-only local rule determines the stated Fibonacci census without further argument. Equivalent results under other terminology remain possible.

## Limitations

The theorem is purely combinatorial. It does not show that adjacent swaps model actual molecular mutations, that even-length graphs are connected, or that the frozen census determines optimal correcting codes. The result is self-reviewed only; no independent scientific audit or verification is claimed. A historical-priority search cannot exclude an unknown equivalent characterization.

## References

1. Y. M. Chee, J. Chrisnata, H. M. Kiah, T. T. Nguyen, *Efficient Encoding/Decoding of Irreducible Words for Codes Correcting Tandem Duplications*, arXiv:1801.02310, first posted 2018-01-08. https://arxiv.org/abs/1801.02310
2. D. Adamson, N. Flaherty, I. Potapov, P. G. Spirakis, *Structural and Combinatorial Properties of 2-swap Word Permutation Graphs*, arXiv:2307.01648, first posted 2023-07-04. https://arxiv.org/abs/2307.01648
3. J. Fuchs, R. Saito, T. Suga, T. Suzuki, Y. Tamura, *Coloring Reconfiguration Under Color Swapping*, ISAAC 2025, DOI:10.4230/LIPIcs.ISAAC.2025.33. https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.33/LIPIcs.ISAAC.2025.33.html
