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

# Verification of the retraction enumerator

The code `verify.py` implements the parameterized maps directly on residue classes and separately computes the generating polynomial from the displayed formulas. Its assertions compare the observed multisets of image cardinalities, the exact number of idempotent maps, and their pointwise composition law. For moduli at most \(25\), it additionally tests each generated map's multiplicativity for every ordered pair of residues.

Run `python verify.py` with Python 3.10 or later. Compare its stdout to `verification_output.txt`. The checked cases are \((p,e)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2)\). All six passed and \(9560\) ordered pairs underwent direct multiplication checks. No external libraries, external computational services, or third-party datasets are required. The checked finite ranges do not prove the general theorem; the symbolic argument in `RESULT.md` does.

The finite computation does not exhaust arbitrary monoid endomorphisms independently of the proved parametrization. It enumerates all endomorphisms allowed by the normal form, checks their retraction property on the full finite residue set, and compares the results with the separate arithmetic polynomial calculation.
