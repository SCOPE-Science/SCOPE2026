# Four-site Laplace dominance and a sharp five-site obstruction for cyclic resetting destinations

## Finding

For target search restarted at exponential times, compare two choices of restart site: (i) independently redraw one of \(m\) modes uniformly before every new attempt, and (ii) visit the same modes in a deterministic cyclic order, with a single uniformly random initial phase. **For any first-passage laws, cyclic sampling dominates independent sampling in completion-time Laplace-transform order for \(m\le4\). Four is sharp**: five modes already permit the opposite strict inequality, even for Brownian motion to a point target.

Precisely, if \(T_{\mathrm{cyc}}\) and \(T_{\mathrm{iid}}\) are their completion times, then for \(1\le m\le4\), every \(s>0\) satisfies
\[
\mathbb E[e^{-sT_{\mathrm{cyc}}}]\ge \mathbb E[e^{-sT_{\mathrm{iid}}}],\qquad
\mathbb ET_{\mathrm{cyc}}\le \mathbb ET_{\mathrm{iid}}.
\]
Both are strict for \(m=2,3,4\) whenever the free first-passage transforms of the modes at \(r+s\), respectively at \(r\), are not all equal. At \(m=1\) there is equality.

For the half-line Brownian target at zero with \(D=r=1\), five sites at distances \(\log2,\log2,\log2,\frac12\log(4/3),\frac12\log(4/3)\) give the *exact reversal at discount \(s=3\)*:
\[
\mathbb E[e^{-3T_{\mathrm{cyc}}}]-\mathbb E[e^{-3T_{\mathrm{iid}}}]
=-\frac{136832}{120583135}<0.
\]
By continuity the reversal holds for nearby distances, so it does not require repeated locations.

## Assumptions and scope

Fix an integer \(m\ge1\), a reset rate \(r>0\), and modes indexed cyclically by \(i\in\mathbb Z/m\mathbb Z\). Mode \(i\) is a fresh independent search attempt with a free hitting time \(H_i\) in \([0,\infty]\), where \(\infty\) represents possible noncapture. Each attempt is interrupted by a fresh independent exponential clock of rate \(r\). On interruption, time continues and the new attempt starts instantly in its next mode. In the independent protocol each mode, including the first, is uniform and independent. In the cyclic protocol the first mode is uniformly random and each subsequent mode is its cyclic successor. The noise and the clock are refreshed after each interruption. This initial randomization is essential to a fair comparison of identical one-attempt marginals.

Assume \(u_i(r)=\mathbb E[e^{-rH_i}]>0\) for at least one mode, with the convention \(e^{-r\infty}=0\). This ensures finite mean completion time for both protocols. When strict comparisons are stated, all relevant \(u_i\) are not equal. For standard Brownian motion on \((0,\infty)\), with absorption at zero, diffusivity \(D>0\) in generator \(D\partial_{xx}\), and restart at \(x_i>0\),
\[
 u_i(z)=\mathbb E_{x_i}[e^{-zH_i}]=e^{-x_i\sqrt{z/D}}.
\]

## Proof

**1. Exact sequence transform.** Fix \(s>0\). Put \(z=r+s\), \(c=r/z\in(0,1)\), \(u_i=\mathbb E[e^{-zH_i}]\), and \(q_i=1-u_i\in[0,1]\). By independence of the reset clock, the discounted weight of capture during a mode-\(i\) attempt is \(u_i\); the weight of a reset before capture is
\[
 \mathbb E[e^{-sR}\mathbf1_{R<H_i}]
 =r\int_0^\infty e^{-(r+s)t}\Pr(H_i>t)\,dt
 =c(1-u_i)=cq_i.
\]
Define the cyclic block products, for every integer \(k\ge0\), by
\[
 B_k=\frac1m\sum_{i=0}^{m-1}\prod_{j=0}^{k-1}q_{i+j\bmod m},
 \quad B_0=1,\qquad \bar q=\frac1m\sum_{i=0}^{m-1}q_i.
\]
The complete discounted transform is
\[
 F_{\mathrm{cyc}}(s)
 =\sum_{n\ge0}c^n(B_n-B_{n+1})
 =1-(1-c)\sum_{n\ge1}c^{n-1}B_n.
 \tag{1}
\]
For independently drawn modes the corresponding products are \(\bar q^n\), yielding
\[
 F_{\mathrm{iid}}(s)=\frac{1-\bar q}{1-c\bar q},\qquad
 F_{\mathrm{cyc}}(s)-F_{\mathrm{iid}}(s)
 =(1-c)\sum_{n\ge1}c^{n-1}(\bar q^n-B_n).
 \tag{2}
\]
The absolutely convergent series hold because \(0<c<1\). For \(P=\prod_iq_i\) one has the exact periodic factorization \(B_{am+b}=P^aB_b\), for \(a\ge0\) and \(0\le b<m\).

