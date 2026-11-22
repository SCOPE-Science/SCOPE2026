# A critical fire-size and persistent-correlation law for star forest fires

## Finding

Let the continuous-time forest-fire process run on the star \(K_{1,n}\), with one hub and \(n\ge1\) labelled leaves. Each vacant vertex grows a tree at rate \(1\); each occupied vertex is struck by lightning at rate \(\lambda>0\); a strike immediately clears the entire occupied connected component. A **hub fire** is a fire that clears the occupied hub (and therefore every currently occupied leaf). Observe a complete regenerative cycle from one such fire to the next. Write \(F_{n,\lambda}\) for the number of vertices cleared by its terminal hub fire, and \(T_{n,\lambda}\) for the cycle duration.

**Exact finite-size law.** Define formal variables \(H,U,V\), and for \(\lambda\ne1\) let
\[
 A=\frac{\lambda+H}{1+\lambda}U,\qquad
 B=\frac{(1+\lambda H)V-(\lambda+H)U}{1-\lambda^2}.
\]
On polynomials define the linear functional
\[
 \mathcal I_\lambda(H^iU^jV^k)
 =\frac{1}{[1+(1+\lambda)i][\lambda+j+\lambda k]}
 \quad(i,j,k\ge0).
\]
For every \(0\le k\le n\), the complete hub-fire size distribution is the finite rational expression
\[
 \boxed{\mathbb P(F_{n,\lambda}=k+1)
 =\lambda(k+1)\binom nk\mathcal I_\lambda(A^{n-k}B^k).}
\]
At \(\lambda=1\), the right-hand side has its continuous extension, or equivalently the non-singular integral representation given in the proof applies. In particular, all displayed probabilities are strictly positive and sum to one.

**Critical limit.** Fix \(c>0\) and put \(\lambda_n=c/n\). Define
\[
 S_c(t)=e^{-t}+\int_0^t e^{-h}
 \exp\{-c[(t-h)+e^{-t}-e^{-h}]\}\,dh,\qquad t\ge0.
\]
There exists a proper, strictly positive random variable \(T_c\) with survival function \(S_c\), and jointly
\[
 \left(T_{n,\lambda_n},\frac{F_{n,\lambda_n}}{n}\right)
 \ \Longrightarrow\ \left(T_c,Y_c\right),\qquad
 Y_c=1-e^{-T_c}.
\]
The nondegenerate fire-fraction law has density, for \(0<y<1\),
\[
 \boxed{f_c(y)=cy(1-y)^{c-1}e^{-c(1-y)}
 \int_{1-y}^{1}s^{-c}e^{cs}\,ds.}
\]
Its endpoints are \(Y_c\to1\) in probability as \(c\downarrow0\) and \(Y_c\Rightarrow\operatorname{Uniform}(0,1)\) as \(c\to\infty\).

**Stationary correlations.** For each \(n\), take the unique stationary forest-fire distribution, and let \(L_{n,i}\in\{0,1\}\) denote occupancy of leaf \(i\). Put \(M_c=\int_0^\infty S_c(t)\,dt\), and give \(A_c\) density \(S_c(t)/M_c\) on \((0,\infty)\). Then the stationary occupied-leaf fraction converges in distribution to \(R_c=1-e^{-A_c}\), and every fixed pair of distinct leaves satisfies
\[
 \boxed{\lim_{n\to\infty}\operatorname{Cov}(L_{n,1},L_{n,2})
 =\operatorname{Var}(R_c)>0.}
\]
Moreover, \(R_c\to1\) in probability as \(c\downarrow0\), while \(R_c\Rightarrow\operatorname{Uniform}(0,1)\) as \(c\to\infty\); hence its variance tends respectively to \(0\) and \(1/12\). These assertions concern the successive limits \(n\to\infty\) at fixed \(c\), then \(c\to0\) or \(c\to\infty\).

## Assumptions and scope

The graph is the finite labelled star \(K_{1,n}\), not a lattice or a fixed-degree tree. Tree-growth clocks are independent rate-one Poisson processes at each site. Lightning clocks are independent rate-\(\lambda\) Poisson processes at each site, independent of growth. Ignition at a vacant site does nothing. Fire propagation is instantaneous along paths consisting only of occupied vertices, and all burnt vertices return to the vacant state. The observable counts **hub-containing fires only**; while the hub is vacant, single-leaf lightning events occur but are not terminal hub fires. The initial state of each regenerative cycle is empty, exactly as after a hub fire. The stationary assertions refer to the continuous-time process, not the event-sampled distribution. No assertion is made about real wildfires or infinite spatial lattices.

## Proof

