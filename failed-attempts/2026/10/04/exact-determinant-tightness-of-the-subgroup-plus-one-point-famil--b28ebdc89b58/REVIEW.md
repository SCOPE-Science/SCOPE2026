# Independent mathematical audit

## correctness

FAIL

The basis-by-basis determinant derivation is correct, but the final set-level invariant uses the wrong extremization. The cited primary definition is D(E)=inf over exponential bases of |det T(E,B)|, whereas the proof maximizes over k. Since every nonzero k occurs, the correct infimum is 2 m^(m/2) sin(pi/m), not the displayed maximum-chord formulas. For m=4 the spectrum has minimum 16 sqrt(2) and maximum 32, while the package claims 32 for D(E_4). The headline exact D(E_m) statement is therefore false.

## originality

PASS

Ferguson--Mayeli--Sothanaphan study exactly this subgroup-plus-one-point family and define determinant tightness, but no inspected source gives the full basis-by-basis chord-length determinant spectrum. Resultary found the audited determinant result and a later exact-Riesz-ratio companion, not an earlier determinant-spectrum theorem. The spectrum itself remains best-of-knowledge original even though the package applies the wrong extremization to obtain its set-level D(E_m).

## value

PASS

The correct per-basis determinant spectrum for this canonical family is a motivated quantitative refinement of the source's Riesz example. That independent value does not rescue the false final set-level extremization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
