---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For every phase-indexed periodic binary word (including n=1,2,3), local x_i=x_{i+1} or x_i=x_{i+3} excludes exactly 0101,0111,1000,1010. At each run ending, the next run must have length <=2 and two neighboring singleton runs cannot occur; the converse checks each run end. The 8-state order-three transfer graph has trace A^n=N_n, and removing the two constant fixed cycles splits its six-state component into complementary 3x3 blocks with characteristic polynomials lambda^3-lambda-1 and lambda^3+lambda-1. Log-det produces the exact stated dynamical zeta and recurrences. The strongly connected component has coprime cycle lengths 3,4, yielding entropy log plastic constant; Mobius inversion gives primitive orbit census. Independently enumerated all 16,382 phase-indexed words lengths 1..13 and independently computed trace counts 2,2,8,6,2,8,16,6,8,32,24,12,54. No enumeration proves the all-n transfer identity.

## originality

PASS

Best-of-knowledge original evaluated claim after statement/implication comparison with cited literature; see four checks and residual risks. No negative search is taken as priority proof.

## value

PASS

The fixed shifts (1,3) define a natural small pseudoperiodicity class; the complete cyclic-run restriction, exact every-n orbit data, entropy and zeta constitute a coherent exact classification, not an unmotivated tiny numerical table. Standard SFT methods are used transparently, while the non-obvious explicit polynomial factorization and cyclic rule are the concrete mathematical information a researcher can reuse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
