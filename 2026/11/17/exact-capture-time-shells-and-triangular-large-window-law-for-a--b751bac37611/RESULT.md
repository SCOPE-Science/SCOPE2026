# Exact capture-time shells and triangular large-window law for a non-bijective quarter-turn map

## Finding

For the planar, non-injective piecewise quarter-turn map
\[
T(x,y)=\begin{cases}(-y,x),&y<0,\\(1-y,x-1),&y\geq0,\end{cases}
\]
let \(G=(\mathbb Z\times\mathbb R)\cup(\mathbb R\times\mathbb Z)\) and let \(U=(0,1)\times((-1,0)\cup(0,1))\). For each \(z\notin G\), define \(\tau(z)=\min\{j\geq0:T^jz\in U\}\). Then \(\tau(z)\) is finite for every such \(z\), and an explicit finite-case formula below computes it exactly from the initial unit-square label. Once the orbit reaches \(U\), it remains there and satisfies \(T^4z=z\). Within \(U\), precisely the two points \((1/2,1/2)\) and \((1/2,-1/2)\) have least period two; every other point has least period four.

With \(\operatorname{area}\) denoting planar Lebesgue measure,
\[
\operatorname{area}\{z\notin G:\tau(z)=0\}=2,\qquad
\operatorname{area}\{z\notin G:\tau(z)=2k-1\}
=\operatorname{area}\{z\notin G:\tau(z)=2k\}=2k\quad(k\geq1).
\]
In particular, for \(|s|<1\), the area generating function is
\[
\sum_{t\geq0}\operatorname{area}\{\tau=t\}s^t
=2+\frac{2s(1+s)}{(1-s^2)^2}.
\]

If \(Z_R\) is uniform on \([-R,R]^2\), with \(R>0\), and \(V_1,V_2\) are independent uniforms on \([0,1]\), then
\[
W_1\!\left(\mathcal L(\tau(Z_R)/R),\mathcal L(2(V_1+V_2))\right)\leq\frac7R.
\]
Consequently \(\tau(Z_R)/R\) converges in law to a triangular distribution supported on \([0,4]\), with density \(s/4\) for \(0<s<2\) and \((4-s)/4\) for \(2<s<4\).

## Assumptions and scope

The switching line is \(y=0\), with the upper branch taken there. The lower and upper rotations both have angle \(\pi/2\), about centers \((0,0)\) and \((1,0)\), respectively. Thus this is a surjective, non-injective instance of the general two-half-plane piecewise-rotation family. The explicit first-entry theorem is asserted only off the integer grid \(G\); this is a full-Lebesgue-measure set, invariant under \(T\). No assertion about all grid-line points is needed. The first-entry times count individual applications of \(T\), not pairs of iterates. \(W_1\) denotes the usual Wasserstein-1 distance on the real line.

For integers \(m,n\), write \(S_{m,n}=(m,m+1)\times(n,n+1)\). Define the integer-square transition
\[
Q(m,n)=\begin{cases}(-n-1,m),&n<0,\\(-n,m-1),&n\geq0.\end{cases}
\]
The exact first-entry rank \(h(m,n)\), with no unspecified constants, is as follows:

| Integer-square condition | \(h(m,n)\) |
| --- | --- |
| \(n\geq1,\ m\leq-1\) | \(2(n-m)+1\) |
| \(n\geq1,\ m\geq0\) | \(2(n+m)\) |
| \(n=0,\ m\leq-1\) | \(-2m+1\) |
| \((m,n)=(0,0)\) | \(0\) |
| \(n=0,\ m\geq1\) | \(2m-1\) |
| \(n=-1,\ m\leq-1\) | \(-2m-1\) |
| \((m,n)=(0,-1)\) | \(0\) |
| \(n=-1,\ m\geq1\) | \(2m+1\) |
| \(n\leq-2,\ m\leq0\) | \(2(-m-n)-2\) |
| \(n\leq-2,\ m\geq1\) | \(2(m-n)-1\) |

The formula is \(\tau(z)=h(\lfloor x\rfloor,\lfloor y\rfloor)\) for \(z=(x,y)\notin G\).

## Proof

**Square transport.** In the lower half-plane the quarter-turn sends \(S_{m,n}\) onto \(S_{-n-1,m}\), and in the upper half-plane it sends \(S_{m,n}\) onto \(S_{-n,m-1}\). Therefore the full dynamics on the off-grid squares is exactly the integer map \(Q\), and the off-grid set stays off-grid.

**Strict first-entry ranking.** All ten rows in the table are nonnegative. Direct substitution into the two branches of \(Q\) proves
\[
h(Q(m,n))=h(m,n)-1\quad\text{if }(m,n)\notin\{(0,0),(0,-1)\},
\]
while \(Q(0,0)=(0,-1)\) and \(Q(0,-1)=(0,0)\). Here is an explicit partition check, including potential transitions across boundaries: when \(n\geq1,m\leq-1\), the image has labels \((-n,m-1)\), belongs to \(n'\leq-2,m'\leq0\), and has rank \(2(n-m)\); when \(n\geq1,m\geq0\), the image has labels \((-n,m-1)\), whose rank is \(2(n+m)-1\) in each of the three subcases \(m=0\), \(m=1\), \(m\geq2\). For \(n=0\), the three ranges \(m\leq-1\), \(m=0\), \(m\geq1\) give image ranks \(-2m\), \(0\), and \(2m-2\) respectively, except that the absorbing row \((0,0)\) is handled separately. For \(n=-1\), the ranges \(m\leq-1\), \(m=0\), \(m\geq1\) give image ranks \(-2m-2\), \(0\), and \(2m\), respectively; the \(m=-1\) case maps immediately to the absorbing row. For \(n\leq-2,m\leq0\), the image ranks are \(2(-m-n)-3\), separately using the image-table ranges \(m=0\), \(m=-1\), \(m\leq-2\). Finally, for \(n\leq-2,m\geq1\), the image rank is \(2(m-n)-2\). Thus every nonabsorbing square reaches the designated pair after exactly its rank many steps, with no earlier entry.

