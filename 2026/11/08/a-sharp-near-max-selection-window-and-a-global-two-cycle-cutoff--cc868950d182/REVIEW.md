# Self-review

## Correctness — PASS

The stated parameter range is universal over nonzero binary matrices on every periodic \(H\)-by-\(W\) grid with \(H,W\ge4\). Its necessity for *exact maximum-selector equality* has an explicit one-hole witness. The reduction to two independent symmetric one-dimensional argmax selectors is an equality of operators after one update, not an approximation. The potential \(m(A)/|A|\) is nondecreasing by reciprocity of the symmetric three-neighbor matrix; equality forces containment two times ahead. This proves eventual period at most two and, because the potential has at most \(3n\) possible values, yields the conservative quadratic settling bound. Singleton/triple and long-run witnesses establish actual cycles and growing transients. The exact finite checker printed `VERIFY_OK checks=238104`. No conclusion about periods at the selection-width endpoint is made.

## Originality — PASS within checked evidence

The motivating 2026 numerical study supplies the model and documents other dynamical outcomes. An already public Rule-54/Rule-18 stripe filtration uses disjoint interval geometry and does not cover all starting matrices or the sharp near-max window. The classical 1980–81 Goles–Olivos two-period results assume fixed thresholds at each vertex, whereas the present all-maxima selection uses a globally state-dependent moving threshold and a separable rank-one field. The proof's reciprocity mechanism resembles potential-game arguments and is acknowledged, not claimed as a new general technique. Searches of relevant published records and literature did not find the exact operator-selection boundary combined with this full-grid classification. The motivating paper's full body and the original classical proofs remained unavailable: priority is provisional, and no inaccessible work was declared not covering on snippets alone.

## Mathematical value — PASS

A positive, sharp finite-size parameter interval is classified **for every initial state** in a model previously explored mainly by numerical phase scans. The theorem makes the compressed two-dimensional system analytically reducible in one iteration, forbids all higher periodic cycles in that region, proves an explicit quadratic-time upper bound, exhibits genuine two-cycles, and shows transients need not be uniformly bounded. The sharpness is specifically of the maximum-selector phase, not of the period-two conclusion beyond the endpoint. This is a structural dynamical boundary, not an arbitrary parameter lookup or routine numerical census.

## Closest literature and scientific limitations

X. Shi and M. Huang, *Dynamics in a Low-Rank Separable Field Cellular Automaton* (arXiv:2606.08983, 2026), provides the exact update and numerical motivation. A published analysis entitled *An irreversible Rule-54/Rule-18 phase filtration in a normalized separable-field automaton* proves a distinct stripe-subsystem statement for threshold regions away from one. E. Goles and J. Olivos (1980, 1981) give foundational period-two theorems under fixed symmetric thresholds. The full primary text of the 2026 source was not accessible through the routes attempted, and specialized global-maximum automata literature may contain related classifications. No independent review of this result has occurred.

Self-review: passed. Independent audit: not yet performed.
