# Independent mathematical audit — 2026-10-01

Audited at: 2026-10-01T04:47:00Z

## Final claim

Unitary conjugacy from full-support intertwining for Cartans in a fixed non-ergodic amenable crossed product

## Correctness — PASS

PASS. The direct-integral argument is mathematically sound at the stated standard-measurability level. On each central fiber, full-support intertwining localizes to Popa intertwining of the two Cartans; the standard factor theorem upgrades that to unitary conjugacy. For finite fibers the statement is elementary. A measurable choice of conjugating unitaries then glues to a unitary in the original finite von Neumann algebra. The two-sided hypothesis is indeed stronger than necessary because one-sided Cartan intertwining is enough in each II_1 factor.

## Originality — FAIL

FAIL. Popa's intertwining theorem already says that for Cartan subalgebras of a II_1 factor, A intertwines into B if and only if the Cartans are unitarily conjugate. The audited proof then performs only the standard central decomposition/localization and measurable selection needed to apply that theorem fiberwise. The condition on every nonzero central cutdown is precisely what forces the factorwise hypothesis. Under the required implication/reduction test, the non-ergodic statement is a routine direct-integral corollary of the established Cartan intertwining theorem plus standard disintegration, not an original theorem.

### Equivalent formulations
FAIL. Popa's intertwining theorem already says that for Cartan subalgebras of a II_1 factor, A intertwines into B if and only if the Cartans are unitarily conjugate. The audited proof then performs only the standard central decomposition/localization and measurable selection needed to apply that theorem fiberwise. The condition on every nonzero central cutdown is precisely what forces the factorwise hypothesis. Under the required implication/reduction test, the non-ergodic statement is a routine direct-integral corollary of the established Cartan intertwining theorem plus standard disintegration, not an original theorem.

### Broader coverage
FAIL. Popa's intertwining theorem already says that for Cartan subalgebras of a II_1 factor, A intertwines into B if and only if the Cartans are unitarily conjugate. The audited proof then performs only the standard central decomposition/localization and measurable selection needed to apply that theorem fiberwise. The condition on every nonzero central cutdown is precisely what forces the factorwise hypothesis. Under the required implication/reduction test, the non-ergodic statement is a routine direct-integral corollary of the established Cartan intertwining theorem plus standard disintegration, not an original theorem.

### Exact database or table
No exact database/table coverage was identified; this is supporting best-knowledge evidence only, not proof by failed search.

### Claim versus prior implication
FAIL. Popa's intertwining theorem already says that for Cartan subalgebras of a II_1 factor, A intertwines into B if and only if the Cartans are unitarily conjugate. The audited proof then performs only the standard central decomposition/localization and measurable selection needed to apply that theorem fiberwise. The condition on every nonzero central cutdown is precisely what forces the factorwise hypothesis. Under the required implication/reduction test, the non-ergodic statement is a routine direct-integral corollary of the established Cartan intertwining theorem plus standard disintegration, not an original theorem.

## Scientific value — PASS

PASS. A clean nonfactor formulation is useful and naturally motivated by ergodic decomposition, but value cannot rescue the decisive originality failure.

## Sources inspected

- **Sorin Popa and Dimitri Shlyakhtenko, Cartan subalgebras and bimodule decompositions of II_1 factors** (https://doi.org/10.7146/math.scand.a-14395): STRONG_PRIOR_COVERAGE. The paper establishes that Cartan conjugacy is characterized by the relevant bimodule embedding/discreteness condition in II_1 factors.
- **Intertwining-by-bimodules technique, Chapter 17** (https://www.math.ucla.edu/~popa/Books/IIun.pdf): DECISIVE_GENERAL_THEOREM. The source explicitly identifies Cartan subalgebras as the setting where Popa intertwining yields unitary conjugacy.

## Residual risks

- The audit does not claim the nonfactor formulation appears verbatim in the older sources; the rejection is by mechanical implication through standard central decomposition.
- Amenability of the original action is unnecessary for the implication once the fiber factors and Cartan hypotheses are in place.

## Disposition

**failed**
