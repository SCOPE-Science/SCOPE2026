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

For h=3,4 and n>=3, the three consecutive h-bit column transition condition L_h(a,b,c) is exactly the B3/S23 fixedness equation for the middle column; periodic closed walks of T_h therefore count all labelled fixed states, even at the smallest n=3. The actual height-four 256-state graph has 499 transitions and exactly one cyclic SCC of 127 vertices/309 edges; self-loop and strong connectivity make its adjacency B primitive. Exact symbolic 127-degree determinant plus rational positive vector v=B^4001 gives Collatz–Wielandt 2.55371542<λ<2.55371544<13/5. The height-three graph contains a 27-state cyclic component of exact characteristic polynomial x^24(x^3-27), giving F3(n)>=3^(n+1) at 3|n. Trace bound F4(n)<=127 λ^n, and integer 127*13^27<3*15^27 handles n>=27. Exact F4 for multiples n=3,6,...,24 are 39,651,5907,99107,1517719,24500451,391780043,6355667155, each below 3^(n+1). Independent local transfer construction reproduced 64-state/256-state graph edges 156/499 and traces F4(3)=39,F4(4)=53,F4(6)=651,F3(3)=127,F3(6)=2595. This is an all-n finite-spectral proof, not extrapolation.

## originality

PASS

The classical cylindrical-automata trace technique and height-three modular resonance are prior, and the finite 4×4=53 value appears in 2018 discussions. None of the inspected statements gives the particular height-four 127-state cyclic component, its certified Perron bound or the every-3-multiple F4<F3 inequality. Such comparisons require the additional height-four analysis.

## value

PASS

The result resolves a natural monotonicity misconception for synchronous Life fixed points under increasing periodic-torus height by an exact infinite family of strict counterexamples, with a sharp arithmetic resonance and certified entropy disparity rather than a tiny isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
