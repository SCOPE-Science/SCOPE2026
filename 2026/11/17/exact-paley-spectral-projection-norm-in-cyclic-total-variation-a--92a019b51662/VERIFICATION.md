---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For real cyclic signals with p prime=1(mod4), the difference D maps signals modulo constants isomorphically to H={u:sum u=0}, and the H unit l1 ball is convex hull of (e_i-e_j)/2, so the sharp TV norm of translation-invariant projection is half the maximal l1 norm of difference between shifted convolution kernels. Classical quadratic Gauss sum gives K(0)=(p-1)/(2p), K(x)=(-1+sqrt(p)chi(x))/(2p) otherwise; Legendre autocorrelation sum_x chi(x)chi(x-d)=-1 yields kernel-difference l1=1+(p-1-2chi(d))/(2sqrt(p)), maximized on quadratic nonresidue arc jumps. The exact norm is 1/2+(p+1)/(4sqrt(p)). A small arc perturbation h and real Fourier basepoint with coefficients 2lambda aligned on residues give the EXACT nonlinear difference S_lambda(b+h)-S_lambda(b)=P_R h+mean(h)1 and hence an attained sharp lower witness for BV Lipschitz. Coordinatewise radial proximal nonexpansivity, Fourier commutation with D and Parseval give upper sqrt(p), not an asserted exact nonlinear constant. Independently recomputed kernel shifts for p=5,13,17,29,37 and all nonzero d, agreeing with nonresidue maxima and formula; these finite p calculations corroborate the all-prime arithmetic proof. RESULT.md blob 01455c13a36c9c6d3db7058276367b555267a722 and artifacts/verify_paley.py blob 4b6e43ffe76310efa476513a1bd7192e4472e40a read.

## originality

PASS

Best-of-knowledge original exact zero-sum derivative l1/TV Paley half-frequency projection constant with extremal arcs and its explicit nonlinear radial soft-threshold witness, not the old full-space Fourier algebra norms or generic Fourier TV recovery.

## value

PASS

Sharp induced BV variation of a natural quadratic-residue spectral projector is a meaningful exact arithmetic operator invariant; Legendre nonresidue arcs classify all sharp jump lengths. Its exact active-mask construction gives a concrete, dimension-growing nonlinear two-input BV instability despite Euclidean nonexpansiveness, useful when interpreting cyclic spectral denoising. The value lies in the extremal zero-sum variation calculation and constructive nonlinear consequence, not in rederiving a Gauss sum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
