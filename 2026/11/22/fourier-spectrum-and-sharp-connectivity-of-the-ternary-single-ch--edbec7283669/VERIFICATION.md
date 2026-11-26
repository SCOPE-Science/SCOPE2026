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

One-hot words are vertices of the ambient product of simplices. The minimal coordinate face for two words only allows their two symbols at each differing coordinate. If there is no proper nonempty zero-sum set of switches, its intersection with the codeword polytope is their segment. Otherwise complementary switches give two other vertices with the same midpoint; an edge face cannot contain that midpoint without containing the other vertices. The minimal nonzero ternary difference multisets are (1,2),(1,1,1),(2,2,2). Thus the step counts are 2*C(n,2), 2*C(n,3) and squared distances 4,6. Translations preserve adjacency, pair steps generate the group, and halving the total number of incident edges yields the two multiplicities. As an alternate Fourier check, each inverse pair of generators contributes 3 to the Laplacian eigenvalue exactly when its character phase is nontrivial. Pair moves contribute for unlike labels; triple moves contribute exactly for triples having two equal character labels and one different (neither all equal nor all distinct). This gives 3*sum_{i<j} c_i*c_j*(1+(c_i+c_j-2)/2)=3F(c)/2, including zero counts by omitting that pair. Exponents modulo the all-ones direction give the stated multinomial generating polynomial with a factor 1/3 from the free shifts. With largest count n-t, F=nt(n-t)+(3t-2n)c1*c2 and t<=2n/3. For t>=2 this is at least the increasing cubic h(t) in the proof, and h(2)-n(n-1)=(n-2)(n-3)>0 for n>=4. Thus only one-defect counts minimize there, giving 2n characters. At n=3 the (1,1,1) characters add two to the six one-defect characters; at n=2 there are just two nontrivial characters. The normalized gap divides by d_n and is 9/(2(n+1)). The graph is complete at 2 and 3, and the zero-sum support-four word (1,1,2,2,0,...) is not a generator at any n>=4. An independent exact check of endpoint-switch faces and character sums through n=5 matched the full spectrum and the gaps/multiplicities (3,2),(9,8),(18,8),(30,10). The frozen exact and LP scripts were read but not run; the fresh finite check is bounded corroboration. Replay: RESULT.md Proof Steps 1–4 or enumerate all shifts and inverse step pairs with the above integer phase test.

## originality

PASS

The same ternary polytope and its facets are prior; standard minimal-switch adjacency and Cayley Fourier diagonalization are not credited as new methods. The supported distinct result is the exact ternary edge census and the complete spectral law and sharp gap with multiplicity of the one-hot one-skeleton. The closest indexed exact graph calculation uses a different group and a different phase count.

## value

PASS

The one-skeleton of a standard ternary SPC polytope is a natural graph family. Identifying its actual edges and the complete unweighted Laplacian spectrum supplies structure not conveyed by a facet count. The sharp spectral gap and its eigenspace multiplicity are exact dimension-dependent connectivity data, with a genuine boundary at lengths two and three; this is not a small test-instance result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
