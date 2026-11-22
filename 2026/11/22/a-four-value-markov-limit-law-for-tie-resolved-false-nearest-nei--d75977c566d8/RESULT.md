# A four-value Markov limit law for tie-resolved false nearest neighbours

## Finding

Let \(0<a,b<1\), and let the stationary two-symbol Markov chain have transition matrix
\[
P=\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix},\qquad
\pi_0=\frac{b}{a+b},\qquad \pi_1=\frac{a}{a+b}.
\]
For its coordinate observation \(h(x)=x_0\), use the ordinary one-delay false-nearest-neighbour (FNN) statistic with ties resolved by the smallest *other* sample index, and any fixed positive distance-ratio and amplitude tolerances. The proportion \(F_n\) of false neighbours among \(n\) sample positions converges almost surely to a random variable \(L\) taking at most four values. The complete law (entries with equal values combine) is:

| Probability | Value of \(L\) |
|---|---|
| \((1-a)b\) | \(\pi_0 a+\pi_1(1-b)\) |
| \((1-a)(1-b)\) | \(\pi_0 a+\pi_1 b\) |
| \(ab\) | \(\pi_0(1-a)+\pi_1(1-b)\) |
| \(a(1-b)\) | \(\pi_0(1-a)+\pi_1 b\) |

In particular,
\[
\mathbb E L=\frac{2ab(2-a-b)}{a+b},\quad
\operatorname{Var}(L)=\frac{b^2a(1-a)(1-2a)^2+a^2b(1-b)(1-2b)^2}{(a+b)^2}.
\]
The limit is a deterministic constant precisely when \(a=b=1/2\). Even along the equal-stationary-mass family \(a=b=s\), its expectation \(2s(1-s)\) varies with temporal persistence, and the limit is random whenever \(s\ne1/2\).

## Assumptions and scope

Consider a *two-sided* stationary ergodic Markov shift on \(\{0,1\}^\mathbb Z\) with both transition probabilities strictly between zero and one. On a finite observation record \(X_0,\ldots,X_n\), use delay length one: \(y_i=X_i\) for \(0\le i<n\). For each \(i\), a nearest neighbour is a position \(j\ne i\) minimizing \(|X_i-X_j|\), and ties go to the smallest such \(j\). A false neighbour is declared when the next-symbol difference and the distance satisfy either of the usual FNN tests, with both tolerances fixed and strictly positive. In the zero-distance case, the ratio is interpreted as infinite if the next symbols disagree and zero otherwise, as in the source's Definition 1.1. This is **not** a smooth generic-observable theorem and does not cover arbitrary tie-breaking.

## Proof

1. Both symbols recur infinitely often almost surely. Let \(J_s=\min\{i\ge0:X_i=s\}\) and \(A_s=X_{J_s+1}\). After a finite random time, the first matching observation for each symbol is fixed at \(J_s\), so every sample position other than the two positions \(J_0,J_1\) selects \(J_{X_i}\) as its nearest neighbour. Those two exceptional positions contribute at most \(2/n\) to \(F_n\). All other chosen distances vanish. Consequently a false neighbour occurs precisely when \(X_{i+1}\ne A_{X_i}\), regardless of the fixed positive tolerances.

2. The finite-state ergodic theorem applies simultaneously to all transition pairs \((X_i,X_{i+1})\). Therefore, conditional on the finite random values \(A_0,A_1\),
\[
F_n\longrightarrow L=\sum_{s=0}^1\pi_s\left(1-P_{s,A_s}\right)
\]
almost surely. This is a pathwise statement; no independence of \(A_s\) from the distant sample is needed.

3. The first-hit successor variables \(A_0,A_1\) are independent. To see this, condition on \(X_0=s\). Then \(J_s=0\), while \(T=J_{1-s}\ge1\) is the first hitting time of the opposite symbol. The transition \(A_s=X_1\) is measurable with respect to the stopped history at \(T\). By the strong Markov property, \(A_{1-s}=X_{T+1}\) is independent of that history with law the row \(P_{1-s},\cdot}\). Thus the joint law is always \(P_{0,\cdot}\otimes P_{1,\cdot}\), independently of \(s\), and remains so unconditionally. Hence \(\Pr(A_0=1)=a\) and \(\Pr(A_1=0)=b\).

4. Substituting the four pairs \((A_0,A_1)\in\{0,1\}^2\) gives exactly the displayed law. The independent component at symbol zero takes values \(a\) and \(1-a\) with probabilities \(1-a\) and \(a\); that at symbol one takes values \(1-b\) and \(b\) with probabilities \(b\) and \(1-b\). Elementary two-point mean and variance identities give the stated formulas. Every factor in the variance numerator is nonnegative and \(a,b\in(0,1)\), so vanishing requires \(1-2a=1-2b=0\). Finally, \(a=b=s\) gives equal stationary masses but mean \(2s(1-s)\), as asserted.

## Verification

The supplied self-contained \(check.py\) exhaustively checks the four weights, mean and variance with exact rational arithmetic at 81 interior parameter pairs and compares 16 length-100000 generated Markov records with the first-hit limiting expression. These computations check the formulas and implementation; the infinite almost-sure convergence follows from the ergodic and strong Markov arguments above, not from finite sampling.

## Relationship to prior work

Śpiewak (2026) analyzes the ordinary FNN algorithm for generic smooth observables and dimensions of invariant measures, not binary quantized observables with a fixed minimum-index tie rule. Kennel and Buhl (2003) introduce a *different symbolic-FNN partition-refinement procedure*. For independent Bernoulli symbols the related four-value law is recovered as the special transition subfamily \(a+b=1\). The correlated case needs the first-hit strong-Markov calculation, and, unlike an IID one-symbol marginal model, its expected limiting FNN score changes when transition persistence changes while stationary symbol masses remain fixed.

## Limitations

The law depends essentially on deterministic smallest-index tie resolution and the one-delay binary quantization; other tie conventions, higher delays, noisy continuous observations and non-Markov sources are not classified. Four listed values may coincide. Results are not an assessment of whether a binary observable provides a valid embedding, and no independent review is claimed. Literature search cannot prove absolute novelty; a different earlier formulation remains possible.

## References

- A. Śpiewak, *On the convergence of the False Nearest Neighbours algorithm*, arXiv:2611.18087v1, publicly posted 13 November 2026. https://arxiv.org/html/2611.18087v1
- M. B. Kennel and M. Buhl, *Estimating good discrete partitions from observed data: symbolic false nearest neighbors*, Physical Review Letters 91 (2003), 084102; arXiv:nlin/0304054. https://arxiv.org/abs/nlin/0304054
