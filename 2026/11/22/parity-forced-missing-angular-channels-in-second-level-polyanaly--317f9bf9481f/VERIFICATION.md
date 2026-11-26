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

The first creation operator applied to the normalized analytic monomials gives the stated basis of the true second level (not the two-level sum), with angular weight p-1. The full angular integral of the compressed multiplier forces output index p+m. In the radial integral let a=p+m/2 and view t as Gamma(a,1) with mean and variance a. Then (t-p)(t-p-m)=(t-a)^2-(m/2)^2, so the integral is Gamma(a)(a-m^2/4); the Gaussian normalization supplies the stated factorials. This also holds at p=0, where the factor t cancels the apparent singularity of the basis expression. The only potential zero is p=m(m-2)/4, integral and nonnegative exactly at even positive m. Expanding the log-gamma ratio gives p^(-1)[1-(m^2/8+m/2)/p+O_m(p^(-2))], so multiplication by the linear term gives the stated 1/p correction. Convergence to 1 makes the perturbation of S^m compact, bounds all nonzero weights away from zero, and leaves exactly the first m output coordinates plus the single missing even-winding output. Thus the range is closed and the index is -m. The Fredholm essential spectrum is the circle; inside it the nonzero index persists for T_m-lambda, and the compression norm is at most one. Independently checked 14 radius quadratures, including nodal zeros and adjacent nonzeros, and ten large-index comparisons (python3 /workspace/checks/finite_review.py 5, requires mpmath; /workspace/checks/5.txt). These approximate checks do not decide exact zeros or infinite spectrum; those follow from the analytic argument.

## originality

PASS

The true-level model, Laguerre/Hermite machinery and Fredholm theory are established, and neither angular equivariance nor the index on its own carries the originality decision. The supported distinct claim is the explicit mixed moment for this specified compressed angular multiplier and its complete finite defect classification for all positive windings. The strongest inspected kernel theorem is about the symbol-to-operator map, not the vector kernel of a particular phase operator. This judgment is limited to the stated comparisons.

## value

PASS

Pure angle multipliers represent the basic Fourier components of angular observables, and the true second level is the first level with a radial node in the mode factors. The formula tells exactly which input and corresponding output mode are missing under compression, at every positive winding, information that the common index and spectra cannot distinguish. The parity exception is a concrete loss of a channel, including p=0 for winding two, not just a rederivation of the shift index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
