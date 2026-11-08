# Parity-optimal two-walker cover starts on balanced complete bipartite graphs

## Finding
For every integer \(n\ge2\), let two independent, synchronous, non-lazy simple random walks explore the unweighted graph \(K_{n,n}\), with the union of their visited vertices counted as covered. The optimal choice of two initial vertices for maximising \(\Pr(C\le t)\), where \(C\) is the first full-coverage time, alternates according to the deadline parity: **split** starts (one vertex in each part) are weakly optimal at every even deadline; **distinct same-part** starts are weakly optimal at every odd deadline. The inequalities become strict, after identifying starts by graph symmetries and ruling out duplicate starts, precisely as follows:

\[
\begin{aligned}
\Pr_{\mathrm{split}}(C\le2k)&>\Pr_{\mathrm{same}}(C\le2k)&&\Longleftrightarrow 2k\ge n-1,\\
\Pr_{\mathrm{same}}(C\le2k+1)&>\Pr_{\mathrm{split}}(C\le2k+1)&&\Longleftrightarrow 2k\ge n-2.
\end{aligned}
\]

In particular, there is no fixed initial placement whose full-coverage time is stochastically no larger than that from every other placement. For \(K_{2,2}\), at deadline one the cover probabilities are \(1/2\) for same-part versus \(1/4\) for split; at deadline two they are \(1/2\) and \(9/16\), respectively. These conclusions apply for all integers \(k\ge0\).

## Assumptions and scope
There are two labeled walkers, independent of one another, each moving simultaneously at every integer time by uniformly selecting one of the \(n\) neighboring vertices. Both starting positions are counted at time zero. The vertex set is partitioned into two labeled sides, each of size \(n\); the walks alternate sides deterministically. A same-part start means two **different** starting vertices in the same side; a split start means one in each side. Graph automorphisms show these are the two nonduplicate starting geometries. Starts in the same vertex are covered by the duplication comparison below.

For \(0\le s\le n\) and integer \(N\ge0\), define
\[
F_n(s,N)=\Pr\bigl(\text{\(N\) independent uniform draws visit every one of \(n-s\) prescribed labels}\bigr)
=\sum_{j=0}^{n-s}(-1)^j\binom{n-s}{j}\left(\frac{n-j}{n}\right)^N.
\]
The initial seed labels are excluded from the prescribed unseen-label set; thus \(F_n(s,N)=0\) when \(N<n-s\). The convention \(0^0=1\) is applied only in the standard empty-draw inclusion-exclusion formula.

## Proof
**Reduction to independent coupon collectors.** Every step from one part lands uniformly in the other, independently of earlier positions. For two independent walkers, all their sampled destinations are independent uniform labels within the selected part. At time \(2k\), each part has received exactly \(N=2k\) draws, independently. Under a split start each part has one initially covered vertex, whereas under a same-part start the two distinct seeds are in one part. Consequently
\[
\Pr_{\mathrm{split}}(C\le2k)=F_n(1,N)^2,\qquad
\Pr_{\mathrm{same}}(C\le2k)=F_n(2,N)F_n(0,N).
\]
At time \(2k+1\), with \(N=2k\), the split configuration yields \(N+1\) draws per side; the same-part configuration yields \(N\) draws on its initially occupied side and \(N+2\) on the other side. Hence
\[
\Pr_{\mathrm{split}}(C\le2k+1)=F_n(1,N+1)^2,\qquad
\Pr_{\mathrm{same}}(C\le2k+1)=F_n(2,N)F_n(0,N+2).
\]

**Sharp even inequality.** Put \(a_{N,j}=j!\left\{\begin{smallmatrix}N\\j\end{smallmatrix}\right\}\), the number of surjections from \(N\) distinguishable draws onto \(j\) labeled destinations, with \(a_{N,j}=0\) when \(j>N\) or \(j<0\). To count draw sequences visiting all previously unseen labels, choose which of the \(s\) initially seen labels also occur among the draws. This gives the identity
\[
F_n(s,N)=\frac{1}{n^N}\sum_{h=0}^{s}\binom{s}{h}a_{N,n-s+h},
\]
which counts trajectories visiting all unseen labels and exactly \(h\) of the \(s\) initially seen labels. Thus, writing \(a_j=a_{N,j}\),
\[
\begin{aligned}
n^N F_n(0,N)&=a_n,\\
n^N F_n(1,N)&=a_{n-1}+a_n,\\
n^N F_n(2,N)&=a_{n-2}+2a_{n-1}+a_n.
\end{aligned}
\]
It follows that
\[
\Pr_{\mathrm{split}}(C\le2k)-\Pr_{\mathrm{same}}(C\le2k)
=\frac{a_{N,n-1}^2-a_{N,n-2}a_{N,n}}{n^{2N}}.
\]

