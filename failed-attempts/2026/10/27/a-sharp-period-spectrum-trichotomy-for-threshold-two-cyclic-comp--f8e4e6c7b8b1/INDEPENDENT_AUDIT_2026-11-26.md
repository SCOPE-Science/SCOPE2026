# Independent mathematical audit

## correctness

PASS

Threshold-two tests depend only on caps at two, and capped addition respects merging into destination colours. Each occupied initial part–colour class moves as a unit; tagging one vertex from each class preserves its labelled trajectory, even when two actual class sizes share a cap. All labelled colours return exactly when all tags return, giving the max entry time and lcm period. An independent bounded reconstruction checked all 17,576 nonempty profiles and 109,512 occupied tags, found max entry nine and periods {1,3,4,6,12}, and verified T^21=T^9 on every tag. It found recurrent profile counts 174, 1826, 18, 6 and 126 in that order, and separately reproduced the K_{5,3,2} time-nine witness by direct labelled updates. The exceptional profiles yield 2, 1 and 7 symmetry classes; per chosen large shore period four has 6 orientations with 2×2 small-shore labellings, period six has 6 orientations with 2³ labellings, and per chosen small shore period twelve has 18,18,6 orientations with 1,2,6 labellings at sizes 1,2,3. Each specified two-large-colour shore has B(n)=2^n−2n−2 assignments. These give the claimed R formulas (states, not cycles), while multinomial weights of all profiles give the transient/period census. Independent replay: /workspace/branches/401e679c-cf1e-4b34-b176-a4f92f9a5b3d/independent_check.py and independent_output.log. The frozen checker sources and output are supporting evidence; small labelled examples alone do not prove the all-size result.

## originality

FAIL

A distinct indexed result has the identical update, graph family, sharp identity and entry bound, exceptional period spectrum and three phase regimes, plus a period-three existence criterion. The same result supplies the exact recurrent capped profiles via its executable cycle enumeration and computes the labelled least period on each capped cycle. The frozen explicit labelled multiplicities are not printed there, but they are a mechanical multinomial weighting of those profiles; the transient census likewise weights profiles after a finite comparison of the supplied bucket traces. The strongest overlap was indexed later; this comparison concerns scientific coverage and mechanical implication, not who discovered it first or whether the records are independent. No distinct surviving dynamical or non-mechanical counting claim is established here.

## value

PASS

On a natural dense graph family, the sharp uniform cutoff, exceptional primitive-period regimes, and all-size counts separate genuine vertex-level waves from artefacts of merging or capping. In particular the eight six-cycles isolated on K_{2,2,2} illustrate why physical period rather than population period is meaningful. The intrinsic usefulness of this classification is distinct from the finding that a matching catalogue already provides the dynamics and a sufficient certificate to recover the counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
