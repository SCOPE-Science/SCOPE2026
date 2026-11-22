---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The exact integer ice rules h_{r,c}+v_{r,c}=h_{r,c−1}+v_{r−1,c} characterize 2-in/2-out orientations on the 3x3 periodic simple four-regular grid. Independent complete full enumeration of all 2^18 edge words produced exactly 148 states. Recomputed unnormalized integer Walsh transform on the whole cube reproduced every signed histogram entry, 162816 zeros, rank99328, min |W|4. The Eulerian bit words lie in the binary 10-dimensional cycle space, forcing 256-fold repeats by the 8-dimensional orthogonal cut space. Recomputed inverse Walsh of nonzero support gives absolute sum1,822,720/262144=445/64; translation averaging proves it is the optimum among all linear projections. Source SPECTRUM.json has all 1024 quotient coefficients, and source check_ice3.py independently describes two complete orientation enumerations; full finite exhaustion is appropriate to this exact finite claim.

## originality

PASS

Best-of-knowledge signed eighteen-edge character spectrum for the first simple square-ice torus is distinct from 148 unsigned configuration count and integrable six-vertex homogeneous-weight torus partition functions. No exact full Walsh table or sharp unrestricted range-projection constant found in searched published records; priority remains bounded.

## value

PASS

The first simple 3x3 periodic ice lattice is a canonical natural small torus, and an exhaustive independent-edge Walsh spectrum plus sharp range projection constant is a nontrivial exact, reusable benchmark of its full binary character response, not merely recomputing the known 148 unsigned configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
