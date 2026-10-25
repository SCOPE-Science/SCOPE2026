---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Definitions and all boundary cases reconstructed from frozen RESULT.md. F(t)=2t−t log t has derivative log(e/t), F(1)=2. For a=max(0,x−r), b=min(1,x+r), ell=b−a, L=log(e/b), r<=ell<=2r for r<=1, and 0<=∫_a^b log(b/t)dt=ell+a log(a/b)<=ell, whence rL<=mu(B)<=4rL. b_R/b_r<=R/r yields mu(B_R)/mu(B_r)>=(R/r)/[4(1+log(R/r))]. Maximizing r^(1−lambda)log(e/r) for 0<=lambda<1 gives A_lambda=4e^(−lambda)/(1−lambda). Telescoping nested means with Holder yields sum S_{p,lambda}=Σ_{j>=0}(1+j log2)^(1/p)2^(−j(1−lambda)/p)<∞ for each fixed lambda<1, including p=1; top-scale mean controlled by mu(X)=2 and Lp. Minkowski proves the advertised norm inclusion. For lambda=0 target Morrey is Lp. Density>=1 and intervals have length>=r prove lower 1-regularity; mass comparison gives doubling<=8. At x=0, mu(B(0,r))/r=2−log r→∞, so upper 1-regularity and endpoint L_M^{p,1} membership of f=1 fail while f=1 has finite L_C norm. Finite test of 20000 independently generated (x,r,R) samples supports but does not prove mass bounds: minimum observed reverse-growth slack 3.49146 and maximum doubling ratio 2.85259; conclusions are analytic. No uniform lambda→1 bound is claimed.

## originality

FAIL

Scientific priority is defeated by the 2006 Nakai general equivalence theorem. The positive subcritical embedding is directly a specialization of its Corollary 2.3 after the exact parameter substitution phi(x,r)=r^(lambda/p)/mu(B(x,r))^(1/p); the submitted ball mass/reverse growth computations verify all the published hypotheses uniformly. The remaining lambda=0 and endpoint constant-function observations are elementary. Nakai did not explicitly publish this 2026 question or log-density example in the inspected theorem, but the audited claim is a mathematical consequence of the stronger prior result, so wording mismatch/newly phrased question cannot establish O. This is a scientific rejection, NOT a failure caused by inaccessible 2026 full text.

## value

PASS

The proposed boundary example addresses a natural mathematical question: whether all strict-subcritical Campanato-to-Morrey embeddings force upper critical volume regularity. A finite nonatomic, compact, connected, doubling, lower-1-regular weight exhibiting a logarithmic defect is mathematically motivated; the sharp critical endpoint and quantified failure are substantive even though the embedding follows from a prior general theorem. This is potential explanatory value, not a claim of independent novelty, and no paper-sized theorem is required. The precise positive range and endpoint failure make a coherent natural counterexample rather than an arbitrary slice or tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
