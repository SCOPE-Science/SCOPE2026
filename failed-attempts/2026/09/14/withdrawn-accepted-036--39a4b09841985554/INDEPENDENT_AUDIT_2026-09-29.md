# Independent Audit — 2026/09/14/036

Audit date: 2026-09-29 (UTC)
Audited tree: `ccb69abf46fad81bf5cefc4108d040224373ac58`

## Disposition

**FAILED** — Rejected on originality and value: the all-nonzero-coupling second-variation non-integrability theorem is already covered by a broader 2025 sextic result; the Heisenberg realization is an incremental refinement.

## Correctness

**PASS**. The variational equations were independently differentiated from H6: along y=0 one gets y1''=0 and y2''+3a x0^3 y1^2=0, while the tangential operator D^2+5x0^4 factors over K through b=x0''/x0'. The claimed normal second-variation monodromy has central commutator U1T2-U2T1; the submitted no-exact-combination argument for dx/w and x^3 dx/w on w^2=2h-x^6/3 is consistent with standard hyperelliptic function-field calculus and does force a nonzero period determinant. Thus a!=0 gives a solvable but nonabelian unipotent extension and the Morales-Ramis-Simo obstruction is mathematically credible. The numerical period determinant is only corroboration and is not needed for this conclusion.

## Originality

**FAIL**. A November 2025 preprint by Neykova and Georgiev studies a general two-degree-of-freedom homogeneous sextic potential containing a D r^3 z^3 term, explicitly uses second variations and a nonzero logarithmic residue, and states Theorem 3: D!=0 implies non-integrability. After the elementary homogeneous/canonical scaling that normalizes the x^6 coefficient, the submitted family has D proportional to a, so its all-a!=0 meromorphic non-integrability conclusion is already a direct specialization of that broader prior result. The submitted Heisenberg/period description is a sharper presentation, but it does not restore originality of the central non-integrability claim as published.

## Scientific value

**FAIL**. The exact period-commutator calculation is technically nontrivial and may be a useful alternate proof, but the research conclusion advertised for the family—second-variation non-integrability whenever the cubic-cubic coupling is nonzero—was already available for a broader sextic potential class before this record. As a standalone finding, the remaining identification of a Heisenberg realization is an incremental structural refinement rather than a new family-level theorem of sufficient value under the audit standard.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://www.preprints.org/manuscript/202511.0820 — Neykova–Georgiev, 2025 preprint: general homogeneous sextic, second variations, nonzero logarithmic residues; Theorem 3 states D!=0 implies non-integrability.
- https://www.numdam.org/item/10.1016/j.ansens.2007.09.002.pdf — Morales–Ramis–Simó higher-variational-equation obstruction used as the standard black box.

Independent checks:
- Independently differentiated VE1/VE2 along y=0 and checked the tangential factorization condition b' + b^2 = -5x0^4.
- Checked the hyperelliptic primitive reduction: for B=u(x)+v(x)w, dB=(r0+r3 x^3)dx/w reduces to 2Pv'+P'v=2(r0+r3x^3), matching the submitted obstruction to exactness.
- Matched the broader 2025 sextic theorem to this family: a canonical homogeneous scaling normalizing x^6 sends the r^3z^3 coefficient to a nonzero scalar multiple of a.

Limitations:
- The 2025 source is a preprint rather than a peer-reviewed article; it nevertheless predates the record and is valid prior art for originality.
- No inaccessible source is represented as read.

