---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python check_sunfleck.py` with Python and SciPy to obtain deterministic comparisons against direct state-trajectory quadrature and brute-force pointwise objective samples. The recorded execution passed 12,050 assertions and returned \(\ell_c=0.276668624779832\ldots\), \(g_*(1)=0.649546035969512\ldots\), relative improvement \(0.292721404613706\ldots\), and limiting gap \(\log3=1.098612288668110\ldots\).

The exact proof in `RESULT.md` derives the whole objective and proves derivative-sign uniqueness for every positive \(a,b,c,d,\ell\) with \(d>b\). The numerical tests do not establish claims outside their samples and are not substituted for symbolic all-domain arguments. No biological parameter calibration, clinical or ecological prediction, or independent audit has been performed.
