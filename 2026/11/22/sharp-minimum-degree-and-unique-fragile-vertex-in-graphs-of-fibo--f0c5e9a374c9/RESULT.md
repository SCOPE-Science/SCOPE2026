# Sharp minimum degree and unique fragile vertex in graphs of Fibonacci \(q\)-decreasing words

## Finding

For every integer \(q\ge2\), let \(G_{q,n}\) be the subgraph of the binary Hamming cube induced on all length-\(n\) \(q\)-decreasing words, where a word is \(q\)-decreasing if each maximal occurrence of a zero-run immediately followed by a one-run, \(0^a1^b\), with \(a\ge1\), satisfies \(qa>b\). An initial one-run has no restriction. Two vertices are adjacent when exactly one coordinate differs.

Write \(\delta_{q,n}\) for minimum vertex degree, and \(M_{q,n}\) for the number of vertices of that degree. Then, for every \(n\ge1\),

\[
\delta_{q,n}=\min(n,q),\qquad
M_{q,n}=\begin{cases}
2^n & 1\le n\le q,\\
q+1 & n=q+1,\\
2 & n=q+2,\\
1 & n\ge q+3.
\end{cases}
\]

At length \(n=q+2\), the only two minimum-degree vertices are \(1^n\) and \(001^q\). For every \(n\ge q+3\), the unique minimum-degree vertex is \(1^n\). Consequently the minimum local one-substitution connectivity stabilizes at exactly \(q\) while the minimizing vertices become unique at the sharp threshold \(q+3\).

## Assumptions and scope

Integers \(q\ge2\), \(n\ge1\), unrestricted endpoints, indexed fixed-length binary strings; the induced graph uses one-bit flips only. A maximal zero-to-one factor may have a trailing zero-run with \(b=0\), which satisfies the inequality automatically. The special initial one-run is unrestricted. In particular, the graph is not the hypercube graph on words merely avoiding \(1^{q+1}\): those words are equinumerous with the chosen family but need not have the same edges. Degrees count distinct one-bit flips, one per coordinate. No assertion is made for noninteger \(q\) or \(q=1\).

## Proof

**1. Universal lower bound.** Suppose an admissible word has \(t\) ones. In any one-run of length \(b\), flipping any of its last \(\min(b,q)\) ones to zero remains admissible: the newly created zero-run, if followed by ones, is followed by at most \(q-1\) ones; other pre-existing zero-to-one constraints either remain unchanged or become easier because a zero-run lengthens or a one-run shortens. Thus at least \(\sum_j\min(b_j,q)\) flips are legal, where \(b_j\) are the one-run lengths. If \(t\ge q\), this sum is at least \(q\). If \(t\le q-2\), all \(n\) flips are legal, since flipping a zero to one leaves at most \(q-1\) ones and every word with at most \(q-1\) ones is admissible. If \(t=q-1\), flipping any one to zero is legal, and flipping the first zero to one is also legal: it either extends the unrestricted initial one-run, or removes the first zero from a zero-run in front of a one-run shorter than \(q\). Hence the degree is at least \(q\). This proves \(\deg(w)\ge\min(n,q)\), including the case \(n\le q\).

For \(n\le q\), all \(2^n\) binary words satisfy the condition and the graph is the entire \(n\)-cube. For \(n>q\), only the last \(q\) one-to-zero flips in \(1^n\) are legal: any earlier flip produces a zero followed by at least \(q\) ones. Therefore \(\delta_{q,n}=q\).

**2. Exact boundary multiplicities.** At length \(n=q+1\), the sole forbidden word is \(01^q\). Removing it from the \((q+1)\)-cube leaves exactly its \(q+1\) neighbors at degree \(q\); all other vertices have degree \(q+1\).

At length \(n=q+2\), the forbidden words are precisely
\[
01^{q+1},\qquad 01^q0,\qquad 101^q.
\]
The first and second differ in one coordinate, the first and third in two coordinates, and the second and third in three coordinates. A surviving vertex has degree at least \(n-2=q\), and has degree \(q\) precisely when it is adjacent to two of these deleted vertices. Only the distance-two pair has common one-step neighbors: \(1^{q+2}\) and \(001^q\); both are admissible. This proves the formula for \(M_{q,q+2}\).

**3. Uniqueness for \(n\ge q+3\).** Let \(w\ne1^n\) be admissible. We show \(\deg(w)\ge q+1\).

