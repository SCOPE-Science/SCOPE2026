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

On monomials T_g is a finite sum of Hilbert–Schmidt weighted shifts. Radial-segment Fubini and the polynomial antiderivative in g give the iterated kernel (g(z)−g(w))^(k−1)/(k−1)! without requiring injectivity. The constant input maps to g^k/k!, so subtracting R_k applies the kernel to f(tz)−f(0), whose Hardy norm is at most t||f||. On the unit circle, coefficient positivity gives |g(z)−g(tz)|≤G−a_1 t, and |zg′(tz)|≤D. Minkowski and extension of the nonnegative integral to t=G/a_1 give the remainder with integral G^(k+1)/[a_1² k(k+1)]. These estimates first hold on polynomials and extend by boundedness. In the Parseval integral for ||g^k||², equality in the triangle inequality occurs at exactly h points modulo 2pi. At each, the normalized squared modulus is |∑p_j exp(iju)|²=1−sigma²u²+O(u⁴); elsewhere on the compact circle it is bounded below its maximum by a fixed gap. Gaussian localization therefore gives h/(2 sqrt(pi sigma² k)) times G^(2k), with relative O_g(k^(−1)). Taking square roots and dividing the remainder by the rank-one norm gives O_g(k^(−3/4)). The second singular value is bounded by the rank-one approximation error; the singular ratio follows. In the binomial case h=m−1 and sigma²=(m−1)²a/(1+a)², so the degree spacing cancels. An independent exact calculation for g=z+z²/2 gives T_g²z=z³/6+5z⁴/24+z⁵/15 by both coefficient recursion and the power kernel, and checks the constant-vector identity for k=1,…,6 and the binomial variance cancellation.

## originality

PASS

The strongest inspected real-variable results give genuine high-power and rank-one analogues, Hardy mapping/quasi-nilpotency results cover related operators and symbols, and the exact shift-polynomial record already exhibits arithmetic/variance-driven circle maxima. None gives the weighted Hardy Volterra norm law and rank-one bound for the stated nonnegative polynomial class. The norm of g^k alone is a standard lattice/Laplace calculation; the supported distinction is its asymptotic control of the whole Volterra power and the stated operator-norm and singular-ratio estimates.

## value

PASS

The result converts qualitative rapid decay of analytic Volterra powers into an exact norm scale and describes which input functional controls the leading behavior. The arithmetic dependence comes from several boundary maxima rather than a single saddle, and combining it with a uniform error estimate gives information on the singular geometry beyond the scalar coefficient norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
