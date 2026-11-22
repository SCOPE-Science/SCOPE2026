# Marked compound-Poisson near-diameter chords of partial permutohedra

## Finding
For integers \(m\ge 2n\ge2\), let
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{nonzero coordinates of }x\text{ are distinct}\}
\]
in its ordinary Euclidean coordinates. Write \((a)_k=a(a-1)\cdots(a-k+1)\), with \((a)_0=1\), and set
\[
Q_n=\sum_{j=1}^{n}j^2=\frac{n(n+1)(2n+1)}6,\qquad N_{m,n}=\sum_{k=0}^{n}(m)_k,\qquad p_{m,n}=\frac{(m)_n}{N_{m,n}}.
\]
Sample two vertices \(X,Y\) independently and uniformly (with replacement), and define their normalized **squared-diameter deficit**
\[
W_{m,n}=\frac{2Q_n-\lVert X-Y\rVert_2^2}{2n^2}.
\]
The diameter \(\sqrt{2Q_n}\) is attained precisely by disjoint-support full-rank vertices (a previously known diameter value). The probability that a random ordered pair is diametral is **exactly**
\[
\boxed{\Pr(W_{m,n}=0)=p_{m,n}^{2}\frac{\binom{m-n}{n}}{\binom mn}.}
\]
Conditioned on both vertices having all \(n\) positive labels, the complete first two moments of the deficit are
\[
\boxed{\mathbb E[W_{m,n}\mid\mathrm{full}]=\frac{(n+1)^2}{4m},\qquad
\operatorname{Var}(W_{m,n}\mid\mathrm{full})=\frac{\bigl(Q_n-[n(n+1)/2]^2/m\bigr)^2}{(m-1)n^4}.}
\]
For any integer sequences \(m,n\to\infty\) with \(n/m\to0\) and eventually \(m\ge2n\), there are three sharply separated regimes. When \(n^2/m\to0\), \(W_{m,n}\to0\) in probability and the diametral-pair probability tends to \(1\). When \(n^2/m\to\lambda\in(0,\infty)\),
\[
\boxed{W_{m,n}\ \xrightarrow{d}\ \sum_{j=1}^{K}U_jV_j,\qquad K\sim\operatorname{Poisson}(\lambda),\quad U_j,V_j\stackrel{\mathrm{iid}}{\sim}\operatorname{Uniform}(0,1),}
\]
with all variables independent. The limiting law has an atom \(e^{-\lambda}\) at zero; each positive jump has density \(-\log t\) for \(0<t<1\). Its mean is \(\lambda/4\), variance \(\lambda/9\), and Laplace transform is
\[
\mathbb E(e^{-sW})=\exp\!\left[\lambda\left(\int_0^1\!\int_0^1e^{-suv}\,du\,dv-1\right)\right],\quad s\ge0.
\]
When instead \(n^2/m\to\infty\) while \(n/m\to0\),
\[
\boxed{\frac{W_{m,n}}{n^2/m}\ \xrightarrow{\Pr}\ \frac14,}
\]
and the diametral-pair probability tends to \(0\). The critical scale is thus \(n\asymp\sqrt m\), at which a random chord has a nondegenerate, explicitly marked compound-Poisson deficit.

## Assumptions and scope
All distances use the *native*, unrescaled Euclidean metric of \(\mathbb R^m\). A rank-\(k\) vertex has precisely the \(k\) largest labels \(n-k+1,\ldots,n\), each once, in distinct coordinate positions; this is the established vertex classification of Heuer and Striker, Proposition 5.7. Its number is \((m)_k\), not the count of every admissible defining word. Sampling is uniform over **vertices**, not over defining words, edges, Gaussian support directions or Euclidean volume. The finite diameter and probability statements assume \(m\ge2n\); the asymptotic assertions also require \(n\to\infty\).

## Proof
**1. Diameter and full-rank reduction.** Every vertex is coordinatewise nonnegative, and its squared norm is at most \(Q_n\). Thus
\[
\lVert x-y\rVert^2=\lVert x\rVert^2+\lVert y\rVert^2-2\langle x,y\rangle\le2Q_n.
\]
For \(m\ge2n\), two full-rank vertices can have disjoint supports, realizing equality. Conversely, equality requires both squared norms to equal \(Q_n\) (hence full rank) and the nonnegative inner product to vanish (hence disjoint support). By the known vertex classification, the probability of full rank is \(p_{m,n}\). Conditional on full rank, each support is an independent uniform \(n\)-subset of \([m]\), and the two label assignments are independent uniform bijections. The disjoint-support probability is \(\binom{m-n}{n}/\binom mn\), giving the exact atom.

**2. Exact first and second moments.** On the full-rank event, \(X\) and \(Y\) are independent uniformly permuted copies of \((1,2,\ldots,n,0,\ldots,0)\). With \(S_n=\sum_{j=1}^{n}j=n(n+1)/2\), the deficit is exactly \(W=\langle X,Y\rangle/n^2\). For two independent permutations of a fixed \(m\)-vector with sum \(S_n\) and squared norm \(Q_n\), permutation sampling gives
\[
\mathbb E\langle X,Y\rangle=\frac{S_n^2}{m},\qquad
\operatorname{Var}\langle X,Y\rangle=\frac{(Q_n-S_n^2/m)^2}{m-1}.
\]
For completeness, the centered entries of a uniformly permuted vector have diagonal covariance \((Q_n-S_n^2/m)/m\) and off-diagonal covariance \(-(Q_n-S_n^2/m)/[m(m-1)]\). Contracting two independent such matrices in the bilinear inner product gives the stated variance. Division by \(n^2\) and \(n^4\) proves the displayed formulas.

