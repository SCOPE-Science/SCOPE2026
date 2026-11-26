# Independent mathematical audit

## correctness

PASS

Equality of the full-circle squared Fourier magnitudes is equivalent to equality of every aperiodic autocorrelation, and coordinate magnitudes fix the support. After fixing the first coefficient to A>0, the outermost lag fixes the last coefficient C, giving immediate uniqueness for one or two nonzero points. For three points with unequal successive gaps, one lag isolates the middle coefficient. For equal gaps, middle candidates B,D obey A(D−B)+C·conj(D−B)=0 and |D|=|B|. Unequal endpoint magnitudes force equality; equal endpoint magnitudes reduce to a prescribed real part on a circle after a rotation. The other possible point gives precisely conjugate reflection times a unimodular scalar. For the four taps, expansion gives coefficientwise conjugates, all nonzero, and on the full circle the two quadratic factors have modulus |2cos(theta)±i s|. The shared support permits no nonidentity shift, the first tap fixes the scalar, and unequal endpoint magnitudes exclude conjugate reflection. These checks cover all s,t in the stated range. As a direct exact replay, the witness at (1,2) has nonnegative-lag autocorrelations (15,−8,5,−2) for each signal, obtained by summing the lagged products. The algebra in RESULT.md lines 24–79 is an all-parameter verification; the supplied finite-grid verifier was not executed as part of this audit.

## originality

FAIL

Beinert and Plonka's 2016 Theorem 3.6 directly covers the four-tap existence and constructs exactly this entire two-parameter family up to data-preserving frequency shifts, exchange, and common reversal/scaling. It is not just an example with the same support cardinality. Their Theorem 2.2 and Lemma 2.3 also give the only potentially nontrivial lower-bound case by a short degree-two specialization; the other gaps have isolated autocorrelation terms. No claim that the earlier paper explicitly states the arbitrary-location cutoff theorem is needed for the failure: the lower bound and the exact construction follow mechanically from those comparisons.

## value

FAIL

The least-support question is natural and the treatment is a clear exposition, but the exact example and full proposed family are a reparameterized known construction. After that coverage is credited, the lower-bound remainder is a two-root specialization of the known general classification plus the elementary fact that unequal gaps isolate the relevant lag. No substantively new obstruction, ambiguity phenomenon, or classification survives in the original claim; making the known example an integer witness does not supply one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
