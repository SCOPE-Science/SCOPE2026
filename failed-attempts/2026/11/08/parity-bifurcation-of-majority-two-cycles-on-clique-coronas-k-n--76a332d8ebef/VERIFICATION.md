---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For clique corona K_n with one private pendant leaf at each core vertex, n>=2, every new leaf bit equals the old hub bit. For a core state a, old leaf state b, hub i sees |a|-a_i+b_i ones among n neighbors. Even n collapses hub update to 0,b,1 according as |a| is below, at or above n/2; immediate periodic configurations are exactly ordered balanced core/leaf pairs, plus the two unanimities. Odd n four local pair-type inequalities imply that nonfixed immediate 2-cycles fall into exactly three disjoint families (one stationary 00 or 11 coordinate and r flips of each type; or all coordinates flip with weights r,r+1), giving P2=2n binom(n-1,r)+2binom(n,r). The symmetric threshold energy gives no eventual period greater than two. Independent full labelled enumeration at n=2..7 matched all P1,P2, corroborating the general proof.

## originality

FAIL

The October 25 publication on exact parity-split recurrence for precisely K_n corona K_1 states the same immediately fixed number and exactly the same primitive two-cycle orbit count, in addition to a full first-entry-depth census. Its formulas Q1=2+C, Q2=(C^2-C)/2 for even n and Q1=2,Q2=C(r+2) for odd n imply the submitted P1=Q1 and P2=2Q2. The odd expression agrees identically because n binom(n-1,r)=(r+1)binom(n,r). The November 1 whiskered-clique publication independently repeats the same counts and asymptotics. Prior coverage is direct and exact, not merely conceptual.

## value

FAIL

The exact parity switch is mathematically interesting, but the entire submitted immediate periodic-state census and asymptotic law have already been proved for the identical graph and rule in two earlier complete sources. Recasting temporal-orbit counts as doubled periodic-state counts is a routine notational conversion, and no independent refinement remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
