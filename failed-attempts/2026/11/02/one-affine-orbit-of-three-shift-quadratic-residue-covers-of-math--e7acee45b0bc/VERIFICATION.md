---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

2 is nonsquare modulo 5, and the square test for nonzero w is N(w)²=w¹²=1; zero is separately included. Nonzero square multipliers normalize pairs of either difference character to the respective pair (0,1) or (0,u), and −1 is square. An independent exact replay encoded a+bu by a+5b, constructed Q_0 by squaring using u²=2, and formed a 25-bit translate mask for each center. Pair unions never gave the full mask; testing all third-center choices gave 150 square pairs with zero extensions and 150 nonsquare pairs with two extensions. The normalized uncovered-size histograms were {2:11,3:10,4:2} and {0:2,2:13,3:8}; successful third centers for (0,u) were codes 16 and 19. Counting extensions with the third code larger than both pair codes gave 100 distinct triples. Applying all 300 square-affine transformations to {0,u,1+3u} reproduced exactly this set. The three stabilizer elements had encoded (multiplier,translation) equal to (1,0),(17,5),(12,16), and (17,5) cycles the three vertices. This is exhaustive for the actual domain, not a sample of finite fields.

## originality

FAIL

Brouwer and the Paley domination literature already give minimum size three. The exact count and single orbit for the same square-affine group are the q=25 row of Resultary 3e8343da37ce. The remaining pair-incidence and stabilizer data follow from this orbit and checking one representative; a separate Paley-25 record also recovers the entire covering set by complementing its classified nonshattered triples. The finding is not distinct relative to this mathematical coverage. The same-day date and the later record do not establish who first proved any of the statements.

## value

FAIL

The geometry of minimum covers at the last order with Paley domination number three is a motivated finite problem. However, the exact order-25 contribution here repeats a complete orbit-table row; its apparent extra pair-incidence and stabilizer facts are the immediate orbit consequences above and a check of the three-point representative. The frozen record yields no surviving independently useful unknown invariant beyond that classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
