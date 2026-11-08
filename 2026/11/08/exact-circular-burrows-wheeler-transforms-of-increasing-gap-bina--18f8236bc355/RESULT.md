# Exact circular Burrows–Wheeler transforms of increasing-gap binary words

## Finding

Let \(k\ge2\) and let \(1\le g_1<g_2<\cdots<g_k\) be integers. Set \(g_0=0\), \(d_j=g_j-g_{j-1}\), and form the binary word

\[
W(g_1,\ldots,g_k)=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_k}1.
\]

Here \(0<1\), and \(\operatorname{BWT}_{\rm cyc}\) is the **circular** Burrows–Wheeler transform: sort all full-length cyclic rotations lexicographically and read the letter preceding each rotation. No terminal/sentinel symbol is added. Then the **entire transform**, not only its run count, is

\[
\boxed{\operatorname{BWT}_{\rm cyc}(W)=
1\,0^{d_k-1}1
\left(\prod_{j=k-1}^{2}0^{(k-j+1)d_j}1\right)
0^{k d_1}10.}
\]

The product is ordered by decreasing \(j\); it is empty for \(k=2\). In particular, the number \(r\) of maximal equal-letter runs obeys

\[
\boxed{r(\operatorname{BWT}_{\rm cyc}(W))=
2k+2-2\mathbf1_{\{d_k=1\}}.}
\]

The input \(W\) has \(2k+1\) runs. Thus, on this full class of increasing-gap words, the transform adds exactly one run when the largest gap exceeds the next largest by at least two; otherwise it removes exactly one. The displayed expression computes a run-length encoding in \(O(k)\) arithmetic operations without constructing the input of length \(k+1+\sum_{j=1}^k g_j\).

As a natural lacunary instance, for integers \(b\ge3\) and \(k\ge2\), let \(P_{b,k}\) be the binary length-\(b^k\) word whose ones are exactly at zero-based positions \(b^j-1\), \(0\le j\le k\). Its zero gaps satisfy

\[
g_1=b-2,\qquad g_j=(b-1)b^{j-1}-1\quad(2\le j\le k),
\]
\[
d_1=b-2,\qquad d_j=(b-1)^2b^{j-2}\quad(2\le j\le k).
\]

Hence the displayed formula gives every run length of \(\operatorname{BWT}_{\rm cyc}(P_{b,k})\) explicitly and \(r=2k+2\).

## Assumptions and scope

The alphabet is the ordered binary alphabet \(\{0,1\}\), with strictly increasing **positive** internal zero-gap lengths and an additional adjacent pair of ones across the circular boundary. There are \(k+1\) ones. Every rotation is distinct: a nontrivial power would repeat the unique maximal circular zero run of length \(g_k\). All equalities are exact for every indicated integer parameter. Circular BWT without a sentinel is essential; this is not a claim for sentinel-terminated BWT or an arbitrary order of zero gaps.

## Proof

**Step 1: Classification and ordering of zero-starting rotations.** Every rotation beginning with a zero has a unique representation starting with \(0^t1\), where \(1\le t\le g_j\) and \(j\in\{1,\ldots,k\}\) identifies the containing zero gap. For each fixed \(t\), there is exactly one such rotation for each \(j\) with \(g_j\ge t\). If two rotations have different \(t\), the one with the larger \(t\) sorts first (its next distinguishing symbol is zero instead of one). Fix \(t\) and write \(m=\min\{j:g_j\ge t\}\). After the common prefix \(0^t1\), the next circular zero-run has length \(g_{j+1}\) if \(j<k\), and length \(g_0=0\) if \(j=k\). These lengths are distinct, so the within-bucket lexicographic order of the gap indices is precisely

\[
(k-1),(k-2),\ldots,m,k.
\]

This fully determines the order, without comparing the remaining suffixes of the rotations. The BWT letter contributed by the rotation indexed by \((t,j)\) is one if and only if \(t=g_j\), because that is exactly when the starting zero is immediately preceded by a one. Otherwise the preceding letter is zero.

**Step 2: Location of the ones in the zero-starting block.** The buckets occur in descending order \(t=g_k,g_k-1,\ldots,1\). A bucket has a one precisely when \(t=g_j\). The first bucket \(t=g_k\) consists of one row and contributes an initial one. At \(t=g_j\) for \(j<k\), the one is penultimate in the bucket, with a final zero contributed by \(j=k\). Thus consecutive ones in the zero-starting block are separated initially by \(d_k-1\) zeros, then by exactly \((k-j+1)d_j\) zeros for each \(j=k-1,k-2,\ldots,2\). To see the latter count, take the trailing one zero in the bucket \(t=g_j\), the \(d_j-1\) full intermediate buckets each of size \(k-j+1\), and the \(k-j\) zero entries preceding the one in bucket \(t=g_{j-1}\). The sum is \((k-j+1)d_j\).

