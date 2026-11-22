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

For hub bit zero, a fixed hub imposes at most floor(n/2) rim ones. Subdivision-site degree two and original rim-site degree three force y_i=x_i∨x_(i+1) and prohibit rim pattern 101. Conversely these conditions make all sites fixed, so each allowed cyclic word corresponds to one state; color complementation gives factor two. Mark a one-run boundary among r runs and count positive one compositions and zero runs of lengths at least two to derive exactly (n/r) binom(j-1,r-1)binom(n-j-r-1,r-1). The four-state de Bruijn transfer forbids 101 and has det(I-tT)=1-(1+z)t+zt^2-zt^3. Its simple Perron root at z=1 has weighted density μ≈0.411495<1/2, hence a z*>1 exponentially bounds the tail excluded by the hub constraint, giving the claimed asymptotic. Independent bitwise graph simulation n=3..7 gave 8,18,22,44,72; polynomial determinant verified by exact SymPy, not used to replace the proof.

## originality

PASS

The exact two-layer gear equilibrium bijection, labelled constrained-run sum and entropy base are not stated by the directly inspected older one-dimensional majority fixed-point paper, nor by published wheel/helm graph results whose adjacency conditions differ. There is historical-priority risk under Jahangir/Ising synonyms.

## value

PASS

Edge subdivision of a wheel changes majority fixed-point count from the known two wheel consensus states to exponentially many, despite the global hub half-density constraint. Exact enumeration, transfer entropy and the forced OR layer quantify a motivated structural change in an accepted graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
