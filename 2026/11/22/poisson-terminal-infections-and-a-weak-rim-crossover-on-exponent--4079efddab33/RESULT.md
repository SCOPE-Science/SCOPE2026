# Poisson terminal infections and a weak-rim crossover on exponential first-passage wheels

## Finding

Let \(W_{n+1}\) be a wheel with hub \(h\) and rim \(v_0,\ldots,v_{n-1}\), \(n\ge5\). Initially only \(h\) is infected; infection is irreversible and crosses each hub--rim edge at rate \(\alpha>0\) and each rim--rim edge at rate \(\beta_n\ge0\), independently and with exponential waiting times. Write \(T_n\) for the first time all rim vertices are infected and \(N_n(t)\) for the number remaining susceptible at time \(t\). Let \(G\) have the standard Gumbel law \(\Pr(G\le x)=\exp(-e^{-x})\).

**Fixed positive rim rate.** For every fixed \(\alpha,\beta>0\), define \(a=\alpha+2\beta\) and
\[
 t_n(x)=\frac{\log n+2\beta/\alpha+x}{a}.
\]
For every fixed real \(x\),
\[
 N_n(t_n(x))\ \Longrightarrow\ \operatorname{Poisson}(e^{-x}),
 \qquad aT_n-\log n-\frac{2\beta}{\alpha}\ \Longrightarrow\ G.
\]

**Weak-rim crossover.** Fix \(\alpha>0\), and let \(\beta_n\ge0\) satisfy \(\beta_n\log n\to c\in[0,\infty)\). Then for every fixed real \(x\),
\[
 N_n\!\left(\frac{\log n+x}{\alpha}\right)
 \Longrightarrow\operatorname{Poisson}\left(e^{-x-2c/\alpha}\right),
\]
and equivalently
\[
 \alpha T_n-\log n+\frac{2c}{\alpha}\ \Longrightarrow\ G.
\]
In particular, a rim rate on the scale \(1/\log n\) already produces a nonzero order-one shift relative to the exact star law \(\Pr(T_n\le t)=(1-e^{-\alpha t})^n\) at \(\beta_n=0\). This is the sharp star-window scale: if instead \(\beta_n\to0\) and \(\beta_n\log n\to\infty\), then \(\alpha T_n-\log n\to-\infty\) in probability.

## Assumptions and scope

The rim is a simple undirected cycle; at every susceptible vertex each infected neighbor transmits at the stated independent exponential rate. Equivalent first-passage realization: give spoke \(hv_j\) an independent \(E_j\sim\operatorname{Exp}(\alpha)\), rim edge \(v_jv_{j+1}\) an independent \(Y_j\sim\operatorname{Exp}(\beta_n)\) (for zero rate, set its weight to infinity), and take the infection time of \(v_i\) to be the shortest weighted-path length from \(h\) to \(v_i\). The exponential memoryless property proves equivalence to the specified Markov SI process. All limits are along integer \(n\to\infty\); convergence is distributional, not an almost-sure statement. The fixed-rate assertion does not require or imply uniformity over all growing rim rates.

## Proof

**1. An exact infinite-rim one-point void probability.** Replace the rim cycle by the integer line, with independent \(\operatorname{Exp}(\alpha)\) seed delays at all integer sites and independent \(\operatorname{Exp}(\beta)\) nearest-neighbor edge weights. Let \(X_0(t)\) indicate that site zero has not been reached by time \(t\). Along either ray, distances from zero to consecutive sites are the arrival times \(S_k\) of a rate-\(\beta\) Poisson process. Conditioned on the edge weights, no seed from that ray can reach zero by \(t\) precisely when its seed delays obey \(E_k>(t-S_k)_+\) for all \(k\ge1\). The Poisson Laplace functional gives the one-ray protection probability
\[
 J_\beta(t)=\mathbb E\exp\left(-\alpha\sum_{k\ge1}(t-S_k)_+\right)
 =\exp\left[-\beta\int_0^t(1-e^{-\alpha(t-s)})\,ds\right]
 =\exp\left[-\beta t+\frac\beta\alpha(1-e^{-\alpha t})\right].
\]
The two rays and the seed at zero are independent. Therefore the infinite-rim survival probability is **exactly**
\[
 p_\infty(t)=e^{-\alpha t}J_\beta(t)^2
 =\exp\left[-(\alpha+2\beta)t+\frac{2\beta}{\alpha}(1-e^{-\alpha t})\right].\tag{1}
\]
This calculation does not assert an exact finite-wheel marginal identity.

