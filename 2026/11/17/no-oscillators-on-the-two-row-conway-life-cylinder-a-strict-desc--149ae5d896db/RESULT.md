# No oscillators on the two-row Conway Life cylinder: a strict descent potential and exact still-life spectrum

## Finding
For every integer \(n\ge3\), consider synchronous Conway B3/S23 updating on two rows and \(n\) labelled cyclic columns, with dead cells immediately beyond the two horizontal boundary rows. Write \(F_n\) for the map and, for a configuration \(x\), let \(S(x)\) be its number of columns containing exactly one live cell and \(D(x)\) the number containing two live cells. The integer
\[
\Phi_n(x)=(n+1)S(x)+D(x)
\]
strictly decreases under every nontrivial update:
\[
F_n(x)\ne x\quad\Longrightarrow\quad\Phi_n(F_n(x))<\Phi_n(x).
\]
Consequently every configuration becomes fixed within \(n(n+1)\) synchronous updates. In particular, no temporal periodic orbit of least period exceeding one exists on any such two-row cylinder. The same fixation conclusion holds for configurations with finite support on the infinite, vertically open, two-row strip.

The least number of vertically open rows capable of sustaining nonconstant temporal periodic behavior is **three**: the three-row cylinder with four columns contains a primitive temporal two-cycle, explicitly exhibited below. Thus this is an exact boundary between fixation and oscillation, not a finite-size extrapolation.

In addition, let \(s_n\) count labelled fixed configurations on the two-row cylinder. Define the four column symbols \(A=\{0,1,2,3\}\), with binary bits representing the two cells, and let \(q(a)\) denote the bit count. Define the new-column function \(H(a,b,c)\) by applying Life independently to the two bits of \(b\), each having \(q(a)+q(c)\) neighbors in the adjacent columns plus the other bit of \(b\). Let the \(16\times16\) integer matrix \(T\) be
\[
T_{(a,b),(b',c)}=\mathbf 1_{\{b=b'\}}\mathbf 1_{\{H(a,b,c)=b\}}.
\]
Then, for every \(n\ge3\),
\[
s_n=\operatorname{tr}(T^n),\qquad
\det(I-zT)=1-z-5z^3+4z^4-4z^5+4z^6.
\]
Equivalently the *transfer-walk* zeta series \(\exp(\sum_{n\ge1}\operatorname{tr}(T^n)z^n/n)\) equals the reciprocal of that polynomial. The first six physically defined counts, for \(n=3,4,5,6,7,8\), are \(16,5,26,82,43,213\). No assertion about distinct-neighbor physical cylinders of circumferences one or two is made.

## Assumptions and scope
The neighborhood is the usual eight-site Moore neighborhood in the square lattice, intersected with the two-row strip and horizontally identified modulo \(n\); cells outside the top and bottom rows remain dead. Since \(n\ge3\), left and right columns are distinct. An unoccupied cell is born exactly at three live neighbors. An occupied cell survives exactly at two or three live neighbors. Updating is simultaneous. The width-three witness has the same horizontal periodic and vertically dead convention. Configurations and fixed points are counted as labelled, not modulo rotation.

## Proof
Put \(u_i\in\{0,1,2\}\) for the number of occupied cells in column \(i\), and \(v_i=u_{i-1}+u_{i+1}\). For a currently empty column, both cells are born if and only if \(v_i=3\); otherwise both remain empty. For a full column, both survive if and only if \(v_i\in\{1,2\}\); otherwise both die. For a singleton column, the current live bit has \(v_i\) live neighbors, and the current dead bit has \(v_i+1\) live neighbors. Hence a singleton updates to a full column for \(v_i=2\), remains the *same* singleton for \(v_i=3\), and becomes empty otherwise. In particular, a singleton column can never be created.

Therefore \(S(F_n(x))\le S(x)\). If the inequality is strict, the boundedness \(0\le D\le n\) gives
\[
\Phi_n(F_n(x))-\Phi_n(x)\le-(n+1)+n=-1.
\]
If instead \(S(F_n(x))=S(x)\), every singleton survives unchanged, so each singleton has two neighbor occupancies summing to three. Since each occupancy is in \(\{0,1,2\}\), those neighbors have occupancies exactly one and two, in some order. In particular, no empty column is adjacent to any singleton column. A birth in an empty column would require its two neighbor occupancies to be one and two, contradicting that fact. Thus no empty column gives birth, and full columns can only remain full or become empty. The singleton columns remain unchanged. Consequently if the configuration changes, \(D\) strictly decreases, and so does \(\Phi_n\). This proves strict descent in all cases.

