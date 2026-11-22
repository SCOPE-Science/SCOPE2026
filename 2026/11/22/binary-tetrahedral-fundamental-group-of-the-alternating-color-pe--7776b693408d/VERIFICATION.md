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

# Computational verification

The standalone `verify.py` enumerates all \(2160\) product-of-simplex cells of \(\operatorname{Hom}(C_5,K_4)\), the \(12\) even palette permutations, and the free cell orbits. It finds quotient cell counts \((20,65,70,25)\) and computes the cellular boundary matrices in degrees \(1,2,3\) using the product-simplex signs together with the orientations induced by orbit-representative relabelings.

The program verifies both integral boundary-square identities and the exact Smith invariant factors \((1^{19};1^{45},3;1^{24})\). This establishes \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z/3\mathbb Z\), \(H_2=0\), and \(H_3\cong\mathbb Z\). The printed transcript in `verification_output.txt` is included, but the executable proof witness is the source `verify.py` and its deterministic exhaustive enumeration and exact integer algebra, not the transcript alone.

Reproduce with `python3 verify.py` using Python 3 and SymPy (its `Matrix` and `smith_normal_form` functions). The separate group-extension proof requires the external, previously established homeomorphism \(\operatorname{Hom}(C_5,K_4)\cong\mathbb{RP}^3\) and standard elementary group theory. Computations do not independently reprove that cited homeomorphism or certify novelty.
