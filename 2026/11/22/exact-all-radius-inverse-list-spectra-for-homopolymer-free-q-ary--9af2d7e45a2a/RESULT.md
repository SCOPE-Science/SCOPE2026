# Exact all-radius inverse-list spectra for homopolymer-free q-ary deletion channels

## Finding

Let \(\Sigma_q\) be an alphabet of \(q\ge3\) labeled symbols, and define the **homopolymer-free** length-\(n\) language
\[H_{q,n}=\{x\in\Sigma_q^n:x_i\ne x_{i+1}\text{ for all }1\le i<n\}.\]
For any receiver \(y\in\Sigma_q^m\) of length \(m\ge1\), let \(P_{q,m,d}(y)\) count the distinct words \(x\in H_{q,m+d}\) that contain \(y\) as a scattered subsequence. Every distinct source is counted once, even when several deletion-position sets give the same receiver. Put
\[r(y)=\#\{i\in\{1,\dots,m-1\}:y_i=y_{i+1}\}.\]
Then, as an identity of formal power series,
\[\boxed{\sum_{d\ge0}P_{q,m,d}(y)z^d=\frac{(q-1)^{r(y)}z^{r(y)}(1+z)}{(1-(q-2)z)^m(1-(q-1)z)}.}\]
Consequently \(P_{q,m,d}(y)>0\) if and only if \(r(y)\le d\). The exact distribution among all length-\(m\) receivers is obtained by putting
\[C_{q,m}(t)=[z^t]\frac{1+z}{(1-(q-2)z)^m(1-(q-1)z)},\quad C_{q,m}(t)=0\ (t<0).\]
The list size corresponding to \(r\) equal neighboring pairs is \((q-1)^r C_{q,m}(d-r)\), and that class contains exactly \(q\binom{m-1}{r}(q-1)^{m-1-r}\) distinct receiver words. For \(0\le r<\min\{d,m-1\}\), consecutive nonzero list sizes are strictly decreasing. No nonempty receiver has a singleton inverse list when \(d\ge1\).

Writing \(F_{q,m,d}\) for the number of **feasible receiver words** (not a deletion-correcting code size),
\[F_{q,m,d}=q\sum_{r=0}^{\min\{d,m-1\}}\binom{m-1}{r}(q-1)^{m-1-r}.\]
Hence under a uniform draw from all \(q^m\) potential receivers,
\[\frac{F_{q,m,d}}{q^m}=\Pr\bigl\{\operatorname{Bin}(m-1,1/q)\le d\bigr\}.\]
In particular, the feasibility fraction tends to zero when \(d/(m-1)\to\alpha<1/q\), to one when \(\alpha>1/q\), and to \(\Phi(t)\) when
\[d=\left\lfloor\frac{m-1}{q}+t\frac{\sqrt{(m-1)(q-1)}}q\right\rfloor,\]
where \(\Phi\) is the standard-normal cumulative distribution function. When \(m\ge d+1\), the minimum nonzero inverse-list size is exactly \((q-1)^d\) and occurs at precisely \(q\binom{m-1}{d}(q-1)^{m-1-d}\) receivers.

## Assumptions and scope

All positions in source and receiver are indexed and linear, not circular. The alphabet has \(q\ge3\) labeled symbols; the source constraint forbids equal adjacent symbols but does not impose any balance or other code constraint. Deletions preserve order and delete exactly \(d\ge0\) symbols. Multiple deletion masks of a fixed source are not counted separately. The receiver may itself contain repeated neighbors. The empty receiver is excluded (\(m\ge1\)). Generating functions are formal, so no convergence hypothesis is required. The asymptotic statements fix \(q\ge3\) and let \(m\to\infty\).

## Proof

**Canonical embedding.** For any admissible source \(x\) containing \(y\) as a subsequence, choose the unique greedy (leftmost) embedding of \(y\) into \(x\). This separates \(x\) uniquely into an initial skipped block, the \(m\) matched letters of \(y\), \(m-1\) internal skipped blocks, and a terminal skipped block. Every skipped letter before a matched \(y_j\) differs from \(y_j\), or the embedding would have matched it earlier. Conversely, any such decomposition respecting adjacency produces an admissible source whose greedy embedding is exactly the designated one. In particular, the argument counts **distinct sources**, not embeddings or deletion masks.

**Initial and terminal blocks.** A nonempty initial skipped block of length \(s\) avoids the first matched letter throughout, has \(q-1\) choices for its first symbol and \(q-2\) for each subsequent symbol. The initial block therefore contributes
\[A(z)=1+\sum_{s\ge1}(q-1)(q-2)^{s-1}z^s=\frac{1+z}{1-(q-2)z}.\]
After the final matched letter, an arbitrary admissible terminal extension of length \(s\) has \((q-1)^s\) possibilities, contributing \(T(z)=1/(1-(q-1)z)\).

**Internal blocks.** Between distinct consecutive matched symbols \(a\ne b\), a skipped block of length \(s\ge1\) must start with a symbol different from both \(a\) and \(b\), then avoid both the previous skipped symbol and \(b\) at each successive step. It has exactly \((q-2)^s\) possibilities; the empty block is allowed. Thus \(B(z)=1/(1-(q-2)z)\). If instead \(a=b\), the block must be nonempty: its first symbol has \(q-1\) choices and each later one \(q-2\), hence \(E(z)=(q-1)z/(1-(q-2)z)\). There are \(r(y)\) equal and \(m-1-r(y)\) unequal internal adjacencies. Multiplication gives
\[A(z)B(z)^{m-1-r(y)}E(z)^{r(y)}T(z)=\frac{(q-1)^{r(y)}z^{r(y)}(1+z)}{(1-(q-2)z)^m(1-(q-1)z)},\]
proving the main identity, including \(d=0\) and the required exact distinct-parent interpretation.

**Support, strict spectrum, and boundary.** Every coefficient in \((1+z)(1-(q-2)z)^{-m}\) is positive because \(q\ge3\); hence the formula yields feasibility exactly when \(r(y)\le d\). Put \(a_t=[z^t](1+z)(1-(q-2)z)^{-m}\). The coefficient relation
\[C_{q,m}(t)=(q-1)C_{q,m}(t-1)+a_t\quad(t\ge1)\]
has \(a_t>0\). Therefore for \(r+1\le\min\{d,m-1\}\), setting \(t=d-r\),
\[(q-1)^rC_{q,m}(t)-(q-1)^{r+1}C_{q,m}(t-1)=(q-1)^ra_t>0.\]
Every nonzero list for \(d\ge1\) has at least two members: if \(r\ge1\), its leading coefficient is at least \(q-1\ge2\); if \(r=0\), the coefficient of positive degree in the displayed rational series exceeds one. When \(m\ge d+1\), the final class \(r=d\) has list size exactly \((q-1)^d\).

**Multiplicity and threshold.** Choose the first receiver symbol in \(q\) ways. At each of the \(m-1\) adjacent steps, choosing equality has one option and choosing inequality has \(q-1\) options; the stated multiplicity follows by choosing the \(r\) equality steps. Summation over \(r\le d\) proves \(F_{q,m,d}\). Dividing by \(q^m\) identifies the binomial distribution exactly, so the law of large numbers and the classical binomial central limit theorem give the threshold and Gaussian window.

## Verification

The standalone `checker.py` provides three separate finite checks: direct generation of every homopolymer-free source and all its distinct receivers, a deterministic greedy-prefix automaton that counts sources without enumerating deletion masks, and integer coefficient checks of the strict spectrum and feasible-output count. It reports 70,295 receiver configurations, 2,260 independent automaton cases, and 2,016 spectrum parameter combinations passing. The infinite claim is proved above; these finite computations are reproducibility cross-checks, not substitutes for the formal combinatorial proof.

For example, at \(q=3\), \(m=5\), \(d=2\), the nonzero inverse lists have sizes \(36,16,4\) for \(r=0,1,2\), respectively; their receiver multiplicities are \(48,96,72\). The remaining \(27\) words of length five with \(r\ge3\) are impossible, totaling the full \(3^5=243\) outputs.

## Relationship to prior work

Atashpendar et al. (first public 2018) enumerate and cluster **unrestricted binary** supersequences and their embedding multiplicities. Their canonical initial-embedding approach is acknowledged; it does not impose an adjacency-distinct source constraint, nor state the multialphabet all-deletion inverse-list law above. Takemoto and Nozaki (first public 2020) construct binary run-length-limited *single*-insertion/deletion-correcting codes and analyze redundancy, rather than counting all admissible sources for arbitrary receivers and deletion counts. Benerjee and Banerjee (first public 2023) study homopolymer-free codes through **Hamming-distance** spheres, not subsequence/deletion inverse lists. These differences concern the objects and quantifiers, not just notation. Relevant existing results on unconstrained deletion descendants and overlapping-read erasures do not imply the present inverse spectrum. See `REVIEW.md` and `AUDIT.json` for comparisons and unresolved historical-priority risks.

## Limitations

The result enumerates inverse lists, not their deletion-mask multiplicities or posterior probabilities under a deletion distribution, and it does not determine a largest deletion-error-correcting code. In particular, the feasible-output count cannot be used directly as such a code size. The theorem excludes the empty receiver and does not address nonlinear GC-balance, fixed-composition sources, bounded runs longer than one, or circular boundary conditions. The novelty assessment is same-model only, not independent certification; unindexed equivalent restricted-language formulas remain possible.

## References

1. A. Atashpendar, M. Beunardeau, A. Connolly, R. Géraud, D. Mestel, A. W. Roscoe, P. Y. A. Ryan, *From Clustering Supersequences to Entropy Minimizing Subsequences for Single and Double Deletions*, arXiv:1802.00703, first public 2018-02-02. https://arxiv.org/html/1802.00703v2
2. R. Takemoto and T. Nozaki, *Construction and Encoding Algorithm for Maximum Run-Length Limited Single Insertion/Deletion Correcting Code*, arXiv:2012.13536, first public 2020-12-25. https://arxiv.org/html/2012.13536v1
3. K. G. Benerjee and A. Banerjee, *Bounds on Size of Homopolymer Free Codes*, arXiv:2305.10741, first public 2023-05-18. https://arxiv.org/abs/2305.10741
