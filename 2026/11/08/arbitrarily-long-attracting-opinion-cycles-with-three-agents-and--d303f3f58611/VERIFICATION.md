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

# Reproduction and limits

Run `python3 verify.py` with the Python standard library. It uses exact fractions, not floating-point arithmetic. The output was `VERIFY_OK: 199 exact prime periods p=2,...,200; trust margins and return multipliers`.

For every tested period the checker confirms that the seven-or-fewer open confidence bands are separated, each intended orbit node has exactly its selected anchor neighbor, the rational orbit closes with no repeated point before the prescribed period, and every relevant membership expression stays at least \(1/(4q)\) from a band boundary. The return is a product of \(p\) affine maps of slope \(1/2\), so its derivative is \(2^{-p}\).

These 199 instances are reproducibility tests only. The all-integer theorem follows from the even/odd separation argument and the affine exact identities in RESULT.md. The test does not cover global basins, arbitrary fixed confidence sets or external publication priority. Independent external validation was not performed.
