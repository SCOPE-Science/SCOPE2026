---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For k>=4 the norm-one circle has 2^{k+1} points. Reduction modulo M=2^{k-1} has four lifts per element and is parameterized without overlap as i^j(1+2iz)/(1-2iz), j=0..3 and z modulo 2^{k-3}. Converting the difference energy to Re((s-1)(w-1))=0 mod M gives a ten-type orientation valuation table; only nine ordered orientations contribute, with Tprime=3*n*2^{n+1}+6*2^n=6(n+1)2^n, n=k-3. Multiplication by |C| and the 16 lifts yields E=3(k-2)2^{2k+3}. Orthogonality supplies unweighted Fourier fourth moment. Independent direct convolution checks through k=7 and angular incidence counts support, not replace, the valuation proof.

## originality

PASS

Best-of-knowledge novel exact fourth-moment/energy value for the dyadic Gaussian norm-one circle at every k>=4. Hickman–Wright study general restriction over residue rings with inequalities and divisor losses, rather than the constant-input circle fourth moment; Nica develops unimodular/Eisenstein spectra primarily in odd residue characteristic. Related exact odd-prime-power circle energy results are not applicable to the highly ramified 2-adic Gaussian ring.

## value

PASS

The natural additive-energy invariant and constant-input Fourier fourth moment have exact linear-in-depth normalized value E/|C|²=6(k-2). It quantifies nontrivial 2-adic collision concentration over an infinite local-ring tower with a structural orientation/valuation proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
