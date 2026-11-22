# Review: single-node integer reachability on small trees

**Correctness (PASS).** All isomorphism types and their coordinate roots through nine vertices are covered by the inductive leaf-attachment generator and canonical rooted-string isomorphism test. The public checker independently computes all determinants by Bareiss integer elimination and rational Gaussian elimination, reproducing the complete table. The exceptional parity condition follows from an explicit modular annihilator and a determinant of absolute value two; integer Cayley–Hamilton ensures longer horizons add no extra lattice states.

**Originality (PASS on inspected evidence; qualified).** The earlier tree-topology literature classifies real controllability using spectral interlacing and component eigenvalues. Earlier path/cycle reachability work and special path/spider unimodularity statements do not give the sharp nine-vertex minimality theorem for arbitrary unweighted tree shapes or the index-two integer-lattice characterization. Actual searches for the tree walk-matrix determinant and integral controllability found no dominating order-nine theorem, but such negative searches do not certify publication priority.

**Value (PASS).** The smallest failure of integer unimodularity in a real-controllable graph is a natural exact boundary: it separates the ability to steer arbitrary real states from the ability to steer arbitrary integer states on otherwise identical unit networks. The fully classified nine-vertex case supplies a concrete parity obstruction and a reproducible finite benchmark; no broader significance beyond these proved facts is assumed.

**Closest literature.** Ji, Lin, Lee and Ling (American Control Conference, 2010), *Multi-agent Controllability with Tree Topology*; Parlangeli and Notarstefano (arXiv:1109.3556, 2011), *On the reachability and observability of path and cycle graphs*. The first gives a real-controllability criterion for trees; the latter gives path/cycle arithmetic criteria. Neither examined statement gives the integer index classification. The 2010 PDF was materially inspected in extracted full text, while its screenshot service was unavailable after a redirect.

**Limitations and risks.** The minimality claim is finite through nine vertices. All edges have unit weight, only one coordinate is actuated, and controls are signed integers. Complete priority search and independent mathematical review are not claimed; unindexed equivalent walk-matrix results remain possible.

Self-review: passed. Independent audit: not yet performed.
