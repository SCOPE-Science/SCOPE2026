# Review of Tribonacci-optimal abductive explanations

## Correctness — PASS

The statement fixes strong-next finite-trace semantics and treats length \(n\ge2\). Expanding the single temporal formula gives precisely \(n-1\) clauses \((\neg r_i\vee d_i\vee d_{i+1})\). Because all occurrences of each time-indexed atom have consistent polarity, locking the values of one true literal per clause is necessary and sufficient for satisfaction under **all** compatible completions. Inclusion-minimal such locks are therefore minimal transversals. Conversely, unlocking all true literals of any clause is necessary and sufficient to make **some** completion violate the formula. Distinct private request literals prove that removing any available true clause literal strictly reduces the family of AXps, giving the unique two full maximizing traces. The binary-word private-witness characterization proves the exact transfer polynomial; its specialization proves the recurrence and growth. Private-witness arguments also establish the cardinality bounds and contrastive extremality; disjoint adjacent-clause replacements of the private vertices realize every intermediate AXp size.

The separate standard-library `verify.py` compares actual finite-trace locking/unlocking semantics with independently generated transversals on every compliant trace through length four. It exhaustively locates all AXp maximizers through length eight and checks the size generating polynomial through length nineteen. These finite runs are corroboration, not proofs of the all-length result.

## Originality — PASS within inspected literature

Fionda, Ielo and Ricca (2026), arXiv:2610.35169v1, introduce and characterize finite-trace AXps/CXps and prove general duality. Their construction in the experiments has \(N\) AXps versus \(2^N\) CXps, with formula and alphabet growing with \(N\). They do not give the opposite fixed-formula exponential AXp/linear CXp separation, exact sharp optimization over all compliant traces, or the individual cardinality polynomial. Ferrère, Maler and Ničković (2015) study related temporal implicants with different trace semantics and no corresponding finite-length extrema. OEIS A000213 already documents the Tribonacci recurrence and matching numerical sequence; those are explicitly **not** presented as new. The potential contribution is the exact explanation-spectrum realization and sharp uniqueness statement for a natural temporal requirement. Priority remains conditional on undiscovered prior equivalent work in combinatorics or temporal diagnostics.

## Value — PASS

The question is a natural explainability-capacity gap: can a fixed, two-atom temporal specification force exponentially many minimal sufficient explanations on a *single* compliant trace, even when there are few minimal possible outcome-changing interventions? The theorem answers with a sharp all-length count, exactly identifies maximizing traces, quantifies explanation sizes, and constructs a small transfer calculation. It gives a precise worst-case family for full AXp enumeration that general hitting-set duality alone does not numerically evaluate. This is not a claim of a newly discovered integer sequence, nor a general complexity theorem for all temporal formulas.

## Closest literature and remaining limits

The principal comparator is arXiv:2610.35169v1, especially its explanation definitions, hitting-set duality, and synthetic evaluation example. The second comparator is the temporal-implicant construction of Ferrère, Maler and Ničković (2015). OEIS A000213 is an exact numeric-table match but supplies no temporal-explanation interpretation or unique maximizing valuations. A combinatorial theorem phrased using domination, private witnesses, or hypergraph transversals might yield an equivalent after translation; this risk remains. The theorem is restricted to compliant fixed-length traces of the guarded bounded-response formula and does not address correlated event features or arbitrary monitoring languages.

Self-review: passed. Independent audit: not yet performed.
