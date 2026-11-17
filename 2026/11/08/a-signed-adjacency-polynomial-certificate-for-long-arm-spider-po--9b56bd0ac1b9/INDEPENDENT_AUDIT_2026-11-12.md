# Independent mathematical audit

## correctness

PASS

For ell>=2k-1 the largest k path eigenvalues lambda_j=2cos(j pi/(ell+1)) satisfy lambda_1>...>lambda_{k-1}>0 and lambda_k>=0. The monic p(x)=prod_{j=1}^k(x-lambda_j) has alternating coefficients with positive relevant elementary symmetric polynomials. The tree is bipartite, so every walk from vertices distance d contributes to p(A) with the same sign (-1)^(k-d) and the unique length-d path makes the entry strictly nonzero for d<=k; d>k vanishes by degree. Arm-contrast sine path eigenvectors of each lambda_j give k(m-1) independent nullvectors; the established zero forcing bound Z<=k(m-1) and M<=Z prove equality. Independently formed representative p(A) for m=3,4, k=3,4 at boundary ell>=2k-1 and checked signs/nullity; those finite cases corroborate, universal result uses exact polynomial and eigenvector proof.

## originality

PASS

Numerical Z=M=(m-1)k for these graph powers is fully covered by the published stronger unequal-arm theorem, and the older Abiad et al Theorem 20 gives conditional general polynomial spectral bound. The new claim explicitly excludes numerical novelty. Neither source constructs this particular top-k-path-eigenvalue polynomial of the *unweighted* spider adjacency nor its exact universal distance sign (-1)^(k-d) and explicit arm-contrast eigenbasis. The earlier optimal symmetric integer matrix is built from sliding-window blocks, not the same spectral functional calculus; no implication of the precise signed canonical matrix follows from M equality.

## value

PASS

The canonical unweighted adjacency polynomial is an exact, fully supported, signed-layer and optimal-nullity spectral certificate on an infinite natural family. It specifies an actual optimal matrix and sign regularity not implied by numerical zero forcing; such constructive spectral matrices are natural inputs to signed-pattern rank and eigenvector analyses. Motivation is the certificate itself, not a false novelty claim for known M.

The dated certificate retains the supplied scientific assessment, sources and limitations.