If \(t\le q-2\), all \(n\ge q+3\) flips are legal. If \(t=q-1\), the \(q-1\) one-to-zero flips are legal; among the \(n-q+1\) zero-to-one flips, at most one can be illegal. Indeed an inadmissible word with exactly \(q\) ones must have the form \(01^q0^r\): the only possible violation has a single preceding zero and a run consisting of all \(q\) ones. These bad targets can differ only at their unique extra one, so at most one zero of \(w\) produces such a word. Therefore \(\deg(w)\ge(q-1)+(n-q)=n-1>q\).

If \(t=q\) and \(w\) has at least two one-runs, all \(q\) one-to-zero flips are legal, as no resulting right-hand run has \(q\) ones; the first zero-to-one flip is also legal (it either joins the initial one-run or leaves a shorter zero-run preceding a one-run of length below \(q\)). If \(t=q\) and there is just one one-run, it is either initial, of shape \(1^q0^c\) with \(c>0\), or noninitial, of shape \(0^a1^q0^c\). In the initial case the first trailing zero may also be flipped, joining the prefix run. In the noninitial case admissibility gives \(a\ge2\) and \(a+c=n-q\ge3\). When \(a\ge3\), flip the first zero to one (the remaining \(a-1\) zeros still exceed the required run capacity); when \(a=2\), necessarily \(c\ge1\), and flipping the first trailing zero extends the one-run from \(q\) to \(q+1\), still permitted by \(2q>q+1\). Each case gives an extra zero-to-one flip beyond all \(q\) one-to-zero flips.

Finally take \(t>q\). If there are at least two one-runs, the already established legal last-\(\min(b_j,q)\) flips total at least \(q+1\): either a run contributes \(q\) and another contributes one, or all runs are shorter than \(q\), so all \(t>q\) ones contribute. If there is one noninitial run of length \(t>q\), its *first* one-to-zero flip is also legal: it lengthens the preceding zero-run and shortens the remaining one-run; it is distinct from the last \(q\) flips. If there is one initial run, the word is \(1^t0^c\) with \(c>0\), because \(w\ne1^n\); flipping the first trailing zero to one is legal in addition to the last \(q\) one-to-zero flips. Thus only \(1^n\) has degree \(q\).

These cases exhaust all admissible words and prove every stated range and equality.

## Verification

The accompanying standalone `verify.py` uses a direct run scanner, constructs each admissible binary word and tests every literal one-coordinate flip, and compares the resulting minimum degree, multiplicities and extremal words with the theorem. It completed 63 parameter pairs for \(2\le q\le8\), \(1\le n\le\min(12,q+4)\), covering 16,018 admissible words. Output: `VERIFY_OK parameter_pairs=63 admissible_words=16018`. Finite checks are corroboration only; the exhaustive all-length argument above is the proof.

## Relationship to prior work

Baril, Kirgizov and Vajnovszki introduced and enumerated the same \(q\)-decreasing words, proved equinumerosity with a run-avoiding language and constructed bounded-change Gray listings; their discussion does not supply the induced one-bit-flip graph's minimum degree or equality classification. Wong, Liu, Lam and Im constructed cyclic two-change listings for this same family; their construction does not assert the one-flip degree minima and rigid extremizers proved here. Eğecioğlu and Iršič analyzed degree sequences for a related Fibonacci-run graph with different boundary/run restrictions. A bijection or equality of vertex counts alone does not transfer degree results, because single-bit adjacency need not be preserved. A prior equivalent graph theorem under another name remains possible and requires human bibliographic review.

## Limitations

This result addresses local degree, not graph connectivity, Hamiltonicity, full degree distributions, constrained Gray-code existence, optimal reconstruction codes, or other \(q\)-ranges. Complete bibliographic novelty cannot be certified by electronic searches or limited primary-source comparison; independent mathematical audit has not been performed.

## References

1. J.-L. Baril, S. Kirgizov and V. Vajnovszki, *Gray codes for Fibonacci q-decreasing words*, arXiv:2010.09505v1 (first public version 2020-10-19), https://arxiv.org/abs/2010.09505 .
2. D. Wong, B. Liu, C. T. Lam and M. Im, *Generating Cyclic 2-Gray Codes for Fibonacci q-Decreasing Words*, WALCOM 2024, DOI:10.1007/978-981-97-0566-5_8, https://doi.org/10.1007/978-981-97-0566-5_8 .
3. Ö. Eğecioğlu and V. Iršič, *Fibonacci-run graphs II: Degree sequences*, arXiv:2010.05521v1 (2020-10-12), https://arxiv.org/abs/2010.05521 .
