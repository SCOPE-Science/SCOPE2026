# Independent mathematical audit

## correctness

PASS

The frozen result is mathematically correct, but is not passed as submitted because its headline one-wall solution has exact prior coverage. I re-audited the repaired result in repairs/2/RESULT.md: n(log 3−H_n)=−4 log(3(2−√3))+O((2−√3)^n), with no novelty claim on the known profile. Strict concavity and interpolation into a positive feasible point give a unique positive optimizer, and differentiation in edge coordinates gives P_ij=v_i v_j on the supported entries with v_i(v_{i−1}+v_i+v_{i+1})=1 and zero ghost entries. Row sums and symmetry give the entropy identity 2∑log(√3v_i) for the normalized deficit. For the repaired proof I checked the half-line identity by clearing denominators: the constant and quadratic coefficients reduce using r+1/r=−4 and the middle coefficient uses (1+r)(1+4r+r²)=0, with r=−(2−√3). The product comparison a_i b_i has residual ∑_d(A_d−1)(B_d−1) because each individual three-term row sum is 3 in the normalized coordinates. The leading term cancels exactly since ∑_{d=−1}^1(1+r^d)(1+r^{−d})=0, leaving a bound proportional to |r|^{n+1}(|r|^i+|r|^{n+1−i}), also at the terminal rows using t₀=0. Thus the sum of absolute residuals is O(|r|^n). The log-coordinate Jacobian and its segment average are symmetric and have uniform positive diagonal dominance margins; their inverse sum-norm bound follows from the max-norm bound and symmetry. The residual thus controls the actual summed log error, not an n times max-error estimate. Telescoping the half-line product gives (1−r)/(1−r³)=1/(3(2−√3)) with exponentially small tail, hence the exact constant and rate. The frozen verify.py was read, not run. An independent finite rational check of the profile and initial entries agreed with the frozen arithmetic, but neither that check nor the frozen script is used to establish the repaired rate. The corrected proof and verification notes provide the replay path.

## originality

PASS

For the frozen submission the headline explicit half-line solution fails originality: it is exactly the strong negative-coupling specialization of a published single-wall factorization, not merely a lookalike recurrence. The finite scaling equations themselves also follow from published general entropy reconstruction. The repaired theorem credits both, and passes only on the sharply controlled finite-path entropy deficit: a closed limiting constant realized with a summable full-length O((2−√3)^n) error. The actual two-wall elliptic source was compared and receives credit for the stronger recurrence solution on its documented branch, but it does not establish the necessary negative-coupling branch, normalization and uniform large-size entropy estimate on the positive optimizer. The repaired cancellation argument proves that estimate without relying on a branch continuation. This is a best-of-knowledge decision, not an assertion of priority for the single-wall profile or closed product alone.

## value

PASS

For the repaired theorem the quantity is the total two-end cost of maximizing entropy under a uniform stationary constraint. The exact closed constant and full-length rate control the pooled entropy loss, rather than just pointwise boundary convergence. The leading cross interaction cancels when translated to the row equations, and the dimension-independent sum estimate turns that cancellation into a bound on the global observable without an n penalty. This is useful for comparing finite path designs and isolating the endpoint contribution from their mutual interaction. The known endpoint profile in isolation would not justify the repaired claim or its value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
