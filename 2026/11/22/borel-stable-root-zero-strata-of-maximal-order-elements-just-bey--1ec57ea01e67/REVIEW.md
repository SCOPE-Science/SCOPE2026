# Self-review

## Correctness

PASS. The path expansion of \(N^{p^k}\) at size \(p^k+2\) has exactly three possible entries, and their formulas give an exhaustive partition by nonzero first-superdiagonal support. The group exponent boundary follows from Frobenius in characteristic \(p\); the hyperplane coefficient condition follows exactly from the admissible location of one length-two path step. A standalone brute-force verifier evaluates actual matrix powers and every zero-pattern cell over small prime fields. The infinite theorem rests on the path argument, not enumeration.

## Originality

PASS for the *Borel-invariant geometry* under inspected literature, not for the unconditional Jordan-type count or abstract computability of zero-pattern counts. Dolfi–Singh–Yadav (arXiv:1905.04244) study power images; Yip (arXiv:1703.00057) already counts unrestricted Jordan types; Van Peski (arXiv:2407.19578) extends unrestricted Jordan statistics. The closest published power-image finding classifies targets, not maximal-order sources. Mallahi-Karai–Ram–Salmasian (arXiv:2611.21451) provides a broad incidence-algebra counting framework that can plausibly recover conditional *numerical* counts by inclusion–exclusion; this substantially limits numerical novelty, but does not classify the actual hyperplane-bundle loci over arbitrary fields. The residual risk is an older unlocated theorem giving this precise Borel-support geometric stratification.

## Value

PASS. Simple-root zero patterns are intrinsic Borel-conjugacy invariants, not arbitrary coordinate slices. The canonical dimension \(p^k+2\) is the first one where the second superdiagonal affects attainment of the new maximal element order. The theorem determines for every Boolean pattern whether maximal-order elements exist and, when nontrivial, identifies their exact codimension-one obstruction. It exposes a structural adjacency phenomenon unavailable from unconditional Jordan counts alone.

## Verification and limits

The proof applies to any characteristic-\(p\) field, while numerical probabilities require a finite field. Verified finite cases are explicitly identified in VERIFICATION.md. No claim is made for larger offsets or for conjugacy-class counts. General incidence-algebra counting may imply the numeric expressions, and the publication-priority risk for geometric statements is nonzero.

Self-review: passed. Independent audit: not yet performed.
