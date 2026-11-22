---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For xi=(s,d,-s,d), g^n(xi) has trace coordinates (U_n,V_n)=(S_n,-S_n) at d=0 where S_n=s^(2^n); determinant coordinates equal d^(2^n). Thus F_n=phi(g^n(xi))=S_n²(2-S_n), and at S_n=2 its s derivative is -2^(n+3)/s_n0, nonzero, granting a unique local analytic branch by IFT. Differentiating the trace renormalization gives A_1=B_1=-2; A_(n+1)=-2S_n B_n, B_(n+1)=S_n(B_n-A_n). Normalization yields 2x2 constant recursion with eigenvalues 2 and -1, giving the parity coefficient s_n´(0)=-(1+(-1)^n 2^(1-n))/(3 s_n0). At n1 direct explicit radical differentiation yields Hdd=12, Hs=-8sqrt2 and H_d=0, so quadratic coefficient +3sqrt2/8. The fixed-depth component side assignment follows the earlier component theorem under strict nearby F_(n-1)>0 and F_(n+1)<0. Independently verified exact sympy Hdd,Hs,Hd and normalized derivatives through sample depths; finite root calculations not used as proof of all n.

## originality

PASS

Ghosh-Simpson already define implicit renormalized crisis surfaces and component regions. The new contribution is the explicit all-depth closed first derivative and exceptional vanishing and second derivative on the symmetric Lozi slice. These quantitative coefficients are not direct text of the cited implicit theorem, although elementary differentiation from published formulas creates a genuine possible low-step novelty/value concern.

## value

PASS

The first crisis boundary has an exceptional quadratic rightward shift while every deeper boundary has a leftward linear shift with an alternating renormalization-depth correction. This concrete tangency-versus-transversality distinction sharpens the bifurcation geometry and is directly useful for local parameter prediction; it is not solely a finite numerical root table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