The potential is a nonnegative integer bounded above by \(n(n+1)\), because there are at most \(n\) nonempty columns and \(\Phi_n=(n+1)S+D\le n(n+1)\). Thus after at most \(n(n+1)\) changes an equilibrium is attained. In any temporal periodic orbit the potential must remain unchanged; strict descent therefore forces a fixed point. For the infinite two-row strip begun with finite support, all configurations have finite support at every finite time by locality, and the lexicographically ordered pair \((S,D)\) strictly decreases at any nonfixed update. There can be only finitely many decreases of the first coordinate and finitely many decreases of the second coordinate between them, proving finite-time fixation without claiming the same uniform bound.

For a one-row strip, no dead cell has more than two live neighbors, so no births occur and occupancy is monotone nonincreasing. Therefore that width also has no temporal oscillators. On the three-row, four-column cylinder, start with live cells exactly at the middle-row columns \(1,2,3\) (columns indexed \(0,1,2,3\)). Its successor has live cells exactly at the three row positions of column \(2\); the next successor returns to the initial state. The two configurations are distinct, proving the sharp width-three onset.

Finally the fixed-column constraint is local in three consecutive four-valued column symbols. Every labelled fixed configuration of circumference \(n\ge3\) determines a unique length-\(n\) closed walk on the pair-state graph \((a,b)\to(b,c)\), and conversely every such closed walk determines one fixed configuration. This proves \(s_n=\operatorname{tr}(T^n)\). Forming the sixteen-state integer matrix directly from the stated local rule and using the exact Newton identities on \(\operatorname{tr}(T),\ldots,\operatorname{tr}(T^{16})\) gives \(\det(I-zT)=1-z-5z^3+4z^4-4z^5+4z^6\). The associated formal determinant-zeta identity follows from \(-\log\det(I-zT)=\sum_{n\ge1}\operatorname{tr}(T^n)z^n/n\) as an identity of power series.

## Verification
The standalone file `verify.py` uses two distinct update implementations: direct per-cell Moore-neighbor counting and a separate column formula. They agree on all \(87{,}360\) two-row binary configurations for the six ring lengths \(3\le n\le8\). On every tested transition, the strict integer potential inequality holds unless the state is unchanged. Independently, a 16-state transfer matrix is constructed and its determinant computed entirely with integer matrix multiplication and Newton identities, producing coefficients \((1,-1,0,-5,4,-4,4,0,\ldots,0)\). Traces equal brute-force still-life counts for each tested circumference. A direct width-three simulation verifies the distinct pair \(224\leftrightarrow1092\) on three rows and four columns (row-major bits). The recorded output is `verify_output.json`. Finite verification corroborates rather than replaces the all-length descent proof.

## Relationship to prior work
Gardner's 1970 presentation of Conway's Life provides the original B3/S23 update, not a two-row cylinder fixation theorem. The well-known blinker gives the classical three-row oscillatory mechanism. Buckingham and Callahan (1998) construct finite Life oscillators with large periods, chiefly via glider reflectors and loops; the accessible author-uploaded text concerns general planar constructions, not a two-row, vertically open cylinder or this descent potential. Published bounded-grid documentation distinguishes finite cylinders from vertical periodic tori. The elementary three-row blinker gives the adjacent-width existence bound, but does not imply the width-two all-period exclusion or the width-two fixed-state determinant. Transfer-matrix counting is standard; the new mathematical content is the strict potential and the resulting sharp geometry threshold, together with its exact all-length census.

## Limitations
The cylinder has vertically *dead* boundaries, not a torus, and the claim does not assert fixation for arbitrary two-dimensional Life configurations or for infinite two-row configurations of infinite support. The convergence upper bound is valid but not claimed sharp. Physical circumferences below three require special boundary conventions and are excluded. The published historical-priority search is not exhaustive: the full 1998 oscilliator article is represented in available extracted text with incomplete theorem text, so possible older narrow-strip work remains a residual risk. Independent mathematical audit has not been performed.

## References
1. M. Gardner, "Mathematical Games: The fantastic combinations of John Conway's new solitaire game 'life'," *Scientific American* 223 (1970), 120–123, publication date 1970-10-01, doi:10.1038/scientificamerican1070-120; https://www.scientificamerican.com/article/mathematical-games-1970-10/ .
2. D. J. Buckingham and P. B. Callahan, "Tight Bounds on Periodic Cell Configurations in Life," *Experimental Mathematics* 7 (1998), 221–241, doi:10.1080/10586458.1998.10504370; author-uploaded extracted text https://www.researchgate.net/publication/2805751_Tight_Bounds_on_Periodic_Cell_Configurations_in_Life .
3. LifeWiki, "Bounded grids," https://conwaylife.com/wiki/Bounded_grid ; "One-cell-thick pattern," https://conwaylife.com/wiki/One-cell-thick%20pattern (reference for classical blinker context).
