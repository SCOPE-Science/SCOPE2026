# Independent Audit — 2026/09/13/063

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fa6615dc89830ae5706e64a9b0bd3f78221e624d`
- Disposition: **FAILED**

## Correctness

**FAIL** — The nonsplitting argument for the standard holomorphic tangent sequence is substantially sound: after averaging a hypothetical holomorphic retraction over the torus action, dbar-closedness forces the vertical coefficient to be constant and would make the nonzero Euler class omega_1+i omega_2 dbar-exact. Equal first Chern classes then show that this standard holomorphic tangent bundle cannot be polystable, hence it has no Hermitian-Yang-Mills Chern connection for that holomorphic structure. But the deposited headline makes two stronger statements not established by this argument. First, the existence of a slope-zero line subbundle proves non-stability, not 'strict semistability' unless semistability of the full tangent bundle is separately proved; the record explicitly withdraws any stability assertion for the quotient. Second, 'no Hull-Strominger solution with HYM tangent connection' is broader than 'no HYM Chern connection for the standard holomorphic tangent structure'. García-Fernández constructs Hull-Strominger solutions on torus bundles over K3 whose tangent connection is HYM by choosing an appropriate holomorphic bundle structure on the underlying smooth tangent bundle; that literature explicitly does not identify it with a preferred holomorphic tangent structure. Thus the standard-tangent obstruction does not exclude all HYM tangent connections, and the claimed two-horn divergence theorem overreaches its proof.

## Originality

**PASS** — The specific combination of an E8 crepant-resolution topology calculation, nonsplitting of the standard tangent extension, vanishing exceptional pairings, vanishing torus-field Futaki density, and the binary-icosahedral scalar edge-gap computation is not simply the statement of the cited general torus-bundle papers. The record contains a genuinely specialized synthesis and explicit E8 calculations. This originality does not cure the correctness defect in the headline inference.

## Scientific value

**FAIL** — Once the unsupported broad HYM-tangent conclusion is removed, the surviving theorem is a narrower obstruction for the standard holomorphic tangent Chern connection together with vanishing checks and a conditional gluing discussion. That no longer resolves the admitted existence-versus-obstruction target, because alternative HYM tangent holomorphic structures remain possible and the full bundle edge invertibility/gluing estimates are explicitly conditional. The corrected remainder is useful diagnostic information but not the claimed decisive result.

## Sources

- T-dual solutions of the Hull-Strominger system on non-Kähler threefolds (Mario García-Fernández): https://arxiv.org/abs/1810.04740 — Constructs torus-bundle Hull-Strominger solutions with a Hermitian-Yang-Mills tangent connection; the construction uses a holomorphic bundle structure on the underlying smooth tangent bundle rather than forcing the standard holomorphic tangent structure.
- Solutions to the Hull-Strominger System with Torus Symmetry (Anna Fino; Gueo Grantcharov; Luigi Vezzoni): https://doi.org/10.1007/s00220-021-04223-7 — Background on torus-symmetric Hull-Strominger solutions and the distinction between choices of tangent connection.

## Limitations

- The audit does not dispute the E8 Cartan determinant/positivity calculation or the scalar link eigenvalue calculation.
- The audit does not prove existence of an alternative HYM tangent connection on this exact E8 resolved space; it shows only that the deposited nonsplitting argument does not rule all such connections out.
- No claim is made that the standard holomorphic tangent bundle is unstable; only non-polystability/non-stability is forced by the displayed equal-slope subbundle plus nonsplitting.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
