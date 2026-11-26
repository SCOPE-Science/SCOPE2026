# Independent mathematical audit

## correctness

PASS

Common atomless independent endpoints have a uniform rank permutation and hence induce a uniform perfect matching. A cut with no open interval has even rank, separates adjacent overlap components, and every component boundary gives one such cut. The cut probability is ((2k−1)!!(2n−2k−1)!!)/(2n−1)!!=p_{n,k}. Conditioned on the cut, the matchings factor and no edge runs between the blocks; the difference between the unrestricted expected edge count and the sum of the two block expectations is exactly (2/3)k(n−k). Thus adding cut covariances gives the claimed strictly negative sum for n≥2. To check the variance, put (A,B)=(left endpoint,1−right endpoint) after the rank-preserving uniform transformation, with density 2 on A,B≥0, A+B≤1. Then E[A²]=1/6, E[A⁴]=1/15, E[A²B²]=1/90, so 1−A²−B² has variance 2/45. This is the covariance for distinct edges sharing a vertex; edges with disjoint vertices are independent. Counting the 3 binom(n,3) unordered incident edge pairs yields the edge variance. For the cutoff estimates p_{n,1}=1/(2n−1), p_{n,i}=O(n^(−i)) for fixed i, and the ratio test shows that the probabilities decrease to the middle. In the unweighted sum, the interior beyond each second term costs at most O(n)p_{n,3}; in the weighted sum, beyond each third term it costs O(n³)p_{n,4}. The paired extremes therefore give S_n=1/n+O(n⁻²) and weighted sum 1+O(n⁻¹). Two simultaneous cuts have probability p_{n,k}p_{k,j} for j<k. Summing with S_k=O(1/k) on the right half and bounding p_{n,k} by p_{n,3} for k=3 through the left half (handling k=2 separately) gives O(n⁻²). This gives both the component variance and the disconnection probability with the stated errors. The standard deviations' product is asymptotic to n√(2/45), giving the −√10 correlation constant after rescaling. The supporting exhaustive checker was inspected without execution; no limiting claim relies on finite samples.

## originality

PASS

The finite identity is not a standalone originality basis. Kasraoui–Zeng's Proposition 3.8 already gives the all-size overlap-edge polynomials via the diagonal specialization of their crossing/nesting series. The standard concatenation of interval components then mechanically gives a full bivariate series, whose mixed derivative recovers the reported sum. What survives is the asymptotic mixed-dependence result: locating the endpoint cuts that alone contribute at order one and proving that all other weighted cuts and simultaneous cuts are negligible, giving the nonzero covariance limit and the sharp correlation coefficient. The exact series does not state or extract those asymptotics; neither separate connectivity nor edge statistics justify them. The available sources do not cover this sharp weighted-cut analysis.

## value

PASS

The component count and overlap-edge count are natural topology and density statistics of the same model. The quantified phenomenon is that an O(1/n) disconnection probability still leaves a nonzero covariance, while the standardized correlation has the exact coefficient −√10 at scale 1/n. The proof identifies the dominant mechanism rather than just printing finite moments from an exact series. This is a useful calibration for dependence in the canonical endpoint model, including its extension to arbitrary common atomless laws, without needing a broader graph class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
