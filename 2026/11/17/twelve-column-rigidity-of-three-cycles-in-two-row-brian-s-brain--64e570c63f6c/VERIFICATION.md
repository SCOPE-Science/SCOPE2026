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

A three-periodic Brian’s Brain site has exactly four possible full histories: silent or firing in one phase modulo 3; firing and refractory transitions force this. For 2-by-n periodic Moore neighbors with eight offset incidences counted separately, the explicit six-term local N_{r,t} rule is necessary/sufficient even at n>=3. Independent enumeration of the 16 column types, 256 ordered-pair transfer states and all 4096 triples gave 199 incident vertices and 346 directed edges. Every cyclic strongly connected component is exactly a single silent loop or one of two directed simple 12-cycles, each internal indegree/outdegree one; all other vertices are transient. A closed length-n walk exists only on those cycles, yielding #Fix(F_n^3)=1+24*[12|n] for all n>=3; the only temporal fixed point is silent, so primitive 3-cycles count (24/3)=8 when 12|n. Crucially the infinite-n conclusion is the finite transfer-graph decomposition, not testing just a finite set of n.

## originality

PASS

The exact all-circumference period-three classification on 2-by-n Moore strip with duplicated offsets appears distinct from classical generic cellular automata graph approaches and a published 3-row Brian’s Brain transfer census; the original 1996 active essay was not readable and retains a residual priority risk.

## value

PASS

Classifies all occurrences of the first nontrivial temporal oscillator period in a canonical three-state refractory automaton across infinitely many circumferences. The 12-column spatial locking, constant 8 oscillator orbits for n divisible 12 and zero period-three spatial entropy are natural and mathematically surprising compared with wider-strip positive-entropy regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
