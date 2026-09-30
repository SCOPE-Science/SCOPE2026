# Independent audit — 2026-09-29
- Source: `2026/09/12/059`
- Assigned/current tree SHA: `7d9d4d1925388ead9c0947c3ce0382d023f65d60`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**PASSED** — The reflection obstruction is correct. The involution y→-y commutes with -Δ_{S²}, z, and x, so the even subspace is invariant under every controlled propagator from the constant ground state. Smooth odd y-harmonic perturbations are arbitrarily H³-close and unreachable, which rules out local exact controllability at every time and hence any small-time polynomial-cost statement.

### Originality

**FAILED** — The exact two-control obstruction was already stated in the primary literature. Boscain, Caponigro, and Sigalotti’s 2014 paper writes the same S² equation with the three coordinate controls x,y,z and explicitly notes that, because of symmetry obstructions, it is not controllable with only two of the three controls. By rotational symmetry this covers the submitted (z,x) pair. The record supplies an explicit proof of an already documented obstruction, not a new result.

### Scientific value

**FAILED** — The explicit invariant-subspace/H³ witness proof is pedagogically clean, but as a research finding it does not move the known controllability boundary: the necessity of all three coordinate controls for this model was already identified in the paper that established the complementary three-control result.

## Independent checks

- current main record tree exactly equals the assigned source-tree SHA
- rechecked commutation of y-reflection with the Laplace–Beltrami operator and x,z multiplication
- rechecked odd spherical harmonic η proportional to y is orthogonal to the invariant even subspace and H³-close after normalization
- matched the model to Boscain–Caponigro–Sigalotti equation (2), which explicitly states noncontrollability with only two of x,y,z

## Limitations

- The audit does not dispute the stronger exact-local noncontrollability proof; it rejects novelty/value as a standalone finding because the two-control symmetry obstruction predates the record.
- The cited prior states the two-of-three obstruction without the record’s exact H³ witness construction, but it covers the same physical/mathematical model and control subset up to coordinate rotation.
- Open-access/transcribed primary material was sufficient; Oxford Download was not needed.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/059
- https://arxiv.org/abs/1302.4173
- https://doi.org/10.1016/j.jde.2014.02.004
