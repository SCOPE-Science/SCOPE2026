# Sharp two-gram ambiguity in \(k\)-Stirling permutations

## Finding

Fix integers \(k\ge 2\) and \(n\ge 1\). A \(k\)-Stirling permutation of order \(n\) is a linear word on the ordered alphabet \(\{1,\ldots,n\}\), with exactly \(k\) copies of each letter, such that all letters strictly between any two consecutive copies of \(i\) are greater than \(i\). Its *two-gram observation* is the complete array \(m_{ab}(w)\) of numbers of oriented adjacent factors \(ab\). Because the symbol multiplicities are fixed, this observation is also the full two-Abelian profile (the length-one counts add no information).

For every attainable profile \(p\), its inverse fiber \(\mathcal F(p)\) consists only of the \(k\)-Stirling permutations having that profile. Then:

1. Every fiber is computed **exactly** by a deterministic largest-label reduction and a product of adjacent-pair counts (described below). This is a constructive enumeration and decoding procedure for every attainable profile, not only an extremal bound.
2. For all \(k\ge2\), \(\max_p |\mathcal F(p)|=(k-1)^{n-1}\). When \(k\ge3\) and \(n\ge2\), there is exactly **one** profile attaining the maximum; for \(k=2\), every fiber is a singleton.
3. For \(k\ge3\), a source is uniquely reconstructible within this class if and only if each label forms a single homogeneous block. Consequently exactly \(n!\) source words, and exactly \(n!\) profiles, have singleton fibers.
4. The uniform-source unique-reconstruction probability for \(k\ge3\) is exactly
   \[
   \frac{n!}{\prod_{j=1}^{n-1}(kj+1)}
   =\frac{\Gamma(1/k)\Gamma(n+1)}{k^n\Gamma(n+1/k)}
   \sim \Gamma(1/k)n^{1-1/k}k^{-n}
   \]
   as \(n\to\infty\) for fixed \(k\). The classical source-cardinality product in this formula is not itself a new enumeration.

The first nonunique case for \(k\ge3\) occurs at \(n=2\): the \(k-1\) words \(1^i2^k1^{k-i}\), \(1\le i<k\), have the same profile, distinct from those of \(1^k2^k\) and \(2^k1^k\).

## Assumptions and scope

Profiles are **linear, oriented, overlapping** adjacent-letter multiplicities. The alphabet is labeled and totally ordered, with the order forming part of the source constraint. The decoder knows \(k,n\). The receiver does not record symbols beyond the complete length-one and length-two factor counts. The competing words in each fiber are restricted to \(k\)-Stirling permutations, rather than all words with the same letter composition. No identification under reversal, cyclic rotation, or letter relabeling is made. In particular, the result does not assert unique reconstruction in the unrestricted word space.

## Proof

**Lemma 1 (visibility and pair multiplicities).** In any \(k\)-Stirling word, the \(k\) copies of the largest label are consecutive. For distinct labels \(a,b\), the oriented factor \(ab\) appears at most once. Indeed, two occurrences of \(ab\) would interlace copies of \(a\) and \(b\); if \(a<b\), the second \(a\) would lie between the two \(b\)'s, and if \(a>b\), the first \(b\) would lie between the two \(a\)'s, contradicting the defining condition. Finally \(m_{aa}\le k-1\), with equality precisely when all copies of \(a\) are consecutive: if the \(k\) copies occupy \(r\) maximal homogeneous runs then \(m_{aa}=k-r\).

**Lemma 2 (profile reduction and exact inverse branching).** For an attainable order-\(j\) profile \(p_j\), with \(j\ge2\), the factor \(j^k\) has \(k-1\) internal \(jj\)-pairs and is adjacent to zero or one lower label on each side. The observation determines which of these three mutually exclusive types occurs:

- At the left boundary, it sees exactly one \(jb\) with \(b<j\); delete \(m_{jj}=k-1\) and that \(jb\) to obtain the unique reduced profile \(p_{j-1}\). Each reduced source has exactly one compatible left-boundary insertion.
- At the right boundary, analogously one \(aj\) is deleted, with one compatible right-boundary insertion.
- In the interior, there are exactly one \(aj\) and one \(jb\), with \(a,b<j\). Delete these and the \(k-1\) occurrences of \(jj\), and add one \(ab\); this uniquely determines \(p_{j-1}\). Every reduced source has exactly \(m_{ab}(p_{j-1})\) compatible insertion gaps.

The symbol multiplicities and adjacent-factor array determine the endpoints of every reduced source, since \(k-\sum_bm_{ab}\) indicates whether \(a\) is its last letter and \(k-\sum_bm_{ba}\) whether it is first. Thus the boundary cases also depend only on profiles. Every insertion of \(j^k\) into a reduced \((k\)-Stirling) source is again permitted, since \(j\) is largest. Distinct inserted words have distinct pairs of (reduced source, insertion position). Therefore, writing \(f(p)=|\mathcal F(p)|\), the exact recurrence is

\[
 f(p_j)=\begin{cases}
 f(p_{j-1}),&\text{boundary insertion},\\
 m_{ab}(p_{j-1})f(p_{j-1}),&\text{interior insertion between }a,b,
 \end{cases}
 \qquad f(p_1)=1.
\]

This also gives a necessary-and-sufficient **realizability algorithm** for a candidate spectrum: perform the stated reductions, require precisely the indicated largest-label pattern and nonnegative reduced counts, require that each indicated boundary letter matches the endpoint inferred from the reduced counts (or that the interior \(ab\) count be positive), and terminate with the sole order-one profile \(m_{11}=k-1\). Every passing step can be inverted, constructing all source words. With the fixed length-one counts, all candidates have precisely \(k\) of every label and \(kj-1\) total two-gram factors at stage \(j\).

