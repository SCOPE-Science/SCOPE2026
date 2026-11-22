---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

This result has only self-review. For each of two graph models there are exactly 20 vertices, three simple neighbors per vertex and 1,048,576 configurations. `nor20.cpp` computes the full functional graph and peels every nonrecurrent state; the 1,008,621 / 1,013,607 transient totals and all fixed and two-cycle orbit counts are verified by that algorithm. `nor20_verify.py` constructs the same graphs using adjacency sets and a distinct vectorized update rule, tests \(F^3=F\) on every configuration, and computes fixed-attraction totals plus all basin multiplicities through recurrent representative fibers. These checks reproduce the C++ census tables, including basin maxima 35 / 388 and the two sizes 156,533 / 150,545 for the all-zero/all-one two-cycles. The two shore fixed states of the bipartite graph have explicit mask identifiers 349866 and 698709 in the declared vertex ordering, each with 388 preimages; exact subset-size counts add to 388.

## Reproduce

`g++ -std=c++17 -O3 nor20.cpp -o nor20`

`./nor20 2` and `./nor20 3` (stdout comparison against `dodecahedral_census.txt` and `desargues_census.txt`)

`python3 nor20_verify.py` (requires NumPy; stdout comparison against `vectorized_check.txt`)

Each program must terminate normally. An optional graph-isomorphism sanity check against canonical dodecahedral and Desargues graph models was performed with NetworkX; it is not required to reproduce the state-space enumerations.

## Limits

Exactness is finite on the two named graphs; neither code nor its logs prove novel priority. The general identity \(F^3=F\) is proved on paper and verified here, not claimed original. There has been no independent external scientific audit.
