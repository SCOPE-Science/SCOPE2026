---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

From unsigned incidence B, the identities A=BᵀB−2I and BBᵀ=(N−2)I+11ᵀ split the space into constants, centered incidence image, and ker B, the last zero dimensional at N=3. On each bipartite detector component an alternating vertex labeling gives one degree of freedom, including an isolated vertex; an odd cycle kills it. Centering removes one degree iff at least one such component is unbalanced. The bottom-sector vectors zero on D are the zero extensions of ker B_G, giving |E(G)|−N+b(G). The constant sector contributes no dark state for nonempty D. The sum of the two nonnegative dark nullities gives the formula, and the second vanishes exactly when each connected component is a tree or odd-unicyclic. Positivity of the detector rates identifies real-eigenvalue modes with these dark modes through the imaginary part of the eigenvalue equation. The dark span reduces the Hamiltonian, has unitary evolution, and the finite-dimensional complementary generator has strictly negative spectral real parts even if it has Jordan blocks; hence pure- and mixed-state projection formulas. At least M−N detectors are needed to observe ker B. The odd spanning cycle or odd (N−1)-cycle with a leaf leaves a connected nonbipartite detector graph at N≥5: for odd N≥7 the distance-two edges connect the complement and 0,2,4 form a triangle; for even N≥6 the leaf attaches in the complement to every cycle vertex but its old neighbor, which has other complement neighbors, and the leaf and two nonconsecutive nonattachment vertices form a triangle. For N=5 the complement is a five-cycle. The N=3 and N=4 lower bounds are the respective middle multiplicities, two and three; the displayed stars attain them (complements are, respectively, an edge with an isolated vertex and a triangle with an isolated vertex). Thus all placement, threshold, and gap statements are correct in the stated regime. Frozen numerical checks were inspected as corroboration, not executed or used to prove general statements.

## originality

FAIL

The headline arbitrary-detector classification for the infinite family N≥5, including the arbitrary-state loss projection, is directly covered by Resultary 1d711c8bda6b. Its graph ranks give exactly the full-absorption component test. Resultary 48fd742d49c4 gives equivalent minimum coordinate-control counts, including the two boundary orders, and a minimum-placement characterization; PBH makes the equivalence exact. The distinct covering catalogue paths are dated later than the frozen path. Mathematical coverage in the inspected corpus is established, not dependence or historical discovery priority. The original zero-forcing paper establishes the comparison number, not fixed-Hamiltonian observability.

## value

FAIL

The classification by two simple graph invariants and the observability/zero-forcing gap are scientifically meaningful for trap design. But both are covered by the verified infinite-family rank result and equivalent actuator theorem. The remaining arbitrary-placement extension to N=3,4 is a routine boundary check of the same incidence decomposition, not a motivated independent invariant or substantive repair. Real nonzero hopping rescaling and the conventional factor two in the losses do not create a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
