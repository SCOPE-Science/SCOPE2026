# An exact weighted-price transition in checkerboard lattice disk coverings

## Finding
Fix the integer square lattice in the Euclidean plane with nearest-neighbour distance one. Put closed disks of radius \(r\ge0\) at sites \((m,n)\) with even \(m+n\), and disks of radius \(s\ge0\) at sites with odd \(m+n\). For any \(s\ge0\), these disks cover the entire plane if and only if \(r\ge F(s)\), where
\[
F(s)=\begin{cases}
\sqrt{1-\sqrt2s+s^2},&0\le s\le1/\sqrt2,\\
(1-\sqrt{2s^2-1})/\sqrt2,&1/\sqrt2\le s\le1,\\
0,&s\ge1.
\end{cases}
\]
For any price ratio \(w>0\), minimize the weighted squared-radius expense \(J_w=r^2+ws^2\), per pair of opposite-parity sites, over *all* such coverings. Set \(c=1+w\). The only possible minimizers are the following two ordered configurations:
\[
\begin{array}{lll}
\text{A:}&s_1=1/(\sqrt2c),&r_1=\sqrt{1-c^{-1}+(2c^2)^{-1}},\\
\text{B:}&s_2=\sqrt{(1+c^{-2})/2},&r_2=(1-c^{-1})/\sqrt2.
\end{array}
\]
Their costs are \(E_1=1-(2c)^{-1}\) and \(E_2=(c-c^{-1})/2\). Hence the global optimum is B when \(0<w<1\), A when \(w>1\), and precisely A and B when \(w=1\). The optimized cost is continuous, but its derivative jumps from \(5/8\) (left) to \(1/8\) (right) at \(w=1\). At the equal-price point both distinct ordered optimal radius pairs have cost \(3/4\); restricting to equal radii instead costs at least \(1\).

## Assumptions and scope
Sites remain fixed at the full unit square lattice. The two periodic parity classes each occupy half the sites. Radii are uniform *within* each class, and costs are proportional to squared radius with a positive class price ratio. No optimization over alternative sensor locations, nonperiodic arrangements, or alternative cost exponents is claimed. The proof includes nonnegative radii and all values of \(s\), including zero and radii large enough to cover using one class alone. The two cost minimizers at \(w=1\) are distinct as *ordered parity-labelled* assignments and related by a unit lattice translation if labels are forgotten.

## Proof
Translate the lattice so that one class-B site is at the origin. Its nearest same-class sites are at \((\pm1,\pm1)\), and its Voronoi cell is the diamond \(D=\{(x,y):|x|+|y|\le1\}\). Every plane point has a representative in this cell under translations by the B sublattice, and its distance to the nearest B site equals its distance \(t\) to the origin. Symmetry reduces to the wedge \(x\ge y\ge0\), \(x+y\le1\). The nearest A site in this wedge is \((1,0)\), so the squared distance to class A is \(1-2x+t^2\).

At fixed \(t\in[0,1/\sqrt2]\), the smallest admissible \(x\) is \(t/\sqrt2\), attained on \(x=y\); consequently the largest squared distance to A at this B-distance is \(H(t)=1-\sqrt2t+t^2\). At fixed \(t\in[1/\sqrt2,1]\), the smallest admissible \(x\) lies on \(x+y=1\) and equals \((1+\sqrt{2t^2-1})/2\); now \(H(t)=t^2-\sqrt{2t^2-1}\). Both functions decrease strictly as \(t\) increases within their open intervals, and agree at the join. Thus among all points not inside any open B disk (i.e. \(t\ge s\)), the supremum of the distance to the A class equals \(\sqrt{H(s)}\) if \(s<1\). For \(s\ge1\), B disks already cover the plane. This proves the piecewise necessary-and-sufficient covering criterion, including its boundary values by closedness.

