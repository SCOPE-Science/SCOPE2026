# Independent mathematical audit

## correctness

PASS

The theorem holds for iid Bernoulli masks with common p, simultaneous gradients and 0<c,p<1. In the projector basis (T,U), E[DAD]=p²A+p(1−p)diag(A) reproduces the stated two-mode matrix and det(I−A)=p²η²K(4−2Sη+pKη²). The proof's line 43 has a normalization slip: I=T+U, with coefficients (1,1), not I=(n−1)T+U; (n−1,1) are its trace contributions. Both coefficients are positive, so the Perron argument is unchanged. Line 53 calls −2pH positive definite; the first-order changes of the reduced matrix at zero are −2pa and −2pL, both strictly negative. Cone domination by ||x_0||²I gives sufficiency and the symmetry-equivalent coordinate starts detect nondecay. The determinant factor is negative at 2, positive at zero, and has a second root above 2. A diagonal entry reaches 1 between the roots (the determinant at its crossing is −A_12 A_21<0), precluding reentry. The objective expansion from E[DHD] gives 2/W and F(2/W)=4(n−1)c(1−c)p(1−p)/W²>0. At the first root the displayed partial derivatives in p, c and n are strictly negative and ∂_ηF<0, giving the claimed monotonicities. Full symmetric-covariance enumeration independently corroborated the boundary in dimensions 2–4; the n=3 example has expected objective ratio 57/50. The two proof slips do not change the result or necessitate a substantive repair.

## originality

FAIL

The central claim as a separate finding is covered by the distinct indexed exchangeable-minibatch theorem, not merely by a similar title or general methodology. Its theorem and descent formula give exactly this cutoff, failure at and above it, and the strict descent gap upon setting q=p². The ancillary n and c comparisons follow by differentiating the same specialized root; necessity for each coordinate start follows by the same two-mode reduction and permutation invariance. This is a decision about demonstrable statement-level coverage in the reviewed corpus, not about which record established it first. The exchangeable record explicitly credits the Bernoulli statement as worked out; the shared public date establishes no publication order.

## value

PASS

The exact gap between a familiar conservative one-step descent bound and asymptotic mean-square stability identifies a concrete failure of one-step diagnostics for simultaneous updates. Its full parameter range, boundary witness and explicit example are useful for this model. This assesses the mathematical content, not a distinct addition beyond the broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
