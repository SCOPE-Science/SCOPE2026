# Independent Audit — 2026/09/11/050

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `3eb6310b26ff526dc8fbee6eb9778fe54893567a`
- Disposition: **FAILED**

## Correctness

**PASS** — The literal finite calculations check out: on the six-point blow-up the stated class L=H-E31 has L·(D1,D2,D3)=(1,1,0), L^2=0 and -K·L=2; the explicit line through p31 and a general interior point is unique and its strict transform has the claimed contacts. At curve class zero, a theta function has its leading monomial, and in the chosen chamber the unique straight+straight pair gives coefficient 1. Thus the two separately defined numbers in the record are indeed both 1. This does not, however, turn the equality into the standard theta/log-GW structure-constant correspondence, because the theta coefficient being extracted is explicitly the curve-class-0 coefficient while N_L is a positive curve-class L invariant.

## Originality

**FAIL** — The two ingredients are standard leading-order facts rather than a new enumerative identity. The coefficient of the leading theta monomial at class zero is the undeformed/tropical product coefficient; the record itself excludes every bent broken line because bending carries positive curve class. The second number is the elementary count of the unique projective line through a fixed blown-up boundary point and a general interior point. General theta/log-GW literature relates matched structure constants and curve classes; it does not make a cross-degree numerical coincidence between a class-zero coefficient and a positive-class line count into a new correspondence. An exact-source search did not locate this packaged equality, but absence of an exact package is not enough to make these standard ingredients original.

## Scientific value

**FAIL** — The result supplies a useful sanity check for conventions, but the headline equality 1=1 has no demonstrated geometric mechanism linking the two sides at the same Novikov degree and does not determine a nontrivial scattering coefficient, higher-order wall, or new log invariant. As a research finding it is therefore too weak: it combines a universal leading theta coefficient with an elementary rigid-line count rather than resolving a substantive enumerative question.

## Limitations

- The correctness pass is for the literal two numerical statements; it is not an endorsement of the claimed novelty of their equality.
- No higher-order coefficient or positive-class theta structure constant was audited or established here.
- The log contribution +1 uses the usual transverse rigid-map argument; the explicit incidence calculation was independently checked.

## Sources

- Mirror symmetry for log Calabi–Yau surfaces I — Mark Gross; Paul Hacking; Sean Keel: https://arxiv.org/abs/1106.4977 — General theta algebra for Looijenga pairs and the curve-class-graded structure constants.
- Intrinsic mirror symmetry and punctured Gromov-Witten invariants — Mark Gross; Bernd Siebert: https://arxiv.org/abs/1609.00624 — General construction of mirror multiplication from curve-counting/scattering data.
- Theta functions, broken lines and 2-marked log Gromov-Witten invariants — Tim Graefnitz: https://arxiv.org/abs/2204.12257 — A genuine two-marked theta/log-GW correspondence in a different boundary setting; useful for distinguishing matched structure constants from the record's cross-degree equality.

GitHub was read only as evidence. The record's pre-existing `AUDIT.json` was inspected only after an independent assessment and was not treated as authority. No repository mutation was performed by this audit chat.
