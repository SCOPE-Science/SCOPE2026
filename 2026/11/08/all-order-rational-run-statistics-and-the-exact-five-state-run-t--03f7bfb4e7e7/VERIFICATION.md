---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Taking the externally established half-scaled rational-base parity difference identity y_{9k..9k+8}=(0,1,y_{4k},0,y_{4k+1},1,0,y_{4k+2},y_{4k+3}), the regular Toeplitz 9-pattern has holes 2,4,7,8. At scale m at most (4/9)^m unspecified positions; since gcd(4,9^m)=1 the same density bound holds on the needed 4k+c progressions. Every factor frequency exists, and the nine-residue recurrence reduces length >=3 factors to shorter ones, with F(1)=2/5 and base pairs F(00)=F(01)=F(10)=3/10, F(11)=1/10. Run tuples correspond exactly to boundary words 1 0^(a1-1) 1 ... and conditional frequency (5/2)F(boundary word). This gives rational all-pattern recursion; exact rational recomputation verified every entry of the /108 matrix and 120000 direct reconstructed Toeplitz symbols. The existence of Toeplitz premise is sourced, not claimed proved ab initio by finite prefix.

## originality

PASS

PASS with qualification: Cassaigne–Espinoza–Rigo–Stipulanti (2026) already prove the Toeplitz structure, unique ergodicity/all-factor-frequency existence and single-symbol frequencies of the difference word. The assessed new content is the explicit terminating rational recursion for EVERY successive run-length tuple and the exact five-by-five adjacent-run transition matrix, not discovery of the Toeplitz word, existence of its frequencies or rationality of a particular single-letter statistic. Other published run-length matrices concern different automatic words.

## value

PASS

PASS: the joint five-state run-length transition law is a precise natural invariant measuring dependence beyond marginals, including eight forbidden transitions; all-pattern rational recurrence gives reusable finite output for arbitrarily long run tuples. This is motivated by the known rational-base automatic word, not an arbitrary slice or unproved general claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
