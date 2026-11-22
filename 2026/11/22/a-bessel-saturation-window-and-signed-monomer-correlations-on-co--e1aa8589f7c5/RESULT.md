# A Bessel saturation window and signed monomer correlations on complete bipartite graphs

## Finding

The equilibrium monomer–dimer gas on the complete bipartite graph \(K_{n,n+k}\), with a fixed shore imbalance \(k\ge0\), exhibits a sharp near-perfect-matching window. Give each matching \(M\) weight \(\lambda^{|M|}\). Let \(J_n=n-|M|\) be the number of unmatched vertices on the smaller shore. For every fixed \(k\ge0\) and \(c>0\), at edge activity \(\lambda=n/c\),
\[
\Pr(J_n=j)=\frac{(n)_j(c/n)^j}{j!(j+k)!B_{n,k}(c)},\qquad B_{n,k}(c)=\sum_{r=0}^n\frac{(n)_r(c/n)^r}{r!(r+k)!}.
\]
Here \((n)_r=n!/(n-r)!\). Let \(I_\nu\) denote the modified Bessel function of the first kind and let \(J\) have law
\[
\Pr(J=j)=\frac{c^{j+k/2}}{j!(j+k)!I_k(2\sqrt c)},\qquad j=0,1,\ldots.
\]
Then the quantitative all-size convergence and its explicit first two factorial moments are
\[
 d_{\rm TV}(\mathcal L(J_n),\mathcal L(J))\le \frac{c}{2n}\frac{I_{k+2}(2\sqrt c)}{I_k(2\sqrt c)},\quad
 \mu=\mathbb E J=\sqrt c\frac{I_{k+1}(2\sqrt c)}{I_k(2\sqrt c)},\quad
 f_2=\mathbb E[J(J-1)]=c\frac{I_{k+2}(2\sqrt c)}{I_k(2\sqrt c)}.
\]

Every pair of **distinct unmatched-vertex indicators in the same shore has strictly negative covariance**, and every pair in opposite shores has **strictly positive covariance**, for every finite \(n\ge2\), \(k\ge0\) and \(\lambda>0\), not merely in the scaling window. In the Bessel window, writing \(C_{LL}, C_{RR}, C_{LR}\) for a marked pair on the smaller shore, larger shore, or across shores respectively, one has
\[
 \lim_{n\to\infty}n^2 C_{LL}=f_2-\mu^2<0,\qquad
 \lim_{n\to\infty}n^2 C_{RR}=f_2-\mu^2-k<0,\qquad
 \lim_{n\to\infty}n^2 C_{LR}=\mu+f_2-\mu^2>0.
\]
Finally, the window is sharp in order: if \(\lambda_n/n\to\infty\), then \(J_n\to0\) in probability, whereas if \(\lambda_n/n\to0\), then \(J_n\to\infty\) in probability (for fixed \(k\)).

## Assumptions and scope

The graph is a complete bipartite graph with labeled shores of sizes \(n\) and \(n+k\), where \(n\ge2\) and the integer \(k\ge0\) is fixed in every asymptotic assertion. A configuration is a matching, with probability proportional to \(\lambda^{|M|}\); unmatched vertices are called monomers. The model is an equilibrium Gibbs matching measure, *not* sequential random adsorption. The activity \(\lambda>0\) is arbitrary for the finite covariance sign theorem and is \(n/c\) for the Bessel limit. The number of unmatched vertices on the larger shore is exactly \(J_n+k\). Covariances are between zero–one monomer indicators of two distinct labeled vertices. All statements are for finite graphs or the stated fixed-imbalance asymptotic; no positive-temperature phase transition is claimed.

## Proof