For completeness, the surjection sequence \((a_{N,j})_{j\ge0}\) is log-concave and has no internal zero. This follows inductively from \(a_{N+1,j}=j(a_{N,j}+a_{N,j-1})\): convolution of a nonnegative log-concave sequence without internal zeros with \((1,1)\) preserves log-concavity; multiplication by \(j\) preserves it, with strictness at positive neighboring entries because \(j^2>(j-1)(j+1)\). The initial sequence \(a_{1,1}=1\) has the required properties. For \(N<n-1\), the three relevant coefficients force equality. For \(N=n-1\), \(a_{N,n-1}>0=a_{N,n}\), so the difference is positive. For \(N\ge n\), it is strictly positive at index \(n-1\), using the strict multiplier step (or \(a_{N,0}=0\) when \(n=2\)). This proves the even assertion with its exact boundary.

**Sharp odd inequality.** The first unseeded uniform draw always exposes a new vertex, giving \(F_n(0,N+2)=F_n(1,N+1)\). Conditioning on the next draw from a system with one seeded vertex gives
\[
F_n(1,N+1)=\frac1nF_n(1,N)+\frac{n-1}{n}F_n(2,N).
\]
Therefore
\[
\Pr_{\mathrm{same}}(C\le2k+1)-\Pr_{\mathrm{split}}(C\le2k+1)
=\frac{F_n(1,N+1)}{n}\bigl(F_n(2,N)-F_n(1,N)\bigr).
\]
The first factor is positive iff \(N\ge n-2\). The second is positive exactly when an additional initially covered vertex has a chance to be decisive, which holds when \(N\ge n-2\), by considering draw sequences that cover exactly the \(n-2\) remaining labels but not the additional specified label. Thus the odd difference is strictly positive precisely in the asserted range.

**No benefit from duplicate initial vertices.** Compare two walkers started at the same vertex to two walkers at distinct vertices in that part. Couple all subsequent sampled destinations identically, step for step: at each step the destination distribution depends only on the current *side*, not on the specific vertex. The visited set for the distinct placement then contains the visited set for duplicate placement, pathwise. Hence duplicates cannot improve on the distinct same-part placement. The exhaustive geometry comparison above establishes deadline-wise global optimality. Since both parity inequalities are strict for arbitrarily large deadlines, no single initial placement has first-order stochastic dominance across all deadlines.

## Verification
The standalone standard-library script `verify.py` enumerates two labeled walks and their visited-set masks with exact integer path counts on \(K_{n,n}\), for \(n=2,3,4\) and deadlines \(0\le t\le8\). It independently checks 81 full-state-versus-coupon identities, 672 exact sharp-parity comparisons over \(2\le n\le17\) and \(0\le k\le20\), and 378 integer log-concavity inequalities for surjection counts over \(1\le N\le27\). All checks passed. The proof, rather than a finite experiment, establishes the unrestricted parameter claim.

Run with `python3 verify.py` from the directory containing this file and the checker; no external packages or datasets are required.

## Relationship to prior work
Rivera, Sauerwald and Sylvester study multiple-walk coverage and mixing-time/expected-cover-time bounds, principally with lazy walks, and not the exact initial-location comparison here. Dey, Kim and Terlov formulate initial-placement questions for expectations of union-range sizes and stochastic range comparisons; the exact full-coverage-by-deadline bipartite parity reversal is not a stated or implied result in the sections examined. Unlike ordinary one-walker starting-side comparisons, this is a two-walker **joint initial configuration** effect on balanced parts. Existing surjection log-concavity is used as a proof ingredient; it does not itself encode the two-walker deadlines without the independent-walk reduction.

## Limitations
The result requires two independent synchronous **non-lazy** walks on the unweighted balanced \(K_{n,n}\), full vertex coverage, and time-zero starts counted as visits. It does not cover asynchronous clocks, more than two walkers, unequal part sizes, heterogeneous transition weights, or the optimal expected cover time. Literature searches do not establish historical priority or replace independent mathematical review.

## References
1. N. Rivera, T. Sauerwald and J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, arXiv:2011.07893v1 (first public version, 2020-11-16), https://arxiv.org/abs/2011.07893 ; *Combinatorics, Probability and Computing*, DOI: https://doi.org/10.1017/S0963548322000372.
2. P. Dey, C. Kim and E. Terlov, *Collaboration of Random Walks on Graphs*, arXiv:2302.14241v1 (2023-02-28), https://arxiv.org/abs/2302.14241.
