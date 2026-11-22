# Independent Gaussian center and gap marks of rare coordinatewise comparisons

## Finding

For every sequence of integers \(n\to\infty\) and \(d=d_n\to\infty\) satisfying
\[
\lambda_n=n(n-1)2^{-d}\longrightarrow\lambda\in(0,\infty),
\]
let \(X_1,\ldots,X_n\) be independent uniform points of \([0,1]^d\), and draw a directed edge \(i\to j\) exactly if \(X_i\le X_j\) coordinatewise. Define the edge's centered coordinate-sum and coordinate-gap marks by
\[
A_{ij}=\frac1{\sqrt d}\sum_{r=1}^d(X_{ir}+X_{jr}-1),\qquad
B_{ij}=\frac1{\sqrt d}\sum_{r=1}^d(X_{jr}-X_{ir}-\tfrac13).
\]
The finite random point measure of these marks,
\[
\Xi_n=\sum_{i\ne j}\mathbf1\{X_i\le X_j\}\delta_{(A_{ij},B_{ij})},
\]
converges in distribution to a Poisson random measure on \(\mathbb R^2\) with intensity \(\lambda\,\gamma\), where \(\gamma\) is the product measure
\[
\gamma=N(0,1/6)\otimes N(0,1/18).
\]
Moreover, for every fixed finite Borel partition \(E_1,\ldots,E_q\) of \(\mathbb R^2\), the joint law of \((\Xi_n(E_1),\ldots,\Xi_n(E_q))\) is at total-variation distance at most a universal constant times
\[
n^3\bigl(4^{-d}+3^{-d}\bigr)
\]
from independent Poisson variables of respective means \(\lambda_n\nu_d(E_a)\). Here \(\nu_d\) is the **exact conditional distribution of one marked edge given comparability**; its Gaussian weak limit is \(\gamma\). This finite-partition approximation holds for all \(n\ge3\), \(d\ge1\), whether or not the critical scaling is imposed.

The probability that the directed comparability graph is a matching is at least \(1-Cn^3 3^{-d}\) for an absolute constant \(C\). Thus the marked Poisson limit describes a collection of asymptotically disjoint comparable pairs. The matching property is a structural ingredient, not a separately claimed novelty.

For \(M_A=\max_{i\to j}A_{ij}\) and \(M_B=\max_{i\to j}B_{ij}\), with empty maxima \(-\infty\), this gives, for all real \(x,y\),
\[
\lim_{n\to\infty}\Pr(M_A\le x,M_B\le y)
=\exp\!\left\{-\lambda\bigl[1-\Phi(\sqrt6\,x)\Phi(\sqrt{18}\,y)\bigr]\right\}.
\]
In particular, independently Gaussian marks do **not** produce independent global maxima: the extremes remain dependent through the common random number of edges. In endpoint coordinates, the conditional scaled vector of the lower and upper coordinate averages converges to a bivariate Gaussian with marginal variance \(1/18\) and covariance \(1/36\), i.e. correlation \(1/2\).

## Assumptions and scope

The order \(\le\) is coordinatewise, ties have probability zero, and all \(nd\) coordinates of the sample are independent uniforms. The sample size tends to infinity and dimension is integer-valued; only sequences with \(\lambda_n\to\lambda\in(0,\infty)\) are asserted to have a nondegenerate marked Poisson limit. Such sequences exist (for example \(n=2^k\), \(d=2k\), with \(\lambda=1\)). The complete mark point measure on \(\mathbb R^2\) is used; no convergence of higher factorial moments or large-deviation assertion is included.

## Proof

**1. Exact one-coordinate law under an oriented comparison.** For two independent \(U,V\sim U[0,1]\), the event \(U\le V\) has probability \(1/2\). Conditional on this event, \((U,V)\) has density \(2\mathbf1\{0<u<v<1\}\), with exact moments
\[
\mathbb E[U^a V^b\mid U\le V]=\frac{2}{(a+1)(a+b+2)}\quad(a,b\ge0\text{ integers}).
\]
Consequently \(\mathbb EU=1/3\), \(\mathbb EV=2/3\), both conditional variances equal \(1/18\), and their conditional covariance is \(1/36\). For \(S=U+V-1\) and \(G=V-U-1/3\), direct expansion gives
\[
\mathbb ES=\mathbb EG=0,\qquad
\operatorname{Var}S=\frac16,\quad
\operatorname{Var}G=\frac1{18},\quad
\operatorname{Cov}(S,G)=0.
\]
For a directed pair \((i,j)\), the comparison \(X_i\le X_j\) conditions independently in each coordinate, so \((A_{ij},B_{ij})\) under this event is the normalized sum of \(d\) iid copies of \((S,G)\). The bounded-vector multivariate central limit theorem proves \(\nu_d\Rightarrow\gamma\), and zero limiting covariance makes the two Gaussian coordinates independent. The conditional endpoint-average Gaussian covariance matrix is \(\left(\begin{smallmatrix}1/18&1/36\\1/36&1/18\end{smallmatrix}\right)\).

**2. Dependency neighborhoods and the graph matching law.** Let \(I_{ij}=\mathbf1\{X_i\le X_j\}\), for \(i\ne j\). Every \(I_{ij}\) has mean \(p=2^{-d}\), and its underlying sample uses only \(X_i,X_j\). Of the ordered-pair indices, exactly \(4n-6\) (including itself) share at least one vertex with \((i,j)\). For two distinct, jointly realizable directed comparisons sharing one vertex, their one-coordinate joint probability is either \(1/3\) (a common lower or upper point) or \(1/6\) (a chain). Opposite orientations on the same two vertices cannot both occur. By coordinate independence, every such joint probability is at most \(3^{-d}\). Thus
\[
b_1\le n(n-1)(4n-6)4^{-d},\qquad
b_2\le n(n-1)(4n-8)3^{-d},\qquad b_3=0
\]
for the local-dependence coefficients of the Arratia–Goldstein–Gordon Poisson approximation, because indices with disjoint endpoints are jointly independent of each edge indicator. A union bound over pairs of incident directed edges yields
\[
\Pr(\exists\text{ two edges sharing a vertex})
\le \tfrac12 n(n-1)(4n-8)3^{-d}.
\]

