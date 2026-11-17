# Independent mathematical audit

## correctness

PASS

Reconstructed the legal (k−1)-vertex overlap graph, with F_(k+2) required edges, strong connectivity via append-ones paths, and signs of out-minus-in imbalances from initial/final bits. The potential g(v) counts initial ones before first zero, setting g(1^(k−1))=k−2; verified every legal edge loses at most one. Summing g against imbalances gives S=F_k−1 and hence R>=S−(k−2)=F_k−k+1 even for arbitrary walk endpoints. The constructive augmentation duplicates j successive append-one edges for each negatively imbalanced vertex except 1^(k−2)0, bijectively balancing remaining positive vertices, with Euler trail from 01^(k−2) to 1^(k−2)0. Checked special k=2 Euler circuit. Inspected checker.py. Independent exact potential and Fibonacci counts recomputed k=2..8, and its own bounded BFS k<=5 is visibly exhaustive; the all-k proof is the potential+augmentation argument.

## originality

PASS

The sharp one-string LINEAR endpoint optimization is not immediately implied by existing sharp CYCLIC Fibonacci-cover bounds for 11-avoidance (equivalent by complement), which give cycle length F_(k+2)+F_k−1. Cutting an optimal cycle creates a linear cover of length F_(k+2)+F_k+k−2, not the optimal F_(k+2)+F_k for k>=4. The new open Euler trail saves k−2 characters against this direct cut. General Matchtigs/minimum string-set formulations do not automatically enforce one finite string or provide evaluated Fibonacci endpoint formula.

## value

PASS

Constrained k-mer spectra and minimum textual representation are a natural genomics/combinatorics invariant. This result gives a sharp all-k one-string optimum, exact unavoidable repetitions, constructive Euler trail, and matching dual certificate. The linear/cyclic endpoint gap is structurally motivated; it is not a routine numeral substitution from the cyclic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
