---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For all gamma>0,kappa>=0,r>0 with x=r/gamma and b=1+4kappa/gamma>=1, the product local Lindblad evolution of |Phi+> gives q_t=(e^-gamma t-e^-2gamma t)/2, w_t=e^-2gamma t/2, c_t=e^-(gamma+4kappa)t/2. A Poisson-age Laplace integral yields q=x/[2(x+1)(x+2)], w=x/[2(x+2)], c=x/[2(x+b)], unique because every positive-rate reset eliminates initial-history dependence. The diagonal Pauli correlators (u,-u,v), u=x/(x+b), v=(x²+x+2)/((x+1)(x+2)), give exact Smax=2sqrt(u²+max(u²,v²)) via Horodecki. Analytically, 2u²>1 iff x>(1+sqrt2)b, and u²+v²>1 iff P_b(x)>0 using the exact rational identity 1-u²-v²=-xP_b(x)/[(x+b)²(x+1)²(x+2)²]. For b>=1 P_b has coefficient signs (+,+,-,-,-,-); it is negative at zero and positive at infinity, hence by Descartes has one simple positive root xi_b and a single strict positive crossing. The derivative v'=2(x²-2)/[(x+1)²(x+2)²] is positive above sqrt2, giving unique witness crossover b_c=z0/(1+sqrt2), z0=3.204257578... . Rescaling x=b^(2/3)y and P_b/b^(10/3)->y^5-4y² establishes xi_b~4^(1/3)b^(2/3), hence the stated physical threshold. X-state Wootters formula gives concurrence 2[c-q]_+ = x[x²+2x+2-b]_+/[(x+b)(x+1)(x+2)], with onset sqrt(b-1)-1 for b>2. The strict CHSH-vs-concurrence gap follows from the at-onset u=2q, v=1-2u and the positivity bounds. A fresh, independently written 16x16 Lindblad solver, Pauli-observable diagonalization and exact SymPy identities passed 285 assertion groups over 75 physical parameter combinations plus branch cases, independent of repository checker.py. Universal claims rest on the reconstructed analytic argument, not the finite tests.

## originality

PASS

Qualified best-of-knowledge pass after rechecking real published Resultary findings and primary sources. Continuous-time Poisson resetting of open Lindblad states (Carollo et al.) and optimal two-qubit CHSH under local decoherence (Kofman-Korotkov, Horodecki) are established prior results and explicitly not novel. Kofman-Korotkov already exhibits competing witness branches under unreset local noise. However, in read original works and two nearest full Resultary findings, no earlier result states or directly implies without a fresh model-specific calculation the full stationary r/gamma vs dephasing b classification with a uniquely crossing quintic, switched rate-controlling CHSH mechanisms, and 2/3 strong-dephasing threshold. The 2026 Bell-reset experiment concerns discrete-time unitary Ising and product depolarization, not independent continuous Lindblad damping/dephasing. Inaccessible literature alone did not determine the verdict. This is not an assertion of worldwide novelty or certification.

## value

PASS

The exact rate required to maintain unfiltered Bell-nonlocal quantum correlations in a Bell source experiencing realistic independent local amplitude loss and pure phase dephasing is a natural motivated invariant of this simple open-qubit system. The global continuous-parameter classification, a sharp competition between longitudinal and transverse optimized CHSH witnesses, and the nontrivial fractional-power dephasing tradeoff distinguish CHSH from concurrence (b^(2/3) vs b^(1/2)). This is more than tabulating a few simulations or simply substituting two numbers into a textbook criterion: the positive-root uniqueness and asymptotic crossover require model-specific analysis. No claim is made of universal experimental performance or a broader arbitrary-channel theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
