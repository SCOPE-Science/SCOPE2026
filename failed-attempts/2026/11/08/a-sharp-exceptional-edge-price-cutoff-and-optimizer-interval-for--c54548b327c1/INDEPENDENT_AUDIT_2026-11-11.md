# Independent mathematical audit

## correctness

PASS

For the centered path coordinate v_i=(n+1)/2−i, the Rayleigh quotient bounds λ2 by (Σw_i+(n−1)^2z)/[n(n²−1)/12]. Parabolic path weights w_i^0=(λ0/2)i(n−i) attain λ2=λ0, with exact path spectrum λ0 k(k+1)/2. Equality at c=(n−1)^2 forces the affine weights w_i(z)=w_i^0−(n−1)z. The second-eigenspace positivity bound on f⊥{1,v} yields the generalized Rayleigh cutoff; disconnection at z=λ0/2 ensures it binds before edge nonnegativity. Rescaling an interior critical design proves strict gain for c below threshold. Independent SymPy reconstructed the C5 weighted Laplacian, checked the centered eigenvector and the complete displayed characteristic polynomial. The exact n=5 radical follows by quadratic crossing; these finite checks supplement the uniform-n polynomial spectral proof.

## originality

FAIL

This *entire* finding is a direct specialization of the already published complete theorem "Mass-independent edge screening and complete critical optimizers for priced reversible cycles" (Resultary, 2026/11/2): set all vertex masses m_i=1 and path prices p_i=1 in its n≥3 theorem. Its q_c=(Σ√p_i)^2 becomes (n−1)^2; its w_i^0 and critical affine family become exactly the present ones, and its full critical optimizer interval has the same generalized Rayleigh endpoint. The n=5 radical was also published explicitly in "The exact price transition for fastest mixing on a five-cycle" (2026/10/12). Difference in notation and exclusion of n=4 cannot make a corollary original.

## value

FAIL

The mathematical cutoff and optimal face are meaningful in isolation, but the present package contributes no new independent exact invariant, classification, or substantive structural lemma beyond the earlier all-mass, arbitrary-edge-price theorem, and its five-cycle radical is independently already published. As a duplicative specialization, the claimed new finding has no incremental mathematical value; correctness and reproducibility cannot rescue known coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
