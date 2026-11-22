# Scientific review of the narrowed Poisson crowd-out theorem

## Correctness

The complete-allocation identity \(W=\nu(H)\) is proved, not assumed. Duplicate requests cannot produce satisfied agents without envy, all satisfied requests are disjoint, and every disjoint collection of uniquely requested \(r\)-sets can be realized by parking the remaining goods as singletons because \(n\ge m\) and \(r\ge2\). Full envy inequalities are checked for selected and losing agents. The original reduction to ordinary matching at \(r=2\) and NP-complete fixed-\(r\ge3\) set packing is valid but not independently novel.

The exact event \(W=0\iff S=0\) follows from the identity. Occupancy inclusion-exclusion and factorial moments give the correct singleton count. The pairwise-intersection expectation is computed over all possible pairs of distinct \(r\)-sets; it bounds both total variation and the expectation gap. In the critical window it is \(O_r(1/m)\), and so the optimal welfare itself has the stated Poisson law and mean. The first and second moments give the two one-sided bounds. A separately implemented complete-allocation enumeration checked 1,661 small profiles, together with exact occupancy counts for four \((M,n)\) instances. These are corroborations, not infinite proofs.

## Originality and explicit historical exclusions

Fiat–Wingarten (2009), Section 4.1 Observation 5, already gives the decisive winner/loser condition for single-minded allocations with prices; at zero prices and constant request size its condition yields the unique-request restriction. With the elementary singleton-parking completion argument it implies the deterministic packing identity. Edmonds/Karp supply the algorithmic boundary. No originality is credited to either.

The classical two-copy coupon-collector results of Newman–Shepp and Erdős–Rényi already give the same \(\log M+\log\log M\) occupancy window and Gumbel zero-singleton limit. No originality is credited to the occupancy limit in isolation.

The narrowed contribution is the exact stochastic comparison between the *maximum welfare of a complete envy-free allocation* and the singleton count when request types are overlapping \(r\)-uniform hyperedges, with the quantitative expected-intersection bound and resulting full welfare distribution. It was not established by the retrieved general pricing or coupon-collector theorems alone; a still-unindexed random-hypergraph/welfare theorem could cover it. This is a qualified best-of-knowledge claim, not a universal novelty guarantee.

The most directly related 2026 manuscript, Inamdar–Jain–Pandey (arXiv:2609.28308), was accessible at the abstract/introduction/summary level but not as a complete primary manuscript; an authorized download route was unavailable. Its positive-demand main domain differs, but no claim of whole-document noncoverage is made. Existing published fair-division and Resultary comparisons did not reveal the exact optimal-welfare law. The residual risk must be retained.

## Value and scope

The quantity is a natural optimization invariant of complete fair division: the optimal welfare under repeated complementary requests, not a fixed allocator's performance. Its full critical distribution and explicit finite error to a classical occupancy observable answer a distinct allocation question in a natural many-agent regime. The contribution is modest, and its ingredients are standard; no new general occupancy theorem, complexity result or coupon-collector theorem is advertised.

## Verification, privacy and provenance limits

The scientific statement and references are neutral and contain no operational metadata. Existing finite verifier and Lean/expert-status file remain unmodified. Scientific assessment is independent from formal verification or expert attestation. All mathematical assertions and conditional limits are restricted to the assumptions recorded in RESULT.md.
