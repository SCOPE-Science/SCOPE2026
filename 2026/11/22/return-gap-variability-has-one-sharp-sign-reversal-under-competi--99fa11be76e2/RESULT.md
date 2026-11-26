# Return gaps with matching mean and variance can move a two-memory response in opposite directions

## Finding

Mean and variance do not determine even the sign of the effect of randomizing a return gap in a two-exponential response model. Let \(J=\log 2\). For every common mean \(\log(9/2)<\mu<\log(25/4)\), there are two strictly positive finite-support gaps \(T_P,T_Q\) with mean \(\mu\) and variance \(J^2\) such that, for the **same** response index \(V(t)=1+e^{-2t}-e^{-t}\),
\[
\mathbb E[V(T_P)]<V(\mu)<\mathbb E[V(T_Q)].
\]
At \(\mu=\log 5\) the two differences from \(V(\mu)\) are \(-1/200\) and \(9/640\). The displayed open interval is exact for this pair of shifted laws, not a bound for all possible gap laws.

## Assumptions and scope

Time \(t\ge0\) is the gap between two episodes. The positive fast term models residual sensitization, and the negative slow term models retained protection. The baseline comparison uses the deterministic gap at the common mean, not a comparison of the two random laws in convex order. The model is a stylized index, not a calibrated response probability or a claim about observed coral bleaching.

## Proof

Let \(T_P=\mu+J K_P\) and \(T_Q=\mu+J K_Q\). Take \(K_P=\pm1\) with probability \(1/2\) each, and take \(K_Q=-2,0,2\) with probabilities \(1/8,3/4,1/8\), respectively. Both centered offsets have mean zero and second moment one before multiplication by \(J\). Thus the gaps have exactly the same mean and variance. All gaps are nonnegative for \(\mu\ge 2J=\log4\), and strictly positive for \(\mu>2J\).

For either law \(B\in\{P,Q\}\), define \(E_{B,s}=\mathbb E[2^{-sK_B}]-1\). Exact averaging gives
\[
\begin{array}{c|cc}
 &E_{B,1}&E_{B,2}\\\hline
P&1/4&9/8\\
Q&9/32&225/128
\end{array}
\]
Writing \(x=e^\mu\), the difference from a fixed gap is
\[
\mathbb E[V(T_B)]-V(\mu)=x^{-2}(E_{B,2}-xE_{B,1}).
\]
It follows that \(P\) lies below the deterministic baseline if and only if \(x>9/2\), and \(Q\) lies above it if and only if \(x<25/4\). The reversed strict ordering cannot occur because these thresholds are ordered. Both endpoints of the resulting interval exceed \(\log 4\), so positivity imposes no further restriction there. At either endpoint exactly one of the changes is zero. Substitution of \(x=5\) gives the stated exact differences.

## Verification

Run `python3 checker.py` in this directory. It checks the probabilities, exact first two moments, positive gaps throughout the stated interval, the four exponential excesses, the two exact thresholds and their endpoint behavior, and the exact response differences at \(\mu=\log5\). The algebra above proves the result on the full interval.

## Relationship to prior work and limitations

Models of thermal variability and recovery motivate allowing two opposing memories, but the assertion here is solely about an explicit mathematical surrogate. Pfab et al., *Heat stress and bleaching in corals: a bioenergetic model* (2024, DOI 10.1007/s00338-024-02561-1), use a dynamic bioenergetic model; their inspected scenario methods use prescribed temperature trajectories and specified stress durations, not the gap comparison above. A fixed-mean comparison of Gamma transit laws in *A three-shape response staircase for fixed-mean reactive transit times* uses differences of Laplace transforms but does not match the variances. *Exactly two arrival-fraction reversals between moment-matched Gamma and inverse-Gaussian residence clocks* compares cumulative arrival fractions, rather than the sign of a two-memory expectation change against a deterministic gap. No priority is claimed for Jensen's inequality, signed-exponential zero bounds, or solving a two-term exponential equation. The substantive point is the explicit failure of the two-moment summary to determine **direction relative to a common fixed baseline**, not merely to determine the numerical expectation. No fitted data, full stress sequence, universal sign interval for other laws, or ecological intervention is asserted.
