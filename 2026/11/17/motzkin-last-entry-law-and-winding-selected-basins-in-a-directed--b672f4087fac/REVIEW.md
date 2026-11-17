# Scientific review

## Correctness — PASS

The one-step edge-difference calculation gives the exact moving/stationary annihilation rule. Survivors of opposing types cannot coexist after \(n-1\) moves because a surviving moving particle would have visited the location of every stationary one. When a type vanishes, the vertex word is already fixed or rotates. For the late-arrival boundary, a unique final collision forces an initial word \((2,u,1)\) up to cyclic origin; precisely Motzkin excursions \(u\) cancel all interior particles in time. This yields \(3nM_{n-2}\), including \(n=2\). Winding invariance and colour-lift multiplicity prove both basin formulas. The standard Motzkin singularity expansion proves the stated square-root asymptotic. Two independent Python programs test the state dynamics and the particle/Motzkin bijection within explicitly bounded finite ranges; they do not stand in for the infinite proof.

## Originality — PASS, qualified

Closest result inspected: Kůrka–Formenti–Dennunzio (DOI 10.46298/dmtcs.2976) explicitly has the **identical stationary/left-moving collision automaton** and proves an infinite-line fixed-site particle-arrival-time distribution. Its Definition 1 uses appearance of a specified particle at a site after age \(t\), rather than first global periodic entry on a finite labelled ring, and its Theorem 3 does not count \(3nM_{n-2}\) cyclicly constrained initial states. The all-size finite-ring Motzkin bijection and winding lift are separate additional results; the particle reduction itself is NOT new. Another full text inspected: Hellouin de Menibus–Le Borgne (arXiv:1903.12622), Sections 1.2 and 2, uses neighbourhood \(\{-1,0,1\}\) on the bi-infinite line, with bidirectionally moving boundaries and invariant-measure asymptotics. Here the neighbourhood is one-sided on finite rings and the exact question is first periodic entry and its extreme Motzkin count. Durrett–Griffeath (arXiv:patt-sol/9303002) studies excitable-medium scaling and spiral thresholds rather than this finite-ring distribution. Fisch's earlier two-sided process concerns infinite-line fluctuations. Belitsky–Ferrari (DOI 10.1007/BF02178546) describes deterministic ballistic annihilation, so it is a plausible related source, but the full text was inaccessible: its abstract cannot exclude equivalent finite-volume counts. Direct comparison with Kůrka–Formenti–Dennunzio and searches of indexed records and earlier accessible claims found no statement or immediate implication of this finite-ring periodic-entry law; lack of a hit alone is not proof of novelty. Priority remains explicitly provisional.

## Value — PASS

Despite the known asymmetric-glider particle rule, the maximum settling time is sharp for every cyclic ring length, while its exact attraction layer has a nonzero polynomial-order probability \(\asymp n^{-1/2}\). The Motzkin formula is a motivated count of the rare final possible collision, not an arbitrarily selected word statistic. Conserved signed winding gives an independent complete classification of eventual fixed and rotating basins. This combines a dynamical phase selector and a sharp, computable last-entry tail for a natural oriented cyclic-competition rule.

## Limits and related literature

The claim concerns the directed rather than standard symmetric nearest-neighbour automaton; it does not establish a result for higher colour counts or arbitrary graphs. The 1995 full text was unavailable through the attempted lawful access routes, and less-indexed exact ring treatments may exist. Periodic orbits need not have primitive length \(n\). Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
