# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-012`

## Correctness — PASS

The extremal theorem is mathematically supported. The branch-excess identity forces either one outdegree-three vertex or two outdegree-two vertices. In the one-branch case, first-return lengths give the Perron equation \(\sum z^{\ell_i}=1\), and exponent transfer yields exactly the looped rose \((1,2,n-1)\) or loopless rose \((2,2,n-2)\). For two branch vertices, the three possible first-return matrix patterns admit strict inequalities at the candidate reciprocal Perron root, excluding equality. A later published proof of the same theorem was inspected in full and independently confirms these steps. The assigned finite verifier covers only \(n=3,4,5\) and is treated as corroboration, not as proof of the infinite statement.

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py
- published full proof: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-maximum-spectral-radius-strongly-connected-tricyclic-digraphs--e58d4b5b4bf1
- Klech, arXiv:2609.18367

### Correctness risks

- Correctness of the infinite theorem rests on the excursion/Perron inequalities, not the small-\(n\) enumeration.

## Originality — FAIL

Current published coverage is decisive. A later published finding dated 2026-09-18 states exactly the same global maximum theorem for strongly connected digraphs with \(m+2\) arcs, with the same reciprocal-root formulas and the same unique rose extremizers in both looped and loopless classes, and supplies a complete proof. Under the required current-coverage standard, the audited claim is therefore covered. Because the covering result postdates the audited record, this finding does not determine historical priority on 2026-09-17.

### equivalent_formulations

Searches:
- semantic search for maximum spectral radius in strongly connected \(m+2\)-arc digraphs
- search by candidate polynomials \(1-z-z^2-z^{m-1}\) and \(1-2z^2-z^{m-2}\)

Evidence:
- A 2026-09-18 published finding is an exact theorem-level match.

Reasoning:
The variable name \(m\) versus \(n\) is immaterial; the graph class, formulas, equality cases and loopless exception are the same.

### broader_coverage

Searches:
- Klech arXiv:2609.18367
- Shan–Wang–He arXiv:2105.03077
- later full global proof

Evidence:
- Klech provides the parent structural classification and poses the maximum problem; Shan–Wang–He treat specified rose/theta/tri-ring subclasses; the later published result covers the full class.

Reasoning:
The later result is strictly decisive full coverage, while the older sources are framework/subclass results.

### exact_database_or_table

Searches:
- spectral-radius tables or graph databases for the \(m+2\)-arc class

Evidence:
- No database table is needed for the coverage determination; the exact theorem is published with proof.

Reasoning:
This axis is inapplicable as a table-lookup novelty question once theorem-level coverage is established.

### claim_vs_prior_implication

Searches:
- claim-to-later-result statement comparison

Evidence:
- Both give \(\rho\le r_m^{-1}\) with \(r_m+r_m^2+r_m^{m-1}=1\) and unique \((1,2,m-1)\) rose; both give the loopless \((2,2,m-2)\) analogue.

Reasoning:
The audited statement is a direct duplicate of the later currently published theorem, so current originality fails.

### source_inspections
- **Maximum spectral radius in strongly connected digraphs with \(m+2\) arcs** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-maximum-spectral-radius-strongly-connected-tricyclic-digraphs--e58d4b5b4bf1. Trigger: Exact semantic match found in the current published corpus. Material read: Complete RESULT.md including the full proof. Method: Full statement-and-proof comparison. Assessment: DECISIVE CURRENT COVERAGE: same class, bounds, roots, equality cases and exceptional case. Evidence: The later theorem proves both maximum formulas and unique rose extremizers.
- **Generating Functions and the Minimum Spectral Radius in Strongly Connected Digraphs with \(m+2\) Edges** — https://arxiv.org/abs/2609.18367. Trigger: Parent preprint and source of Conjecture 5.15. Material read: Current abstract/scope and bibliographic record. Method: Primary-source scope comparison. Assessment: The source establishes the surrounding class structure/minimum problem; the maximum theorem is the conjectural target. Evidence: It studies exactly \(\mathcal{SC}_{m+2}(m)\).
- **Some alpha-spectral extremal results for some digraphs** — https://arxiv.org/abs/2105.03077. Trigger: Closest earlier subclass extremal literature. Material read: Abstract and class descriptions. Method: Primary-source scope comparison. Assessment: Covers rose, generalized-theta and tri-ring subclasses, not the full class. Evidence: Its scope is subclass extremality rather than the global \(m+2\)-arc maximum.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-maximum-spectral-radius-strongly-connected-tricyclic-digraphs--e58d4b5b4bf1
- https://arxiv.org/abs/2609.18367
- https://arxiv.org/abs/2105.03077
- assigned RESULT.md and artifacts/verify.py

### residual_risks

- The exact covering theorem was published after the audited record; current coverage does not settle historical first-discovery priority.

## Scientific value — PASS

The theorem is a natural sharp extremal classification resolving an explicit recent conjecture, with unique equality cases and a structural first-return proof. Its mathematical value remains substantial even though current originality fails.

### Value sources

- Klech, arXiv:2609.18367
- full global maximum proof in the current published corpus

### Value risks

- Scientific rejection is due to current coverage, not lack of intrinsic mathematical significance.

## Limitations

- The claim is rejected scientifically because originality fails under current published coverage.
- The later covering record postdates this record, so the audit does not assert that historical priority was lost at the original publication date.
- The package's finite enumeration is not an infinite proof.

## Disposition

**FAILED**
