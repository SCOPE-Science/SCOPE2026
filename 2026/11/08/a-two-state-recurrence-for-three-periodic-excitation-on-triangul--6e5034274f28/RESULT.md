# A two-state recurrence for three-periodic excitation on triangular cactus chains

## Finding
For each integer \(m\geq 1\), let \(T_m\) be the **chain triangular cactus** with vertices \(x_0,x_1,\ldots,x_m,y_1,\ldots,y_m\): for every \(1\leq j\leq m\), the three vertices \(x_{j-1},x_j,y_j\) form a triangle, and there are no other edges. Thus consecutive triangles meet in one vertex, nonconsecutive triangles are disjoint, and \(T_m\) has \(2m+1\) vertices.

Under synchronous threshold-one, three-state Greenberg–Hastings excitation, the exact number \(N_m\) of *initially primitive period-three configurations* on these labelled vertices is
\[
N_1=6,\qquad N_2=24,\qquad N_m=4N_{m-1}+N_{m-2}\quad(m\geq3).
\]
Equivalently,
\[
\sum_{m\geq1}N_m z^{m-1}=\frac{6}{1-4z-z^2}.
\]
The first six values are \(6,24,102,432,1830,7752\). The all-resting state is the unique fixed configuration, and the number of distinct primitive temporal three-cycles equals \(N_m/3\). Moreover,
\[
N_m=\left(3+\frac6{\sqrt5}\right)(2+\sqrt5)^{m-1}
+\left(3-\frac6{\sqrt5}\right)(2-\sqrt5)^{m-1},
\]
so the exponential growth factor per triangle is \(2+\sqrt5=\varphi^3\), the cube of the golden ratio \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
The graph is finite, undirected, simple, with the stated vertex names and edges; vertices are **distinguishable** and temporal phases are all counted. Each vertex is in state \(0\) (rest), \(1\) (excited), or \(2\) (refractory). The simultaneous map \(F\) obeys \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) if and only if at least one neighbor is currently in state \(1\); otherwise \(0\mapsto0\). A configuration has initially primitive period three if \(F^3(c)=c\) and \(F(c)\neq c\), with no transient steps. The claim concerns period-three states only, not eventual basins or other periods.

## Proof
**1. Characterize primitive three-cycles.** At a single vertex of any \(F^3\)-fixed state, either the vertex stays at \(0\) for all three times or it advances exactly through the three states, in cyclic order. Indeed, the transitions \(1\to2\to0\) are compulsory, and for a vertex to return to \(1\) after three steps it must perform \(0\to1\) on the third step; the same argument applies after time shifts. Any permanently resting vertex cannot have an advancing neighbor: such a neighbor would be excited at one of the three times and would excite it. Because \(T_m\) is connected, a nonfixed three-periodic configuration therefore has *every* vertex advancing.

An initial phase assignment \(c:V(T_m)\to\mathbb Z/3\mathbb Z\) makes every vertex advance at every step if and only if each vertex \(v\) has a neighbor of initial phase \(c(v)+1\pmod3\). Necessity follows by considering the time when \(v\) is resting. Sufficiency follows because all phases are then incremented simultaneously at each step, preserving this local successor-neighbor condition. Thus our count is exactly the number of such successor-supported phase assignments.

**2. First triangle.** Process triangles left to right, retaining the color of the last connector \(x_j\) and a Boolean flag \(s\), which records whether \(x_j\) has a successor-phase neighbor *within the already processed triangles*. At the first triangle, the left connector \(x_0\) and private vertex \(y_1\) must both be supported within the triangle. For each fixed color of \(x_1\), there is exactly one choice of \((c(x_0),c(y_1))\) giving \(s=0\) and exactly two giving \(s=1\). The three choices of color for \(x_1\) give the initial row vector
\[
 v_1=(3,6).
\]

