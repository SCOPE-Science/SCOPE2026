# Independent mathematical audit

## correctness

PASS

A signed edge difference has masses (a,1−2a,a) with a=p(1−p)>0 and a≤1/4. At a nonedge the two bits use disjoint signed variables; at an edge their only shared variable is the signed difference on that edge, even if the endpoints have common neighbors. Given its value the bits are independent, and the conditional means depend only on its magnitude by symmetry. The variance of the nonzero-magnitude indicator is 2a(1−2a), giving exactly the stated covariance times the product of central-mass gaps. As an independent check on the gap bound, each signed law is a mixture of a point mass at zero and the p=1/2 signed law with mixing weight 4a. Given j active laws, the gap by Vandermonde is C(2j,j)/(4^j(j+1)), positive and decreasing in j with consecutive ratio (2j+1)/(2j+4). Thus the mixed gap is at least b_n for all j≤n−2, with the empty sum included. Under the probability floor, 2a(1−2a)≥a≥ε(1−ε), giving c_n as stated. There are at most n² distinct means in the empirical covariance formula, each obeying Hoeffding for the independent repeat experiments. With accuracy c_n/8, the covariance error is at most 3c_n/8, yielding strict separation at c_n/2 and the stated count 32c_n⁻² log(2n²/δ). Stirling gives the n⁶ factor. This is a sufficient guarantee, not a minimax claim; stable labels and identical per-edge probabilities across the two replicas are essential model assumptions. Inspected RESULT.md, VERIFICATION.md and verify.py as text; the attached finite checks were not rerun.

## originality

PASS

The strongest inspected covariance tomography precedents recover under a different percolation mechanism or from a different observable. Neither raw-degree covariance nor an old fact about the distribution of a Bernoulli sum establishes the support and recovery guarantee for this equality-only channel. This judgment is bounded, not historical priority.

## value

PASS

The observation channel erases degree magnitudes and both edge lists, yet the exact sign pattern of a second-moment statistic still reconstructs an arbitrary labelled host with heterogeneous probabilities. Establishing strictness for every edge and giving a uniform positive margin makes the result useful for lossy graph measurement rather than a restatement of raw-degree covariance. The sample estimate is not asserted optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
