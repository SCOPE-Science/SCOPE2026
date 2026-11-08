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

# Exact verification

Run `python3 verify.py` (Python 3.9+). No external packages or data are required. The checker fully enumerates all \(2^{20}=1,048,576\) vertex subsets by common-neighbor intersection and independently enumerates unions of neighborhood-subset families; both yield 8,621 faces including the empty face. It constructs 4,238 Morse pairs, checks each of 41,940 signed Hasse incidences, and verifies acyclicity by an exhaustive directed topological sort.

The signed integer recursion for degree-2 Morse weights is evaluated on the whole finite complex and gives 95 zeros, 30 coefficients \(+2\), 17 coefficients \(-2\), and gcd \(2\). An explicit coefficient \(+2\) occurs for the critical 3-cell with face mask 8707. Exact unreduced mod-two simplicial boundary ranks in dimensions 1 through 8 are \((19,161,798,1400,1120,560,160,20)\), consistent with the universal coefficient theorem. The included `verification_output.txt` was produced by running the included verifier. The result proves the complete nonequivariant homotopy type of this one finite complex; it does not establish a general family claim or replace independent external validation.
