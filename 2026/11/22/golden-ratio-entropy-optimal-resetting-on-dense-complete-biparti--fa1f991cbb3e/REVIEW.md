# Scientific review — golden-ratio entropy-optimal resetting on dense bicliques

## Correctness — PASS
The complete observed-vertex transition probabilities, stationary class masses and KL collision correction are reconstructed in RESULT.md. Their exact identity yields the strict finite root-side ordering. A global positivity-and-cutoff argument traps every optimal reset probability on the relevant scale; compact-uniform limiting entropy and a strictly concave function prove the unique asymptotic optimum. On balanced graphs it is the inverse golden ratio. `verify.py` independently solves finite stationarity systems with rational arithmetic and evaluates row entropies, replaying 2622 assertions. The infinite assertions rely on the proof rather than sampled graph sizes.

## Originality — PASS, qualified
The 2022 work of Wang and Chen supplies the relevant general entropy-rate framework, and Riascos and collaborators supply broader stationary network-reset theory. Full published result texts concerning stars, regular large-girth networks and complete graphs were compared. The star comparison already covers the center-versus-leaf boundary \(K_{1,m}\), which is not separately claimed as new. The new result is the full arbitrary-part KL ordering together with the **jointly dense** \(K_{a_n,b_n}\) all-maximizer limit and explicit golden-ratio specialization. The regular and clique results do not dominate this different domain and scaling. A broader unindexed equivalent theorem remains a priority risk; publication priority is not independently certified.

## Mathematical value — PASS
Two-part networks are a natural structural family for nonequilibrium transport, and observed trajectory entropy is a motivated stochastic observable. A sharp destination-side rule and a universal leading optimal intensity are precise, reusable facts beyond the known star case. The golden-ratio constant emerges from the strict limiting concavity and the optimality equation; it is not a fitted constant or an arbitrary parameter choice.

## Limitations
The claim is about stationary observed vertex entropy for uniform discrete-time jumps and a fixed-root independent reset event. It does not establish finite-size optimizer uniqueness, tagged-event entropy, first-passage optimization or weighted-network results. The finite checker corroborates formulas but does not prove the global theorems. Neither independent manuscript review nor a comprehensive priority audit has occurred.

Self-review: passed. Independent audit: not yet performed.
