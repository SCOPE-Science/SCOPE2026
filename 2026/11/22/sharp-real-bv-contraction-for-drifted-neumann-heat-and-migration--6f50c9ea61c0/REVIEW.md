# Independent mathematical audit

## correctness

PASS

Differentiate the backward Neumann equation for smooth data to get the Dirichlet heat equation with drift b. For BV data, extend by its one-sided traces and mollify. L1 convergence of functions and weak convergence of derivative measures against the positive-time kernel give the same formula, without assuming strong BV-norm approximation of a jump. The Dirichlet gauge exp(b(y-x)/2-b²t/4) has the correct sign; integrating in x identifies survival from y with reverse drift -b. Positivity gives the total-variation upper bound by the maximal column mass; a single jump attains each column mass, and support of the variation measure on the unique maximizing point proves all nonconstant equality cases. The Gaussian finite-grid Prékopa argument gives a log-concave limit: any touching path that does not cross immediately has probability zero by boundary regularity and the strong Markov property, and hitting exactly at t is a null event. Analyticity, positivity and boundary zeros then give uniqueness and an interior maximum. Strict submultiplicativity follows from integrating strictly submaximal column mass off this one point against the strictly positive kernel. The sine coefficients follow by integrating exp(-by/2). For short time, the killed image expansion minus the two one-sided losses has exponentially smaller first spatial derivative near the midpoint: all omitted image distances, including the tails of the one-sided reflected integrals beyond the opposite endpoint, are at least 5/4 for y in [1/4,3/4]. The two leading absolute first-passage slopes are exp(-(y-bt)^2/(4t))/sqrt(pi t) and exp(-(1-y+bt)^2/(4t))/sqrt(pi t) with uniform relative O_b(t) near the midpoint, by differentiating the reflection formulas and applying Mills' expansion to the tilted tails. Their ratio is exp(-(y-1/2-bt)/(2t)). Evaluate at y=1/2+bt±M_b t² with M_b sufficiently large: the derivative changes sign, proving the required bracket without having to assume O(t) localization first. The two reflection tails at that critical point each contribute 4 sqrt(t/pi) exp(-1/(16t)) to the exit probability, establishing the drift-neutral leading prefactor. At large time the first mode has curvature -(pi²+b²/4) times its value at its peak; for the tilted second sine mode, its derivative divided by the first mode at that point is -2pi sin(pi y_infty). This recovers c_b from the ratio of sine coefficients. The next spectral gap is 8pi², so the quadratic implicit-expansion error O_b(exp(-6pi²t)) dominates it. The independent replay `python3 /workspace/branches/frozen_review_checks.py` (section 3, passes) integrates tilted Gaussian images at 85 digits and confirms the spectral formula, short-time scaling for three signed drifts, and the first long-time correction for two nonzero drifts at selected times. The supplied checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the combined sharp BV norm, optimizing-jump classification, and explicit two-end optimizer laws. Differentiation, fixed-start survival, log-concavity and spectral theory are known inputs. Nearby indexed claims are materially related, but their available statements are for different functionals or geometries, not this full statement.

## value

PASS

The exact operator norm and equality profile answer a natural sharp stability question for reflecting diffusion that qualitative contraction cannot answer. In particular the worst jump shifts by order t with nonzero drift, although the leading norm deficit has the same asymptotic prefactor and exponent as at zero drift. Its distinct late relaxation scale and coefficient give quantitative information beyond using the principal eigenfunction for norm decay alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