**3. Poisson overlap and marked products.** Conditional on both vertices being full-rank, let \(K\) count coordinates where their supports intersect. It has hypergeometric law
\[
\Pr(K=k\mid\mathrm{full})=\frac{\binom nk\binom{m-n}{n-k}}{\binom mn},\quad 0\le k\le n,
\]
with falling-factorial moments
\[
\mathbb E[(K)_r\mid\mathrm{full}]=\frac{(n)_r^2}{(m)_r}\quad(0\le r\le n).
\]
If \(n^2/m\to\lambda\in(0,\infty)\), these converge to \(\lambda^r\) for each fixed \(r\). The standard factorial-moment argument (or the hypergeometric Poisson limit) gives \(K\Rightarrow\operatorname{Poisson}(\lambda)\). Given \(K=k\), the labels on the overlapping coordinates for each vertex are independently uniform ordered \(k\)-samples **without replacement** from \(\{1,\ldots,n\}\). For each fixed \(k\), after division by \(n\) the pairings jointly converge to independent uniform \((0,1)\) marks. Therefore
\[
W=\sum_{i:\,X_iY_i>0}\frac{X_i}{n}\frac{Y_i}{n}
\]
converges, conditioned on full rank, to the asserted marked Poisson sum. The tight overlap-count distribution allows summation over \(k\). The full-rank probability tends to one: since
\[
\frac{N_{m,n}}{(m)_n}=1+\sum_{r=1}^{n}\frac1{(m-n+1)(m-n+2)\cdots(m-n+r)},
\]
for \(m-n\ge1\) this excess is at most \(1/(m-n)\). Hence the same limit holds for the original uniform-vertex law. An independent product of two uniform \((0,1)\) variables has density \(-\log t\), and the atom, moments, and Laplace formula follow from compound-Poisson calculus.

**4. Other regimes and the sharp atom threshold.** If \(n^2/m\to0\), Markov's inequality and the conditional mean show convergence of \(W\) to zero, and the exact disjoint-support product tends to one. If \(n^2/m\to\infty\) but \(n/m\to0\), the conditional expectation is \((n^2/m)(1+o(1))/4\), while the conditional relative variance is \(O(m/n^2)\to0\). Chebyshev's inequality gives the asserted normalization. The probability of zero overlap is bounded by \(\exp(-n^2/m)\), hence tends to zero. Since full-rank probability tends to one in both regimes, these conclusions are unconditional. At criticality, the exact probability of no support overlap tends to \(e^{-\lambda}\) by expanding its finite product, and the full-rank factor again tends to one.

## Verification
The standalone program `verify_chords.py` enumerates complete vertex sets in eight small parameter cases, compares every ordered vertex pair against the exact diameter and contact classification, and computes full-rank means, variances, and zero-overlap probabilities using exact rational arithmetic. It additionally checks hypergeometric overlap factorial moments approaching Poisson values for three increasing parameter sizes. The calculation is a finite diagnostic; the infinite limiting statement follows from the proof, not from simulations.

## Relationship to prior work
Heuer and Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, arXiv:2012.09901, Proposition 5.7, give the vertex classification and exact counts used here, alongside inequalities, facets, and volume questions. Behrend et al., *Partial permutohedra*, arXiv:2207.14253, develop facial structure, Ehrhart theory, and volume formulas. Existing published work already determines the Euclidean diameter of partial permutohedra, including its saturation at \(m=2n\), and separate work determines **adjacent-edge** lengths; neither supplies a randomly sampled **vertex-pair** deficit limit. The new assertion is the exact random diametral-pair atom, conditional chord moments, and marked compound-Poisson critical distribution with adjacent subcritical and supercritical regimes. The diameter value itself is explicitly **not** claimed as new.

## Limitations
The asymptotic theorem assumes the sparse ratio \(n/m\to0\) and is not a statement about a uniform point of the whole polytope, a uniformly chosen edge, or the full dense regime \(n/m\to c>0\). The weak limit does not assert a quantitative total-variation rate for the continuous deficit law. The earliest source date belongs to the original construction, not to these results. Historical priority remains provisional, especially for possible unindexed probability results on sparse randomly permuted vectors. Independent mathematical review has not been performed.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first public version 2020-12-17), https://arxiv.org/abs/2012.09901 .
2. R. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial permutohedra*, arXiv:2207.14253 (first public version 2022-07-28), https://arxiv.org/abs/2207.14253 .
3. *The Euclidean diameter of partial permutohedra saturates exactly at* \(m=2n\), published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-euclidean-diameter-of-partial-permutohedra-saturates-exactly--cb2829b66c5c .
4. *Poisson edge-length spectrum and a length-condensation transition for partial permutohedra*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-poisson-edge-length-spectrum-and-a-length-condensation-transitio--c92e973354a1 .
