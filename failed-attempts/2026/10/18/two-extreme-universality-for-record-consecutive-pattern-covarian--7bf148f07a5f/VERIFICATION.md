---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Before the window the record event and pattern use disjoint independent observations. After the window the insertion rank at position i is independent of the relative-order permutation at positions 1,…,i−1: each earlier permutation has one extension at each possible insertion rank. This independence is from relative order, not from the actual preceding values. Inside the window, only a pattern prefix maximum of rank s can be a record. Among the j+k−1 ranks up to the end of the window, the set of k ranks assigned to the window is uniform even given its relative order. To beat the j−1 earlier observations the top k−s+1 of all these ranks must be in that set, a probability of binom(j+s−2,s−1)/binom(j+k−1,k)=Q_s(j,k). Subtract the window's unconditional record means and multiply by 1/k! to obtain the exact formula and independence of ambient n. At fixed k, Q_k=k/j−k(k−1)/j²+O_k(j⁻³); Q_(k−1)=k(k−1)/j²+O_k(j⁻³); all lower ranks are O_k(j⁻³). Rank k always contributes and rank k−1 contributes exactly when before k. Subtracting k/j−k(k−1)/(2j²)+O_k(j⁻³) gives the stated signed limit, also for k=2. The explicit 132 numerator is 4−3j over 6j(j+1)(j+2), hence its sign switch is correct. Read the frozen verification notes and script without executing the latter; exhaustive comparisons cover k≤4 and n≤6, with separate large-position rational checks for k≤7, not a proof of the unrestricted identity.

## originality

FAIL

A distinct indexed Resultary result (5bf194eee4a8) explicitly gives the stronger finite-band covariance kernel for arbitrary pattern length and every pair of positions, under exactly the same uniform-permutation hypotheses. Summing in the record position gives the frozen exact law; retaining the two highest rank terms of its displayed product gives the frozen limit and eventual sign. There is no materially uncovered assertion in the frozen finding. This is a judgment of demonstrable coverage in the available corpus, not a claim that the October 26 catalogue entry was published before the October 18 frozen record or that it establishes historical priority.

## value

PASS

The mathematical phenomenon is useful independently of priority: a local pattern window contributes to dependence with the global record count, and the order of just its two highest ranks controls the leading sign for every fixed pattern length. This gives a tractable positional explanation and distinguishes eventual sign from small-window-position behavior. It does not, however, provide a separate original increment over the stronger indexed kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
