# Independent mathematical audit

## correctness

PASS

For any contiguous partition let z be blockwise constant with strict boundary gaps, choose strictly positive multipliers on internal edges and zero on boundary edges, and put m_i(x_i−z_i)=λ_i−λ_{i−1}. This is the stationarity sign for z_i−z_{i+1}≤0; the block means, prefix-sum multipliers and gaps vary continuously so the partition persists on an open neighborhood. On the quotient by constants, the step functions identify the seminorm with weighted ℓ1, giving the maximum step-column gain. A step inside (p,q] becomes the constant (T_q−T_j)/(T_q−T_p) on that block; the two edge jumps give exactly the chord's height (with zero artificial boundary weights). Taking the max over attainable partitions gives the upper hull at every knot by the two-support extreme point of the fixed-barycenter linear program. Finite continuous piecewise linearity yields the global bound by summing segment increments, including segments in chamber boundaries where the neighboring restrictions agree. A sufficiently small step in a maximizing chamber attains the bound; an identity chamber is allowed when the factor is 1. Concavity and minimal stabilizing enlargement follow from hull minimality. The two sample constants and 558 exact additional input pairs agreed with an independent upper-hull and weighted max–min computation: python3 /workspace/reproductions/3.py. This calculation is supplementary; the general proof is not inferred from it.

## originality

FAIL

The earlier Resultary record c4a7412f8310 states precisely the same sharp two-input edge-TV modulus on a chain with arbitrary positive observation masses and edge weights, with zero auxiliary endpoint weights, the same upper concave envelope and chord formula, attainment for every profile, and the same concavity criterion. I inspected its Finding and assumptions in the mirror, not just a title or abstract. Minimal stabilizing enlargement is an immediate implication of the already-stated criterion and the definition of the least concave majorant. The examples do not supply a surviving substantive remainder. A separate same-day exact overlap corroborates coverage but is not used to infer chronological precedence.

## value

FAIL

The underlying upper-hull theorem is a useful diagnostic for shape-constrained regression, but the submitted record contributes no distinct useful result beyond the earlier theorem. Hull minimality restates the known concavity boundary as an enlargement rule by definition, and the sample gains and supplementary checks are evaluations of the known formula. There is no separate new finding of scientific value to repair and retain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
