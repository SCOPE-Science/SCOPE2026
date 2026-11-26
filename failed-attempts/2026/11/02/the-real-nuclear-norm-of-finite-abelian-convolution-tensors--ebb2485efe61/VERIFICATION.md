---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For counting-measure Euclidean spaces the unitary Fourier transform turns convolution into coordinatewise multiplication scaled by √n. The real locus groups conjugate characters; there are r real characters because |Hom(G,{±1})|=|G/2G|=|G[2]|. The orthonormal coordinate of a conjugate pair is √2 times a single Fourier coefficient. Thus each real coordinate contributes a scalar tensor scaled by √n and each pair a real complex-multiplication tensor scaled by √(n/2). The latter has projective norm 4: four unit-cost signed coordinate terms give the upper bound, and its real injective norm 1 and squared coefficient norm 4 give a matching dual bound. Orthogonally supported blocks across the factors add in projective norm: the sum of unit block witnesses has injective norm at most one by Cauchy–Schwarz and the bound on the largest block length of a unit vector. This gives r√n+4((n−r)/2)√(n/2). Over C, Fourier gives n unit pure terms scaled by √n, with the output index inverted if using the bilinear coefficient pairing. The injective bound √n and squared coefficient norm n² give the same lower bound n^(3/2). The trivial group, exponent-two groups, and the two order-four examples all agree with the formulas.

## originality

FAIL

The real abelian formula was not found verbatim. Derksen's proof, however, already decomposes the identical multiplication tensor by the orthogonal group-algebra factors, with the counting-measure Hilbert normalization. In the abelian case, taking the conjugation-fixed part groups the known character blocks in real singletons and conjugate pairs, with a √2 change of length. The resulting real multiplication norms are the scalar norm and Dai–Lim's explicit norm 4. Orthogonal additivity is an immediate norm identity (one Cauchy–Schwarz bound on the supports). Together these already determine the formula and the equality criterion by direct substitution, not a separate norm calculation or obstruction. Prochno alone does not imply the real projective norm merely by knowing the injective norm.

## value

FAIL

A real-versus-complex comparison on natural convolution tensors is well motivated. Here the exact gap, equality condition and order-four comparison are mechanical consequences of the already available block calculation and local norms. The record does not establish a separate difficult threshold, a new type of block, or a new application of the exact value beyond reading off the proportion of real characters. The explicit formula is a useful exposition of that consequence, not a distinct scientific result at the required bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
