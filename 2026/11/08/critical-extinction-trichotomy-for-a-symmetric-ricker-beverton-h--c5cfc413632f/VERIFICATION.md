---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

F_k(y,z)=(z e^-y/(1+kz),y e^-z/(1+ky)) maps each coordinate strictly below the opposite input, so both even subsequences decrease to zero. Taylor expansion of F_k^2 gives x_next=x(1-2kx-2t+O((x+t)^2)) and t_next=t(1-2x-2kt+O((x+t)^2)), whence S=x+t=Theta(1/m) and sum S diverges while sum S² converges. Exact L_next=-L-[phi_k(y)-phi_k(z)], phi_k(u)=u-log(1+ku), and order-reversal give increment of |L| equal phi_k(max)-phi_k(min). For k>1 sign eventually negative and ratio ->1, giving n y,n z ->1/(k+1). For k=1 the ratio tends positive finite and diagonal iff equal starts, producing complementary alternating profiles. For k<1 off-diagonal ratio separates; the dominant two-step component ~1/(2km), minority has exponent m^-1/k and a strictly positive constant by summability of logarithmic remainder. Independent code verified the exact ratio identity and regimes up to n=150000: k=.6 dominant n*y=1.66411 vs 1/k=1.66667, k=1 n(y+z)=.999974, k=1.5 n(y+z)=.797897 vs 2/(k+1)=.8; full k>1 ratio convergence is slower than these samples, consistent with asymptotic proof.

## originality

PASS

The exact source Ouyang–Zhang–Chen (2023) covers the same Ricker–Beverton–Holt map and proves global extinction when ab<=1, but indexed published statements do not provide critical a=b=1, p=q=k, two-step normalized n^-1 parity composition and the minority n^-1/k amplitude. Resultary searches identified other symmetric Ricker competition and cyclic ecological models with different update formulae; no equivalent trichotomy was found. OA article is published under CC, but fetching its publisher full text failed, leaving a substantial qualified originality risk.

## value

PASS

At the neutral ab=1 linearization both +1 and -1 multipliers force nontrivial two-step normal form. The exact phase transition at k=1 between symmetric, memory-retaining and parity-selected extinction has a natural ecological interpretation and gives needed sharp normalized rates/positive minority constant, unlike a restatement of known unnormalized extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
