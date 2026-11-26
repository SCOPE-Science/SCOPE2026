# Independent mathematical audit

## correctness

PASS

On differences of trace-one states the full replacement term is −r times the identity superoperator. The evolution contracts by at least e^(−rt) in trace norm on Hermitian differences; the CPTP reset-age integral is normalized, positive and stationary. This proves stationarity and uniqueness on the full state space. Evolution starting in the ground state preserves the claimed X sector and qubit exchange. Writing q=r+γ and d=r+2γ, the balances give y=γx/q, x=2g Im(w)/d, and q w=ig(1−2x−2y). Eliminating gives x+y=2g Im(w)/q and w=igq/(q²+4g²), yielding the stated populations and C=2[|w|−y]_+. The sign condition qd>2γg and its positive root for g>γ follow; equality is separable. To cross-check the optimum, set u=2g/q and t=γ/d. The unclipped concurrence is (u−tu²)/(1+u²), the Rayleigh quotient of [[0,1/2],[1/2,−t]] at (1,u). Its top eigenvalue is (√(1+t²)−t)/2, positive, attained only at the positive ratio u=√(1+t²)−t. This confirms g_*, the envelope, strict increase with r at fixed γ, and both stated endpoint limits. At fixed γ>0, approaching 1/2 forces t→0 and u→1, since the half-ceiling deficit on the positive branch is (u−1)²/[2(1+u²)]+tu²/(1+u²); hence r→∞ and g∼r/2. This is a fixed-emission statement as in the envelope and Limitations, not a claim about sequences varying γ, where the necessary and sufficient conditions are r/γ→∞ and 2g/(r+γ)→1. At fixed g, C∼2g/r instead. Read CHECK.py and VERIFICATION.md without executing the uploaded code.

## originality

PASS

Credit reset-assisted stationary entanglement, radiative damping, the standard concurrence formula and the no-emission joint-reset specialization as prior. The surviving scope is the exact positive-emission phase boundary and attainable coupling envelope for the specified pair Hamiltonian and joint ground reset.

## value

PASS

For a natural driven and damped two-qubit model the exact condition distinguishes reset rescue from large-reset suppression at fixed coupling, and the attainable optimum quantifies when compensating with larger drive yields a different limit. The strict equality boundary and a unique global coupling choice are more informative than a sample trajectory or a fixed-coupling improvement claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
