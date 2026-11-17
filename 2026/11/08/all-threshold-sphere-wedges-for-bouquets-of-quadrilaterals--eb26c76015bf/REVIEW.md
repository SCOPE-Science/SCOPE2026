# Independent mathematical audit

## correctness

PASS

An induced independence number for a v-free subset is sum_i max(e_i,epsilon_i), while adjoining v takes the maximum with 1+sum epsilon_i. Matching v-free S to S+v whenever legal leaves exactly k-1 selected middle vertices and local endpoint states 0,a,c. The subsequent earliest a_i toggle removes all residual faces except one critical 0-cell and C(m,k-1) critical (2k-3)-cells. The directed-Hasse acyclicity proof controls arrows across v and B strata and inside each selected-middle-index block: c-states cannot grow and the first non-c a-toggle has one-way orientation. This is an all-m,k proof of the integral wedge by Forman. I inspected the independent induced-subgraph DP and complete Hasse sort in verify.py, and the recorded 30 finite cases including m=6,k=6 have expected critical counts; those tests are not the infinite proof.

## originality

PASS

Best-of-knowledge PASS for the k>=4 vertex-bouquet integral classification. The closest edge-glued/corner-glued square sequences do not include one-vertex bouquets with cut vertices; the indexed broad connected-bipartite wedge theorem only concerns the third threshold.

## value

PASS

All-threshold integral wedge classification on a canonical cut-vertex family at k>=4 includes a sharp contractible/noncontractible threshold and closed binomial count, where known square-sequence constructions do not apply. A globally acyclic symbolic matching gives structural understanding useful for vertex-glued graph complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
