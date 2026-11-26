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

The two critical-contact cubic equations follow by clearing 4p^2 from h(p)=p and h(p)=1-p. Each polynomial has opposite signs at 1/4 and 1/2 and a strictly signed derivative on this interval. The turns map first to 1 or to the specified outer turn, then to the endpoint orbit 1,0,0. Each outer branch covers [0,1]; the two inner branches cover [p,1] or [1-p,1]. Positive-length Markov cylinders are in bijection with paths: a new interior boundary is a turn pulled back through a strictly monotone piece. Old folds cannot disappear under further composition, since close to a fold the image on both sides lies in the same one-sided neighborhood, on which f is strictly monotone. Thus these cylinders count exactly the maximal laps. On vectors constant on the outer and inner branch pairs, the two transition matrices act by [[2,2],[1,2]] and [[2,2],[1,0]], respectively. The all-ones vector lies in this subspace, so these two-dimensional characteristic polynomials give the stated recurrences from n=1 (the full four-dimensional characteristic polynomial alone would not justify cancellation of its z^2 factor). L_1=4 and L_2=14 or 10 give nonzero positive coefficients for the dominant roots. The lap-growth theorem yields the claimed topological entropies.

## originality

FAIL

The distinct, earlier-dated Resultary result a68222704328 explicitly contains both of the frozen parameters and their exact transition matrices, lap recurrences and entropies. It is not merely a paper about the family or a general entropy theorem. Earlier catalogue date alone does not settle public priority; the explicit statement-level coverage settles the scientific overlap.

## value

FAIL

Exact entropy at a naturally defined critical contact could be useful as a calibration of the dynamics; the contacts are not arbitrary parameters. But the frozen finding supplies no new calibration point, sharper invariant, or new structural explanation beyond the earlier five-case classification. It repeats precisely two already-derived cases, so no independently valuable remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
