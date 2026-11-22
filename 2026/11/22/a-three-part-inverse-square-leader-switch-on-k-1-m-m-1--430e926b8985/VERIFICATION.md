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

The independent validation channel has not been performed. To check the mathematical claims, run `python3 verify.py` with SymPy available. The program constructs rational grounded matrices from unweighted complete tripartite graphs, checks all pair orbits for sizes 2--5, checks representative larger sizes 6--10, and confirms exact general rational identities plus polynomial coefficient positivity.

The complete argument is in RESULT.md: Jacobi complementary minors, spectral projection and resolvent identities, exact derivatives, strict rational differences for five pair types, and four globally positive coefficient certificates. Finite examples support those infinite-parameter arguments but are not an infinite enumeration. All calculations use unnormalized graph Laplacians and the squared inverse of the **principal follower block** after two vertices are pinned. Other spectral orders and unequal edge weights are not certified.
