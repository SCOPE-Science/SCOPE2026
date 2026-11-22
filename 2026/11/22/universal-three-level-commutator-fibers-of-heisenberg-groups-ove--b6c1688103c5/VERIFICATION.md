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

# Verification notes

The theorem is proved from direct Heisenberg multiplication, additive-character orthogonality, the three cardinalities of the character annihilator ideals, and explicit finite character sums. These steps apply to every finite commutative local ring \(R\) with \(\mathfrak m^2=0\) and \(\dim_{R/\mathfrak m}\mathfrak m\ge2\), irrespective of a coefficient-field splitting.

`check.py` is a standalone standard-library Python 3 script. Reproduce by executing `python3 check.py` from the directory containing the embedded files. It exhaustively enumerates the rank-one horizontal commutator map for seven finite ring models, including a mixed-characteristic ring; all target counts are compared with the three formulas. It checks larger symplectic ranks two and three using exact convolution of the independently enumerated rank-one distribution. An additional full enumeration over the principal ring \(\mathbb Z/8\mathbb Z\) checks the distinct four-level comparator and zero-determinant count \(736\). The expected final line is `PASS: all exhaustive tests and convolution comparisons`, recorded in `check_output.txt`. The largest exhaustive test considers \(531441\) quadruples over a ring of cardinality \(27\). Finite computations corroborate, rather than prove, the unbounded mathematical theorem.

Further internal consistency checks are: the three target strata partition the coefficient ring, the strictly positive fiber sizes sum with their multiplicities to \(t^{4h}\), the central-coordinate factor is \(t^2\), and the zero-target probability equals the displayed conditional-concentration formula. No higher-radical, nonlocal, or noncommutative coefficient-ring theorem follows. No independent audit or certified global literature-priority validation was performed.
