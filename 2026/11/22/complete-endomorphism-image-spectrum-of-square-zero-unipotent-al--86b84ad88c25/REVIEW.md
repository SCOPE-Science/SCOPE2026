# Scientific review

## Correctness — PASS
Every endomorphism necessarily respects the right-translation orbit fibers; homomorphism identities force a shared additive first-coordinate linear operator and an affine component-label map, while leaving one arbitrary function. This is a theorem about all set maps, not merely linear maps. The image polynomial follows by counting occupied cosets independently within each output orbit. The forbidden image interval and sharp endpoint count follow from the rank of the common operator. The universal deductions are given in `RESULT.md`; finite tests in `checker.py` independently corroborate the small cases, including exhaustive four-point all-set-map enumeration. No unproved numerical extrapolation is needed.

## Originality — PASS, with limitations
The 2014 archival source describes general medial-quandle structure, not this exact endomorphism image multiplicity polynomial. The closest publicly available semisimple Alexander-quandle retraction theorem cannot subsume a nonsplit unipotent operator. The closest exact same-object paper counts *subquandles*, not multiplicities of endomorphisms by image cardinality; the new occupancy factor weights surjective maps, an additional invariant not supplied by an unweighted subquandle polynomial. Hou's related 2011 work concerns automorphisms; its full text was unavailable, so the priority risk is recorded. The proof does not claim novelty for the automorphism count, the orbit decomposition, or Stirling numbers. Similar statements under rack/medial-quandle terminology might remain undiscovered.

## Value — PASS
Counting all noninvertible set-theoretic endomorphisms by image size is an intrinsic structural statistic of a finite algebraic object. The complete polynomial is exact in an unbounded family, and the sharp missing range between \(p^{2d-1}\) and \(p^{2d}\) is a structural constraint on all possible endomorphism images, not a minor fixed-parameter exercise. It pinpoints a nonsemisimple boundary beyond an existing semisimple classification.

## Sources and remaining risks
Full published material was examined for the archival medial-quandle structure theorem and for the same-object subquandle enumeration and the semisimple endomorphism theorem. An original paper on Alexander quandle automorphism groups was not readable in full, and an earlier equivalent all-endomorphism result could exist under different nomenclature. The checker does not prove infinite-dimensional assertions by itself; the elementary proof does.

Self-review: passed. Independent audit: not yet performed.
