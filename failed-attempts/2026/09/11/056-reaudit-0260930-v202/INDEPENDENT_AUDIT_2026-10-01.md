# Independent mathematical audit — 2026-10-01

## Certified random two-generation probability interval for HN: P2(HN) in [0.999998364, 1.000000000]

**Disposition:** failed.

The interval arithmetic is correct, but the result is a direct calculation from the published ATLAS maximal-subgroup table and a standard union bound, so it fails originality and value.

## Correctness

**PASS** — The 14 maximal-subgroup indices in the audited package match the current ATLAS HN table. For each maximal class of index m, the number of conjugates is at most m and one conjugate contains a random ordered pair with probability 1/m^2, giving the stated union bound. An independent exact rational recomputation gives S=6979253/4266108000000, lower endpoint 4266101020747/4266108000000 and the A12-based upper endpoint 1299599999999/1299600000000.

## Originality

**FAIL** — The interval is mechanically implied by the published ATLAS maximal-subgroup table together with the standard maximal-subgroup union bound; exact decimal/rational evaluation is not a new mathematical statement when the underlying table and inequality are prior data.

## Scientific value

**FAIL** — This is a known-table recomputation with an elementary union bound. It supplies neither a sharp probability nor a new group-theoretic mechanism, so the exact rational endpoints do not constitute a separately motivated mathematical gap under the audit standard.

## Sources checked

- ATLAS of Finite Groups, Harada-Norton group HN maximal subgroup table.
- Burness, Liebeck and Shalev, Generation and random generation: from simple groups to maximal subgroups, Adv. Math. 248 (2013).
- Resultary semantic search for HN random two-generation probabilities.
- Audited package RESULT.md and artifacts/compute_interval.py.

## Residual risks

- The bound is deliberately crude and not a sharp determination of P2(HN).
