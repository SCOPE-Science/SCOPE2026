# Exact sample-size suppression in finite neutral complex contagion

## Finding
Consider neutral two-type social imitation with a quadratic exposure threshold. For every population size \(N\ge 2\) and every number \(m\ge 1\) of independent encounters sampled uniformly with replacement, including possible self-encounters, the exact fixation probability \(H_{N,m}(i)\) from \(i\in\{0,\ldots,N\}\) individuals of type \(X\) is determined by the following positive weights.

When \(m=1\), \(H_{N,1}(i)=i/N\). For \(m\ge2\), put \(\alpha=N/(m-1)\) and
\[
 w_k=\frac{\Gamma(N+\alpha)\Gamma(1+\alpha)}{\Gamma(N-k+\alpha)\Gamma(k+1+\alpha)}\quad(0\le k\le N-1),\qquad
 H_{N,m}(i)=\frac{\sum_{k=0}^{i-1}w_k}{\sum_{k=0}^{N-1}w_k}.
\]
(The empty numerator for \(i=0\) is zero.) The weights satisfy \(w_k=w_{N-1-k}\). For every \(N\ge3\), the one-mutant fixation probability strictly decreases with the encounter size \(m\), and
\[
 2^{1-N}< H_{N,m}(1)<\frac1N\quad(m\ge2),\qquad
 \lim_{m\to\infty}H_{N,m}(1)=2^{1-N}.
\]
For \(N=2\), the fixation probability from one individual is always \(1/2\).

For each *fixed integer* \(m\ge2\), write \(a=1/(m-1)\) and
\[
 I_m=(1+a)\log(1+a)+a\log a-2(a+\tfrac12)\log(a+\tfrac12)>0.
\]
Then the sharp population-size asymptotic is
\[
 H_{N,m}(1)\sim\sqrt{\frac{1+a}{\pi N a(a+\tfrac12)}}\,\exp(-NI_m)\quad(N\to\infty).
\]
The rate \(I_m\) strictly increases with \(m\), from \(I_2=\log(32/27)\) toward \(\log 2\); thus even two independently sampled contacts turn neutral rarity from the voter-law \(1/N\) into exponential fixation suppression. These are results about eventual absorption, not deterministic coexistence or finite-time quasi-stationarity.

## Assumptions and scope
There are \(N\) labeled agents with types \(X\) and \(Y\). At each discrete step one focal individual is chosen uniformly. Independently, \(m\) contacts are drawn independently and uniformly from the entire current population, *with replacement*; both repeated contacts and sampling of the focal individual are allowed. If \(K\) contacts have type \(X\), a type-\(Y\) focal individual changes to \(X\) with probability \((1/2)(K/m)^2\), and a type-\(X\) focal individual changes to \(Y\) with probability \((1/2)(1-K/m)^2\). Otherwise no change occurs. One may implement the quadratic factor by independently drawing a threshold \(M\) with distribution \(\Pr(M\le z)=z^2\) on \([0,1]\) and, if the opposite-type encounter fraction is at least \(M\), switching with neutral Fermi probability \(1/2\). Payoffs of the two types are equal; no mutation, immigration, or spontaneous change occurs. The absorbing states are the all-\(X\) and all-\(Y\) configurations.

The binomial with-replacement exposure assumption is essential: without-replacement contact sampling or a graph excluding the focal individual produces different finite-state rates. For the large-\(N\) asymptotic, \(m\) is fixed before \(N\to\infty\); the two limits are not asserted to commute uniformly.

## Proof
Write \(x=i/N\) and let \(K\sim\operatorname{Bin}(m,x)\). The second binomial moment gives
\[
 B_m(x)=\mathbb E[(K/m)^2]=x^2+\frac{x(1-x)}m.
\]
The count of type-\(X\) agents is therefore a birth--death chain with one-step transition probabilities
\[
 p_i=\tfrac12(1-x) B_m(x),\qquad q_i=\tfrac12 x B_m(1-x)
 \quad (1\le i\le N-1).
\]
Both probabilities are strictly positive for interior states, so absorption in \(0\) or \(N\) occurs almost surely. Direct cancellation yields
\[
 \frac{q_i}{p_i}=\frac{m(N-i)+i}{mi+N-i}.
\]
When \(m=1\), this ratio is one, and the harmonic equation for the absorption probability gives \(H_{N,1}(i)=i/N\). When \(m\ge2\), with \(\alpha=N/(m-1)\), it is \((N+\alpha-i)/(\alpha+i)\). For \(\Delta_i=H_{N,m}(i)-H_{N,m}(i-1)\), the harmonic equation
\[
 p_i(H_{N,m}(i+1)-H_{N,m}(i))=q_i(H_{N,m}(i)-H_{N,m}(i-1))
\]
shows that \(\Delta_{i+1}/\Delta_i=q_i/p_i\). Repeated multiplication gives \(\Delta_{k+1}=\Delta_1 w_k\) with the displayed Gamma-product weights. The boundary condition \(\sum_{i=1}^N\Delta_i=1\) proves the exact formula. Gamma reflection is not needed: direct cancellation of the finite products gives \(w_k=w_{N-1-k}\).

