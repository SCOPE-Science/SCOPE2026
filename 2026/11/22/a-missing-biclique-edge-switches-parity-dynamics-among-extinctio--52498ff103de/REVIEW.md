# Independent mathematical audit

## correctness

PASS

With both residual shores nonempty the four independent input functionals (the endpoint values and the residual sums) map bijectively to the four output cell values. Hence im B is precisely the four-cell-constant space and rank B^(t+1)=rank M^t. If both shores are even, the two off-diagonal blocks of M are H=[[0,1],[1,1]]. H^2+H+I=0, so M^3 swaps the shores, M^6=I and M^2 has no nonzero fixed vector because H^2-I is invertible. Thus the fixed-space dimensions for powers 1,2,3,6 are 0,0,2,4, ruling out period two and proving the stated counts. The minimal polynomial on this image is (t^2+t+1)^2 and the complement is killed in one step. If both shores are odd, the two blocks are J=[[0,0],[1,0]]; the ranks are N,4,2,0 and force two length-three nilpotent blocks and the zero singletons. In the mixed case, M^2 has the two rank-one idempotent blocks JH,HJ and M swaps their image lines. This gives J_2(1), while N,4,3,2,2,... forces one length-three nilpotent block and N-5 zero singletons. Kernel dimensions of the successive nilpotent powers give exactly the successive differences in the stated first-entry populations. The last relevant shell is nonempty except in even-even at m=n=2, and Fitting projection gives exactly q^(N-r) points per recurrent state, hence the stated basins. The intact operator A has rank two and A^3=(mn mod 2)A, with shore swap on its image if both shores are odd. These are finite-field statements for the synchronous loop-free update only.

## originality

PASS

The four-dimensional six-periodic companion block and its finite-field orbit census are already known; even the boundary m=n=2 is covered by Q2 with one edge removed. The original contribution is the graph-specific, complete three-phase classification under deletion of a biclique cross-edge, including the nilpotent filtration and basin shells throughout the two regimes not supplied by the known six-periodic block.

## value

PASS

A biclique is a natural uniform interaction graph and one cross-edge deletion is its smallest bipartite defect. The precise recurrence and transient invariants show a sharp change not captured by the already known universal six-periodic block: mixed parity produces primitive two-cycles, whereas odd-odd removes all nonzero recurrent behavior despite an unedited oscillatory module. The all-size, all-characteristic-two-field counts quantify these alternatives including their sharp entry times and basins. Value is in the complete phase classification, not a new general method for linear automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
