# A sharp sparse-weight law for circular Burrows–Wheeler runs

## Finding

Let \(n\ge2\) and \(1\le k<n\). For a binary word \(w\in\{0,1\}^n\) of weight \(k\), let \(B(w)\) be its *sentinel-free circular Burrows–Wheeler transform*: sort all \(n\) full cyclic rotations lexicographically (including multiplicity) and read the preceding character of each rotation. Let \(r(w)\) be the number of ordinary *linear* constant-letter runs of \(B(w)\). Write \(g_1,\ldots,g_k\) for the nonnegative numbers of zeroes between consecutive ones in cyclic order, and let \(p_{\le k}(m)\) be the number of integer partitions of \(m\) into at most \(k\) parts, with \(p_{\le k}(0)=1\) and \(p_{\le k}(m)=0\) for \(m<0\).

**Theorem.** Every mixed binary word of weight \(k\) satisfies \(r(w)\le 2k\). If its cyclic zero-gap lengths are positive and pairwise at distance at least two, i.e. \(g_i\ge1\) and \(|g_i-g_j|\ge2\) for all \(i\ne j\), then **equality holds**: \(r(w)=2k\).

The number of indexed length-\(n\) weight-\(k\) binary words satisfying that sufficient gap condition is exactly
\[
\boxed{n(k-1)!\,p_{\le k}\bigl(n-k(k+1)\bigr).}
\]
Such words are primitive, and their necklace count is exactly \((k-1)!p_{\le k}(n-k(k+1))\). In particular the bound \(2k\) is attainable at every length \(n\ge k(k+1)\); the condition is sufficient, **not necessary**, for equality.

If \(W_{n,k}\) is uniform among the \(\binom nk\) indexed length-\(n\) words with exactly \(k\) ones, then
\[
\boxed{\Pr\{r(W_{n,k})=2k\}\ge\max\left\{0,\ 1-\frac{k^2(k-1)}{n-1}\right\}.}
\]
Consequently, for every sequence \(k=k(n)\ge1\) with \(k=o(n^{1/3})\) and \(k<n\), the circular BWT has its maximum possible \(2k\) linear runs with probability tending to one. This includes every fixed positive weight, for which the failure probability is \(O_k(n^{-1})\).

## Assumptions and scope

Alphabet order is \(0<1\), and the circular transform has **no sentinel**. All rotations are counted, even when an input is periodic. The run count is *linear*: the first and last BWT positions are not joined. Indexed words are counted separately, including distinct rotations. The necklace count concerns primitive necklaces only. No arbitrary-weight population equality is claimed: the displayed partition formula counts the explicit *certified family* with separated positive gaps, which is a subset of the maximum-run population.

## Proof

**1. Universal bound.** Since \(0<k<n\), both letters occur. The lexicographically first full cyclic rotation begins at the start of a longest zero run: such a rotation has as many leading zeroes as possible and is preceded by a one. Therefore \(B(w)\) starts with \(1\). The transform is a permutation of the input letters, so it contains exactly \(k\) ones. A binary word starting in one and containing \(k\) ones has at most \(k\) one-runs and at most \(k\) zero-runs, hence at most \(2k\) runs in total. (The last rotation also contributes a zero, but that is not needed for the upper bound.) Periodic equal rotations cause no problem: their preceding characters agree.

**2. Separation lemma.** Assume all cyclic zero gaps are positive and pairwise differ by at least two. Label the zero-starting rotations by \((i,t)\), where \(i\) is a zero gap of length \(g_i\) and \(1\le t\le g_i\) is the number of leading zeroes before the following one. Such a rotation begins with \(0^t1\), and its BWT letter is one exactly when \(t=g_i\) (it then starts at the first zero immediately after a one). Rotations with larger \(t\) precede those with smaller \(t\), regardless of any within-level ordering. Thus all zero-starting rotations split into nonempty consecutive levels labeled by decreasing \(t\). There is precisely one marked one in each level \(t=g_i\), and no marked one at any other level. Between any two marked levels, their gap lengths differ by at least two, so an intermediate nonempty level contributes only zeroes. The unique largest-gap level consists of one rotation, whose BWT letter is one. The one-starting rotations follow all zero-starting rotations and all have preceding letter zero, because all gaps are positive (no two ones are adjacent). Consequently \(B(w)\) starts in one and its \(k\) marked ones are pairwise nonadjacent and followed by at least one zero. It therefore has exactly \(2k\) runs.

**3. Exact certified-family enumeration.** Write the strictly increasing rearrangement of the gap multiset as \(h_1<h_2<\cdots<h_k\). The separation condition is equivalent to
\[
h_i=2i-1+d_i,\qquad 0\le d_1\le d_2\le\cdots\le d_k.
\]
Since \(\sum_i h_i=n-k\), necessarily \(\sum_i d_i=n-k(k+1)\). Increasing \(k\)-tuples of nonnegative integers with this sum are partitions into at most \(k\) parts, hence are counted by \(p_{\le k}(n-k(k+1))\). Every admissible distinct gap multiset has \(k!\) labeled cyclic orderings. Circularly shifting the chosen one-root in an oriented necklace identifies exactly \(k\) of these orderings. There are no nontrivial rotational stabilizers because all gaps differ, so each necklace is primitive and has exactly \(n\) distinct indexed word representatives. Thus the necklace count is \(k!p_{\le k}/k=(k-1)!p_{\le k}\), and the indexed word count is \(n(k-1)!p_{\le k}\). All steps also hold for \(k=1\); the single positive gap is \(n-1\).

