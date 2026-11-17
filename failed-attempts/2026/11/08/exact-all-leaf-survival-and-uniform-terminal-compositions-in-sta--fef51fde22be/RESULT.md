# Exact all-leaf survival and uniform terminal compositions in star-opinion voter dynamics

## Finding
Let \(r\ge3\) and \(n\ge r+1\) be integers. For the symmetric productive opinion-graph voter process on the star with \(r\) mutually incompatible leaves, initialize one agent in each leaf and the remaining \(n-r\) agents at the center. At its absorbing time, write \(K_i\) for the number of agents with leaf opinion \(i\). For each vector of integers \(k_i\ge1\) with \(\sum_{i=1}^r k_i=n\),
\[
\mathbb P(K_1=k_1,\ldots,K_r=k_r)=\binom{n+r-1}{2r-1}^{-1}.
\]
Consequently, the exact probability that *all initial leaf opinions survive* is
\[
\mathbb P(K_i>0\ \text{for all }i)=\frac{\binom{n-1}{r-1}}{\binom{n+r-1}{2r-1}}=
\frac{(2r-1)!}{(r-1)!\,n(n+1)\cdots(n+r-1)}.
\]
Conditioned on this event, the terminal vector is uniform over all \(\binom{n-1}{r-1}\) positive weakly ordered compositions of \(n\) into \(r\) parts. In particular, for three leaf opinions the all-survive probability is exactly \(60/[n(n+1)(n+2)]\), and for fixed \(r\) it has asymptotic order \(n^{-r}\) with coefficient \((2r-1)!/(r-1)!\).

## Assumptions and scope
There are \(n\) agents, a center opinion \(C\), and leaf opinions \(L_1,\ldots,L_r\). An agent with opinion \(C\) may interact with any leaf opinion, but two leaves never interact with one another. At a productive update, choose uniformly among unordered agent pairs holding adjacent opinions, then choose uniformly one of the two agents to copy the other's opinion. Repeat until no adjacent-opinion agent pairs remain. The same absorption distribution applies to ordinary pair sampling with idle steps deleted. The result concerns the finite-population symmetric process on a complete agent-interaction graph; no directed or asymmetric update biases are allowed.

For each time \(t\), let \(K_i(t)\) denote the leaf count, \(M(t)=\sum_i K_i(t)\) the total leaf population and \(n-M(t)\) the center population. All leaf counts start at one. Absorption occurs exactly when \(M=0\) or \(M=n\): with a nonempty center and at least one leaf, some compatible pair exists. The final statement for a positive vector requires the second absorbing boundary \(M=n\).

## Proof
**Step 1: the aggregate unbiased walk.** When \(0<M=m<n\), the number of center–leaf compatible pairs with leaf type \(i\) is \((n-m)K_i\), so that type is sampled with probability \(K_i/m\). Its count then increases or decreases by one with equal probability \(1/2\), depending on the copying direction. Thus the total leaf count \(M\) makes a simple symmetric nearest-neighbor step, independent of the selected label, and is absorbed at \(0\) or \(n\). Starting from \(r\), the finite gambler's-ruin calculation gives
\[
\mathbb P(M(T)=n)=r/n,
\]
where \(T<\infty\) almost surely.

**Step 2: equality of probabilities for all-positive states, conditional on an aggregate path.** Fix any finite permitted trajectory of aggregate sizes, including the final boundary, and condition on its up/down directions. Because up/down copying is a fair coin independently of which leaf label was selected, given a step from total \(m\) the leaf updated is selected proportionally to its current count. By induction along this prescribed aggregate path, at any intermediate size \(m\), every all-positive vector of leaf counts of total \(m\) has the same conditional probability \(w_m\). The assertion is true initially since the unique positive vector of total \(r\) is \((1,\ldots,1)\). For an up step \(m\to m+1\), any positive target \(k\) receives mass only from positive predecessors \(k-e_i\) with \(k_i\ge2\), totaling
\[
 w_{m+1}=w_m\sum_{i:k_i\ge2}\frac{k_i-1}{m}=w_m\frac{m+1-r}{m},
\]
which is independent of \(k\). For a down step \(m\to m-1\), any positive target \(k\) receives mass from \(k+e_i\), totaling
\[
 w_{m-1}=w_m\sum_{i=1}^r\frac{k_i+1}{m}=w_m\frac{m-1+r}{m},
\]
again independent of \(k\). If the aggregate goes below \(r\), every positive vector is impossible; a leaf opinion with zero count can never reappear, so all subsequent all-positive conditional masses remain zero. Hence, after averaging over every aggregate path that reaches \(M(T)=n\), the probability of each positive terminal vector is one common value \(p\).

