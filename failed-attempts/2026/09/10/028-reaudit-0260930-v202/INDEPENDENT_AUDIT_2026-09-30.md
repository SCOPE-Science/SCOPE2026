# Independent scientific audit — SCOPE-20260910-028

Audited: 2026-09-30 UTC

Disposition: **failed**

## Correctness

**PASS** — Fresh rational-interval recomputation of all 400 panels reproduces min H>=0.154805591681, J1 in [2.4357131762,2.4360736905], J2 in [0.06535452556,0.06541913570], area in [1530.403724,1530.630242], and Hawking mass in [1.005683582,1.010214681]. These imply the stated outer-untrapped and [0.96,1.06] mass claims. Huisken-Ilmanen states the outermost-minimal-surface area bound |N|<=16 pi m^2, supporting the existence-conditional ADM area cap.

## Originality

**PASS** — No prior exact finite-radius interval for this specific Brill-Lindquist mass/separation/radius cell was located; the primary Penrose source supplies only the general area inequality.

## Value

**FAIL** — The scientifically new portion is a single coordinate sphere at r=10 for one chosen mass ratio and separation. The radius is not shown to be a natural threshold, extremizer, first/last admissible radius, classification boundary, or invariant required by a downstream theorem; the broad [0.96,1.06] mass target and positivity check are routine asymptotic computations. Correctness and reproducibility do not supply the missing mathematical motivation for this precise slice.

## Sources and residual risk

- https://www.emis.de/journals/NYJM/JDG/2001/59-3-1nf.htm — Primary-paper abstract stating the outermost minimal-surface bound by ADM mass. Assessment: Covers the area-cap theorem, not the local r=10 interval.

Residual risks:
- A numerical-relativity table with this exact cell could be poorly indexed.

The detailed machine-readable audit is in `INDEPENDENT_AUDIT_2026-09-30.json`.
