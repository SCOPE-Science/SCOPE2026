---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility verification

The standalone Python 3 script `check_exact.py` (requires SymPy) was executed successfully against the actual code text packaged here. It checks the normalized mass PGF, the first two coefficients, strict log-concavity, and the two-sided numerical root enclosure. In particular, exact rational upper/lower Taylor bounds for \(e^\sigma\) prove opposite signs of the transition equation at two specified rational decimals and prove a strictly negative degree-104 log-PGF coefficient at \(\sigma=1/20\). The bound on the Taylor remainder is a geometric majorant of the positive omitted terms. It also evaluates four finite coefficient families as supplementary checks. No floating-point values are used to decide theorem-critical inequalities.

The **infinite** assertions are established analytically in RESULT.md: the discrete compound-Poisson characterization treats all log-PGF coefficients, and the positive Maclaurin series for \(D(x)\) proves the threshold's global uniqueness. No finite loop establishes those universal claims.

Literature matching remains limited to accessible source sections and published research searches, and no independent audit or externally certified proof is claimed.