**Step 3: One-starting rotations and final boundary.** There are \(k+1\) rotations starting with one, and each is distinguished lexicographically by the following circular zero-run of length \(g_k,g_{k-1},\ldots,g_1,g_0\); hence they sort in exactly that descending order. The one starting at the **first** marker of \(W\) is preceded by the final marker, hence contributes a one, and its following gap is \(g_1\), making it penultimate in this block. All other one-starting rotations contribute zero, including the final row corresponding to gap \(g_0\). Between the one at \(t=g_1\) and this penultimate one there are one trailing zero from that bucket, \(g_1-1\) complete \(k\)-row zero buckets, and \(k-1\) initial zeros of the one-starting block, altogether \(k g_1=k d_1\) zeros. There is then a final zero. Concatenating these blocks proves the complete transform formula.

**Step 4: Run count and marker corollary.** Every zero exponent after the second one is positive because \(d_j\ge1\). The initial two ones are adjacent exactly when \(d_k=1\), reducing the otherwise \(2k+2\) BWT runs by two. The original word starts and ends with one and has exactly \(k\) nonempty zero runs and \(k+1\) one runs, hence \(2k+1\) runs. Finally, the marker positions \(b^j-1\) give the displayed gap and increment identities by subtraction. Since \(d_k\ge4\) when \(b\ge3\) and \(k\ge2\), the marker corollary follows.

## Verification

The independent Python script `verify_bwt.py` builds the input, sorts every actual full cyclic rotation, and compares every output bit against the displayed run-length formula. Its exhaustive small-gap test uses all \(4^k\) increment vectors with \(1\le d_j\le4\) for \(2\le k\le7\), giving \(21{,}840\) complete tests. It also checks \(17\) radix-power-marker prefixes in bases \(3\) through \(7\), with lengths at most \(2400\). The script checks BWT length, ones count, and the claimed run count. Run with `python3 verify_bwt.py` using Python 3 and the standard library. These finite checks test implementation and boundary behavior; they do not replace the general proof.

## Relationship to prior work

Frosini et al. (2022) prove logarithmic BWT-run bounds for purely morphic binary words, without providing this complete output on arbitrary increasing zero-gap vectors. Fici et al. (2023) study changes in BWT runs under morphisms, a different parameterization. Giuliani et al. (first publicly posted 2024; journal article 2025), Section 4, Proposition 18, explicitly use **increasing polynomial zero gaps** and infer the BWT run count for those specialized words. This is a genuine close antecedent, including the observation that rotation ordering depends on the next gap; the run-count phenomenon for that polynomial subclass is **not** claimed as new. The present statement instead provides the entire transform (individual run lengths and precise order), uniformly for **every arbitrary strictly increasing integer gap vector**, including the adjacent-end-marker boundary, with an exact boundary transition. Brlek et al. (2019) analyze transforms of other morphic families. No inference about unpublished or unindexed results follows from an unsuccessful search.

## Limitations

No conclusion is asserted for nonmonotone or tied positive gaps, for arbitrary binary words, or for sentinel-terminated transforms. The general theorem is elementary in mechanism and closely related to the rotation-bucket reasoning in Giuliani et al.; a broader unpublished or unindexed formulation may already subsume it. The verification is exhaustive only over the specified finite test domains. No independent formal proof or external audit has been performed.

## References

- A. Frosini, I. Mancini, S. Rinaldi, G. Romana, and M. Sciortino, *Logarithmic Equal-Letter Runs for BWT of Purely Morphic Words* (first posted 2022-02-05), https://arxiv.org/abs/2202.02609 .
- G. Fici et al., *On the Impact of Morphisms on BWT-Runs* (CPM 2023), https://doi.org/10.4230/LIPIcs.CPM.2023.10 .
- S. Giuliani, S. Inenaga, Z. Lipták, G. Romana, M. Sciortino, and C. Urbina, *Bit Catastrophes for the Burrows–Wheeler Transform* (first posted 2024-04-16; Theory of Computing Systems, 2025), https://arxiv.org/abs/2404.10426 and https://doi.org/10.1007/s00224-024-10212-9 .
- S. Brlek et al., *Burrows–Wheeler Transform of Words Defined by Morphisms* (2019), https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf .
