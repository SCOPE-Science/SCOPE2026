# Independent mathematical audit

## correctness

PASS

For m>=2 and ell>=3, the hub-deleted tridiagonal block D has Dirichlet modes sin(jk*pi/ell). The even j=2 Dirichlet mode supported on any single petal has zero coupling at the hub, proving m independent obstructions and that every size-m coordinate set meets each petal and omits the hub. For a chosen hub-neighbor per petal, the PBH test splits into h=0 (tridiagonal recurrence), odd j resonance (nonzero Fredholm product), even j resonance ((m-1)*mu_j*h=0), and nonresonant eigenvalues (reflection yields hypothetical lambda=2m). Interlacing against the m hub-deleted paths gives lambda_2<4<=2m; the embedded hub star forces lambda_1>=2m+1, excluding 2m. Thus all parameter quantifiers and forced zero-forcing failure are proved analytically, not inferred from the exact rank checks. Independently rebuilt unweighted integer Laplacians and exact sympy Krylov ranks for all (m,ell) with m=2..3 and ell=3..6; 8 cases succeeded. The known Z=m+1 is not a new theorem.

## originality

PASS

Best-of-knowledge: the graph-specific fixed unweighted-Laplacian PBH optimal actuator set and necessity of one input per petal do not follow from the known zero-forcing value m+1, qualitative all-weights controllability characterizations, or same-graph characteristic polynomial calculations. The latter establish spectral factors but not eigenvector restrictions on explicit actuator positions. No earlier full-family placement result was found in semantic Resultary search. The ell=3 or 4 subfamily might be derivable from a cograph theorem and the m lower bound may follow from the graph spectrum; no novelty is claimed for these background ingredients.

## value

PASS

Dedicated fixed-Laplacian leader count and placement are natural structural invariants for symmetric networks. For every nontrivial petal length the optimum uses exactly m inputs while zero-forcing requires m+1 and EVERY minimum actuator placement stalls zero forcing. This is a motivated all-parameter limitation of a common sufficient design method, not a tiny instance or routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
