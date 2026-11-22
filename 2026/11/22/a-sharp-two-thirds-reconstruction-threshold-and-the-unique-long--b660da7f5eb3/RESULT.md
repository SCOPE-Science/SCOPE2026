# A sharp two-thirds reconstruction threshold and the unique long-read ambiguity fiber of binary two-marker words

## Finding

For every integer \(n\ge5\), let \(\mathcal B_{n,2}\) be the set of length-\(n\) binary words with exactly two ones. A *linear length-\(k\) read multispectrum* \(\mathcal M_k(w)\) is the multiset of all \(n-k+1\) contiguous length-\(k\) factors, counted with multiplicity and with neither circular wraparound nor reversal identification.

**Theorem.** For each integer \(k\) satisfying \((n+1)/2<k\le n\), put
\[
r=n-k+1,\qquad c=k-r-1,\qquad m=r-c=2n-3k+3.
\]
Every equivalence class of \(\mathcal M_k\) on \(\mathcal B_{n,2}\) is a singleton except possibly one. If \(m\ge2\), that exceptional class has exactly \(m\) words, whose zero-based one-positions are
\[
(a,a+r),\qquad c\le a\le r-1.
\]
If \(m\le1\), the multispectrum map is injective. The number of distinct multispectra is therefore
\[
\binom n2-\max\{0,m-1\}.
\]
Moreover the exact smallest read length permitting unique reconstruction of **every** word in this fixed-weight family is
\[
\boxed{\kappa(n)=\left\lfloor\frac{2n+1}{3}\right\rfloor+1}\qquad(n\ge5).
\]
This is a sharp *in-class* reconstruction statement. It does not assert reconstruction among words of unknown weight or under a set-only read channel.

## Assumptions and scope

All word indices and read starts are zero-based. Fix \(n\ge5\), \(1\le k\le n\), and two one-positions \(0\le a<b\le n-1\). The read starts are exactly \(t=0,\ldots,r-1\), where \(r=n-k+1\). Their order is discarded, but multiplicities and within-read letter order remain known. Unless specified otherwise the proof of the fiber classification uses \(k>r\), equivalent to \(k>(n+1)/2\). No periodic boundary condition is imposed on the input.

## Proof

**Step 1: reads containing at most one one when the gap is long.** Set \(d=b-a\). If \(d\ge k\), no length-\(k\) factor contains both ones. The indices of the unique one within the one-containing reads form the disjoint union of integer intervals
\[
[0,a]\ \dot\cup\ [b-r+1,k-1].
\]
Indeed \(a\le r-2\), \(b\ge k\), and their separation is strict because \(b-r+1-a=d-r+1>0\). The first interval starts at zero and the second ends at \(k-1\). The spectrum hence recovers their endpoints, which recover \(a\) and \(b\) uniquely.

**Step 2: paired reads when the gap is short.** Suppose \(1\le d<k\). A factor containing both ones occurs, and the difference between their within-read positions equals \(d\); hence \(d\) itself is known from the multiset. Put \(c=k-d-1\). In all two-one reads the first one occupies precisely the consecutive positions
\[
[A,B]=[\max(0,a-r+1),\min(a,c)],
\]
with each value appearing once. This interval is nonempty since the two markers can be covered by a length-\(k\) window. As a function of \(a\), its endpoints identify \(a\) uniquely unless both endpoints are constant. The only possible non-singleton plateau is
\[
c\le a\le r-1,
\]
on which \([A,B]=[0,c]\). The plateau can have more than one element only when \(c<r-1\).

**Step 3: distinguish every plateau position except at gap \(d=r\).** For a plateau word, the single-one reads have within-read one-positions, counted with multiplicity, in the interval multiset
\[
[c+1,a]\ \uplus\ [a+d-r+1,d-1],
\]
where an interval with lower endpoint exceeding its upper endpoint is empty. Increasing \(a\) by one adds the value \(a+1\) to the first interval and removes the value \(a+d-r+1\) from the second. Therefore the sum of the one-positions across the single-one reads changes by exactly \(r-d\). For \(d\ne r\) this nonzero increment distinguishes every plateau member. For \(d=r\), the two intervals become
\[
[c+1,a]\ \uplus\ [a+1,r-1]=[c+1,r-1],
\]
independent of \(a\). The two-one reads also have the same complete within-read patterns, because \(d=r\) and \([A,B]=[0,c]\). Zero-only reads are determined by subtracting the numbers of one- and two-one reads from the fixed total \(r\). Thus all plateau words have identical multispectra and no further collisions exist.

