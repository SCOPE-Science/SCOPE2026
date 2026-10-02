# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-a74f4be4d9c8`

## Correctness — PASS

The character count is correct. Rossmann's all-ring Proposition 2.3 gives a class-two central extension with commutator subgroup \(\mathbf F_qE\), abelian quotient \(\mathbf F_qV\), and the graphical commutator form. Fixing a central character therefore gives a projective representation problem for the finite abelian quotient. The standard projective-representation theorem says that the irreducible projective representations attached to a cocycle are parametrized by the dual of the radical of its commutator bicharacter and all have degree the square root of the radical index. Trace-pairing nondegeneracy identifies that radical with \(\ker B_\Gamma(y)\). Hence rank \(2i\) contributes exactly \(q^{n-2i}\) characters of degree \(q^i\), including characteristic two. The complete-bipartite and complete-graph formulas then follow from standard finite-matrix rank counts.

### Correctness sources

- Rossmann 2022 full text, especially §1.6 and Proposition 2.3
- classical projective representations of finite abelian groups
- assigned RESULT.md

### Correctness risks

- The theorem does not imply polynomial dependence on \(q\) for arbitrary support-constrained alternating matrix spaces.

## Originality — FAIL

The final claim is already implied by prior general representation theory plus Rossmann's published all-ring group structure. Rossmann supplies the exact central extension and commutator matrix for every characteristic. Classical projective-representation theory for finite abelian groups supplies the radical parametrization and common degree for every cocycle, without an odd-characteristic hypothesis. Combining those two statements immediately gives the audited rank formula; the complete-bipartite clause is then the standard rectangular-matrix rank count. The absence of the formula from Rossmann's odd-\(q\) discussion does not make this mechanically implied specialization original under the required implication-based standard.

### equivalent_formulations

Searches:
- Resultary: graphical group character degrees characteristic 2 alternating rank formula
- Rossmann full-text §1.6 and Proposition 2.3
- projective representations of finite abelian groups radical bicharacter

Evidence:
- Rossmann already identifies the all-characteristic commutator extension.
- Backhouse's projective-representation theorem states that all irreducible projective representations have degree equal to the square root of the radical index and are labelled by the dual radical.

Reasoning:
The audited twisted-group-algebra lemma is an instance of the classical projective-representation theorem, and its radical is exactly Rossmann's kernel matrix.

### broader_coverage

Searches:
- classical twisted group algebra/projective representation theory
- Herzog–Lev 2006 class-two p-groups
- Rossmann 2022

Evidence:
- The prior theory is strictly broader than graphical groups and does not rely on odd characteristic for complex projective representations of a finite abelian quotient.

Reasoning:
Specializing the general theorem to Rossmann's extension covers the full final claim.

### exact_database_or_table

Searches:
- current Resultary graphical-group records
- standard alternating/rectangular matrix rank counts

Evidence:
- No table is needed: theorem-level implication already covers the formula.

Reasoning:
The K_{a,b} formula is a standard rank-count substitution once the general character formula is known.

### claim_vs_prior_implication

Searches:
- statement-by-statement implication comparison

Evidence:
- For each \(y\), prior projective-representation theory gives number \(|\operatorname{rad}eta_y|\) and degree \(\sqrt{|A|/|\operatorname{rad}eta_y|}\); Rossmann gives \(\operatorname{rad}eta_y=\ker B_\Gamma(y)\).

Reasoning:
Substitution yields exactly \(q^{n-2i}\) characters of degree \(q^i\) for rank \(2i\), with no new lemma required.

### source_inspections

- **Enumerating conjugacy classes of graphical groups over finite fields** — https://doi.org/10.1112/blms.12665. Trigger: Primary graphical-group structure and the odd-characteristic character question. Material read: Full open-access HTML through §1.6 and Proposition 2.3, including the odd-\(q\) rank-count discussion. Method: Primary theorem and implication comparison. Assessment: Supplies the all-characteristic central extension and exact commutator matrix needed for the specialization. Evidence: Proposition 2.3 gives commutator subgroup \(\mathbf F_qE\), quotient \(\mathbf F_qV\), and equality of group commutator with the graphical Lie bracket for every commutative ring.
- **On the form of the finite-dimensional projective representations of an infinite abelian group** — https://doi.org/10.2307/2038859. Trigger: General projective-representation theorem for abelian groups. Material read: Primary abstract stating the radical-index degree theorem and dual-radical parametrization. Method: General-theorem implication comparison. Assessment: COVERING ingredient. Evidence: The square root of the index of the cocycle radical is the degree of every projective irreducible, and projective irreducibles are labelled by the dual radical.
- **A character theory for projective representations of finite groups** — https://doi.org/10.1016/j.laa.2014.11.027. Trigger: Modern finite-group formulation of the same projective theory. Material read: Accessible primary proposition text for the finite abelian case. Method: Independent theorem cross-check. Assessment: Confirms the classical abelian projective-representation mechanism. Evidence: Its abelian-group proposition derives irreducible projective degrees from maximal cocycle-symmetric subgroups.

### checked_sources

- Rossmann 2022 full text
- Backhouse 1973 projective-representation theorem
- projective character theory for finite abelian groups
- current Resultary graphical-group search
- assigned RESULT.md

### residual_risks

- No historical-priority claim is made about who first noticed this specialization; the scientific originality failure is implication-based.

## Scientific value — FAIL

The formula is useful, especially in characteristic two, but under the required value bar its proof is a direct specialization of classical projective-representation theory to Rossmann's already published central extension. The complete-bipartite expression adds only a standard rectangular rank count. This is a clean observation, not a new structural lemma or nonmechanically determined invariant.

### Value sources

- Rossmann Proposition 2.3
- classical projective representations of abelian groups
- standard finite-matrix rank enumeration

### Value risks

- Failure of value here reflects mechanical implication, not mathematical incorrectness.

## Limitations

- Correctness passes.
- Originality and scientific value fail because prior general representation theory plus Rossmann's all-ring structure mechanically imply the result.
- Arbitrary-graph polynomiality remains unresolved.

## Disposition

**FAILED**