**2. Finite-radius coupling.** Let \(R_n=\lceil(\log n)^2\rceil\). For each rim vertex \(i\), define \(X_i^{(R)}(t)\) to be the event that no seed at rim distance at most \(R_n\) can reach \(i\) by following the direct rim arc of at most \(R_n\) edges. If \(4R_n<n\), these events depend only on the independent spoke and rim weights in the \(R_n\)-neighborhood of the target. An infection path omitted by this truncation must traverse at least \(R_n\) consecutive rim edges in one direction by time \(t\), since all seed delays are nonnegative. Hence for any \(i\),
\[
 \Pr\bigl(X_i^{(R)}(t)\ne\mathbf1\{v_i\text{ susceptible at }t\}\bigr)
 \le2\Pr\bigl(\operatorname{Pois}(\beta_n t)\ge R_n\bigr).\tag{2}
\]
Here \(\operatorname{Pois}(0)\) is zero. For each time sequence used in the theorem, \(\beta_n t=O(\log n)\), so the bound in (2), multiplied by any fixed power of \(n\), tends to zero by the Poisson Chernoff bound. Formula (1), with \(\beta=\beta_n\), is consequently an asymptotically exact one-point probability on the finite wheel, with error superpolynomially small:
\[
 \Pr(X_i^{(R)}(t)=1)=p_\infty(t)+o(n^{-K})\quad\text{for every fixed }K>0.\tag{3}
\]

**3. Local pair protection.** For two different rim sites whose cyclic separation is at most \(2R_n\), choose the disjoint outward rays of length \(R_n\) running away from one another around the longer complementary arc. If both truncated survival indicators equal one, both sites' spoke delays exceed \(t\) and neither outward ray can send infection to its endpoint. Write
\[
 J_{\beta,R}(t)=\mathbb E\exp\left(-\alpha\sum_{k=1}^{R}(t-S_k)_+\right).
\]
Independence gives the strict bound
\[
 \Pr\left(X_i^{(R)}(t)=X_j^{(R)}(t)=1\right)
 \le e^{-2\alpha t}J_{\beta_n,R_n}(t)^2.\tag{4}
\]
The right side is at most \(e^{-2\alpha t}[J_{\beta_n}(t)+\varepsilon_n]^2\), where \(\varepsilon_n\le\Pr(\operatorname{Pois}(\beta_n t)\ge R_n)\). Under fixed \(\beta>0\) at \(t=t_n(x)\), it is \(O(n^{-(2\alpha+2\beta)/(\alpha+2\beta)})\). Under \(\beta_n\log n\to c\) at \(t=(\log n+x)/\alpha\), it is \(O(n^{-2})\). The constants may depend on the fixed parameters and \(x\), but not on \(i,j,n\).

