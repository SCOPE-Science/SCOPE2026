# Independent mathematical audit

## correctness

PASS

Modulo constants, the adjacent increments give ℓ¹ coordinates; the norm into the integral of the absolute derivative is exactly the maximum of the three single-jump column norms. The reflected terminal steps have derivative proportional to 3x²−2x−a² with two internal roots; the central derivative is proportional to 1+a+a²−3x² with two internal roots. Splitting at the roots gives A and B as stated. A increases, while the log derivative of B+1 has the sign of (a−1)(a+2); the endpoint limits force a unique crossing and minimizer. Independent exact-rational replay: python3 /workspace/independent_checks.py (section 4) proves opposite signs at the stated rational endpoints and bounds the gain using monotonicity of A; it also checks the comparison values. This is about fixed endpoints, symmetric grids and unrestricted real data, not range escape.

## originality

FAIL

Shown already covered. A distinct indexed theorem on all endpoint-fixed grids gives identical single-jump gains at m=0 and proves that its unrestricted unique global minimizer is exactly the symmetric crossing. The extra decimal precision in the frozen bracket only refines evaluation of an already specified unique root; it is not a surviving scientific claim.

## value

FAIL

The variation norm is a meaningful design criterion, but this submission resolves only a restriction already answered by the broader exact theorem. Tightening a decimal bracket for the same already isolated and explicitly characterized crossing does not supply an independently useful new invariant or mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
