# Scientific review

## Correctness — PASS

The central quantifiers cover every nonempty finite open path, every deterministic three-color initial word for the height bounds, and independent uniform initialization for the asymptotic law. The synchronous update, height increment rule, and initial 1-Lipschitz lift are specified explicitly. The proof checks residue matching and the spatial Lipschitz invariant, proves the invariant ceiling and unit-speed propagation from a maximum, and gives a converse speed-of-influence bound from the level \(K-2\). This traps the extinction clock between two functionals of the near-maximum set. The uniform word-to-independent-increments bijection, Donsker invariance principle, almost-sure uniqueness of Brownian maximizers and Lévy arcsine law complete the infinite-size argument. The expectation limit follows from a uniform bound. The provided `verify.py` is an actual executable cross-check, not the infinite proof: it exhausts every initial word through length ten, and independently compares integer-state trajectories through length nine. No external certification is represented.

## Originality — PASS, qualified

Published background establishes the infinite-lattice fixed-site activity rate (Durrett–Steif 1991); one-dimensional local relaxation regimes (Fisch–Gravner 1995); and the exact finite-graph synchronization criterion and diameter bound (Gravner–Lyu–Sivakoff, first preprint 2016-10-24). The last is the strongest general conceptual overlap and its monotone ranking method is explicitly credited. Its statements and inspected proofs do not state a limiting distribution for total extinction of growing open paths. The nearest later published research record on paths counts only the extremal class with time \(n+1\), as far as its accessible summary establishes. Search comparisons for aliases such as global all-rest time, Brownian-argmax location, and first extinction time found no covering conclusion. Full text of that nearest record could not be retrieved; that uncertainty and the possibility of unindexed equivalents are residual risks, not a claim of absolute uniqueness.

## Value — PASS

The precise clock distribution is a motivated global invariant of a canonical one-dimensional excitable medium. It distinguishes the typical macroscopic relaxation time from the local inverse-square-root activity law and from the rare maximal-delay endpoint count. The limit is a nontrivial transformed arcsine law with a universal full CDF and sharp asymptotic mean, established for all growing path lengths by structural deterministic inequalities. An exact global timing law is useful for understanding how a wave network's last activity depends on its boundaries and the location of its initial dominant height; this is not an arbitrary small finite-table increment.

## Closest literature and limits

Sources: Durrett–Steif (1991), pp. 669–690; Fisch–Gravner (1995), pp. 329–348; Gravner–Lyu–Sivakoff (arXiv:1610.07320v1, Sections 2–4); and *A square-root law for maximal extinction times in three-state excitation on finite paths* (published summary, 2026-11-08; full text unavailable). The deterministic height representation and Brownian limit were not externally audited. The cited results on local activity, diameter-only global bounds, and maximal endpoint population are not presented as new.

Self-review: passed. Independent audit: not yet performed.