**4. Rare surviving sites are Poisson.** Two truncated indicators are independent when their cyclic distance exceeds \(2R_n\). The dependency graph thus has at most \(4R_n\) neighbors per site. Let \(p_n\) be their common success probability. The elementary local-dependence Poisson bound (Arratia--Goldstein--Gordon's Chen--Stein bound) controls total-variation error against \(\operatorname{Pois}(np_n)\) by a constant multiple of
\[
 b_1=n(4R_n+1)p_n^2,\qquad
 b_2=\sum_i\sum_{0<d(i,j)\le 2R_n}\Pr(X_i^{(R)}=X_j^{(R)}=1).
\]
For fixed \(\beta>0\), (1)--(4) give \(b_1=O(R_n/n)\) and \(b_2=O(R_n n^{-\alpha/(\alpha+2\beta)})\); for the weak-rim regime they give \(b_1,b_2=O(R_n/n)\). All errors vanish, as does the truncation error for the entire rim by the union bound.

**5. Evaluate the Poisson means and the completion event.** For fixed \(\beta\), substitute \(t_n(x)\) into (1):
\[
 np_\infty(t_n(x))=\exp\left[-x-\frac{2\beta}{\alpha}e^{-\alpha t_n(x)}\right]\longrightarrow e^{-x}.
\]
For \(\beta_n\log n\to c\), at \(t=(\log n+x)/\alpha\), formula (1) gives
\[
 np_\infty(t)=\exp\left[-x-2\beta_n t+\frac{2\beta_n}{\alpha}(1-e^{-\alpha t})\right]
 \longrightarrow e^{-x-2c/\alpha}.
\]
Finally \(\{T_n\le t\}=\{N_n(t)=0\}\). Evaluating the mass at zero of the limiting Poisson laws proves both completion-time assertions. For sharpness, suppose \(\beta_n\to0\) while \(\beta_n\log n\to\infty\). At any fixed \(K>0\), choose \(t=(\log n-K)/\alpha\). Equation (1) gives \(np_\infty(t)\to0\), and the same truncation argument as (2) applies because \(\beta_n t=o(\log n)\). The union bound gives \(\Pr(T_n>t)\le np_\infty(t)+o(1)\to0\). Since \(K\) is arbitrary, \(\alpha T_n-\log n\to-\infty\) in probability, as claimed. \(\square\)

## Verification

The standalone `verify_wheel.py` uses only the Python standard library. It independently constructs the full finite-state SI Markov generator for wheels with 6, 8 and 10 rim sites, computes the site-zero survival probability by continuous-time Markov uniformization, and compares 12 numerical values at four rate/time combinations to the infinite-line expression (1). All twelve checks pass. They test the model and the one-point coupling, not the infinite-size Poisson theorem. The proof of the theorem is the analytic argument above, including the local-dependence and truncation bounds.

## Relationship to prior work

Bhamidi, van der Hofstad and Hooghiemstra study exponential first-passage weights and hopcounts on random configuration-model graphs; their graph ensemble and typical-vertex statements do not yield deterministic hub-rooted wheel flooding extremes. Renlund analyzes propagation speeds along infinite width-two ladders; it does not yield a terminal-infection law for a cycle of sites all attached to one infected hub. Leskelä and Ngo treat flooding times on sparse random configuration models with bounded empirical high-degree moments; the wheel has a hub of growing degree and the required deterministic geometry is outside that theorem. The published wheel SIS model with recovery studies stationary mean-field quantities, not exact irreversible SI terminal times. The established Poisson approximation theorem is applied rather than claimed as new.

Published research findings on *clique bouquets* involve disjoint peripheral petals (and a different \(\log\log n\) shift), not a single growing peripheral cycle. Published wheel *bond-percolation* connectivity findings concern a static thresholded edge graph; shortest-path sum constraints for exponential passage times are not equivalent to independent-edge openness at a single time. These comparisons do not establish uniqueness, and the prior-art evaluation remains provisional.

## Limitations

Only the specified irreversible SI/independent exponential-passage model, hub initial condition and simple wheel geometry are covered. The results are weak-convergence statements for the number of last susceptible sites and the finishing time. No exact finite-wheel distribution or higher-order asymptotic error constant is claimed. No Gumbel moment convergence, nonexponential edge-weight generality, or uniform assertion over unrestricted rate sequences is proved. The shifted weak-rim Gumbel law requires the finite limit \(\beta_n\log n\to c\); the separate star-window escape assertion assumes \(\beta_n\to0\) and \(\beta_n\log n\to\infty\). Independent scientific validation and definitive historical-priority confirmation remain outstanding.

## References

1. S. Bhamidi, R. van der Hofstad and G. Hooghiemstra, *First passage percolation on random graphs with finite mean degrees*, first public arXiv posting 2009-03-30, https://arxiv.org/abs/0903.5136.
2. H. Renlund, *First-passage percolation on ladder-like graphs with heterogeneous exponential times*, arXiv posting 2011-02-23, https://arxiv.org/abs/1102.4744.
3. L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, arXiv posting 2018-06-25, https://arxiv.org/abs/1806.09568.
4. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen--Stein method*, Ann. Probab. 17 (1989), 9--25, https://doi.org/10.1214/aop/1176991491.
5. L. Jiao, D. Guo and Y. Wang, *SIS Process with Heterogeneous Infection Rates in Wheel Graphs*, Mathematics 13 (2025), 3580, https://doi.org/10.3390/math13223580. This studies a different, recovering epidemic model.