For \(0<k\le\lfloor(N-1)/2\rfloor\), each factor \((N-j+\alpha)/(j+\alpha)\) for \(1\le j\le k\) is at least one, and at least the first is strictly greater than one if \(N\ge3\). Its logarithmic derivative in \(\alpha\) is \(1/(N-j+\alpha)-1/(j+\alpha)\le0\), strictly for \(j<N/2\). Hence every interior weight \(w_k\), extended to the opposite half by symmetry, strictly *decreases* with \(\alpha\). Because \(\alpha=N/(m-1)\), the normalizing sum strictly increases with \(m\), so \(H_{N,m}(1)=1/\sum_k w_k\) strictly decreases. Moreover \(\alpha\to\infty\) makes all \(w_k\to1\), while \(\alpha\downarrow0\) gives \(w_k\to\binom{N-1}{k}\). This proves the two strict bounds and the \(m\to\infty\) limit. The case \(N=2\) follows from the two unit weights.

For the sharp asymptotic let \(a=1/(m-1)>0\), so \(\alpha=aN\), and put \(x=k/N\). Stirling's formula, uniformly on compact subsets of \((0,1)\), gives
\[
 w_k=\left(\sqrt{\frac{a(1+a-x)}{(1+a)(a+x)}}+o(1)\right)e^{N\phi_a(x)},
\]
where
\[
 \phi_a(x)=(1+a)\log(1+a)+a\log a
 -(1+a-x)\log(1+a-x)-(a+x)\log(a+x).
\]
The function \(\phi_a\) is strictly concave, since
\[
 \phi_a'(x)=\log\frac{1+a-x}{a+x},\qquad
 \phi_a''(x)=-\frac1{1+a-x}-\frac1{a+x}<0.
\]
Its unique maximum is \(\phi_a(1/2)=I_m\), and \(\phi_a''(1/2)=-2/(a+1/2)\). Contributions away from any fixed neighborhood of \(1/2\) are exponentially smaller; Stirling estimates also bound the endpoint terms. Applying the discrete Laplace method gives
\[
 \sum_{k=0}^{N-1}w_k\sim
 \sqrt{\frac{a}{1+a}}\sqrt{\pi N(a+\tfrac12)}\,e^{NI_m}.
\]
Taking its reciprocal proves the stated exact prefactor and exponential rate. Finally,
\[
 \frac{d}{da}I_m=\log\frac{a(1+a)}{(a+\tfrac12)^2}<0,
\]
so \(I_m\) increases as \(m\) increases, while its limits as \(a\to\infty\) and \(a\downarrow0\) are \(0\) and \(\log2\). At \(m=2\), \(a=1\), yielding \(I_2=\log(32/27)\).

## Verification
`verify.py` is standalone (Python standard library) and independently evaluates the exact binomial encounter sums rather than treating the simplified quadratic moment as an input. It compares the candidate exit probabilities with harmonic equations for \(2\le N\le23\), \(1\le m\le11\), solves independent rational linear systems for smaller populations, checks reflection and monotonicity, and compares exact Gamma-sum probabilities with the saddlepoint asymptotic at several population sizes. The extracted program reports `VERIFY_OK` with 2863 checked instances. Finite checks support, but do not replace, the all-population proof and Laplace argument.

## Relationship to prior work
Chiba-Okabe and Plotkin, *Social learning with complex contagion* (2024), introduce the stochastic Fermi-plus-threshold update with binomial encounter statistics and primarily analyze its large-population replicator-like limit and finite simulations. At zero payoff difference and quadratic threshold, its exact finite-binomial encounter mechanism is the one studied here. The earlier nonlinear \(q\)-voter literature of Castellano, Muñoz and Pastor-Satorras (2009), and Moretti et al. (2013), provides the same *mean-field flipping polynomial* in the \(q=2\) case with noise parameter \(\varepsilon=1/(2m)\): \(z^2+2\varepsilon z(1-z)\). Those papers already establish the qualitative existence of ordering for \(\varepsilon<1/2\) and use Fokker--Planck large-population approximations. They do not, in the inspected calculations, state this finite contact-sample fixation formula, exact monotonicity in \(m\), or fixed-\(m\) one-mutant exponential rate and prefactor. This work claims none of their baseline model, their qualitative phase structure, or the general birth--death absorption identity as new. It concerns a with-replacement encounter mechanism, not a finite graph implementation that excludes the focal neighbor.

## Limitations
The result is neutral (no payoff selection), uses one fixed quadratic threshold shape and binomial with-replacement encounter samples, and concerns eventual fixation rather than fixation times or general graphs. The asymptotic is proved for each fixed \(m\ge2\), not uniformly when \(m\) grows with \(N\). Although a direct covering theorem was not located in inspected sources, historical nonlinear-voter theory is substantial and an equivalent unindexed finite-state derivation may exist. No independent external audit or priority certification has been performed.

## References
1. H. Chiba-Okabe and J. B. Plotkin, *Social learning with complex contagion*, arXiv:2406.14922v1 (first publicly posted 2024-06-21), https://arxiv.org/html/2406.14922v1 .
2. C. Castellano, M. A. Muñoz and R. Pastor-Satorras, *The non-linear q-voter model*, arXiv:0907.1775, https://arxiv.org/pdf/0907.1775 .
3. P. Moretti, S. Liu, C. Castellano and R. Pastor-Satorras, *Mean-field analysis of the q-voter model on networks*, arXiv:1301.7563, https://arxiv.org/pdf/1301.7563 .
