# Cycle-length ordering of observed entropy under stochastic resetting

## Finding
Fix an integer \(n\ge3\). On the cycle \(C_n=\mathbb Z/n\mathbb Z\), a walker at each discrete time either resets to vertex \(0\) with probability \(\gamma\in(0,1)\) or moves to either cyclic neighbour with probability \((1-\gamma)/2\) each. Only successive **vertices** are observed; reset labels are not. Let \(h_n(\gamma)\) be the stationary Shannon entropy rate (natural logarithms). Define
\[
 z=1-\gamma,\qquad d=\sqrt{\gamma(2-\gamma)},\qquad q=\frac{z}{1+d}\in(0,1),\qquad a=\frac z2,
\]
\[
 B(\gamma)=-\gamma\log\gamma-z\log(z/2),\qquad
 \Delta(\gamma)=(\gamma+a)\log(\gamma+a)-\gamma\log\gamma-a\log a>0.
\]
Then, for every \(n\ge3\) and \(0<\gamma<1\),
\[
 \boxed{h_n(\gamma)=B(\gamma)-\frac{2\gamma\Delta(\gamma)}d
 \frac{q+q^{n-1}}{1-q^n}.}
\]
The infinite-line reset walk has entropy rate
\[
 h_\infty(\gamma)=B(\gamma)-\frac{2\gamma\Delta(\gamma)}d q,
\]
and the **exact** finite-cycle deficit is
\[
 \boxed{h_\infty(\gamma)-h_n(\gamma)=
 \frac{2\gamma\Delta(\gamma)}d\frac{(1+q^2)q^{n-1}}{1-q^n}>0.}
\]
Consequently the complete size ordering at every fixed positive reset probability is
\[
 \boxed{h_3(\gamma)<h_4(\gamma)<h_5(\gamma)<\cdots<h_\infty(\gamma).}
\]
For fixed \(\gamma\), the deficit is asymptotic to \(2\gamma\Delta(\gamma)(1+q^2)q^{n-1}/d\), giving its **exact** exponential convergence rate and prefactor. If \(M_n=\max_{0\le\gamma\le1}h_n(\gamma)\), then each maximum is attained at an interior positive resetting probability, and
\[
 \boxed{\log2<M_3<M_4<\cdots\nearrow M_\infty<\log3.}
\]
These inequalities do not assume or assert uniqueness of maximizing resetting probabilities.

## Assumptions and scope
For every integer \(n\ge3\), the ring has distinct clockwise and anticlockwise neighbours. The transition matrix, with all entries to the same destination **merged**, is
\[
 Q_{\gamma,n}(i,j)=\gamma\mathbf1_{\{j=0\}}+
 \frac{1-\gamma}{2}\bigl(\mathbf1_{\{j=i+1\pmod n\}}+\mathbf1_{\{j=i-1\pmod n\}}\bigr).
\]
At \(\gamma>0\) this finite chain has a unique stationary law \(\pi_n\). For the infinite line the analogous reset chain also has a unique stationary probability law. The entropy rate is the conditional entropy of the next observed vertex given the current vertex, averaged in stationarity: \(h_n=\sum_i\pi_n(i)H(Q_{\gamma,n}(i,\cdot))\). It is **not** thermodynamic entropy production or the entropy of the unobserved reset/hop action. Endpoint values are continuous extensions, \(h_n(0)=\log2\) and \(h_n(1)=0\); the strict size comparisons concern \(0<\gamma<1\).

## Proof
**1. Reset-renewal Green function.** Let \(P_n\) denote the unbiased nearest-neighbour transition matrix on \(C_n\). The reset law is
\[
 \pi_n(j)=\gamma\sum_{t=0}^\infty z^tP_n^t(0,j),\qquad z=1-\gamma.
\]
For the simple random walk on \(\mathbb Z\), the Green sequence \(G_z(k)=\sum_{t\ge0}z^tP_{\mathbb Z}^t(0,k)\) solves \(G_z(k)=z[G_z(k-1)+G_z(k+1)]/2\) away from zero and \(G_z(0)=1+zG_z(1)\). The positive summable solution is
\[
 G_z(k)=\frac{q^{|k|}}d,\qquad
 d=\sqrt{1-z^2},\qquad q=\frac{z}{1+d},
\]
using \(z(q+q^{-1})=2\) and \(G_z(0)=1/d\). Projecting the line walk modulo \(n\), then summing the absolutely convergent image series, gives for \(0\le j<n\)
\[
 \pi_n(j)=\frac{\gamma}{d}\sum_{\ell\in\mathbb Z}q^{|j+\ell n|}
 =\frac{\gamma}{d}\frac{q^j+q^{n-j}}{1-q^n}.
\]
At \(j=0\) this formula is understood as \((1+q^n)/(1-q^n)\). In particular \(\pi_n(1)=\pi_n(n-1)=\gamma(q+q^{n-1})/[d(1-q^n)]\). The infinite-line neighbour occupation is \(\pi_\infty(1)=\gamma q/d\).

**2. Local entropy and merged actions.** At a vertex other than the two neighbours of the reset vertex, the three possible observed successor probabilities are \(\gamma,a,a\) with \(a=z/2\), so the outgoing entropy is \(B(\gamma)\). At either neighbour of zero, reset and the ordinary move toward zero have identical observed destination, so its row probabilities are \(\gamma+a,a\); its entropy is \(B(\gamma)-\Delta(\gamma)\). The same holds at the two vertices for \(n=3\); there are still exactly two reset neighbours, while the root has three distinct successors. The merging loss is positive because
\[
 \Delta(\gamma)=(\gamma+a)\,H_2\bigl(\gamma/(\gamma+a)\bigr)>0,
\]
where \(H_2(u)=-u\log u-(1-u)\log(1-u)\). Stationary averaging yields \(h_n=B-2\pi_n(1)\Delta\). Substituting Step 1 proves the asserted finite and infinite formulas.

