# Independent mathematical audit

## correctness

PASS

For every fixed J,a,b,r>0 the trace-preserving completely positive no-reset evolution yields the displayed positive, unit-trace reset resolvent, and differences contract at least as e^{-rt}. An independent exact substitution into the full four-by-four master equation verified the stationary matrix, all nine printed coefficients of P, and 55 strictly positive monomials in Q; thus the second concurrence branch is strictly negative. For the first branch positivity is equivalent to P>0 by rationalization of nonnegative operands. P0–P2 are negative and P5–P8 positive. B3 decreases in J² and is positive at J²=a²/20; if P3≥0, then J²>a²/20 and the verified expression B4−B3 is strictly negative, so P4>0. Descartes' rule (discarding zero coefficients) with the endpoint signs gives one simple positive root and the exact inclusive separable interval. The independent radicand limit r⁴(s_o²−w²)=24a²J² in the limit, together with q+k=2J/r+O(r⁻²), gives the claimed expansion. Replay: python3 /workspace/branches/independent_exact_checks.py qubits. Frozen checker inspected, not run; its 880 numerical assertions are reported by the source, not independently replayed. The high-rate law is pointwise in the fixed noise/coupling rates.

## originality

PASS

The strongest inspected matches already contain joint-reset stationary concurrence, one-onset diagrams and high-reset entanglement under other hypotheses. They do not cover the specific mixed local axes, for which the verified result is a strictly positive unique threshold for every finite positive pair of local rates. This is a bounded statement-level conclusion, not a general novelty claim for entanglement by resetting or for the resolvent.

## value

PASS

An exhaustive classification of the entanglement sign for a naturally specified pair of local Pauli errors distinguishes an axis-induced change in the achievable phase diagram: no finite fixed pair of noise rates forbids entanglement, and no further disentanglement window is possible beyond the onset. The latter does not follow just from the high-reset expansion; the threshold can be calculated from the explicit polynomial. This does not mean concurrence is monotone above onset or remains appreciable as r grows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
