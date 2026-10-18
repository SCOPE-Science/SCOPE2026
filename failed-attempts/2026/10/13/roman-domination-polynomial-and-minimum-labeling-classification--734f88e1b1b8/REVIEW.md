# Independent mathematical audit

## correctness

PASS

The proof is correct: fixing two-labeled edges F in K_n, every edge inside the unused vertex set W must carry 1 and every other non-F edge independently 0 or 1. Inclusion-exclusion on nonisolated support vertices gives A_s(m) and the exact weight polynomial. The minimum bound 2 ceil((n-w)/2)+binom(w,2)>=n-1 has equality only for perfect matchings with w=1 (odd n) or w=2 (even n). Independently enumerated all ternary labelings n=3,4,5, verified all coefficients, and checked the exact optimum counts through n=12; unrestricted correctness rests on the proof.

## originality

FAIL

An actual earlier Git-published same-repository record gives the exact identical polynomial and every minimum function for all n>=5, so this later claim is already covered on its infinite domain. Under w=n-c and m=k, every summand in the two displayed formulas coincides, with the earlier separate z^N term equal to A_0(0) in the later sum. Prior record import 2026-10-13T00:44:50Z, later duplicate 00:46:43Z; earlier commit is an ancestor of later by an actual compare. n=3,4 are only two elementary already covered small graph cases; the extra endpoints cannot rescue originality.

## value

FAIL

There is no surviving substantive contribution beyond the prior n>=5 all-coefficient enumerator and matching equality classification; adding T_3=K_3 and T_4=K_{2,2,2} is a small known-graph specialization, not a new motivated result. Validity and reproducibility do not make this duplicated theorem valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
