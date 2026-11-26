---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The all-n asymptotic and concentration for fixed labeled q >= 4 are correct. First letter and bigrams give the unigram counts by adding the initial occurrence to incoming bigram counts. On a distinct-letter run chain the unique nonloop path forces every loop to be exhausted before leaving its vertex. There are q! binom(n-1,q-1) such words for n >= q. The type bound used in the proof is also valid: disjoint nonempty cyclic-root letter sets leave at most q long runs; at equality every root is a one-letter power, and the no-outside-occurrence property excludes any remaining letters outside those runs. Types with s < q contribute O_q(n^(q-2)) by the weighted one-equation count and bounded number of types, with the runless case supported at bounded lengths. Independently, for a singleton's Euler walk fix its last-exit tree to the terminal letter. Every vertex's departures other than its fixed tree exit (all departures at the terminal) must go to one common destination: otherwise permuting them gives a second trail, since a stopped incomplete walk would leave balanced unused edges whose last-exit tree leads to the already exhausted terminal vertex. After fixing this finite type, differences of free multiplicities must be circulations on a partial functional digraph, hence constant on each directed cycle and zero off the cycles; fixing total length removes one cycle parameter. The only q-cycle possibility uses all q self-loops, leaving a single path of tree exits, again the run-chain case. This is an infinite proof check, not an inference from finite enumeration.

## originality

FAIL

The leading coefficient and concentration are not merely consistent with the prior upper bound; they follow directly from the stronger published finite-type structure and per-type counting rule. At k=2, q disjoint nonempty cyclic-root factor sets on q letters must be the q singletons. The cited exclusion of outside occurrences leaves exactly long monochromatic chains at maximal type; all other types are bounded by one lower power using the prior equation (8). Finishing with a count of permutations and positive compositions (and the elementary path argument for short runs) requires no new structural result. This is verified prior implication, not a claim that a prior paper printed the same q>=4 formula verbatim.

## value

FAIL

The run-chain interpretation is clear and useful exposition, but as an independent finding this is a routine extremal-case evaluation of an existing all-k structural and counting theorem. The familiar labeled-composition coefficient and restatement as conditional probability do not supply a new combinatorial invariant, obstruction or quantitative result beyond that immediate implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
