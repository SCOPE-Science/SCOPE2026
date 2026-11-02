# Independent mathematical audit

## correctness

PASS

For n≥1, 1≤k≤n, alpha>k+1, f0>0, beta=C(n,k) and m=alpha−k−1>0, the constant support R*=f0^(−1/m) is stationary by f0 R*^m=1. In inverse Gauss coordinates r[u]=(u^2+|∇u|^2)^(1/2), b[u]=∇²u+ug; at u=R* the first variations are δr=phi and δb=∇²phi+phi g. The curvature quotient equals sum over k-element subsets of products of inverse principal radii; differentiating at R*I gives DG[eta]=−C(n−1,k−1)R*^(−k−1)tr eta=−(k beta/n)R*^(−k−1)tr eta. Inserting into u_t=−f0 r^alpha G(b)+beta u gives Lphi=(k beta/n)Δphi−beta m phi. As ΔY_l=−l(l+n−1)Y_l, the claimed lambda_l follows for every l≥0. Degree zero alone has decay beta m; degree one is the least nonconstant rate beta(m+k)=beta(alpha−1), so the gap is beta k. Endpoint k=n and n=1 have the same binomial identity; alpha=k+1 is excluded, and no nonlinear faster-rate theorem is inferred.

## originality

FAIL

The exact eigenvalue expression is not printed as a stand-alone theorem in the inspected sources, but is an immediate standard spectral consequence of the already-published normalised support PDE. Li–Sheng–Wang (2020), equations (1.8), (2.13)–(2.16), and Sheng–Sheng–Yang (2026), equations (2.11), (2.12), (2.21), supply the same scalar equation, the curvature-radius tensor and its first derivative. At an isotropic radius tensor, symmetry and binomial counting give DG[eta]=−C(n−1,k−1)R^(−k−1)tr(eta); the standard sphere-Laplacian eigenvalues then yield the full submitted spectrum with one substitution. Thus this is a direct textbook first-variation/spectral corollary of prior published identities, not a mathematically distinct new result. Absence of the precise displayed formula or title in the papers does not defeat the implication comparison. This judgment does not assert that the formula was explicitly tabulated in those papers.

## value

FAIL

The full local spectrum and decay gap are natural diagnostics of an important normalized curvature flow, but in this package they result only from substituting the standard first variation of the already-published support equation into the classical unit-sphere Laplacian eigenvalues. The βk gap is the immediate difference of the l=0 and l=1 eigenvalues, and the global sharpness via homotheties was already established by Sheng–Sheng–Yang. No nonstandard structural lemma, independent asymptotic theorem, motivated boundary/counterexample or new classification mechanism is proved. The computation is a routine local linearization rather than a substantively independent mathematical contribution. Degree-one modes are translation/centering directions, further qualifying the claim that this necessarily represents intrinsic shape relaxation; no nonlinear improvement is asserted or proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
