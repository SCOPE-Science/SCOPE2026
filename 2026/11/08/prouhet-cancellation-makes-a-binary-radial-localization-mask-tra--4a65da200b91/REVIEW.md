# Independent mathematical audit

## correctness

PASS

Under the stipulated one-variable Fock norm, polar integration diagonalizes the indicator Toeplitz operator in the unit monomials, and the centered eigenvalues are q_n/2. For h=2^k, binary block multiplicativity reduces q_n to signed samples of the product of k forward differences of the unit-shell average of the Gamma density. Interval averaging bounds the sum of absolute samples by h^(-1)||H||_1+||H'||_1. Each difference integrates a derivative over an interval of its step length, giving the factor 2^(k(k−1)/2); the L1 bound for each Gamma derivative follows from the Rodrigues formula and the Laguerre squared norm n!/r!, for r=k,k+1<=n. This proves the factorial estimate for its full stated range. For k=floor(log(n)/(2 log 2)), both terms have log at most −(log n)^2/(8 log 2)+O(log n log log n), so all positive powers are summable. The Laplace product for the generating series tends to zero as real z increases to 1; absolute summability then gives the exact zero trace. At z=0 the product is strictly positive since the sum of its factor defects converges. This gives both signs for the centered operator, and its compactness fixes the essential spectrum of the uncentered operator. No sharpness or sign pattern is certified. The frozen checker and its documented 120-check success message were inspected as finite corroboration, not executed; the checker uses int.bit_count and therefore needs Python 3.10+ despite the 3.9 floor in the notes. No formal verification or expert attestation is asserted.

## originality

PASS

The radial eigenvalue formula, dyadic Thue–Morse identity and operator-ideal consequences of rapid diagonal decay are established tools. The inspected comparisons do not cover the specific nondecaying Thue–Morse mask's all-index factorial estimate, squared-log upper bound and zero trace. This is a bounded best-of-knowledge judgment for that conjunction, not priority for radial spectral homogenization or for Prouhet cancellation.

## value

PASS

The canonical nonperiodic binary coloring tests whether complete included and excluded shells can coexist with strong spectral averaging for Gaussian localization. The explicit finite-order bound gives eigenvalue control for this fixed mask, and the exact trace separates it from the periodic unit-shell example, which has a different trace. Neither a compactly supported approximation nor an asymptotic density computation answers those questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
