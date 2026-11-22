---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For regular n>=3, polygon-intersection of the vertex-diameter disk is disk area pi/4 minus exactly two disjoint adjacent circular caps, giving the exact mean ((pi/2-pi/n)/sin(2pi/n)+1/2). The disk condition cos(theta-2pi j/n)>=||x|| makes depth an equally spaced circular arc count, with sharp discrepancy 1/n attained at side midpoints. Coupling uniform n-gon area to uniform circumdisk at total variation delta_n and the pi-Lipschitz sin² CDF yields the stated limit and finite-n Kolmogorov bound. Independently evaluated mean via both polygon cap area and closed form for n=3,5,8,18. These agree; the proof provides universal n and boundary cases.

## originality

FAIL

Direct same-object complete PMF from published prior result; The prior stronger exact finite distribution subsumes the main numerical/probabilistic conclusion. A correct proof, sharper presentation or new verification does not make a covered claim original; reject, no disclaimer repair.

## value

PASS

Quantitative coverage depth of natural vertex-to-center diameter disks is a useful geometric statistic, and the exact finite mean, sharp discrepancy and limit distribution are motivated and correct. Nevertheless value alone does not rescue the claim because a published all-k exact distribution for exactly the same depth already dominates its content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
