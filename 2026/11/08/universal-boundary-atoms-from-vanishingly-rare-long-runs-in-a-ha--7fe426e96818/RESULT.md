# Universal boundary atoms from vanishingly rare long runs in a harmonic active particle

## Finding

**Theorem (rare-long-run stationary limit).** Let \(\kappa,v>0\), let \(G\) be any probability law on \((0,\infty)\) of finite mean \(\nu>0\), and prescribe \(\mu>\nu\). For every \(L>\max\{\mu,\nu\}\), independently choose each run duration from the law
\[
G_L=(1-p_L)G+p_L\delta_L,\qquad p_L=\frac{\mu-\nu}{L-\nu}.
\]
Let the propulsion sign \(\sigma_t\in\{-1,+1\}\) reverse at every renewal and let the confined position evolve as \(\dot X_t=-\kappa X_t+v\sigma_t\). Denote by \(\pi_G\) and \(\pi_L\) its equilibrium-time stationary position laws under \(G\) and \(G_L\), respectively, and put \(V=v/\kappa\). Then
\[
\boxed{\ \pi_L\Rightarrow \frac{\nu}{\mu}\pi_G+\frac{\mu-\nu}{2\mu}(\delta_{-V}+\delta_V)\ },\qquad L\to\infty.
\]
In fact, for the Wasserstein distance with cost \(|x-y|\),
\[
\boxed{\ W_1\!\left(\pi_L,\frac{\nu}{\mu}\pi_G+\frac{\mu-\nu}{2\mu}(\delta_{-V}+\delta_V)\right)
\le \frac{Vp_L}{\mu}\left(2\nu+\frac4\kappa\right).\ }
\]
The waiting-time laws satisfy \(G_L\Rightarrow G\) while every \(G_L\) has mean \(\mu\), yet the stationary position distributions do **not** converge to \(\pi_G\). The two limiting boundary atoms each have exactly the mass \((\mu-\nu)/(2\mu)\), even though \(\pi_G\{\pm V\}=0\).

**Concrete fluctuation sign reversal.** In units \(\kappa=v=1\), take \(G=\delta_{9/10}\), \(\mu=1\), and therefore \(p_L=(1/10)/(L-9/10)\). Put \(a=\tanh(9/20)\). The limiting second moment, fourth moment and fourth cumulant are
\[
M_2=1-2a,\qquad M_4=1-2a-\frac23a^3,\qquad
\mathcal K_4=-2+10a-12a^2-\frac23a^3>0.0329.
\]
For every \(L\ge300\), the finite-\(L\) stationary law already has strictly **positive** fourth cumulant. In contrast, for exponential switching of mean \(1\), the fourth cumulant equals \(-2/15\), so a rare long-run component reverses the sign of stationary non-Gaussianity while preserving the mean waiting time.

## Assumptions and scope

Run intervals are strictly positive and independent, alternating the propulsion sign deterministically. No positional thermal noise is added. \(G\) may be discrete, continuous, heavy tailed, or unbounded, subject only to \(0<\mathbb ET=\nu<\infty\); the introduced long-run atom is at the deterministic duration \(L\). The stationary law means observation at equilibrium renewal time, not sampling immediately after a flip. The statement holds for fixed \(\kappa,v,G,\nu,\mu\) as \(L\to\infty\); it is not a simultaneous weak-trap or vanishing-mean limit.

The physical support is \([-V,V]\). All stationary even moments exist because the position is bounded. For deterministic \(G\), the equilibrium phase is uniform over the underlying periodic orbit; an arbitrary nonstationary phase convention is excluded.

## Proof

**1. Embedded contractive chain.** At a flipping instant let \(Z=\sigma X/V\in[-1,1]\), where \(\sigma\) is the *new* propulsion sign. A run of length \(T\) ends at \(X_T/V=\sigma[1+(Z-1)e^{-\kappa T}]\). Since the new sign is \(-\sigma\), the next signed entry position is
\[
Z'=F_A(Z):=A-1-AZ,\qquad A=e^{-\kappa T}\in(0,1).
\]
For every strictly positive waiting-time law the iterated random affine maps admit a unique invariant distribution, obtained by coupling from the infinite past: products of Lipschitz factors tend to zero because \(\mathbb E A<1\). All coordinates remain in \([-1,1]\). Choose an independent fair initial sign for the stationary symmetric extension.

