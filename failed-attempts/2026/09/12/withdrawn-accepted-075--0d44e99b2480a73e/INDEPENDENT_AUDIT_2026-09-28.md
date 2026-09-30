# Independent Audit — 2026/09/12/075

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c1af3c8b638ba4850d17aac5406c08e6a8048048`
- Disposition: **FAILED**

## Correctness

**FAIL** — The independently reconstructed normal-form data agree with the record: r_t=-1/[x(x-1)(x-2)] and the double-pole coefficients are 1/2-sqrt(2)/2, 3/4-sqrt(3)/2, 5/4-sqrt(5)/2, and 3/2. The Kovacic exclusions and the displayed Schlesinger-factor obstruction are internally coherent. However the headline PPV conclusion is inconsistent as written. 'Full SL2 over the dt-constants' would be the constant differential subgroup and would satisfy differential equations dt(g_ij)=0; that is incompatible with the simultaneous assertion that the defining dt-ideal is zero apart from det=1. The full non-isomonodromic group is instead SL2 over the parameter differential field (after the standard PPV constant-field/differential-closure setup), not SL2 over the dt-constant field. The record also writes the base simply as C(t,x) while invoking classification results whose PPV formulation uses an appropriate differentially closed dx-constant field. The final group statement therefore cannot be accepted literally.

## Originality

**FAIL** — Arreche's PPV algorithms are explicitly designed to compute the parameterized differential Galois group of one-parameter second-order rational differential equations and to distinguish full differential SL2 from the constant/isomonodromic case. The record applies that standard pipeline, plus Kovacic's ordinary algorithm, to one deliberately generic radical Heun specialization. It does not establish a new Heun-family classification, a new PPV-group phenomenon, or a new algorithm beyond the existing theory.

## Scientific value

**FAIL** — As a worked symbolic example the computation is reproducible, but a single arbitrary specialization is scientifically narrow and the central PPV field-of-constants statement is misstated. Correcting the terminology would leave a routine application of established algorithms rather than a result with substantial independent value.

## Sources

- Computing the differential Galois group of a one-parameter family of second order linear differential equations (Carlos E. Arreche): https://arxiv.org/abs/1208.2226 — Develops PPV algorithms for one-parameter second-order equations and differential equations defining their parameterized Galois groups.
- On the computation of the parameterized differential Galois group for a second-order linear differential equation with differential parameters (Carlos E. Arreche): https://doi.org/10.1016/j.jsc.2015.11.006 — Published algorithmic treatment of parameterized differential Galois groups for second-order equations.

## Limitations

- This audit does not allege that the record's displayed Kovacic or Schlesinger algebra is numerically wrong; the decisive correctness failure is the incompatible final PPV group description.
- A corrected statement would need to specify the PPV base/constant differential field precisely and distinguish dx-constants from dt-constants.

GitHub was read only as evidence. No GitHub mutation, dispatcher completion call, or separate publication/report action was performed by this audit chat.
