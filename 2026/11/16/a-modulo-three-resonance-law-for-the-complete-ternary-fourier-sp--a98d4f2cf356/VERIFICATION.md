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

Run `python3 verify_colours.py` and `python3 verify_transfer.py` in the directory containing these files. Both use only the Python standard library and exact integers.

- `verify_colours.py` enumerates all proper three-colourings of each cycle with \(3\le n\le7\), forms every ternary character coefficient as a pair of Eisenstein integers, and compares all \(\sum_{j=3}^{7}3^j=3279\) coefficients with the theorem's formula.
- `verify_transfer.py` independently computes the trace of site-weighted adjacency transfer matrices using exponent-residue triples rather than enumerating colourings and compares the same coefficients.
- Both check the resonance multiplicity and rank, including \((n,Z_n,\operatorname{rank})=(4,12,15)\) and \((7,210,519)\).

These are finite checks only. The all-order theorem rests on the self-contained edge-increment and signed-powers proof in `RESULT.md`. No external proof certification, Lean proof, or independent mathematical audit is claimed.