**2. Coupling at the switching instants.** Set \(a_G=\mathbb E_G[e^{-\kappa T}]<1\). Couple the independent driving times for \(G_L\) and \(G\) at each event: with probability \(1-p_L\) use the same \(G\)-distributed time, and with probability \(p_L\) use \(L\) versus an independent \(G\)-time. Their exponential factors \(A_L,A_G\) satisfy \(\mathbb E|A_L-A_G|\le p_L\), and \(\mathbb EA_L\le(1-p_L)a_G+p_L\). For the coupled stationary signed entry positions \(Z_L,Z_G\), independence of the next duration and entry positions and the inequality
\[
|F_A(z)-F_B(w)|\le A|z-w|+2|A-B|\quad(z,w\in[-1,1])
\]
give
\[
d:=\mathbb E|Z_L-Z_G|\le\mathbb EA_L\,d+2p_L,
\qquad d\le\frac{2p_L}{(1-p_L)(1-a_G)}.
\]

**3. Time-stationary renewal reward.** For any bounded measurable \(f\), the stationary position expectation is exactly
\[
\pi_H(f)=\frac1{\mathbb E_H T}\mathbb E\left[\int_0^T
f\bigl(\sigma V[1+(Z_H-1)e^{-\kappa s}]\bigr)\,ds\right],
\]
where \(H\in\{G,G_L\}\), the fair sign \(\sigma\) is independent of the signed entry \(Z_H\), and the current duration \(T\) is independent of both. This is the equilibrium occupation identity, including size bias of long intervals, not the unweighted jump-epoch law.

**4. A quantitative weak limit.** In the Kantorovich–Rubinstein formula, take any real \(1\)-Lipschitz \(f\) with \(f(0)=0\); hence \(|f|\le V\) on the support. Split the \(G_L\) reward into ordinary \(G\)-runs and exceptional length-\(L\) runs. Coupling the ordinary runs to \(G\), the difference in their *integrands* contributes at most
\[
\frac{(1-p_L)Vd}{\mu}\mathbb E_G\int_0^T e^{-\kappa s}\,ds
=\frac{(1-p_L)Vd(1-a_G)}{\kappa\mu}\le\frac{2Vp_L}{\kappa\mu}.
\]
The missing fraction of ordinary runs changes their total reward by at most \(p_L\nu V/\mu\). In any exceptional run, the distance to the appropriate propulsion endpoint \(\sigma V\) is at most \(2V e^{-\kappa s}\), so the difference from an atom accumulated over that entire run is at most \(2Vp_L/(\kappa\mu)\). Finally, because \((1-p_L)\nu+p_LL=\mu\), the difference between \(p_LL\) and \(\mu-\nu\) equals \(p_L\nu\); correcting the endpoint weights therefore costs at most \(p_L\nu V/\mu\). Summing all four bounds proves
\[
W_1\le\frac{Vp_L}{\mu}\left(2\nu+\frac4\kappa\right).
\]
As \(p_L\to0\), weak convergence follows. The base stationary position is strictly inside \((-V,V)\) almost surely: its past-filter representation \(X_0= v\int_0^\infty e^{-\kappa s}\sigma_{-s}\,ds\) has positive-length intervals of both propulsion signs almost surely, so its absolute magnitude is strictly below \(V\). Thus the new atoms show genuine discontinuity under mere weak convergence of waiting laws.

