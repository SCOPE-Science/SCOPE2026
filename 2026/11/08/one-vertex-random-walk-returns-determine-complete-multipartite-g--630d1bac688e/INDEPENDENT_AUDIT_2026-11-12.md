# Independent mathematical audit

## correctness

PASS

For known N>=2, connected K_(n1,...,nr), r>=2 and root v in part i of size a, P decomposes into zero on within-part zero-sum W and invertible quotient Q=uw^T-diag(d_j), d_j=n_j/(N-n_j); determinant=(-1)^r*(1-r)*product(d_j) !=0. Zero spectral weight at v is 1-1/a, recovering a. After removing that atom, quotient diagonal resolvent G(z) yields X(z)=(z-G(z)^(-1))/(d_i+z-G(z)^(-1))=sum_{j!=i}d_j/(z+d_j). Distinct poles -s/(N-s) and positive residues m_s*s/(N-s) recover remaining part sizes and multiplicities. Reversible P has at most N real spectral atoms; the difference of two return measures has <=2N atoms, so equality of moments t=0..2N-1 forces equality by Vandermonde. Without N, rooted K_(a,b) all return p_2t=1/a, p_(2t+1)=0 regardless of b. Algebra checked with independent exact rational quotient/full-matrix resolvents on small multipartitions, not used as unrestricted proof.

## originality

PASS

Best-of-knowledge distinct exact result after comparing named equivalent, broader and database formulations; known subclaims explicitly credited, with residual priority risks.

## value

PASS

Exact one-sensor inverse reconstruction for a natural graph family is a meaningful spectral identifiability theorem: it upgrades general forward random-walk resolvents to constructive part-size recovery, identifies a finite-lag cutoff, and gives a sharp unknown-order obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
