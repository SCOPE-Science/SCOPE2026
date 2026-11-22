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

The prey equations of a positive prime-2 orbit force 0<a<b<1 and give uniquely positive v1=(1+ca)(2-a-b/a) and v2=(1+cb)(2-b-a/b). Their exact difference is (b-a)[a+b-ab+abc(3-a-b)]/(ab)>0. Thus predator multiplier R(a)=k>1 and R(b)=1/k<1 force q=theta/beta>[(1+ca)(1+cb)]^-1>(1+c)^-2; R(a)>1,r>0 force q<(1+ca)^-1<1. For every interior q pick z=1+ca in (q^-1/2, min(1+c,q^-1)), then sufficiently close b>a; beta=(k-k^-1)/((b-a)(q-[(1+ca)(1+cb)]^-1))>0 and r=1-k+a beta((1+ca)^-1-q)>0 as b->a. All four orbit equations follow exactly; boundary strictness is proved. A rational witness at c=1,q=1/2 was independently checked.

## originality

PASS

Shoyimardonov 2022/2023 treats equilibria, stability and Neimark–Sacker in this discrete Holling-II toxic plankton map, not an identified necessary-and-sufficient existential parameter-fiber window for strictly positive primitive 2-cycles. A published linear-response plankton no-2-cycle theorem has a different predator multiplier. The potentially close Khan–Alayachi 2022 paper includes periodic points in abstract, but its full equation-specific text was inaccessible (Oxford institutional VPN disconnected). A named material uncertainty remains, not automatic FAIL; the exact constructive feasibility interval survives best-of-knowledge review.

## value

PASS

Determines the complete strict toxin-to-conversion feasibility region for positive prime-two coexistence in a natural saturating/toxic plankton map; proves impossibility outside it for every choice of remaining parameters and constructs examples for every interior ratio. Both exact strict endpoints and positivity constraints are motivated biological/dynamical barriers, not just a finite trial or local bifurcation heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
