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

# Reproducibility and verification

The standalone `checker.py` uses only Python 3's standard library. Run `python3 checker.py` in the extracted artifact directory; its success marker is `ALL_CHECKS_OK`. The checker was run to completion from the current result materials before publication.

For the abelian groups \(C_2,C_3,C_4,C_6,C_2\times C_2,C_2\times C_3\), over the tested two- and three-colour palettes, it enumerates colour-word shift orbits, independently enumerates primitive colour patterns on quotients, constructs subgroups and performs incidence-Mobius inversion, and compares all predicted orbit multiplicities. It also tests the nonabelian Dedekind group \(Q_8\) with two colours. For specified small groups, it independently enumerates finite actions on carriers up to four points and checks rigidity by all commuting colour-preserving relabellings. It confirms the one-colour \(S_3\) example outside the theorem's domain.

The finite computation does not establish the universal theorem or historical novelty. These are supported respectively by the mathematical proof and by a bounded comparison with accessible sources. The source-based historical assessment is provisional; independent validation was not performed.
