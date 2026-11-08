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

# Verification record

The scientific claim concerns all \(p,m,\varphi,q\) with \(p\mid(q-1)\). Its proof is the Fourier-support argument in RESULT.md. The finite checks are corroboration, not an infinite proof.

The standalone `check_joint_ranks.py` generates all coefficient vectors in the algebra basis for eight binary Alexander quandles over \(\mathbb F_3\). It computes the original basis multiplication table, builds the left and right multiplication matrices, determines their ranks by exact Gaussian elimination modulo three, and compares the complete bivariate rank count with the closed theorem formula. It does not rely on Fourier coordinates for its observed ranks.

The recorded `check_joint_ranks.out` gives 33,048 coefficient vectors and 66,096 operator-rank calculations, with no discrepancy. Of particular importance, the three-dimensional binary unipotent example and its semisimple comparator both have \(h=2\) but respectively have \(d=1\) and \(d=0\), with coefficients \([X^1Y^1]=8\) and \(24\).

Run using a standard Python 3 interpreter from the artifact directory: `python3 check_joint_ranks.py`. No external libraries, network access, or environment-specific data are needed. The checker is finite, and neither untested primes nor extensions of the coefficient field are claimed to have been exhaustively enumerated.
