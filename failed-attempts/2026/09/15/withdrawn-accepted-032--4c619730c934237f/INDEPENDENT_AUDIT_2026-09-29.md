# Independent audit — 2026/09/15/032

**Date:** 2026-09-29  
**Disposition:** **FAILED**  
**Audited tree:** `3672ad9d6ea955bddd0179e90007de638c52c0a7` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**PASS** — The finite-dimensional calculations are correct. For B1=C^3 with weights (0.6,0.2,0.2), any unitary u has |tau1(u)|>=0.6-0.4=0.2, so ker(tau1) contains no unitary. B2=C^5 with the uniform trace does contain trace-zero unitaries. The reduced D-amalgamated free product of D⊗B1 and D⊗B2 over D=M2 factors canonically as D⊗((B1,tau1)*(B2,tau2)); Dykema’s finite-dimensional abelian free-product criterion applies to the scalar factor and gives the advertised simple unique-trace example.

## Originality

**FAIL** — The substantive phenomenon is already present in Dykema’s scalar reduced free products: Avitzour’s kernel-unitary hypothesis is sufficient but not necessary for simplicity. Passing from the scalar example to amalgamation over M2 by tensoring every algebra and expectation with M2 is formal and introduces no new amalgamated mechanism.

## Value

**FAIL** — As a sanity-check counterexample the construction is correct, but as a research record it is only a tensor amplification of a known scalar non-necessity phenomenon. It does not provide a new criterion, obstruction, invariant, or genuinely amalgamated example, so it falls below the scientific-value threshold for a validated finding.

## Literature/evidence checked

- [Dykema, Simplicity and the stable rank of some free product C*-algebras](https://arxiv.org/abs/funct-an/9702015): Gives a necessary-and-sufficient simplicity criterion for reduced free products of finite-dimensional abelian algebras and explicitly goes beyond Avitzour’s sufficient conditions.
- [McClanahan, Simplicity of reduced amalgamated products of C*-algebras](https://doi.org/10.4153/CJM-1995-032-0): Background for sufficient simplicity criteria in genuinely amalgamated reduced free products; the filed example does not use a new amalgamated mechanism.

## Limitations of this audit

Main-branch tree and blob guards were checked before staging and matched the assignment. Literature search is claim-specific and is not a proof of absolute priority. GitHub was read only; no repository writes were made. No inaccessible source is claimed as read.
