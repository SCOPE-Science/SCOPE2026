# Scientific audit — SCOPE-20260913-028

Date: 2026-10-01 UTC

## Final claim

For a projective K3^[2]-type fourfold with Neron-Severi lattice U, the two primitive isotropic boundary rays cannot both be nef, hence the same holomorphic model cannot carry Lagrangian fibrations along both rays.

## Correctness

**PASS** — In U, the difference of the two primitive isotropic generators has square -2, is primitive, and has divisibility one; it pairs with the two isotropic rays with opposite signs. The K3^[2] wall-divisor classification makes this a genuine wall, while the possible square -10 wall type requires divisibility two and does not occur in this unimodular U. Therefore the wall separates the two isotropic boundary rays of the positive cone, so the closure of one Kähler chamber contains at most one. A holomorphic Lagrangian fibration supplies a nef isotropic pullback class, giving the stated obstruction. The lattice arithmetic was independently rechecked exactly.

Residual risk: The existence/model discussion relies on established period-map, Torelli, and cone results; the machine artifacts alone do not prove those geometric theorems.

## Originality

**FAIL** — The mathematical content is a direct specialization of the established K3^[2] wall-divisor and Kähler-cone theory: square -2 primitive classes are walls, and Kähler chambers are components cut by those wall hyperplanes. In NS=U, the elementary identity q(a f1+b f2)=2ab immediately supplies the separating square -2 class f1-f2. Thus the no-two-nef-rays conclusion is mechanically implied by prior general theory.

Residual risk: The exact sentence may not appear verbatim in the sources, but implication—not wording—is decisive for originality.

### Equivalent formulations

The K3^[2] wall-divisor description includes square -2 walls, which is the exact mechanism used by the record.

### Broader coverage

General monodromy/reflection theory and hyperkähler cone results cover the wall/reflection framework for the special U-polarized situation.

### Exact database or table

No table is relevant: this is a theorem implication, not a finite database claim.

### Claim versus prior implication

Once f1-f2 is recognized as a square -2 wall divisor, chamber separation immediately prevents both isotropic boundary rays from lying in one nef-cone closure.

## Value

**FAIL** — The deduction is a short lattice substitution into known cone/wall theorems and does not establish a new boundary phenomenon, classification, or independently motivated invariant. Its correctness is useful as a clarification, but the present value bar excludes routine specializations of general theory.

Residual risk: A distinct geometric construction or consequence not already forced by the general chamber theorem could change the assessment; none is supplied here.

## Sources inspected

- A note on the Kähler and Mori cones of hyperkähler manifolds — https://arxiv.org/abs/1307.0393 — COVERING: Square -2 classes are wall divisors; the paper also identifies the K3^[2] square -10 divisibility-two wall type.
- Prime exceptional divisors on holomorphic symplectic varieties and monodromy-reflections — https://arxiv.org/abs/0912.4981 — BROADER_COVERAGE: Supplies general geometric framework used by the record’s lattice reflection argument.
- Published finding SCOPE028 — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE028 — SELF_MATCH_ONLY: The exact indexed wording was the record itself, but general prior theory already implies it.

## Disposition

FAILED