**4. Quantitative high-probability bound.** Uniformly sample an indexed weight-\(k\) word and designate one of its \(k\) one-positions uniformly. The resulting rooted cyclic gap vector is uniform among the \(\binom{n-1}{k-1}\) weak compositions of \(N=n-k\) into \(k\) nonnegative parts; the designation does not affect the separation event. A fixed gap vanishes with probability \((k-1)/(n-1)\). For any two fixed gap coordinates, condition on the remaining \(k-2\) coordinates: if their sum leaves \(s\ge0\), the two selected gaps can be written as \((a,s-a)\), with \(s+1\) equiprobable choices, of which at most two obey \(|2a-s|\le1\). Summing over all possible \(s\), the number of bad weak compositions is at most \(2\binom{n-2}{k-2}\) (the hockey-stick identity; for \(k=2\) the same bound follows directly). Thus a specified gap pair violates the distance-two condition with probability at most \(2(k-1)/(n-1)\). A union bound over \(k\) zero-gap events and \(\binom{k}{2}\) close-pair events gives total failure probability at most
\[
\frac{k(k-1)}{n-1}+\binom{k}{2}\frac{2(k-1)}{n-1}
=\frac{k^2(k-1)}{n-1}.
\]
The exact separated-gap count from Step 3 and the sufficiency from Step 2 establish the probability lower bound. If \(k=o(n^{1/3})\), the displayed failure bound tends to zero. This proves all statements.

## Verification

Run `python3 check_exhaustive.py` and `python3 check_gaps.py` from this package using standard Python 3. The former reconstructs the circular transform by sorting every full rotation, checks universal and certified upper/lower run bounds and the partition count on 53,979 indexed words, including certified counts for all tested valid small parameters. The latter independently constructs sorted cyclic-rotation indices from the gap representation, checks 926 separated-gap examples (including all distinct permutations of base gap sets through five markers) and 54 partition parameters. Recorded outputs are in `checks.txt`. These finite tests do not substitute for the general proof. The probability bound was obtained by counting and a union bound, not extrapolated from sampling.

## Relationship to prior work

Giuliani et al., *Bit catastrophes for the Burrows–Wheeler Transform* (arXiv:2404.10426), Section 4, Proposition 15, obtain \(2k\) BWT runs for particular *increasing polynomial gap* constructions; the sparse-gap mechanism is a close antecedent and that special construction is not claimed as new. The accessible published-finding corpus finding *Exact circular Burrows–Wheeler transforms of increasing-gap binary words* treats **strictly increasing gaps in their cyclic order with one adjacent marker pair** and gives the *entire transform*. It does not treat arbitrary permutations of separated positive gaps, the certified-family partition count or the random sparse-weight law. Another published-finding corpus finding classifies **weight three** exactly, including the particular limiting probability \(1-6/n+O(n^{-2})\); a separate weight-four finding tabulates that weight. Those are stronger at fixed small weights but not an all-weight law with growing \(k\). Kumallagov (2026) studies a different extremal question, maximal total run count \(n\) over larger alphabets. Bannai et al. (2025) study BWT compressiveness and its relations to other repetitiveness measures, not this fixed-weight distribution. The contribution here is a uniform all-weight *sufficient* structural criterion, exact counting of its primitive certified examples, and a probability-one regime for \(k=o(n^{1/3})\). No global novelty beyond the inspected sources is asserted.

## Limitations

The separation condition is stronger than necessary; the exact fraction of *all* maximum-run words for general \(k\) is not determined. The \(o(n^{1/3})\) window is a proven sufficient regime and is not claimed to be sharp. The confidence bound may be vacuous at small \(n\), when the exact certified-family count remains valid. The result does not apply to the sentinel-terminated or bijective BWT. An earlier unindexed equivalent random-weight theorem remains possible. No independent mathematical audit has been performed.

## References

- S. Giuliani, S. Inenaga, Z. Lipták, G. Romana, M. Sciortino, and C. Urbina, *Bit catastrophes for the Burrows–Wheeler Transform*, arXiv:2404.10426, first posted April 16, 2024. https://arxiv.org/abs/2404.10426 .
- H. Bannai, T. I, and Y. Nakashima, *On the Compressiveness of the Burrows-Wheeler Transform*, CPM 2025, DOI:10.4230/LIPIcs.CPM.2025.17. https://drops.dagstuhl.de/storage/00lipics/lipics-vol331-cpm2025/html/LIPIcs.CPM.2025.17/LIPIcs.CPM.2025.17.html .
- D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267, first posted May 31, 2026. https://arxiv.org/abs/2606.01267 .
- *Exact run spectrum of the circular Burrows–Wheeler transform for binary words with three ones*, published mathematical finding, November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-run-spectrum-of-the-circular-burrows-wheeler-transform-for--1b2e4b268091/RESULT.md .
- *Exact circular Burrows–Wheeler transforms of increasing-gap binary words*, published mathematical finding, November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-circular-burrows-wheeler-transforms-of-increasing-gap-bina--18f8236bc355/RESULT.md .
