# Independent Audit — 2026/09/15/017

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `99d09dfe18fbf4792f9e700e3f1414e74aebca95`
- Disposition: **FAILED**

## Correctness

**PASS** — The exponent-one conclusion is correct. The Moore-spectrum cofiber sequence gives 3·id_{V(0)}=0. In the V(1) cofiber sequence, the low 3-local stem calculation gives [Σ^5V(0),V(0)]=0 and both [V(0),V(0)] and [Σ^4V(0),V(0)] ≅ Z/3. For an essential v1 self-map, precomposition sends id to the nonzero v1 class and is an isomorphism, so [V(1),V(0)]=0; the naturality factorization of 3·id_{V(1)} through V(0) therefore vanishes. The null-map split case is also killed by 3. Nontrivial BP-homology then forces the exact stable 3-primary exponent to be one.

## Originality

**FAIL** — The key structural fact predates the record. Ichigi–Shimomura (2004), in their work on V(1) at the prime 3, explicitly use a V(0)-module structure ν∈[V(1)∧V(0),V(1)]_0. Since V(0)=S/3 and 3·id_{V(0)}=0, a unital V(0)-module is already annihilated by multiplication by 3. Thus the headline conclusion 3·id_{V(1)}=0 is an immediate consequence of established structure, even though the submitted cofiber proof is a valid alternative argument.

## Scientific value

**FAIL** — The record gives a neat elementary proof, but it does not add a new exponent theorem or a new computation of V(1): the decisive exponent-one fact is already encoded in the standard V(0)-module structure used in the literature. Its value is expository rather than a new independent research finding.

## Sources

- E(2)-invertible spectra smashing with the Smith-Toda spectrum V(1) at the prime 3 (Ippei Ichigi; Katsumi Shimomura): https://doi.org/10.1090/S0002-9939-04-07387-3 — The paper explicitly invokes the V(0)-module structure on V(1), which already forces multiplication by 3 to vanish.
- On the existence of the self map v_2^9 on the Smith-Toda complex V(1) at the prime 3 (Mark Behrens; Satya Pemmaraju): https://arxiv.org/abs/math/0303223 — Standard prime-3 V(1) background and self-map context.

## Limitations

- The audit accepts the submitted low-stem/cofiber proof as mathematically valid; rejection is for originality and scientific value.
- The prior V(0)-module citation concerns the standard essential Smith-Toda V(1); the record's additional null-v1 split case is elementary and not a new Smith-Toda theorem.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