**Step 3: a product martingale fixes that common value.** Define \(H(t)=\prod_{i=1}^r K_i(t)\). Only one leaf count changes per productive step and it changes by equal-probability increments \(+1\) or \(-1\); hence \(H(t\wedge T)\) is a bounded martingale. Since \(H(0)=1\) and \(T<\infty\) almost surely, bounded optional stopping yields
\[
 1=\mathbb E[H(T)].
\]
If \(M(T)=0\) or any leaf has gone extinct, the product vanishes. Therefore by Step 2,
\[
 1=p\sum_{\substack{k_i\ge1\\\sum_i k_i=n}}\prod_{i=1}^r k_i.
\]
The generating identity
\[
\left(\sum_{j\ge1}jz^j\right)^r=z^r(1-z)^{-2r}
\]
identifies the sum as the coefficient \(\binom{n+r-1}{2r-1}\). Thus \(p=\binom{n+r-1}{2r-1}^{-1}\), proving the pointwise formula. Counting the positive compositions using stars and bars gives the all-survive probability, and the common mass gives conditional uniformity. The factorial and asymptotic forms follow from expanding the binomial coefficients. \(\square\)

## Verification
The included `proof_checker.py` independently constructs the exact rational absorbing Markov-chain equations for all leaf-count states for eight cases: \((r,n)=(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5)\). It solves the rational boundary-value systems, checks the predicted probability for every positive terminal composition and checks total all-leaf survival. All eight cases passed. Run `python proof_checker.py` with SymPy installed. This finite check tests the proof but does not replace the pathwise martingale argument covering arbitrary integers \(r\ge3\) and \(n\ge r+1\).

## Relationship to prior work
Berenbrink, Götte, Hoefer and Koglin [1] introduce the voter model with opinion graphs and characterize stabilization and individual-opinion survival. Their star case is a natural source of this question; the inspected primary article does not state the exact simultaneous all-leaf survival probability or conditional terminal composition law. Vazquez and Redner [2] analyze the classical constrained three-opinion system, and Mobilia [3] analyzes a biased three-opinion generalization. Both are directly relevant to the two-leaf special case, so no novelty is claimed for that special case. The result here quantifies the simultaneous survival event for *arbitrary* \(r\ge3\) and provides the joint law conditional on full survival. Known martingales and gambler's-ruin methods are explicitly used as proof tools; the result is not claimed to introduce those methods.

## Limitations
This result describes only full survival of all initial leaf types and the terminal composition *conditional on that event*. It does not give the full probability distribution of terminal supports allowing some initial leaves to vanish, nor does it cover unequal initial leaf counts, heterogeneous interaction weights, asymmetric copying, finite interaction networks other than the complete graph, or rates/times to absorption. It also does not assert priority over potentially unindexed equivalent calculations in classical neutral population or branching-process literature. Numerical verification covers only eight small parameter pairs and is not a proof of all-size behavior.

## References
1. P. Berenbrink, T. Götte, M. Hoefer, and T. Koglin, *The Voter Model with Opinion Graph*, arXiv:2610.16684 (first posted 12 October 2026), https://arxiv.org/abs/2610.16684 .
2. F. Vazquez and S. Redner, *Ultimate Fate of Constrained Voters*, J. Phys. A 37 (2004), 8479–8494, arXiv:cond-mat/0405652, https://arxiv.org/abs/cond-mat/0405652 .
3. M. Mobilia, *Fixation and Polarization in a Three-Species Opinion Dynamics Model*, Europhys. Lett. 95 (2011), 50002, arXiv:1104.5147, https://arxiv.org/abs/1104.5147 .
