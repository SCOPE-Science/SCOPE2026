# Biased Hata maps: exact excursion counts, occupation transform, and critical crossover

## Finding

The random piecewise-affine Hata map has an explicit off-critical residence-time law. Put \(0<p<1\), \(p\ne 1/2\), and \(\delta=|2p-1|\). Starting uniformly in the **disfavored half** of \((0,1)\), let \(N\) be the number of returns to that half after its first exit and let \(S\) count all discrete-time visits to that half, including the initial visit. Then
\[
\Pr(N=k)=(1-\theta)\theta^k\quad(k=0,1,2,\ldots),\qquad
\theta=\frac{1-\delta}{1+3\delta},\qquad
\mathbb E N=\frac{1-\delta}{4\delta},\qquad
\mathbb E S=\frac{1+3\delta}{2\delta^2}.
\]
The law of \(S\) has an exact algebraic probability generating function stated below. There are two distinct near-critical scaling limits:
\[
\delta N\ \Longrightarrow\ \operatorname{Exp}(4),\qquad
\mathbb E\!\left[e^{-s\delta^2 S}\right]\longrightarrow
\frac{2}{1+\sqrt{1+2s}}\quad(s\ge0),\qquad \delta\downarrow0.
\]
The first limit is an exponential distribution of rate \(4\). The second Laplace transform determines a probability law of mean \(1/2\), different from the exponential law. In particular, typical counts of extra excursions and total residence time occur on distinct inverse-bias and inverse-bias-squared scales. For every initial distribution absolutely continuous with respect to Lebesgue measure (and independent of future map choices), the trajectory tends almost surely to the endpoint favored by the bias, with logarithmic distance-decay exponent \(\delta\).

## Assumptions and scope

For \(x\in(0,1)\) away from dyadic boundary points, define
\[
\tau_0(x)=\begin{cases}x/2,&x<1/2,\\ 2x-1,&x>1/2,\end{cases}
\quad
\tau_1(x)=\begin{cases}2x,&x<1/2,\\(x+1)/2,&x>1/2.\end{cases}
\]
At every nonnegative integer time, apply \(\tau_0\) with probability \(p\) and \(\tau_1\) with probability \(1-p\), independently of previous choices and of the initial state. The disfavored half is \((1/2,1)\) when \(p>1/2\), and \((0,1/2)\) when \(p<1/2\). The initial point for the distributional formulas is uniform on this half. Define the first exit time \(E=\inf\{n\ge1:X_n\notin H\}\) and
\[
N=\#\{n\ge E+1:X_{n-1}\notin H,\ X_n\in H\},\qquad
S=\sum_{n\ge0}\mathbf1_H(X_n).
\]
Each return is one crossing from the favored half back into \(H\); thus \(N\) counts the complete extra disfavored sojourns. The formulas and assertions hold under the annealed law of initial point and independent random map choices. Dyadic endpoints form a null exceptional set and do not affect the stated results.

The exact transform is most simply written with \(P=\max(p,1-p)=(1+\delta)/2\), \(Q=1-P=(1-\delta)/2\), \(z\in(0,1]\),
\[
\begin{aligned}
g(z)&=\frac{1-\sqrt{1-4PQz^2}}{2Qz},\\
b(z)&=\frac{Pz}{1-Qzg(z)},\\
F(z)&=\frac{b(z)}{2-g(z)},\\
\theta&=\frac{Q}{3P-1}.
\end{aligned}
\]
Then
\[
\boxed{\mathbb E[z^S]=\frac{(1-\theta)F(z)}{1-\theta F(z)}.}
\]
At \(z=0\), this is defined by continuous extension, equal to zero. Neither this identity nor the near-critical limit is claimed for a nonuniform initial distribution. The endpoint-convergence assertion does extend to arbitrary absolutely continuous initial distributions.

## Proof

