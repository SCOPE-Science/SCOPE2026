# Independent mathematical audit

## correctness

PASS

Completing the square in the Gaussian correlation gives (2s)^(-1/2) exp(−πs(j−k)²/2); Fourier series on the coefficient circle then give the theta multiplier, multiplied by |1−t exp(−2πiξ)|² after filtering. The sharp bounds are its continuous extrema, and bounded invertibility of the filter for t≠±1 gives the same closed span. The Jacobi product has positive increasing affine factors in u=cos(2πξ); the sum of their logarithms has negative second derivative. The logarithm of the positive affine filter factor is concave, so minima are at endpoints and the maximum is unique. At endpoint equality the maximum is interior and both endpoints are strictly below every interior value. Endpoint equality yields the stated t_s; the interior derivative equation follows with convergence for fixed 0<q<1. For t between 0 and t_s normalization by the left endpoint yields a strict pointwise decrease away from that endpoint because t/(1+t)² is increasing. After t_s normalization by the right endpoint gives a strict increase away from it because t/(1−t)² is increasing. Comparing at a maximizer away from the minimizing endpoint gives strictness for the max/min ratio. Negative t in (−1,0) increases the unfiltered endpoint ratio; F_t=t²F_(1/t) covers |t|>1. For small q, (H−J)/(sqrt(H)+sqrt(J))² expands to q+q³+O(q⁵). The q and q³ terms in the multiplier cancel, giving uniformly 1+q²−4q²u²+O(q⁴); the value at zero and the upper envelope pin down the maximum, yielding 1+4q²+O(q⁴) after division by the endpoint minimum. This is the squared bound ratio, not its square root.

## originality

PASS

The distinct claim is the exact fixed-width global minimax for a real filter with two adjacent taps, with reciprocal minimizers, extremal-frequency information, and sharp weak-overlap excess. The periodized Riesz criterion, Gaussian theta multiplier and unfiltered bounds are prior work.

## value

PASS

An invertible filter with only one neighboring translate is a minimal local modification of the representation of the same space. The exact optimal coefficient and worst-frequency equation specify the best such preconditioner at every width. The drop in excess from order q to order q² is a genuine rate improvement for this restricted family, not just a numerical gain at one width; the proof shows it need not trade away the shift-invariant subspace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
