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
# Reproduction and limits

Run `python3 verify.py` from the folder containing the script. It is self-contained and uses only Python 3 standard-library modules. Brute-force enumeration examines all \(2^{n+\binom n2}\) two-color assignments for each \(n=3,4,5\), computes valid strong total covers, and counts complementary cover pairs, including their vertex-side layer distributions. The exact ordered counts are 20, 154, and 1432, giving 10, 77, and 716 unordered pairs. Subsequent checks cover the closed-form symmetries and parity for \(3\le n\le100\), and numerical total-variation approximations using theta truncations. These are finite computations; the written proof is the basis of the all-dimensional formula and its rate. There is no independent mathematical audit.
