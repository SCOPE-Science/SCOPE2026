# Independent mathematical audit

## correctness

PASS

The first n−1 coordinates identify the intrinsic torus with an (n−1)-torus. Their negative fractional parts are independent uniforms, and the last part forces their total J to be the ceiling of the first n−1 parts' sum. Cube slabs give the exact Eulerian weights, with J=1 deterministically at n=2. Subtracting the translate from each integer point leaves precisely n bounded digits in [0,t−1] summing to tk−J, so the count, coincident count atoms and occupancy interval are all handled. At t=1 the law is Bernoulli with success exactly J=k. For the mean, Haar averaging gives volume in the lattice measure (Euclidean measure divided by the root-lattice covolume √n); projecting Δ to the first n−1 coordinates gives the cube slab with sum in [k−1,k]. The ceiling shifts the sum of uniforms by at most one, so the CLT has center n/2 and asymptotic variance n/12. At either fixed-t threshold the other endpoint is separated linearly from the center; the near endpoint yields the stated Gaussian CDF with the appropriate sign. For t=2 the binomial index deviates from its center by √n(2a−Z/√12) in the limit; uniform Stirling on bounded scaled intervals and tightness give the negative quadratic limit, including −χ²₁/6 at a=0. Off center the first entropy derivative gives the stated Gaussian variance; empty events have probability tending to zero. The supplied checker.py was inspected but not executed, and the finite checks it defines are not needed for the analytic proof.

## originality

PASS

The mean and Eulerian volume are classical; the distinct contribution is the intrinsic random-translate multiplicity law together with its two rank-edge limits and the t=2 crossover. The nearest same-object and nearest same-statistic records were read and do not imply that combination or its specialized transition laws. This is not a historical-priority certification.

## value

PASS

Dilated hypersimplices are standard lattice polytopes, and intrinsic periodic translation is the nontrivial randomization for this affine object. The full law distinguishes typical multiplicity from occupancy and mean. In particular the central non-Gaussian log-multiplicity limit occurs well inside the occupied regime rather than at either occupancy edge, an exact and useful contrast not recoverable from the volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.
