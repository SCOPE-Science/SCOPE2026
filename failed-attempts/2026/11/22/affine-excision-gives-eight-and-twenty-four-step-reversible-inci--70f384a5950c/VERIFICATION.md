---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For even s, the incidence Gram matrices are J_(s^2) and (J_(s+1)+I) tensor J_s, of ranks 1 and s. The even column sum kills J_(s^2)B, giving A^3=0. Thus ranks 2rho and s+1 of A and A^2 give exactly the three zero-primary multiplicities. For odd s the Gram matrix on points is I+J and its sole kernel direction is not killed by B^T, so rho=s^2. The zero-sum point space paired by B^T with its image gives s^2-1 copies of J_2(1). A concrete length-three zero chain starts at the indicator of one parallel class of lines, maps to the all-ones point vector, then to the all-ones line vector, then to zero. The line kernel of B has dimension s; after its all-ones direction in that chain, the remaining s-1 directions are singletons. This independently accounts for the full adjacency dimension. A zero Jordan block of length j gives one wave block of length 2j because the wave block has characteristic polynomial (X+1)^(2j) and one fixed direction. For J_2(1), h(T)=(I+diag(A,A))T, h=X^2+X+1, has square zero and rank two, including after scalar extension; it gives h^2. The gcd with X^t-1 gives the displayed time census, cyclic generators attain the maximum period in each required primary part, and Möbius inversion gives orbit counts. One fixed wave state satisfies u=v and Au=0, proving rank recovery without any assumption of Desarguesian coordinates. Replay using RESULT.md Steps 1–5. Inspected the scripts and four saved examples, not running the scripts; the examples agree with the formulas and the adjacency script shares construction/elimination code with the wave script. No experimental universality is inferred.

## originality

FAIL

There is demonstrable broader coverage by the distinct indexed Resultary record 914535ff5fe5 on finite partial geometries. It concerns the same update, labeling and extension fields, includes every affine plane with no further hypothesis, and gives the exact orders and the same all-iterate and primitive-orbit formula through adjacency kernels. The affine formulas are its direct specialization using the incidence Gram matrices. This is a finding of equivalent mathematical coverage, not an inference of chronological priority or copying from the shared publication date.

## value

FAIL

A sharp rank-sensitive census would be valuable if uncovered. Relative to the already indexed general classification, however, the remaining contribution is a pedagogically useful direct kernel evaluation with elementary incidence identities and parity substitution. The record does not classify the unknown even binary ranks or provide a distinct new excision theorem beyond juxtaposing the already covered affine and projective orders. No substantive surviving claim in the frozen record warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
