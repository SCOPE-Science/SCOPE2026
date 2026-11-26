# Independent mathematical audit

## correctness

PASS

The m+5 edges form a connected tree on m+6 vertices; the gate v has degree four. Initially u adopts but v sees 1/4, so the original closure stops at three. Removing au or bu leaves u with one seed out of two neighbors. After u adopts, all admissible targets are enabled: v with exposure 2/5, x or y with 1/2, and internal/terminal path targets with 1/3 or 1/2, respectively. Propagation back to v gives 2/4 unless v was the target, and then onward to every other susceptible vertex. Removing bv leaves v with at most one adopter among four even after u adopts, so no path or leaf can be reached. The outcome is constant conditional on each of the three sampled edges, so the differing number of eligible targets per edge does not bias 2/3 versus 1/3; the mean is 5+2m/3. Independent finite replay: label a,b,u,v,x,y,w1,... by 0,1,2,3,4,5,6,...; enumerate edges (0,2),(1,2),(1,3), and all nonadjacent target labels >=2 other than the susceptible endpoint; after replacement repeatedly add the first enabled vertex using the exact integer test denominator(theta)*adopting_neighbors > numerator(theta)*degree. This checked 3000 rewiring/threshold combinations, m=1..20 at 1/4,3/10,333/1000,1/3; at 1/3 an internal path target fails, and static closure at 1/5 fills every test tree. Strictness and m=1 are handled analytically. Source code was inspected, not executed. Editorial: the stated quotient is mean/baseline; the phrase 'baseline-to-mean' inverts its label. The numerical quotient and mathematical amplification claim are correct. The degree-four and connectivity hypotheses apply to the original graph.

## originality

PASS

Best of knowledge: the closest inspected work already gives the elementary move and qualitative enhancement; it does not give the exact edge-conditioned law, unbounded one-replacement comparison, or universal target property on this tree family.

## value

PASS

Shows a fixed-degree originally connected family where just one locally homophilic replacement before adoption changes the scale of final adoption with probability bounded away from zero, irrespective of which admissible recipient is sampled in the successful cases. The quantitative separation between local suppression and global possible amplification is useful as a worst-case check on interpretation of random-network averages. This is not a statement about ordinary ongoing rewiring or realistic spread predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
