# Scientific review: half-degree rigidity and threshold collapse

## Correctness — PASS

The proof is complete for the stated finite connected even-regular graphs and for every squared cycle of length at least five. It first establishes that a configuration fixed by the third iterate is locally either always zero or rotating through all three phases. For the active set \(S\), successor-color contacts satisfy \(\theta|S|\le\sum_{v\in S}d^+(v)\le e(S)\le r|S|\). At \(\theta=r\), each inequality must be an equality, forcing \(S=V\), a proper three-coloring, and exactly \(r\) successor and \(r\) predecessor neighbors at each vertex. This condition is sufficient by direct update. The cube-root eigenvector equivalence is verified by separating real and imaginary parts; it is not confused with a plain eigenvalue test. Every consecutive triple in \(C_n^2\) is a triangle, which forces the three-periodic spatial coloring and the exact six-or-zero census. Finally, independent binary block choices give the stated threshold-one exponential lower bound.

Two independent executable checks corroborate the finite cases. `verification/direct_update.py` applies the rule itself on all \(796797\) configurations for \(5\le n\le11\) and three thresholds. `verification/phase_patterns.py` independently enumerates \(2795520\) augmented phase assignments for \(5\le n\le10\), plus the constructive family through \(n=27\). Their captured results agree with the proved formulas. Neither enumeration is substituted for the infinite proof.

## Originality — PASS, with historical qualification

The closest substantive primary source is Fisch and Gravner, *One-dimensional Deterministic Greenberg–Hastings Models* (1995), especially its introduction and §§2–4 on contact thresholds, stable periodic objects and infinite-line phases. It motivates the problem but does not state a finite ring-square period-three census or general even-regular balanced-coloring equivalence. Gravner, Lyu and Sivakoff (2016 preprint; 2018 journal) treat threshold-one dynamics on arbitrary graphs rather than this threshold-two boundary. Durrett and Griffeath (1993 preprint) establish background threshold/range phenomena in lattice excitable media, but the full text was unavailable and remains a priority uncertainty.

Overlap was checked against closely related earlier specialized calculations in the accessible mathematical record, including a threshold-one squared-cycle census and a threshold-two cubic-line-graph colouring correspondence. The present theorem is not an implication of either statement as stated: it addresses the distinct threshold on squared cycles (which are not uniformly within the earlier cubic-line-graph family), proves a general even-regular rigidity and spectral criterion, and independently constructs the threshold-one comparison lower bound. The relationship is explicit rather than hidden. Searches did not reveal an equivalent published theorem, but unsuccessful searches do not establish absolute priority. Potential equivalence in unindexed literature is a residual risk.

## Mathematical value — PASS

The precise boundary at half the graph degree is a structural obstruction for immediate excitation cycles across an unrestricted class of regular networks, reducing a dynamical problem to balanced three-colorings and a strong cube-root eigenvector constraint. On the natural finite-range, one-dimensional family \(C_n^2\), this yields a sharp arithmetic finite-size classification and an explicit entropy-collapse contrast: threshold one supports at least \(3\cdot2^{n/3}\) three-periodic configurations at circumferences divisible by three, whereas threshold two supports six, and threshold three none. This makes a concrete dynamical distinction between wave propagation with one or two required contacts. The result is a motivated contact-threshold boundary, not merely a recomputation of a known table or a parameter substitution in an unrelated formula.

## Limitations and remaining risks

The spectral eigenvalue condition alone is not sufficient without cube-root coordinates. The theorem does not classify other temporal periods or basins, and the general even-regular case need not have a closed population formula. A few foundational historical sources could not be fully inspected; independent historical validation and independent mathematical audit are outstanding. No claim of comprehensive historical priority or external certification is made.

Self-review: passed. Independent audit: not yet performed.
