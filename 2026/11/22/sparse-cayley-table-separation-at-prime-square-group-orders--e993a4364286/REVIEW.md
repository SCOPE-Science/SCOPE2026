# Self-review

## Correctness — PASS

The abstract invariant identifies a group only up to isomorphism. For a prime-square order, the two targets are precisely the cyclic and rank-two elementary abelian groups. Every sparse multiplication pattern yields a relation matrix whose rows split into a unit vector and an incidence difference. Total unimodularity makes every determinant a sum of at most \(2^k\) unit-determinant terms. If \(p>2^k\), these minor bounds forbid hidden \(p\)-torsion and force every label difference to be either zero in both targets or primitive in both. The union bound is strictly below one because \(t\le3k\) and \(\binom{3k}{2}<4^k<p^2\). The addition-chain construction supplies the upper bound and the exact families. All boundaries, including \(p=2\), are addressed. The code checks small cases but is not a substitute for the theorem's proof.

## Originality — PASS, historically provisional

OEIS A387855, dated October 8, 2025, names the invariant and tabulates up to order 23. The full Chernev–Chernev preprint of November 19, 2026 was inspected and gives a general upper bound and small-order computations, not the all-prime indistinguishability lemma or exact Mersenne/Fermat families. Bean's Latin-square critical-set bound and Gowers–Long's approximate associativity result concern materially different notions; neither implies the new claim. Published-result searches and comparison with all 98 recoverable claims in the current accessible algebra ledger found no equivalent or stronger theorem. Earlier unindexed results remain a priority risk.

## Mathematical value — PASS

The new lower bound is uniform over all primes and all partial multiplication constraints, rather than an isolated addition-chain example. It identifies the precise three-entry threshold on the entire family of prime-square orders, gives the first unlisted exact cases \(25,49,121\), and ties infinitely parametrized exact families (conditional on prime existence) to addition chains and incidence-matrix structure. It quantifies the information content of sparsely sampled group tables, which is the invariant's motivating question.

## Scope and risks

The sandwich does not determine \(m(p^2)\) for every prime; no infinitude claim is made. The October 2025 sequence record is the earliest verified public source used for scope. The later November 2026 preprint is compared for priority only. Independent mathematical verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
