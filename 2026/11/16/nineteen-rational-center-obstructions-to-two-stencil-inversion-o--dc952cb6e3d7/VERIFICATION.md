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

# Reproducibility and verification

The analytic argument is in `RESULT.md` and applies to every \(m,n\ge3\) and every rational \((\alpha,\beta)\). The code `verify_two_stencils.py` checks the *finite* sample grids and is not an infinite proof.

Run `python verify_two_stencils.py` with Python 3.10 or later, SymPy and NumPy installed. It independently uses exact reduction modulo cyclotomic polynomials to classify the rational gains and exact multiplicities for all \(3\le m,n\le14\) (144 grids). It additionally checks all 19 exceptional gains at all \(3\le m,n\le60\) (63,916 floating-point comparisons). The floating tests use a \(10^{-8}\) zero tolerance and are explicitly noncertifying outside these grids.

The checker reports `PASS` on completion. No formal proof assistant, human referee, external certification or independent mathematical audit is claimed. The proof's critical unbounded step is the standard degree formula \(\varphi(q)/2\) for the real subfield of a cyclotomic field, together with enumeration of \(\varphi(q)=4\).
