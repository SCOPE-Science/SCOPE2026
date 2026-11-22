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

For q=2^m, r=q+1, graph-independent incidence vectors form the union of r coordinate subgroups H_i in H^r, each of size q with pairwise intersection {0}. Inclusion correction gives f=sum 1_{H_i}-(r-1)delta_0, hence unnormalized Walsh multiplier q(t-1), with t the number of zero frequency blocks. Therefore the omitted shell has exactly r(q-1)^{r-1} characters; the rank is q^r minus that count and the least nonzero singular value is q. Inverse Walsh of this shell is T(x)=(-1)^k(q-1)^{r-k-1}(r-qk), k nonzero coordinate blocks, including k=r after cancellation. The projection kernel delta_0-q^{-r}T has sharp l1 and linfty convolution norm equal to its absolute kernel sum; grouping x by k and evaluating the sign change at k=1 gives 1+[r(q-1)^{r-1}/q^r]*((q-2)2^{r-1}+2). For r=q+1, its leading growth is (q/e)2^q. I independently enumerated integer Walsh transforms and absolute kernels for m=1,2, obtaining ranks 5,619 and norms 7/4,7397/512. These finite checks corroborate, not prove, the all-m result; the character and binomial identities are the proof.

## originality

PASS

PASS best of knowledge: the independent-set polynomial and the q(t-1) identity follow from established subgroup enumeration and are not credited as new. Resultary contains related Hamming-shell restricted low-degree Fourier sampling and other endpoint Walsh projections, but their mathematical domains do not imply this full Fourier-complement projection norm. Main remaining risk is an equivalent Krawtchouk/Hamming-scheme l1-idempotent identity in classical literature.

## value

PASS

The first complete-multipartite resonance r=q+1 is the natural first parameter at which convolution becomes singular. Its range projection remains orthogonal in l2 but has an exactly calculated exponentially growing endpoint amplification even while each positive multiplier is at least q. That all-m exact operator invariant identifies a structural stability failure at a natural graph-theoretic threshold, not just a numerical special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
