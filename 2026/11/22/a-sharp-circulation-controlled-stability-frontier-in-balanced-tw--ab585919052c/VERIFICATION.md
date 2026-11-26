---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At a positive homogeneous equilibrium the interactions cancel by row balance. Adding the two stage equations gives total density 2, and subtraction then gives zero contrast, so this equilibrium is uniquely (1,1) for every species. Differentiation and the orthogonal sum/contrast basis give blocks -2I, -G, G, -2ΔI; a Schur determinant and polynomial extension give the stated quadratic for each eigenvalue of G with multiplicity, including defective G. For s=1+Δ and q=(Δ-1)^2-z^2, the real part of the square root with nonnegative real part is less than s exactly when Re(q)+(Im(q))^2/(4s^2)<s^2. This gives the rational frontier; substitution of iω yields ω=-ab/s at equality. A strict violation gives a positive root real part. A contact does not by itself imply nonlinear stability or a bifurcation and does not exclude instability caused by another mode. The matched spectra are 0,0,±2g and 0,0,±2ig; the mixed circulant has 0,-2g,g(1±i), yielding the stated numbers and nonzero-frequency contact. The trace-zero/row-zero argument proves the size minimum for that contact; solving the two- and three-species symmetric balance equations proves the comparison minimum. The explicitly specified G_mix is a four-vertex directed circulant with additional arcs, not a graph whose only arcs form a simple directed four-cycle; the witness and minimum are for the stated matrix class, not bare four-cycle support. Read the frozen verification note and checker as evidence without executing the checker.

## originality

PASS

Prior stage-structured Jacobians, aggregate cancellation, the Schur reduction, and the reciprocal stability mechanism are not new here. The surviving claim is a finite-demography all-spectrum criterion in this complementary, deterministic stage model, with size-sharp matched-network and nonzero-frequency tests. The closest accessible records do not cover that combination. This is a best-of-knowledge result, not a priority certification.

## value

PASS

Zero on every species-pair aggregate can suggest no community-level effect, yet at the same edge magnitudes and demographic rates the construction changes the stability verdict. The exact threshold quantifies when maturation compensates circulation, distinguishes stationary from nonzero-frequency contacts, and shows the smallest balanced networks needed for each comparison. This is a local structural baseline, neither a nonlinear Hopf theorem nor an empirical stability prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
