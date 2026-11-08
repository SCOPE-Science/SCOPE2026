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

The standalone program `CHECK.py` was run with Python 3 using integer and rational arithmetic; output ended in `CHOW_COMPONENT_DEGREE_CERTIFICATE_OK`. It checks the two components' degrees for the six exact parameter pairs in the result, and confirms the quadric fixed-point computation under two disjoint choices of torus weights. It independently checks the quadric numbers for five cases using the Grassmannian top-coefficient/Vandermonde formula. The known \((1,3)\) values \(92\) and \(140\) are a literature cross-check.

The arithmetic samples do not prove the all-parameter formula. That proof uses (i) the classification of degree-two cycles, (ii) generic birationality of the two parameterizations, (iii) identification of the Chow polarization with \(\xi+2h\), and (iv) the projective-bundle pushforward and Grassmannian localization identities. The mathematical review is not independent, and no independent validation has been performed.