**Period on the absorbing squares.** Both squares are exchanged by \(T\). A direct calculation on each gives
\[
T^2(x,y)=\begin{cases}(1-x,1-y),&(x,y)\in S_{0,0},\\(1-x,-1-y),&(x,y)\in S_{0,-1}.\end{cases}
\]
Each map on the right is an involution, so \(T^4\) is the identity on \(U\). Since \(T\) exchanges the two squares, there can be no fixed points there. The only points fixed under \(T^2\) are the two displayed centers, proving the least-period statement.

**Exact shell areas.** The sets of labels of a given first-entry time are disjoint complete unit squares, so their areas equal their integer-label counts. Rank zero occurs only in the two absorbing labels. For the even time \(2k\), the conditions \(n\geq1,m\geq0,n+m=k\) give \(k\) labels; the conditions \(n\leq-2,m\leq0,-m-n=k+1\) give another \(k\). For the odd time \(2k-1\), the two unbounded-quadrant terms each contribute \(\max(k-2,0)\) labels, while the four axis-adjacent branches contribute two labels if \(k=1\) and four labels if \(k\geq2\). The sum is \(2k\) in every case. Summing \(2k(s^{2k-1}+s^{2k})\) proves the generating function, absolutely for \(|s|<1\).

**Large-window law with error.** Checking the ten rank cases gives the global inequality
\[
|h(m,n)-2(|m|+|n|)|\leq3.
\]
Since \(\bigl||\lfloor x\rfloor|-|x|\bigr|<1\) for noninteger \(x\), it follows pointwise off-grid that
\[
|\tau(x,y)-2(|x|+|y|)|\leq7.
\]
When \((x,y)=Z_R\), the two variables \(|x|/R\), \(|y|/R\) are independent uniform \([0,1]\). Coupling the two normalized capture times using this same point yields \(W_1\leq7/R\), and convolution of two uniform densities gives the stated triangular limiting law. This establishes both the finite-window bound and the limit without extrapolating any finite enumeration.

## Verification

The self-contained `check.py` uses exact rational coordinates to verify square transport and the four-step identity; exact integer operations check the rank recurrence and global rank-size bound for all labels in \([-250,250]^2\), and count both parity shells for \(1\leq k\leq80\). The checker terminates with `QUARTER_TURN_EXACT_LATTICE_AND_SHELL_CHECK_OK`. These bounded tests serve as consistency checks; the infinite assertions follow from the case-by-case algebra and counting above.

## Relationship to prior work

Bédaride–Bertazzon–Kaboré (arXiv:2202.13107v1, 2022), Definition 1 and Theorems 15 and 31, establish the piecewise-rotation family and general bounded-attractor bounds, including rational even-denominator rotations. They do not assert an exact off-grid first-entry rank, a full exact shell-area distribution, or a large-window limiting law for this canonical non-injective instance. The Boshernitzan–Goetz (2003) general attracting/repelling dichotomy is qualitative, not an exact capture-time census. Earlier results of Goetz (1998) and Bédaride–Kaboré (2018) treat differently positioned centers or bijective maps. Cimà–Gasull–Mañosa–Mañosas (2024) study an explicitly invertible piecewise rotation with unbounded periods, rather than a finite-time trapping two-square system.

## Limitations

Grid-line orbits are deliberately excluded from the global first-entry and least-period assertions. The triangular law concerns uniform sampling in centered expanding squares and does not claim a universal distribution for other sampling schemes. Each positive-time shell is a finite union of unit squares, although the total transient domain is unbounded. This theorem describes a particular normalized non-bijective quarter-turn configuration; it is not a classification of all angles or center placements. A general result in an inaccessible full text (Boshernitzan–Goetz 2003) could contain a specialized equivalent example, although its available abstract does not show the claimed formula; publication priority cannot be guaranteed by these searches alone.

## References

- N. Bédaride, J.-F. Bertazzon and I. Kaboré, *Piecewise rotations: limit set for the non-bijective maps*, arXiv:2202.13107v1 (26 February 2022); *Dynamical Systems* 38 (2023), 52–78. DOI: 10.1080/14689367.2022.2132917.
- M. Boshernitzan and A. Goetz, *A dichotomy for a two-parameter piecewise rotation*, *Ergodic Theory and Dynamical Systems* 23 (2003), 759–770. DOI: 10.1017/S0143385702001396.
- A. Goetz, *Dynamics of a piecewise rotation*, *Discrete and Continuous Dynamical Systems* 4 (1998), 593–608.
- N. Bédaride and I. Kaboré, *Symbolic dynamics of a piecewise rotation: Case of the non symmetric bijective maps*, arXiv:1705.05009v1 (2017), *Qualitative Theory of Dynamical Systems* 17 (2018).
- A. Cimà, A. Gasull, V. Mañosa and F. Mañosas, *On some rational piecewise linear rotations*, arXiv:2306.17543v1 (2023), *Journal of Difference Equations and Applications* 30 (2024), 1577–1589.
