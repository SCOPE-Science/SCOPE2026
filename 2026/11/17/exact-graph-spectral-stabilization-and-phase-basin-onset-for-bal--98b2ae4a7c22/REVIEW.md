# Scientific review: balanced antipodal spectral stabilization

## Correctness (C): PASS

The exact triadic derivative at a balanced sign pattern has rank one, producing a symmetric Jacobian. The quotient decomposition into the collective sign direction and its orthogonal shape modes is exact; the symmetric Schur-complement equivalence proves necessity as well as sufficiency of the proposed finite-graph criterion, including equality boundaries. An explicit block spectrum proves the community threshold. Direct substitution into the flow yields the exact invariant-circle equation, and one-dimensional sign analysis and Taylor expansion establish the basin fraction, square-root onset and critical cubic instability. The bundled `checker.py` provides 452 successful finite-dimensional comparisons but is not used to prove the all-graph statement.

## Originality (O): PASS within inspected evidence

The motivating 2026 mixed-order model paper [1] studies finite-size synchronization, rather than proving a balanced-antipodal arbitrary-weight-graph criterion. Skardal–Adhikari–Restrepo [2] already treats antiphase community clusters in a related all-to-all community framework; this is acknowledged, and no general first discovery of antiphase states is asserted. The inspected model and analysis there do not give the finite-graph compression/Schur criterion or the exact uniform-relative-phase basin fraction. Skardal–Arenas [3] gives a stability test for a different, symmetric higher-order interaction. Closely related special-topology calculations exist; the new contribution is a necessary-and-sufficient arbitrary-graph obstruction together with a natural sharp block-model boundary and its exact invariant-circle basin law. Search coverage does not establish exhaustive priority: a hidden equivalent signed-Laplacian theorem or a special community reduction remains a risk.

## Mathematical value (V): PASS

Graph heterogeneity is not a cosmetic perturbation: rank-one global triadic feedback can stabilize the community-difference mode but cannot fix any noncontracting internal shape mode. The theorem gives an exact, implementable obstruction and minimum triadic gain on every finite weighted graph of the stated kind. On the standard two-block family it yields a sharp assortativity condition, a nonlinear critical boundary, and an exactly quantified positive-measure interval of initial phase differences captured by antiphasing. The basin fraction is not promoted to a full-torus probability.

## Sources and residual limits

[1] Sharma et al., *Synchronization transitions in Kuramoto oscillators with mixed interactions*, doi:10.1140/epjs/s11734-026-02482-w; full lawful arXiv https://arxiv.org/html/2611.09564v1.

[2] Skardal, Adhikari and Restrepo, *Multistability in coupled oscillator systems with higher-order interactions and community structure*, https://arxiv.org/abs/2207.00070.

[3] Skardal and Arenas, *Memory selection and information switching in oscillator networks with higher-order interactions*, https://arxiv.org/abs/2007.11561.

Independent external verification, exhaustive historical-priority assessment, nonlinear classification of general nonhyperbolic graph endpoints and full-phase-space basin volume are not performed.

Self-review: passed. Independent audit: not yet performed.
