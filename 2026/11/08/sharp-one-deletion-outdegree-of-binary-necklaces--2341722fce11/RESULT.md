# Sharp one-deletion outdegree of binary necklaces

## Finding
Let a binary necklace of length \(n\ge1\) be an equivalence class of words in \(\{0,1\}^n\) under cyclic rotation, with reversal and complementation **not** identified. Delete exactly one position, and identify resulting words of length \(n-1\) under cyclic rotation. For a necklace \(W\), write \(\mathcal D(W)\) for its set of distinct resulting necklaces, counting the empty necklace as one when \(n=1\). Put \(M(n)=\max_{W}|\mathcal D(W)|\).

For all positive integers \(n\),
\[
M(n)=\begin{cases}
1,&n=1,\\
2,&n=2,3,\\
n-2,&n\ge4\text{ and }(n\text{ even or }n\in\{5,7\}),\\
n-3,&n\ge9\text{ odd}.
\end{cases}
\]
The bounds are sharp, and the following words attain them: \(01\) for \(n=2\), \(001\) for \(n=3\), \(00101\) for \(n=5\), \(0010101\) for \(n=7\); for every even \(n=2m\ge4\), \(0^2(10)^{m-2}1^2\); and for every odd \(n=2m+1\ge9\), \(0^3(10)^{m-2}1^2\). Any constant word is a maximizer for \(n=1\).

## Assumptions and scope
Words are finite and indexed before taking rotation classes. The binary alphabet is fixed and labeled. A cyclic run of a nonconstant necklace is a maximal cyclic interval of equal symbols, including across the wraparound boundary. Its number of cyclic runs is a positive even integer. A deletion inside one run has the same necklace descendant as a deletion anywhere else in that run. There is no unknown deletion position in the output, and there is no quotient by reversal or symbol complement.

## Proof
**1. Universal run bound.** If \(W\) is nonconstant and has \(r\) cyclic runs, then \(|\mathcal D(W)|\le r\): deleting any position from one run gives the same output modulo rotation. A constant word has precisely one descendant. For even \(n\), the only word with \(r=n\) is the alternating necklace \((01)^{n/2}\), which has exactly two distinct one-deletion necklaces for \(n\ge4\), one for each deleted symbol. All other nonconstant necklaces have \(r\le n-2\), since \(r\) is even. Hence \(M(n)\le n-2\) for all even \(n\ge4\).

**2. Odd-length near-alternation.** Let \(n=2m+1\ge5\). A nonconstant necklace has either \(r\le n-3\), or \(r=n-1=2m\). In the latter case there is exactly one cyclic run of length two and every other run has length one. Up to rotation and complement, its run sequence is that of \(w=00(10)^{m-1}1\). The cyclic zero-run lengths, indexed in order, are \((2,1,\ldots,1)\), while each of the \(m\) one-runs has length one. Delete the one separating the unique zero-run of length two from the next singleton zero-run, or the one separating the last singleton zero-run from the unique double zero-run. Both descendants have cyclic zero-run list \((3,1,\ldots,1)\) and so coincide modulo rotation. If \(m\ge4\), delete instead the one separating the first two singleton zero-runs, or the one separating the last two singleton zero-runs. Both descendants have cyclic zero-run list \((2,2,1,\ldots,1)\), differing only by a cyclic shift. These are two distinct pairs of run deletions, because \(m\ge4\); thus \(|\mathcal D(W)|\le r-2=n-3\). For \(m=2,3\), the first pair alone yields \(|\mathcal D(W)|\le r-1=n-2\). Together with the run bound this proves the claimed upper bounds for all odd \(n\ge5\).

**3. A family with no run-deletion collisions.** Fix integers \(a,b\ge2\) and \(t\ge1\), and set \(w=0^a(10)^t1^b\). Its cyclic run lengths, starting at the distinguished zero-run, are
\[
(a,1,1,1,\ldots,1,b),
\]
with exactly \(t\) singleton zero-runs and \(t\) singleton one-runs, and precisely \(r=2(t+1)\) runs. We show that deleting from two different cyclic runs never produces rotation-equivalent words.

