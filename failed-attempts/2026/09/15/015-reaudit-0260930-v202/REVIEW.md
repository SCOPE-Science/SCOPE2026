# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. The direct-integral argument is mathematically sound at the stated standard-measurability level. On each central fiber, full-support intertwining localizes to Popa intertwining of the two Cartans; the standard factor theorem upgrades that to unitary conjugacy. For finite fibers the statement is elementary. A measurable choice of conjugating unitaries then glues to a unitary in the original finite von Neumann algebra. The two-sided hypothesis is indeed stronger than necessary because one-sided Cartan intertwining is enough in each II_1 factor.

Originality: FAIL. Popa's intertwining theorem already says that for Cartan subalgebras of a II_1 factor, A intertwines into B if and only if the Cartans are unitarily conjugate. The audited proof then performs only the standard central decomposition/localization and measurable selection needed to apply that theorem fiberwise. The condition on every nonzero central cutdown is precisely what forces the factorwise hypothesis. Under the required implication/reduction test, the non-ergodic statement is a routine direct-integral corollary of the established Cartan intertwining theorem plus standard disintegration, not an original theorem.

Scientific value: PASS. A clean nonfactor formulation is useful and naturally motivated by ergodic decomposition, but value cannot rescue the decisive originality failure.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
