# Gumbel saturation and a Poisson rare-gap law for discrete dimer parking

## Finding

Let a line have \(n\ge2\) sites and its \(n-1\) possible adjacent dimers. Run the Page–Rényi parking process: every adjacent pair receives attempts at rate one, independently, and an attempt occupies both sites if they are both vacant. Let \(A_n(t)\) count adjacent pairs whose sites are both vacant at time \(t\); let \(\tau_n\) be the time of the final successful attempt and \(T_n\) the total number of attempts through that success (including unsuccessful attempts and the last success).

For every fixed \(x\in\mathbb R\), putting \(t_n(x)=\log n+x\),

\[
A_n(t_n(x))\ \xrightarrow{d}\ \operatorname{Poisson}(e^{-2-x}).
\]

Consequently, for the standard Gumbel law \(\Pr(G\le x)=\exp(-e^{-x})\),

\[
\tau_n-\log n+2\ \xrightarrow{d}\ G,
\qquad
\frac{T_n}{n}-\log n+2\ \xrightarrow{d}\ G.
\]

Equivalently, \(\Pr(\tau_n-\log n\le x)\to\exp(-e^{-2-x})\). The shift \(2\) comes from the exact limiting density \(e^{-2}\) of potentially available dimers near jamming, not from a free fitting constant.

## Assumptions and scope

All attempts are independent rate-one Poisson processes, one per edge of the finite path of \(n\) sites. Successful arrivals irreversibly fill the two endpoint sites. The superposed sequence of attempted edges is i.i.d. uniform among the \(n-1\) edges, hence the attempt-count law is also that of the original discrete uniform-trial model. A fixed \(x\) is held constant while \(n\to\infty\); this is a distributional statement, not an error estimate uniform over growing \(x\).

Each edge's first attempted time \(\xi_i\) is independent \(\operatorname{Exp}(1)\). Its later attempts cannot succeed after its first rejection, so the occupied configuration at any time is exactly the greedy matching obtained by processing those edges with \(\xi_i\le t\) in increasing order. Define \(v(t)=1-e^{-t}\) for \(t\ge0\), and for \(k\ge1\),

\[
u_k(v)=\sum_{j=0}^{k-1}\frac{(-v)^j}{j!}.
\]

## Proof

