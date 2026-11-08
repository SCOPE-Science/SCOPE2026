# Scientific review

## Correctness

**PASS.** The discounted hitting transform \(p_\varepsilon=(1-\gamma)e_r^\top[I-(1-\gamma)Q_\varepsilon]^{-1}b_\varepsilon\) follows from first-step conditioning, is analytic at zero, and is strictly positive for positive holding probability. The bipartite parity equation forces at least \(k=\min(m,S-m)\) holds on every successful cycle; a prescribed path with one hold per member of a minority class proves the matching positive order. The renewal equation supplies the exact mean and the exponential rare-arrival limit. The three-transient-state star equations were reconstructed symbolically, and the optimizer's uniqueness follows from a verified quartic derivative with one Descartes sign change. The independently run checker passed 179 assertions. Numerical checks are supportive only, not proofs of infinite asymptotics.

## Originality

**PASS, qualified.** The closest primary source, Suarez-Jimenez, Riascos and Boyer (arXiv:2604.20770), provides multiwalker spectral encounter theory and comparisons of simultaneous versus independent reset mechanisms. Rubio-Gómez, Riascos and Mateos (arXiv:2508.05313) give earlier two-walker spectral formulas and identify bipartite periodicity. The new claim concerns a separate small-*independent-hold* parameter under a fixed synchronous reset, with a universal minority-count singular exponent for arbitrary numbers of walkers and every connected bipartite graph, plus a leaf-count-independent star optimization theorem. Betz–Le Roux's general finite-chain metastability and Silvestrov's general rare-event framework cover broad methods and may offer alternative derivations of the exponential law; neither accessible material explicitly supplies this bipartite exponent/optimizer classification. Indexed published-finding corpus queries and available local prior-claim searches found no equivalent or stronger explicit classification. These are implication comparisons, not a claim of uniqueness based on absence of matches; priority uncertainty remains around general rare-chain specializations.

## Value

**PASS.** A synchronized multiagent search has an exact, topology-independent hierarchy of parity-repair costs that grows with the size of the smaller initial bipartition cohort; a single hold is insufficient for balanced groups of four or more agents. This resolves a concrete accessibility-to-metastability transition for the motivated synchronous-resetting network model, with a sharp power-law delay and its limiting distribution. The star result further identifies an exact, finite optimal amount of independent inactivity even though either deterministic synchronous motion or complete immobility makes the meeting time infinite, and exposes an unexpected independence from the number of leaves. These statements are more than a reparameterization or finite table evaluation, and isolate experimentally meaningful constraints on coordinated search.

## Closest literature and limits

Primary material inspected: arXiv:2604.20770v2, Sections II, III.5, IV and Appendix A; arXiv:2508.05313v1, Sections 2–3 and the displayed spectral examples; Betz–Le Roux (2016), introduction and metastability examples; Silvestrov (2022), public overview only. Main originality risk: general metastability theorems may imply the renewal and exponential portions, and an unindexed worked bipartite specialization could cover the remaining claims. Domain is finite graphs and fixed \(\gamma\in(0,1)\); no thermodynamic or double-scaling limit is asserted.

Self-review: passed. Independent audit: not yet performed.
