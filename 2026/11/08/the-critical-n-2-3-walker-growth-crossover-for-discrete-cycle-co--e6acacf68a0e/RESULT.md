# The critical \(n^{2/3}\) walker-growth crossover for discrete-cycle cover times

## Finding

Consider \(k_n\) independent synchronous simple symmetric nearest-neighbor random walks, all initially at the same vertex of the cycle \(C_n\). Let \(T_n\) be the first integer time when their union of visited vertices equals the whole cycle. Put
\[
L_n=\log k_n,\qquad
b_n=\sqrt{2L_n-\log L_n-\log\pi},\qquad
t_n=\frac{(n-1)^2}{4b_n^2},\qquad
Z_n=2L_n\left(\frac{T_n}{t_n}-1\right).
\]
Here \(k_n\ge2\) is integer and \(L_n\to\infty\); all displayed quantities are considered for sufficiently large \(n\) so that \(b_n>0\).

**Theorem (critical lattice crossover and sharp boundary).** If \(L_n/n^{2/3}\to c\in[0,\infty)\), then
\[
Z_n\ \Longrightarrow\ \frac{16}{3}c^3-G_1-G_2,
\]
where \(G_1,G_2\) are independent standard Gumbel random variables, \(\Pr(G_j\le x)=\exp(-e^{-x})\). Equivalently, at every real \(x\),
\[
\lim_{n\to\infty}\Pr(Z_n\le x)
=1-\int_0^\infty \exp\!\left(-u-\frac{e^{x-16c^3/3}}{u}\right)\,du.
\]
If instead \(n^{2/3}=o(L_n)\) and \(L_n=o(n)\), then \(Z_n\to+\infty\) in probability: the same continuum-centered second-order window ceases to be tight. In either case \(T_n\sim n^2/(8L_n)\) in probability, provided \(L_n=o(n)\).

Thus \(n^{2/3}\) is the exact scale at which the quartic correction to the discrete-walk large-deviation rate becomes visible in the cover-time fluctuation window. The two-Gumbel *shape* is already known in the Brownian setting; the new result is the finite-lattice simultaneous-growth crossover, its coefficient, and the sharp failure of the uncorrected continuum window beyond it.

## Assumptions and scope

A simple random walk on \(C_n\) moves one edge clockwise or anticlockwise with probability \(1/2\) per step. Choices are independent across time and across walks; every walk starts at vertex \(0\). A vertex visited at or before time \(t\) is covered, so time zero covers the starting vertex. There is no random initial positioning, continuous-time clock, resetting, or interaction. The result concerns the joint asymptotic \(n\to\infty\) and \(k_n\to\infty\), including exponentially many walkers. For the second statement \(L_n\) must remain sublinear in \(n\).

Write \(S_i(j)\) for the integer lift of the \(i\)-th walk, initialized at zero, and define
\[
M_t^+=\max_{1\le i\le k_n}\max_{0\le j\le t}S_i(j),\quad
M_t^-=-\min_{1\le i\le k_n}\min_{0\le j\le t}S_i(j).
\]
All paths have unit steps and begin at zero, so the union of integer sites visited by the lifts is precisely the interval \([-M_t^-,M_t^+]\cap\mathbb Z\). Its reduction modulo \(n\) covers the cycle exactly when it has at least \(n\) integers. Hence the exact identity
\[
\{T_n\le t\}=\{M_t^++M_t^-\ge n-1\}.
\tag{1}
\]

## Proof

**1. A lattice moderate-deviation tail.** For one symmetric walk \(S\) of \(t\) steps let \(H_t=\max_{0\le j\le t}S(j)\). For integers \(a\ge1\), the reflection principle yields
\[
q_t(a):=\Pr(H_t\ge a)
=\Pr(S(t)\ge a)+\Pr(S(t)\ge a+1).
\tag{2}
\]
Define the exact Cramér rate
\[
I(v)=\frac{1+v}{2}\log(1+v)+\frac{1-v}{2}\log(1-v),\qquad |v|<1.
\]
If \(t\to\infty\), \(a/\sqrt t\to\infty\), and \(a/t\to0\), Stirling's formula at the smallest parity-admissible endpoint and summing the neighboring binomial masses in their asymptotically geometric tail give, uniformly under those three conditions,
\[
q_t(a)=\frac{\sqrt{2/\pi}}{a/\sqrt t}
\exp[-tI(a/t)](1+o(1)).
\tag{3}
\]
For completeness, if \(s\) is the first integer at least \(a\) with the same parity as \(t\), then
\[
\Pr(S(t)=s)=\sqrt{\frac{2}{\pi t(1-(s/t)^2)}}
\exp[-tI(s/t)](1+o(1)),
\]
and the ratio of successive nonzero masses to the right is \((t-s-2j)/(t+s+2j+2)\) at displacement \(s+2j\). Its initial distance from one is asymptotic to \(2a/t\), whereas the ratio changes negligibly across its effective \(O(t/a)\) terms because \(a^2/t\to\infty\). The resulting geometric multiplier is \(t/(2a)(1+o(1))\). Replacing \(s\) by \(a\) changes the exponent by \(O(a/t)=o(1)\); the two tails in (2) are asymptotically equal. This proves (3) without invoking an unquantified invariance principle.