**1. Exact finite distribution.** There are
\[
 N_{n,k,j}=\binom nj\binom{n+k}{j+k}(n-j)!
 =\frac{n!(n+k)!}{j!(j+k)!(n-j)!}
\]
matchings that leave \(j\) unmatched smaller-shore vertices. Multiplying by \(\lambda^{n-j}\), dividing by the common factor \(n!(n+k)!\lambda^n\), and taking \(\lambda=n/c\) gives precisely the normalized weights in the finding. Conditional on \(J_n=j\), each shore's unmatched set is uniform among subsets of sizes \(j\) and \(j+k\), and the two sets are independent.

**2. Quantitative Bessel limit.** Put \(a_j=c^j/(j!(j+k)!)\) and \(b_{n,j}=(n)_j/n^j\) for \(j\le n\), otherwise \(b_{n,j}=0\). The finite law is the infinite law with weights \(a_j\) tilted by \(b_{n,j}\in[0,1]\). The infinite normalizer is
\[
 \sum_{j\ge0}a_j=c^{-k/2}I_k(2\sqrt c).
\]
For all integers \(j\ge0\),
\[
 1-b_{n,j}\le\frac{j(j-1)}{2n},
\]
by telescoping the product \(\prod_{i=0}^{j-1}(1-i/n)\) when \(j\le n\), and trivially when \(j>n\). Rejection-coupling of the two distributions bounds total variation by \(\mathbb E(1-b_{n,J})\le\mathbb E[J(J-1)]/(2n)\). Shifting the Bessel power series yields \(\mathbb E (J)_r=c^{r/2}I_{k+r}(2\sqrt c)/I_k(2\sqrt c)\), proving the displayed bound and moments. Domination of each weighted factorial-moment series also gives convergence of all fixed moments of \(J_n\).

**3. Strict finite spatial signs.** For an arbitrary \(\lambda>0\), write \(t=1/\lambda\). The normalized deficit generating polynomial is proportional to
\[
 P_{n,k}(t)=\sum_{j=0}^n\frac{(n)_j}{j!(j+k)!}t^j
 =\frac{n!}{(n+k)!}L_n^{(k)}(-t).
\]
The generalized Laguerre polynomial \(L_n^{(k)}\) has \(n\) distinct positive zeros \(x_1,\ldots,x_n\) for \(k\ge0\). This classical fact also follows directly from orthogonality against every polynomial of smaller degree with strictly positive weight \(x^k e^{-x}\) on \((0,\infty)\): fewer than \(n\) real odd-multiplicity sign changes would give a polynomial of degree below \(n\) whose product with \(L_n^{(k)}\) has constant nonzero sign, contradicting orthogonality. Thus
\[
 \mathbb E[s^{J_n}]=\prod_{i=1}^n \frac{x_i+ts}{x_i+t},
 \qquad p_i=\frac{t}{x_i+t}\in(0,1),
\]
so \(J_n\) is a sum of independent Bernoulli variables with distinct success probabilities \(p_i\). Write \(\mu_n=\sum p_i\), \(S_n=\sum p_i^2\), and \(v_n=\sum p_i(1-p_i)>0\). Conditional uniformity in Step 1 gives the exact covariances
\[
 C_{LL}=\frac{\mu_n^2-nS_n}{n^2(n-1)}<0,\qquad
 C_{LR}=\frac{v_n}{n(n+k)}>0.
\]
The first inequality is strict Cauchy–Schwarz because the \(p_i\) are distinct. For \(C_{RR}\), append \(k\) deterministic Bernoulli ones to the \(p_i\) and use the identical formula with \(n+k\) in place of \(n\); the augmented list is nonconstant, hence \(C_{RR}<0\) as well.

