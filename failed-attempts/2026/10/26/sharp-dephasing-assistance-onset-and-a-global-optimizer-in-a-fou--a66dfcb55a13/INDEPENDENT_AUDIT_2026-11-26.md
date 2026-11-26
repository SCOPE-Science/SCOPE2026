# Independent mathematical audit

## correctness

PASS

Independently reduced the spin generator to the centered, bias-normalized fermionic one-particle matrix M. Its equation has commutator with hopping 2 and centered diagonal U(3,1,−1,−3), damping (G/2){B,M} at the endpoints B=diag(1,0,0,1), damping 2γ on the off-diagonal, and drive diag(G,0,0,−G). The current divided by f is 4 Im M_12. The dissipative part of the homogeneous equation forces zero boundary rows and columns by the real Hilbert–Schmidt pairing; the commutator and nonzero hopping force the remaining rows to vanish even at γ=0. Reflection with alternating site signs and conjugation reduce the system to ten real unknowns. Exact elimination reproduced both zero-dephasing rational formulas, the six polynomial coefficients and all thirteen derivative coefficients at G=1. See `python /workspace/branches/review-computations/check_transport.py`; frozen code was inspected, not executed. The positive W coefficients yield a simple unique threshold. Under W=xG² at small G or W=x/G² at large G, scaled polynomials tend respectively to 2293760x−49152 and x−192; bracket their roots to justify both laws. At G=1 the ordered root brackets imply either strict negativity on γ>0 or exactly one positive zero of the derivative with a positive-to-negative crossing. At scale γ=cU, the leading denominator is nonzero for c>0, so the leading quotient and its c derivative converge uniformly near c=1. Bracketing by c on either side of 1 gives the optimizer and current limits. All-G checks are only initial-response checks for the frozen result.

## originality

FAIL

A distinct indexed four-site Wannier–Stark result on the same Hamiltonian, jump rates and normalized current explicitly gives the identical onset polynomial and both reservoir-coupling limits, and proves the global shape for all G rather than merely G=1. Its exact resistance and all-G shape also directly imply both strong-tilt optimizer limits. The later-labelled catalogue path does not establish who obtained the result first or when; this is an evidence-based coverage decision, not a historical-priority finding. No substantive uncovered remainder of the frozen finding was established.

## value

FAIL

Exact onset and optimizer behavior are well motivated for the first size beyond the published two- and three-site formulas. However, the same finite-chain boundary, both onset laws, and a stronger global classification are already available in the matched result, and the strong-tilt limits are an immediate leading-degree consequence of its compact resistance and uniqueness. The frozen alternative calculation does not establish a separate, independently useful result beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
