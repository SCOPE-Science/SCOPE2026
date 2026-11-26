# Independent mathematical audit

## correctness

PASS

The frozen mathematical assertions reproduced independently: exhaustive traces with centers allowed inside the support yield counts 25, 300, 2200 and 3600 in degrees 1–4, with the 100 failed triples exactly the square-equilateral set and each missing the all-positive trace. The separate smaller-order replay gives dimensions 2, 2, 3, 3 at orders 5, 9, 13, 17. The bound of 25 traces rules out sizes >=5. Independently generated full orbits matched the eight stated representatives and sizes. Replay scripts and machine-readable results are in /workspace/branches/f6ec5214-9a68-4bbc-9b04-e447ee1bbc19/ (paley25_independent, paley25_triple_overlap and paley_smaller_orders). The repaired Finding is only the maximum-size witness census and symmetry classification. Its replacement verifier builds adjacency from the norm N(a+bt)=a²−2b² and the Euler criterion x^12=1, thus excludes zero and includes all 25 centers. Each of 12650 supports is tested for all 16 four-bit masks. The 600 group maps are distinct by their values at 0, 1 and t and preserve adjacency. Exhausting the retained set by full orbits and counting maps that fix the representative verifies the reported order-size pairs by orbit–stabilizer. The repaired verifier was executed and printed all eight rows and VERIFY_OK supports=12650 shattered=3600 orbits=8. Semantically inspected replacements: /workspace/repairs/5/RESULT.md, VERIFICATION.md and paley25_verify.py. No frozen verifier was executed.

## originality

PASS

PASS applies to the repaired four-set census and orbit classification only. For the frozen submission, the exceptional-triple classification was presented as a principal distinct finding but was materially covered up to nonsquare scaling by the earlier exact closed-cover census, and the prior open Lovász complex already excludes the same 100 triples by the all-positive trace. It is not a false theorem: the independent replay verifies that no other triples fail and that the closed-cover family becomes the failed family under the nonsquare transform. The repair explicitly credits that overlap and removes the exceptional triples, complete polynomial and earliest-order assertion as contributions; it retains the distinct all-16-mask four-support result. Best available exact prior sources classify one trace at a time, or work in a different center convention, and do not supply the retained count or orbit decomposition.

## value

PASS

The repaired invariant concerns extremal witnesses in a natural Paley graph at an order attaining the information bound, not an arbitrary subset slice. It identifies the complete set size and eight symmetry classes of all maximum witnesses, five free classes and three with stabilizer orders 2 or 4. This refines equality in the bound beyond existence, and distinguishes genuine shattering from the much larger set of quartets with a common open neighbor. A researcher comparing the structure of maximum supports across small finite fields can use the canonical orbit representatives and weights without redoing the support census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
