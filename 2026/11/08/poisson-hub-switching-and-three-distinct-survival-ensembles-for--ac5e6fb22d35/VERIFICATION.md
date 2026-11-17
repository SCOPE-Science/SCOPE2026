---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Exact strong lumping of all injective labelled configurations yields killed generator [[-k,k],[r,-k]], with r=(n-k)/(n-1). Its eigenvalues -k +/- sqrt(kr) yield the two survival expressions. Positive eigenfunction h(A)=sqrt(k), h(B)=sqrt(r) defines the long-horizon Q-process whose hub switches occur at equal rate sqrt(kr), hence Poisson counts. Terminal survival probability of B is sqrt(k)/(sqrt(k)+sqrt(r)), and exclusion stationary probability k/(k+r); all three are strictly ordered for 2<=k<n. Independent direct enumeration of labelled states reconstructed killed and safe rows, including dense k=n-1 boundary; 79,396 separate row assertions overall, not an infinite proof.

## originality

PASS

PASS: Classical Darroch-Seneta quasistationarity and the general Shiatis exponential martingale/Doob relation do not supply the exact star-specific eigenpair, symmetric Poisson hub-switching and three explicit distinct hub occupancy ensembles. The published October 26 graph-wide equality classification shows when exclusion and noncollision coincide, but does not determine the star conditional occupation rates. These full statements were compared by implication rather than headings. Risk remains that another unindexed star example solves the same two-class chain.

## value

PASS

PASS: The star is a natural singular bottleneck for exclusion and collision processes; exact comparison of never-collide conditioning, terminal-time survival conditioning and suppression of collisions resolves genuinely different probability laws in the same network. The Poisson rate and universal 1/2 occupancy versus unequal exclusion rates provide direct process-level observables for all k,n, not merely a routine matrix entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