**3. A marked Poisson process approximation, not merely a count approximation.** Fix any finite Borel partition \(E_1,\ldots,E_q\). Split each Bernoulli indicator into mutually exclusive marked events \(I_{ij,a}=I_{ij}\mathbf1\{(A_{ij},B_{ij})\in E_a\}\). Enlarge each dependency neighborhood to all categories of all pairs meeting the original pair. The marked extension of Arratia–Goldstein–Gordon's Theorem 2 (their Section 3.1) preserves the values of \(b_1,b_2\) and keeps \(b_3=0\). The resulting random indicator array is within total-variation distance \(O(b_1+b_2)\) of independent Poisson variables with means \(p\nu_d(E_a)\) at each ordered-pair/category index. Summing over all \(n(n-1)\) indices proves the partition-count statement, with independent Poisson means \(\lambda_n\nu_d(E_a)\).

Because \(\lambda_n\to\lambda\) and \(\nu_d\Rightarrow\gamma\), the counts on any finite family of disjoint continuity sets converge jointly to the counts of a Poisson point process with mean measure \(\lambda\gamma\). Both the total expected number of atoms and the mark laws are tight, so this yields convergence of finite random point measures. More explicitly, under the critical scale,
\[
n^3 3^{-d}=O\!\left(n^{3-2\log_2 3}\right)\longrightarrow0,
\qquad
n^3 4^{-d}=O(n^{-1})\longrightarrow0,
\]
since \(3-2\log_2 3<0\). This completes the point-process and matching claims.

**4. Dependent extremes from independent Gaussian marks.** The event \(M_A\le x\), \(M_B\le y\) means there is no atom in \(\{(a,b):a>x\text{ or }b>y\}\). Since \(\gamma\) is a product Gaussian law, the limiting forbidden-region measure is \(\lambda[1-\Phi(\sqrt6x)\Phi(\sqrt{18}y)]\). The Poisson void-probability formula gives the displayed bivariate extreme-value law. For finite real thresholds the boundary has zero \(\gamma\)-measure, justifying the limit.

## Verification

The accompanying standalone Python 3 script `checks/marks_exact.py` uses only the standard library and recomputes the triangle moments exactly as rationals, shared-vertex one-coordinate ordering probabilities by independent permutation enumeration, the dependency-neighborhood count, critical-scale decay tests, and the linear covariance transformation. Run `python3 checks/marks_exact.py` after extracting the embedded script. A successful run prints `PASS: 3007 exact rational and combinatorial checks`. These computations verify inputs to, but do not substitute for, the multivariate central limit theorem or the cited Poisson-process approximation theorem.

## Relationship to prior work

Bhattacharjee–Ilienko–Jin–Molchanov (arXiv:2611.01096, Sections 1, 2 and 10) establish fluctuation regimes for the **unmarked number** of non-Pareto vertices, and expressly credit Ilienko–Jin (arXiv:2603.18698) with a Poisson point-process limit for **fixed-dimensional coordinate projections of the non-Pareto vertices** at the critical sparsity boundary. The present statement concerns a different statistic: the joint \(\sqrt d\)-fluctuations of the full-coordinate sum and gap of **both endpoints of each directed comparison**, jointly across all rare comparisons. A fixed-dimensional projection limit does not itself imply these growing-dimensional empirical-coordinate fluctuations or their marked edge process. The known unmarked Poisson count is not the asserted contribution.

Bollobás–Brightwell (1995) established chain and maximum-degree thresholds for random high-dimensional orders; the absence of shared endpoints at this sparse scale is consistent with and may follow from their degree threshold, and is used here rather than asserted independently as new. Arratia–Goldstein–Gordon (1989, 1990) supply the general locally dependent Poisson-process approximation and its marked-type extension. The model-specific joint endpoint marks, their exact covariance, and the dependent-extremes law are the proposed refinement.

## Limitations

Only binomial samples with independent uniform coordinates (or their exactly transformed marginal-rank equivalents) are established. No phase diagram away from sparsity, no process limit for all possible coordinate functionals, and no convergence of high factorial moments are asserted. The joint-mark theorem uses standard general approximation results; its historical priority may be limited by a sufficiently broad pre-existing marked point-process specialization. The full text of the most closely related 2026 fixed-projection preprint and the 1995 random-order article could not be materially inspected; their publicly available abstracts, the accessible 2026 follow-up's detailed explicit description, and the theorem statements quoted there were compared instead. The absence of an exact prior statement in searchable materials is not a proof of uniqueness.

## References

1. C. Bhattacharjee, A. Ilienko, B. Jin, I. Molchanov, *From Gaussian to stable and back: Non-Pareto points in growing dimension*, arXiv:2611.01096v1, first public 2026-10-31. https://arxiv.org/abs/2611.01096
2. A. Ilienko, B. Jin, *Pareto points in growing dimensions*, arXiv:2603.18698v1, first public 2026-03-19. https://arxiv.org/abs/2603.18698
3. B. Bollobás, G. Brightwell, *Random high-dimensional orders*, Advances in Applied Probability **27** (1995), 161–184, DOI 10.2307/1428102. https://doi.org/10.2307/1428102
4. R. Arratia, L. Goldstein, L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science **5** (1990), 403–434, https://doi.org/10.1214/ss/1177012015 (especially Theorem 2 and Section 3.1).
