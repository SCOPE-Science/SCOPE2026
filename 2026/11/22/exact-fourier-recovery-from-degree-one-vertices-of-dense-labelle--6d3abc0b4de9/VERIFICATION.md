---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For any forced set J, its internal edges form a matching; every unmatched vertex in J independently chooses an outside neighbor (choices may coincide), and outside edges are arbitrary. Expanding the product of 1−2 times the degree-one indicators gives the probability-normalized Walsh formula, including J empty and J=[n]. Independent replay /workspace/replay/audit_3.py, run with Python 3, counts graphs by extending the joint degree-zero/degree-one bitsets one vertex at a time and directly sums the profile characters. All weight vectors through n=8 agree, including exactly rank two at 2 and 3, minima at weights 2,3 for n=4 and weight 4 for n=5, and strict decrease for n=6,7,8. Read the binomial multiplicity as the contribution of a weight layer; equal eigenvalues from different layers have summed multiplicity, as in the stated ten at n=4. For n≥8, twice the expected number of leaves bounds the eigenvalue deficit and is below one. For n≥9, conditional on a specified vertex being a leaf, the probability of any second specified leaf is [1+(n−2)^2]/[(n−1)2^(n−2)], separating the cases where the first leaf does or does not choose the second. The consecutive spectral difference is twice the first leaf probability times a conditional parity expectation bounded below by 1−2(n−1)q_n>0; the subtracted quantity is 100/128 at nine and decreasing. The maximum eigenvalue is one, and the n≥9 reciprocal bound is at most 16/7, so eight is attained only at n=4. At weight n the difference between odd-count probability and mean count is bounded by twice the second factorial binomial moment; that moment and the squared first moment are both O(n^4/4^n), proving the reciprocal expansion. The finite replay is not used as an all-order certificate.

## originality

PASS

The checked count/concentration papers and related profile convolutions do not cover the all-order positive spectrum, extremal weights and sharp conditioning of the labeled degree-one set in unconditioned simple G(n,1/2). Common methods and the coincident small-order singularity pattern are not credited as new.

## value

PASS

The profile is a natural label-sensitive graph statistic. The collapse at n=2,3 does not anticipate the exact recovery threshold at n=4, the two exceptional minimum-weight layers, or the global change to a unique least-stable all-vertex mode. The exact sharp uniform stability and the decay of the conditioning deficit answer substantive recovery questions beyond the elementary expectation that degree-one vertices become rare.

The dated certificate retains the supplied scientific assessment, sources and limitations.
