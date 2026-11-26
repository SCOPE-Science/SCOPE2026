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

For n>=2a the integer triangular sum packet T of support length L=2a-1 embeds without folding. The sum distribution of the two length-a blocks is T+2*T_s+T_2s (ordered pairs). Parseval contributes the factor 1/n; squares of the three packets give 6||T||^2=4a^3+2a and the cross terms are 8C_n(s)+2C_n(2s). They vanish exactly for disjoint support packets, with successive gaps s,s,n-2s after reflection, giving the threshold and all equality separations. The linear C(h) strictly decreases through h=L: expand each packet as nested centred interval indicators; pairwise overlaps are nonincreasing, and the full-length interval with itself decreases at every step. In the stated window t<=a<L we have n>2L, and 2s>=2a>L, so only C(s) and C(n-2s) contribute. For s>L the second strictly grows from its value at L. Below L-floor(t/2) the second is zero; stepping to that endpoint can cost at most 2 (odd t) but saves at least 8 on the first term. Each relevant tail overlap of length v<=a contributes sum_{j=0}^{v-1}(j+1)(v-j)=B(v). For the objective F(u)=8B(u)+2B(t-2u), the forward difference 4(u+1)(u+2)-2(t-2u)^2 strictly increases on integers through the admissible edges. For t>=2 its smaller root lies in [0,floor(t/2)), by the endpoint signs when extending the polynomial to floor(t/2); the ceiling rule and adjacent tie follow. Integrality is equivalent to the odd square 2(t+3)^2-1. For the negative Pell equation x^2-2y^2=-1, any positive solution with y>=3 is reduced to a smaller positive solution by multiplication by 3-2sqrt(2) (4/3<x/y<3/2 and x>y); y=2 is impossible and y=1 is the base solution. This gives exactly the stated odd powers after restricting t>=2. Expanding the root gives u=(1-1/sqrt(2))*t+O(1); evaluating the cubic terms yields 1-2sqrt(2)/3. Independent replay python3 -B /workspace/reproductions/1.py uses squared difference autocorrelation by cyclic bit rotations, checking 1197 width/period cases, all ties through t=10000 against exact integer forward differences, and full shift tests for the Pell ties through t=1000. The optimizer theorem below threshold remains restricted to t<=a.

## originality

PASS

The ordinary Fourier identities and run-based autocorrelation evaluation are prior. The relevant new result is the exact cyclic optimization including the optimizer window and its arithmetic two-optimum classification, not evaluation of the fourth moment by itself. The strongest inspected matches concern continuous two-interval data or autocorrelation evaluation; neither states or immediately solves the cyclic integer optimizer problem. This is a bounded scientific judgment with an unresolved nearby four-tone hit.

## value

PASS

For equal two-block apertures the Fourier fourth moment changes with their discrete separation. The exact first modulus permitting noninteracting sum packets gives a design cutoff; below it the theorem explains how much penalty is unavoidable and when two inequivalent placements tie instead of one. The infinite negative Pell sequence and complete near-threshold minimizer rule are substantial beyond autocorrelation evaluation or a handful of optimized examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
