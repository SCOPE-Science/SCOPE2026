# Scientific review: Lambert-fold extinction with a noninteger power correction

## Correctness — PASS

The claim is restricted to the explicitly parameterized Lambert-W fold \(a=\alpha(d+1)e^{1-q}\), \(b=q(d+1)e^{1-q}\), with \(0<q<d/(d+1)\). In blown-up physical-time coordinates, the angular drift has an exact quadratic maximum and the radial eigenvalue equals \(-\mu<0\). A small positive-ratio rectangle is forward invariant, the radial population decreases exponentially, and the exact angular Riccati asymptotic gives \(w=1/(\kappa t)+O(\log(t)/t^2)\). An integrable-remainder argument then supplies the strictly positive finite amplitude of \(u\sim C e^{-\mu t}t^{-\nu}\). The strong-stable graph follows from the isolated negative eigenvalue and its exact eigenvector. For \(b<d\), the prey-only equilibrium is hyperbolically stable. All conclusions are local except the existence of the positive global trajectories started inside the invariant wedge. Symbolic reconstruction and an independent numerical diagnostic were run successfully; numerical results are not used as infinite-time proofs.

## Originality — PASS on inspected evidence

The initiating 2022 paper [1] already has the change of variables \(z=v/u\), the Lambert-W angular fixed-point formulas, and hyperbolic stability diagrams. Its sections Methods, Results and Discussion were inspected, as were the corresponding full arXiv sections. None of these establishes the at-equality directional relaxation coefficient, the noninteger power in physical-time population extinction, or the strong-stable exceptional trajectory. These are not reclaims of the earlier fixed-point census.

The 2021 same-functional-response paper [2], whose accessible full text was inspected around steady-state analysis and its discussion, addresses delays and stochastic effects; it does not supply the undelayed angular-fold decay profile. Jost–Arino–Arditi [3] addresses deterministic extinction for a different ratio-dependent response; the full 1999 work was not accessible in this comparison, leaving a named residual risk. Xiao–Jennings [4] includes constant-rate harvesting and explicitly makes the origin nonstationary. Analogous published mathematical results on double-zero extinction and saddle-node slowing concern different equations and do not by themselves imply this exact coupled ratio–abundance asymptotic. Targeted publication-record searches revealed no directly covering formula; a failed search alone is not treated as proof of uniqueness.

## Value — PASS

The collision of the Lambert-W extinction directions is the exact boundary of the extinction stability regions studied in [1]. At that boundary, the theorem identifies an open positive-state extinction sector, computes the **two distinct observable decay scales**—slow ratio relaxation and exponentially vanishing abundances with a noninteger power—and isolates an exceptional pure-exponential curve. The optional \(b<d\) condition shows that this critical extinction sector can coexist with a stable prey-only attractor, so the threshold matters for fate selection, not only for local eigenvalue arithmetic. These are natural quantitative dynamical invariants of the underlying ecological model, rather than a chosen finite enumeration or cosmetic algebraic specialization.

## Closest literature and residual limitations

[1] K. B. Blyuss, Y. N. Kyrychko, O. B. Blyuss, *Frontiers in Applied Mathematics and Statistics* 8, 1083815 (2022), https://doi.org/10.3389/fams.2022.1083815.

[2] K. B. Blyuss, S. N. Kyrychko, Y. N. Kyrychko, *Chaos* 31, 073141 (2021), https://doi.org/10.1063/5.0055623.

[3] C. Jost, O. Arino, R. Arditi, *Bulletin of Mathematical Biology* 61, 19–32 (1999), https://doi.org/10.1006/bulm.1998.0072 (abstract/metadata only during this review).

[4] D. Xiao, L. S. Jennings, *SIAM Journal on Applied Mathematics* 65, 737–753 (2005), https://doi.org/10.1137/S0036139903428719 (abstract-level comparison).

The theorem is deterministic and local to the angular fold. It does not infer stochastic extinction times, global attraction, or an elementary formula for the initial-condition-dependent amplitude. An unindexed or inaccessible equivalent asymptotic result remains possible.

Self-review: passed. Independent audit: not yet performed.
