# Range-two excitation changes sparse ring resonances into exponential primitive-three populations

## Finding
For each integer \(n\ge5\), let \(G_n=C_n^2\) be the square of the labelled cycle: its vertices are \(\mathbb Z/n\mathbb Z\), with \(i\) adjacent to \(i\pm1\) and \(i\pm2\). On \(G_n\), apply synchronous three-state, threshold-one Greenberg–Hastings dynamics. Let \(P_n\) count initial configurations of **least temporal period three**.

Set \(f(X)=X^3-3X^2+2X-2\) and \(g(X)=X^4+X^3+2X^2+3X+4\). Then for all \(n\ge5\), counting roots with algebraic multiplicity,
\[
P_n=(-1)^n+\sum_{f(\alpha)=0}\alpha^n+2\sum_{g(\beta)=0}\beta^n.
\]
In particular, \(P_5,P_6,P_7,P_8,P_9,P_{10},P_{11},P_{12}\) are \(150,270,588,1548,4092,10710,26400,65574\). Let \(\rho\in(2,3)\) be the unique real root of \(f\), numerically \(\rho=2.521379706804\ldots\). Then
\[
P_n=\rho^n+O(2^n),\qquad \frac{P_n}{3^n}\sim\left(\frac\rho3\right)^n.
\]
All \(n\ge5\) have \(P_n>0\), and the number of distinct three-state orbits is exactly \(P_n/3\). In contrast, with only nearest-neighbor edges on \(C_n\), the initial primitive-three population is exactly \(6\) when \(3\mid n\) and \(0\) otherwise. Thus adding next-nearest-neighbor connections changes bounded arithmetic resonance into exponential proliferation, while the fraction of all colorings that are initially periodic still decays exponentially.

## Assumptions and scope
Every vertex has a state in \(\{0,1,2\}\). At one update \(U\), the state \(1\) becomes \(2\), \(2\) becomes \(0\), and \(0\) becomes \(1\) if and only if at least one adjacent vertex is currently in state \(1\); otherwise it stays \(0\). All vertices update simultaneously. Explicitly,
\[
P_n=|\{x\in\{0,1,2\}^{\mathbb Z/n\mathbb Z}:U^3x=x,\ Ux\ne x\}|.
\]
The labels around the cycle are fixed, and rotated or color-shifted configurations are not identified. The restriction \(n\ge5\) ensures that \(i\pm1,i\pm2\) are four distinct neighbors. No statement is made about other possible temporal periods or transient basins.

## Proof
**1. Local condition for primitive period three.** In a three-step periodic trajectory, at a given vertex either all three updates leave it at state \(0\), or it advances at every step through the three colors. Indeed, the forced transitions \(1\to2\to0\) leave no other three-step closed temporal word. If a vertex is always \(0\), none of its neighbors can be advancing: an advancing neighbor visits state \(1\) once every three steps and would excite the fixed vertex. As \(G_n\) is connected, a nonfixed three-periodic state has *every* vertex advancing. Conversely, an initial coloring \(x\) advances everywhere forever if each vertex \(i\) has a neighbor \(j\) with \(x_j\equiv x_i+1\pmod3\). At its unique resting step the neighbor is then excited, and the same relation remains true after every uniform color shift. Consequently the exact primitive-three condition is
\[
\forall i\in\mathbb Z/n\mathbb Z,\quad
\exists j\in\{i-2,i-1,i+1,i+2\}:x_j\equiv x_i+1\pmod3.
\]
There are no hidden fixed states in this count: the only globally fixed coloring of a connected graph is the all-resting state, which fails this condition.

**2. Closed transfer walks.** Index an \(81\)-dimensional integer matrix \(T\) by four-letter words \((a,b,c,d)\in\{0,1,2\}^4\). Its only potential nonzero transitions are
\[
T_{(a,b,c,d),(b,c,d,e)}
=\mathbf1\bigl\{\text{at least one of }a,b,d,e\text{ equals }c+1\pmod3\bigr\},
\]
for \(e\in\{0,1,2\}\). For \(n\ge5\), a closed length-\(n\) walk in this transfer graph corresponds bijectively to a labelled cyclic coloring obeying the local condition: each step tests the central vertex using exactly its four neighbors. Therefore \(P_n=\operatorname{tr}(T^n)\).

