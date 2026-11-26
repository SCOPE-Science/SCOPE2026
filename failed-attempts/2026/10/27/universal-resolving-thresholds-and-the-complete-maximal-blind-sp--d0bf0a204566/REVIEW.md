# Independent mathematical audit

## correctness

PASS

A failing set lies in a single pair's equalizer, and at maximum cardinality it must be that full equalizer. At pair distance r, the fraction of landmarks in the equalizer is the return probability for r independent increments with law (1/q,(q-2)/q,1/q). In the binary case only even r contribute, and the successive normalized central binomial coefficients strictly decrease, giving r=2 when available and the empty set for d=1. For q>=3 the convolution preserves symmetry and nonincreasing masses away from zero by the differences in lines 58–74; p_(r+1)(0)=p_r(0)-2[p_r(0)-p_r(1)]/q. For q>=4 the positive central gap at r=1 persists. For q=3 central masses tie at r=1,2 only: the j=1 difference p_r(1)-p_r(2) starts positive at r=1 and persists by its positive coefficient in the difference recurrence, giving a positive central gap at every r>=2. In dimension one only r=1 is feasible. Same-sign versus opposite-sign local contributions give the stated two-coordinate parity and ternary permutation conditions. For any designated ternary permutation, take endpoints (alpha,pi(beta)) and (beta,pi(alpha)) with alpha!=beta to realize its graph. One- and two-coordinate projections distinguish the constraint supports; actual projections recover the parameters and certify the counts. A separate direct enumeration of all target pairs and their distance equalizers matched the full families in 11 small graphs (binary d=1–4, ternary d=1–3 and q=4,5 with d=1,2), not a substitute for the proof. Supplied verify.py was inspected, not executed.

## originality

FAIL

The distinct indexed mixed Hamming graph theorem mathematically covers both the complete threshold and the census for d>=2, not merely the well-known reduction to bisectors. The only remaining domain d=1 is the complete graph K_q: each pair's equalizer is its complement, so the threshold q-1 and all binom(q,2) maximum sets (including the single empty set for K_2) are immediate. This is a coverage verdict for the frozen standalone claim, not a ruling on historical priority: the broad match has a later catalogue date, and its relationship to the earlier-labelled frozen result is not established.

## value

PASS

The family-wide extremal question is meaningful: an exact uniform landmark threshold is different from finding a small resolving set, and all largest failing sets explain which geometric obstructions realize it. The ternary transition in possible supports is informative beyond the threshold number. This assesses the scientific content, not its eligibility as a distinct standalone contribution given the exact overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
