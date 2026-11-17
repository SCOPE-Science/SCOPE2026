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

For the unique two-cycle, x+y=1-d follows by telescoping logit h(f(t))-h(t)=a(t-b). Exact cycle equation x=[(1-x)(1-d-x)/(d+x)] exp[-a((1-d)/2-x)] gives x~(1-d)d^-1 exp(-1/d) at both nearby parameters using uniform endpoint bounds of the earlier Oct11 theorem. Exact multiplier (1-aq(x))(1-aq(y)) expands to 1+Lambda=-d(1-d)Delta_a+4x/(1-d)+o(x) uniformly for the two exponentially close parameters; neutral condition yields constant4 and comparison sign. Independent high precision values d=.12,.08,.05,.035 converge to normalized constants.

## originality

PASS

Full Oct 11 exact same map theorem read: supplies unique transverse crossing and only error O(delta^-2 exp(-1/(20delta))) for delta=d/2, so does not settle first nonzero e^(-1/d) coefficient or stability-margin constant. Kryzhevich–Zhang–Chmara primary 2024 article covers qualitative symmetric/asymmetric dynamics, not this asymptotic. New result is narrow but genuinely beyond-all-algebraic-orders refinement.

## value

PASS

At exponentially close coupling scales, every algebraic-order approximation is identical and cannot determine which side of the neutral flip the rational curve lies. The explicit sign and normalized prefactor answer a natural singular-bifurcation question, motivated by a known previously unresolved threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
