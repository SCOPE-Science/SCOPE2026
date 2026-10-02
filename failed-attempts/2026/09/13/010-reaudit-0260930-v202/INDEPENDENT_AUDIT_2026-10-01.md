# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260913-010`

Disposition: **FAILED**

## Correctness — PASS

For \(f=x^5+y^6+z^7+x^3y^2z\), the tail monomial has weighted degree \(226>210\) for weights \((42,35,30)\), so the Fermat face controls the local Newton number. The local Jacobian leading monomials are \(x^4,y^5,z^6\), giving \(\mu=4\cdot5\cdot6=120\). Fresh exact Gröbner reconstruction gives global Jacobian colength 136 and Tjurina colength 101; the lex elimination contains \(z^{12}(81z^8+13671875)\), consistent with 16 nonzero simple critical points once the origin's multiplicity 120 is removed. Dyckerhoff's theorem identifies Hochschild homology of the matrix-factorization category with the Jacobian algebra, giving total dimension 120, and the standard critical-locus Behrend formula in ambient dimension three gives value 120. Thus the numerical statements are internally consistent and independently reproduced.

## Originality — PASS

General ingredients are classical—Kouchnirenko for \(\mu\), Saito for quasihomogeneity, Dyckerhoff for Hochschild homology, and Behrend for the critical-locus sign—but searches did not locate the exact polynomial's combined local/global tuple \(\mu=120,\tau=101\), gap 19, global Jacobian colength 136 and 16 off-origin Morse points. The categorical equality \(\dim HH=\mu\) and the Behrend equality are prior general consequences, so originality is confined to the explicit polynomial computation rather than those identities themselves.

### Equivalent formulations

**Searches:** published SCOPE records for the exact polynomial and Milnor–Tjurina tuple; primary literature search for x^5+y^6+z^7+x^3y^2z

**Evidence:** No independent exact occurrence of this polynomial with the 120/101/136 tuple was located.

Milnor/Tjurina colengths and the 16 off-origin critical points are equivalent algebraic formulations of the explicit Jacobian/Tjurina computations for this germ.

### Broader coverage

**Searches:** Kouchnirenko Newton polyhedra Milnor number; Dyckerhoff matrix factorizations Hochschild Jacobian algebra; Behrend critical locus Milnor fibre

**Evidence:** These sources cover the general implications \(\mu=\nu_{Newton}\) under nondegeneracy, \(HH(MF)\cong Jac(f)\), and the Behrend critical-locus formula.

They explain several consequences but do not supply the polynomial-specific Tjurina and global-critical calculations.

### Exact database or table

**Searches:** published SCOPE semantic search: exact polynomial Milnor 120 Tjurina 101; web exact-polynomial search

**Evidence:** The same SCOPE record was the only exact finding located; no established singularity table entry for this polynomial was found.

Best-of-knowledge novelty remains for the explicit tuple, with the caveat that absence from search is not proof of novelty.

### Claim versus prior implication

**Searches:** Dyckerhoff Theorem 6.6; Kouchnirenko theorem; Behrend critical-locus formula

**Evidence:** Prior theory mechanically implies the HH and Behrend numbers once \(\mu=120\) is known, but does not mechanically give \(\tau=101\), global colength 136, or the 16-point decomposition without polynomial computation.

The final explicit tuple contains computational information not exhausted by the cited general theorems, so the claim is not wholly covered.

### Source inspections

- **Compact generators in categories of matrix factorizations** (https://arxiv.org/abs/0904.4713). Trigger: Hochschild dimension assertion. Material read: Section 6.3, especially Theorem 6.6. Method: full-text inspection. Assessment: covers the general \(HH(MF)\cong\) Jacobian-algebra implication. Evidence: Theorem 6.6 identifies Hochschild homology of the 2-periodic matrix-factorization dg category with the Jacobian algebra, concentrated in one parity.
- **Polyèdres de Newton et nombres de Milnor** (https://doi.org/10.1007/BF01389769). Trigger: Newton-number computation. Material read: the theorem-level Newton nondegeneracy implication as used by the record. Method: primary theorem comparison. Assessment: covers the general local Milnor-number step. Evidence: For convenient Newton-nondegenerate hypersurface germs, the Milnor number equals the Newton number.

### Checked sources

- published SCOPE semantic search
- Kouchnirenko 1976
- Dyckerhoff arXiv:0904.4713
- Behrend 2009
- exact-polynomial literature search

### Residual risks

- A specialized singularity database not indexed by the searches could contain the same explicit polynomial tuple.
- The global 16-point simplicity was inferred from exact colength/elimination structure and the record's decomposition; no independent symbolic factorization over an algebraic closure was stored in the public package.

## Scientific value — FAIL

The polynomial is an isolated ad hoc Fermat-plus-tail example, and the package gives no prior mathematical motivation for needing precisely its Tjurina number, global critical count, or the numerical coincidence once \(\mu\) is known. The calculations are correct and plausibly unpublished, but they amount to routine exact Gröbner/Newton evaluation of one unmotivated germ; the general HH/Behrend equalities are already known.

## Limitations

- The exact polynomial tuple is best-of-knowledge original, but the general HH/Behrend equalities are prior consequences once the Milnor number is known.
- No claim of full singularity classification is made.

The finding is not accepted because all three scientific axes do not pass. The original research files and evidence are preserved in the failed-attempt package.
