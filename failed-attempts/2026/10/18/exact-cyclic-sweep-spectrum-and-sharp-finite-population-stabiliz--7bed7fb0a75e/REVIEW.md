# Independent mathematical audit

## correctness

PASS

The derivative accounts for current coordinates: c=alpha/N and y_i=-c(sum_{j<i}y_j+sum_{j>=i}x_j). Thus M=-c(I+cL)^(-1)(I+R), where L and R are strictly lower and upper all-ones triangles. Both triangular factors have unit diagonal, so det M=(-c)^N. Independently, in the characteristic pencil the first row is (z+c,c,...,c). Subtract each original preceding row from rows 2,...,N; these become bidiagonal with entries -d,z in columns i-1,i, where d=(1-c)z+c. Expansion yields (z+c)z^(N-1)+c sum_{j=1}^{N-1}d^j z^(N-1-j), including N=1. Multiplying by z-1 and using z-d=c(z-1) gives the frozen numerator. Differentiating at z=1 gives 1+alpha, so the apparent extra root is absent. For 0<c<1, any root with |z|>=1 would satisfy z=(1-c+c/z)^N, contradicted by the strict triangle inequality off z=1. A C^1 map with derivative spectral radius less than one is locally exponentially attracting. At c=1 the roots are distinct nontrivial (N+1)-st roots of unity, giving the matrix identities and exact linear period via a primitive root. For c>1 the product of moduli is c^N>1. Fixed permutations give conjugacy; the logistic slope and synchronous rank-one Jacobian are as stated. Equality is not a claim about nonlinear stability. Independent exact check `python /workspace/checks.py 1` updates basis vectors and checks 48 matrices in dimensions 1–6 at four slopes in two orders, including exact boundary periods. The finite checks corroborate the arbitrary-N proof.

## originality

FAIL

The spectral threshold follows from classical SOR convergence, and the entire characteristic polynomial, including the critical resonance, is a direct pencil substitution into Sun–Ye's existing equicorrelation Gauss–Seidel spectral formula. The nonlinear local interpretation is a standard consequence of the linearization. This is verified earlier mathematical coverage by reduction; it is not based on the unavailable Jiang full texts or on date proximity of Resultary entries.

## value

FAIL

The fixed-sweep question is naturally motivated and the exact resonance is useful to know. However the audited specification needs no further exact invariant beyond the existing equicorrelation spectrum under a direct pencil substitution and textbook SOR/local stability consequences. A self-contained alternate determinant proof and the logistic slope substitution do not establish an independent mathematical gain here. Nonlinear stability at criticality would be a separate question and is not proved in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
