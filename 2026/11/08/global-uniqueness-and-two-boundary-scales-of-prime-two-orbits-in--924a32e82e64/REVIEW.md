# Review of a global prime-two-orbit classification

## Correctness

**PASS.** The theorem is proved for all real \(r>0\), \(c,m\ge0\), \(c+m>0\), with cycles restricted to distinct \(0<u<v<1\). A first exact symmetric identity from \(u f_r(u)=v f_r(v)\) forces \(s=u+v>1\) and gives the product \(p(s)\). The other symmetric equation forces \(r=R(s)\). The discriminant is positive precisely on \(1<s<s_*\); an independent complementary-product identity ensures that the two roots are inside \((0,1)\). The rational function \(R(s)\) is strictly decreasing from infinity to \(r_*\), proving the complete if-and-only-if and uniqueness, including both coefficient boundary cases. Exact product limits yield the two different endpoint power laws. Five symbolic identities and 54 high-precision orbit/boundary instances were reproduced by the included checker. Computations corroborate but are not the infinite proof.

## Originality

**PASS, with priority caveats.** The full accessible text of Pires–Andrade–Herrmann (arXiv:2606.05351v1) was compared through the model equations, equilibrium calculations, chaotic/period-doubling discussion, conclusions, and references. It establishes the family and numerical period-doubling scenario, but not a global one-branch parametrization of all positive primitive two-cycles nor the distinct high-growth endpoint exponents. A previous local flip analysis already gives the threshold and near-onset two-cycle; those facts are not asserted as novel here. The cubic map's all-growth uniqueness and exact boundary rates are strictly stronger and cannot be deduced merely from local bifurcation existence. The standard logistic case is already known and is included only as a boundary check. Jung et al. (2020) study an earlier Allee special model; only its abstract was accessible, so possible historical priority for that special case is unresolved. General sources on cubic and logistic dynamics could contain an equivalent result under alternative parametrization; historical novelty is provisional pending independent exhaustive review.

## Mathematical value

**PASS.** The most immediate question after a period-doubling calculation is whether the born period-two cycle is the only one and whether it persists through higher-period and chaotic regimes. For a general cubic map, the sixth-degree nonfixed factor of the second iterate permits multiple two-cycles; a local flip theorem cannot answer the global census. Here the nonnegative Allee-logistic structure forces one and only one positive orbit for the entire parameter ray, with a monotone exact parametrization. The linear-growth degeneracy changes both high-growth endpoint powers sharply. Such classification provides an exact periodic-orbit benchmark, though extrapolation to high growth is algebraic and may leave the interval-invariant biological regime.

## Closest literature and limits

Pires et al. (2026, arXiv:2606.05351v1): map, extinction transitions and numerically displayed period-doubling/chaos. Jung et al. (2020, DOI:10.3938/jkps.76.533): earlier special Allee model, abstract only. Wolfram MathWorld, *Logistic Map*: classical quadratic endpoint. The classification excludes strong Allee \(c<0\), all higher periods, stability after first flip, global attraction and physical invariance of \([0,1]\) for arbitrarily high growth.

Self-review: passed. Independent audit: not yet performed.
