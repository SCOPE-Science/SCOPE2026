# Independent audit — 2026-09-29

Record: `2026/09/16/009`  
Audited source tree: `a0d87fef2fc9d3782bcf9a6b2c2da777fa1c47a5`  
Disposition: **failed**

## Correctness

The record does not validate its central zero-density theorem. It applies the first-version Qi–Qiao short-interval large-sieve threshold T^(4/7), but arXiv:2608.29558v2 was posted on 2026-09-09—before this record's 2026-09-16 publication—and improves the effective interval to sqrt(T)<M<=T. Thus the record's claims that T^(4/7) is the smallest interval for the method and is 'sharp' were already stale. More importantly, the asserted hard-cutoff zero-density bound is supported only by a prose sketch: the required zero-detection/mollifier parameter ranges, spectral normalization, H-uniformity, and error terms are not supplied, and the named output/artifacts/threshold_check.py artifact is absent from the audited tree. The threshold algebra alone cannot certify the stated zero-density theorem.

## Originality

Spectral-aspect zero-density for SL(2,Z) Hecke–Maass L-functions was already proved by Liu–Streipel (International Journal of Number Theory 20 (2024), 849–866): their Theorem 1.3 deduces a weighted zero-density estimate from a mollified twisted second moment in Gaussian spectral windows, with the underlying moment theorem uniform for T^epsilon<=M<=T^(1-epsilon). That does not automatically cover the record's hard cutoff or large H range, but it means the record is not the first short-spectral-window zero-density result and any novelty claim must be framed around precisely proved differences. No such rigorous comparison is carried out.

## Scientific value

The calculation comparing the three first-version Qi–Qiao sieve branches with the trivial benchmark is useful diagnostic algebra, but it is not a validated research theorem of the scope claimed. A publishable result would need a complete zero-density derivation from a specified version of the large-sieve theorem and a comparison with the existing Liu–Streipel spectral zero-density theorem.

## Limitations

- This audit does not prove that no hard-cutoff or larger-H refinement can be obtained from Qi–Qiao; it finds that this record does not supply such a proof.
- The v2 Qi–Qiao theorem is a stronger large-sieve input than the v1 threshold used by the record, so a new derivation would have to be redone from the current theorem rather than merely relabeling the old threshold.
- The claimed output/artifacts/threshold_check.py file is absent from the audited repository tree.
- Liu–Streipel use a smooth Gaussian spectral weight and a smaller H range; their theorem is prior art for spectral zero-density, not a verbatim duplicate of every parameter in the record.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/16/009
- https://arxiv.org/abs/2608.29558v2
- https://bpb-us-w2.wpmucdn.com/faculty.umaine.edu/dist/1/19/files/2023/10/GL2MaassForms-preprint.pdf
- https://doi.org/10.1142/S1793042124500441
