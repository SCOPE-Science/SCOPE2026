# Independent mathematical audit

## correctness

PASS

The source-specific leakage calculation was independently reconstructed from the frozen package and its actual verifier. For g=10/7 and h=8/5, the intended three triads close to machine precision; the cross pair (-p,-qg) uniquely sums to the absent mode k_ext=(1.556836734693878,1.372668410498753)i-coordinate pair with magnitude about 2.0755623777 and distance about 0.64807 from the signed seven-mode support. Substitution into the source helical interaction formula gives nonzero output coefficients for both helicities and derivatives about -0.0101118124 and -0.00135287564 at t=0. A single nonzero absent-mode derivative is sufficient to disprove invariance of the seven-mode Fourier support.

## originality

FAIL

Kishimoto--Yoneda (2022) prove a complete classification of real 3D Euler flows with finitely many Fourier modes: apart from stationary 2D-like and Beltrami flows, there are none. The source triad-triplet solution is explicitly time-dependent and finitely supported, so that older theorem already implies that it cannot be an exact full Euler solution. The audited calculation identifies a concrete missing mode, but the final scientific conclusion is a source-specific certificate of a result already implied by the stronger classification.

## value

FAIL

The explicit leakage coefficient is a useful debugging certificate, but it is a routine source-parameter substitution once one tests closure, and the scientifically important nonexistence conclusion was already settled by a complete finite-mode classification. Under the requested value bar, a narrow mechanically implied diagnostic does not become worthwhile merely because it gives numerical coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
