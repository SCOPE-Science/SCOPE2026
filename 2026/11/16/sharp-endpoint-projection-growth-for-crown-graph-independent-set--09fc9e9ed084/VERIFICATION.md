---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

An independent subset of the crown graph is a subset of one shore or the two matched vertices at one index, giving W(u,v)=N1_(u=0)+N1_(v=0)+n-1-2|u+v|. Odd n zeros are u,v !=0 with |u+v|=(n-1)/2, each shell vector has N-2 allowed ordered choices, while even n has no zero. The exact zero-shell Fourier inverse produces Krawtchouk kernel q(x,y), and averaging ANY projection over translations yields the unique Fourier-diagonal range projector of no larger l1/linfty norm, hence sharpness. Splitting kernel mass at origin/diagonal/off-diagonal gives Lambda_n=1+[D+(N-4)L-2(N-2)B]/N²; Krawtchouk generating function yields L=2^((n+1)/2)B; Jensen/triangle show Theta growth. Independent integer Walsh and inverse-kernel computations check n=3,5: 18/300 zero frequencies and norms 49/16,733/128.

## originality

PASS

No matched published SCOPE or primary reference gives this crown-graph signed independent-set Walsh shell and sharp minimum endpoint range projection. Published clique-corona formulas and crown independent-set counts involve other graphs or unsigned counts; neither imply this exact Krawtchouk absolute-norm expression.

## value

PASS

The parity contrast between an invertible Boolean convolution and a growing projection norm even as odd-size nullity fraction vanishes is mathematically motivated and relevant for Fourier recovery and finite combinatorial harmonic analysis. All-length sharp growth is a nontrivial structural consequence, not just a small-graph enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
