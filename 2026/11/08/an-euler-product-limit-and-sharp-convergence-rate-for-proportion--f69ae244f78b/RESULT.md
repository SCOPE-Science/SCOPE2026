# An Euler-product limit and sharp convergence rate for proportional-choice coupon collection

## Finding

Consider the uniform coupon collector that is offered a uniformly random set of \(d_N\) distinct types from \(N\) types at each independent round and retains exactly one offered type of minimum current multiplicity. Its completion time \(T_N\) is the first round after which every type has been retained at least once. Let
\[
1\le d_N\le N-1,\qquad q_N:=1-\frac{d_N}{N},\qquad S_N:=T_N-N.
\]
For \(0<q<1\), define independent nonnegative-integer geometric variables \(G_m(q)\) by
\[
\Pr(G_m(q)=k)=(1-q^m)q^{mk},\qquad k\in\{0,1,2,\ldots\},\quad m\ge1,
\]
and set \(S(q):=\sum_{m\ge1}G_m(q)\). This sum is almost surely finite. Write \((a;q)_\infty=\prod_{j=0}^\infty(1-aq^j)\) and \((q;q)_k=\prod_{j=1}^k(1-q^j)\), with \((q;q)_0=1\).

**Theorem (proportional-choice regime).** For every \(N\) with \(1\le d_N<N\), there is a coupling satisfying \(S_N\le S(q_N)\) almost surely and
\[
\boxed{d_{\rm TV}\big(\mathcal L(S_N),\mathcal L(S(q_N))\big)
\le\frac{q_N^2}{(N-d_N)(1-q_N)^5}=\frac{q_N}{N(1-q_N)^5}.}
\]
Thus, whenever \(d_N/N\to\theta\in(0,1)\), putting \(q=1-\theta\),
\[
\boxed{\mathcal L(T_N-N)\longrightarrow\mathcal L(S(q))\quad\text{in total variation}.}
\]
The limit has the exact probability-generating function, atom probabilities, mean, and variance
\[
\boxed{\begin{aligned}
\mathbb E z^{S(q)}&=\frac{(q;q)_\infty}{(zq;q)_\infty},&&|z|<q^{-1},\\
\Pr(S(q)=k)&=\frac{(q;q)_\infty q^k}{(q;q)_k}=q^k\prod_{m>k}(1-q^m),&&k\ge0,\\
\mathbb E S(q)&=\sum_{m\ge1}\frac{q^m}{1-q^m},\\
\operatorname{Var}S(q)&=\sum_{m\ge1}\frac{q^m}{(1-q^m)^2}.
\end{aligned}}
\]
All finite positive moments of \(S_N\) converge to those of \(S(q)\) when \(q_N\to q\in(0,1)\).

**Sharpness and first-order correction.** Fix rational \(q\in(0,1)\) and restrict to positive integers \(N\) for which \(d_N=(1-q)N\) is integral. Set
\[
C(q):=\frac{1-q}{2q}\sum_{m\ge1}\frac{m(m-1)q^m}{1-q^m}>0.
\]
Then
\[
\boxed{\Pr(S_N=0)=(q;q)_\infty\left(1+\frac{C(q)}N+o(N^{-1})\right).}
\]
Consequently the displayed \(O(N^{-1})\) total-variation rate has the **optimal order** along every such fixed rational-ratio sequence. The familiar Euler-product and \(q\)-series identities are used as classical identities; the contribution is their appearance in this particular growing-choice coupon model, the strong convergence and the matching finite-size correction.

For example, if \(d_N=N/2\) for even \(N\), the limiting chance of completing the collection in exactly \(N\) rounds is \((1/2;1/2)_\infty\approx0.2887880951\), while \(\mathbb E(T_N-N)\to1.6066951524\) and \(\operatorname{Var}(T_N-N)\to2.7440338888\).

## Assumptions and scope

Each round samples a \(d_N\)-subset without replacement, independently of previous rounds. The collector retains one offered coupon; whenever any offered coupon is unseen, the minimum-multiplicity rule selects an unseen one. Ties may be broken arbitrarily in a measurable way. Each type starts with zero retained copies. One accepted coupon per round entails \(T_N\ge N\). The theorem covers any sequence with \(q_N\to q\in(0,1)\); the explicit quantitative bound holds at every finite \(N\) with \(1\le d_N<N\). The stronger first-order expansion is stated for fixed rational \(q\) on its integral subsequence, not for arbitrary rounding fluctuations in \(d_N\).

