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

# Reproducibility and limits

Run `python3 verify.py` and `python3 check_modular.py` with Python 3 standard library. The accompanying `verify_output.txt` and `check_modular_output.txt` are actual recorded output from running these source files in the same directory.

`verify.py` independently enumerates all \(1545\) nonempty faces at \(p=5\) and all \(130921\) nonempty faces at \(p=7\). It checks the sizes of all dimensions, the translation-invariant faces, that the invariant facets are exactly \(F_a=\{(i,i+a)\}\), and local representation weights. The Euler characteristics of the geometric quotients are \(-7\) and \(-23\), respectively, by the fixed-point formula.

`check_modular.py` constructs the actual orbit chains of the barycentric subdivision for \(p=5\), preserving ordered face-flags, and builds every boundary in dimensions one through three. Counts are \((313,3200,8640,8640)\) for quotient cells through dimension three. Over \(\mathbb F_2\) it finds boundary ranks \((312,2888,5752)\); over \(\mathbb F_3\) ranks \((312,2888,5751)\); over \(\mathbb F_5\) ranks \((312,2888,5748)\). Consequently \(H_1=0\) over each field, and the dimension of \(H_2\) is respectively \(0,1,4\). This independently checks the prime-specific low-dimensional conclusion.

Neither finite experiment independently establishes the universal formula. That follows from the proof with established connectivity and integral homology for ordinary chessboard complexes, plus the exact local lens-space structure and standard homotopical/algebraic-topological sequences. In particular the mod-\(p\) calculations alone do not distinguish exponent \(p\) from higher \(p\)-powers; the Mayer–Vietoris exact sequence does.

Independent external validation has not been performed.
