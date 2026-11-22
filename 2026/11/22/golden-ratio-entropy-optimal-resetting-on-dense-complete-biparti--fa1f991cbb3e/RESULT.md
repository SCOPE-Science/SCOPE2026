# Golden-ratio entropy-optimal resetting on dense complete bipartite graphs

## Finding
Consider an observed discrete-time nearest-neighbor walk on the loopless complete bipartite graph \(K_{a,b}\), with a probability \(r\) of resetting at each step to a fixed vertex of its \(a\)-vertex part. Let \(h_{a\mid b}(r)\) be its stationary Shannon entropy rate in nats per observed vertex transition. For every \(a,b\ge1\) and \(0<r<1\), resetting in the smaller part yields strictly more trajectory entropy than resetting in the larger part (when the parts differ):
\[
 a<b\quad\Longrightarrow\quad h_{a\mid b}(r)>h_{b\mid a}(r).
\]
When both part sizes grow proportionally, this preference has a sharp nontrivial optimal scale. Suppose that \(a_n/n\to\alpha>0\) and \(b_n/n\to\beta>0\). Define \(c_{\alpha,\beta}>0\) by the unique solution
\[
 c_{\alpha,\beta}(1+\alpha c_{\alpha,\beta})\sqrt{\alpha\beta}=1.
\]
For **every** choice of entropy-maximizing reset probabilities \(r_n\in\mathop{\rm argmax}_{0\le r\le1}h_{a_n\mid b_n}(r)\),
\[
 nr_n\longrightarrow c_{\alpha,\beta},\qquad
 n\left[\max_r h_{a_n\mid b_n}(r)-\frac12\log(a_nb_n)\right]
 \longrightarrow c_{\alpha,\beta}-\frac{\log(1+\alpha c_{\alpha,\beta})}{2\alpha}>0.
\]
In particular, for the balanced graph \(K_{n,n}\), every maximizing reset probability obeys
\[
 nr_n\longrightarrow\frac{\sqrt5-1}{2},
\]
with optimal entropy gain \(\big[(\sqrt5-1)/2-\tfrac12\log((1+\sqrt5)/2)\big]/n+o(1/n)\). This golden-ratio constant concerns **observed vertex transitions**; resets and ordinary hops producing the same destination are merged.

## Assumptions and scope
The two parts have exactly \(a,b\in\mathbb N\) vertices, with at least one vertex per part. At each step, independently of all prior choices, reset to one specified root in the first part with probability \(r\in[0,1]\), or otherwise jump uniformly to a neighbor. The entropy is that of the stationary vertex sequence, not that of a separately observed reset/hop label. Write \(q=1-r\), \(H_2(r)=-r\log r-q\log q\), and adopt \(0\log0=0\). For \(0<r<1\), the chain is irreducible, aperiodic and has a unique stationary distribution. At \(r=0\), the irreducible chain is periodic but its stationary entropy is unambiguous; at \(r=1\), define the entropy by its constant-root stationary chain. In each case the entropy-rate identity is \(h=-\sum_x\pi(x)\sum_yP(x,y)\log P(x,y)\). All logarithms are natural.

## Proof
**1. The exact stationary law and the collision correction.** Every vertex in the root's part jumps to the opposite part with probability \(q\), whereas every vertex in the opposite part jumps to the root's part with probability one. Consequently the stationary total masses of the root's part and its opposite are
\[
 \pi(A)=\frac1{2-r},\qquad\pi(B)=\frac{q}{2-r}.
\]
A row originating in \(A\) has the root as a destination with probability \(r\), and all \(b\) opposite-part vertices with individual probability \(q/b\). Its entropy is therefore \(H_2(r)+q\log b\). A row originating in \(B\) has destination probabilities \((r+q/a,q/a,\ldots,q/a)\) on the \(a\)-vertex part. Define its deviation from uniformity by
\[
 K_a(r)=\log a+\left(r+\frac qa\right)\log\left(r+\frac qa\right)
 +(a-1)\frac qa\log\frac qa.
\]
The displayed expression is the nonnegative Kullback--Leibler divergence from the uniform distribution on \(A\). For \(0<r<1\), algebra yields the particularly useful form
\[
 K_a(r)=\log q+\left(r+\frac qa\right)\log\left(1+\frac{ar}{q}\right).\tag{1}
\]
It is zero when \(r=0\) and tends to \(\log a\) as \(r\uparrow1\). All rows of \(B\) have entropy \(\log a-K_a(r)\), so
\[
 \boxed{h_{a\mid b}(r)=\frac{H_2(r)+q\log(ab)-qK_a(r)}{2-r}}.\tag{2}
\]
In particular \(h_{a\mid b}(0)=\tfrac12\log(ab)\) and \(h_{a\mid b}(1)=0\). Equation (2), unlike a hidden-action entropy, combines the overlapping reset and ordinary-hop probability at the root.

