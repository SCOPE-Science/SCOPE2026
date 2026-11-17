# Independent mathematical audit

## correctness

PASS

The pairing of two permutation matrices is the number of fixed points of the relative permutation modulo two; therefore the Fourier restriction is the central convolution with z^Fix(g) at z=-1. Frobenius character theory gives (1/n!) sum z^Fix chi_lambda=s_lambda[p1=z,pj=1 (j>=2)]. Setting a=z-1 gives sum e_k u^k=(1+u)exp(a u), e_k=a^(k-1)(a+k)/k!. For conjugate lambda=(n-4,3,1), the explicit three-by-three dual Jacobi--Trudi determinant reduces to the displayed product after multiplying by n!/d_lambda. The hook-length formula gives d=n(n-1)(n-3)(n-6)/8 and regular multiplicity d^2. For |z|=1, the quadratic term cannot vanish since |z^2+(n-4)z|<=n-3<n-1. The exhaustive 15 partition sectors at n=7 have a unique zero eigenvalue in dimension 21 and degree-square sum 5040; exact nullity is 441. Independently checked all n=7..20 symbolic determinant identities and the full n=7 table; finite checks do not prove all n.

## originality

PASS

Classical Frobenius/Schur machinery permits this computation, but the relevant inspected prior results address trivial-character fixed-point polynomials, a derangement adjacency class function, or other symmetric-group Fourier blocks; none inspected implies the specified (3,2,2,1^(n-7)) factor, binary parity singularity and quantified nullity. Historical priority is only best-knowledge; same-day related published works are not chronologically ordered.

## value

PASS

The object is a natural binary Fourier submatrix indexed by permutation matrices; exact failure of self-sampling injectivity in every n>=7 is a nontrivial representation-theoretic obstruction. The infinite Specht-sector factor and exact first seven-letter rank are independently useful, rather than a renamed character formula or arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
