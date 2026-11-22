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

# Reproducibility and limits

The two executable Python 3 programs in `code/` have no dependencies outside the standard library and require no input files or network access. In a directory containing the embedded package files, run:

```sh
python3 code/check_direct.py
python3 code/check_quotient.py
```

Their JSON outputs match `data/check_direct.json` and `data/check_quotient.json`. Each includes assertions that stop execution on a discrepancy. The programs were executed from the package directory during preparation.

The first checker enumerates all 4,960 three-landmark sets and all 35,960 four-landmark sets on 32 vertices, checking separation of 496 unordered vertex pairs; it constructs jump/slide transitions and performs all-source BFS on the resulting sixteen eighty-state components. The second checker separately uses all 242 nonzero ternary vectors and all 1,820 four-subsets of the even antipodal quotient, identifies 16 pentads with 80 distinct projected four-sets, and verifies the 1,280 lifts and 80-state distance profile.

Central independently reproduced outputs are: optimum size 4, optimum count 1,280, sixteen jump components of size 80, uniform jump degree 12, 7,680 global jump edges, component distance profile \((1,12,30,28,9)\), component diameter 4, and exactly zero slide edges.

The complete all-dimensional significance is neither asserted nor inferred. The proof in `RESULT.md` is an elementary finite combinatorial proof specific to the five-cube. The checkers are independent algorithmic implementations, not externally audited implementations or formal theorem-prover certificates. Historical originality is assessed separately and has residual literature-access risk. Independent audit has not been performed.
