# Mathematical audit — 2026-10-01

## Final claim assessed

Exact tuple-orbit profiles of the five reduct groups of the Rado graph

## Correctness — PASS

PASS. Homogeneity of the Rado graph identifies injective ordered \(k\)-tuple orbits for the base automorphism group with labeled graphs on \(k\) vertices. Global complementation acts by translation by the all-ones edge vector. Vertex switching acts by the cut space, whose dimension is \(k-1\); adjoining complementation adds one independent translation for \(k\ge3\). Therefore the injective orbit counts are the stated powers of two, and the full ordered-tuple counts follow by partitioning coordinates by equality pattern, giving the Stirling transform. The package verifier exhaustively reproduces these translation-orbit counts through its finite range.

## Originality — FAIL

FAIL. Bodirsky--Pinsker's complete primary text restates Thomas's classification of the five closed supergroups exactly as the automorphism group, complement extension, switch extension, complement-plus-switch extension, and full symmetric group. Classical Seidel switching theory identifies switching classes with two-graphs, and the cut translations on a fixed labeled \(k\)-set form a \(k-1\)-dimensional binary space. Once those established ingredients are combined with Rado homogeneity, each claimed injective orbit count is an immediate quotient-cardinality calculation; the Stirling transform for repeated tuple coordinates is standard equality-pattern bookkeeping. Exact wording of the profile is not required under the implication standard.

### equivalent_formulations

Searches: Rado graph five closed supergroups complement switch tuple orbits; Mallows Sloane switching classes two-graphs cut space

Evidence: The five groups are explicitly described in the primary reduct-classification literature. Classical switching-class theory gives the same quotient by vertex-switch translations.

Reasoning: The edge-vector quotient used by the package is exactly the standard labeled switching-class formulation.
### broader_coverage

Searches: Bodirsky--Pinsker arXiv:0903.2553 full text; Mallows--Sloane DOI 10.1137/0128070

Evidence: Bodirsky--Pinsker give the five closed groups and define complement and switching generators. Mallows--Sloane/Seidel theory supplies the established switching equivalence and two-graph correspondence.

Reasoning: Together these ingredients mechanically dominate the finite injective orbit calculation.
### exact_database_or_table

Searches: Resultary semantic search for Rado reduct tuple-orbit profiles

Evidence: The assigned record is the exact textual match, but novelty fails by implication from older structural theory.

Reasoning: Absence of a verbatim orbit table does not establish originality when the values are immediate quotient dimensions.
### claim_vs_prior_implication

Searches: Thomas/Bodirsky--Pinsker five-group classification; standard Seidel switching equivalence on a labeled vertex set

Evidence: For \(k\) labeled vertices there are \(2^{\binom{k}{2}}\) edge vectors and a cut space of size \(2^{k-1}\); complementation contributes the extra independent binary translation in the relevant groups.

Reasoning: The package's formulas follow without a new nonstandard lemma; repeated coordinates then contribute the standard Stirling transform.

## Scientific value — FAIL

FAIL. The profile is a convenient summary, but after the five reduct groups and switching-class structure are known, all five injective counts are one-line dimensions of elementary binary translation spaces and the noninjective counts are a routine Stirling transform. This is a textbook-level specialization rather than a motivated mathematical gap.

## Source inspections

- **All reducts of the random graph are model-complete** — https://arxiv.org/abs/0903.2553. Material read: Primary full text through the group-classification statements and definitions of complement and switch. Assessment: DECISIVE_PRIOR_GROUP_STRUCTURE. Evidence: Theorem 2 lists precisely the five groups used by the package and defines the complement and switch generators.
- **Two-Graphs, Switching Classes and Euler Graphs are Equal in Number** — https://doi.org/10.1137/0128070. Material read: Primary abstract and bibliographic statement, supplemented by standard switching-class references. Assessment: ESTABLISHED_SWITCHING_EQUIVALENCE. Evidence: The classical theory identifies Seidel switching equivalence with two-graph structure; the finite cut-space cardinality is an elementary consequence of the switching definition.

## Limitations and residual risks

The formulas are correct, but they are rejected as a new finding because they are routine finite-orbit consequences of the classical five-group reduct classification and standard Seidel-switching/cut-space theory.

- No access limitation affects the failure: the implication uses only explicit group generators plus the elementary finite cut-space action.

## Disposition

**failed**