**4. Critical covariance coefficients.** Put \(A=f_2-\mu^2\) and \(v=\mu+f_2-\mu^2=\operatorname{Var}(J)>0\). Conditional uniformity gives
\[
 C_{LL}=\frac{\mathbb E[J_n(J_n-1)]}{n(n-1)}-\left(\frac{\mathbb EJ_n}{n}\right)^2,
\]
\[
 C_{RR}=\frac{\mathbb E[(J_n+k)(J_n+k-1)]}{(n+k)(n+k-1)}-\left(\frac{\mathbb EJ_n+k}{n+k}\right)^2.
\]
The cross-shore covariance equals \(\operatorname{Var}(J_n)/(n(n+k))\). Moment convergence proves the three coefficients. To establish strict negativity rather than merely nonpositivity, the Bessel probabilities satisfy \(j\Pr(J=j)=c\Pr(J=j-1)/(j+k)\). Therefore
\[
 \mu=c\,\mathbb E\frac1{J+k+1},\qquad f_2=c\,\mathbb E\frac J{J+k+1},
\]
so \(A=c\operatorname{Cov}(J,1/(J+k+1))<0\), because \(J\) is nondegenerate and the reciprocal is strictly decreasing.

**5. Sharp window order.** In the unscaled activity parametrization, successive deficit weights satisfy
\[
 \frac{w_{n,j+1}}{w_{n,j}}=\frac{n-j}{\lambda_n(j+1)(j+k+1)}.
\]
If \(\lambda_n/n\to\infty\), the sum of weights for \(j\ge1\) divided by \(w_{n,0}\) tends to zero by comparison with \(\sum_{j\ge1}(n/\lambda_n)^j k!/[j!(j+k)!]\). If \(\lambda_n/n\to0\), for each fixed \(r\) all \(w_{n,j+1}/w_{n,j}\to\infty\) for \(0\le j\le r\), forcing \(\Pr(J_n\le r)\to0\). These are exactly the two claimed regimes.

## Verification

The companion `CHECK.py` uses independent recursion over labeled matchings on small complete bipartite graphs, exact rational partition-function comparisons, exact finite-site covariance checks, and numerical checks of the total-variation inequality. Running it with Python 3 produces `MONOMER_DIMER_EXACT_CHECKS_PASSED 728`. These finite and numerical tests supplement but do not replace the all-size analytic proof above; in particular they are not an exhaustive validation of an infinite limit.

## Relationship to prior work

Heilmann and Lieb (1970) established fundamental analytic properties of the general monomer–dimer system, not the specific near-perfect-matching Bessel deficit law here. Davies, Jenssen, Perkins, and Roberts (2015) established sharp matching occupancy-fraction extremality results using complete bipartite graphs, but their examined model-specific theorems and derivations do not state the present fixed-imbalance saturation window, two-shore signed monomer covariances, or their limiting coefficients. DeSalvo (2026) studies a general Bessel probability law and explicit approximations for conditioned differences and contingency tables, without identifying the present Gibbs matching observable or the same spatial covariance formulas. The factorial matching enumeration, the Laguerre identity, and the abstract Bessel distribution are established tools, not claimed as individually new. This finding is the combined graph-specific finite correlation law, sharp window, and explicit quantitative limit. Prior equivalence in unindexed literature remains possible.

## Limitations

The graph must be complete bipartite, the edge activity uniform and positive, and the imbalance \(k\) fixed as \(n\to\infty\); growing imbalance or heterogeneous weights are not classified. The numerical verifier is supplementary. The result concerns equilibrium matchings rather than irreversible dimer deposition. Historical originality is assessed only against sources actually examined, and independent scientific validation is not claimed.

## References

- O. J. Heilmann and E. H. Lieb, “Monomers and Dimers,” *Physical Review Letters* 24 (1970), 1412; DOI: https://doi.org/10.1103/PhysRevLett.24.1412. Published 1970-06-22; abstract accessible.
- E. Davies, M. Jenssen, W. Perkins, and B. Roberts, “Independent Sets, Matchings, and Occupancy Fractions,” first publicly available 2015-08-19, https://arxiv.org/abs/1508.04675. Relevant full text examined.
- S. DeSalvo, “Two moments suffice for Bessel approximation: conditioned differences, contingency tables, and probabilistic divide-and-conquer,” first publicly available 2026-10-30, https://arxiv.org/abs/2611.00263. Relevant full text examined.
