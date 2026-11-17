---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Every candidate occurs on exactly two approvals, so fixed-size-k welfare is identically 2k and no strict Pareto improvement exists. Distinct voter ballots intersect in at most one candidate, making EJR=JR; for k≥n/2 JR is exactly absence of cyclic triple missing candidates (k<n/2 JR vacuous). Any deviating candidate set T consists of runs: a JR committee permits at most r improving touched voters for run lengths 1,2, and at most r+1≤4r/3 for r≥3; hence |I_W(T)|≤4|T|/3. For k<3n/4, Hare affordability is impossible; with ≤3 missing candidates at most one voter is unrepresented and the endpoint double-improvement needed to exceed |T| is impossible, hence near-full JR committees are also core. For n≥16, ceil(3n/4)≤k≤n-4, construct missing positions {0,1,3,4} plus {7+3j:0≤j≤n-k-5}, with no cyclic three consecutive missing. The T={1,2,3} deviation improves exactly voters1–4 and 4k≥3n. Independently checked the first witness n=16,k=12 in integer arithmetic; the proof, not finite scans, establishes all n,k.

## originality

PASS

Becker–Greger–Peters 2026 prove existence of core/core+ committees for every approval election, not universal core membership of EJR committees; Pierczyński–Skowron restricted-domain results likewise address existence. The assigned result is a sharp *existence of noncore fair committee* threshold on cyclic two-approval ballots. Related Resultary interval and two-ballot findings concern different graph topologies/fairness. PASS best of knowledge; unindexed cycle-specific core analyses remain a risk.

## value

PASS

Provides a sharp, natural separation boundary between representation and coalition stability on minimal-degree cyclic approval profiles, including the smallest positive witness and the full phase diagram. Core-existence results do not answer when a given EJR committee may be blocked.

The dated certificate retains the supplied scientific assessment, sources and limitations.