## Proof

**1. Exact independent phases.** With precisely \(m\) still unseen types, the next offer fails to contain an unseen type with probability
\[
a_{m,N}=\frac{\binom{N-m}{d_N}}{\binom{N}{d_N}}=
\begin{cases}
\displaystyle\prod_{j=0}^{m-1}\frac{N-d_N-j}{N-j},&m\le N-d_N,\\
0,&m>N-d_N.
\end{cases}
\]
It depends only on \(m\), not on the identities or multiplicities of seen types. As different rounds are independent, the strong Markov property at successive discoveries yields independent geometric failure counts \(F_{m,N}\), with
\[
\Pr(F_{m,N}=k)=(1-a_{m,N})a_{m,N}^{k},\quad k\ge0,\qquad
S_N\stackrel{d}=\sum_{m=1}^N F_{m,N}.
\]
This finite decomposition is already implicit in prior treatments of least-collected coupon offers. It supplies the starting point, not an independent novelty claim.

**2. Uniform coupling and error.** Write \(r_N=N-d_N\) and \(b_{m,N}=q_N^m\). If \(m\le r_N\), then
\[
\frac{a_{m,N}}{b_{m,N}}=\prod_{j=0}^{m-1}\frac{1-j/r_N}{1-j/N}.
\]
Every factor is in \([0,1]\), and its deficit equals
\[
1-\frac{1-j/r_N}{1-j/N}=\frac{j(N-r_N)}{r_N(N-j)}\le\frac{j}{r_N}
\qquad(0\le j\le r_N-1).
\]
Using \(1-\prod_i(1-x_i)\le\sum_i x_i\) gives
\[
0\le q_N^m-a_{m,N}\le\frac{q_N^m m(m-1)}{2r_N}.
\]
For \(m>r_N\) the same inequality holds because \(a_{m,N}=0\) and \(m(m-1)/(2r_N)\ge1\). Extend \(F_{m,N}=0\) for \(m>N\). By inverse-CDF coupling, all \(F_{m,N}\) and \(G_m(q_N)\) can be realized with \(F_{m,N}\le G_m(q_N)\) simultaneously. Since geometric failure means are \(a/(1-a)\),
\[
\begin{aligned}
d_{\rm TV}(\mathcal L(S_N),\mathcal L(S(q_N)))
&\le\Pr\Big(\sum_m F_{m,N}\ne\sum_mG_m(q_N)\Big)\\
&\le\sum_{m\ge1}\mathbb E\big(G_m(q_N)-F_{m,N}\big)\\
&=\sum_{m\ge1}\frac{q_N^m-a_{m,N}}{(1-a_{m,N})(1-q_N^m)}\\
&\le\frac{1}{2r_N(1-q_N)^2}\sum_{m\ge1}m(m-1)q_N^m\\
&=\frac{q_N^2}{r_N(1-q_N)^5}.
\end{aligned}
\]
The sums are finite as expectations because \(q_N<1\). If \(q_N\to q\in(0,1)\), the right side is \(O(N^{-1})\). Meanwhile the coupling of \(S(q_N)\) and \(S(q)\) by their geometric coordinates, dominated on a compact subset of \((0,1)\), gives convergence in total variation. This establishes the claim.

**3. Law and moments of the limit.** The geometric probability-generating functions multiply to
\[
\mathbb E z^{S(q)}=\prod_{m\ge1}\frac{1-q^m}{1-zq^m}.
\]
This analytic product converges whenever \(|z|<q^{-1}\). For a self-contained coefficient calculation, put \(H(z)=\prod_{m\ge1}(1-zq^m)^{-1}=\sum_{k\ge0}h_kz^k\). The identity \((1-zq)H(z)=H(qz)\) yields \(h_0=1\) and \((1-q^k)h_k=qh_{k-1}\), hence \(h_k=q^k/(q;q)_k\). Multiplying by \((q;q)_\infty\) gives the stated atoms. Independent geometric means and variances give the Lambert series displayed above. Uniform geometric tail domination in a neighborhood of \(q\) gives uniform exponential moments for some fixed exponent, proving convergence of every positive finite moment.