**2. Exact optimal root-side ordering.** Interchanging the two parts while moving the root from one to the other changes only the divergence term, giving
\[
 h_{a\mid b}(r)-h_{b\mid a}(r)=\frac q{2-r}\,[K_b(r)-K_a(r)].\tag{3}
\]
For a positive real argument \(x\), extend (1) to \(K_x(r)\). Direct differentiation gives
\[
 \frac{\partial K_x(r)}{\partial x}=\frac{xr-q\log(1+xr/q)}{x^2}>0,
 \qquad 0<r<1,\tag{4}
\]
by \(\log(1+u)<u\) for \(u>0\). Thus (3) is strictly positive for \(a<b\), strictly negative for \(a>b\), and zero for \(a=b\). At \(r=0,1\) both root choices have the same entropy. This proves the root-side comparison for every finite graph and reset rate.

**3. An exact gain identity and a global optimizer cutoff.** Set \(L_{a,b}=\tfrac12\log(ab)\), and let \(N_{a,b}(r)=H_2(r)-rL_{a,b}-qK_a(r)\), so that
\[
 h_{a\mid b}(r)-L_{a,b}=\frac{N_{a,b}(r)}{2-r}.\tag{5}
\]
For each fixed finite \(a,b\), \(K_a(r)=O_{a}(r^2)\) as \(r\downarrow0\). Therefore \(N_{a,b}(r)=r\log(1/r)+O_{a,b}(r)>0\) for sufficiently small \(r>0\); a global maximizer exists and is interior. From (1), \(K_a(r)\ge\log q\). Using \(-q\log q\le r\) and \(H_2(r)=-r\log r-q\log q\) gives the universal bound
\[
 \frac{N_{a,b}(r)}r\le 2-\log(r\sqrt{ab}),\qquad 0<r<1.\tag{6}
\]
Every maximizing reset probability has positive gain by the preceding argument; consequently it necessarily satisfies
\[
 0<r\sqrt{ab}<e^2.\tag{7}
\]
This bounds **all**, not just selected, global maximizers without assuming uniqueness.

**4. The proportional dense-bipartite scaling function.** Suppose \(a_n/n\to\alpha\in(0,\infty)\) and \(b_n/n\to\beta\in(0,\infty)\). On each fixed bounded interval of \(c\ge0\), insert \(r=c/n\) into (1)--(5). The uniform expansions, with the convention \(c\log c=0\) at zero, are
\[
 n\{H_2(c/n)-(c/n)L_{a_n,b_n}\}
 \longrightarrow c[1-\log(c\sqrt{\alpha\beta})],
\]
\[
 nK_{a_n}(c/n)\longrightarrow -c+(c+1/\alpha)\log(1+\alpha c).
\]
Both convergences are uniform on compact \(c\)-intervals: the first follows from the uniform continuity of \(c\log c\) on such intervals and the Taylor remainder of \((1-r)\log(1-r)\); the second follows from the uniform convergence of \(a_n/n\) and smoothness of \(\log(1+x)\) on bounded nonnegative intervals. Hence
\[
 n[h_{a_n\mid b_n}(c/n)-L_{a_n,b_n}]
 \longrightarrow F_{\alpha,\beta}(c)
 =\frac12\left[c\{2-\log(c\sqrt{\alpha\beta})\}
 -(c+1/\alpha)\log(1+\alpha c)\right] \tag{8}
\]
uniformly on compact sets, with \(F_{\alpha,\beta}(0)=0\).

