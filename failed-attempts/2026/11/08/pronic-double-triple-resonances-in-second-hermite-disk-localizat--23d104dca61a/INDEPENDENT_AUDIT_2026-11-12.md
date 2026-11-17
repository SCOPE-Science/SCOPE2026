# Independent mathematical audit

## correctness

PASS

The disk STFT/true polyanalytic Fock radial diagonalization gives λ_n(R)=(2n!)^−1 ∫_0^R e^(−t)t^(n−2)P_n(t)^2dt, P_n=t²−2nt+n(n−1), with cancellation at n=0,1. Differentiating e^(−R)R^(n−1)P_n(R)P_(n+1)(R)/(2(n+1)!) gives the exact adjacent difference. For R>0 vanishing is equivalent to P_n or P_(n+1) zero, hence a three-index plateau. P_m(R)=m²−(2R+1)m+R² has at most two integer roots; if two occur, integer Vieta/discriminant constraints give R=k(k+1) and centers k²,(k+1)², separated by 2k+1≥3; no four consecutive equal. λ_m’ vanishes at its center root while adjacent slopes are positive; their ratio m/(m+1) follows by substitution. Verified the differential and characteristic polynomial relationships against the pinned checker code; at m=1, R=2, the exact adjacent slope ratio is 1/2. Finite quadrature in the package is only corroboration.

## originality

FAIL

The complete October26 published theorem “Three-mode disk localization and triangular spectral resonances in the second-excited Hermite sector” already gives the identical normalized eigenvalue integral and adjacent gap product, triples at n±sqrt(n), exactly the same pronic simultaneous double triple centers and prohibition of four consecutive equal labels. It additionally proves a sharper three-candidate norm theorem. The submitted transverse neighboring slope ratio is a mechanical one-line evaluation of the same published derivative/integral and introduces no independent structural phenomenon. Thus the final claim is previously covered, although correct.

## value

PASS

The full second-Hermite resonance stratification and simultaneous spectral degeneracies are mathematically natural in localization theory; indexed triple resonances and exact pronic double centers are useful spectral facts. But their mathematical value was already realized by the earlier stronger theorem. The added elementary slope ratio alone lacks sufficient distinct novelty and mathematical depth to rescue the submitted final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