For \(s\in[0,1]\) the cheapest feasible choice has \(r=F(s)\). On the first interval the objective is \(J_w(s)=1-\sqrt2s+cs^2\), a strictly convex quadratic, with its unique minimum at \(s_1=1/(\sqrt2c)\) and cost \(E_1=1-(2c)^{-1}\). On the second interval \(J_w(s)=cs^2-\sqrt{2s^2-1}\); its derivative is \(2s[c-(2s^2-1)^{-1/2}]\), which changes sign exactly once, at \(s_2=\sqrt{(1+c^{-2})/2}\), from negative to positive. Its unique minimum is \(E_2=(c-c^{-1})/2\). For \(s>1\), the objective is at least \(w\), and the endpoint \(s=1\) is already included in the second interval; hence it cannot improve the minimum.

Subtracting gives \(E_2-E_1=(w-1)/2\), proving all global minimizer cases and their uniqueness within the two branches. Differentiating yields \(E_2'(w)=(1+(1+w)^{-2})/2\) and \(E_1'(w)=(1+w)^{-2}/2\); their values at \(w=1\) are \(5/8\) and \(1/8\). For equal radii, the square-lattice covering radius is \(1/\sqrt2\) (the center of a unit square is farthest from all sites); with \(w=1\), expense is therefore at least \(2(1/\sqrt2)^2=1\). Both competing optima have expense \(3/4\). All claims follow.

## Verification
The included `check_checkerboard.py` computes the piecewise threshold independently against a dense fundamental-cell grid and, for several price ratios, compares both analytical branch minima with independent bounded scalar minimization. It prints `CHECKERBOARD_FEASIBILITY_GRID_OK` and `CHECKERBOARD_WEIGHTED_TRANSITION_OK` when tests pass. These finite diagnostics cannot certify coverage of infinitely many points; the preceding Voronoi-cell argument is the proof. Requires Python 3, NumPy, and SciPy.

## Relationship to prior work
Abbas and Koutsoukos (2015; first public date 2014-09-17), *Efficient Complete Coverage Through Heterogeneous Sensing Nodes*, derive one branch of the present checkerboard feasibility curve for a labelled larger-radius class (their configuration X) and explicitly optimize its *equal-price* energy, obtaining the \(\sqrt{5/8}\) large radius and its companion small radius. Neither that benchmark nor the underlying grid design is claimed as new. Their Section V identifies generalized cost models as a future direction. The mathematical contribution here is the complete two-branch, all-nonnegative-radius criterion **under arbitrary positive unequal class prices** and its exact globally optimized price diagram, including the discontinuous change of selected parity-labelled design. The triangular-lattice mixed-radius price law is geometrically different: its index-three sublattice gives different feasibility and a different critical price. An indexed equal-radius two-disk covering of well-rounded flat tori optimizes centers rather than fixed checkerboard parity radii, and does not imply this weighted phase law.

## Limitations
This is a fixed-lattice classification, not a global optimum among all disk arrangements. The fixed-lattice equal-price minimizer and part of the feasibility boundary were previously established, and are used as context only. Novelty of the weighted full phase diagram is assessed relative to accessed literature and indexed statements; unindexed equivalent results cannot be ruled out. No independent audit has been performed.

## References
1. W. Abbas and X. Koutsoukos, *Efficient Complete Coverage Through Heterogeneous Sensing Nodes*, IEEE Wireless Communications Letters 4(1), 14–17 (2015), first published online 2014-09-17, doi:10.1109/LWC.2014.2358631; lawful full text: https://cs.vuse.vanderbilt.edu/koutsoxd/www/Publications/06901219.pdf .
2. F. Tóth, *Covering the plane with two kinds of circles*, Discrete & Computational Geometry 13 (1995), 445–447 (cited by reference 1; potential general covering comparator, not asserted full-text inspected).
3. R. Kershner, *The number of circles covering a set*, American Journal of Mathematics 61 (1939), 665–671 (classical equal-radius global baseline).
