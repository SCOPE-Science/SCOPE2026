---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 3rd-root binomial filter gives |S|=(M+t_k)/3, coordinate means b=u_k/M and pair means c=-t_k/M, so Gram=[[a,b 1^T],[b1,(a-c)I+c11^T]]. For regular residues |t_k|=|u_k|=1, this is scalar plus one rank-one correction, with eigenvalues (M+4t)/(3M) multiplicity n and (M+(1-3n)t)/(3M) multiplicity one. Exceptional residues b=0 yield a, a-c, and a+(n-1)c. Direct parity-specific cross-multiplication establishes positivity and strict regular-versus-exceptional condition ratios for n>=5; square-root expansion yields 1+3(n+1)/2^(n+1)+O(n²4^-n). Independent full cube enumeration of all masks and Gram entries n=5,6,7,8 confirms exact spectra and two-residue optimizer ties. General claim follows from the algebra, not four sample dimensions.

## originality

FAIL

A published same-mask **degree-at-most-two** Walsh theorem gives exact Fourier moments m_j and the full coefficient Gram matrix G[I,J]=m_|I△J| for every |I|,|J|<=2, covering all constant and degree-one indices. Its exact n,r moments imply the present entries after multiplying by |S|/2^n: a=D/(3M), b=a*m1=u_k/M, c=a*m2=-t_k/M. Thus the entire present first-band Gram is a principal submatrix of the prior fully known matrix. The rank-one diagonalization and finite residue-choice inequality are routine consequences of those entries, not an independently original new spectral invariant or substantive classification. Strict finite optimizer is not stated verbatim in earlier quadratic theorem, but follows from its more general explicit moment law and elementary arithmetic; failing to quote the same numbers is not enough for novelty.

## value

FAIL

The proposed conditioning numbers are mathematically meaningful deterministic sampling diagnostics, but the degree-one instance is a straightforward specialization of the published larger-band exact Gram-moment theorem and a rank-one matrix calculation. With its complete math already entailed by known formulas, the submitted theorem does not constitute a distinct valuable unknown invariant under the originality/value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