**1. Regeneration and the exact marked law.** A hub fire empties all vertices, so successive cycles are independent and identically distributed by the Poisson memoryless property. Let \(H_0\sim\operatorname{Exp}(1)\) be the first hub growth time in a cycle. Before \(H_0=h\), each leaf evolves independently as a two-state chain with vacancy-to-occupation rate \(1\) and occupation-to-vacancy rate \(\lambda\), starting vacant. Its occupation probability at time \(h\) is
\[
 p_h=\frac{1-e^{-(1+\lambda)h}}{1+\lambda}.
\]
Once the hub grows, prior to the terminal hub fire, an occupied leaf stays occupied and a vacant leaf grows at rate \(1\). The hub and each occupied leaf have independent ignition hazards \(\lambda\), so the total terminal-fire hazard is \(\lambda(1+K_u)\), where \(K_u\) is the occupied-leaf count at time \(u\) after hub growth. To compute the probability of surviving this killing hazard, weight each leaf path by \(\exp[-\lambda\int_0^u X_s ds]\).

Conditional on \(H_0=h\), the killed one-leaf endpoint generating polynomial is \(a(h,u)+zb(h,u)\), with
\[
 a(h,u)=(1-p_h)e^{-u},\qquad
 b(h,u)=p_he^{-\lambda u}+(1-p_h)\int_0^u e^{-s}e^{-\lambda(u-s)}\,ds.
\]
The integral has the continuous form \(ue^{-u}\) when \(\lambda=1\). The joint unnormalized probability of surviving through time \(u\) after hub growth and having exactly \(k\) occupied leaves is
\[
 e^{-\lambda u}\binom nk a(h,u)^{n-k}b(h,u)^k.
\]
Multiplying by the terminal rate \(\lambda(k+1)\), integrating \(u\ge0\) and then averaging \(h\) against \(e^{-h}dh\) gives the exact, manifestly nonnegative integral
\[
 \mathbb P(F_{n,\lambda}=k+1)=\lambda(k+1)\binom nk
 \int_0^\infty e^{-h}dh\int_0^\infty e^{-\lambda u}
 a(h,u)^{n-k}b(h,u)^k\,du.
\]
Substitute \(H=e^{-(1+\lambda)h}\), \(U=e^{-u}\), \(V=e^{-\lambda u}\); then \(a=A\), \(b=B\). Integrating each monomial gives exactly \(\mathcal I_\lambda\), proving the finite expression. The total absorption probability is one: after hub growth, a hub ignition clock of positive rate \(\lambda\) alone guarantees eventual termination. Each size has positive probability from appropriate birth and ignition histories.

**2. Critical terminal-fire time.** For \(\lambda_n=c/n\), couple the leaf paths before the terminal hub fire to independent pure-birth paths begun empty. Up to any fixed time \(t\), the expected number of extra individual leaf lightning events while the hub is vacant is at most \(n\lambda_n t=ct\); divided by \(n\) this vanishes. Uniform laws of large numbers for independent pure-birth clocks imply that, on every compact time interval,
\[
 \frac{K_n(s)}n\ \longrightarrow\ u(s):=1-e^{-s}
\]
in probability, uniformly in \(s\), when the potential leaf paths are continued without the global fire. Conditional on the hub growth time \(h\), the probability of no terminal hub fire up to \(t\ge h\), averaged over these potential paths, is
\[
 \mathbb E\exp\left[-\lambda_n(t-h)
 -\lambda_n\int_h^t K_n(s)\,ds\right]
 \longrightarrow\exp\left[-c\int_h^t u(s)\,ds\right].
\]
The last integral equals \((t-h)+e^{-t}-e^{-h}\). Averaging against the independent density \(e^{-h}\) of \(H_0\), and including \(H_0>t\), proves the formula for \(S_c\). It is a proper survival function because \(u(t)\to1\), making the integrated hazard diverge after any finite \(h\). Continuity of the time-changed hazard and uniform convergence of leaf fractions at the killing time prove the asserted joint weak convergence.

Differentiate \(S_c\): the density of \(T_c\) is
\[
 c(1-e^{-t})\int_0^t e^{-h}
 \exp[-c((t-h)+e^{-t}-e^{-h})]dh.
\]
Changing variables \(y=1-e^{-t}\) and \(s=e^{-h}\) yields the displayed \(f_c\). For \(c\downarrow0\), the hazard never exceeds \(c\), so \(T_c-H_0\to\infty\) in probability and \(Y_c\to1\). For \(c\to\infty\), conditional on every \(H_0=h>0\), the post-growth hazard is at least \(c(1-e^{-h})\); thus \(T_c-H_0\to0\) in probability. Since \(1-e^{-H_0}\) is uniform on \((0,1)\), \(Y_c\) has the stated upper endpoint law.

