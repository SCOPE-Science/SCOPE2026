# Unique reversal of stationary circulation under heterogeneous aspiration learning

## Finding

Two agents with unequal public-good contributions, updating by payoff-based aspiration rather than imitation, exhibit a **single, exactly determined reversibility threshold**. In their four-state strategy Markov chain, the stationary probability current around the action square reverses direction exactly once as the common aspiration varies. In particular, this reversal can occur at strictly positive aspirations **within a genuine social dilemma** (public-good multiplier strictly between one and two).

Write the individual contributions as \(a>b>0\), the return multiplier as \(r=2B>0\), the aspiration as \(A\in\mathbb R\), and the Fermi sensitivity as \(\beta>0\). Put
\[
 t=e^{-\beta A},\quad c_a=e^{\beta(B-1)a},\quad c_b=e^{\beta(B-1)b},\quad
 h_a=e^{\beta Ba},\quad h_b=e^{\beta Bb}.
\]
Define two explicit numbers
\[
 P=(h_a-1)(c_b-1)-(h_b-1)(c_a-1),
\]
\[
 Q=c_ac_bh_ah_b\left[\left(1-h_a^{-1}\right)\left(1-c_b^{-1}\right)
 -\left(1-h_b^{-1}\right)\left(1-c_a^{-1}\right)\right].
\]
If \(B\ne1\), then \(PQ<0\) and the **unique reversible aspiration** is
\[
 \boxed{A_*=-\beta^{-1}\log(-P/Q).}
\]
Orient the four-state action square as \((0,0)\to(1,0)\to(1,1)\to(0,1)\to(0,0)\), where \(1\) denotes cooperation. Denote the common signed stationary edge current in this orientation by \(J\). Then
\[
 \boxed{\operatorname{sgn}J=\operatorname{sgn}\bigl((B-1)(A-A_*)\bigr).}
\]
The sign is strict away from \(A_*\). At \(A_*\), detailed balance holds on **every edge** and stationary entropy production is zero; elsewhere the chain is nonreversible with strictly positive entropy production. If \(B=1\), or if the two contributions are equal, the chain is reversible for every aspiration.

Two analytically transparent slices are \(B=\tfrac12\), for which \(A_*=0\), and \(B=2\), for which \(A_*=a+b\), **independently of the sensitivity** \(\beta\). The latter identity follows from an exact four-factor polynomial identity, not asymptotics.

In the proper social-dilemma regime \(r=\tfrac32\), \(a=2\), \(b=1\), \(\beta=4\log2\), one has \(A_*=\tfrac12>0\). Exact stationary currents are
\[
 \begin{array}{c|ccc}
 A&0&\tfrac12&1\\\hline
 J&\tfrac1{2904}&0&-\tfrac8{2055}
 \end{array}.
\]
The corresponding clockwise/anticlockwise transition-product ratios are, respectively, \(33/26\), \(1\), and \(26/33\). Thus the same finite social dilemma exhibits opposite persistent probability currents on either side of a positive aspiration threshold.

## Assumptions and scope

The state is \(s=(s_1,s_2)\in\{0,1\}^2\) with \(s_i=1\) for cooperation, and the heterogeneous linear public-goods payoffs are
\[
 \pi_i(s)=B(as_1+bs_2)-\alpha_i s_i,\qquad (\alpha_1,\alpha_2)=(a,b).
\]
At each discrete step, one of the two agents is sampled uniformly. It flips its own action with probability
\[
 q_i(s)=\frac1{1+\exp\{\beta[\pi_i(s)-A]\}};
\]
otherwise the state stays unchanged. No additional mutation, social imitation, or counterfactual-introspection transition is included. Since \(0<q_i(s)<1\), the four-state Markov chain is irreducible and aperiodic and has a unique strictly positive stationary distribution \(\rho\). We consider every finite \(A\in\mathbb R\) and \(\beta>0\); zero-temperature or infinite-aspiration limits are not included. The required heterogeneous case is \(a>b>0\); exchanging player labels only reverses the chosen cycle orientation.

For any adjacent states \(u,v\), set \(j_{u,v}=\rho(u)T_{u,v}-\rho(v)T_{v,u}\). Conservation on a four-cycle forces all oriented edge currents to equal \(J\). Define the stationary entropy-production rate per update by
\[
 \Sigma=\sum_{\{u,v\}}j_{u,v}\log\frac{\rho(u)T_{u,v}}{\rho(v)T_{v,u}},
\]
where exactly one orientation of each undirected edge is included. This is nonnegative and equals \(J\log R\) for the cycle-product ratio below.