**4. Positive first-order no-delay correction.** Fix rational \(q\) with \(r_N=qN\) integral. For each fixed \(m\), the finite product in step 2 has expansion
\[
a_{m,N}=q^m\left[1-\frac{1-q}{qN}\frac{m(m-1)}2+O_m(N^{-2})\right].
\]
The uniform bound from step 2 now reads
\[
0\le N(q^m-a_{m,N})\le\frac{q^m m(m-1)}{2q},
\]
a summable majorant in \(m\). Moreover
\[
\begin{aligned}
\log\frac{\Pr(S_N=0)}{(q;q)_\infty}
&=\sum_{m\ge1}\log\left(1+\frac{q^m-a_{m,N}}{1-q^m}\right),
\end{aligned}
\]
where \(a_{m,N}=0\) for \(m>N\). By the pointwise expansion, \(N\log(1+t_{m,N})\to (1-q)m(m-1)q^m/[2q(1-q^m)]\), with summable domination from \(\log(1+t)\le t\). Dominated convergence therefore gives
\[
N\log\frac{\Pr(S_N=0)}{(q;q)_\infty}\longrightarrow C(q).
\]
The constant is finite and strictly positive (the \(m=2\) summand is positive), yielding the first-order formula. Total variation dominates the difference of probabilities of the event \(\{0\}\), so its lower bound is \((q;q)_\infty C(q)/N+o(N^{-1})\); combined with step 2 this proves sharp order.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to compare geometric phase distributions against independent enumeration of coupon-offer histories at small sizes and checks the key probability inequalities at further sizes. High-precision numerical checks cover the zero-delay correction, \(q\)-product probabilities and moment formulas. It reports **598 passed finite assertions** under Python 3 standard library only. Reproduce with `python verify.py`. These tests check finite identities and numerical consistency; the infinite total-variation limit and sharp asymptotic follow from the preceding proof.

## Relationship to prior work

Doumas and Spektor, *Two Multi--Draw Coupon Collector models with different retention rules* (first posted 2026-07-01), supply the same uniform least-collected model, its finite geometric holding-time representation (equations (74)–(75)), and fixed-offer-size Gumbel asymptotics (Theorem 20). Their fixed-\(d\) regime has completion times of order \(N\log N\), while \(d_N/N\to\theta\in(0,1)\) forces completion in \(N+O_{\Pr}(1)\) rounds. Their asymptotic expansions expand products with constants depending on a fixed \(d\), and do not directly establish the displayed growing-choice Euler law or its sharp \(N^{-1}\) rate. Xu and Tang's earlier *A Generalized Coupon Collector Problem* establishes the model's mean and analyzes fixed offer sizes, not this tight limiting distribution. Berend and Sher study package drawing with **all** offered types retained, a different stopping rule under proportional package sizes, leading to logarithmic rather than near-linear collection time. Classical Euler \(q\)-products and the associated \(q\)-binomial identity are not new here.

## Limitations

The theorem assumes independent uniform offers of distinct types and exactly one retained coupon per round. It concerns the first complete set, not several copies per type. It does not address \(d_N/N\to0\) or \(d_N/N\to1\), where different normalization and crossover phenomena can occur; it does not establish the full second-order probability mass function, only the first-order no-delay mass correction. The literature comparison supports a best-knowledge distinction, not a definitive worldwide historical-priority certificate; the precise Euler limiting family also appears independently in classical \(q\)-probability theory.

## References

1. A. V. Doumas and S. Spektor, *Two Multi--Draw Coupon Collector models with different retention rules*, arXiv:2607.01463v1 (2026-07-01). https://arxiv.org/abs/2607.01463 ; accessible primary full text: https://www.researchgate.net/publication/408403711_Two_Multi--Draw_Coupon_Collector_models_with_different_retention_rules
2. W. Xu and A. K. Tang, *A Generalized Coupon Collector Problem*, Journal of Applied Probability **48** (2011), 1081–1094, https://doi.org/10.1239/jap/1324046020 ; author-hosted full text: https://people.ece.cornell.edu/atang/pub/11/Coupon_collector.pdf
3. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953 (2026), https://arxiv.org/abs/2605.06953
