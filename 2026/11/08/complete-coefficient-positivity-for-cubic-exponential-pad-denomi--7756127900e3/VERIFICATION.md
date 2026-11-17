---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The standard exponential [k/3] denominator with t=k+1 is 1-3z/(t+2)+3z²/[(t+1)(t+2)]-z³/[t(t+1)(t+2)]. Translation z=t+x gives t(t+1)(t+2)q(t+x)=2t-3tx-x³. The strictly increasing cubic x³+3tx=2t has u between 1/2 and 2/3; the roots R=t+u and Z=t-u/2+i sqrt(3t+3u²/4), conjugate Z, are simple. Their moduli obey |Z|²-R²=3t(1-u)>0. The partial-fraction coefficient of (1-z/R)^-1 is A=|Z|²/|R-Z|²>0, while the sum of two complex residue moduli is 2|B|=R|Z|/[v|R-Z|]. Exact symbolic factoring reduces A>2|B| to the positive cubic u³-4u²+10u-4 on (1/2,2/3), with positive multiplier 9u⁴(1-u)/[4(2-3u)²]. The n-th coefficient is at least R^-n(A-2|B|)>0 for all k,n. SymPy checked both factorizations exactly; independent rational recurrence checked k<=80,n<=100. No numerical cutoff is used to establish the all-order result.

## originality

PASS

Fasi–Higham 2019 pose positivity for all odd m, without proving even this fixed cubic case. The full 2026 Scardino arXiv text proves full positivity for k=0 at arbitrary odd m and eventual positivity for general k under spectral minimality, but no theorem of all-index positivity for every k at m=3. The present uniform real-residue domination is an additional quantified all-k/all-n result; it is not the already-known partial-fraction identity.

## value

PASS

Closes a natural smallest nontrivial unresolved odd-denominator case of an explicitly motivated numerical-linear-algebra conjecture, despite the known general failure at degree five. Uniform all-index strict inequality over arbitrary numerator order is a substantive sharp positive region, not just finite positive checks, and the strict gap identifies a robust analytic mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
