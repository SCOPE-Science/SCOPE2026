---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For T>=0 let s=u-T/2 and q=2+i omega. After taking out exp(-qT/2), expand (s+T)^m and use int_0^infty s^j exp(-qs) ds=j!/q^(j+1); this gives m! E_m(qT)/q^(m+1). For T<0 use s=u+T/2 and get the constant gamma integral times exp(qT/2). Neither branch for T<=0 vanishes. The positive branch maps (T,omega) bijectively onto Re z>0 by z=(2+i omega)T with real Jacobian 2T. At a zero the derivative from E_m and the nonzero scalar prefactor multiplies this by a positive squared modulus; E'_m=E_{m-1} and E_m-E_{m-1}=z^m/m! exclude multiple roots. For m<=4 the stated Hurwitz minors are positive (m=0 is constant); the m=5 leading coefficients 1,5,20,60,120,120 give fourth determinant -38400. For m>=6 the third determinant a1 a2 a3-a1^2 a4-a3^2+a1 a5 for descending monic coefficients a_j=(m)_j reduces to -2m^2(m-1)(m-2)(m-5). The strict right-half-plane consequence is valid even with possible imaginary-axis roots: translating z to z+epsilon makes an assumed closed-left-half-plane polynomial strictly Hurwitz, contradicting a negative limiting minor. Positive coefficients exclude positive real roots, yielding conjugate pairs. Independently, /workspace/replay/4_root_disks.py certifies the low-degree signs using exact rational Rouché bounds on five published root disks, and Gauss–Lucas propagates the two base cases. The uploaded checker and recorded output were inspected, not executed. No all-order zero-count claim is made.

## originality

FAIL

The two sign patterns needed for the entire threshold are in Ryoo's published Table 2, degree four and degree five. The table prints approximations; a short exact disk check validates the signs rather than assuming that a table of decimals is a rigorous proof. Together with the classical derivative identity and Gauss–Lucas, those signs give every degree by immediate implication. The cross transform is the elementary binomial Laplace integral and a diffeomorphic change of variables, already exhibited for the first nontrivial order by Gröchenig–Jaming–Malinnikova. Simple roots and the local orientation are direct implications, not independent geometric phenomena. The checked sources do not assert the full pulse-family theorem in this wording, but the claimed cutoff is the mechanical transfer of the published root data. The inaccessible 1972 paper is not the basis of this decision.

## value

FAIL

A meaningful cross-versus-self cutoff could be valuable if it isolated a new phenomenon. Here the only cutoff is the direct right-half-plane rendering of known low-degree root signs propagated by Gauss–Lucas; simplicity and orientation are automatic from the derivative identity and the explicit coordinate map. A nicer exact proof and a certified rendering of the table do not leave an independently valuable distinct claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
