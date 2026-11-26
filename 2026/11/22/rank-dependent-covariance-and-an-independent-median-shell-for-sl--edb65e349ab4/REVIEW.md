# Independent mathematical audit

## correctness

PASS

Re-audited the corrected RESULT.md: atomlessness plus the probability integral transform preserves all ranks almost surely. Given the shared endpoint x at lag k, the two retention events are conditionally independent, with equal parameters by time reversal. Within one pair, either both replacement endpoints are below Z_{j−1} or both above Z_j for a shared j-th value. Integration of the fresh uniform endpoint gives h(x)=E[Z_{j−1}1{x<Z_{j−1}}+(1−Z_j)1{x>Z_j}]. For the size-k−1 uniform sample, x f_{Z_{j−1}}(x) and (1−x)f_{Z_j}(x) are respectively (j−1)/k and (k−j)/k times the same Beta(j,k+1−j) density, and h(0)=(j−1)/k. Hence the covariance is Var(h(U)), with a strictly positive CDF variance; the coefficient vanishes exactly at the odd-width central rank. In that case the common conditional Bernoulli parameter is constant, giving independent indicators. More distant input sets are disjoint. The new repair checker, replayed with cd /workspace/repairs/2 && python3 -B verify.py, exhausts 5040 and 362880 relative orders at k=3 and 4 and gives respectively 0 and (11/1400,11/1400) for the interior ranks. The proof, not these small checks, covers all widths. Frozen verify.py was inspected, not executed; the corrected verification front matter was preserved verbatim.

## originality

PASS

The repaired claim is restricted to full-width separation and interior ranks. It removes the overlapping lag-one formulas and rank optimizer, expressly credits and excludes the extrema, and does not claim novelty for independence beyond the overlap range. The exact interior-rank formula and unique median exception are distinct on the inspected evidence.

## value

PASS

Lag k is the last lag with shared input, so the distinction between the central rank and every other interior rank is a natural sharp dependence boundary rather than a selected numerical case. The exact formula identifies the mechanism and a usefully reusable covariance even when it is nonzero; disjoint-window independence serves only as context.

The dated certificate retains the supplied scientific assessment, sources and limitations.