**5. The explicit fourth-cumulant witness.** For a deterministic run duration \(t>0\) and \(\kappa=v=1\), the stationary orbit reaches \(\pm a_t\) with \(a_t=\tanh(t/2)\). Its normalized position density is
\[
q_t(x)=\frac{\mathbf1_{\{|x|<a_t\}}}{t(1-x^2)}.
\]
Integration gives \(\mathbb E_{q_t}X^2=1-2a_t/t\) and \(\mathbb E_{q_t}X^4=1-(2/t)(a_t+a_t^3/3)\). Under the theorem with \(t=9/10\) and \(\mu=1\), this density receives mass \(9/10\), while the two endpoint atoms have mass \(1/20\) each. Substitution produces the stated \(M_2,M_4,\mathcal K_4\).

The displayed strict numerical bound is rigorously checkable using only rational arithmetic: with \(u=9/10\), let \(s=\sum_{j=0}^{14}u^j/j!\) and \(e=s+u^{15}/(15!(1-u/16))\). Then \(s<e^u<e\), so \(a=(e^u-1)/(e^u+1)\) lies between \((s-1)/(s+1)\) and \((e-1)/(e+1)\). Substituting lower bounds for positive terms and upper bounds for negative terms proves \(\mathcal K_4>329/10000\). Let \(\varepsilon_L=\frac{(1/10)}{L-9/10}(29/5)\) be the bound from step 4. On \([-1,1]\), the observables \(x^2\) and \(x^4\) have Lipschitz constants \(2\) and \(4\). Consequently
\[
|\mathcal K_{4,L}-\mathcal K_4|\le4\varepsilon_L+3\cdot(4\varepsilon_L)=16\varepsilon_L
\le\frac{232}{25}\frac1{L-9/10}<\frac{329}{10000}\quad(L\ge300).
\]
This proves the finite-\(L\) sign. The exponential-waiting comparison follows from the classical confined-telegraph stationary moments \(\mathbb EX^2=1/3\), \(\mathbb EX^4=1/5\), giving \(\mathcal K_4=1/5-3/9=-2/15\).

## Verification

The standalone `verify.py` checks the exact rational exponential interval, strict fourth-cumulant lower bound, the finite-\(L\) Wasserstein-derived sign inequality, the closed deterministic-cycle moment integrals, and an independent invariant-affine-moment recursion for several finite choices of \(L\). Execute with `python verify.py` from the extracted package. The recurrence is a finite diagnostic for the worked example; the general theorem is proved in steps 1–4 rather than inferred from numerics.

## Relationship to prior work

Farago and Smith (2024) formulate general non-Markovian tumbling in a confining potential and derive position-dependent effective rates and a numerical stationary-distribution method; their worked clocks are exponential, semi-Gaussian and half-\(t\). The present result instead analyzes a singular fixed-mean family of atomic waiting laws, quantifies its stationary weak limit, and finds a positive fourth-cumulant regime. Sun, Ye and Podgornik (first publicly circulated in September 2024) develop exact moments for a distinct Markov model with finite-duration zero-propulsion tumble phases; their rate model does not supply this rare-long-run renewal limit. The stationary-excess/renewal-reward principle and exponential-run telegraph stationary law are classical ingredients; novelty is not attributed to them.

## Limitations

The atom law is a limit of stationary distributions, not a claim that finite \(L\) has atoms at \(\pm V\). Convergence is in Wasserstein-\(1\) on the bounded physical support, not in total variation; the limit is singular with endpoint atoms. Neither a nonstationary synchronized start nor a joint limit in \(L\), trap stiffness and mean is covered. The theorem is conditioned on the alternating-sign model, not on arbitrary reorientation rules or thermal noise. Publication-priority uncertainty from unindexed general renewal-limit results remains.

## References

1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576 (first public 2024-01-03), https://arxiv.org/abs/2401.01576 .
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578 (first public 2024-09-01), https://arxiv.org/abs/2409.00578 .
3. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. 063203 (2021), https://doi.org/10.1088/1742-5468/ac014d .
4. W. Whitt, *The renewal-process stationary-excess operator*, Journal of Applied Probability (online bibliographic record), https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/renewalprocess-stationaryexcess-operator/8BECC3AEE18F7B18AFD46CFFDDB4725E .
