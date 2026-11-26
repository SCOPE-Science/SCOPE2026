# Independent mathematical audit

## correctness

PASS

The definition uses the half-open prefix starting at zero and half-open shells. Group the terms at 4j through 4j+3: their signs are τ(3j),τ(3j),−τ(3j+1),−τ(3j+2), giving F(4m)=3F(m)−S(m), with S(m) the ordinary Thue–Morse prefix at 3m. Pair cancellation gives S=0 for even m and a=τ(3m)=−S for odd m. The four corrections are (0,a,2a,3a) for even m and (a,2a,3a,3a−b) for odd m, b=τ(3m+1), all of absolute value at most 4. In the base shell k=1 the extrema and two bottom equality positions follow by direct summation. In the induction only m=A=4^k and A+1 can yield either of the next two lowest values; at A the four increments are 0,1,2,3, and at A+1 the corrections are all positive. All other parents are ≥L+2, hence their descendants are ≥3L+2. For the upper bound only parents U or U−1 matter. At U, m is even and the next index is inside the shell, so maximality forces a=−1. At U−1 the only dangerous correction is +4, requiring a=+1,b=−1. Then z=(3m−1)/2 and z+1 both have sign −1, forcing z odd and τ(z+2)=+1. Thus F(m+2)=U+1, impossible in the shell. The exceptional last odd m=4A−1 has b=+1 by its stated base-four digit string, excluding the same danger. The explicit N_k is in the shell, is even and has the given base-four expansion. Since 3(N_k−1)=10·4^k−1 has digits 21 followed by k threes, a=+1 there, and N_(k+1)=4(N_k−1)+2 gives F(N_(k+1))=3F(N_k), with F(14)=12. No uniqueness of the maximum is inferred. Independent direct bit-count enumeration /workspace/newman_replay.py confirms both levels/uniqueness and the maximum with its witness through k=9. This is corroboration; the induction proves the entire domain. Frozen source/checker and log were inspected, not executed.

## originality

PASS

Pass for the precise shell extrema, first two equality positions at the lower end, and explicit maximizing family. Shallit studies exactly this F, not merely a related variant, and gives an automaton computing every value. His stated bounds and equalities do not directly settle the shell optimization. An automaton implementation or explicit Coquet-type formula is relevant prior machinery, but the inspected statements do not establish the optimization without further analysis. Coquet and Hofer full texts remained inaccessible and are residual priority risks.

## value

PASS

Quartic intervals are aligned with the natural base-four scaling of rarefaction by three. Exact smallest, next-smallest and largest discrepancies with their specified locations describe what happens at every finite scale, information not supplied by power-law growth envelopes or isolated values. The result also gives an elementary proof of sharp bounds; no value is assigned to a full maximizer classification, which is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
