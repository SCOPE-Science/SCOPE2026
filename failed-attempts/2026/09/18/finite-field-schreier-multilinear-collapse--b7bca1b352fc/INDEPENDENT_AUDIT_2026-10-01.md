    # Independent mathematical audit — 2026-10-01

    ## Record

    **Locally finite Schreier multilinear algebras collapse over finite fields**

    Disposition: **FAILED**.

    ## Correctness — PASS

    Assuming the cited locally finite Schreier classification, the vanishing argument is correct. The essentially-unary group-action case cannot realize vector addition. In the affine/vector-space case every polynomial operation is affine; evaluating an added multilinear operation with all but one variable equal to the original additive zero makes the function constant in that variable, forcing every affine coefficient to vanish, and evaluation at the all-zero tuple fixes the constant. The zero-product converse and the unital contradiction are then standard.

    ## Originality — FAIL

    The result is a direct corollary of the 2026 Kearnes--Moorhead--Szendrei classification together with the elementary form of polynomial operations on a vector space. The prior theorem already forces every locally finite Schreier variety into the essentially-unary or affine/vector-space alternatives; the presence of ordinary vector addition excludes the first, and multilinearity immediately kills every higher-arity affine operation. Under an implication-based originality standard, the finite-field collapse is therefore covered even though the exact corollary is not quoted in the abstract.

    ### Equivalent formulations

Searches: locally finite Schreier varieties finite field multilinear algebra zero multiplication; Schreier finite field multilinear collapse; published SCOPE search: Schreier finite field

Evidence: No separately named theorem was located, but the Kearnes--Moorhead--Szendrei classification gives an equivalent structural route that immediately yields the claim.

Reasoning: Changing the phrasing from polynomial equivalence to vanishing multilinear products does not escape coverage when the latter is a one-step consequence of the former.

### Broader coverage

Searches: Kearnes Moorhead Szendrei Locally finite Schreier Varieties arXiv:2609.19651; Burgin Schreier varieties linear Omega-algebras 1974; Lewin Schreier varieties linear algebras 1968

Evidence: The 2026 paper classifies locally finite Schreier varieties via finite group-action or finite-field affine/vector-space structure. Older linear-algebra papers provide historical narrower context.

Reasoning: The 2026 classification is strictly broader than the finite-field multilinear corollary and supplies all non-elementary structure needed for it.

### Exact database or table

Searches: published SCOPE repository search: Schreier finite field; published-record semantic query: locally finite Schreier multilinear finite field

Evidence: Repository code search returned no separate exact record; the semantic record-search service returned no usable result.

Reasoning: This is not a database/table claim. The decisive originality failure comes from theorem implication, not duplicate tabulation.

### Claim versus prior implication

Searches: arXiv:2609.19651 polynomially equivalent G-set vector space finite field; affine polynomial operations vector spaces

Evidence: The classification places the variety in the vector-space alternative once ordinary addition rules out the group-action alternative; multilinearity then forces affine higher-arity operations to be zero.

Reasoning: The final theorem is mechanically implied by the broader prior classification plus a textbook affine-linearity observation, so it is covered under the required implication test.

    ## Source inspections

    - **Locally finite Schreier Varieties** (arXiv:2609.19651): trigger — the record explicitly invokes its classification as the only substantive structural input; material read — primary abstract plus detailed lawful public theorem summaries describing the group-action/vector-space dichotomy; full primary text could not be retrieved through the lawful routes available in this audit; assessment — COVERING through a decisive broader classification. Evidence: The public theorem summaries identify the two polynomial-equivalence alternatives. With the record's ordinary vector addition, only the vector-space alternative remains.
- **Schreier varieties of linear Omega-algebras** (DOI:10.1070/SM1974v022n04ABEH001705): trigger — closest older linear-algebra prior art cited by the record; material read — available abstract/bibliographic description of homogeneous-identity linear Omega-algebra results; assessment — background prior art; not needed for the decisive coverage finding. Evidence: The older source concerns linear Omega-algebras and homogeneous identities; the 2026 classification is the stronger covering result.

    ## Checked sources

    - arXiv:2609.19651
- Burgin (1974) DOI:10.1070/SM1974v022n04ABEH001705
- Lewin (1968) DOI:10.1090/S0002-9947-1968-0224663-5
- published SCOPE repository searches

    ## Residual risks

    - The primary 2026 full text was not lawfully retrievable during this run, but the coverage comparison is already decisive from the classification statement publicly available; inaccessible details would not restore originality unless the public classification statement were materially misleading.

    ## Scientific value — FAIL

    The collapse is clean and correct, but as a research finding it is a short mechanical specialization of the newly published general classification: once the affine alternative is known, multilinearity annihilates the extra operations in a few lines. Under the stated value bar this is a routine corollary rather than an independently motivated mathematical gap.

    ## Limitations

    The mathematical implication is correct, but the research finding is rejected because it is mechanically covered by the broader locally finite Schreier classification and is a routine affine-linearity corollary.

    This document records a mathematical assessment of the stated claim and its literature context. It does not convert historical same-model review evidence into independent evidence.
