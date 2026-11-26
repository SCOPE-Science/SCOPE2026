# Independent mathematical audit

## correctness

PASS

Reflection fixing the two distinguished sites splits the matrix into odd path adjacency (m−1 sites) and an even tridiagonal chain (m+1 sites) with nonzero nearest-neighbor entries, including sqrt(2) at both ends for all m≥2. The odd polynomial is U_(m−1)(z/2). At gamma=0 the Fourier cycle spectrum gives even factor (z²−4)U_(m−1); reversing endpoints makes the linear terms in gamma cancel, and the two endpoint diagonal perturbations have product +gamma² and leave the odd-size path polynomial as their cofactor (path size m−1, of either parity). The even polynomial is therefore (z²+gamma²−4)U_(m−1). The off-diagonal entries of the even matrix are nonzero, so its eigenspace at any eigenvalue is one-dimensional by the first-row recurrence. At each positive interior coincidence the two distinct mobile energies each double a simple pinned root in the even block, giving J_2 and a separate odd-sector J_1 at each energy. Otherwise below gamma=2 both blocks have simple roots, even though the direct sum shares pinned eigenvalues. At gamma=2, the quadratic root has multiplicity two in the even sector for odd m, and three for even m; in the latter case the odd sector adds just one simple zero. This includes the four-site m=2 case. Exponentiating the largest nonsemisimple real block yields upper and lower norm bounds of the claimed polynomial order, preserved under a fixed similarity; above 2 the positive imaginary energy gives exponential growth. The smallest interior rate is 2 sin(pi/m) and tends to 2 pi/m in ratio. The frozen checker was inspected as source and was not used as a proof or rerun.

## originality

FAIL

The primary paper arXiv:2107.00286 already covers the exact spectrum and the interior collision locations follow from it; the spectrum alone is not a Jordan theorem. More decisively, the full claimed Jordan classification and propagator growth are stated for the identical ring in the distinct Resultary record a67607eb9317, including both parities, m=2, and the off-collision regime. That is complete verified coverage, not a conclusion about who discovered it first. The exact matching record is later-dated than the frozen record.

## value

FAIL

The separation between real spectrum and bounded propagation is a scientifically useful distinction, but in this frozen claim the entire size-uniform classification and sharp rates are already covered for the same ring. The smallest-root asymptotic is a direct elementary consequence; the record establishes no different parameter regime, new observable or stronger theorem that survives that overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
