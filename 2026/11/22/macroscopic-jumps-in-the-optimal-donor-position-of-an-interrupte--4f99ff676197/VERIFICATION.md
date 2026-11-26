---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The probability of reaching position i is q^{i−1}; multiplying by foreign-load transfer (1−r)r^{i−1} for i<j gives the female geometric sum. For male export conditional on reaching the donor, the backward recurrence is E=1−q+qr E_next with terminal value 1; multiplication by q^{j−1} gives the displayed score including mandatory terminal departure. Direct subtraction gives the adjacent sign factor: its first and last terms are positive exponentials in real j with nonzero rates, hence its second derivative is positive. The strict candidate reduction can be stated more precisely than the proof's informal local-maximum wording: if G(J)<0 and J<i<n, either F_i<F_J or there was a positive increment between J and i; in the latter case convexity and G(J)<0 force all increments from i to the end to be positive, so F_i<F_n. This proves F_i<max(F_J,F_n), including flat-adjacent cases. For fixed r,w, J_n=ceil(4 log(n)/|log r|) makes the r^{J−1} term O(n^{−4}); the other positive term at J is exponentially small and the squared departure rate is at least (log n)^2/(4n^2) throughout the window. Subtracting the common baseline w(1−r)/(1−qr), at q_- the J-score is asymptotic to 2 log(n)/((1−r)n) and the terminal score is at most O(n^{-2}); at q_+ the terminal score exceeds every nonterminal score by a uniform leading term asymptotic to (1−r)n^{-1/2}, dominating O(log n/n) and exponential errors. Continuity of the early maximum minus the terminal value supplies an interior tie that excludes all intervening positions. Only r,w are fixed as n grows; no uniqueness is inferred. An independent exact witness using the two backward recurrences is reproducible with `python3 /workspace/checks/donor_witness.py`; see its adjacent output log. The endpoint differences F_10−F_4 are about −1.97069×10^{−7} and +1.42956×10^{−6} and the minimum other-position lower-end gap is about 0.00356173, verified by rational comparisons. Coupling the nine continuation draws via common uniforms bounds each score's Lipschitz constant by 18 (reward in [0,2]), hence each gap can shrink by at most 36×10^{−6} across the bracket. The root approximation and tied score agree with the record. These finite checks do not replace the asymptotic proof.

## originality

PASS

The supported distinct result is a sharply nonlocal global tie in this particular interrupted, one-donor allocation model, with quantitative separation and a small exact witness. Sex allocation across flowers, directional pollination, pollen carryover and differential export are not new. The closest checked modern positional-allocation entry changes both the decision variable and visitation law; the closely related older ESS model was inspected in its primary published text and has different allocations, transfers and objective.

## value

PASS

The stated tradeoff naturally links directed visitation, foreign receipt before the donor, and loss of donor pollen after it. The result demonstrates that small changes in visitation persistence can move the optimal position by nearly the whole path, which cannot be inferred from comparing adjacent positions alone without the global candidate reduction. The small exact witness and uniform asymptotic scaling make this a useful theoretical benchmark for richer models. It is neither evidence of a universal biological rule nor a calibrated fitness or evolutionary-stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