The analytic rate expansion is
\[
I(v)=\frac{v^2}{2}+\frac{v^4}{12}+O(v^6),\quad v\to0,
\]
so for \(z=a/\sqrt t\),
\[
tI(a/t)=\frac{z^2}{2}+\frac{z^4}{12t}+O\!\left(\frac{z^6}{t^2}\right).
\tag{4}
\]

**2. The critical correction to each extreme.** Fix any \(x,y\in\mathbb R\), take \(t=\lfloor t_n(1+x/(2L_n))\rfloor\), and put \(a=\lceil\sqrt t(b_n+y/b_n)\rceil\). If \(L_n/n^{2/3}\to c<\infty\), then \(t\to\infty\), \(a/\sqrt t\sim b_n\to\infty\), and \(a/t=O(L_n/n)\to0\). Moreover \(z=b_n+y/b_n+o(1/b_n)\), since \(b_n/\sqrt t=O(L_n/n)\to0\). Using (4),
\[
tI(a/t)=\frac{b_n^2}{2}+y+\frac{b_n^6}{3(n-1)^2}+o(1),
\]
because \(b_n^6/(3(n-1)^2)\to\delta=8c^3/3\) and \(z^6/t^2=O(L_n^5/n^4)=o(1)\). The normalization defining \(b_n\) ensures
\[
k_n\frac{\sqrt{2/\pi}}{b_n}e^{-b_n^2/2}\to1.
\]
Consequently, by (3),
\[
k_n q_t(a)\longrightarrow e^{-y-\delta}.
\tag{5}
\]
The same formula holds for the negative minimum by symmetry.

**3. Independence of the two extremes in the limit.** For positive integer levels \(a,d\), the strong Markov property at the first of the two opposite crossings and the exponential maximal inequality \(\Pr(H_t\ge h)\le e^{-h^2/(2t)}\) give
\[
\Pr(H_t\ge a,\ -\min_{j\le t}S(j)\ge d)
\le2\exp\!\left[-\frac{a^2+(a+d)^2}{2t}\right].
\tag{6}
\]
At levels \(a,d=\sqrt t(b_n+O(1/b_n))\), this is at most \(2\exp[-(5+o(1))L_n]\); multiplying by \(k_n=e^{L_n}\) makes it vanish. By (5), inclusion-exclusion, and independence of the walkers, the two normalized global extrema
\[
\left(b_n\left(\frac{M_t^+}{\sqrt t}-b_n\right),
 b_n\left(\frac{M_t^-}{\sqrt t}-b_n\right)\right)
\Longrightarrow(G_1-\delta,G_2-\delta)
\tag{7}
\]
with independent standard Gumbels. The dependence of \(t\) on the fixed \(x\) does not affect the limit.

**4. Inversion to cover time.** The time choice above satisfies
\[
b_n\left(\frac{n-1}{\sqrt t}-2b_n\right)\longrightarrow-x.
\tag{8}
\]
Indeed \(b_n^2/(2L_n)\to1\), and rounding time changes the left-hand side by \(o(1)\). Combining (1), (7), and (8), and using that a sum of independent Gumbels has a continuous distribution,
\[
\Pr\left(Z_n\le x\right)
\longrightarrow\Pr(G_1+G_2-2\delta\ge-x).
\]
This is precisely the first assertion, including its integral CDF: write \(G_j=-\log E_j\) for independent unit-rate exponential variables \(E_j\), so \(-G_1-G_2=\log(E_1E_2)\).

