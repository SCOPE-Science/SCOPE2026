# Sharp \(\lfloor 2n/3\rfloor\) reconstruction threshold and last-step fibers for three-marker circular words

## Finding

Fix any integer \(n\ge6\). Consider all binary words of length \(n\) with exactly three ones, modulo cyclic rotation **but not reflection**. The full oriented cyclic \(k\)-spectrum of a word is the multiset of its \(n\) length-\(k\) cyclic factors, with each occurrence counted and all positions (including wraparound) included. The least read length that distinguishes every such necklace is exactly

\[
R(n)=\left\lfloor\frac{2n}{3}\right\rfloor.
\]

At the immediately shorter read length \(k_0=R(n)-1\), every inverse fiber has cardinality at most two. The number of fibers of cardinality two is

\[
B(n)=1+\mathbf 1_{\{n\equiv1\pmod3,\ n\ge10\}}.
\]

Thus, for each \(n\ge6\), at most two different ambiguous pairs remain one symbol below the sharp threshold. They are precisely mirror-image orders of three *distinct* circular gaps. If \(n=3m+r\), the multisets of the three step-distances between consecutive ones that generate those pairs are

| Residue | Ambiguous gap multisets |
|---|---|
| \(r=0\) | \(\{m-1,m,m+1\}\) |
| \(r=1\) | \(\{m-1,m,m+2\}\), and \(\{m-2,m+1,m+2\}\) if \(m\ge3\) |
| \(r=2\) | \(\{m-1,m+1,m+2\}\) |

For instance, at \(n=9\) the necklaces represented by `101001000` and `101000100` have identical length-five spectra but different length-six spectra. The exceptional small lengths have \(R(3)=R(4)=1\) and \(R(5)=2\).

## Assumptions and scope

All letters are in \(\{0,1\}\). The three ones are distinct marked positions, but the observations are **unindexed multisets** of oriented cyclic factors; rotations of source words are identified and reversal is not. A necklace with three ones is represented uniquely, up to cyclic reordering, by a triple of positive clockwise step gaps \((a,b,c)\) satisfying \(a+b+c=n\). The associated sequence is \(1\,0^{a-1}1\,0^{b-1}1\,0^{c-1}\) read cyclically. A length-\(k\) factor containing all three ones will be called a *triple read*. Here \(1\le k\le n\), and all counts include multiplicity.

## Proof

**1. Triple-read criterion.** A cyclic window contains all three ones precisely when it omits the interior of some clockwise gap. For a gap of step length \(g\), the shortest cyclic window containing all three ones has length \(n-g+1\). Hence a triple read exists if and only if \(\max(a,b,c)\ge n-k+1\). Equivalently, none exists exactly when every gap is at most \(n-k\). Any triple read gives the two successive inter-marker step distances as its internal one-to-one separations; the third is \(n\) minus their sum. It therefore determines the entire necklace (including its clockwise orientation). Thus any spectrum containing a triple read is a singleton fiber among weight-three necklaces.

