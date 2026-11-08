# Exact finite-population consensus decay at two neutral contrarian corners

## Finding

At two singular parameter corners of the ratio-dependent, three-agent contrarian-majority model, the deterministic opinion-density map is respectively the identity or a global opinion reversal. The finite, randomly repartitioned population is not stationary at either corner: its heterozygosity has the exact geometric law

\[
\mathbb E\!\left[p_t(1-p_t)\right]=p_0(1-p_0)q_N^t,\qquad q_N=1-\frac{2}{3(N-1)},
\]

for every integer \(t\ge0\) and every \(N\ge3\) divisible by three. It reaches the unanimous set in finite time almost surely, with the exact exponential tail rate \(\log q_N\). At the identity corner it fixes to either opinion; at the reversal corner it enters an alternating unanimous pair. In each case the probability assigned to the initially A-favored eventual consensus phase is exactly the initial A fraction.

## Assumptions and scope

Fix \(N=3m\ge3\) labeled agents with opinions in \(\{A,B\}\). At each integer time choose uniformly a partition of these agents into unordered triples, independently of earlier partitions and local activation coins. In every triple, first determine its current majority. Conditional on the original triple being unanimous, each agent independently opposes the majority with probability \(c_{3,0}\); conditional on its having a two-to-one majority, each agent independently opposes the majority with probability \(c_{2,1}\). Every agent otherwise adopts that majority. The parameters are reactivated on each round and are symmetric under the interchange \(A\leftrightarrow B\). This specifies an annealed Markov chain, not a model with permanently assigned contrarian personalities and not a single Bernoulli flip shared by a whole triple.

Let \(K_t\in\{0,\ldots,N\}\) count opinion A, \(p_t=K_t/N\), and initially \(K_0=k\). The *neutral corner* is

\[
(c_{3,0},c_{2,1})=(0,1/3),
\]

and the *reversal corner* is

\[
(c_{3,0},c_{2,1})=(1,2/3).
\]

The source density polynomial is

\[
F(p)=(1-c_{3,0})p^3+3(1-c_{2,1})p^2(1-p)+3c_{2,1}p(1-p)^2+c_{3,0}(1-p)^3.
\]

Direct substitution gives \(F(p)=p\) and \(F(p)=1-p\) at the respective corners. The map-level neutral identity was also identified in earlier local-flip work; the finding here is the *finite-population stochastic law under independent agent activations*, not the already known map identity.

## Proof

**1. Exact conditional local laws.** Suppose a triple contains \(a\in\{0,1,2,3\}\) agents holding A before discussion. At the neutral corner, the number of A agents after discussion is

\[
B_a\sim\operatorname{Binomial}(3,a/3).
\]

Indeed, the unanimous cases yield deterministic unanimous agreement, and in either mixed case each agent follows the original majority with probability \(2/3\) and opposes it with probability \(1/3\). At the reversal corner the corresponding number is

\[
\widehat B_a\sim\operatorname{Binomial}(3,1-a/3).
\]

Consequently, the conditional local means are respectively \(a\) and \(3-a\). At both corners the conditional variance is zero for unanimous triples and exactly \(2/3\) for either mixed triple. Conditional on a given partition, local output coins across distinct triples are independent.

**2. Mixed-triple enumeration.** Let \(M\) denote the number of mixed triples in the randomly selected partition. Given \(K_t=k\), any one triple is a uniformly sampled three-subset, so

\[
\mathbb E[M\mid K_t=k]=\frac N3\left(1-\frac{(k)_3+(N-k)_3}{(N)_3}\right)=\frac{k(N-k)}{N-1},
\]

where \((r)_3=r(r-1)(r-2)\), also taken as zero when \(r<3\). The cancellation is valid for \(N=3\) as well. For each fixed partition, the conditional total mean is \(k\) at the neutral corner and \(N-k\) at the reversal corner, independent of that partition. The law of total variance therefore gives

\[
\begin{aligned}
\mathbb E[K_{t+1}\mid K_t=k]&=\begin{cases}k&\text{neutral},\\N-k&\text{reversal},\end{cases}\\
\operatorname{Var}(K_{t+1}\mid K_t=k)&=\frac{2k(N-k)}{3(N-1)}.
\end{aligned}
\]

**3. Exact quadratic eigenfunction.** Define \(H(k)=k(N-k)\). At either corner, using the preceding conditional mean and variance,

\[
\mathbb E[H(K_{t+1})\mid K_t=k]
=H(k)-\frac{2k(N-k)}{3(N-1)}=q_NH(k),
\]

where \(q_N=1-2/[3(N-1)]\in(0,1)\). Iteration gives, with no asymptotic approximation,

\[
\mathbb E[H(K_t)]=H(k)q_N^t,
\qquad
\mathbb E[p_t(1-p_t)]=\frac{H(k)}{N^2}q_N^t.
\]

