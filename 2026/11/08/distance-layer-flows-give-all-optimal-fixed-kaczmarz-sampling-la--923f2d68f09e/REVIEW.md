# Independent mathematical audit

## correctness

PASS

For every graph and anchor set A, v_x=1+sqrt(2)d(x,A)>0 and every normalized anchor/edge measurement has squared inner product with v at most one. Thus Rayleigh yields λ_min M≤1/S. A breadth-first rooted forest supplies positive subtree masses H_x and probabilities p_a=H_a/S, p_edge=sqrt(2)H_x/S, normalized because each node contributes v_x(1+sqrt(2)d_x)=v_x² to the sum. Direct balance gives Mv=v/S. Since M has nonpositive off diagonal entries, D(M−S^(-1)I)D is a weighted graph Laplacian when D=diag(v), hence positive semidefinite. Equality in Rayleigh removes all same-distance edges, and eigenvector equations are exactly the nonnegative downhill layer flow balances and anchor formulas; all solutions are valid and normalize automatically. A vertex with two closer neighbors gives two distinct BFS forest choices with positive weights, while unique predecessor fixes every balance; this proves iff uniqueness. Independent numerical eigenchecks on path4, C4, K3, K4 with multiple anchors verified λ_min=1/S and the uniqueness criterion.

## originality

PASS

Earlier exact path-endpoint optimizer theorem is a strict instance of the all-graph potential and flow law; 2015 Gower–Richtárik supplies abstract randomized Kaczmarz/SDP machinery but not universal explicit graph distance potential, complete face and graph predecessor uniqueness. Previously indexed inverse-positive SPD coordinate designs apply to square systems, whereas this includes redundant cycles and multiple anchors. The new all-graph classification is not obtained by relabeling those settings.

## value

PASS

Complete exact characterization of the entire optimizer face over any connected graph, a closed graph-distance formula for the best Kaczmarz one-step contraction and a linear-time BFS construction solve a natural algorithmic design problem; flow nonuniqueness on graphs with cycles is a motivated structural phenomenon, not a narrow numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
