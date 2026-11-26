---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the positive left half, the return is G(x)=16cx^2(1-x)^2, strictly increasing as a function on the half interval. The ratio G(x)/x peaks at 64c/27 and at 1/2 equals 2c. Thus the sign regions and monotone, no-overshoot returns give the 0/1/2 positive fixed-point census and the precise phase limits. The only genuine cycles of F have period two. At 0, the polynomial is an extension, not the true return: 0->1/2->1->c. This attaches 0 to the periodic basin at and above threshold and to the ghost below. The right separator is L(r)=1/2+sqrt(r/(4c)), giving ghost length r+sqrt(r/(4c)); its two terms decrease strictly with c above the fold. Direct exact substitution gives 7/9 and 1/2 at the two marked parameters. Empirical limits are the phase averages; applying bounded convergence to continuous test functions against any invariant measure makes it a mixture of those limits with basin-mass weights. Since only the ghost limit changes under pushforward, its coefficient must vanish. This proves the invariant-probability census without using continuity of F at the border. Independently, x(1-x)^2=4/27-h^2+h^3 for h=x-1/3. Expansion of 1/(16c) gives the 16/27 fold coefficient, and at the fold h_next=h-(9/4)h^2+O(h^3) on the attracting side so n*h_n->4/9. For positive left ghost returns, y_n=16c*x_n satisfies y_next=y_n^2(1-x_n)^2. The positive increments of -2^(-n)log y_n are -2^(-n)log(1-x_n); the weighted tail times 2^n tends to zero, proving the stated doubly exponential equivalent. The even-phase rate in part (iii) uses positive left ghost starts, as given by its basin formula. If extending the rate to the subcritical start x=0, reindex at F^3(0)=c: the original even iterates then tend to 1/2, not to 0. This phase exception does not affect the all-orbit empirical claim. Independent exact identities are replayable with python /workspace/branches/independent-algebra.py (item 3); continuum claims follow from the orbit argument.

## originality

PASS

Fixed-point absence, non-invariant limit phenomena, and low-c border nonexistence are known. The strict-alternation fold even has this numerical threshold as a boundary limit. What survives is the true discontinuous-border orbit and invariant-measure classification across the sharp threshold, with positive critical basin and exact supercritical empirical partition including the equal endpoint split.

## value

PASS

The quadratic symmetric border is a natural part of the motivating family: the apparent return fixed point at zero is not an actual one. The full alternation-range classification shows exactly when true invariant probabilities first appear despite universal time-average convergence and quantifies how much initial mass selects the non-invariant limit. The 2/9 physical birth and the half-basin endpoint give real structural information beyond a known ghost example or a generic saddle-node. No claim is made beyond the stated border slice or about finite-precision behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
