# Independent mathematical audit

## correctness

PASS

In RESULT.md lines 15–35 and 54–66, d_n≥(1−η)∫t^n dν>0 gives positive weights bounded by (1−η)^(−1/2). For n>0, the charge (t^n−a^n)(ν−σ) is positive and gives strictly positive energy to every nonzero polynomial: its ν contribution cannot be supported on the finite polynomial zero set plus {a}. This proves the Löwner inequality with strict difference, reducing the standard all-shift k-hyponormality test to H_{0,k}. A positive representing measure would have support in [0,1] by bounded moments; polynomial density there contradicts the negative part of the signed representative. At the touching endpoint of the uniform case the same domination works and the signed measure is negative on {a}, since the uniform component has no atom. Congruence by A_k^(−1/2) gives the inclusive top-eigenvalue threshold; in rank one the eigenvalue is the squared evaluation norm in the orthonormal polynomial basis. For the uniform model, Legendre parity and positivity outside [−1,1] make the kernel sums strictly increasing. The Laplace prefactor at the sole maximum q gives the stated geometric sum, including 1−q^(−2). For the moving edge, extend each j-series by zeros. For fixed ℓ, k^(−2ℓ) times the product of the two binomial coefficients converges uniformly for 0≤j≤k to (j/k)^(2ℓ)/(ℓ!)²: each of its fixed number of normalized factors differs from j/k by O(ℓ/k); the omitted j<ℓ coefficients cause no problem. The summable factorial majorant then controls tails uniformly. The Riemann sum and differentiated I0/I1 identity give the positive edge limit, and at c=0 the kernel is exactly (k+1)². These analytic arguments cover the full stated domain. Direct recurrence at X=2 gives P_0 through P_3 equal to 1, 2, 11/2, 17, hence the quoted kernel values and strict example. The supplementary rational code CHECKER.py was inspected, not executed; its finite calculations do not certify the infinite or asymptotic assertions.

## originality

PASS

The standard Gram-matrix evaluation norm, weighted-shift moment criterion, existence of finite-order rungs in other families and classical polynomial asymptotics are not new. The examined statements do not cover the transfer from an initial finite Gram condition to every tail for ordered signed supports, or its sharp continuous-interval operator thresholds. This is a best-of-knowledge result, not a historical-priority certification.

## value

PASS

This gives a finite exact test for a natural non-atomic signed-charge class where the usual characterization involves infinitely many Gram matrices. Strict positivity of the tails even at an initial singularity makes the test useful at the sharp boundary. The same relation produces every exact finite-order non-subnormal rung in a concrete interval model and distinguishes exponential fixed-gap decay from the inverse-square crossover. These are operator-level consequences beyond evaluating a single standard special-function sum. Interlaced charges and general overlapping atoms remain outside the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
