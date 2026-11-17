# Independent mathematical audit

## correctness

PASS

C: If k>=2, an occupied singleton with utility zero can move into the gap immediately preceding another occupied run and gain exactly one neighbor, so it is unstable. If a run has length >=3, an interior dissatisfied occupant can profit from a boundary vacancy whenever some vacant run has length >=2. Conversely all dimer occupants already have utility one; with isolated single vacancies, every dissatisfied interior occupied vertex sees two occupied neighbors before moving, and every vacancy continues to have two occupied neighbors after such a move. Counting cyclic gap compositions gives D=n/(k/2)*C(z-1,k/2-1), H=n/z*C(k-z-1,z-1), subtracting the three repeated 110 patterns exactly at k=2z. Independently enumerated literal occupant-to-vacancy jumps for all 2^n bit strings, 3<=n<=12, agreeing with formula at every k, including n=3 and full/empty boundaries. All-n classification follows from run arguments, not finite experiments.

## originality

PASS

O: PASS best-of-knowledge with explicit full-text access risk. Deligkas–Eiben–Schierreich–Voudouris (2026) introduces the anonymous-neighbor network model and a one-neighbor-utility obstruction on other topologies; the accessible abstract and bibliographic text do not establish this all-cycle exact run/census theorem, but its full text was inaccessible (arXiv HTML/OA and Oxford VPN). Friedrich et al. study colored Schelling preferences, Aziz et al. fully occupied swaps. No direct logically dominating inspected statement is known, and inability to inspect one plausible source alone does not force rejection.

## value

PASS

V: PASS. The all-size exact existence condition reveals a sharp and natural 2/3 density transition with odd-population exclusion below threshold, plus full integer equilibrium census. This closes a mathematically meaningful special-case gap in the anonymous-neighborhood jump game, without claiming arbitrary graph equilibria or dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
