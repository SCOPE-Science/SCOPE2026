# Scientific review: weighted triangular-book anti-coordination

## Correctness — PASS

The theorem's exhaustive two-hub case distinction, page best replies, and both explicit hub inequalities produce the exact interval and every equilibrium, including equality boundaries. Every equilibrium cut has one of two specified weights. The maximum over both hub patterns is the global maximum cut; potential identity proves its Nash stability and the welfare/price-of-anarchy formula. The asymmetric perturbation makes each page's choice unique and renders the opposite-hub best reply unstable. Exact-rational direct enumeration of 318,360 profiles across 2,605 settings independently confirms the formula in finite cases; it is not used as an infinite proof.

## Originality — PASS, subject to known residual risks

The closest comparison is Lampis (2021, Theorem 3.5), which explicitly uses a symmetric two-center complete bipartite partition gadget to show hardness of minimum stable cut. That substantially covers the underlying subset-sum mechanism, which is credited, not relabeled as new. Kun, Powers and Reyzin (2013) already establish a general price-of-anarchy bound, and their unweighted game is the natural antecedent; the present special-class exact count and perturbation behavior is not a consequence of that bound. The inspected material in Deligkas et al. (2023) concerns complexity of anti-coordination outcomes; Carosi et al. (2018) concerns strong-equilibrium existence; and Lampis (2021) does not supply the asymmetric positive-spine complete Nash census, exact two-level efficiency diagram, or the arbitrarily small perturbation's exponential equilibrium collapse. The assessment compares mathematical implications, not just titles, and cannot exclude unpublished or unindexed equivalents.

## Value — PASS

A natural two-hub network has a complete exact enumeration despite potentially complex weighted equilibrium selection. The result isolates a sharp structural transition: a slight systematic asymmetry changes both the entropy of stable configurations and the worst-equilibrium efficiency discontinuously. The full formula also shows how different spoke strengths and the common hub edge govern equilibria through one explicitly defined subset-sum window. These statements supply interpretable boundary information beyond simple existence or one illustrative profile; the symmetric partition condition alone is prior art.

## Closest literature and limits

- Deligkas, Eiben, Gutin, Neary and Yeo, *Some coordination problems are harder than others* (2023), arXiv:2311.03195; binary anti-coordination complexity.
- Lampis, *Minimum Stable Cut and Treewidth* (2021), arXiv:2104.13097, Theorem 3.5; symmetric two-hub partition reduction already known.
- Carosi, Fioravanti, Gualà and Monaco, *Coalition Resilient Outcomes in Max k-Cut Games* (2018), arXiv:1810.09278; general weighted max-cut game and strong equilibria.
- Kun, Powers and Reyzin, *Anti-Coordination Games and Stable Graph Colorings* (2013), arXiv:1308.3258; unweighted stable colorings and general price-of-anarchy bound.

Restrictions: strictly positive weights, exactly two actions, and triangular-book graph; an unindexed equivalent statement remains possible. Reproducible finite exact checks are not independent validation or a substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