**1. Exact dyadic Markov reduction.** By reflection \(x\mapsto 1-x\), the case \(p<1/2\) becomes the case \(P>1/2\) with the maps interchanged. Hence assume \(p=P>Q=1-p\) and let \(H=(1/2,1)\). Introduce cells
\[
L_j=(2^{-j-2},2^{-j-1}),\qquad
R_j=(1-2^{-j-1},1-2^{-j-2}),\qquad j\ge0.
\]
Under the piecewise-affine maps, uniform conditional measure on an individual cell maps to uniform measure on the target cell, except when the image is an entire opposite half. In that case the new cell index has the geometric distribution \(w_j=2^{-j-1}\), and the conditional distribution inside the new cell is again uniform. Consequently, for uniform initial measure on \(H\), the cell labels form an exact Markov chain, with transitions
\[
\begin{array}{c|cc}
 &\tau_0\ (P)&\tau_1\ (Q)\\ \hline
L_j\ (j\ge1)&L_{j+1}&L_{j-1}\\
L_0&L_1&R_J\\
R_j\ (j\ge1)&R_{j-1}&R_{j+1}\\
R_0&L_J&R_1
\end{array}
\qquad \Pr(J=j)=2^{-j-1}.
\]
These transitions follow directly by applying the two affine formulas to cell endpoints. At every cross-half step the landing index \(J\) has a fresh geometric law, independent of past cell labels; this independence also follows from conditional uniformity. The initial cell in the uniform right half has exactly the same geometric law.

**2. Return probability and geometric count.** Write \(r=Q/P<1\). While the chain stays on the left, its depth index moves up with probability \(P\) and down with probability \(Q\). Gambler's-ruin first-passage probabilities give probability \(r^j\) of hitting \(L_0\) from \(L_j\). At \(L_0\), eventual crossing to the right has probability \(h_0\) satisfying \(h_0=Q+P r h_0\), hence \(h_0=r\). It follows that
\[
\Pr(\text{eventually revisit }H\mid L_j)=r^{j+1}.
\]
A fresh left excursion starts at geometric index \(J\), so its success probability is
\[
\theta=\sum_{j\ge0}2^{-j-1}r^{j+1}
=\frac{r}{2-r}=\frac{Q}{3P-1}=\frac{1-\delta}{1+3\delta}.
\]
Every right excursion terminates almost surely because its index drifts toward \(R_0\) with drift \(P-Q=\delta>0\), and from \(R_0\) it has probability \(P>0\) of exit. After each right-to-left crossing, the future right-return event has probability \(\theta\) independently of previous excursions. Therefore \(N\) is geometric on \(\{0,1,\dots\}\) with parameter \(1-\theta\), and its mean has the stated value. As \(\theta=1-4\delta+O(\delta^2)\), the geometric Laplace transform proves \(\delta N\Rightarrow\operatorname{Exp}(4)\).

