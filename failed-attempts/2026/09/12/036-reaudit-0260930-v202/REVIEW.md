# Review status

Fresh independent audit: **FAIL**. The original package is retained as failed-attempt evidence.

- Correctness: **PASS** — Direct differentiation of F=Y^2 Z-X^3-X^2 Z over F_7 gives singular locus X=Y=0. In the Z-chart of the origin blow-up the strict transform is B^2-A^3-A^2=0 with the blow-up coordinate free, so A=B=0 is a singular line; the X- and Y-chart equations have no simultaneous zero of equation and gradient. Hence the one-step origin blow-up is not smooth. The homogeneous scaling homotopy contracts the affine cone to its vertex, so A^1-invariance of KH gives KH_{-1}(S)=KH_{-1}(F_7)=0. The claimed exact K_{-1}(S) is explicitly left open. A reproducibility defect was also found: METADATA names output/artifacts/geom.py and output/artifacts/ledger.py, but both paths are absent from the audited Git tree.
- Originality: **FAIL** — The core scientific content is covered by standard general facts: blowing up the vertex of an affine cone produces the total-space geometry governed by O(-1) over the projective base, so a singular nodal base leaves a singular blow-up; homotopy K-theory is A^1-invariant, so a positively graded cone contracts for KH. The F_7 coordinate check is therefore a specialization, not a new obstruction theorem.
- Scientific value: **FAIL** — The record diagnoses that a one-step smooth-square strategy fails for one named cone but leaves the requested exact K_{-1} group open. Because the obstruction is a direct instance of standard cone blow-up geometry and A^1 invariance, the object-specific calculation does not supply a motivated new boundary, classification or exact invariant.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for the complete assessment.