**2. The bound through four modes.** By arithmetic-geometric mean \(P\le\bar q^m\). It is enough to show \(B_b\le\bar q^b\) for each \(1\le b<m\). For \(m=2\), \(B_1=\bar q\) and \(B_2=P\le\bar q^2\). For \(m=3\), the cyclic adjacent-pair products run over all unordered pairs, so \(B_2=e_2/3\le\bar q^2\) by the elementary symmetric-mean inequality; again \(B_3=P\le\bar q^3\). For \(m=4\), writing the indices as \(1,2,3,4\),
\[
 B_2=\frac{(q_1+q_3)(q_2+q_4)}4\le
 \frac{(q_1+q_2+q_3+q_4)^2}{16}=\bar q^2.
\]
Every three-element subset is a cyclic triple, whence \(B_3=e_3/4\le\bar q^3\) by the symmetric-mean inequality; \(B_4=P\le\bar q^4\). For \(m=1\) both protocols coincide. Thus all summands in (2) are nonnegative for \(m\le4\). In the nonconstant case, at least the full-cycle product bound is strict for \(m\ge2\); therefore (2) is strictly positive at every \(s>0\).

**3. Mean ordering.** All \(u_i(r)>0\) for Brownian search, and more generally the hypothesis that at least one is positive makes \(P(r)<1\), ensuring geometric convergence of the periodic renewal series at \(c=1\). Since \(1-c=s/(r+s)\), taking \(s\downarrow0\) in (1) yields
\[
 \mathbb ET_{\mathrm{cyc}}=\frac1r\sum_{n\ge1}B_n(r),\qquad
 \mathbb ET_{\mathrm{iid}}=\frac1r\sum_{n\ge1}\bar q(r)^n.
 \tag{3}
\]
The same product inequalities establish the mean order, strictly when the mode transforms at \(r\) are not all equal.

**4. Sharpness at five modes and beyond.** For \(m=5\), take \(q=(3/4,3/4,3/4,1/4,1/4)\) and \(c=1/4\). The exact cyclic-product summation is
\[
 F_{\mathrm{cyc}}(3)=\frac{2729396}{5242745},\qquad
 F_{\mathrm{iid}}(3)=\frac{12}{23},
\]
and their difference is \(-136832/120583135\). These parameters are physically realized with \(r=D=1\), \(s=3\), and the five positive Brownian reset distances stated above because \(u_i(4)=e^{-2x_i}=1-q_i\).

For every \(m\ge5\), take the boundary vector consisting of three consecutive ones and \(m-3\) zeros. It has \(B_2=2/m>9/m^2=\bar q^2\). This strict inequality persists for some vectors with every component in \((0,1)\). Holding any such vector fixed and choosing sufficiently small \(c>0\), equation (2) gives
\[
 F_{\mathrm{cyc}}-F_{\mathrm{iid}}
 =(1-c)c(\bar q^2-B_2)+O(c^2)<0,
\]
because its \(n=1\) term is zero and the remaining tail is uniformly \(O(c^2)\). Every interior vector is realizable by finite positive Brownian distances \(x_i=-\sqrt{D/(r+s)}\log(1-q_i)\) at a chosen \(s=r(1-c)/c\). Hence the universal four-mode threshold is sharp for the whole Brownian class.

## Verification

A standalone Python 3 checker (`verify_cyclic.py`) recomputes the five-mode witness with `fractions.Fraction`, confirms the elementary reduction of cyclic products to rational finite sums, and checks many independent rational examples with up to four modes. Run `python3 verify_cyclic.py`. Its finite tests do **not** certify the all-parameter inequalities; the complete mathematical proof is above. The witness is an exact rational identity, not a floating-point comparison.

## Relationship to prior work

Julián-Salgado, Dagdug and Boyer study Brownian resetting to two sites with independently occurring site-specific reset clocks. Méndez, Flaquer-Galmés and Campos study positions independently redrawn from a given spatial distribution. Both supply close, relevant first-passage renewal foundations, but neither study cyclically correlated site choices with a single randomized initial phase. Equations (1)–(2) show why independent-location theories alone do not imply the result: cyclic success depends on consecutive block products \(B_k\), while independent resetting depends only on \(\bar q\). In particular, a comparison derived merely from the single-site, equal-marginal or distributed-source formula would miss the five-mode obstruction. The cyclic-versus-independent comparison and its sharp four/five boundary are the assessed statements, not the classical exponential first-hit transform or the elementary symmetric-mean inequalities by themselves.

## Limitations

Laplace-transform ordering is weaker than stochastic ordering of completion times; no pointwise ordering of survival probabilities is asserted. The five-mode example reverses one positive-discount Laplace comparison, not necessarily the mean completion time. Strictness at \(s>0\) requires the corresponding free transforms to differ; if all are identical the two protocols have the same completion law. The proof assumes independent Poisson attempt clocks, deterministic cyclic succession with uniformly randomized starting phase, instantaneous relocation, and regenerative attempts; it is not a result for periodic reset **times**, time-dependent correlated clocks or other arbitrary schedules. The targeted literature comparison does not rule out an unindexed stronger scheduling inequality and is not an independent originality certification.

## References

1. P. Julián-Salgado, L. Dagdug, and D. Boyer, "Diffusion with two resetting points," arXiv:2311.11897 (first public version 2023-11-20). https://arxiv.org/abs/2311.11897
2. V. Méndez, R. Flaquer-Galmés, and D. Campos, "First-passage time of a Brownian searcher with stochastic resetting to random positions," arXiv:2401.01125 (first public version 2024-01-02). https://arxiv.org/abs/2401.01125
