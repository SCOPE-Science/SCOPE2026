---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: Each matching consists of disjoint row i<j and distinct columns a!=b; expanding sum over these gives S_i S_j-C_ij. Flipping one sign changes W by -2s_e times 2(n-1) disjoint signed edges, hence W remains all-positive 3n(n-1) modulo4. Hadamard 4-column balanced-sign block yields every row sum and pair inner-product sum zero; adding one arbitrary column covers n=0,1 mod4 (n>=4). Fourier diagonalization separates invertibility of counting convolution from noninvertibility of idempotent projection. Eight sign-column multiplicities give exact multinomial formula. Random independent column signs yield centered joint CLT of row sums; C_ij/n -> 0 in L2 and bounded EW²/n² ->3 ensure uniform integrability; diagonalized Q=U²-(V²+T²)/2 yields E|Q|=2/sqrt(3). Exhaustive independently assembled signs for n=2..5 verified zero counts 0,0,1160,7560 and congruence.

## originality

PASS

PASS, best-of-knowledge: targeted Resultary, relevant published research and primary mathematical comparisons did not show claim coverage; overlap and residual risks separately specified.

## value

PASS

PASS: The exact all-n singularity classification and sharp asymptotic amplification for the natural two-edge-matching frequency layer in K_{3,n} is a structural Fourier recovery boundary, distinct from the full matching generating function and distinct four/six-cycle orbits; precise fixed-layer invariant has motivated uses in diagonalization and projection norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