The neutral process \(K_t\) is a bounded martingale. At the reversal corner, \((-1)^t(K_t-N/2)\) is a bounded martingale. For any opinion configuration, the reversal update is obtained by complementing the neutral output, and the neutral transition kernel commutes with global opinion complementation. Therefore the full configuration-valued kernels obey \(P_{\mathrm{rev}}=P_{\mathrm{neu}}C=CP_{\mathrm{neu}}\) and \(P_{\mathrm{rev}}^t=P_{\mathrm{neu}}^tC^t\), where \(C\) complements all opinions. This is a distributional duality, not merely an equality of moments.

**4. Finite-time entry and its sharp tail exponent.** Let \(T=\inf\{t\ge0:K_t\in\{0,N\}\}\). Both corners preserve the set \(\{0,N\}\): the neutral chain keeps each unanimity, while the reversal chain swaps the two every round. Hence \(\{T>t\}=\{0<K_t<N\}\). On this event,

\[
N-1\le H(K_t)\le N^2/4.
\]

For \(0<k<N\) the exact expected quadratic law yields the two-sided survival estimates

\[
\frac{4k(N-k)}{N^2}q_N^t
\le\mathbb P(T>t)\le
\frac{k(N-k)}{N-1}q_N^t.
\]

Thus \(T<\infty\) almost surely and, since both constants are positive,

\[
\lim_{t\to\infty}\frac{1}{t}\log\mathbb P(T>t)=\log q_N.
\]

If \(k=0\) or \(k=N\), then \(T=0\) deterministically and the displayed positive-constant tail assertion is not invoked.

**5. Exact outcome probabilities.** At the neutral corner, bounded martingale convergence and almost-sure unanimity imply \(K_t\to K_\infty\in\{0,N\}\), so \(\mathbb P(K_\infty=N)=k/N\). At the reversal corner, the signed centered bounded martingale converges to \(+N/2\) exactly on the event that all sufficiently late even rounds are all A and all sufficiently late odd rounds are all B, and to \(-N/2\) for the opposite phase. Its expectation remains \(k-N/2\), proving that the first phase has probability \(k/N\).

## Verification

The included standalone `check.py` enumerates every unordered triple partition and each possible post-update binomial outcome in exact rational arithmetic for \(N=3,6,9\) and every initial A count. It checks both conditional means, the conditional variance, the one-step quadratic eigenfunction, global-complement kernel duality, the deterministic identity/involution substitutions, and the \(N=3\) special case. In that three-agent case the consensus-set entrance time from either mixed initial state is geometric with success probability \(1/3\), hence mean \(3\). All exact finite tests passed. These tests corroborate but do not substitute for the symbolic proof valid for every multiple of three.

Reproduce with `python check.py`; it uses only the Python standard library.

## Relationship to prior work

Galam (2026, *Entropy* 28(4), 443, first published April 14) defines the two independent contrarian activation probabilities and computes the associated density recursion, fixed points, and phase diagram. Toth and Galam (2021 preprint; 2022 journal) identified the infinite fixed-point identity regime for a configuration-dependent *group-decision flip* model; this is not claimed new here. Galam's July 2026 microscopic study analyzes reversibility and nonequilibrium flux for a different, uniform-contrarian model. Neutral fixation probabilities and quadratic diversity observables are classical motifs in voter and genetic-drift processes; the specific independent-per-agent triple updating, dual singular corners, exact \(N\)-dependent eigenvalue and both-phase consensus-time law above are the assessed additional statements. No general uniqueness of this result across unpublished or unindexed literature is claimed.

## Limitations

The independent Bernoulli activations and uniform fresh repartitioning are essential to the exact variance factor. Fixed personalities, shared flips of an entire group, spatially fixed groups, nonuniform shuffling, other update protocols, and populations not divisible by three are outside this theorem. The result gives exact diversity decay and the sharp *exponential rate* of the consensus-set hitting-time tail, not its exact full distribution or optimal prefactor for every \(N\). It does not address parameter neighborhoods away from the two exact corners, global mixing in a spatial model, or social realism of those extreme behavioral rates.

## References

1. S. Galam, “Ratio-Dependent Contrarian Activation in Opinion Dynamics,” *Entropy* **28**(4), 443 (published April 14, 2026). DOI: https://doi.org/10.3390/e28040443 ; open preprint https://arxiv.org/html/2604.27226v1 .
2. G. Toth and S. Galam, “Deviations from the Majority: A Local Flip Model,” arXiv:2107.09344 (first posted July 20, 2021); *Chaos, Solitons & Fractals* **159**, 112130 (2022). https://arxiv.org/abs/2107.09344 .
3. S. Galam, “Contrarian Majority Dynamics: Violation of Detailed Balance and Nonequilibrium Steady States,” arXiv:2607.02358 (first posted July 2, 2026). https://arxiv.org/abs/2607.02358 .
4. G. Toth, “Models of opinion dynamics with random parametrisation,” *Journal of Mathematical Physics* **65**, 073301 (2024). https://doi.org/10.1063/5.0159643 .