**3. Exact finite-size deficit and strict order.** Subtracting the infinite-line expression from the image sum and factoring,
\[
 \frac{q+q^{n-1}}{1-q^n}-q=
 \frac{(1+q^2)q^{n-1}}{1-q^n}.
\]
All factors in the stated deficit are strictly positive. Define \(g_n=q^{n-1}/(1-q^n)\). For \(0<q<1\),
\[
 \frac{g_{n+1}}{g_n}=q\frac{1-q^n}{1-q^{n+1}}<1.
\]
Therefore the deficits strictly decrease with \(n\), proving \(h_{n+1}>h_n\) for every \(n\ge3\). The exact formula gives the claimed geometric asymptotic immediately as \(n\to\infty\) with \(\gamma\) fixed. This strict all-rate ordering is not explained by termwise ordering of unreset return probabilities: at four steps, \(P_{C_4}^4(0,0)=1/2\) exceeds \(P_{C_3}^4(0,0)=3/8\), whereas at three steps \(P_{C_3}^3(0,0)=1/4>P_{C_4}^3(0,0)=0\). The Green-function resummation is essential.

**4. Optimized entropy hierarchy.** Each \(h_n\) is continuous at \(\gamma=0,1\) by the stationary-resolvent expression. For fixed \(n\), \(\pi_n(1)\to1/n\) as \(\gamma\downarrow0\), since the geometric resolvent of a finite irreducible walk tends to its unique invariant law, even when the unreset walk is periodic. Expansion gives
\[
 h_n(\gamma)=\log2+\left(1-\frac2n\right)\gamma\log(1/\gamma)+O_n(\gamma).
\]
Thus \(M_n>\log2\) and, since \(h_n(1)=0\), a maximizer lies in \((0,1)\). Applying the pointwise strict inequality at a maximizer of \(h_n\) yields \(M_{n+1}>M_n\). Pointwise \(h_n\uparrow h_\infty\), and choosing any near-maximizer of the limiting function shows \(M_n\uparrow M_\infty\). Finally, every positive reset probability has a strictly positive collision loss and \(B(\gamma)\le\log3\); at \(\gamma=0,1\) the continuous limiting entropies are \(\log2,0\). Compactness gives \(M_\infty<\log3\). This completes all claims.

## Verification
The accompanying Python standard-library program `verify.py` independently constructs exact rational transition matrices, solves exact rational stationary systems, and computes row entropies directly from their **merged** probabilities. Its 1,048 checks compare them with the Green-function expression, verify stationary normalization and balance, test the finite-size deficit identity and finite examples of strict size ordering, and check the Green root recurrence. Execute with `python3 verify.py`. These finite diagnostics do not prove the all-size theorem; Steps 1–4 do.

As numerical illustrations (not certified extrema), at \(\gamma=1/3\), the entropy rates for the triangle, square and pentagon are respectively about \(0.8675632285\), \(0.9137730407\), and \(0.9305766085\) nats per step, versus the infinite-line value about \(0.9407407232\). The direct matrix solver and the analytic formula agree to the checker tolerance across the tested domains.

## Relationship to prior work
Wang and Chen (2022) established the reset-chain transition matrix and stationary Green/resolvent approach, and studied the Markov entropy rate on networks. Their regular-network simplified entropy formula treats the reset label as a separate outcome even when a normal jump reaches the same vertex; it is not the observed-vertex entropy in the present model. The published result *Sharp regular-graph entropy envelope for random walks with stochastic resetting* supplies the general collision correction and sharp high-girth universal-cover upper envelope, and shows convergence along large-girth regular graphs. We use that conceptual distinction as established prior work. It does **not** give the ring-specific closed form, a strict comparison between *successive* ring sizes, or the exact positive finite-size deficit and asymptotic coefficient. The published complete-graph entropy optimization likewise concerns another graph family, not these statements. Zelenkovski and collaborators (2023) explicitly use the merged reset transition matrix but study search time, not path entropy. These comparisons concern the implications of stated theorems; novelty remains conditional on bibliographic completeness.

## Limitations
The model requires symmetric nearest-neighbour walking, one fixed reset vertex, constant per-step reset probability, finite cycles with \(n\ge3\), and observed vertices rather than reset-action labels. It does not establish unique optimal reset rates or their monotonicity with cycle size, and it does not extend the strict ordering to arbitrary graph families. The exact finite-size correction specializes an already known graph-wide collision mechanism and upper envelope; that limits the breadth and priority significance of the contribution. External independent scientific review has not been performed.

## References
1. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665 (first posted 2022-08-11), https://arxiv.org/abs/2208.05665.
2. *Sharp regular-graph entropy envelope for random walks with stochastic resetting* (2026-10-18), https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-regular-graph-entropy-envelope-for-random-walks-with-stoch--4bc2723b4c40/RESULT.md.
3. *Lambert-\(W\) entropy-optimal resetting on complete graphs* (2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-lambert-w-entropy-optimal-resetting-on-complete-graphs--86b682727fbd/RESULT.md.
4. K. Zelenkovski et al., *Random Walks on Networks with Centrality-Based Stochastic Resetting*, Entropy 25, 293 (2023), https://www.mdpi.com/1099-4300/25/2/293.
