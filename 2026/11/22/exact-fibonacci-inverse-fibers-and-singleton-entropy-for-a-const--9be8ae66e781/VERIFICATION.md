---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

An output mark forces an occupied pair, and the cyclic 111 exclusion forces the immediate outer neighbors to zero. No two marks can be at gap 1 or 2, and filling just the occupied pairs realizes any allowed output. At gap 3 the two outer zero requirements coincide; at gap 4 there is no free site; at larger gaps the d-4 free sites form a path with no adjacent ones. This gives the product of F_(d-2) including a single marked pair followed by its own wraparound gap. At zero output the preimages are all cyclic independent sets, counted by F_(n-1)+F_(n+1) on fixing one site. Pointing an output mark multiplies by k, whereas assigning the marked coordinate gives n choices; counting ordered gap compositions therefore gives both sums, the singleton one allowing only gaps 3 and 4. For a gap series W(z), the 1/k weighting gives the formal sum -log(1-W(z)); multiplying its derivative by z introduces n, giving zW'/(1-W). Adding the zero word to the image yields the stated rational functions. The log-derivative power sums give leading Perron coefficients exactly 1; the two companion matrices are primitive (cycle lengths 1,3 and 3,4). The ratio is consequently as stated. For k≥2 the addition identity for F bounds the product by F_(n-3k+1)≤F_(n-5)<F_(n-2), and the Lucas zero fiber is strictly larger still. Choosing one representative per output is exactly the maximal injective codebook. All arguments use indexed rings and n≥5; the smaller coefficients of the rational series are only a formal extension.

## originality

PASS

Bounded comparison found structurally close cyclic counted-preimage results but not an existing restricted cyclic AND fiber classification or singleton-growth result implied by the inspected sources. The novelty assessment does not extend to the gap-composition method, Fibonacci/Lucas laws, or CA transfer methods as such.

## value

PASS

For the indexed detector that reports adjacent coincident ones, one needs both the size of an optimally chosen zero-error codebook and the fraction of outputs inherently determining the input without such a codebook. The exact per-output law yields both and explains why exponentially many uniquely recoverable outputs still form a vanishing share. The constrained input is natural for separating occurrences of occupied pairs, and the classification covers every target rather than selected patterns or small lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
