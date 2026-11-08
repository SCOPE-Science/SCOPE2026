# Scientific review

## Correctness — PASS

**Domain and normalization:** \(n\ge4\) cyclic voters and candidates, voter \(i\) approves \(\{i-1,i\}\), committee size \(k\in[1,n]\); improvement means *strictly more approved candidates* from an affordable deviating set. The Hare quota inequality is \(k|S|\ge n|T|\), including equality. The proof reconstructs EJR and JR definitions, establishes their equivalence because every pair of distinct voters shares at most one approval, proves all size-\(k\) committees Pareto efficient by constant total utility \(2k\), derives the sharp \(4/3\) runwise improver bound and the at-most-three-missing-candidates exclusion. The constructed unselected set has no cyclic triple zero and a four-voter/three-candidate profitable deviation for every parameter in the stated interval. Necessity and sufficiency include boundary equality, \(k=n\), and low-seat elections. Integer exhaustive checks and constructive tests corroborate the theorem; they are not substituted for the infinite proof.

**Risk:** The theorem presupposes the ordinary *integral* Hare core, not fractional core+, and fixed-size Pareto comparisons; adopting other conventions changes the question.

## Originality — PASS (best knowledge)

Primary comparison: Becker, Greger and Peters, arXiv:2609.11912, prove existence of at least one core+ committee in all approval elections, not whether a given EJR committee may be blocked on a cyclic two-approval instance. Pierczyński and Skowron, arXiv:2108.01987, prove core existence on restricted domains rather than a sharp structural separation. Aziz et al., arXiv:1407.8269, define JR/EJR and establish the hierarchy, without this precise threshold. Direct claim and alias searches in mathematical research records yielded no implication-equivalent result. The precise quantity being classified is existence of an EJR *noncore* committee, not core nonemptiness, generic EJR-versus-core incomparability or any probability. The closest indexed search results concerned unrelated voting rankings and did not cover the threshold.

**Risk:** This is a best-knowledge priority assessment. Unindexed manuscripts, a stronger as-yet-unfound cyclic-classification theorem, or alternative definitions of cyclic approval fairness could require a future reassessment. No independent novelty certification is claimed.

## Mathematical value — PASS

Core is a stronger cooperative stability requirement than JR/EJR; recent resolution of general core existence heightens interest in exact relations between ordinary proportionality axioms and core behavior. The theorem supplies a sharp parameter phase transition, the smallest electorate in the specific canonical two-regular cyclic profile, and a simple explicit infinite family of EJR-and-Pareto efficient but core-blocked outcomes. The structural \(4/3\) gain bound and four-voter/three-candidate obstruction explain the transition; the phenomenon is not a table recomputation or merely a tiny numerical improvement. It isolates a useful boundary for testing committee rules against coalition deviations without contradicting the existence of a stable alternative.

**Risk:** Scope is deliberately one regular cyclic approval profile, not arbitrary approval elections or a minimum over all possible profiles.

Self-review: passed. Independent audit: not yet performed.
