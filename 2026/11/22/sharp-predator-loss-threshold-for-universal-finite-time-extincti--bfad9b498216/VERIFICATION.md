---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For q=s^(1-r), the pre-hit equations give q'=-a q-cp with c=(1-r)d and 0<a<=beta. The biomass s+(d/e)p is nonincreasing; consequently neither variable blows up and the Allee term alone forces uniform exponential decrease of s while positive. A finite maximal pre-hit solution must tend to s=0, since p stays positive on any finite interval and otherwise the smooth interior solution extends. On an infinite pre-hit trajectory the exponential bound makes s and s^r integrable, so the exact predator equation gives p(t)~C exp(-mu t), C>0. Because a-beta is O(s+p), the integrating factor has exp(integral a)~C' exp(beta t), C'>0. The cumulative forcing in the exact q identity diverges for mu<=beta, linearly at equality. For mu>beta and s<=delta sufficiently small, p(t)<=p0 exp(-lambda t) with lambda=mu-e delta^r>beta. Integrating q'>=-beta q-cp gives the strictly positive barrier when cp0<q0(lambda-beta). For any other fixed 0<s0<L, continuous dependence on the predator-free orbit up to a finite time with 0<s<delta brings a whole interval of positive seeds into the strict barrier. Conversely q'<=-cp and p>=p0 exp(-mu t) force a hit when cp0>mu q0. The earlier exponential estimates also give convergence of both species to zero for every infinite-lifetime orbit.

## originality

PASS

Finite-time extinction in related nonsmooth predator–prey systems and a persistent-predator criterion for this exact family are known. The supported distinct result is the endogenous mortality threshold, including equality, and existence of both hit-time behaviors for every fixed sub-Allee prey initial value above it.

## value

PASS

The exact loss-rate cutoff distinguishes finite-time extinction from mere asymptotic decay under endogenous predator dynamics, without an imposed persistence bound. The critical equality and the contrasting seed outcomes above it provide a useful qualitative classification even without a global seed separatrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
