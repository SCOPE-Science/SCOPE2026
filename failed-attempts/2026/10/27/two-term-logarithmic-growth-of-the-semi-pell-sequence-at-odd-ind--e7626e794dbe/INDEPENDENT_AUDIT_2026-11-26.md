# Independent mathematical audit

## correctness

PASS

The marked odd-multiplicity model gives the recursion: at even weights halve all parts; at odd weights split between exactly one unit part (two possible markings of that part when n>1) and at least three (delete two units and preserve marking). Positivity gives strict odd-index increase by the recursion. For n<2^k the unrestricted binary-partition coefficient bounds the count after a factor 2^k for markings. At u=k/2^k, the tail of the Euler product from J=k−ceil(log₂ k) is bounded by the convergent product of (1−exp(−2^(j−1)))^−1. The initial factors contribute at most ∑_{i<J}(k−i−log₂ k+O(1)), yielding k²/2−k log₂ k+O(k). In the lower construction, the prescribed counts of the r=k−ceil(log₂ k)−2 nonunit sizes use weight at most 2^k/(2k)+2^k/4, below 2^k−1. The filler unit multiplicity is odd and positive, and the product of the numbers of multiplicity choices is injective; taking its log gives the matching lower order. The two odd dyadic endpoints bracketing n differ by O(k) at the stated precision, giving the uniform odd-index result. Even-index scaling is correctly excluded. An independent recurrence/ordinary-partition DP checked the constant-scale sandwich at nine dyadic endpoints (python3 /workspace/branches/independent_checks.py); those finite examples do not prove the asymptotic. The supplied script and verification notes were inspected, not executed.

## originality

FAIL

The stronger classical unrestricted binary-partition asymptotic transfers at exactly this precision through a direct multiplicity encoding in the published semi-Pell overpartition model. Forgetting the markings gives the upper comparison. For the lower comparison, take any binary partition of m=floor(n/4). For each occupied 2^i of multiplicity a≥1, put 2a−1 copies of 2^(i+1); the new nonunit weight is at most 4m≤n−1 for n odd. Add units to reach n and mark the largest size. The image has all multiplicities odd; the original multiplicities are recovered from the nonunits. Thus b(floor(n/4))≤s(n)≤2n b(n), where b is the ordinary binary partition count. De Bruijn's two terms for log b carry over because both rescaling n by a constant and multiplying the count by 2n change the logarithm by O(log n). This is a direct squeeze using the pre-existing model, not a claim that the inspected sources already print the semi-Pell asymptotic verbatim. The later relative-growth record alone would be too coarse to determine the coefficient.

## value

FAIL

The odd-index growth question is motivated and the submitted self-contained proof is valid. At the specified precision, however, the result does not distinguish the semi-Pell family from ordinary binary partitions: constant-scale embedding and the polynomial markings factor preserve both terms. The proof does not supply a finer semi-Pell invariant such as the linear log term or a sharper count ratio that survives this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
