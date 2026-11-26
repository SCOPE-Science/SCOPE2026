# Independent mathematical audit

## correctness

PASS

Whitening by y=H^(1/2)e turns each probe into the Euclidean orthogonal rank-one projector P_z onto H^(1/2)z. In the two unit diagonal directions the Hessian entries a,b,d satisfy b=(κ−1)cos(2θ)/2 and 4ad=(κ+1)²−(κ−1)²sin²(2θ). The two normalized whitened directions have inner product b/√(ad), so the equal-weight mean M of the two projections has eigenvalues (1±δ)/2 as claimed. Independence and P_z²=P_z give E[P̄²]=(1−1/n)M²+M/n, so the risk is exactly the maximal eigenvalue of F(M). Its two values average to F(1/2)+(η²/4)(1−1/n)δ², and F(1/2)=1/(n+1)+(n+1)(η−2n/(n+1))²/(4n). This gives the sharp achievable lower bound and the unique step. For n>1 equality forces δ=0; for n=1, at η=1 the larger factor is (1+δ)/2, again forcing δ=0. With κ>1 on the specified angle interval this means θ=π/4. At this angle the conditional risk operator is scalar, and fresh independent batches give the exact horizon law by conditioning. At θ=0 the small eigenvalue tends to zero; minimizing its own scalar risk gives a lower bound 1−λ_-/(1/n+(1−1/n)λ_-), which tends to 1 for fixed n, while η=1 gives an upper bound of 1. The interior curvature floor never activates since zᵀHz≥2.

## originality

FAIL

The 12 October planar sketch-and-project result supplies the exact orientation-dependent spectrum of the identical whitened two-direction projector. The full new-looking batch formula is then the direct iid moment expansion of those same projectors; optimizing that scalar polynomial yields the claimed optimum, its equality cases, horizon identity and axis-aligned limit. Thus the frozen exact invariant is mechanically implied by the inspected published spectrum plus elementary iid algebra. This is a prior-coverage decision, not a mathematical error or a verdict based on unavailable text.

## value

FAIL

Quantifying orientation and batch size is a reasonable motivation, but the proposed exact benchmark is a routine iid averaging calculation from the indexed planar projector spectrum, with optimization by a single scalar square completion. The record offers no further distinct non-mechanical phenomenon, proof ingredient or invariant in its stated scope. A useful explanatory restatement of known projector data is insufficient for this exact-result criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
