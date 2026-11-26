# Independent mathematical audit

## correctness

PASS

The comparison is for periodic alternating P1 elements with n divisible by four. The diagonal and absolute row radius of M are (a+b)/3 and (a+b)/6; the constant and alternating vectors realize both Gershgorin endpoints, so Jacobi gives 3. Independently taking traces and determinants of the cell symbols, the two-symbol product for the identity weight has trace 1+qu/6 and determinant (3q+2u)^2/144, where q=r+1/r and u=4-cos(theta). The eigenvalue branches in the proof follow. The upper branch increases to u=5, a discrete phase available because n/2 is even. The lower branch is always at least 1 and its continuous minimum is at u=3q/2 (with u=3 at r=1). For r>=3 it minimizes on the phase set at u=5; below r=3 the stated bound suffices without replacing the discrete minimum by the continuous one. The equality condition on the exact branch is 3r^2-6r-13=0, with its sole admissible root 1+4/sqrt(3). Local diagonal-mass weights give diagonal 4/(a+b) and neighbor entries -2h/(a+b)^2, proving the stated polynomial in M. Its mass-product eigenvalue is 1+4ab sin^2(theta/2)/(3(a+b)^2), giving the claimed maximum, minimum, and limit. An independent rational four-mode check at n=4, r=4 confirms the complete spectra and the reported strict ordering.

## originality

PASS

Best-of-knowledge pass for the exact alternating-periodic spectra, sharp identity-weighted BRAS/Jacobi contrast reversal, and exact diagonal-local-mass comparison. The BRAS definitions, general lower bound, contrast-induced degradation, diagonal weighting remedy and its approach to unit conditioning on a graded example are already established in the inspected antecedents.

## value

PASS

The alternating family separates the effect of contrast from mesh order and supplies a sharp all-size benchmark beyond qualitative warnings about grading. It gives both the range in which the original BRAS improves on Jacobi and a reproducible regime in which it is strictly worse, while bounding the weighted counterpart for every contrast. This is an exact, motivated counterexample and design comparison, not a claim that weighting or grading effects were newly discovered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
