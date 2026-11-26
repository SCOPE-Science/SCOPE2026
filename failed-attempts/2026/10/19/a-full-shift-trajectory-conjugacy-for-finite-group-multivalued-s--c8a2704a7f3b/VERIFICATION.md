---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Freeness on letters uniquely recovers the branch h_t from x^(t)_1 and x^(t+1)_0. The first letter at time j is (h_(j-1)…h_0) applied to the j-th initial letter. Arbitrary first letters and labels reconstruct the initial word by inverse prefix products, then the whole trajectory by the ordered recurrence. Each input/output coordinate requires only finitely many coordinates, and advancing time shifts the code. The product order needs no commutativity. Repeated words give q^n fixed trajectories, cylinder counts give log q, the formal exponential series gives (1-qt)^(-1), and Möbius inversion followed by division by least period gives the primitive orbit count. The proof includes q=1 and does not confuse fixed full trajectories with multivalued periodic states.

## originality

FAIL

A distinct Resultary record already covers the decisive stronger trajectory-lifting relation. Its proof explicitly says that every lift sequence of a quotient orbit is an actual trajectory, because the next orbit fibre is the full image. The frozen conjugacy follows directly by writing the free alphabet as B×H, coding the quotient shift by orbit letters and successive group differences, and recording one freely chosen fibre coordinate per time. This proves coverage by implication; the other result is not claimed to print the same conjugacy formula or to have priority.

## value

FAIL

Distinguishing trajectory invariants from periodic-state invariants is useful and the gauge is a clean exposition. As a distinct mathematical contribution, however, the entire finding is a routine full-shift recoding of the already established unrestricted lift relation. The entropy, zeta and orbit counts are standard consequences and leave no separately needed case or obstruction in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
