# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-7ad39a71543a`

## Final claim

Finite-index Grothendieck quotients give the stated complete ideal cotorsion pair, exact object-level defect classes, all finite-abelian defect groups, and direct-sum stabilization index equal to the order of the defect.

## Correctness — PASS

The semisimple splitting proof is correct. Euler class additivity makes the finite-index subcategory extension closed; quotient-exponent direct sums place the needed truncations inside it. The explicit Ext decomposition gives the ideal orthogonality, cone conflations give complete ideal approximations, and the long exact cohomology sequence gives the iff object-level obstruction classes. For direct sums, the defect is additive, so the least positive \(r\) for which a special approximation exists is exactly the order of the defect class.

### Correctness sources

- assigned RESULT.md
- Ren–Wang primary parity paper
- earlier finite-Grothendieck-quotient theorem

### Correctness risks

- The theorem is confined to bounded complexes over a semisimple finite-length category.

## Originality — FAIL

Current published coverage is decisive. A 2026-09-19 published theorem already has the same finite-index subgroup \(H\le K_0(\mathcal S)\), the same exact category, the same complete ideal cotorsion pair, the same quotient-valued truncation defects, the same iff object-approximation criteria, the full \(G\times G\) defect spectrum, and realization of every finite abelian group. The only conspicuous extra sentence here—the least direct-sum stabilization number—is an immediate corollary: the prior theorem gives existence iff the defect vanishes, and additivity gives defect \(r\delta\) on \(A^{\oplus r}\), so the least \(r\) is the group-element order.

### equivalent_formulations

Searches:
- Resultary semantic query for finite-abelian Grothendieck cotorsion obstructions
- full comparison with 2026-09-19 `Finite Grothendieck quotients control object-cotorsion completeness`

Evidence:
- The earlier theorem states exact defects \(\delta_-,\delta_+\), iff special approximation, all \(G\times G\), and all finite abelian \(G\).

Reasoning:
The formulations are the same after replacing \(\Lambda\) by \(H\); stabilization is obtained by applying the prior iff criterion to direct sums.

### broader_coverage

Searches:
- 2026-09-19 finite-Grothendieck-quotient theorem
- 2026-09-17 finite-\(K_0\)-quotient theorem
- Ren–Wang parity source

Evidence:
- The 09-19 theorem strictly contains the structural content of the audited record; the 09-17 theorem already gives the general finite-quotient incompleteness mechanism.

Reasoning:
Broader current coverage leaves no independent theorem-level content beyond a one-line order corollary.

### exact_database_or_table

Searches:
- current Resultary cotorsion/K0 records

Evidence:
- The decisive source is a theorem, not a table; database lookup is inapplicable once theorem-level coverage is found.

Reasoning:
No numerical table is needed to settle implication.

### claim_vs_prior_implication

Searches:
- direct implication check for stabilization

Evidence:
- Prior iff criterion: special approximation of \(B\) exists iff \(\delta(B)=0\); additivity: \(\delta(A^{\oplus r})=r\delta(A)\).

Reasoning:
Thus the minimum \(r>0\) is exactly \(\operatorname{ord}(\delta(A))\), mechanically.

### source_inspections

- **Finite Grothendieck quotients control object-cotorsion completeness** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-grothendieck-defect-ideal-cotorsion-pairs--98ec2c64f97b. Trigger: Near-exact earlier theorem. Material read: Complete published RESULT.md. Method: Full statement and proof implication comparison. Assessment: DECISIVE COVERAGE. Evidence: Same category, ideals, exact defect criteria, full defect spectrum, and finite-abelian realization.
- **A parity obstruction to completeness of object cotorsion pairs** — https://arxiv.org/abs/2609.18681. Trigger: Primary source of the motivating parity example. Material read: Primary paper introduction, theorem statement, and construction inspected from the full PDF. Method: Primary-source scope comparison. Assessment: Background only; it treats the parity instance. Evidence: The paper constructs the even-total-cohomology counterexample and frames the completeness question.

### checked_sources

- 2026-09-19 finite Grothendieck quotient theorem
- 2026-09-17 finite K0 quotient theorem
- Ren–Wang arXiv:2609.18681
- assigned RESULT.md

### residual_risks

- No residual novelty survives under implication-based comparison.

## Scientific value — FAIL

The finite-abelian obstruction mechanism is mathematically worthwhile, but it was already established by the earlier broader theorem. The only residual order-of-defect statement is a routine application of the earlier iff criterion and direct-sum additivity, so it does not meet the value bar as a separate finding.

### Value sources

- earlier full finite-Grothendieck-quotient theorem
- assigned direct-sum corollary

### Value risks

- Failure is due to duplication/mechanical implication, not incorrectness.

## Limitations

- Correctness passes; originality and scientific value fail under prior published coverage.
- The failed package must preserve the original scientific evidence.
- No historical-priority claim beyond the repository chronology is needed for the scientific rejection.

## Disposition

**FAILED**