## Proof

**1. Cycle-product test.** Write \(z=e^{-\beta A}=t>0\). Computing the flip rates directly from the payoffs gives the clockwise-to-anticlockwise edge-product ratio
\[
 R(t)=\frac{(1+c_at)(1+h_bt)(1+c_bh_at)}
 {(1+c_ah_bt)(1+h_at)(1+c_bt)}.
\]
(The uniform agent-choice factors cancel.) With \(F\) and \(G\) respectively the numerator and denominator, elementary expansion gives the exact identity
\[
 F(t)-G(t)=t(P+Qt).
\]
Kolmogorov's cycle criterion states that a strictly positive nearest-neighbor chain on the four-cycle is reversible exactly when its clockwise and anticlockwise edge products agree; hence it is reversible precisely when \(P+Qt=0\), unless both coefficients vanish. Moreover, writing the oriented edge fluxes as \(f_i=\rho_iT_{i,i+1}\) and \(g_i=\rho_{i+1}T_{i+1,i}\), stationarity implies \(f_i-g_i=J\) for all \(i\). If \(J>0\), every \(f_i>g_i\), hence \(\prod_i f_i/\prod_i g_i>1\), with converse and the equality case similarly. The stationary probabilities telescope from this ratio, so
\[
 \operatorname{sgn}J=\operatorname{sgn}\bigl(R(t)-1\bigr)
 =\operatorname{sgn}(P+Qt).
\]

**2. Exact coefficient signs.** Let \(u=\beta(B-1)\) and \(v=\beta B\). If \(B\ne1\), define for \(z>0\)
\[
 f(z)=\frac{e^{uz}-1}{e^{vz}-1},\qquad
 g(z)=\frac{1-e^{-uz}}{1-e^{-vz}}.
\]
Since \(v>0\) and \(v-u=\beta>0\), the integral representations
\[
 f(z)=\frac uv\frac{\int_0^z e^{uw}\,dw}{\int_0^z e^{vw}\,dw},\qquad
 g(z)=\frac uv\frac{\int_0^z e^{-uw}\,dw}{\int_0^z e^{-vw}\,dw}
\]
show strict monotonicity. The first integral ratio is the weighted average of \(e^{-\beta w}\) with positive weight \(e^{vw}\), hence strictly **decreases** with its upper endpoint; the second is the weighted average of \(e^{\beta w}\) with positive weight \(e^{-vw}\), hence strictly **increases**. Multiplying by \(u/v\) gives \(f\) decreasing and \(g\) increasing if \(B>1\), with both directions reversed if \(0<B<1\). Factoring the coefficients yields
\[
 P=(h_a-1)(h_b-1)[f(b)-f(a)],
\]
\[
 Q=c_ac_b(h_a-1)(h_b-1)[g(b)-g(a)].
\]
All prefactors are strictly positive, and \(a>b\); therefore \(P>0>Q\) if \(B>1\), and \(P<0<Q\) if \(0<B<1\). In either case \(PQ<0\); the unique positive root is \(t_*=-P/Q\), corresponding to the displayed \(A_*\). Since \(t=e^{-\beta A}\) is strictly decreasing, the sign of \(P+Qt\) is \(\operatorname{sgn}((B-1)(A-A_*))\), giving the current reversal.

**3. Reversible and entropy-production boundaries.** For the exceptional \(B=1\), both \(c_a=c_b=1\), and direct substitution yields \(R(t)=1\). When \(a=b\), the symmetric factors similarly give \(R(t)=1\). These are reversible for every \(A\). In all other cases, \(J\) and \(\log R\) have the same nonzero sign away from \(A_*\), so \(\Sigma=J\log R>0\); at the unique crossing, both vanish. This is the exact finite-state entropy balance, not an assertion about deterministic time-periodic strategies.

**4. Closed-form slices.** At \(B=\tfrac12\), substitute \(c_a=h_a^{-1}\) and \(c_b=h_b^{-1}\) into the expressions for \(P,Q\). Their exact cancellation \(P+Q=0\) implies \(t_*=1\) and \(A_*=0\). At \(B=2\), put \(x=e^{\beta a}\), \(y=e^{\beta b}\), with \(x>y>1\). The polynomial identity is
\[
 \begin{split}
 &(1+xt)(1+y^2t)(1+yx^2t)\\
 &\quad -(1+xy^2t)(1+x^2t)(1+yt)\\
 &=-t(x-1)(x-y)(y-1)(txy-1).
 \end{split}
\]
Thus the sole positive zero is \(t_*=1/(xy)\), giving \(A_*=a+b\) for every \(\beta>0\).

