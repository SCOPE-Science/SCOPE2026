# The first loss of binary substring-composition information under two-moment compression

## Finding
For a binary word \(w=w_1\cdots w_n\), let \(h_{i,k}(w)=\sum_{j=i}^{i+k-1}w_j\), for \(1\le k\le n\) and \(1\le i\le n-k+1\). The **full length-resolved substring-composition observation** \(\mathcal H(w)\) records, for every \(k\), the entire multiset of the integers \(h_{i,k}(w)\), with multiplicities. The **two-moment compression** \(\mathcal Q(w)\) records only the two sums
\[
M_{r,k}(w)=\sum_{i=1}^{n-k+1}h_{i,k}(w)^r,\qquad r\in\{1,2\},\quad 1\le k\le n.
\]
All words here are indexed, finite and linear; reversal is not quotiented out in the counts.

**Theorem (sharp first compression loss).** For every \(1\le n\le10\) and every two binary length-\(n\) words \(u,v\), equality \(\mathcal Q(u)=\mathcal Q(v)\) implies equality \(\mathcal H(u)=\mathcal H(v)\). At \(n=11\), precisely **two** two-moment fibers contain more than one full-composition fiber:

- \(\{\mathtt{00100111001},\mathtt{10011100100},\mathtt{00110110001},\mathtt{10001101100}\}\);
- \(\{\mathtt{01100011011},\mathtt{11011000110},\mathtt{01110010011},\mathtt{11001001110}\}\).

Each four-word fiber splits into exactly two full-observation fibers, each a reversal pair. There are exactly \(1050\) distinct two-moment observations at \(n=11\) but \(1052\) full-composition observations. Furthermore, adding just **one cubic statistic**, \(M_{3,3}(w)=\sum_{i=1}^{n-2}h_{i,3}(w)^3\), to \(\mathcal Q(w)\) recovers the entire \(\mathcal H(w)\) for every \(1\le n\le11\). No cubic statistic at window length one or two can supply new information beyond the two moments.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\) with the ordinary Hamming-weight interpretation. A length-\(k\) substring starts at each of the \(n-k+1\) indexed positions; all overlapping instances count, including multiplicities of equal weights. Moment sums use **raw integer power sums**, not normalized variance or standard deviation. The claim is a complete finite classification for \(n\le11\), with no claim about longer words or noisy measurements.

The full observation can equivalently be encoded by the nonnegative integers
\[
c_{k,j}(w)=\#\{i:h_{i,k}(w)=j\},\quad 1\le k\le n,\ 0\le j\le k.
\]
Then \(M_{r,k}=\sum_{j=0}^{k}j^r c_{k,j}\), so equality of full observations implies equality of two-moment observations, but the converse is the question investigated.

## Proof
All cases belong to a fixed finite domain of \(2+4+\cdots+2048=4094\) binary words. The included deterministic, standalone `verify.py` is an exhaustive proof certificate, not a sample. For each \(1\le n\le11\), it visits each integer \(0\le x<2^n\) exactly once and converts it to its unique fixed-width binary word. For every word, length, and position, the program forms every substring weight as the difference of two integer prefix sums. It accumulates **all** counters \(c_{k,j}\) and then obtains both moments by the displayed integer formula. It partitions the complete word set by equality of the moment vector, and within each moment fiber partitions again by equality of the full counter array. No cases are omitted, no hashes substitute for comparing actual signatures, and all arithmetic is exact.

For lengths \(1,\ldots,11\), the numbers of distinct moment vectors are
\[
2,3,6,10,20,36,72,135,272,528,1050.
\]
The program confirms that all fibers have one full observation through length ten. At length eleven the moment-fiber size distribution is \(64\) singletons, \(980\) doubletons and \(6\) four-word fibers, while the full-observation size distribution is \(64\) singletons, \(984\) doubletons and \(4\) four-word fibers. The only two moment fibers that split are exactly those written in the finding; within each, the two full profiles are reversal pairs. These integer identities also verify the population total, e.g. \(64+2(980)+4(6)=2048\).

For the two nonreversal representatives in the first exceptional fiber, \(\mathtt{00100111001}\) and \(\mathtt{00110110001}\), the cubic length-three sums are respectively \(49\) and \(43\). For \(\mathtt{01100011011}\) and \(\mathtt{01110010011}\), they are respectively \(50\) and \(56\). Reversal leaves every length-resolved substring-weight multiset unchanged. Thus one additional cubic length-three sum separates both exceptional four-word fibers, while all other fibers were already homogeneous for \(\mathcal H\). Finally, weights of length-one windows belong to \(\{0,1\}\), and weights of length-two windows belong to \(\{0,1,2\}\); on the latter set the identity \(t^3=3t^2-2t\) holds. Therefore cubic sums at lengths one or two add nothing to the two-moment readout. The degree-three statistic at length three is the shortest-window cubic addition capable of repairing the observed loss.

## Verification
Run `python verify.py` using Python 3.10 or later. The program implements two independent exact methods for the same profiles: prefix-sum differences and a second direct summation over every substring. Their results are checked for **each** of the \(4094\) source words. It additionally asserts all listed moment-class counts, the exact exceptional word sets, the length-eleven fiber-size histogram, the distinct full-observation count, and sufficiency of the extra cubic statistic. The observed terminal line is `VERIFY_OK: all 4094 binary sources of lengths 1..11 checked by two methods`.

## Relationship to prior work
Acharya, Das, Milenkovic, Orlitsky and Pan introduced reconstruction from complete substring-composition multisets. Their 2010 conference paper explicitly lists the first nonreversal **full-composition** ambiguity at length eight and further full-composition collisions at eleven; their 2014 preprint provides a polynomial factorization framework. Those full-observation collisions also collide under any moment compression, but they do not determine when two-moment fibers first split into *different* full observations. The present statement concerns the **additional** identifications caused solely by two-moment compression and the least-window-degree cubic repair, not the known full-observation reconstruction theorem.

Published work on partial composition observations, including Ye and Elishco (2022), considers subsets of observed individual compositions such as prefix–suffix reads or bounded-length reads; these are not the length-resolved pooled moment channel. An indexed full-composition census through length twenty-three independently reports \(1052\) full observations at length eleven, consistent with the second count above, but does not provide the two-moment quotient or its two exceptional fibers. No claim of global uniqueness or priority certification is made.

## Limitations
This is a sharp **finite** threshold and classification, not an all-length characterization. Exactness follows from exhaustive deterministic code with transparent indexing and an independent implementation; computation is proof only because all \(2^n\) binary words in the stated finite range are actually examined. The physical availability of separately measured length-resolved power sums is an idealized readout assumption. No result is asserted about alphabet sizes above two, statistical noise, or lengths twelve and higher. Earlier uncatalogued treatment of this particular two-moment compression remains a residual priority risk. The relevant 2010 conference record specifies a June 13–18 public-event interval, not a verified individual-paper release day.

## References
1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *On Reconstructing a String from its Substring Compositions*, ISIT 2010, pp. 1238–1242, https://doi.org/10.1109/ISIT.2010.5513668. Public author manuscript: https://people.ece.cornell.edu/acharya/papers/rcn_str_sbs.pdf.
2. The same authors, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, first public preprint 2014-03-10, https://arxiv.org/abs/1403.2439.
3. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, initial submission 2022-08-31, https://arxiv.org/abs/2208.14963.
4. *Exact composition-multiset ambiguity spectrum for binary words of lengths \(1\)–\(23\)*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-composition-multiset-ambiguity-spectrum-for-binary-words-o--1ad4f8d99e9e/RESULT.md.
