# Scientific review

## Correctness — PASS

The stated \(n\ge2\) theorem includes all normalized symmetric integer proposal laws, zero moves and proposals always rejected at every site. The endpoint Rayleigh vector proves the sharp baseline, explicit matrix entries prove attainment, a graph-Laplacian norm and spectral second-moment lemma prove positive shape stability, and scaling away unproductive proposal mass proves the full bound. The exact all-parameter equality case is unique. The finite arithmetic checker has 15,483 successful tests, which only support the all-n proof rather than substitute for it.

## Originality — PASS (qualified)

The strongest matching primary studies are the continuous-state Metropolis box analyses [1, 2]. The continuous optimum \(1/2\) is prior work; the proposed contribution is the exact finite discrete correction and uniqueness with the two-component stability inequality. Unrestricted symmetric Markov mixing [3] is broader in feasible kernels but cannot supply the same constrained optimum because it allows an inadmissible zero-spectral-radius kernel. The nearest-neighbor path theorem [4] disallows the long jumps that attain the present optimum. Searches for equivalent statements, broader implications and exact tables identified no matched result in the inspected sources; independent priority validation is absent. A straightforward independent derivation from the continuum insight remains a material risk in novelty assessment.

## Mathematical value — PASS

The theorem determines a natural state-independent rejected-jump Monte Carlo design at every finite lattice size, including a quantitative penalty for throwing proposal mass into zero/overlong displacements and for uneven jump lengths. Unlike an isolated finite graph calculation, this all-size classification gives exact spectra, mixing profiles, and an acceptance-rate interpretation. The shape coefficient is conservative, and no claim is made for other sampler classes.

## Closest literature and limits

1. Chepelianskii et al. (2023), arXiv:2303.08535: continuum optimum at \(1/2\).
2. Chepelianskii et al. (2022), arXiv:2207.10488: continuous proposal and box localization framework.
3. Boyd, Diaconis and Xiao (2004): unconstrained graph-kernel spectral optimization.
4. Boyd, Diaconis, Sun and Xiao: nearest-neighbor finite path mixing.

Self-review: passed. Independent audit: not yet performed.
