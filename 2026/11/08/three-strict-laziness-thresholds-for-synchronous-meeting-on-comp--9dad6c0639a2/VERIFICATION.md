---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The labelled one-step transition rule yields exactly the three nonabsorbed pair orbits CC/CI/II and the displayed 3x3 substochastic matrix M with d=a+b-1, q=(1-p)/d, r=(1-p)/a, c=p+(a-1)q. Independent fresh symbolic adjugate calculation derived Q and R exactly and verified S=(b-1)Q+R and all six endpoint factorizations. Absorption occurs with a uniform positive probability within bounded steps for each finite a,b and 0<p<1, making I-M invertible with positive determinant. Each quadratic has opposite nonzero signs at p=0 and 1, so exactly one simple interior root. Its Q,R Sylvester resultant has the strictly negative factor -2(a+b-1)(a(b-2)+(b-1)^2)P(a,b), with P(x+2,y+2) all 36 coefficients strictly positive. The base witness at a=b=2, p=4/15 yields Q=-41/225 and R=-128/75, forcing alpha<beta; S(beta)=(b-1)Q(beta)<0 forces gamma>beta. Independent full unordered-pair chain solution (18 graph-size/rate instances and 270 state comparisons), plus 49 size-pair root checks, corroborates the universal algebra. Boundary a=b=2 and a or b=2 are included; p=0,1 excluded.

## originality

PASS

The generic product-chain absorption construction is known, but the precise all-a,b strict three-root phase order has not been found in the relevant accessible comparisons. The exact complete-bipartite result concerns a graph without clique edges and does not imply the split-graph result. Historical priority remains qualified.

## value

PASS

The complete split family K_a join edgeless K_b is a canonical nonregular graph family and mean first encounter by initial pair orbit is a natural observable in synchronous two-walker dynamics. Before symbolic elimination, a generic absorbing-chain recipe yields individual rational means but gives no reason that all three pairwise differences cross precisely once, nor that their distinct crossing order is universal over two unbounded integer size parameters. The nonvanishing resultant establishes a natural global phase portrait with four strict rank orders and exact threshold polynomials, a mathematically informative structural classification beyond a small finite census, special parameter substitution or routine textbook calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
