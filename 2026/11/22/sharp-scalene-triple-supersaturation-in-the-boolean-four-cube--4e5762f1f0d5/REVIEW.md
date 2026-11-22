# Scientific assessment

## Correctness — PASS

The domain is the sixteen vertices of the Boolean four-cube, and the claim concerns unordered triples with three distinct Euclidean distances. The proof establishes the full-parity identity by direct Hamming-distance counting. Its global lower bound and all equality cases are obtained by the displayed maximal-index recurrence over exactly 65,536 masks. The standalone standard-library checker enumerates every mask, independently computes every scalene-triple count by direct incidence among 256 triples, compares full per-cardinality minima and equality predicates, and checks the parity identity. No sampled data are substituted for global proof. The code was executed successfully from its actual file path. The theorem has no infinite-dimensional implication.

## Originality — PASS (best-knowledge, priority provisional)

Ionin (2009) covers maximal cardinality and structural bounds for Hamming-space isosceles sets, but the inspected Hamming-space sections do not give quantitative minimum counts of scalene triangles for each cardinality of the sixteen-vertex cube. Yi (2026) gives Euclidean isosceles cardinality and structure results, not a fixed-cube defect profile. Mukkamala (2025) forbids monochromatic equilateral triangles of one Hamming length, which neither contains nor implies the scalene-triple minimization. Searches under isosceles/scalene/nonisosceles, Boolean cube/four-cube/Hamming, supersaturation, and antipodal parity classes did not reveal a statement implying the formula and equality types. Related published four-cube mathematical records concern Walsh spectra, geodesic transversals, and vertex-simplex distances, rather than scalene triple counts. Search failure is not proof of worldwide novelty; the residual risk is unindexed finite extremal tables.

## Mathematical value — PASS

This is a complete *supersaturation and rigidity law*: it quantifies how non-isosceles triples must appear when a fixed metric point set exceeds its maximum all-isosceles size, for every possible enlargement, and classifies all minimizers. The four-cube is the first Boolean cube whose parity halves contain two distinct nonzero pairwise distances (squared distances 2 and 4), making the antipodal-pair transition nontrivial. The exact switch after four added opposite-parity vertices identifies a genuine geometric mechanism rather than an isolated arbitrary count. This is a finite, natural benchmark for larger Hamming-space stability questions, not a claimed general theorem.

## Limits and references

The global part uses complete finite integer enumeration and is limited to the sixteen-vertex cube. This does not establish analogous bounds in any higher dimension or arbitrary Euclidean space. Historical-priority confidence is limited by the possibility of unindexed tables, and no independent audit has been conducted. The principal comparisons are Yi (arXiv:2611.05421), Ionin (doi:10.37236/230), and Mukkamala (arXiv:2506.18782).

Self-review: passed. Independent audit: not yet performed.
