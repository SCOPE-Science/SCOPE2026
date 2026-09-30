# Independent Audit — 2026/09/13/045

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `f647e4901d3c5e3739a97ba700abe924a9c456a0`
- Disposition: **FAILED**

## Correctness

**PASS** — The algebraic identities and the c=-5 portrait withstand independent checks. Eliminating the two critical roots of c z^2+2z-c^2 gives exactly v1+v2=-4/c^2 and v1 v2=-4/c; for odd c this forces both critical values to have 2-adic valuation 1. At c=-5 the fixed multipliers stated in the record are correct, the genuine period-2 factor z^2+z+1 has multiplier 19/31, and the exact period-3 factor/resultant computation supports the listed Newton valuations. The Hensel computation for sqrt(-31) and the exact invariance v(G(z))=v(z) for negative valuations support the two distinct stable critical-tail valuations. The record appropriately stops at non-absorption for periods <=3 and does not infer a wandering component.

## Originality

**PASS** — The exact critical-value symmetric identities and the fully certified c=-5 low-period portrait are specific computations not supplied by the cited general p-adic-dynamics papers. They are more than a direct invocation of a general theorem, and the record provides exact resultants and valuation certificates for the chosen parameter.

## Scientific value

**FAIL** — The result remains a low-period obstruction for one stress-test parameter. It proves neither side of the admitted wandering dichotomy, excludes attraction only through period 3, and leaves higher-period attractors and wandering status completely open. The exact computations are technically careful but do not yet change the scientific status of the motivating problem enough to justify a validated research finding.

## Sources

- Wild recurrent critical points (Juan Rivera-Letelier): https://arxiv.org/abs/math/0406417 — General residue-characteristic background; does not contain the c=-5 portrait.
- Equations at infinity for critical-orbit-relation families (Rohini Ramadas; Rob Silversmith): https://arxiv.org/abs/2008.10095 — Related critical-orbit-relation framework, not a source for the exact 2-adic calculations audited here.

## Limitations

- The audit did not attempt to classify cycles of period >=4 for c=-5.
- No claim is made that the absence of an indexed exact prior source alone proves originality; the originality assessment rests on the specific new elimination/resultant computation relative to the general cited theory.

GitHub was read only as evidence. Open-access/preprint sources were checked first; no Oxford Download was needed in this run.
