# Independent mathematical audit

## correctness

PASS

With independent coordinate inputs and real symmetric L, PBH tests injectivity of evaluation on each eigenspace. The one-edge change is (t−1)bbᵀ, b=e_000−e_100. With z_j=(−1)^x_j, the fixed eigenspaces at 2 and 4 are spanned by (z_2,z_3) and (z_1(z_2−z_3),z_2z_3), respectively. Constants give the sole zero mode because all t>0 considered give a connected positive network. The remaining space is spanned by z_1,z_1(z_2+z_3),z_1z_2z_3; in an orthonormal basis the diagonal 2,4,6 has a rank-one perturbation with every coordinate of its perturbation vector nonzero. For t≠1 no perturbed eigenvalue can equal a diagonal entry (the determinant lemma gives values −4(t−1),4(t−1),−4(t−1)), and none can repeat: a repeated eigenspace would contain a nonzero vector orthogonal to the perturbation vector, hence an eigenvector of the unperturbed diagonal matrix, which is impossible. The evaluation determinant at 2 forces opposite transverse parities and excludes singletons. Those parities also make the evaluation rows at 4 independent: the even row is (0,1), the odd row has nonzero first entry. A vector of the moving space vanishing on such a pair must be proportional to z_1(z_2−s)(z_3−s), where s=z_2=z_3 at the even site. Its support is the opposite transverse edge, and a transverse unit neighbor outside the support has exactly one nonzero support neighbor. The Laplacian applied to it is nonzero there, ruling out an invisible eigenvector. This proves the sixteen placements (four choices from each class). At t=1 the eigenvalue-2 and eigenvalue-4 spaces both have dimension three and their three-row evaluations on the stated triple have determinants of moduli four; the one-dimensional modes are visible. Independent replay: python3 /workspace/reproduce_reviews.py 3 (SymPy 1.14.0) directly constructed the Laplacian, reproduced the characteristic polynomial, and used exact Gram determinants of full Kalman matrices for all sixteen predicted placements. Each determinant vanishes to order four in δ=t−1 at zero and its remaining factor has no real roots in (−1,0) or (0,∞). Sum-of-squared-minors gives the exact rank interpretation. The script additionally checked all pairs at t=1/2,1,2 and the uniform triple; analytically excluded placements rely on the fixed PBH eigenspace, not on those samples.

## originality

PASS

The supported distinct claim is the exact coordinate-pair table as one parity rule for every positive nonunit weight, not the homogeneous minimum, the PBH method, or unrestricted multiplicity-based controllability. Inspected results and related one-link defect records do not yield that classification.

## value

PASS

The cube is a basic graph with multiple symmetric diffusion modes, and a single perturbed edge is a natural test of exact dedicated placement under broken symmetry. The result decides all location choices and every positive weight, rather than one generic rank example or an unmotivated small search. The lack of extra exceptional weights and the precise transverse control rule are useful when a pair of sites must be chosen without knowing the detuning magnitude. No robustness or quantitative control-energy bound is claimed near t=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
