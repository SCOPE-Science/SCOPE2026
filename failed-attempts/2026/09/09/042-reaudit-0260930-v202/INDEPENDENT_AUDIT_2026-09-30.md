# Independent audit — SCOPE-20260909-042

Audited at: 2026-09-30T22:49:30Z

Final disposition: **failed**.

## Correctness

**PASS** — Fresh matrix enumeration from the stated Fuchsian models reproduced all 24 hyperbolic triples, the closed word totals 3070 or 118097, zero nontrivial parabolics, and the quoted type counts/minima on representative cases including (2,4,5), (3,3,4), (4,5,6), and (6,6,6). A separate exact-affine Euclidean enumeration reproduced (3,3,3): 1969/78892/37236, (2,4,4): 69/2277/724, and (2,3,6): 59/2567/444 trivial/rotation/translation counts. The bounded census is correct as defined.

## Originality

**PASS** — No checked source gives this exact free-reduced spelling census to L=10 over all triples 2<=p<=q<=r<=6. Closest literature studies triangle-group geometry, congruence-surface systoles, or nonsystolic actions rather than this table.

### Equivalent formulations

Searches checked: published-record search: triangle group short word trace census p q r up to 6 length 10; web triangle group trace spectrum length 10.

Evidence: The exact semantic match was the present record.

Reasoning: No equivalent bounded table was located.

### Broader coverage

Searches checked: Schein-Shoan systolic length triangular modular curves; Karrer-Schwer-Struyve (2,4,5) (2,5,5) not systolic; Singerman Fuchsian subgroup geometry.

Evidence: These sources study geometric actions, subgroup/surface systoles, or general triangle groups, not all freely reduced generator spellings to L=10 in the stated model.

Reasoning: Their results do not imply the table counts/minima.

### Exact database or table

Searches checked: triangle group trace tables small p q r; short word trace spectrum von Dyck groups.

Evidence: No checked exact table covered all 24 triples and three Euclidean boundary cases with the same enumeration convention.

Reasoning: The table appears distinct from standard databases.

### Claim versus prior implication

Searches checked: standard Fuchsian trace classification |tr|>2; triangle-group presentation relators.

Evidence: Classical trace classification explains the labels but does not compute this finite list.

Reasoning: The numeric census requires enumeration.

### Source inspections

- **The Triangle Groups (2, 4, 5) and (2, 5, 5) are not Systolic** (https://doi.org/10.1007/s00373-020-02209-1): NOT_COVERING. Material read: open-access full HTML including abstract, main theorem and argument context. Proves nonsystolicity of two groups; it does not enumerate trace spectra or short words.
- **Systolic length of triangular modular curves** (https://arxiv.org/abs/2012.08796): NOT_COVERING. Material read: abstract and scope. Computes upper bounds for systoles of congruence-subgroup surfaces using generator traces, not the L=10 spelling census.

Checked sources: published SCOPE findings search; Karrer-Schwer-Struyve 2020; Schein-Shoan 2020; standard triangle-group references.

Residual risks: Older computational trace tables may be poorly indexed; no exact matching table was found.

## Scientific value

**FAIL** — The enumerated objects are freely reduced spellings, not relator-reduced group elements: relations such as \(\(a^p\)\)=1 and \(\(b^q\)\)=1 make many length-9/10 witnesses equivalent to much shorter words, so the cutoff L=10 and word counts are presentation-spelling artifacts rather than a natural length-spectrum invariant. Together with the arbitrary small parameter box p,q,r<=6, this makes the table a routine bounded enumeration without a sufficiently motivated mathematical boundary. Correctness and novelty alone do not establish value.

## Scientific rejection

The computation is preserved, but a finding is accepted only when correctness, originality and value all pass. The failed value assessment above therefore prevents validation.
