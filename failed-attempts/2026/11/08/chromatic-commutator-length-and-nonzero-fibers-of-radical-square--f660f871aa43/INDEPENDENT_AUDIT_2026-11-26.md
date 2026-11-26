# Independent mathematical audit

## correctness

PASS

In A the vertex quotient is commutative and two arrows multiply to zero. For e:s→t each coefficient is (α_s−α_t)v_e−(β_s−β_t)u_e, and [e_s,e]=e. For r pairs, concatenating their diagonal coefficients gives q^(2r) possible labels; on a supported edge, an equal endpoint label would force zero. Conversely, for any proper support coloring with those labels, one differing diagonal coordinate supplies a nonzero coefficient in a local linear equation, so the arrow variables solve independently for the required targets. This includes the empty sum at zero and the width attained by taking all arrows nonzero. For a single pair unequal endpoints give q solutions per edge for every output, while equal endpoints give q² for zero and none otherwise. Expanding the extra factor on each nonsupported arrow contracts sets of forced equalities, retaining supported edges (including loops, which give zero colorings). This accounts for opposite/parallel arrows separately and uses field rank, not a prime-field assumption. Over F₂, K5 alone among its support subgraphs needs more than four colors: every proper subgraph allows a nonadjacent pair to share a color. Thus exactly the all-one target has length two. Orienting any graph by a total order preserves colorability; all arrows supported reduces 4-colorability to variable-input membership, and a proposed color assignment or bracket pair is a polynomial certificate. The reduction is not a fixed-algebra assertion. Ran python3 /workspace/reproductions/quivers.py: 140,969 ordered pairs in three cases over F₂,F₃,F₄, using path-basis multiplication and comparing all target populations with the contraction count, including mixed orientations/multiplicity. Example F₄ two opposite arrows: 7936 for zero and 3840 for each of the 15 nonzero targets. Independently checked all 1024 binary K5 supports and verified a two-bracket witness by multiplication. Uploaded verifier was inspected, not run; finite checks are not the universal proof.

## originality

FAIL

The indexed companion record b7fb936d5d53 states the same unrestricted length, width and full prescribed-fiber theorem on the same loopless multiquivers. This establishes exact equivalent coverage, not chronological priority between same-day entries. The earlier general zero fiber is independently established in the Nov. 2 adjoint-rank record. The genuinely different emphasis here, the binary K5 example and NP-completeness, is mechanically implied by the shared support-coloring characterization. Neither leaves a separately valuable claim to repair.

## value

PASS

The core theorem concerns natural width and elementwise distribution invariants, reveals exact support obstructions and gives a graph criterion for constructing commutator decompositions. That mathematical value is present in the shared result. Once the duplicate theorem is credited, the example and direct decision reduction do not support a separately valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