First, a zero deletion and a one deletion have different zero/one contents, hence distinct descendants. Among zero deletions, deleting from \(0^a\) preserves the number of runs, whereas deleting any singleton zero-run merges its adjacent one-runs and reduces the number of runs by two. When a singleton zero-run is deleted, the unique zero-run of length \(a\) is unchanged, and therefore anchors the cyclic run sequence uniquely. Number the singleton zero-runs in the order following \(0^a\) by \(j=1,\ldots,t\). Deleting the \(j\)-th one for \(j<t\) changes the anchored one-run list \((1,\ldots,1,b)\) by merging its \(j\)-th and \((j+1)\)-st entries into a \(2\) at position \(j\), while the final run of length \(b\) remains at the end; deleting the \(t\)-th singleton zero-run changes that final entry to \(b+1\). These \(t\) anchored lists are different, even when \(b=2\). Consequently all \(t+1\) zero-run deletions are distinct. Swapping the roles of zeros and ones and reading the cycle in the opposite direction gives the identical argument for the \(t+1\) one-run deletions, anchored at the unique \(1^b\) run. Thus
\[
|\mathcal D([0^a(10)^t1^b])|=2(t+1)=r.
\]

**4. Sharp constructions and small lengths.** For even \(n=2m\ge6\), choose \(a=b=2\), \(t=m-2\), yielding \(2(m-1)=n-2\) descendants. At \(n=4\), \(0011\) has two descendants and the bound is also sharp. For odd \(n=2m+1\ge9\), choose \(a=3,b=2,t=m-2\); the family gives \(2(m-1)=n-3\). Direct deletion gives three descendants from \(00101\) and five from \(0010101\), attaining the odd bounds at \(n=5,7\). At lengths \(1,2,3\), direct checking gives \(1,2,2\). This completes all cases. \(\square\)

## Verification
A self-contained Python 3 verifier enumerates all binary necklaces of lengths \(1\) through \(15\) and constructs their complete sets of one-deletion descendants by literal deletion and cyclic minimization. It separately checks all constructions for admissible lengths through \(300\), the universal run bound, and rotation invariance on additional examples. Execute `python verify.py`; the recorded output is `VERIFY_OK necklace_classes=4807 exhaustive_n=1..15 witnesses_n=4..300`. The computer checks are finite corroboration; the proof above covers every length.

## Relationship to prior work
Levenshtein's classical deletion-channel work and Sloane's survey give the linear-word one-deletion descendant size as the ordinary number of runs and the unrestricted linear maximum as the word length. Liron and Langberg give run-sensitive bounds and extremizers for linear subsequence deletion, not the maximum among rotation classes of both inputs and outputs. Burudgunte, Valiant and Wang study circular random trace reconstruction with multiple independent deletions; that statistical recovery question does not determine this exact single-deletion support maximum. The present result identifies a rotation-induced parity loss, including an additional odd-length obstruction when \(n\ge9\). The historical-priority comparison is not an exhaustive proof of novelty.

## Limitations
Only the binary alphabet, exactly one deleted symbol, and cyclic rotation equivalence are treated. The theorem gives a maximum over all source necklaces, not the descendant count of every source, a minimum, or a code-size bound. No statement about deletion likelihoods, stochastic sample complexity, multiple deletions, reversal classes, or larger alphabets follows automatically. Earlier unindexed studies of necklace deletion posets could potentially contain an equivalent theorem; independent audit is not yet performed.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes* (first arXiv version 2002-07-22), https://arxiv.org/abs/math/0207197, especially Section 5 on descendants.
2. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel* (first arXiv version 2012-02-08), https://arxiv.org/abs/1202.1644, Sections I–II.
3. A. Burudgunte, P. Valiant and H. Wang, *New Bounds for Circular Trace Reconstruction* (first arXiv version 2025-12-02), https://arxiv.org/abs/2512.02412; HTML proceedings https://doi.org/10.4230/LIPIcs.ITCS.2026.30, Sections 1–2.
