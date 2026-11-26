# Independent mathematical audit

## correctness

FAIL

The mathematical conclusions check under the explicitly uniform-permutation model, but the frozen Finding states only independent continuous priorities and the assumptions falsely assert that independence and continuity imply a uniform permutation. Without identical or otherwise exchangeable priorities the stated Δ_6=1/9 is false: assign independent continuous variables on disjoint ordered intervals enforcing 0,2,4,1,3,5. Both graphs then accept exactly 0,2,4 and the increment is zero. The distance is three at N=6 (only at N=5 does the labeled chord have distance two). For the uniform model, first arrival is uniform and restriction to the complement of its closed neighborhood leaves uniform relative order, proving the recursion. On coupled graphs, an earliest discrepancy must be at a chord endpoint; any later one has an earlier discrepant neighbor. An induced-subgraph discrepancy analogously has a decreasing-priority path to a deleted vertex. These paths are simple, length ℓ has order probability 1/(ℓ+1)!, and with only two degree-three vertices the path multiplicity bounds 8/6/2 (arbitrary chorded start/chord endpoint/cycle) hold. For N≥29 the retained 28 vertices form the stated path with its chord; outside H the endpoint distance is at least 13, and inside H a vertex at endpoint distance d has distance at least 13−d to a deleted site. Taking the smaller of the two necessary discrepancy-event bounds and summing with |D−D^H|≤2 and at most four sites per d produces B_12. An independent rational run checked N=5–28 (direct permutation enumeration too at 5–7), the exact gadget gain 13738981531700639/304554407185153125, and a factorial-tail upper bound about 0.00850039683462, giving the lower bound about 0.03661135071382. Replay: python3 /workspace/branches/44029fc6-da00-4bb1-a32d-c92bf0036c1e/independent_check.py. The supplied code was inspected, not executed. This proves the advertised numerical result in the intended uniform regime, not the frozen equivalence of priority assumptions.

## originality

FAIL

The distinct indexed opposite-short-chord record covers the complete sign classification even after correcting the priority hypothesis, by a closely related finite-cutoff locality method. Its stated constants do not literally give the threshold 0.0366 from cutoff 29; that modest numerical sharpening is separately assessed for value and does not establish a substantive distinct claim. The overlap concerns current statement coverage, not priority or copying.

## value

FAIL

An all-size increase from one exclusion bond and a genuine small-cycle boundary would be informative if not already covered. The remaining modest constant improvement over a known uniform positive bound has no identified sharp threshold, application, new invariant or mathematically privileged decimal; it uses the same factorial-locality mechanism. Correcting the iid assumption alone therefore would not yield a distinct valuable survivor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
