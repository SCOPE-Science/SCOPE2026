# Independent mathematical audit

## correctness

PASS

Expanding Q_A=v^TAv for v=otimes_j s^(j), independent factor Rademacher signs, shows Q_A-tr A=sum_{nonempty pair patterns P}c_P chi_P. Distinct chi_P are orthogonal Walsh characters, so Var Q_A=sum c_P^2. Pattern groups G_P partition upper-triangular off-diagonal entries and are nonempty, hence all coefficient constraints independent and kernel codimension prod_j(1+binom(d_j,2))-1; g_P=2^(|J(P)|-1)prod_inactive d_j. Orthogonal projection on each group mean-zero hyperplane with symmetric Frobenius doubling yields dist_F(A,K)^2=(1/2)sum c_P^2/g_P; sharp bounds follow. For two factors gmin=2,gmax=max(m,n), so constants 4 and 2max(m,n). SPD witness I4+tK_{+-} has tensor variance 0 or 16t² and ordinary independent-sign variance 8t². Independently enumerated all sign assignments for random symmetric integer matrices in dimensions (2,2),(2,3),(2,2,2), directly verifying variances 96,316,296 and coefficient-count/kernel dimensions. General proof rests on Walsh orthogonality, not these examples. Degenerate D=1 handled separately.

## originality

PASS

Meyer–Avron (2026 journal publication, arxiv:2309.04952) gives an EXACT Gaussian tensor-probe variance with partial-transpose structure, and a Rademacher upper bound rather than this exact Walsh equality and full nullspace. Bujanović–Kressner (2020) address Rademacher rank-one probe unbiasedness and probability inequalities, without the claimed kernel projection/dimension. Classical Hutchinson independent-coordinate variance is inapplicable because tensor entries are dependent. Full theorem plus exact nullspace/distance and positive-definite cancellation contrasts survive these checks. Related tensor-chaos/partial-trace literature remains priority risk.

## value

PASS

Kronecker-structured trace estimators are natural where only tensor-vector products are cheap. Worst-case bounds can be vacuous for a given operator; exact operator-specific variance, a complete zero-fluctuation subspace and optimal distance-to-kernel bounds distinguish cases with zero noise from those with amplified noise. Positive-definite opposing witnesses make this a structural classification, not a renamed textbook Hutchinson moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
