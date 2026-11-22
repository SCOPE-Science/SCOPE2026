# Independent mathematical audit

## correctness

PASS

PASS. In a rank-k paving matroid (2<=k<n), each (k-1)-set is independent, so every missing k-set S closes to one unique rank-(k-1) hyperplane H. Every replacement (S\{s}) union {j} with j outside H is a basis. Their uniform average y has deficits exactly 1/k on S, zero on H\S, and mass 1/(n-h) outside H. For any z in the base polytope, rank(H)<=k-1 forces a=sum_{outside H}z_i>=1, and b=sum_{H\S}z_i>=0. Disjoint-block Cauchy gives ||1_S-z||²>=(a+b)²/k+a²/(n-h)>=1/k+1/(n-h); y attains it, and equality uniquely specifies y. Tight rank plus coordinate-zero constraints expose a product of (k-1)- and (n-h-1)-simplices; its intrinsic Euclidean volume is sqrt(k(n-h))/((k-1)!(n-h-1)!). Distinct large hyperplanes cannot share k-subsets; hence histogram multiplicities lambda_h*binom(h,k). Convexity of distance maximizes on hypersimplex vertices; variance identity for residuals with pairwise distinct nonbasis residuals strictly excludes nonvertex maximizers. Independently evaluated the n=8,k=3 two-hyperplane non-sparse case with exact rational projection witness averages and 42 zero, 4 at 7/12, and 10 at 2/3 squared distances. No claim of arbitrary-norm or non-paving projection.

## originality

PASS

Best-of-knowledge PASS for non-sparse paving metrics and hyperplane-size tomography; the constant-h sparse-paving subcase is prior covered and excluded as a new standalone finding.

## value

PASS

PASS: Complete non-sparse paving hyperplane-size metric tomography is a mathematically natural inverse invariant, distinguishing same-rank matroids by all missing-vertex distances. The exact nearest face, Hausdorff maximizers and heterogeneous shell histogram are not routine Ehrhart coefficient substitutions; the non-sparse h>k regime and inverse recovery give substantive value beyond the known sparse case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