**3. Exact occupation transform.** Let \(g(z)\) be the generating function of the time for the right-cell index to fall one level when above zero. Its first-step decomposition is
\[
g(z)=z\big(P+Q g(z)^2\big).
\]
The root with \(g(0)=0\) is the displayed square-root expression, with \(g(1)=1\). Let \(b(z)\) generate the number of time indices spent in \(R\) starting at \(R_0\) until the first exit to \(L\). A step from \(R_0\) exits with probability \(P\), or moves to \(R_1\) with probability \(Q\) and then returns to \(R_0\). Thus
\[
b(z)=Pz+Qzg(z)b(z)=\frac{Pz}{1-Qzg(z)}.
\]
For an initial right depth \(j\), the whole right-sojourn generating function is \(g(z)^j b(z)\). Averaging over the geometric starting depth gives
\[
F(z)=\sum_{j\ge0}2^{-j-1}g(z)^j b(z)=\frac{b(z)}{2-g(z)}.
\]
Successive complete right-sojourn lengths are independent and identically distributed, since their starting depths are freshly geometric. The number of such right sojourns is \(N+1\), independent of their lengths: right-to-left exit creates a uniform left half and the ensuing yes/no return event depends only on the future left path. Summing the geometric series gives
\[
\mathbb E[z^S]=\sum_{k\ge0}(1-\theta)\theta^k F(z)^{k+1}
=\frac{(1-\theta)F(z)}{1-\theta F(z)}.
\]
The expected number of visits in one right episode begun at depth \(j\) is \((j+1)/\delta\), because its right-index drift is \(-\delta\) and every return of the reflected walk to zero has exit probability \(P\). More directly, differentiation of \(g\) and \(b\) at one gives \(g'(1)=1/\delta\) and \(b'(1)=1/\delta\). Since \(\mathbb E J=1\), \(F'(1)=2/\delta\); hence
\[
\mathbb E S=\frac{F'(1)}{1-\theta}
=\frac{1+3\delta}{2\delta^2}.
\]

**4. Critical crossover.** Set \(P=(1+\delta)/2\), \(Q=(1-\delta)/2\), and \(z=e^{-s\delta^2}\) for fixed \(s\ge0\). Direct expansion of the analytic expressions (with nonnegative square root) yields, as \(\delta\downarrow0\),
\[
\begin{aligned}
g(z)&=1-\delta\big(\sqrt{1+2s}-1\big)+O_s(\delta^2),\\
F(z)&=1-2\delta\big(\sqrt{1+2s}-1\big)+O_s(\delta^2),\\
1-\theta&=4\delta+O(\delta^2).
\end{aligned}
\]
Inserting these into the exact pgf, including \(s=0\) by normalization, gives \(2/(1+\sqrt{1+2s})\). This function is a Laplace transform: it arises as the pointwise limit of Laplace transforms of nonnegative random variables and is continuous at zero with value one. The Laplace continuity theorem gives convergence in distribution, and differentiation at \(s=0\) gives its mean \(1/2\). These are two distinct scalings: the count \(N\) grows on order \(\delta^{-1}\), while the total occupation \(S\) grows on order \(\delta^{-2}\).

**5. Almost-sure endpoint selection.** Every right episode ends almost surely. After an exit into the left side, the probability of no future return to the right is \(1-\theta>0\), independently at each renewed left excursion. Thus there are a.s. finitely many crossings; eventually the chain is in the left half forever. Its depth index then tends to infinity and obeys \(J_n/n\to P-Q=\delta\) by the strong law for the Bernoulli increments after the last crossing. On \(L_j\), \(2^{-j-2}<X_n<2^{-j-1}\), so \(-\log_2 X_n/n\to\delta\), which entails \(X_n\to0\). The reflected case gives \(-\log_2(1-X_n)/n\to\delta\) and \(X_n\to1\) when \(p<1/2\). The joint law for uniform-half initial states assigns probability one to this event; absolute continuity of the initial distribution transfers it to every Lebesgue-absolutely-continuous initial law by null-set domination.

## Verification

Run `python verify.py` with Python and `sympy`. The standalone program checks the exact dyadic-cell branch images, algebraic formulas for return probabilities and both expectations, seven Taylor coefficients of the occupation generating function at one rational parameter, normalization and derivative at one, numerical near-critical Laplace values, and seeded independent stochastic-cell simulations and direct-interval-map trajectory comparisons. It completed **95 checks** without failure. The experiments are finite corroborations; the exact-law and infinite-time conclusions follow from the proof above, not from sampling or enumeration.

## Relationship to prior work

Hata and Yano [1] introduced the present two-map dyadic partition, derived its unbiased transition matrix, and proved arcsine and Darling–Kac laws for selection probability \(p=1/2\) (Theorem 1.1 and their Section 3). The present result instead treats every fixed \(p\ne1/2\) and determines the total **number of later cross-half excursions**, the complete **occupation generating function**, exact means, endpoint selection, and two distinct near-critical distributions. The earlier recurrent law does not itself determine these off-critical quantities.

Nakamura, Nakano, Toyokawa and Yano [2] generalized the critical random-map arcsine mechanism using a geometric deformation of the maps and a core condition, again under equal map selection. That map-deformation parameter is different from the random selection imbalance \(\delta=|2p-1|\) here. General biased-random-walk hitting-time identities are ingredients in the proof, not prior statements of the dyadic-map result. Published results on the Pelikan map [3] concern doubling-versus-halving maps with a different branch structure and do not directly imply the Hata-map two-half renewal law. The comparison is statement-based; unindexed equivalent calculations remain possible.

## Limitations

The occupation pgf and geometric excursion law assume an initially **uniform disfavored half** and independent identically distributed map choices. They are annealed, not quenched, statements. The endpoint selection and logarithmic contraction exponent hold for arbitrary absolutely continuous initial laws; no uniform-in-initial-point deterministic assertion is made. The result does not characterize the full finite-horizon occupation process, its quenched distributions, or the selection-balanced critical dynamics anew. The critical limiting Laplace law is specified explicitly by its transform rather than by a density. Possible unindexed renewal calculations for this particular Hata map remain an originality limitation.

## References

[1] G. Hata and K. Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, first publicly posted August 3, 2021, arXiv:2108.01332v1, https://arxiv.org/abs/2108.01332 . See equations (1.10), (1.13), Theorem 1.1 and Section 3, especially the transition matrix (3.5).

[2] F. Nakamura, Y. Nakano, H. Toyokawa and K. Yano, *Arcsine law for random dynamics with a core*, first posted June 1, 2022, arXiv:2206.00226v1, https://arxiv.org/abs/2206.00226 . See introduction, generalized Hata–Yano family, and main arcsine result.

[3] J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, *Transition to anomalous dynamics in a simple random map*, first posted August 18, 2023, arXiv:2308.09269v1, https://arxiv.org/abs/2308.09269 . Different (Pelikan) random interval map.
