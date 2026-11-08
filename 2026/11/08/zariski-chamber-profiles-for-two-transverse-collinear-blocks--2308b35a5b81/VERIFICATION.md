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
# Verification of the two-line chamber enumerator

The proof in `RESULT.md` applies for all \(n,m\ge3\). The finite arithmetic checks below test independently computed exact intersection matrices and all their negative-definite principal supports for \((3,3)\) and \((3,4)\).

Compile and run in a directory containing the standalone files:

```sh
c++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

The output must equal `verification_output.txt`, including its final `ALL_CHECKS_PASSED` line. The program enumerates each binary mask of all negative curves (\(17\) curves at \((3,3)\), \(21\) at \((3,4)\)), computes every chosen intersection matrix independently, and tests strict negative definiteness with exact integer Bareiss elimination. A separate binomial combinatorial program path derives the predicted four marked profiles and compares every coefficient. Integer divisibility/overflow checks are fatal, not silently ignored. The exhaustive finite check does not replace the general Bézout/adjunction and Schur-complement proof, and it is not an independent scientific audit.