**3. Exact characteristic computation.** The integral matrix just defined satisfies the polynomial identity
\[
\det(XI_{81}-T)
=X^{69}(X+1)f(X)g(X)^2.
\]
This is an *exact finite integer computation*, not an inference from fitted counts. The standalone program `verify/transfer.py` constructs all \(81\) rows from the displayed indicator, computes and factors the characteristic polynomial using exact symbolic integer arithmetic, and independently compares traces against Newton power sums for lengths \(5\) through \(18\). Its complete captured output is `verify/transfer.out`. The standard trace-eigenvalue identity applied to this factorization yields the asserted formula, including algebraic multiplicities. It is valid for every \(n\ge5\), not only the finitely tested lengths.

**4. Strict exponential separation.** The discriminant of \(f\) is \(-104\), so \(f\) has one real root and one conjugate pair. Since \(f(2)=-2\) and \(f(3)=4\), the real root \(\rho\) lies strictly between \(2\) and \(3\). The product of the three roots is \(2\), so the conjugate roots have common modulus \(\sqrt{2/\rho}<1\). Every root of \(g\) has modulus at most \(2\): after substituting \(X=2z\), its coefficients in ascending degree are \((4,6,8,8,16)\), which are nondecreasing; the elementary Eneström–Kakeya bound gives \(|z|\le1\). Hence all contributions other than \(\rho^n\) are \(O(2^n)\), proving both asymptotics. Positivity for every \(n\ge5\) also follows constructively: the cyclic coloring \(x_i\equiv i\pmod3\) satisfies the neighbor test, including the wraparound vertices, because a successor appears within two steps to at least one side.

**5. Nearest-neighbor comparison.** On \(C_n\) with only edges \(\{i,i\pm1\}\), each vertex of a primitive-three coloring must receive the successor color from at least one adjacent vertex. An edge supplies that successor relation at at most one of its endpoints. With \(n\) vertices and \(n\) edges, all edges must supply exactly one endpoint, yielding a consistently oriented directed cycle. The colors therefore advance by \(+1\) or \(-1\) around the ring; this closes exactly when \(3\mid n\), with three shifts for each orientation. The nearest-neighbor count is thus \(6\) or \(0\) as claimed.

## Verification
The exact transfer program checks the displayed \(81\)-state characteristic factorization and, by a separate dynamic-programming trace calculation, checks the root-power formula for each length \(5\le n\le18\). The separate direct-simulation program enumerates all \(3^n\) configurations for \(5\le n\le11\), tests \(U^3x=x\ne Ux\), and compares each answer with the local neighbor criterion. It also exhaustively checks the nearest-neighbor count for \(3\le n\le12\). Both programs were executed from the files provided in this package, and their actual outputs are supplied alongside them. The complete infinite-length assertion depends on the transfer bijection and exact characteristic identity, **not** on extrapolation from finite enumeration.

## Relationship to prior work
Greenberg and Hastings (1978) introduced the excitable-medium model. Durrett and Griffeath (1993, publicly posted March 22) investigated its behavior as neighborhood range and threshold vary, chiefly in lattice scaling and spiral formation. Gravner, Lyu and Sivakoff (preprint October 24, 2016; open-access published version 2018) proved general circulation and synchronization results for three-color excitation on graphs (notably their Theorem 3). Those results concern long-run activity and topological persistence and do not state this finite ring-square primitive-three population or its characteristic polynomial. The open second-power *path* has a three-term primitive-three counting recurrence with the same cubic \(f\); closing that path to a ring is not a direct specialization, and the present exact formula contains an additional doubled quartic spectral correction. The range-one ring comparison is explicitly proved here rather than inferred from the general activity criterion.

## Limitations
Only initially primitive-three states on labelled finite graphs \(C_n^2\), \(n\ge5\), are classified. The asymptotic constant and error term count states, not all eventual oscillatory basins. The \(81\)-state determinant is certified by supplied executable exact computation; a shorter hand calculation of its factorization is not claimed. Some older foundational full texts were not fully accessible, so historical priority remains qualified. No independent audit or third-party validation is claimed.

## References
Greenberg, J. M. and Hastings, S. P., "Spatial Patterns for Discrete Models of Diffusion in Excitable Media," SIAM J. Appl. Math. 34 (1978), 515–523. DOI: 10.1137/0134040 (publication month known; exact day not assumed).

Durrett, R. and Griffeath, D., "Asymptotic Behavior of Excitable Cellular Automata," Experimental Mathematics 2 (1993), 183–208. Original public preprint: arXiv:patt-sol/9303002, March 22, 1993. DOI: 10.1080/10586458.1993.10504277.

Gravner, J., Lyu, H. and Sivakoff, D., "Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs," original preprint arXiv:1610.07320 (October 24, 2016); Ann. Appl. Probab. 28 (2018), 3324–3357. DOI: 10.1214/17-AAP1350. Public full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
