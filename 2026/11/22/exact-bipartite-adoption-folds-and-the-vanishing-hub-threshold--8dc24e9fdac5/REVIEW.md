# Scientific review: exact bipartite adoption folds

## Correctness — PASS

The model, rescaling, graph, exponent and all parameter ranges are explicit. Every nonzero equilibrium is fully positive and equal within each bipartition. The scalar equilibrium parameter has one strict nondegenerate minimum by the exact derivative (2). The full-network Jacobian decomposes into two collective modes and strictly damped within-part modes; the determinant sign proves the claimed saddle/attractor separation. The star limit follows from the fold identity and the strictly increasing function \(F_d\). `verify_bipartite.py` passes 313 supplementary checks, including rational exact examples. No finite sample is used as an infinite-size proof.

## Originality — PASS, bounded literature comparison

The primary 2026 study derives the model, its narrow-degree scalar reduction and homogeneous equilibria, but its complete accessible text does not state an exact \(K_{m,n}\) threshold or its \(n^{-1/(d+1)}\) star limit. A 2024 payoff-biased social contagion model uses a different update mechanism; 2013 star SIS analysis concerns a stochastic epidemic; and hypergraph contagion fold criteria use group-dependent infection, not a sum of neighbor powers. Indexed published mathematical findings involving multipartite hypergraph contagion and bipartite anti-coordination learning do not imply this exact network-ODE result under the same hypotheses. Source coverage is incomplete for some broader historical material, which remains a priority risk. Absence of a keyword hit is not a uniqueness proof.

## Value — PASS

The node-level model was motivated by nonlinear collective adoption, but its scalar approximation assumes concentrated degrees. The theorem supplies an analytically exact, qualitatively different prediction in the canonical heterogeneous test family \(K_{1,n}\): a finite-density adoption attractor emerges at a vanishing influence threshold, with a sharp exponent depending on reinforcement \(d\). The whole-biclique equilibrium census and transverse stability analysis rule out hidden partially active equilibria and symmetry-breaking stable branches; the result is thus not just a one-dimensional restatement. These features are useful when deciding whether coarse degree-averaged collective-action predictions can represent hub-dominated networks.

## Closest work and limits

The model and homogeneous branches are due to Ariwayo–Morsky–Asllani (2026), arXiv:2607.05608. Chiba-Okabe–Plotkin (2024), Cator–Van Mieghem (2013) and hypergraph contagion work contain related mechanisms in different dynamical systems. The result does not establish global basins, finite-state stochastic dynamics, or accuracy of any approximation on its prescribed narrow-degree domain. Literature novelty has not received independent verification.

Self-review: passed. Independent audit: not yet performed.
