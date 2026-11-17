# Independent mathematical audit

## correctness

PASS

PASS: In squared-radius variable u with v=1-u, the disk and outer-annulus radial Gram matrices are G_ij=B(m+1,i+j+1), B_ij(eps)=int_0^eps v^(i+j)(1-v)^m dv, and their generalized eigenvalues are concentration eigenvalues (common pi cancels). Since B(eps)/eps tends to e_0e_0^T, lambda_max/eps tends to (G^-1)00=(n+1)(n+m+1), the Jacobi endpoint Christoffel kernel. Write B=D_eps(H+O(eps))D_eps, D_jj=eps^(j+1/2), H_ij=1/(i+j+1). Then eps^(2n+1) B^-1G tends to (H^-1)nn e_ne_n^T G, whose only positive eigenvalue is (2n+1)binom(2n,n)^2 B(m+1,2n+1); reciprocation gives sharp lambda_min and spectral condition number. At n=1, m->infinity with eps=tau/(m+1), the measure tends to exp(-x)dx, so the two eigenvalues of its 2x2 [1,1-x] restricted moment Gram matrix are Lambda_+/-=1-e^-tau(1+tau^2/2) +/- tau e^-tau sqrt(1+tau^2/4). Positive mass on both sides gives 0<Lambda_-<Lambda_+<1. Independent high-precision beta-moment generalized eigenvalues at three (m,n) pairs and two thicknesses matched leading constants; finite checks corroborate but do not prove fixed-n or m-growing limits.

## originality

PASS

Qualified PASS: Related Zernike/Jacobi and Slepian papers concern constructing bases, PDE operators or different ball/Fock localization; no inspected older result gives this disk-norm outer-annulus generalized-eigenvalue condition number coefficient together with n=1 high-m Laguerre crossover. The endpoint Christoffel/Hilbert and Laguerre ingredients themselves are classical; residual classical moment-method equivalence and inaccessible annular-Jacobi primary full-text risk are recorded.

## value

PASS

PASS: Observability and conditioning of a natural finite Zernike azimuthal subspace under only thin-ring measurements is a motivated inverse problem. The precise eps^(-2n) divergence with coefficient and the noncommuting large-azimuthal scaling identify meaningful numerical-conditioning boundaries; not an arbitrary one-off small calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