**5. Exact social-dilemma witness.** Take \(B=3/4\), so the public-good multiplier \(2B=3/2\) lies strictly between one and two: unilateral contribution reduces one's own payoff by \(a/4\) or \(b/4\), while increasing the group's combined payoff. For \((a,b,\beta)=(2,1,4\log2)\), the five primitive exponentials entering the transition matrix are rational powers of two. Substituting gives \(A_*=1/2\). Solving \(\rho T=\rho\), \(\sum\rho_i=1\), in state order \(00,10,11,01\), gives at the reversible point
\[
 \rho=\left(\tfrac5{16},\tfrac{17}{64},\tfrac9{64},\tfrac9{32}\right),\quad J=0.
\]
At \(A=0\), exact balance gives \(J=1/2904\) and \(R=33/26\); at \(A=1\), it gives \(J=-8/2055\) and \(R=26/33\). These are opposite strict signs for physical, nonnegative aspiration values.

## Verification

Run `python verify_aspiration_cycle.py` using Python 3 and SymPy. The standalone script constructs the full four-state Markov transition matrices directly from payoff and flip definitions; solves the stationary equations with exact rational arithmetic for six witness cases; checks all oriented edge currents, both cycle-product ratios, both exceptional multiplier identities, and the \(B=2\) symbolic factorization. Its additional 18-parameter floating-point cross-check verifies the general coefficient signs and positive unique root, **not** the continuous theorem; the latter is proved analytically by the integral monotonicity argument above. The script requires no network, saved intermediate logs, or external data files.

## Relationship to prior work

Foster, Knight and Krapohl [1] introduce and examine exactly this heterogeneous-contribution public-goods payoff structure and aspiration flip mechanism. Their focus is extrinsic/intrinsic learning and stationary cooperation abundance; the present result instead determines an exact four-state Kolmogorov cycle product, reversible aspiration level, stationary probability-current direction, and entropy-production boundary. It does not claim novelty for the payoff or aspiration update themselves.

Du and coauthors [2] derive detailed balance for a **one-dimensional homogeneous cooperator-count birth–death chain**; that count process has no four-state cycle and does not force reversibility in the **labeled heterogeneous** chain considered here. Zhou and coauthors [3,4] study population-level aspiration robustness and heterogeneous update functions, not this full-strength directed cycle product. Foster, Knight and Krapohl [5] study a different rule, **counterfactual introspection**, with a product-measure stationary law; that property does not apply to payoff-to-aspiration switching. The general cycle criterion and four-state Markov calculations are standard tools, not claimed as inventions.

## Limitations

The theorem is exact for **two labeled agents**, no additional mutation, a common aspiration and common positive sensitivity, and the specified linear shared-benefit payoffs. It does not classify stationary probability currents for three or more agents, mutation-modified updates, unequal sensitivities or aspirations, or nonlinear public-good rewards. Current reversal concerns microscopic circulation; it does not prove monotone changes in mean cooperator abundance or the existence of time-periodic cooperation sample paths. The closed-form threshold \(A_*=a+b\) at \(r=4\) is not itself a social dilemma; the separate \(r=3/2\) witness is within the social-dilemma regime. No independent scientific audit has been performed. An equivalent calculation in unindexed literature cannot be excluded.

## References

[1] H. Foster, V. Knight and S. Krapohl, *The Cooperation Ceiling: Extrinsic Population Dynamics and the Intrinsic Escape*, arXiv:2606.31740v1 (first public 2026-06-30). https://arxiv.org/abs/2606.31740

[2] J. Du, B. Wu, P. M. Altrock and L. Wang, *Aspiration dynamics of multi-player games in finite populations*, Journal of the Royal Society Interface 11 (2014), 20140077. https://doi.org/10.1098/rsif.2014.0077

[3] L. Zhou, B. Wu, V. V. Vasconcelos and L. Wang, *Simple property of heterogeneous aspiration dynamics: Beyond weak selection*, arXiv:1809.01967. https://arxiv.org/abs/1809.01967

[4] L. Zhou, B. Wu, J. Du and L. Wang, *Aspiration dynamics generate robust predictions in heterogeneous populations*, Nature Communications 12 (2021), 3250. https://doi.org/10.1038/s41467-021-23548-4

[5] H. Foster, V. A. Knight and S. Krapohl, *An Exact Cooperation Formula for Introspection Dynamics in the Heterogeneous Public Goods Game*, arXiv:2605.23513 (first public 2026-05-22). https://arxiv.org/abs/2605.23513