**3. Attach one triangle.** For a fixed old connector color \(a=c(x_{j-1})\), old support flag \(s\in\{0,1\}\), new connector color \(b=c(x_j)\), and new private color \(y=c(y_j)\), let \(U_a,U_b,U_y\) mean that the respective vertex has a successor-colored neighbor in this *new triangle*. The extension is valid exactly when \(U_y=1\) and \(s\lor U_a=1\); the new support flag is \(U_b\). Rotating all three colors does not change any condition, so fix \(a=0\). Exhaustively listing the nine ordered pairs \((b,y)\in\{0,1,2\}^2\) yields the transition table
\[
R=\begin{pmatrix}1&2\\2&3\end{pmatrix},
\]
whose rows are old support flags \(0,1\) and columns are new support flags \(0,1\). More explicitly, for old flag \(0\), the valid extensions with new flag \(0\) and \(1\) occur respectively \(1\) and \(2\) times; for old flag \(1\), they occur respectively \(2\) and \(3\) times. This is a finite direct case analysis, also independently enumerated by `check_transfer.py`. Each extension finalizes all previous vertices and the old connector, leaving only the new connector to be tested in a future triangle.

For the final connector \(x_m\) there is no future triangle, so its support flag must be \(1\). Hence, with \(e_1=(0,1)^{\mathsf T}\),
\[
N_m=(3,6)R^{m-1}e_1\quad(m\geq1).
\]
There is no quotient by graph automorphisms or time shifts.

**4. Recurrence and fixed states.** Direct multiplication gives \(R^2=4R+I\), so \(N_{m+2}=4N_{m+1}+N_m\); the initial vector gives \(N_1=6\) and \(N_2=24\). Summing this recurrence produces the stated generating function, and diagonalizing \(R\), whose eigenvalues are \(2\pm\sqrt5\), gives the closed expression. On a connected graph, a state fixed by \(F\) cannot contain \(1\) or \(2\), since these advance automatically. Hence the all-zero state is the only fixed state. Because every nonfixed \(F^3\)-fixed state has least period exactly three, the orbits counted by \(N_m\) have three phases, proving the orbit formula.

## Verification
Two independently written Python-standard-library programs accompany this proof. `check_transfer.py` independently enumerates the nine local pairs for both flag values, checks the reduced \(2\times2\) transfer against a complete six-state (three-color, two-flag) transfer for all \(1\leq m\leq100\), verifies the recurrence, and checks divisibility by three. `check_dynamics.py` constructs the labelled graph and directly applies the synchronous three-state update to **every** state for \(1\leq m\leq5\), a total of \(199287\) states, confirming exactly one fixed point and the predicted primitive-three populations. The commands are `python3 check_transfer.py` and `python3 check_dynamics.py`; neither requires third-party packages. Their captured standard outputs are included. These finite computations corroborate the exact all-\(m\) argument above; the transfer construction and matrix identity are the infinite proof.

## Relationship to prior work
The threshold-one Greenberg–Hastings model and its periodic excitation mechanisms were studied by Durrett and Griffeath (1993). Gravner, Lyu, and Sivakoff (preprint 2016, publication 2018) establish broad circulation/activity criteria on arbitrary finite graphs, including the distinction between eventual synchronization and persistent excitation. Their criteria do not give the number of *initially primitive three-periodic* configurations in a chain triangular cactus or the transfer matrix above.

Borissevich and Došlić (2015) study this same **chain triangular cactus graph** and derive a different recurrence for ordinary dominating subsets; those subsets do not encode a partition of all vertices into three temporal phases with cyclic successor support. Their stated recurrence \(t_m=3t_{m-1}+2t_{m-2}\) for dominating sets therefore neither equals nor determines the count here. The graph family has a fixed number of triangles and vertices for each length, but its linear chain attachment pattern affects the dynamical phase census differently from a triangle bouquet with the same elementary sizes.

## Limitations
This result concerns only the finite chain triangular cacti \(T_m\), the specified three-state threshold-one dynamics, and configurations periodic from the start with primitive period three. It does not classify longer or transient trajectories, arbitrary cactus branching patterns, other excitation thresholds, or other state alphabets. Independent mathematical/literature validation has not been performed; unindexed publications, alternative combinatorial formulations (including cyclic total-domination colorings), or implicit specializations of broader results may affect historical priority. The conclusion does not assume that unsuccessful database searches prove novelty.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (arXiv:patt-sol/9303002), submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv:1610.07320), first version 2016-10-24; *Annals of Applied Probability* **28** (2018), 3324–3357, DOI:10.1214/17-AAP1350. Author-available full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
3. K. Borissevich and T. Došlić, *Counting Dominating Sets in Cactus Chains*, *Filomat* **29** (2015), 1847–1855, DOI:10.2298/FIL1508847B, https://www.pmf.ni.ac.rs/filomat-content/2015/29%20-%208/29-8-16-871.pdf .
