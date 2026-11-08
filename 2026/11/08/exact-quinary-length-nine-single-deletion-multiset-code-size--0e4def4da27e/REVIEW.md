# Scientific review

## Correctness

PASS. The deletion-output neighborhoods give an exact binary optimization, with no missing conflicts or extra constraints. The checksum class contains exactly 143 valid vectors by a cyclic alphabet relabeling. Both independent finite formulations were solved to global integer optimality: the first has 495 five-term inequalities, the second has 4,950 pairwise inequalities, and both report 143 with a zero optimality gap. The included code regenerates and checks all objects. Computation depends on the stated mixed-integer solver; there is no independently checked exact rational branch-and-bound trace.

## Originality

PASS against the inspected sources. Kreindel, Barouch Essayag and Zabokritskiy (arXiv:2601.05636, Section 5.5) give the same quinary checksum construction but report exact optima only through length eight, and explicitly conjecture the length-nine equality. Their related arXiv:2603.18322 addresses deletion balls and general bounds. No accessible source or closely ranked indexed record was found giving the length-nine exact maximum; search absence does not prove priority. Ordinary string deletion codes and high-deletion multiset codes are distinct objects.

## Value

PASS. This answers the first open blocklength of a specific published conjecture with an exact natural parameter and globally optimized finite evidence. It gives a new sharp benchmark for five-symbol unordered deletion coding rather than a numerical perturbation of a known code size.

## Risks

The proof of the upper bound relies on the soundness of two floating-point mixed-integer branch-and-bound implementations using the same underlying HiGHS library; it is computational rather than an independent exact rational certificate. Earlier unpublished or unindexed exact computations may exist. No general conclusion for all lengths is claimed.

Self-review: passed. Independent audit: not yet performed.
