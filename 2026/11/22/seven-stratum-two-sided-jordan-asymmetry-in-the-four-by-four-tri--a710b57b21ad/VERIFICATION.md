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

# Verification

`check_asymmetry.py` directly assembles the ten-by-ten matrices of left and right multiplication by each nilpotent radical element of the four-by-four upper-triangular matrix algebra. It calculates matrix powers through degree four and recovers nilpotent Jordan block multiplicities using consecutive rank differences. It then compares the actual signed Jordan multiplicity differences to the independent Boolean-support formula and exact seven-stratum multiplicity table, including total mass. Run with `python3 check_asymmetry.py`; the captured output is `check_asymmetry.out`.

The exhaustive checked configurations are every radical element over the prime fields GF(2), GF(3), and GF(5), respectively 64, 729 and 15625 inputs. All checks passed. There is no claim of an exhaustive enumeration over every extension field, every algebra size, or a computer proof of the universal theorem: the explicit principal-block and support-count proof supplies the all-field argument. The only external review recorded here is unperformed.
