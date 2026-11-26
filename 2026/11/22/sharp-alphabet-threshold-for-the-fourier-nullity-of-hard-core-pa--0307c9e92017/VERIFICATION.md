---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Unnormalized convolution on all of H^n diagonalizes in the character basis. Orthogonality at a supported site gives q−1 or −1, so the multiplier is the path independent-set sum with P_i=P_(i−1)+a_i P_(i−2), P_0=P_(−1)=1. Reducing all activities modulo q gives the 6-periodic sequence 1,0,−1,−1,0,1 starting at i=0. The nonzero residues ±1 exclude zeros off n≡1 mod 3 without requiring q prime. For n=3k+1 use an indeterminate Q in place of q. The constant term vanishes; differentiating in each trivial-coordinate activity at all activities −1 splits the occupied-site weight into segments j−2 and n−j−1. The product is zero unless j≡1 mod 3, where it is (−1)^k, including empty end segments. Thus a zero at q requires q|t for the number t of trivial designated sites. At q≥k+2 this forces t=0. Conversely specified activities −1 at the designated sites propagate P_1=0 to every P_(3h+1), regardless of the two intervening activities. Counting character choices gives nullity q^(2k)(q−1)^(k+1) and the stated rank and fraction (also valid at k=0).

## originality

PASS

The binary signed recurrence, its six-cycle and the related binary invertibility residue already appear in prior catalogue work. The supported distinct result is the sharp higher-alphabet classification of the kernel in the singular residue, including the explicit extra-zero boundary witnesses. The checked partition-function and graph papers do not give that classification.

## value

PASS

A full kernel characterization for all abelian alphabet structures of a given order determines exactly which Fourier modes are lost. The sharp boundary separates structural zeros from additional arithmetic cancellations and explains a nonvanishing limiting fraction of lost modes at threshold. This is more informative than an isolated determinant evaluation or a recurrence reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
