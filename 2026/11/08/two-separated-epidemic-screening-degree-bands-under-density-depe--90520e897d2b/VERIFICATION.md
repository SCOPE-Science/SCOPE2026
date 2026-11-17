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

Differentiate R(u)=a u^s/[mu+b u^t(1-cu^-d)] using s+t=1. The sign is mu+b(1-alpha)u^t-b c[1-alpha+d(1+alpha)]u^(t-d). For alpha<=1 it increases and cannot create a local maximum. For alpha>1 rewrite as mu/b-G; G has a unique minimum at uc because u^(d-t+1)Gprime=(alpha-1)t u^d-cH(d-t). This proves exactly two zero crossings iff the endpoint/minimum inequalities hold. Positivity of denominator follows c k0^-d<1. Exact rational cube-root enclosures from inspected checker.py certify all 18 integer scores and return-normalizer c=10838475198270720/3751881733704241; independently recalculated c and the 10 passing degrees. An unstable diagonal is sufficient for the Metzler block; the theorem does not assert an exact patch reproduction number.

## originality

PASS

Ripoll–Avinyó–Pellicer–Saldaña (2015) already derives the very score and condition (9); this is not a new epidemic model nor threshold. Inspection of its actual full paper, equations and figure 3, found examples of monotonic and one-peaked scores, not this sharp two-extrema criterion or a strict disconnected integer-degree witness. Resultary search found no implication-equivalent classification; no absolute priority assertion.

## value

PASS

Counterexample and necessary-and-sufficient calculus classification expose a structurally important failure of one-band intuition for a natural, previously published sufficient-invasion screen. The finite witness is exactly realized by positive model parameters with rational margins, not an arbitrary unmotivated parameter slice; the screen/outbreak distinction is explicitly maintained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
