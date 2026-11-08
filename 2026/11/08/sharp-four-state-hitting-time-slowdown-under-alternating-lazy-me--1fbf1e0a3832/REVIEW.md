# Scientific review

## Correctness

**PASS.** The target-absorbed two-phase recurrence \(a=\mathbf1+Ab\), \(b=\mathbf1+Ba\) follows directly from the first-step rule and is uniquely solvable because connectedness and holding probabilities yield uniform finite-time absorption. The exhibited cycle/paw matrices and six phase-conditioned rational expectations satisfy the equations exactly; both static means for the reported start-target pair equal \(6\). The finite upper-bound claim is certified by a standalone exhaustive enumerator over all simple labeled graphs on two, three and four vertices. It retains exactly connected graphs, evaluates both phases and all target/start pairs, performs only rational calculations with checked equation residuals, and reports a sharp largest ratio \(646/607\). The witness is separately checked via the six-dimensional phase-augmented equations. This does not assert results beyond four vertices.

## Originality

**PASS under accessible-source comparison, with historical-priority risk.** Shimizu–Shiraga (arXiv:2102.08002, Sections 1.2, 4 and Eq. (3)) study precisely the same lazy Metropolis walk in dynamic graphs but give general mixing/hitting/cover-time bounds rather than the exact pointwise ratio to both fixed-graph hitting times. Sauerwald–Zanetti (arXiv:1903.01342, Introduction/results) establish dynamic hitting bounds but not this finite extremal classification. Nonaka et al. (2010) treat static Metropolis kernels. Targeted searches found no equivalent small-graph threshold or stated exact ratio; lack of a located result is not proof of absolute novelty. A close unindexed finite enumeration could exist.

## Value

**PASS.** Under a shared time-independent stationary distribution, general results guarantee useful polynomial bounds, but they do not decide whether periodic changes can be worse than *each* available static topology for a fixed route. The theorem supplies the smallest possible obstruction, a concrete graph-theoretic mechanism (alternating a regular cycle with a degree-heterogeneous paw), and the complete sharp finite-size extremum across every four-vertex graph pair. This is a natural finite network-design comparison rather than a parameter-substitution exercise; the modest \(6.43\%\) size and absence of an asymptotic extension are explicit limitations.

## Literature comparison and scope

The exact conclusion concerns \(60\)-family finite Markov-chain hitting times, not global mixing or cover times. The cited papers' asymptotic estimates allow such slowdowns; they do not yield the precise factor or minimal order. Only the new finite-domain theorem has been checked here. No independent audit is implied.

Self-review: passed. Independent audit: not yet performed.
