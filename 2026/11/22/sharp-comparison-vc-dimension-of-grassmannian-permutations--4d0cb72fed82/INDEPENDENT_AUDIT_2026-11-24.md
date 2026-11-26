# Independent mathematical audit

## correctness

PASS

A restriction to selected positions retains at most one descent because the selected parts of the two increasing runs remain increasing. Failure on four positions for three comparisons and on six for four also excludes smaller supports of the indicated sizes by appending increasing largest entries. In the support graph a degree-three vertex gives three edges on four vertices; two nonadjacent degree-two vertices give four distinct edges on at most six vertices, while two adjacent degree-two vertices give three edges on at most four. Thus at most one vertex has degree two and all others have degree one after omitting isolates; k edges use at least 2k-1 sites. This shape is not sufficient, e.g. the support {(1,2),(2,3)} cannot realize two inversions. For the lower bound at n=2k-1, the record's value ordering realizes (1,k),(1,k+1) with labels 00,10,11 using the two runs split after k-1 and the paired blocks for the other queries; the exceptional 01 ordering puts k+1 before 1 in value and k last, moving the split to after k. Both constructions preserve increasing within-run order and give independent pair labels. Padding and the one-query case finish the dimension theorem. Independent permutation/trace enumeration and exact split recursion reproduced both finite obstructions and (VC,Ldim)=(1,1),(2,2),(2,3),(3,4),(3,5) for n=2–6; replay: python3 /workspace/branches/a287adc2-ab35-40f6-963b-a83bab29ccd7/independent_check.py (retained output independent_check.txt in the same directory). The original tree_n6.txt is present in the frozen directory despite not being listed among the initially attached code files. Replay: python3 /workspace/branches/independent_tree_1.py <frozen-directory>/tree_n6.txt; it verified all 31 query nodes and 32 legal distinct depth-five witnesses with correct labels. Every permutation except the identity gives one unique subset-then-complement presentation; the identity accounts for n+1 subsets, so 2^6-6=58 concepts exclude depth six. These checks settle the theorem and the first-gap claim; independent enumeration did not extend the auxiliary n=7,8 table. Frozen scripts were inspected but not executed.

## originality

PASS

The exact all-order VC dimension and six-site adaptive separation for this concept class are distinct on the inspected evidence. Credit the established class, its count, the fixed two-chain lower-bound mechanism and nearby results for other classes; do not infer historical priority.

## value

PASS

Exact complexity for a standard permutation class under natural positional comparisons is useful independently of enumeration. The hereditary support obstruction and the odd-order construction explain why changing the split matters. The exact first two-unit static/adaptive gap is an independently useful witness, not an arbitrary dimension table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
