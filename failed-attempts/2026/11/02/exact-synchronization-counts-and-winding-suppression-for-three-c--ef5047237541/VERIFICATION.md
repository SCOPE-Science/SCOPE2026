---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated CCA counts and asymptotics hold. A synchronization coloring uniquely determines a 1-Lipschitz integer height after rooting one vertex, with three choices of its root color. The rung difference d and upper increment a determine the lower increment a+e-d, which must also be in {-1,0,1}. Cyclic trace matches the initial rung difference, and constant-term extraction enforces exact closure of the upper height, hence also of the lower height; column 1 is labelled and there is no quotient by rotations. This includes the two triangles at n=3. Open paths have neither closure condition. I recomputed the Laurent characteristic polynomial symbolically and the first four counts by independent spanning-tree integration (261,1485,8409,49215), with open counts 363,2313,14739,93921 for the same lengths. On the Fourier circle the larger quadratic root is increasing in s=2cos(theta), with the unique maximum at 2; neither the other root nor s has comparable modulus. Its log has quadratic coefficient -sigma²/2 and an even analytic expansion, giving the relative O(1/n) Gaussian estimate. The open Perron vector (1,t,1) gives the stated B. Exact symbolic and finite replay: python3 /workspace/branches/reproduce_frozen_math.py 5.

## originality

FAIL

The principal all-length cyclic count, exponential rate and Gaussian prefactor already occur for an exactly equivalent basin in Resultary cae3512f5687. The later distinct indexed record 21af972dbcc9 explicitly identifies the basins, counts all winding sectors, and even contains the same reduced three-state Laurent block up to a permutation. Dates are not used to infer authorship or order between derivations. The open denominator is the sum of paths in that already-specified step graph; its three-state Perron amplitude and the displayed ratio are direct endpoint specialization and division, not a separate uncovered invariant of sufficient substance for repair.

## value

FAIL

The dynamical invariant and the cyclic seam effect are well motivated, but the exact closed basin and the Gaussian winding penalty are already covered. The remaining comparison uses the same step graph with free endpoints and an elementary Perron projection. It is a helpful reformulation and interpretation of current coverage, not a distinct unknown exact result or independently substantial new boundary theorem in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
