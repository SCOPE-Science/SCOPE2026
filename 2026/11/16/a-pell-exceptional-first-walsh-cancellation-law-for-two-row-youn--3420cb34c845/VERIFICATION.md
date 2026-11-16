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
# Verification and limits

Run `python3 check_young.py`. It compares the signed-prefix transfer and analytic low-support counts against an independent full integer Walsh transform for widths one through nine, checks the transfer mass, and verifies the first Pell widths through width 150. Run `c++ -O2 -std=c++17 check_direct.cpp -o check_direct && ./check_direct` for independent full integer Walsh transforms through width ten, including Parseval checks.

The complete transform enumerates a finite frequency space; the all-width claims instead follow from the explicit algebraic proof. The transfer recurrence gives exact finite nullities for each input width but does not establish a limiting density or any asymptotic rate. The referenced published mathematical records are compared for implication with the stated theorem, not treated as an exhaustive historical priority certificate.