**5. Unique asymptotic optimum, all maximizing sequences, and the golden ratio.** For \(c>0\), differentiating (8) yields
\[
 F'_{\alpha,\beta}(c)=-\frac12\log[c\sqrt{\alpha\beta}(1+\alpha c)],
 \qquad F''_{\alpha,\beta}(c)=-\frac1{2c}-\frac\alpha{2(1+\alpha c)}<0.\tag{9}
\]
Thus \(F\) strictly increases from zero, then strictly decreases, with its unique maximizing argument \(c_{\alpha,\beta}\) defined in the Finding. In particular \(F(c_{\alpha,\beta})>0\), and the root equation in (9) reduces the maximum to
\[
 F(c_{\alpha,\beta})=c_{\alpha,\beta}-\frac1{2\alpha}\log(1+\alpha c_{\alpha,\beta})>0.\tag{10}
\]
By (7), the rescaled values \(nr_n\) for all global maximizers belong eventually to a common compact interval, because \(\sqrt{a_nb_n}/n\to\sqrt{\alpha\beta}>0\). Uniform convergence in (8) then implies every subsequential limit of \(nr_n\) maximizes \(F\); uniqueness forces \(nr_n\to c_{\alpha,\beta}\), and (10) gives the maximal entropy-gain limit. For \(\alpha=\beta=1\), the defining equation becomes \(c(1+c)=1\), with positive solution \(c=(\sqrt5-1)/2\). Substitution in (10) gives the balanced golden-ratio gain.

## Verification
Run `python3 verify.py` using Python's standard library. The checker constructs each small biclique's complete observed transition matrix, solves its stationary equations with **exact rational Gaussian elimination**, and computes row entropy directly, independently of (2). It compares the two possible root sides, verifies the divergence identity, and examines the finite-size scaling on several proportional-size families. A successful replay prints `CHECKS_OK 2622`. These tests verify algebra and normalization in finite cases; all quantified inequalities and limits follow from the analytic proof above, not from numerical sampling.

## Relationship to prior work
Wang and Chen, *Entropy rate of random walks on complex networks under stochastic resetting* (2022), develop the entropy-rate framework and find nonmonotone rate dependence on finite networks; their inspected text does not give (3)--(4), nor the simultaneous proportional-size optimizer of (8)--(10). Riascos, Boyer, Herringer and Mateos (2019) give network-reset stationary and first-passage theory but not this trajectory-entropy classification. Burda, Duda, Luck and Waclaw (2008) optimize entropy over a different, broader family of Markov walks constrained by graph edges; it does not directly supply the fixed-root reset parameter optimum.

Related publicly available finite-graph results establish a strict center-versus-leaf entropy ordering and two distinct asymptotic reset exponents **on stars** \(K_{1,m}\); that star regime is not the proportional-size regime \(a_n,b_n\asymp n\). A regular-graph entropy-envelope result concerns fixed-degree large-girth families; balanced bicliques have girth four and increasing degree. A complete-graph entropy-optimum result gives a Lambert-\(W\) scale for cliques, not a bipartite golden-ratio scale. The novelty assessed here is **the complete finite-size root-part ordering together with the all-global-optimizer dense-bipartite limit**, not the generic entropy formula or an already-known star example.

## Limitations
Only a fixed deterministic reset vertex, uniform nearest-neighbor hopping, homogeneous independent per-step reset probability, and stationary **vertex-observed** Shannon entropy are considered. The theorem does not assert finite-size uniqueness of optimal reset probabilities. The limit assumes both parts grow proportionally with strictly positive finite ratios; it does not apply to a fixed-size part such as a star. Entropy of tagged reset events, first-passage performance, and weighted or directed graphs are different observables. Source comparisons do not establish independent scientific validation or exhaustive global publication priority; an implicit statement in wider Markov entropy literature remains possible.

## References
1. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665, first available 2022-08-11; *Physical Review E* **106**, 054137 (2022). https://arxiv.org/abs/2208.05665
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, first available 2019-10-29. https://arxiv.org/abs/1910.13568
3. Z. Burda, J. Duda, J. M. Luck and B. Waclaw, *Localization of maximal entropy random walk*, arXiv:0810.4113, first available 2008-10-22. https://arxiv.org/abs/0810.4113
4. *Distinct optimal-reset exponents at the hub and leaves of a star*, publicly available research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-distinct-optimal-reset-exponents-at-the-hub-and-leaves-of-a-star--6fb1fef030da
5. *Sharp regular-graph entropy envelope for random walks with stochastic resetting*, publicly available research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-regular-graph-entropy-envelope-for-random-walks-with-stoch--4bc2723b4c40
6. *Lambert-\(W\) entropy-optimal resetting on complete graphs*, publicly available research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-lambert-w-entropy-optimal-resetting-on-complete-graphs--86b682727fbd
