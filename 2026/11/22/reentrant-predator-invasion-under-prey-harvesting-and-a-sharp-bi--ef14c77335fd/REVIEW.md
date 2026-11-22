# Review of the reentrant-invasion theorem

## Correctness — PASS

The paper's integer-order equations reduce the prey-only equilibrium to the strictly decreasing harvest map \(H(x)=r(1-x/K)(1+qx)\) when \(qK\leq1\). The rare-predator eigenvalue is \(G(x)=Ax/(1+Bx)-d-vx\). Multiplying by \(1+Bx>0\) gives one concave quadratic, which has exactly two positive simple roots if and only if \(A>(\sqrt v+\sqrt{dB})^2\). The decrease of \(H\) proves the complete strict-invasion classification, with explicit boundary and carrying-capacity cases. The center-manifold calculation independently establishes the criticality of each simple collision: the quadratic coefficient is \(Q=-m-RG'(x_0)\), with \(R=f_y/f_x>0\), giving the sharp self-limitation cutoff at the low-harvest collision. The rational witness and finite numerical equilibrium checks passed after running the standalone checker. No finite check is being used to prove an infinite classification.

## Originality — PASS, with bounded historical risk

The originating 2026 study provides the ecological system and prey-only stability criterion, not the complete two-harvest-window classification together with the direction and stability of both transcritical coexistence branches. Prior ecological work already contains reentrant invasion and backward bifurcations in other models; the broad phenomena are **not** claimed new. The comparison concerns the exact 2026 model with simultaneous Holling-II predation, prey-proportional counterattack and saturated harvesting, and the explicit critical value \(m_{\rm crit}\). Earlier pest-impulse and three-species fear models use different equations and do not imply this classification. The 2025 anti-predator/refuge/additional-food manuscript was accessible only at the abstract level, so overlapping unpublished/older specializations remain a material priority risk. No full-text non-coverage claim is made for that source.

## Mathematical value — PASS

The source model's harvesting control and prey counterattack compete in the predator invasion exponent in a way that makes monotone threshold intuition fail. Determining whether there are zero, one or two invasion crossings, locating both exact thresholds, and deciding whether coexistence enters from the stable or unstable side address ecological interpretation of harvest variation. The local backward branch is particularly important: it permits a positive saddle coexistence state on the non-invasion side, so an invasion eigenvalue by itself does not describe the full equilibrium structure. The explicit discriminant and self-limitation criteria are substantive sharp boundaries, not merely a numerical example.

## Limits and competing literature

This does not determine global basins, nonlinear cycle behavior, extinction for finite predator introduction, or Caputo fractional-order bifurcation properties. The result is a model-specific local classification, not first discovery of reentrant invasion. Closest fully available source: Govindan and Singh (2026), https://doi.org/10.1371/journal.pone.0360316. Other compared literature: Qin and Dong (2024), https://doi.org/10.1186/s13662-024-03804-9; Öztürk (2026), https://doi.org/10.1140/epjp/s13360-026-07832-0. Incomplete comparison risk: Ojha and colleagues (2025), https://doi.org/10.1016/j.chaos.2025.116409.

Self-review: passed. Independent audit: not yet performed.
