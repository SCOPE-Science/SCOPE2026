# Independent mathematical audit

## correctness

PASS

PASS: In J(n,2) with degree 2(n-2), common-neighbor algebra A²=(d-4)I+(n-6)A+4J and AJ=dJ reduces RK4 polynomial to I,A,J. Adjacent entries are h*F_n(h)/24, nonadjacent entries h²[12-(12n-8)h+(7n²-10n+4)h²]/6; the latter quadratic has negative discriminant, and diagonals are strictly positive since r(z)=1-z+z²/2-z³/6+z⁴/24>e^-z for z>0. F_n is strictly decreasing: derivative quadratic discriminant -16 Q(n) where Q(4+t)=209t⁴+2092t³+7616t²+11808t+6480>0. Thus exact all-h positivity interval [0,tau_n]. Nonzero Laplacian eigenvalues are n,2(n-1), giving spectral stability [0,alpha/(2(n-1))] where alpha³-4alpha²+12alpha-24=0; exact comparison identity shows equality only n=4 and strict positivity/stability separation for n>=5. Scaled cubic root yields n*tau_n->gamma=1.0389..., ratio 2gamma/alpha≈0.746. The adjacency algebra gives same result for any strongly regular graph with identical parameters. Independently exact rational checks for n=4..6 validate matrix entries, not universal n.

## originality

PASS

PASS (best-of-knowledge): general SSP RK stability results and prior sharp RK4 positivity work for paths, cycles and complete multipartite graphs do not cover triangular/Johnson J(n,2) (different adjacency algebra and eigenvalue spectrum). Contemporary Radau IIA positivity on triangular graphs is a different numerical method. No prior exact J(n,2) RK4 F_n(h) or sharp asymptotic stability-versus-positivity gap appeared in targeted search.

## value

PASS

PASS: The sharp universal end-step positivity interval and strict quantified separation from absolute stability for a classical named graph family are mathematically useful for positivity-preserving discretization. The strong-regular-parameter extension includes nonisomorphic Chang graphs. It is a motivated structural classification, not merely an arbitrary single matrix evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
