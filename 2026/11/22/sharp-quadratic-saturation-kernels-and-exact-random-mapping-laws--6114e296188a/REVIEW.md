# Review of bounded unary orbit-type saturation

## Correctness — PASS
The quantified domain is all integers \(d\ge1\) and all finite nonempty total unary functions. Every equality pattern of one orbit prefix has a first-repeat form \((t,c)\) with \(t+c\le d\), or has no repeat. Distinct required cycle lengths force disjoint components of at least \(d\) vertices; an additional point is necessary to realize the no-repeat type. Exactly one chain extension attains the bound, with the stated automorphism factors. The two generating functions follow from component SET decompositions with mandatory maximum-height conditions; the singular expansion at \(z=e^{-1}\) proves the limit. All critical steps are included in RESULT.md. Direct standard-library checks in `verify.py` independently enumerate all maps on up to six points and reproduce the exact coefficient formulas. Finite tests support rather than replace the full proof.

## Originality — PASS within inspected evidence
The strongest recent comparison, Kuželka, arXiv:2608.30580, was read in its accessible full HTML text, including the general model-counting theorem and forward-profile/cycle/decorated-tree algorithm (Sections 3, 8.1.2–8.1.6). Its universal algorithm can in principle count this particular fixed existential-conjunction property and is not claimed to be new. The precise \(d^2+1\) sharp universal saturation kernel, its \(d\) extremal isomorphism types, the closed explicit two-term EGF and limiting probability product were not stated or directly established in the inspected text. The classical random-mapping component EGF and analytic method are separately credited to Soria and Flajolet–Odlyzko. Searched published-finding corpus records concerning unary-function FO spectra, idempotent quantifier-free profiles, and generic unary type spaces; their statements concern different invariants and do not imply the complete bounded all-type saturation package. Search cannot prove historical novelty. The Flajolet–Odlyzko conference chapter was accessible only at abstract level and the large older literature presents a residual priority risk.

## Value — PASS
There is a concrete finite-model-theoretic gap between counting individual one-variable equality types and constructing the smallest single function realizing all types simultaneously. The sharp quadratic resource threshold and classification of every extremizer are structurally meaningful, while the finite-size EGF and fixed-depth random saturation limit quantify how common complete local expressivity is among finite unary structures. The precise counts are not merely redefinitions of generic model-counting tractability. The limit is restricted to fixed depth; no uniform varying-depth assertion is made.

## Closest literature and limitations
- Ondřej Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580 (2026), full text inspected.
- Philippe Flajolet and Andrew M. Odlyzko, *Random Mapping Statistics* (1990), https://doi.org/10.1007/3-540-46885-4_34 (abstract level only).
- Michèle Soria, *Distribution of Image Points in Random Mappings* (1996), https://algo.inria.fr/seminars/sem96-97/soria.html (accessible seminar text inspected).

Independent historical-priority and mathematical verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
