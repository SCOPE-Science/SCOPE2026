---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS for exactly p in {5,7,11,13}. Cyclotomic minimal-polynomial divisibility shows F_A(u)=0 exactly when 0 and ±u_k cover Fp once, giving D_p all signed permutations of 1..d and |D_p|=2^d d!. After translating B and signed-coordinate normalization u=(1,..,d), every p-element spectrum gives a (p−2)-clique of V_p={v∈D_p:v−u∈D_p}. An independently written exact NetworkX maximal-clique enumeration, using a different implementation from checker.py, confirms profiles p=5 {3:1}, p=7 {5:1}, p=11 {2:120,9:1}, p=13 {1:24,2:324,3:225,5:42,11:1}. The numbers of graph vertices are respectively 3,5,69,319 and edges 3,10,156,926. Each has a UNIQUE clique of order p−2, the radial one. Consequently every full B is an affine line; |D_p|p^(d−1)/(p−1) yields 10,392,5622144,1425765120 distinct spectra. Independent modular checks confirm the stated p=13 noncollinear four-character witness. These are exhaustive FINITE checks, not proof for p>13; the analytic reduction establishes their exact relevance to the claimed four primes.

## originality

FAIL

FAIL due to a decisive earlier general theorem: Kim–Hirasaka–Mizoguchi (2014), Theorem 1.1, shows every BH(p,p) for prime p≤17 is equivalent to Fp. A spectral Lee-cross pair produces exactly such a BH(p,p); dephasing a Fourier-equivalent exponent matrix and using the sites e_k forces B to be an affine line. The source spectral counts are then the elementary signed-permutation/orbit formula. Egan–Flannery–Ó Catháin (2015) explicitly cites the theorem as Proposition 5.4. No match of wording or published Lee-cross count table is needed: the prior implication completely covers the central claim. The secondary p=13 noncollinear partial witness is independently valid, but it cannot make an already-covered full-spectrum claim original.

## value

FAIL

FAIL for the submitted principal result because its all-spectrum rigidity and complete four-prime numerical census are immediate specializations of the pre-existing universal small-degree BH classification, with only elementary dephasing and orbit counting. The Lee cross and its spectra are natural geometric/Fourier objects, and the exact numbers can be useful as examples, but this contribution establishes no distinct unknown natural invariant or structural boundary beyond the known matrix theorem. The p=13 four-character noncollinear partial witness is a correct local illustration, not a motivated exact partial-family classification or a substantive independent theorem. Independent exact computation and a working checker do not alone establish mathematical value, and the principal claimed discovery is a known corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
