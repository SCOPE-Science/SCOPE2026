# Scientific review

## Correctness (PASS)

Each increasing \(r\)-tuple induces one shortcut witness with probability \((c/n)^r\), giving the exact expected witness spectrum. Among \(r!\) rank orders on an undirected cycle, exactly \(2r\) make it a redundant forward arc plus an increasing alternative path. The standard factorial-moment argument for short cycles gives the independent marked Poisson limits. Distinct witness cycles of bounded lengths overlap with probability \(O(n^{-1})\); the sum of longer-witness expectations is controlled by \(\sum_{r>L}c^r/r!\). These bounds prove uniqueness/disjointness and transfer the limit to actual redundant arcs. The verifier checks finite instances only; the analytic proof supplies the infinite conclusion.

## Originality (PASS, subject to historical priority)

The closest material includes Albert and Frieze's fixed-probability random graph orders (1989), Rödl and Thoma's dependent-arc and cover-graph work (2005), Karrer and Newman's Poisson-multigraph ordered-DAG models (2009), and Clough et al.'s empirical transitive-reduction comparisons (2013). The accessible statements do not yield the full simple-Bernoulli \(c/n\) deletion law and alternative-path marked distribution. General sparse-cycle Poisson facts are classical and credited as inputs. The entire related Rödl–Thoma text was inaccessible; historical priority remains an uncertainty, not a certification.

## Value (PASS)

The number of relations that may be deleted without changing reachability is a canonical, naturally motivated complexity measure of a sparse causal DAG. The result identifies its full distribution and independent witness-length classes, with the unusual structural fact that witnesses almost never overlap. This is a usable null-model benchmark for transitive-reduction savings and the causes of redundancy.

## Scope and limitations

Only fixed \(c>0\), independent simple Bernoulli arcs and the \(n\to\infty\) regime are covered. No growing-density extension or finite-size total-variation rate is asserted. A higher-order or differently parameterized published theorem could still dominate the conclusion. See the structured scientific comparison in `AUDIT.json` for searches, sources and residual risks.

Self-review: passed. Independent audit: not yet performed.
