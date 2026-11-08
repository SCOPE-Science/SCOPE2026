# Review of the critical-radius checksum construction

## Correctness — PASS

The prefix-class argument supplies the universal lower bound \((q-1)q^{n-1}\); the checksum eliminates exactly one last-symbol choice per prefix class. For the four expressly stated pairs, `verify.py` enumerates every vertex, computes the complete closed incoming radius-\(t\) ball by two distinct exact methods, and checks that its intersection with the code is nonempty and differs from all other intersections. The program was extracted from the proposed deliverable and executed, producing `VERIFY_OK cases=4`. The result is a finite computer-assisted theorem, not an unbounded generalization.

## Originality — PASS, with priority qualifications

Boutin–Horan Goliber–Pelto (arXiv:1412.5842), inspected through the full relevant identifying-code section, proves the bound but explicitly leaves critical word length \(n=2t-1\) open; its critical construction has \(q^{t}\) additional vertices. Searches for critical-radius, ternary/quaternary identifying codes and exact four values located no theorem covering these four cases. Prior reported binary critical cases and radius-two nonbinary cases address different parameter pairs and logically do not imply this four-case modular construction. The 2015 undirected paper does not apply to the directed in-ball problem. Search absence is not proof of first discovery, and unindexed equivalent work remains a residual risk.

## Value — PASS

At the minimal length where radius-\(t\) identification is possible, the first two higher radii are a natural open boundary problem. This supplies four exact nonbinary sensor minima (including a graph with 16,384 vertices), together with a single reproducible algebraic construction rather than isolated opaque subsets. The answer requires no downstream theorem, but does not settle arbitrary alphabets or radii.

## Scientific limitations

No statement is proved for \(q\) outside \(\{3,4\}\), for \(t\) outside \(\{3,4\}\), or for undirected or rotation-quotiented graphs. No independent audit has been performed. The theorem relies on a finite exhaustive verifier whose loops, complete domains and reverse-edge interpretation are included.

Self-review: passed. Independent audit: not yet performed.