**3. Stationary limiting occupation and correlation.** Renewal-reward theory says that the age since the last hub fire, viewed at a stationary time, has density \(\mathbb P(T_{n,\lambda_n}>t)/\mathbb E T_{n,\lambda_n}\). The cycle durations are uniformly integrable for \(n\) sufficiently large at each fixed \(c>0\). To see this, when \(\lambda_n\le1/2\), the one-leaf killed survival after hub growth, started vacant (the worst case), is bounded by \(e^{-\lambda_n u}/(1-\lambda_n)\). Hence the probability of survival for \(u\) after hub growth is at most
\[
 (1-\lambda_n)^{-n}e^{-n\lambda_n u}
 \le e^{2c}e^{-cu}.
\]
Together with the independent \(\operatorname{Exp}(1)\) hub-growth wait, this gives a uniform integrable exponential-convolution tail. Therefore the stationary age converges to \(A_c\) with the given density and finite normalizer \(M_c\). The same compact-time leaf-fraction law, integrated using this tail bound, gives convergence of the stationary occupied-leaf fraction to \(R_c=1-e^{-A_c}\).

Exchangeability of the leaves gives, for any \(n\ge2\),
\[
 \operatorname{Var}\!\left(\frac1n\sum_{i=1}^nL_{n,i}\right)
 =\frac{\operatorname{Var}(L_{n,1})}{n}
 +\frac{n-1}{n}\operatorname{Cov}(L_{n,1},L_{n,2}).
\]
All fractions lie in \([0,1]\), so convergence in distribution implies convergence of their first two moments. This proves the covariance limit. Since \(S_c(t)>0\) for all finite \(t>0\), \(A_c\) is nondegenerate; the map \(t\mapsto1-e^{-t}\) is strictly increasing, whence \(\operatorname{Var}(R_c)>0\). When \(c\downarrow0\), \(\mathbb E T_c\to\infty\) and the stationary age escapes to infinity, so \(R_c\to1\). When \(c\to\infty\), \(T_c\to H_0\) and the survival functions are dominated by that for \(c=1\), making the stationary age converge to \(\operatorname{Exp}(1)\); hence \(R_c\) tends to the uniform distribution. Its variance is \(1/12\).

## Verification

The standalone `fire_star_verify.py` independently compares the polynomial-integral formula against absorption probabilities of the full hub/count continuous-time Markov chain with transient states \((h,k)\), \(h\in\{0,1\}\), \(0\le k\le n\). It uses exact `fractions.Fraction` rational arithmetic and a separately constructed generator, tests sizes \(1\le n\le5\) at six positive lightning rates other than one, and checks positivity and normalization. Run `python fire_star_verify.py`. The checker is supplementary: finite checks alone do not prove the infinite-graph-size statements. The survival, limit-density and stationary results are established analytically above.

## Relationship to prior work

Drossel and Schwabl (1992) introduced the forest-fire mechanism. Van den Berg and Brouwer (2004) and Stahl (2012) study continuous-time Poisson-growth/Poisson-ignition forest fires on lattices and stationary existence questions. Volkov (2009) treats one-dimensional half-line forests with ignition at the boundary; Graf (2014) studies regular rooted trees of fixed branching and a distinct finite-depth regime. These works supply models and motivation but do not state the present growing-degree star's exact marked law or its critical stationary mixture. The published independent-patch model “Exact catastrophe-rate staircase for the most probable number of occupied habitat patches” treats an *independent, constant-rate, total-reset clock* and a modal classification, not an occupied-hub gate with state-dependent total lightning hazard. Neither its assertion nor its argument implies the present star law without a separate dynamical reduction and analysis.

## Limitations

Hub-containing fires are the sampled events; singleton leaf fires while the hub is vacant are excluded from the fire-size distribution but included in the actual dynamics and proof. The critical parameter \(c\) is the aggregate rate scale \(n\lambda_n\); no universality beyond the exactly specified star graph and Poisson clocks is claimed. The large- and small-\(c\) statements are sequential endpoint limits of the fixed-\(c\) laws. The finite generating formula is rational in \(\lambda\ne1\) and interpreted by continuity at one. The historical-priority searches are bounded; specialized unpublished or unindexed star-model analyses might exist. Originality has not received independent validation.

## References

1. B. Drossel and F. Schwabl, “Self-organized critical forest-fire model,” *Physical Review Letters* 69 (1992), 1629–1632, published 14 September 1992, https://doi.org/10.1103/PhysRevLett.69.1629.
2. J. van den Berg and R. Brouwer, “Self-Organized Forest-Fires near the Critical Time,” first posted 24 December 2004, https://arxiv.org/abs/math/0412488.
3. S. Volkov, “Forest fires on \(\mathbb Z_+\) with ignition only at 0,” *ALEA* 6 (2009), 399–414, https://alea.impa.br/articles/v6/06-18.pdf.
4. A. Stahl, “Existence of a stationary distribution for multi-dimensional infinite volume forest-fire processes,” 25 March 2012, https://arxiv.org/abs/1203.5533.
5. R. Graf, “Self-destructive percolation as a limit of forest-fire models on regular rooted trees,” 1 April 2014, https://arxiv.org/abs/1404.0325.
6. “Exact catastrophe-rate staircase for the most probable number of occupied habitat patches,” 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-catastrophe-rate-staircase-for-the-most-probable-number-of--86c46a755dbf/RESULT.md.
