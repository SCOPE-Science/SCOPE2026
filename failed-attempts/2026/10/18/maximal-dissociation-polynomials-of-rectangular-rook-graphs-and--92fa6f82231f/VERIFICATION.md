---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 5–81. A selected edge uv in K_{m,n} has selected line-graph degree d(u)+d(v)−2. Feasibility therefore permits only K2 and two-edge stars as nontrivial components. If a singleton edge exists, an unused vertex on either shore would permit converting that singleton to a star. Conversely, with both shores occupied any omitted edge has two distinct selected neighbours. With no singleton, a new edge meeting a used vertex would add a neighbour to an already paired selected cell (or itself have two neighbours), so the only possible extension joins two unused vertices. This gives the two maximality cases. Each labelled singleton and oriented star contributes respectively xyz and either xy²z²/2 or x²yz²/2; the denominators are the interchangeable leaves. The star-only EGF is e^{y+T}+e^{x+T}−e^T by the union of two full-shore cases. Both shores full with at least one singleton contributes e^{A+T}−e^T. Unused-label factorials and star/singleton multiplicity factorials give the stated sum. Zero-sized boards contribute one. In the wide regime no configuration can occupy more than 2m columns; equality requires every row to contain two selected cells in distinct columns and thus no singleton. Hence the maximal configurations are exactly star-only ones covering all rows, with b=m−2c and n−2m+3c unused columns. All indicated c are feasible; the displayed coefficients and support follow, including the two-row example. The separate bounded check (python3 /workspace/review_checks.py 3) enumerated feasible selections and tested every possible one-cell extension on 27 boards, including the 21 nonempty reported boards and three empty cases, and made 60 additional algebraic wide-coefficient comparisons. The frozen code was inspected, not run. Its own 325-pair sweep checks nonempty positive-size species outputs and the one-row formula; it is not an independent wide-coefficient check for every one of those pairs. Neither finite computation replaces the proof.

## originality

FAIL

The distinct indexed record 3a4eb8e0ebb5 gives the same inclusion-maximal dissociation criterion and every coefficient of the same two-parameter labelled polynomial, including exactly the wide-board coefficients and parity gaps. The frozen exponential generating function is a direct resummation of these already specified coefficients; it provides no additional enumeration. This is demonstrated equivalent coverage, not a determination of historical priority or provenance. The comparator's displayed catalogue path is later than the frozen record's directory date.

## value

PASS

The complete labelled census is a useful structural invariant of a natural graph family. The necessary-and-sufficient side-occupation criterion converts an arbitrary maximality test into a precise packing classification. The wide-board family has unbounded size range but only even attainable sizes, and the polynomial distinguishes their exact multiplicities. This is more informative than a maximum size or an all-feasible-set census; the substantive mathematical value does not make the result distinct from the comparator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
