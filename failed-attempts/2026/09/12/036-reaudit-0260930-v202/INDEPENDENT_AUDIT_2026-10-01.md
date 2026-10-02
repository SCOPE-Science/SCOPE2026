# Independent mathematical audit — SCOPE-20260912-036

**Audit date (UTC):** 2026-10-01 (UTC)  
**Disposition:** failed

## Final claim reviewed

Single-square cdh obstruction for the cone over the split nodal cubic over F7 with KH_{-1} vanishing

## Correctness — PASS

Direct differentiation of F=Y^2 Z-X^3-X^2 Z over F_7 gives singular locus X=Y=0. In the Z-chart of the origin blow-up the strict transform is B^2-A^3-A^2=0 with the blow-up coordinate free, so A=B=0 is a singular line; the X- and Y-chart equations have no simultaneous zero of equation and gradient. Hence the one-step origin blow-up is not smooth. The homogeneous scaling homotopy contracts the affine cone to its vertex, so A^1-invariance of KH gives KH_{-1}(S)=KH_{-1}(F_7)=0. The claimed exact K_{-1}(S) is explicitly left open. A reproducibility defect was also found: METADATA names output/artifacts/geom.py and output/artifacts/ledger.py, but both paths are absent from the audited Git tree.

## Originality — FAIL

The core scientific content is covered by standard general facts: blowing up the vertex of an affine cone produces the total-space geometry governed by O(-1) over the projective base, so a singular nodal base leaves a singular blow-up; homotopy K-theory is A^1-invariant, so a positively graded cone contracts for KH. The F_7 coordinate check is therefore a specialization, not a new obstruction theorem.

### Equivalent formulations
Reasoning: The record’s singular-cylinder description is equivalent to specializing the general cone blow-up geometry to the nodal cubic.

Searches:
- Resultary nodal cone blow-up KH query
- cone blow-up total space O(-1)

Evidence:
- The Z-chart calculation is the local-coordinate form of the standard vertex blow-up of an affine cone.

### Broader coverage
Reasoning: Those frameworks dominate the stated one-object diagnostic, although the singular-base case needs the obvious local singularity check.

Searches:
- T. Yusof, K_{-1} and higher reduced K-groups of cones of smooth plane curves
- Cortinas-Haesemeyer-Schlichting-Weibel on cdh and negative K-theory

Evidence:
- Prior cone/KH literature sets up vertex blow-ups and A^1-invariant homotopy K-theory in substantially broader settings.

### Exact database or table
Reasoning: No exact table is needed because the claimed obstruction follows from broader geometry.

Searches:
- Resultary exact split nodal cubic F7 query

Evidence:
- Resultary returned the same SCOPE record and no separate exact table.

### Claim versus prior implication
Reasoning: The final headline statements are mechanically implied by these prior general principles plus elementary differentiation.

Searches:
- general affine-cone blow-up geometry
- KH A^1-invariance

Evidence:
- A singular projective base yields a singular total-space chart; homogeneous scaling is an A^1-contraction.

### Source inspections

- **K_{-1} and higher reduced K-groups of cones of smooth plane curves** (doi:10.1007/s40840-021-01175-y). Trigger: closest cone K-theory/blow-up treatment. Material read: primary article’s geometric setup for blowing up an affine cone at its vertex and the resulting exceptional/projective geometry. Method: full-text inspection. Assessment: general cone setup predates the record; the F_7 nodal coordinate specialization is not a new general mechanism. Evidence: The blow-up-at-vertex construction is standard cone geometry rather than a phenomenon peculiar to this equation.
- **Cyclic homology, cdh-cohomology and negative K-theory** (Annals of Mathematics 167 (2008)). Trigger: KH/cdh background used by the claim. Material read: primary theorem-level material on cdh descent and homotopy K-theory context. Method: full-text/source comparison. Assessment: supplies the broader homotopy-K/cdh framework; no exact F_7 coordinate calculation is needed for A^1 contraction. Evidence: KH is the A^1-invariant theory used in cone descent arguments.

### Checked sources

- Resultary semantic search
- Yusof 2022 primary article
- Cortinas-Haesemeyer-Schlichting-Weibel 2008 primary paper
- assigned Git tree and declared artifact paths

### Residual risks

- The record’s statement that the “correct descent needs” a specific conductor/Frobenius route is methodological guidance, not a proved uniqueness claim, and was not treated as an additional theorem.
- The two declared reproducibility scripts are absent from the audited tree.

## Scientific value — FAIL

The record diagnoses that a one-step smooth-square strategy fails for one named cone but leaves the requested exact K_{-1} group open. Because the obstruction is a direct instance of standard cone blow-up geometry and A^1 invariance, the object-specific calculation does not supply a motivated new boundary, classification or exact invariant.

## Limitations

- The exact group K_{-1}(S) remains open.
- The two reproducibility paths declared in METADATA.json, output/artifacts/geom.py and output/artifacts/ledger.py, are absent from the audited tree.

The finding is not accepted because all three scientific axes do not pass. The original research files and evidence are preserved in the failed-attempt package.
