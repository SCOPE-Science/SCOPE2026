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

# Verification and reproducibility

`check_wave.py` constructs finite projective planes of orders \(2,4,5\), then tests the incidence-square identity, calculates the exact wave matrix over \(\mathbb F_3\), computes its modular kernel dimensions at relevant times, and verifies its minimal global order. Run with `python3 check_wave.py` in a directory containing NumPy. Its observed exact nullities match the analytic formula: order \(2\) gives \((t,E)=(1,0),(4,4),(8,28)\); order \(4\) gives \((1,20),(2,40),(3,41),(6,82),(9,42),(18,84)\); order \(5\) gives \((1,0),(4,4),(8,124)\). Additional tested time points appear in `check_wave_output.txt`.

`check_direct.py` uses only the Python standard library, constructs the incidence graphs with different finite-field arithmetic and coordinate charts, and performs neighbor-by-neighbor updates of individual labelled states. Run with `python3 check_direct.py`. It checked \(804\) fixed-seed configurations across orders \(2,4,5\) and observed no periods outside those proved, attaining the predicted exact maximum in all three cases. Its observations are recorded in `check_direct_output.txt`.

The tests do not enumerate every configuration in any of these state spaces and do not prove a universal formula. The mathematical proof uses the incidence identity and complete Jordan structure over every \(\mathbb F_{3^f}\). The unrestricted period and fixed-point claims do not rely on these samples.
