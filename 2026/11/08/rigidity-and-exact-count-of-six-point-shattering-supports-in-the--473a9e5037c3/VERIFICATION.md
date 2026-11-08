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

# Reproduction of exact finite checks

Run `python3 verify.py` from this directory. The script constructs the Boolean hit trace for all \(286\) three-subset query centers, enumerates all \(462\) six-edge multisets from the six possible edges on a four-point residual core, and checks that exactly four pass all \(64\) trace requirements. Each passing case has the three two-fold spokes and therefore is a hub relabeling of the asserted unique orbit. It also checks the \(28\) possible three-core multisets at ambient size twelve.

Run `python3 independent_check.py` from this directory. It derives a different, purely Boolean cover-mask criterion and independently reproduces the \(462\)-case census and its four passing cases, including the exact count. Both checks have no third-party dependencies. The main proof has independent structural arguments applying directly to arbitrary candidate support at the fixed ambient order, so the programs are corroborative rather than sources of an extrapolated general theorem.

The proof does not claim publication priority, a result for ground-set orders other than thirteen, an external audit, or independent scientific certification.
