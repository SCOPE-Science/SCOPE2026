# A sharp two-thirds rank for triangle formation among size-ordered random stick fragments

## Finding

For each integer \(n\ge3\), divide the unit interval at \(n-1\) independent uniform positions. Write the resulting \(n\) positive fragment lengths in increasing order as \(S_{(1)}<\cdots<S_{(n)}\). Let \(p_{n,i}\) be the probability that the three consecutive **size-ranked** fragments \(S_{(i)},S_{(i+1)},S_{(i+2)}\) form a nondegenerate triangle, \(1\le i\le n-2\). Set \(m=n-i-1\). Then

\[
1-p_{n,i}=\frac{n!\,(2m+1)!}{(m+1)!\,(n+m)!}.
\]

For every \(n\ge3\), the complete rank profile has exactly one maximum, at

\[
i_*(n)=n-1-\left\lfloor\frac{n+1}{3}\right\rfloor.
\]

The probability is strictly increasing through that index and strictly decreasing afterward (where the respective ranges are nonempty). Thus for \(n\ge5\) the most triangle-friendly consecutive size ranks lie strictly inside the sorted list, not at its shortest or longest end. The maximal success probability has the sharp asymptotic law

\[
1-p_{n,i_*(n)}=\sqrt6\left(\frac34\right)^n\bigl(1+O(n^{-1})\bigr),
\qquad \frac{i_*(n)}n\longrightarrow\frac23.
\]

## Assumptions and scope

The cut positions are sampled independently and uniformly on the original unit interval, then sorted. Fragment lengths are sorted **by magnitude**; they are not consecutive in physical left-to-right position. A strict triangle requires the sum of its two shortest chosen lengths to exceed the longest. Ties have probability zero. The theorem includes every integer \(n\ge3\), all admissible ranks, and no other cutting scheme or length distribution.

## Proof

**Exponential representation.** Independent rate-one exponentials \(E_1,\ldots,E_n\), divided by their sum, have the uniform simplex distribution of the \(n\) stick spacings. This positive common normalization leaves both size ranks and triangle inequalities unchanged. Let \(E_{(1)}<\cdots<E_{(n)}\) denote their order statistics and \(Y_j=E_{(j)}-E_{(j-1)}\), with \(E_{(0)}=0\). The \(Y_j\) are independent exponentials of rates \(n-j+1\).

**Exact probability.** For a consecutive rank triple, the only nonredundant triangle inequality is \(E_{(i)}+E_{(i+1)}>E_{(i+2)}\). Cancelling the common increment \(Y_{i+1}\) shows this is exactly \(E_{(i)}>Y_{i+2}\). Since \(Y_{i+2}\) is independent of \(E_{(i)}\), with rate \(m=n-i-1\), the failure probability is

\[
q_{n,i}:=1-p_{n,i}=\mathbb E e^{-mE_{(i)}}
=\prod_{r=m+2}^{n}\frac{r}{r+m}
=\frac{n!\,(2m+1)!}{(m+1)!\,(n+m)!}.
\]

Equivalently, \(e^{-E_{(i)}}\) has a \(\mathrm{Beta}(m+2,i)\) distribution, giving the same expression from its \(m\)-th moment.

**Exact unique mode.** Consecutive failure probabilities satisfy, for \(2\le m\le n-2\),

\[
\frac{q_{n,i+1}}{q_{n,i}}
=\frac{(m+1)(n+m)}{2m(2m+1)},
\qquad m=n-i-1.
\]

The ratio is less than one if and only if \(n<3m-2+2/(m+1)\), and greater than one if and only if \(n>3m-2+2/(m+1)\). Since \(3m-2<3m-2+2/(m+1)<3m-1\) for integer \(m\ge2\), no ratio equals one for integer \(n\). While \(i\) rises, \(m\) falls through consecutive integers, so the sign switches exactly once; the minimizing \(m\) is \(m_* =\lfloor(n+1)/3\rfloor\). At \(n=3\) and \(n=4\), direct inspection of the one or two admissible ranks gives the same formula. Hence \(p_{n,i}\) has the claimed unique maximizer and strict changes on each side.

**Asymptotic frontier.** Since \(m_*=n/3+O(1)\), Stirling's formula, uniformly for bounded integer \(m-n/3\), yields

\[
\frac{n!\,(2m+1)!}{(m+1)!\,(n+m)!}
=\sqrt6\,(3/4)^n(1+O(n^{-1})).
\]

The linear term in the perturbation \(m-n/3\) cancels because the exponential rate has its stationary point at \(m/n=1/3\). The maximizing rank consequently satisfies \(i_*/n\to2/3\). No probabilistic approximation is used to prove the finite-rank statements.

## Verification

The accompanying `verify.py` checks the exact formula against a second beta-moment evaluation using rational arithmetic, all adjacent ratios and strict unique maxima for \(3\le n\le100\), and the scaled asymptotic ratio at increasing sample sizes. These are independent finite checks only; the all-size proof is the order-statistic factorization and integer sign comparison above. Run `python verify.py` with the Python standard library.

## Relationship to prior work

The classical three-piece broken-stick triangle probability and the exponential normalization of uniform spacings are established background, not claimed as new. Ionascu and Prajitura (2010, arXiv:1009.0890) analyze triangle constructions from three uniformly broken parts; they do not study an \(n\)-fragment size-ranked consecutive-triple profile. Holst (1980) gives foundational representations and order-statistic laws for uniform spacings; those standard tools are used directly here, but the inspected article does not state this triangle-formation mode or its sharp exponential frontier. Crowdmath (2018) studies broken-stick polygon events and the number of feasible triangles, not the size-rank phase profile. Published-record searches found no covering profile theorem. This is not a claim of independent priority certification.

## Limitations

The rank-profile theorem is specific to uniform simultaneous cuts, equivalently normalized independent exponentials. Sorted triples and physically adjacent triples are different observables. The exact large-sample frontier describes only the *most likely consecutive size-ranked triple*, not the probability that some arbitrary triple forms a triangle. A stronger or overlooked published specialization may exist; independent mathematical and historical audit remains outstanding.

## References

- E. J. Ionascu and G. Prajitura, *Things to do with a broken stick*, arXiv:1009.0890 (first arXiv submission 2010-09-05), https://arxiv.org/abs/1009.0890.
- L. Holst, *On the lengths of the pieces of a stick broken at random*, Journal of Applied Probability 17 (1980), 623–634, https://doi.org/10.2307/3212956.
- P. A. Crowdmath, *The Broken Stick Project*, arXiv:1805.06512 (2018), https://arxiv.org/abs/1805.06512.
- W. Verreault, *On the probability of forming polygons from a broken stick*, arXiv:2107.09604 (2021), https://arxiv.org/abs/2107.09604.
