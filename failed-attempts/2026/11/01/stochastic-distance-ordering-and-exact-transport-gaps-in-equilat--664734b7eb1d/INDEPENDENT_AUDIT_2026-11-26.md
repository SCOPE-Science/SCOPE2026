# Independent mathematical audit

## correctness

PASS

With both edges oriented from the same part, the shortest distances conditional on same, incident, or disjoint labels have laws |U−V|, U+V, and 2−|U−V|. For incident edges sharing their first endpoint, the alternate cross routes exceed x+y by 2−2x or 2−2y, and the opposite-endpoint route has length 4−x−y; the other orientation is reflected. For disjoint edges the two cross routes have lengths 2±(x−y), while the same-part routes have lengths at least two. The per-edge label counts 1, N−2, P−N+1 give the stated mixture and both CDF branches, including the single-edge and four-cycle cases. At fixed N the difference is the positive factor 1/Psmall−1/Plarge times B_N. B_N is strictly positive in the interior; on [1,2] its quadratic in u=2−t has maximum 2(N−1)^2/(3N−4), and the density difference is positive up to that threshold and negative after it, so TV (supremum over measurable sets) equals the threshold gap. The three component first moments 1/3, 1, 5/3 give the W1 constant via stochastic order and quantile coupling; the second moments 1/6, 7/6, 17/6 give the stated second moment. The star and balanced mixture weights give the stated limits. This is a proof for unit lengths and independent normalized arclength, not vertex sampling or an unequal-length network. Replay: RESULT.md lines 41–94; verify_exact.py and VERIFICATION.md were inspected as finite corroboration, not executed or used as the proof.

## originality

FAIL

Distinct indexed findings establish equivalent coverage of the principal distance law and stochastic comparison. The sharp gaps are correct but mechanically extractable from the already stated law by first-moment subtraction and a one-variable quadratic maximization. This verdict is not a claim of priority between records with the same displayed day, or a finding that either comparison record explicitly prints both gap constants.

## value

FAIL

The distance law and ordering are natural invariants, but their equivalent coverage is established. The remaining W1 and TV constants supply no independently useful nonroutine mathematical remainder under the standard: one is the already determined mean difference, and the other is the maximum of the single quadratic CDF difference already fixed by the known law. No substantive repaired claim is supported by the frozen evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