**5. Sharp failure beyond the crossover.** Suppose \(n^{2/3}=o(L_n)\) and \(L_n=o(n)\), and again use \(t=\lfloor t_n(1+x/(2L_n))\rfloor\) for fixed \(x\). With \(a=\lceil(n-1)/2\rceil\), the exact rate in (3) satisfies
\[
tI(a/t)-\frac{a^2}{2t}
\sim\frac{b_n^6}{3(n-1)^2}
\sim\frac{8L_n^3}{3n^2}\longrightarrow\infty.
\]
The discarded higher-order terms are relatively \(O((a/t)^2)=o(1)\), even when the correction diverges. The Gaussian prefactor and definition of \(b_n\) now give \(k_nq_t(a)\to0\). Coverage by time \(t\) requires at least one of the two global extrema to reach \(a\), so by the union bound
\[
\Pr(T_n\le t)\le2k_nq_t(a)\longrightarrow0.
\]
This is \(Z_n\to+\infty\) in probability. Finally the first-order asymptotic follows in both regimes: for subcritical or critical growth, it follows from tightness of \(Z_n\); for supercritical sublinear \(L_n\), the exact-rate tail applied at fixed relative times \((1\pm\varepsilon)n^2/(8L_n)\) gives the corresponding lower and upper probability bounds, as the correction is \(o(L_n)\). For the upper bound, use the independent single-direction maxima of \(k_n\) walkers at level just above half the circumference; their crossing probabilities tend to one by (3), and both sides are reached with probability tending to one by a union bound. Thus \(T_n\sim n^2/(8L_n)\) in probability. \(\square\)

## Verification

The standalone `verify.py` checks the exact reflection identity (2), the exact pathwise coverage criterion by independent exhaustive enumeration of signs and Cartesian products of walks, and an exact finite-time dynamic-programming formula for the cycle-cover CDF. Running `python verify.py` gives `PASS 3242 exact checks`. This is an integer/rational finite consistency check, not a proof of the infinite-size limits. Separately, evaluating the exact binomial upper tail at lattice sizes of a few thousand supports the positive critical shift in (5); asymptotic claims above rely on the displayed analytic estimates.

## Relationship to prior work

Rivera, Sauerwald and Sylvester [1], first public November 16, 2020, give cycle multiwalk cover-time bounds on finite graphs in their §5.1, with the worst-start result stated for at most \(n\) walkers and only at order-of-growth precision. The present critical regime has \(k_n=\exp(\Theta(n^{2/3}))\), well outside that parameter range.

Majumdar, Sabhapandit and Schehr [2] established the periodic **Brownian** cover-time distribution for many walks, including its non-Gumbel two-extreme shape; Kundu, Majumdar and Schehr [3] developed the Brownian span law underlying it. The two-Gumbel shape and the continuum first-order law are therefore *not* claimed new. Their Brownian scaling does not provide the joint discrete limits, the \(n^{2/3}\) crossover, the \(16c^3/3\) lattice correction or the sharp beyond-critical failure; ordinary fixed-walker invariance principles cannot control these exponentially rare crossing probabilities. Kim and Lawley [4] study a different many-searcher limit on a fixed discrete network, and Alon et al. [5] provide order-scale cycle bounds.

## Limitations

The formula is specific to unit-step, unbiased, independent, synchronously updated walks from a common starting point on a simple cycle. The limiting second-order law is proved when \(\log k_n=O(n^{2/3})\), and sharp loss of tightness of that centering is proved for \(n^{2/3}\ll\log k_n\ll n\). This does not identify a replacement centered law for every larger walker count, does not give moment convergence or a full uniform approximation in \(x\), and does not address biased or continuous-time walks.

## References

1. N. Rivera, T. Sauerwald and J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, arXiv:2011.07893, first public November 16, 2020. https://arxiv.org/abs/2011.07893
2. S. N. Majumdar, S. Sabhapandit and G. Schehr, *Exact distributions of cover times for \(N\) independent random walkers in one dimension*, arXiv:1609.06325, first public September 20, 2016, particularly the periodic case in §V and Eqs. (20)–(26). https://arxiv.org/abs/1609.06325
3. A. Kundu, S. N. Majumdar and G. Schehr, *Exact distributions of the number of distinct and common sites visited by \(N\) independent random walkers*, arXiv:1302.2452, 2013. https://arxiv.org/abs/1302.2452
4. H. Kim and S. D. Lawley, *Cover times of many random walkers on a discrete network*, arXiv:2310.07905, first public October 11, 2023. https://arxiv.org/abs/2310.07905
5. N. Alon, C. Avin, M. Koucký, G. Kozma, Z. Lotker and M. Tuttle, *Many Random Walks Are Faster Than One*, arXiv:0705.0467, 2007. https://arxiv.org/abs/0705.0467
