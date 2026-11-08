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
# Reproducibility and independent-audit status

Execute `python3 pappus_dominance_verify.py` from a directory containing the standalone script; it uses only the Python standard library and does not read external files. Compare stdout with `pappus_dominance_verify_output.txt` and check the terminal token `INTEGRAL_PAPPUS_DOMINANCE_WEDGE_CHECK_PASS`.

The script enumerates all \(262144\) candidate vertex sets by two separately written face criteria, all \(118562\) nonempty simplices, and all \(900162\) covering incidences of the nonempty face poset. For **each** of two exact deterministic matchings it checks pair uniqueness and exhaustive acyclicity by a complete topological sort. It produces the exact integral oriented Morse boundary matrices: first \(\begin{pmatrix}0&0&-1\\0&0&1\end{pmatrix}\), then the \(1\times2\) zero matrix. The proof of the actual wedge type additionally invokes Forman's Morse CW construction and Hurewicz to infer that the unique attaching map from a nine-cell is nullhomotopic.

The SHA-256 pair digests printed by the program allow comparison of the full matching certificates. This is an exact computation for this finite complex and does not cover other graphs, computational environments, an equivariant action, or scientific originality beyond the inspected sources. Independent mathematical verification has not been performed.
