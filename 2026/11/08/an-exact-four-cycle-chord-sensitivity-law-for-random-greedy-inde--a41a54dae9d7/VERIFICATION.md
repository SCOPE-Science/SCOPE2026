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

For random-order greedy MIS on a path P_n and endpoint-four-cycle graph B_n=P_n+{0,3}, first-vertex conditioning gives nf_n=n+2sum_{j=0}^{n-2} f_j and F(z)=(1-e^-2z)/(2(1-z)^2). Conditioning on B_n first vertex gives the stated convolution recurrence; the unique power-series solution yields Delta(z)=[(3-3z+z^2)-(3+3z+z^2)e^-2z]/[2(1-z)]. Coefficients give increments -(-2)^(n-2)(n-3)(n-4)/(2n!), Delta_5=1/15, Delta_6=0, alternating strictly shrinking tail, Delta_n>0 for n>=7, limiting (1-7e^-2)/2 and factorial alternating remainder. Independently computed exact expected output from induced-subgraph first-arrival dynamic programming for n=4..11; deltas were 0,1/15,0,4/105,1/45,26/945,41/1575,823/31185. Recurrence and analytic alternating bound, not bounded calculation, establish all orders.

## originality

PASS

PASS best-of-knowledge. The principal earlier path-minimal theorem is only among trees, whereas B_n is unicyclic; its known counterexamples to greedy edge monotonicity use different graphs. The separate previously published short-chord sign reversal is on rings C_n, not the endpoint chord of a path. No source inspected gives this exact all-order four-cycle-tail GF, exceptional n=4,6, positivity thereafter, or limiting sensitivity. Simple first-vertex recurrences are standard background but do not alone supply the classified chord law.

## value

PASS

A path is extremal for random-greedy independence among trees; adding a bipartite 4-cycle is a minimal structural perturbation beyond that tree class. An exact sign and equality classification for one edge addition supplies a useful sharp counterexample/boundary to monotonicity expectations, with a nontrivial all-order generating function and limit, rather than arbitrary small-size arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
