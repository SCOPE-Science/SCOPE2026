# Independent mathematical audit

## correctness

PASS

For exact-degree harmonic cubics the sphere Laplacian eigenvalue is 3(d+1); both sphere and corner measures are probability-normalized. The singleton sign-character block consists of x_i(a x_i²+Σ_{j≠i} b_j x_j²) with 3a+Σ b_j=0. Off-axis permutations split it into the line Z_i and the zero-sum contrasts Q_{i;jk}, of dimension d−2. Each triple character supplies the single square-free line R_{ijk}. For both Hermitian forms signs separate distinct characters, the permutation-invariant pairing of the line with contrasts is zero, and each contrast Gram form is scalar on the standard zero-sum coordinate space. Permutations also identify ratios across blocks of a given type. At a corner the projected gradient of Z_i is (3/d−3/(d+2))(e_i−x_i x), giving energy 36(d−1)/(d³(d+2)²); Q vanishes at corners but has ambient (already tangent) energy 8/d²; R has ambient energy 3/d² and radial squared component 9/d³. The sphere squared norms of these representatives computed from degrees two, four and six are respectively 6(d−1)/(d(d+2)²(d+4)), 4/(d(d+2)(d+4)), and 1/(d(d+2)(d+4)). Dividing by 3(d+1) times these norms verifies all three branches including d=3 and their multiplicities. Only R vanishes for d=3, hence rank six. The ratios T/Z=d(d+2)/3 and S/Z=(d−3)(d+2)/2 exceed one for d≥4, and T/S=2d/[3(d−3)] gives the exact tie at 9. The condition numbers refer respectively to the ratio of squared singular values and its square root. RESULT.md, VERIFICATION.md and check_cubic_gradient.py were inspected, not executed; the reported d=3–7 Gram checks do not supply the arbitrary-dimensional argument.

## originality

PASS

Best of current knowledge, the exact gradient-only spectrum on the full-support signed cube is distinct. Same-node scalar results and a same-day different-node gradient result are strong method-level overlaps, not the same spectral result.

## value

PASS

The cube is a natural orbit and gradient-only reconstruction is materially different from scalar interpolation. The exact branches quantify the rank recovery in d≥4, the surviving cubic blind mode in d=3, and the transition determining the sharp upper bound and condition growth. These are directly usable quantitative recovery bounds for the specified nodes and norm; finite full-rank checks, scalar interpolation ranks or a general derivative evaluation algorithm do not give them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