**2. Spectra without triple reads.** Suppose no cyclic length-\(k\) window contains all three ones, and denote the *unordered* multiset of gaps by \(G=\{a,b,c\}\). Each factor with exactly two ones separated by \(d\) intervening *steps* (at fixed positions \(i<i+d<k\), and zeros elsewhere) occurs exactly \(\#\{g\in G:g=d\}\) times: choose the one gap of size \(d\) and align its endpoints at those factor positions. The no-triple assumption guarantees that the third one is outside the factor. A factor with its single one at position \(j\), indexed from zero, occurs

\[
3-\#\{g\in G:g\le j\}-\#\{g\in G:g\le k-1-j\}
\]

times, by subtracting the possibilities containing the preceding or following one; those two excluded events cannot both occur when no triple read exists. Finally, the all-zero factor occurs \(\sum_{g\in G}\max(g-k,0)\) times. These formulas show that **the entire spectrum depends only on the unordered gaps** whenever triple reads are absent. If additionally all gaps are strictly less than \(k\), the two-one factor counts recover the multiplicity of *every* gap size; consequently the unordered gap multiset is recoverable exactly.

**3. Upper bound.** Put \(K=\lfloor2n/3\rfloor\). If the spectrum at \(k=K\) has a triple read, Step 1 proves uniqueness. Otherwise all three gaps are at most \(n-K\), which is strictly smaller than \(K\) for every \(n\ge6\). Thus Step 2 recovers their multiset. When \(n=3m\), the only possible gaps are \((m,m,m)\). When \(n=3m+1\), they are permutations of \((m-1,m+1,m+1)\) or \((m,m,m+1)\), omitting nonpositive cases. When \(n=3m+2\), they are permutations of \((m,m+1,m+1)\). Each multiset has repeated entries, so all permutations define the same cyclic gap order. The necklace is uniquely recovered.

**4. Sharpness and the exact final ambiguity.** Put \(k_0=K-1\). For any three *distinct* positive gaps summing to \(n\), with each gap no larger than \(n-k_0\), Step 1 shows no triple read exists; Step 2 then shows that the two different cyclic orders of those gaps have the same spectrum. For \(n=3m+r\), setting \(H=n-k_0\) and distributing the deficit \(3H-n\) among the three gaps gives exactly the distinct-gap multisets listed under **Finding**. The possible deficit partitions are \((2,1,0)\) for \(r=0\), \((4,1,0)\) and \((3,2,0)\) for \(r=1\), and \((3,1,0)\) for \(r=2\), with the stated positivity exclusions. This gives the lower bound \(R(n)\ge K\).

For \(n\ge11\), every gap in a no-triple-read necklace at length \(k_0\) is less than \(k_0\). Step 2 therefore recovers its unordered gaps. Three distinct gaps have exactly two different cyclic orders, while any repetition has one. Hence the displayed pairs exhaust all nonsingleton fibers, and no fiber has size greater than two. For the remaining finite values, the complete no-triple-read gap multisets and their recoverability are checked by direct enumeration of all positive gap triples; the two-element fiber counts for \(n=6,7,8,9,10\) are respectively \(1,1,1,1,2\), and every other fiber is a singleton. All code cases are explicitly reproduced in `verify.py`. Finally, a shorter spectrum is obtained by taking the length-\(k\) prefix of every factor in a longer one, retaining multiplicities, so the collision at \(k_0\) persists for every smaller read length.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. It independently enumerates positive gap triples modulo cyclic order for \(6\le n\le80\), verifying the exact threshold and all critical-predecessor fiber classes. A separate implementation generates marked binary words by choosing three positions, then deduplicates by all cyclic rotations for \(6\le n\le17\). It also checks the triple-read and exact factor-frequency identities for \(6\le n\le37\). The script was executed and returned `ALL TESTS PASSED`. These finite checks are not substitutes for the unrestricted proof above.

Run: `python verify.py`.

## Relationship to prior work

Gabrys and Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra* (initial arXiv release April 12, 2018), develops reconstruction codebooks and linear substring multispectra; it does not give this fixed-three-marker cyclic threshold or boundary ambiguity list. Marcovich and Yaakobi, *Reconstruction of Strings from their Substrings Spectrum* (initial arXiv release December 23, 2019), studies linear multispectrum reconstruction under read losses and errors; its cyclic observation is discussed as a variant, not settled with these exact sparse-string formulas. Ota and Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words* (first public September 5, 2023), is especially close: it gives an algorithmic necessary-and-sufficient reconstructibility criterion for individual circular strings, using substring frequencies and minimal absent words. It does **not explicitly state** the all-length worst-case weight-three threshold or the exact critical-predecessor fibers. Their general criterion can algorithmically decide individual instances, so the contribution here is the closed-form sparse-family theorem and its gap-order explanation, not a claim that circular-spectrum reconstructibility was previously unsolved. The comparison papers above provide different source sets or error models, rather than an explicit all-length sparse circular threshold.

## Limitations

The theorem is restricted to binary circular words with exactly three ones and *complete, multiplicity-preserving, oriented* cyclic factor multispectra. It does not address lost, noisy, unoriented, or partial reads, nor larger fixed weights. Reconstruction is up to rotation, not absolute starting position. The primary literature checked does not establish universal novelty against every unindexed manuscript; a prior characterization specialized implicitly to three-marker sequences remains an originality risk. The independent audit has not been performed.

## References

1. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (first submitted April 12, 2018), https://arxiv.org/abs/1804.04548 .
2. S. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108 (first submitted December 23, 2019), https://arxiv.org/abs/1912.11108 .
3. T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences, E107.A(3), 409–416 (2024); publicly available September 5, 2023, https://doi.org/10.1587/transfun.2023TAP0015 .
