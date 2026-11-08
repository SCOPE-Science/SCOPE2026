# Mathematical review

## Correctness — PASS

The formal domain is the original Table 1 game with source payoffs \(u_H=v-(v+c)x/2\), \(u_D=v(1-x)/2\), and confidence matrix \(B=\operatorname{diag}(1/2,1/2)\). The source's \([\cdot]_0^1\) truncation reduces to the stated positive-part rule because \(-1\le h\le49/68\), as proved by the nonnegative degree-two Bernstein tensor for \(1+h\) and convexity in opinion fraction. Scalar comparison traps the strategy component in \([1/3,7/10]\). The exact nullcline identity shows only one interior equilibrium; exact Jacobians give two boundary sinks and one hyperbolic saddle. Positive scaling of the opinion component preserves equilibrium indices; the planar index/Poincaré–Bendixson argument rules out cycles and recurrent saddle connections. Convexity and explicit edge identities establish the one-way barrier. The invariant stable-graph equation gives coefficient \(44/103\); substitution checks that graph is on the appropriate clipped branch. The resource log-odds identity gives the limiting continuum. The symbolic verification program has passed; numerical trajectories are only illustrations.

## Originality — PASS on inspected evidence

The initiating preprint Lorits–Gubar (arXiv:2307.04902v1, Section 3 and Figure 1) already exhibits distinct numerical outcomes from initial opinion values 0.45 and 0.7. We do not claim numerical bistability or the classical stable-manifold/index theorems as new. Its accessible full text gives the equations and plot but no theorem on all interior initial states, no exact one-sided half-opinion barrier, no signed \(44/103\) local basin curvature, and no full resource-limit family. Paarporn et al. (arXiv:1803.06737v1, Section IV) use \(\dot o=-\gamma(o-n)\) rather than payoffs-based clipped opinion imitation; their control results do not cover the identified stable graph. Ito–Yamamichi (2024, doi:10.1093/pnasnexus/pgae455) classify directly environment-driven two-variable games, not this triangular three-state opinion–strategy system. Targeted published-research semantic comparisons and own recoverable claims found no theorem implying all four linked conclusions. This is best-knowledge originality, not a proof of absence in the full literature.

## Value — PASS

The source shows different outcomes for two sampled initial opinions but does not tell which mixed initial strategies select which outcome. Proving a sharp one-sided barrier and calculating that the basin boundary bends strictly above the naive half-opinion threshold turns the simulation into a structural initial-condition classification. The continuum of environmental memories proves that convergence to the same behavioral endpoint does not force environmental convergence to a single state. These are motivated, model-specific conclusions relevant to empirical basin estimation and interpretation of opinion-driven ecological feedback, rather than arbitrary numerical slices.

## Closest literature and residual risks

[1] Lorits and Gubar, *An evolutionary game with environmental feedback and players' opinions*, arXiv:2307.04902v1 (2023), equations (7)–(10), Section 3, Table 1 and Figure 1: the initiating equations and numerical examples, not the claimed classification.

[2] Paarporn, Eksin, Weitz and Wardi, *Optimal control policies for evolutionary dynamics with environmental feedback*, arXiv:1803.06737v1 (2018), Section IV: different linear opinion rule and controlled problem.

[3] Ito and Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus (2024), doi:10.1093/pnasnexus/pgae455: a broader title but structurally different ecological-payoff feedback; existence of multiple regimes is not a novelty claim here.

Residual risk: another unindexed or inaccessible treatment may derive an equivalent all-initial-state basin classification; no independent external audit or publication-priority certification has been undertaken. Stable graph's global shape remains implicit, and the result is parameter-specific.

Self-review: passed. Independent audit: not yet performed.
