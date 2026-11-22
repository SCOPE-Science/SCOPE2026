# Review of two-sided finite-horizon edge activation in priced complete prisms

## Correctness — PASS

The claimed global optimizer is derived for the entire independent-edge simplex, not assumed two-class: strict trace-exponential convexity and injectivity of individual edge Laplacians yield uniqueness; graph automorphisms then force the two symmetric classes. Exact tensor-product spectra produce the trace and budget equation. The strict convex scalar log-objective and two one-sided derivatives give both activation horizons, including equality endpoints and the equal-price case. The long-time correction and two network-size scales follow by direct limits. `verify.py` completed 15,520 finite independent spectral, budget, symmetric-grid and asymmetric perturbation checks. Those tests are supplemental, not infinite proofs.

## Originality — PASS on inspected evidence

Closest directly comparable work is *Three allocation scales in priced complete prisms* (November 8, 2026), which studies precisely the same two-layer graph and price classes, but minimizes total effective resistance and proves all edges are active. The new pointwise exponential heat trace instead permits disconnected short-horizon optima and has two exact reactivation horizons with distinct network-size scales. Boyd (2006) supplies general convex spectral design, while Ghosh, Boyd and Saberi (2006) treat effective resistance with a one-bridge barbell. A prior matching-priced complete-network heat-trace claim concerns a different feasible graph with nonmatching cross-layer edges and does not imply this prism classification. Searches of published-finding corpus and primary literature found no directly covering theorem. This is a best-evidence originality judgment, not a proof of uniqueness in all literature; unindexed work is a residual risk.

## Value — PASS

A complete exact support diagram for a natural two-community graph addresses when apparently useful bridging links should be funded at finite observation times. The result gives a meaningful counterpoint to stationary resistance optimization: for nonunit price, the finite-horizon optimum initially disconnects the network although the stationary design funds all edges. The two price sides have sharply different reactivation scales, respectively linear and linear-logarithmic in the clique size. This is a structural intervention law, not just a relabeled optimizer or one small numerical instance.

## Boundaries and evidence

The exact rates are the unique solution of a scalar exponential equation only in the interior; no elementary radical closed form is claimed there. The proof does not extend to incomplete matchings, unequal layers or varied individual prices. The checker uses selected finite matrices, and independent validation is pending.

Self-review: passed. Independent audit: not yet performed.
