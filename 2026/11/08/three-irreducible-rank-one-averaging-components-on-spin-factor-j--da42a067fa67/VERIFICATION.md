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

# Verification evidence

The standalone `check_averaging.py` enumerates all nonzero rank-one endomorphisms by unique normalized image lines and all nonzero linear functionals, reconstructs spin-factor multiplication directly, and checks the original averaging identity for all basis pairs. Jordan commutativity makes the second averaging identity identical after exchanging inputs. The checker confirms each of three disjoint count strata and the condition \(P^2=0\). Five configurations are checked: two determinant classes for \(n=3\) over \(\mathbb F_3\) and \(\mathbb F_5\), and \(n=4\) over \(\mathbb F_3\). Output is preserved in `CHECKER_OUTPUT.txt`, ending `SPIN_AVERAGING_DIRECT_ORIGINAL_IDENTITIES_OK`.

Reproduction: run `python3 check_averaging.py` from a directory containing that file, with Python 3 only. The code is finite-field prime arithmetic and makes no claims about extension fields or infinite-dimensional instances. The full proof separately treats all fields of characteristic other than two, and the finite-field count uses a standard quadratic Gauss-sum calculation. The geometric statement concerns the **reduced** solution variety, not scheme-theoretic reducedness of the raw averaging equations.