**Worst-case bound.** Lemma 1 shows that each inverse branching factor in Lemma 2 is at most \(k-1\); there are \(n-1\) reduction stages. Hence \(f(p)\le(k-1)^{n-1}\). To attain equality, start with \(1^k\), and at stage \(j\) insert \(j^k\) into one of the \(k-1\) gaps between consecutive copies of the still-contiguous \((j-1)^k\). Each resulting two-gram profile is independent of which of those gaps is chosen, and all stages contribute factor \(k-1\). Therefore the upper bound is attained.

When \(k\ge3\), the maximizing profile is unique, by induction. At stage \(1\) its only fully contiguous label is \(1\). In any maximizing profile at stage \(j>1\), the preceding profile must maximize the fiber and the last insertion must have branching factor \(k-1\). In every representative of the unique preceding maximizing profile, the only fully contiguous label is \(j-1\): this holds because insertion inside \((j-2)^k\) splits that block into nonempty pieces while leaving the new \((j-1)^k\) whole. Thus the only maximum-factor insertion is inside \((j-1)^k\), and its resulting profile is independent of the particular gap. For \(k=2\), every nonloop pair occurs at most once and every loop at most once, so all inverse branching factors equal one.

**Singleton characterization.** Assume \(k\ge3\). A concatenation of the \(n\) distinct blocks \(1^k,\ldots,n^k\) can be built by inserting each largest block only at boundaries between existing blocks or at the ends. Every such insertion has branching factor one, so its profile has a singleton fiber. Conversely, for any word with a noncontiguous label, consider the first stage during deletion-reversed construction at which some block ceases to be contiguous. Before that insertion, all existing blocks are contiguous, and the inserted largest block splits a run \(a^k\); its inverse branching factor is \(m_{aa}=k-1\ge2\). Subsequent fiber factors are positive integers, so the final profile is non-singleton. There are exactly \(n!\) permutations of the homogeneous blocks, giving the count of singleton words and profiles.

**Probability.** The standard largest-label insertion recurrence gives \(|\mathcal S_{k,n}|=\prod_{j=1}^{n-1}(kj+1)\). Divide the \(n!\) singleton words by this product and apply \(\Gamma(n+1)/\Gamma(n+1/k)\sim n^{1-1/k}\) to obtain the stated asymptotic.

## Verification

The standalone `verify.py` generates every source by independent largest-label position insertion, groups sources by directly enumerated two-grams, and compares the empirical multiplicities against a separate **profile-only** reduction algorithm. It checks all cases \(2\le k\le4\), \(1\le n\le5\), and \(k=5\), \(1\le n\le4\). The test also checks the exact source-size product, maximum fiber, uniqueness of the maximizing profile, singleton count, and singleton-block criterion. The finite tests are consistency checks, **not** a substitute for the preceding all-length arguments.

For \(k=3\), the numbers of attainable profiles at orders \(n=1,2,3,4,5\) are \(1,3,16,123,1234\); the worst fibers are \(1,2,4,8,16\), and the singleton profiles are \(1,2,6,24,120\). For \(k=4\), these three sequences are respectively \(1,3,16,124,1263\), \(1,3,9,27,81\), and \(1,2,6,24,120\).

Run `python3 verify.py` from the directory containing this document. Its output finishes with a `PASS` statement only after all assertions hold.

## Relationship to prior work

Janson, Kuba and Panholzer (2008, arXiv:0805.4084v1), Section 2.1, establish the underlying \(k\)-Stirling insertion construction and source cardinality; their Theorems 1 and 2 and Section 5 concern tree bijections and ascent/descent/plateau statistics, not full labeled directed-pair spectra or inverse-fiber extremizers. Karhumäki, Saarela and Zamboni (2013, arXiv:1301.5104v1), Definition 2.1 and Lemma 2.3, establish two-Abelian factor-count equivalence and its endpoint characterization; their main counts address unrestricted words and infinite-word complexity, not the present constrained family. González D'León (2016) studies selected ascending adjacent-pair statistics of ordinary Stirling permutations, rather than equality of *all* oriented pair multiplicities. These foundational results are used, not claimed as novel.

The novelty claimed here is the all-parameter *restricted-source* exact fiber reduction, exponential sharp maximum with its unique profile, and exact singleton reconstruction criterion/probability for \(k\ge3\). Established unique reconstruction of noncrossing double-occurrence words already implies the \(k=2\) boundary case, which is included only for completeness. General Euler-trail counting of arbitrary strings does not automatically impose the nested Stirling condition or give the stated extremal restricted fibers.

## Limitations

All uniqueness and fiber statements are **relative to the \(k\)-Stirling language**. They do not establish reconstruction among unrestricted multipermutations, nor a formula for the *total number* of attainable two-gram profiles for arbitrary \(k,n\). The reconstruction algorithm is constructive, but its full output can be exponentially large. The recurrence and sharp extremal law are mathematical deductions from the class's insertion property, and this proximity to the known insertion construction is a remaining originality risk; earlier equivalent restrictions of general Euler-trail enumerations cannot be ruled out solely through indexed search.

## References

1. S. Janson, M. Kuba, and A. Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, arXiv:0805.4084v1, first publicly posted 2008-05-27, https://arxiv.org/abs/0805.4084 .
2. J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, first publicly posted 2013-01-22, https://arxiv.org/abs/1301.5104 .
3. R. S. González D'León, *A note on the γ-coefficients of the tree Eulerian polynomial*, Electronic Journal of Combinatorics 23(1), P1.20, first published 2016-02-05, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p20/pdf/ .
