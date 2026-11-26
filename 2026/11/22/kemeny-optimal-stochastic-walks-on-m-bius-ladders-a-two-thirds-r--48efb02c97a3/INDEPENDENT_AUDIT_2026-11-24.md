# Independent mathematical audit

## correctness

PASS

The regularized Laplacian inverse trace is strictly convex in all independent edge weights, because its second directional derivative for nonzero symmetric H is twice the squared Frobenius norm of A^{-1}HA^{-1/2}. Rotational averaging preserves feasibility and connectivity; homogeneity of inverse Laplacian eigenvalues then forces a full row budget in the invariant family. The even Fourier gaps reduce to the cosecant-square sum; on the odd grid, the individual gaps are 1+b−(1−b)cos θ, and the surviving Poisson terms are signed by (−1)^ℓ at frequencies ℓm. This gives the claimed F_m. Differentiating the cosecant-square grid sum twice, with (csc² x)''=6csc⁴ x−4csc² x, yields the fourth-power sum (m⁴+2m²)/3. The source has a form-feed in the displayed fraction at line 77, but the recovered identity and its use in F_m'(0)=−(m²−1)²/6 are correct. Strict convexity and divergence at b=1 prove uniqueness and interiority. M_4 and M_6 are K_4 and K_{3,3}, giving equal weights; for m≥4 the displayed lower bound at b=1/3 is positive. For b=c m^{-2/3}, m√b grows as m^{2/3}, making q^m exponentially small; scaling F_m' by m² gives 1/6−1/(4c^{3/2}). Root bracketing and expansion of the two terms then give the claimed correction, while b=1/3 yields m²/4+O(m). This proves the penalty 3/2. The exact inverse-trace reproduction uses full rational matrices, not Fourier eigenvalues.

## originality

PASS

There is exact prior coverage of the unweighted Kirchhoff index, hence the fixed equal-edge benchmark, and distinct prior optimization of this graph for SLEM and for a weighted spanning-tree determinant. Those results do not imply the stochastic inverse-trace optimizer. A distinct, same-date squared-cycle entry shares the two-thirds scale and objective, but concerns a different set of edges and cannot give the exact Möbius allocations by relabeling. The exact Möbius Kemeny entry is the assigned record itself, not independent coverage. Best-of-knowledge judgment, limited to the inspected evidence.

## value

PASS

On a natural cubic graph family this distinguishes two objectives by a qualitatively different conductance scale and by whether holding is beneficial. The exact unrestricted optimizer, correction term, and asymptotic penalty explain a genuine optimization feature not visible from the unweighted Kirchhoff formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
