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

Normalize nonzero inputs by the sum of squared radii. For d=N−1 assign to each of the N sign rows a norming coordinate; two rows collide. Both the agree and disagree sets of signs are nonempty, so the two scalar sums A±B satisfy |A+B||A−B|=|A²−B²|≤(R−t)² with R the sum and t the minimum radius. All other factors are ≤R. Cauchy–Schwarz on the remaining m radii with sum S yields exactly F_n(z)=m^q(m+z)^(2−q)/(m+z²), z=mt/S∈[0,1]. Its derivative has the sign of (2−q)m−2mz−qz², strictly decreasing with opposite endpoint signs, giving the claimed z_n. For the witness, keep one full signed coordinate for each row except a pair differing only in the last sign, and give that pair a shared coordinate omitting the last component. For either omitted row at each other coordinate the first m sign products match at index one and disagree at least once, so their absolute sum is ≤m−2; adding z_n≤1 cannot exceed m. Thus the omitted norms are m and all other norms m+z_n. Saturation is attained with one coordinate per row, and conversely compactness gives an attaining tuple; equality in Cauchy–Schwarz and the scalar triangle inequality forces equal positive radii and a different norming coordinate for each row modulo global reversal. The root equation gives 1−z_n=O(q); near 1 the log derivative at 1 is O(q/n) and its derivative O(1/n), yielding F_n(z_n)−F_n(1)=O(q²). Now F_n(1)=n(1−1/n)^q and n log(n/(n−1))→1, proving the deficit asymptotic. Independent decimal evaluation of the n=4 witness gives 3.532200615298932666… .

## originality

PASS

The functional itself is exactly the published higher-order Zbăganu functional. The saturation-side dimension scale overlaps the arithmetic theory, and a distinct indexed same-day result gives the exact order-three dimension sequence using the same one-collision proof idea. The supported distinct claim is the all-orders n≥4 penultimate evaluation and deficit; neither checked theorem supplies it. No publication ordering is inferred for the two indexed records.

## value

PASS

The last dimension before saturation is selected by the sign-cube geometry, not by numerical convenience. Quantifying the exact cost of losing one norming coordinate for every order and showing the deficit is asymptotic to 4/N provide a usable benchmark for comparing geometric versus arithmetic signed-sum invariants. The simple shared-coordinate construction explains why a tailored unequal-radius witness is needed instead of an equal-radius estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