**1. Exact finite mean.** Consider a separate path of \(k\) sites. Its left endpoint remains vacant up to time \(t\) with probability \(u_k(v(t))\). To see this, set that probability to \(h_k(t)\). The endpoint becomes occupied only when the leftmost edge attempts while both its vertices are free. Removing that edge disconnects the rest, so its instantaneous success probability is \(e^{-t}h_{k-1}(t)\), with the first-attempt clock still unexpired. Thus \(h'_k(t)=-e^{-t}h_{k-1}(t)\), \(h_k(0)=1\), and \(h_1\equiv1\). Passing to \(v=1-e^{-t}\) and inducting yields \(h_k(t)=u_k(v(t))\).

An edge \(i\), separating the sites into lengths \(i\) and \(n-i\), is available at time \(t\) if its own clock exceeds \(t\) and the boundary site on each side is vacant in the respective independent subprocess. Therefore

\[
\Pr\{\text{edge }i\text{ available at }t\}
=e^{-t}u_i(v(t))u_{n-i}(v(t)),
\qquad
\mathbb EA_n(t)=e^{-t}\sum_{i=1}^{n-1}u_i(v(t))u_{n-i}(v(t)).
\]

The alternating exponential-series remainder gives \(|u_k(v)-e^{-v}|\le1/k!\) for all \(0\le v\le1\), and \(0\le u_k(v)\le1\). Hence, uniformly over these \(v\),

\[
\left|\sum_{i=1}^{n-1}u_i(v)u_{n-i}(v)-(n-1)e^{-2v}\right|
\le2\sum_{j=1}^{\infty}\frac1{j!}<4.
\]

At \(t=t_n(x)\), \(e^{-t}=e^{-x}/n\) and \(v\to1\), so \(\mathbb EA_n(t_n(x))\to\lambda_x=e^{-2-x}\).

**2. Finite-window dependence reduction.** Let \(I_i(t)\) indicate availability of edge \(i\). Define \(I_i^{(R)}(t)\) by running the same priority rule with only edge clocks in the radius-\(R\) interval \([i-R,i+R]\cap[1,n-1]\) and checking availability of the middle edge. If \(\xi_i\le t\), both indicators vanish. When \(\xi_i>t\), deciding whether its left endpoint was occupied starts at edge \(i-1\), then can propagate to edge \(i-2\) only if the latter has an earlier clock, and similarly thereafter. For any influence from outside this interval, there must be a strictly decreasing run of at least \(R\) consecutive clock values along the left or the right side. The relative order of any specified \(R\) independent continuous clocks is uniform, so a union bound gives

\[
\Pr(I_i(t)\ne I_i^{(R)}(t))\le\frac{2}{R!}.
\]

Set \(R_n=\lceil3\log n\rceil\), and \(\widetilde A_n(t)=\sum_i I_i^{(R_n)}(t)\). The coupling bound \(\Pr(A_n(t)\ne\widetilde A_n(t))\le2n/R_n!\to0\) holds for every time \(t\), and their means differ by at most the same quantity. Each truncated indicator depends only on independent clocks inside its own radius-\(R_n\) window, and satisfies \(I_i^{(R_n)}(t)\le\mathbf1\{\xi_i>t\}\).

**3. All factorial moments.** Fix an integer \(r\ge1\) and put \(t=t_n(x)\). In the ordered distinct-index expansion of \(\mathbb E(\widetilde A_n(t))_r\), classify tuples as well separated if every pair of indices differs by more than \(2R_n\). Their truncated indicators are independent. The remaining tuples number at most \(O_r(n^{r-1}R_n)\); for every such tuple, independence of the distinct central exponential clocks and the preceding upper bound give a product expectation at most \(e^{-rt}=(e^{-x}/n)^r\). Thus the total contribution of nearby tuples is \(O_r(R_n/n)=o(1)\). The same estimate applies to products of their marginal probabilities. Since each marginal is at most \(e^{-t}=O(1/n)\), the sum over well-separated tuples differs from \((\mathbb E\widetilde A_n(t))^r\) by \(o(1)\). It follows that

\[
\mathbb E(\widetilde A_n(t_n(x)))_r\longrightarrow\lambda_x^r
\quad\text{for every fixed }r.
\]

These are all factorial moments of \(\operatorname{Poisson}(\lambda_x)\). The Poisson distribution is moment-determinate, so \(\widetilde A_n(t_n(x))\) converges to that law. The coupling proves the asserted convergence for \(A_n\).

**4. Continuous saturation time.** Once all adjacent vacant pairs disappear, no later arrival can succeed; conversely, if some pair is still vacant, the earliest future attempt among available pairs must succeed. Therefore, pathwise, \(\{\tau_n\le t\}=\{A_n(t)=0\}\). The Poisson limit gives

\[
\Pr(\tau_n-\log n\le x)\longrightarrow
\exp(-\lambda_x)=\exp(-e^{-2-x}),
\]

which is the claimed shifted Gumbel law.

**5. Attempts in discrete time.** Superpose the \(n-1\) rate-one Poisson attempt streams and write \(N_n(t)\) for the total number of attempts through time \(t\). This is a Poisson process of rate \(n-1\) and \(T_n=N_n(\tau_n)\) pathwise. By the exact mean above, \(\mathbb EA_n(3\log n)\le(n-1)n^{-3}\to0\), hence \(\Pr(\tau_n>3\log n)\to0\). Doob's \(L^2\) maximal inequality for the compensated Poisson martingale yields, for every \(\epsilon>0\),

\[
\Pr\left\{\sup_{0\le t\le3\log n}|N_n(t)-(n-1)t|>\epsilon n\right\}
\le\frac{12(n-1)\log n}{\epsilon^2n^2}\longrightarrow0.
\]

Consequently \(T_n/n-\tau_n\to0\) in probability, since also \(\tau_n/n\to0\) in probability. Slutsky's lemma transfers the Gumbel law to the trial count.

## Verification

The accompanying standalone `verify_parking.py` uses exact rational arithmetic. It independently enumerates attempted-edge subsets and all their possible chronological orders for paths of \(2\) through \(8\) sites at three rational attempt probabilities; it verifies each exact edge-availability probability and the mean. It also checks the pathwise equivalence between the existence of a vacant adjacent pair and at least one future successful placement, over every full priority permutation and time cut through \(7\) sites. Finally it checks finite alternating-series identities and controlled large-size values of the exact first moment. Running `python3 verify_parking.py` produced `PASS: 6154 exact identities and controlled numerical mean checks`. These finite checks corroborate, but do not replace, the all-order proof above.

## Relationship to prior work

Gerin, *The Page–Rényi parking process* (arXiv:1411.8002; first public version 2014-11-28, published 2015), gives the clock construction and proves only the first-order trial-count result \(T_n/(n\log n)\to1\) in probability. The present finding gives the order-\(n\) fluctuations and their exact Gumbel centering, via a Poisson law for rare available edges at the terminal time scale. Page's original vacancy-distribution study concerns the final number of isolated places; Penrose's random-parking work concerns jamming coverage. Related physics work analyzes mean attempt counts or availability. No priority claim is made for the clock coupling, the final occupancy density, or the first-order trial-count law.

## Limitations

The result applies to fixed-length-two dimers on a one-dimensional open interval with uniform attempt rates, and establishes weak limits rather than explicit finite-\(n\) total-variation rates. It does not treat larger parked objects, nonuniform clocks, cyclic boundaries, or joint fluctuations with final occupancy. Earlier historical treatments of the saturation time may exist; this text does not claim an independently certified literature census. The all-order result is mathematical, not inferred from finite checks.

## References

- L. Gerin, *The Page–Rényi parking process*, arXiv:1411.8002, initially posted 2014-11-28; *Electronic Journal of Combinatorics* 22(4) (2015), P4.4. https://arxiv.org/abs/1411.8002 ; https://doi.org/10.37236/5150
- E. S. Page, *The distribution of vacancies on a line*, *Journal of the Royal Statistical Society, Series B* 21 (1959), 364–374. https://doi.org/10.1111/j.2517-6161.1959.tb00343.x
- M. D. Penrose, *Random parking, sequential adsorption, and the jamming limit*, *Communications in Mathematical Physics* 218 (2001), 153–176. https://doi.org/10.1007/s002200100387
- A. E. Bea, I. M. Irurzun, and E. E. Mola, *Scaling properties in the average number of attempts until saturation in random sequential adsorption processes*, *Physical Review E* 73 (2006), 051604. https://doi.org/10.1103/PhysRevE.73.051604
