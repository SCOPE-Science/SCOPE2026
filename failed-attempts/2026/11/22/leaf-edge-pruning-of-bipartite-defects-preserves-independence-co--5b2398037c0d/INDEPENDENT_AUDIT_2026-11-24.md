# Independent mathematical audit

## correctness

PASS

The mixed edge e={v,w} has cofaces exactly e∪T for T⊆N_F(w)∖{v}: the leaf cannot see another vertex across its shore, while the other endpoint sees exactly those additional neighbours. Fixing one of the d−1 extra neighbours as an apex pairs all 2^(d−1) cofaces including e; removing the pairs in descending order of the subset size makes each lower face free with precisely its designated codimension-one coface. The remaining subcomplex deletes exactly the faces forbidden by adding vw to H_F. Forest pruning preserves the number c of edge-containing components and reduces to a matching; the two contractible shore simplices then give S^0 for c=0 or two vertices with c joining edges after contraction for c≥1. Pendant pruning and failure of the deletion at a single isolated defect edge also follow.

## originality

FAIL

The fixed-shore deletion is directly covered by the general dominated-edge collapse of Boissonnat and Pritam; the specific pair count is forced by the number of deleted faces. The complete bipartite-forest homotopy classification is also explicitly present in the proof of earlier Resultary 636cc79caa35. This is demonstrated coverage, not a failure to retrieve literature.

## value

FAIL

The original would be useful as a worked example, but the scientific deliverables proposed as new are an immediate instance of the general dominated-edge criterion with an unavoidable face-count calculation and an already established forest classification. There is no surviving independently useful new invariant, strengthened hypothesis range, or sharper collapse bound in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
