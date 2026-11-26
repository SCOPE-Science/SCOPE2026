# Independent mathematical audit

## correctness

PASS

At a stationary time, the independent backward Poisson intervals have rate r. Conditional on their lengths, the reset sum is centered Gaussian with covariance (2D/r) T_q I_d, where q=b² and T_q=Σ_{j≥0} q^j E_j with iid unit-rate exponentials. This proves the sign invariance and gives P_d=(r/(4πD))^(d/2) E[T_q^(−d/2)]. The stationary construction converges in L²; shared-noise coupling shrinks an arbitrary initial displacement by a^{N_t} almost surely, proving uniqueness. The radial Fourier transform Φ_b(u)=Π_{j≥0}(1+b^{2j}u²)^(−1) is bounded at large u by any fixed finite leading product, giving integrability against every polynomial and hence a bounded smooth density. The identity Φ_b(bu)−Φ_b(u)=u²Φ_b(u) gives I_{d+2}=(b^(−d)−1)I_d and C_{d+2}/C_d=1/(2πd). For d=2, integrate [Φ_b(bu)−Φ_b(u)]/u; Tonelli with the decreasing function's derivative integrates over v≤u≤v/b, giving I_2=log(1/b). For the odd anchor the tail of the log product is bounded by u²b²/(1−b²), and Φ_b(u)≤1/(1+u²), so I_1→π/2 by dominated convergence. Iteration gives the exponents n(n−1) and n² and the stated constants, including the finite d=1 limit. At b=0 the conditional variance uses only E_0, whose inverse d/2 moment diverges for d≥2. All contraction limits keep d,D,r fixed. Replay: verify.py lines 16–39 and 59–89, inspected, not run; VERIFICATION.md lines 19–23 records 30 exact-law and 8 endpoint quadrature comparisons, largest relative discrepancy 0.019803931. Finite log-frequency truncation and tolerances corroborate sampled values only.

## originality

FAIL

The full contact law, including the claimed planar anchor, dimension shift and both parity asymptotics, is a direct specialization of a published stronger Mellin transform, not merely similar to a one- or three-dimensional resetting result. The stationary contact is the negative moment at s=−d/2 of the very same weighted-exponential variable in Bertoin–Biane–Yor (2004), Eq. (1.3) and Theorem 1.1(i), Eq. (1.7). The frozen proof's frequency integral is equivalently that same negative moment times Γ(d/2)/2. This is positive prior-coverage evidence, not a priority inference from failed access or a title match.

## value

FAIL

The contact density is a naturally motivated diagnostic, and the direct elementary derivation is readable. But the frozen contribution is an exact contact law obtained mechanically from a stronger known invariant of the identical effective-time distribution. The planar anchor, ladder and parity hierarchy are all covered, including fixed-rate prefactors after rescaling; the package supplies no additional nonmechanical conclusion about the resetting process. Re-expressing the Mellin identity or reproducing its values by quadrature does not establish an independent scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
