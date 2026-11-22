---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

At rho=10 the coexistence Jacobian J=[[-5,-1],[5,0]] has distinct negative real eigenvalues (-5±sqrt5)/2. The smooth perturbation admits uniform-in-time z=A z1+O(A²) by a Hurwitz Duhamel/bootstrap estimate valid for bounded input. Frozen impulse primitive I(t) reaches prey drop 0.07623851566 A<0.09 A; exact sqrt5 sinusoid u1(t)=[sin(sqrt5 t)-e^(-mu1 t)+e^(-mu2 t)]/10 takes value -0.10336010535 at t=2, below moving N_a=1-0.09A. The low/high uniform convolution estimates stay below threshold with O(A²) margin, while P=5+O(A)>1 throughout. Once crossing into N<N_a<1, prey decays, followed by predator. The gain squared w²/[4(w^4+15w²+25)] has unique maximum at sqrt5. Direct independent SymPy rational/symbolic checks corroborated eigenvalues and gain and explicit time value; proof handles the all-small-A quantifier. Filippov result is existence only, not uniqueness at grazing.

## originality

PASS

Qualified best-of-knowledge: earlier Gao et al introduce frequency-induced tipping and focus examples; the inspected prior Resultary frozen-safe extinction proof explicitly assumes a complex stable focus q>0, and the joint accessibility theorem is about a smooth periodic orbit, not admissible switched extinction. The strictly real-node example exhibiting all-frozen-safe and two-frequency-safe versus middle-frequency extinction from one seed adds a distinct nonoscillatory boundary case. Full Gao primary appendix could not be obtained through OA or authorized institutional connection; this remains a named risk and does not alone defeat the specific non-coverage comparison.

## value

PASS

Motivated counterexample to interpreting frequency-induced tipping as requiring an oscillatory linear eigenpair: distinct real-negative node eigenvalues still yield narrow-band forcing extinction while all comparable frozen rates and both extreme frequencies are safe. The exact moving threshold and transfer peak furnish a reusable spectral-versus-nonlinear-boundary distinction; not just a generic gain calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
