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

The full direct power-domination checker is `verify_power.cpp` (compile with `g++ -std=c++17 -O3 verify_power.cpp -o verify_power` and run `./verify_power`); it returns `VERIFY_OK` after testing all 33,856 subsets for the 3-, 4-, and 5-label instances. The exact slide-adjacency and graph-diameter checker is `verify_slides.py` (`python3 verify_slides.py`), returning `SLIDES_OK` for orders 3 through 8. A separate labelled-forest polynomial check is `verify_polynomials.py`, returning `POLYNOMIAL_OK` for orders 3 through 5. These are finite checks only.

The proof in `RESULT.md` derives the universal forest condition, all inclusion-minimal configurations, explicit incidence-preserving token-slide bijection, and sharp diameter bounds without extrapolating from the checks. Independent mathematical validation has not been performed.
