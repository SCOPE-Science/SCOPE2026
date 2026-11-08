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

# Exact arithmetic verification

Run \`python3 verify.py\` with the Python standard library. The script checks 1,249 exact assertions, including independently reconstructed polynomial coefficients from finite differences applied to lattice-slice counts, identities (3)–(4) of the mathematical statement in dimensions \(1\) through \(32\), and the exact first nonpositive case at \(d=17\). The reported result is \`EXACT_CHECKS_OK=1249\`.

The lattice slices count \((t-j+1)(j+1)^d\) at each integer dilation parameter. The verifier evaluates the polynomial at enough integer points to determine all coefficients, then compares exact rational coefficients to the Bernoulli expressions computed from the standard Bernoulli recurrence. It additionally tests the specified negative witnesses for every \(18\le d\le32\).

These computations are finite and do not prove the conclusion for all larger dimensions. The infinite part is the analytic Bernoulli growth inequality in the proof, based on Euler's even-index formula and \(1<\zeta(r)<2\). No external formal certification or independent review was performed.
