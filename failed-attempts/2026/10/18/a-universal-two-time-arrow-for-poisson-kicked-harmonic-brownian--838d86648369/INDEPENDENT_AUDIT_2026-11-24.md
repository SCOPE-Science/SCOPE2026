# Independent mathematical audit

## correctness

PASS

The log moment makes the absolute past shot sum well defined: the time integral of min(1,e^(−κs)|Y|) at fixed |Y|=y is y/κ for y≤1 and (1+log y)/κ for y>1. The Brownian convolution exists separately and the linear homogeneous difference decays, giving the stationary law. Independent innovations split the pair as (U,aU+V) with a=e^(−κt) in (0,1). Jumps during (0,t] contribute positive Lévy mass on the vertical axis; the swapped pair has only horizontal and inverse-slope diagonal jump support, hence no such mass off the origin. Lévy uniqueness proves nonexchangeability for each positive t, including D=0 and jumps without ordinary moments. With fourth absolute moment, the common U gives mixed cumulant a^q c_(p+q); c_n=ρE[Y^n]/(nκ) for n=3,4 by time-integrating e^(−nκs). Marginals match; covariance is symmetric, degree-three centered mixed moments are cumulants, and the two degree-four moments have equal three-pairing term 3 Var(Z) Cov(Z_0,Z_t). This verifies signs, the degree threshold from c_3 and c_4>0, and the exact contrasts. Maximizing a(1−a) and a(1−a²) gives the two stated lags; division gives a+a³, strictly increasing on (0,1), so the inversion for κ is exact. Frozen verify.py was inspected, not executed; the recorded 2310 rational assertions are finite checks, not the proof.

## originality

FAIL

The frozen package combines an exactly covered polynomial mechanism with a moment-free nonexchangeability consequence of the classical independent-linear-forms characterization of Gaussian laws. The alternate Lévy-support proof is clean but the same conclusion is already implied; degree, peak, and exact two-lag estimation do not supply a distinct substantive remainder here. No catalog priority order is assigned.

## value

FAIL

A signed thermal-noise-independent witness and its optimal lag are useful, but both are already furnished by the same-model theorem. Taking a ratio of an existing exact curve, enumerating polynomial degrees through four using the existing cumulants, and reproving a classical Gaussian characterization consequence by a support argument do not add a substantial surviving scientific claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