**Step 4: count the exceptional class.** For \(d=r\), \(c=k-r-1\), so exactly the integers \(a=c,c+1,\ldots,r-1\) realize the plateau. Their count is \(m=r-c=2n-3k+3\). These are valid global one-positions since \(k>r\). Replacing the \(m\) distinct input words by one output class decreases the number \(\binom n2\) of spectra by \(m-1\) if \(m\ge2\), and by zero otherwise.

**Step 5: sharp reconstruction threshold, including all shorter reads.** The exceptional fiber disappears once \(m\le1\), equivalent to
\[
k\ge\left\lceil\frac{2n+2}{3}\right\rceil=\left\lfloor\frac{2n+1}{3}\right\rfloor+1.
\]
For \(n\ge5\), this read length satisfies \(k>(n+1)/2\), so Steps 1–4 prove injectivity there and at all longer lengths.

To show every shorter length fails, first at \(k=1\) all weight-two words have identical observations. At \(k=2\), the two distinct words with one-positions \((0,2)\) and \((0,3)\) have the same bigram multiset for \(n\ge5\). For each remaining length
\[
3\le k\le\left\lfloor\frac{2n+1}{3}\right\rfloor,
\]
write \(r=n-k+1\) and choose an integer
\[
\max(0,n-2r)\le a\le \min(r-1,n-r-1).
\]
This interval contains at least two distinct integers: if \(r>n/2\), its lower endpoint is zero and upper endpoint is at least one; if \(r\le n/2\), its length is at least two because \(3r\ge n+2\). Each choice defines a valid weight-two word with one-positions \((a,a+r)\), equal to the first \(n\) symbols of an infinite period-\(r\) word with a single one in residue class \(a\). The \(r\) consecutive length-\(k\) windows sample each starting phase modulo \(r\) exactly once. Their entire multispectrum is therefore independent of \(a\), proving distinct confusable words at every shorter length. This completes the proof.

## Verification

The included `verify_spectrum.py` enumerates complete multispectrum fibers independently of the symbolic proof, for every \(5\le n\le56\) and every \(k>(n+1)/2\), and compares the entire non-singleton-class list against the theorem. It separately tests the sharp first-injective threshold for all \(5\le n\le34\). The included `verify_witness.py` checks all admissible construction parameters for every \(5\le n\le120\) and \(3\le k\le\lfloor(2n+1)/3\rfloor\). Outputs are in the adjacent `.out` files and the code runs with the Python standard library alone. These finite checks support, but do not replace, the universal proof above.

## Relationship to prior work

The February 2026 work of Chakraborty, Grossi, Kimura, Punzi, Sadakane and Zuba concerns representations preserving the **set** of distinct \(k\)-mers for compression; it does not give a fixed-weight, multiplicity-sensitive reconstruction classification. Angal and collaborators (October 2026) study length-\(k\) *scattered subsequence* decks, also with fixed-weight classes, which is a different observation channel: the present theorem reads **contiguous factors only**. Alekseev–Smetanin (2022) likewise study fragment reconstruction using nonconsecutive selections; their sufficient bounds do not settle this linear contiguous-read result. Related exact length-three multiset-profile calculations for sparse words do not imply this uniform long-read theorem, its single exceptional class, or the sharp threshold. The proof does not claim novelty of elementary periodic-window rotation itself.

## Limitations

This is an in-class theorem conditioned on the known fixed weight two. It does not extend to arbitrary weights, circular reads, noisy or missing reads, sets of reads without multiplicities, or equivalence allowing reverse complement. A complete independent audit and comprehensive historical priority determination have not been performed.

## References

- S. Chakraborty, R. Grossi, R. Kimura, G. Punzi, K. Sadakane, W. Zuba, *Variations on the Problem of Identifying Spectrum-Preserving String Sets*, arXiv:2602.19408v1, posted February 23, 2026. https://arxiv.org/html/2602.19408v1
- K. Angal et al., *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1, posted October 30, 2026. https://arxiv.org/html/2610.41110v1
- V. A. Alekseev and Yu. G. Smetanin, *On the Word Fragment Length for Unambiguous Reconstruction of a Periodic Word from a Complete Multiset of Fragments of Fixed Length*, *Doklady Mathematics* 105 (2022), DOI:10.1134/S106456242202003X. https://doi.org/10.1134/S106456242202003X
