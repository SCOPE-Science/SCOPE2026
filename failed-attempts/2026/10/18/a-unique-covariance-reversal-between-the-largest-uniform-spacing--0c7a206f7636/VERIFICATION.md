---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Finding is correct. The translated conditional simplex gives the exact covariance m(1-t)^m[B_m(b)-b H_m/m], with B_m(b)=E[(b-(M-Y_1))_+]. The labeled-coordinate joint event has volume (1-kb)_+^(m-1)/(k+1), including dimension two by direct one-coordinate integration on the nonempty interval. Inclusion–exclusion and integration give the displayed finite formula. B_m(b)/b increases strictly from 1/m to 1, since there is positive mass of M-Y_1 in every (0,b), and H_m/m lies strictly between. At t=1/2 the conditional mean is (m+1)/(2m), equal to H_m/m only at m=2 and larger thereafter, giving the claimed endpoint comparison. Under exponential normalization, the exact unnormalized gap law is e^v[1-(1-e^-v)^m]/m. Concentration of the sum gives uniform relative asymptotics e^v/m up to C log log m without needing independence of gap and sum. Integration and the two-sided bracket give s=mb_m asymptotic to log log m, then e^s-1=(1+o(1))sH_m gives the second log and additive o(1); replacing b_m by t_m costs o(1) on the scaled threshold. The adjacent wording about piecewise polynomials is imprecise: B_m is piecewise polynomial in b, whereas the covariance itself is piecewise polynomial in t and piecewise rational in b. Independent finite replay: python3 /workspace/check_frozen_mathematics.py 2, with 234 exact rational comparisons to a joint-tail inclusion–exclusion integral for m=2 through 14. This does not certify uniqueness or the asymptotic; those follow analytically.

## originality

FAIL

A distinct published Resultary record (ce8f3c1a316a) covers the full covariance sign theorem, including the m=2 boundary, the exact finite formula and the second logarithm with additive o(1). Two other distinct records corroborate partial or full exact coverage. This is a statement-level duplication decision, not an attribution of priority or an inference from folder dates. No distinct supported finding remains by correcting the polynomial wording or rewriting the derivation.

## value

PASS

As mathematics, the all-m crossing and additive o(1) threshold expansion answer a natural question about competition between a simplex maximum and a threshold count, and locate the transition far below the typical maximum. That significance is not new scientific value added by this record: the available exact coverage forces rejection on originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
