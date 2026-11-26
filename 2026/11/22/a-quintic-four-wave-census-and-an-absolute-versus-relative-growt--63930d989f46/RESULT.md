# A quintic four-wave census and an absolute-versus-relative growth reversal on wheels

## Finding
Let \(W_n=K_1\vee C_n\), \(n\ge3\), be the labelled wheel with one hub and \(n\) rim vertices, and let \(F_n\) be simultaneous four-state, threshold-one Greenberg–Hastings dynamics. Write \(O_n\) for the number of **primitive temporal four-cycle orbits** (not configurations) of \(F_n\). Define
\[
A(z)=(1+z^2)(1-z-2z^2-2z^3-z^4-z^5),\qquad B(z)=1-z-z^2-z^3.
\]
Then the exact all-circumference orbit generating function is
\[
\boxed{\sum_{n\ge3}O_nz^n=-z\frac{A'(z)}{A(z)}+z\frac{B'(z)}{B(z)}.}
\]
In particular, \(O_3,O_4,\ldots,O_{12}\) are
\[
6,\ 20,\ 50,\ 120,\ 308,\ 756,\ 1824,\ 4380,\ 10450,\ 24812.
\]
The four-state model has exactly \(4O_n\) immediately primitive-four-periodic labelled configurations, and its unique fixed configuration is all rest. No claim about the complete eventual-basin census or other eventual periods is needed or made.

Let \(\lambda\) be the unique positive zero of
\[
X^5-X^4-2X^3-2X^2-X-1,
\]
and let \(\mu\) be the positive zero of \(X^3-X^2-X-1\). Then
\[
\lambda=2.33529479891245\ldots,\qquad \mu=1.83928675521416\ldots,\qquad O_n=\lambda^n+O(\mu^n).
\]
Consequently the probability, under independent uniform four-state initial colors, of **starting** in a primitive four-cycle is asymptotic to \((\lambda/4)^n\).

For contrast, the published three-state wheel census gives a primitive-three-orbit population \(P_n\sim\rho^n\), where \(\rho=2.20556943040059\ldots\) is the positive zero of \(X^3-2X^2-1\). Thus increasing the palette from three states to four produces an **absolute-versus-relative growth reversal**:
\[
\lim_{n\to\infty}\frac{O_n}{P_n}=\infty,
\qquad
\lim_{n\to\infty}\frac{O_n/4^n}{P_n/3^n}=0.
\]
There are eventually more four-phase orbits in absolute number, while the chance of being initially on one becomes exponentially smaller relative to the available state space.

## Assumptions and scope
The graph is the simple undirected labelled wheel: hub \(h\) is adjacent to all \(n\) distinct rim sites, and rim site \(i\) is adjacent to \(i-1,i+1\pmod n\). Each vertex has state \(0,1,2,3\). Every synchronous update sends \(1\mapsto2\mapsto3\mapsto0\), and sends \(0\mapsto1\) if and only if a **distinct neighbor** currently has state \(1\); otherwise it leaves \(0\) unchanged. A primitive temporal four-cycle orbit is a set of four distinct configurations cyclically permuted by the update. Spatial rotations are not quotiented out. Initial-color probability refers to the product uniform distribution on all \(4^{n+1}\) assignments. The comparison with three states uses the same graph family and threshold but changes the number of refractory phases.

## Proof
**1. All vertices rotate in a four-periodic state.** If \(F_n^4(x)=x\), a vertex visiting a nonzero state must traverse all four states in the next four steps and hence advance at every step. A vertex that stays at zero throughout cannot be adjacent to such a rotating vertex: the latter would visit state \(1\) once during those four steps and excite it. Connectivity implies either no vertex rotates (the all-zero fixed state) or **every vertex** rotates, each following its initial state plus the time modulo four. In the latter case the configuration has least period four. Such a coloring is therefore periodic if and only if every vertex of color \(0\) has a neighbor of color \(1\), every vertex of color \(1\) has a neighbor of color \(2\), every vertex of color \(2\) has a neighbor of color \(3\), and every vertex of color \(3\) has a neighbor of color \(0\); equivalently every vertex of color \(r\) has a neighbor of color \(r+1\pmod4\). This condition guarantees excitation at each future zero-phase, so it is also sufficient.

**2. Fix hub phase zero.** Global addition of a constant modulo four preserves the rotating-color condition and acts freely on its solutions. With hub color \(0\), the hub needs at least one rim vertex of color \(1\). A rim vertex \(i\) of color \(3\) automatically has its successor color \(0\) at the hub; for rim color \(b\ne3\) its two rim neighbors must include \(b+1\). Hence, writing consecutive rim colors \(a,b,c\), the local admissibility criterion is
\[
b=3\quad\text{or}\quad a=b+1\pmod4\quad\text{or}\quad c=b+1\pmod4.
\]
Use the sixteen ordered-pair states \((a,b)\in\{0,1,2,3\}^2\). Define the \(16\times16\) \(0\)-\(1\) matrix \(T\) with edge \((a,b)\to(b,c)\) exactly when this condition holds, and let \(U\) be the principal submatrix restricted to the nine pairs with neither coordinate equal to \(1\). Standard closed-walk counting identifies \(\operatorname{tr}(T^n)\) with the admissible indexed circular rim words, while \(\operatorname{tr}(U^n)\) counts precisely those with no rim \(1\). The latter violate the hub's successor requirement, and no others do. Therefore the total number of rotating configurations is
\[
4\bigl(\operatorname{tr}(T^n)-\operatorname{tr}(U^n)\bigr),
\]
so dividing by four temporal phases gives \(O_n=\operatorname{tr}(T^n)-\operatorname{tr}(U^n)\). This is an exact identity for every simple wheel \(n\ge3\).

**3. Exact characteristic polynomials.** Ordinary integer characteristic-polynomial computation from these explicitly defined matrices gives
\[
\det(XI-T)=X^9(X^2+1)(X^5-X^4-2X^3-2X^2-X-1),
\]
\[
\det(XI-U)=X^6(X^3-X^2-X-1).
\]
These polynomial equalities are independently reproduced by the included `checks/verify_transfer.py`, which uses the exact Faddeev–LeVerrier recursion and verifies the final Cayley–Hamilton remainders, rather than merely fitting finite counts. Since \(\det(I-zT)=A(z)\) and \(\det(I-zU)=B(z)\), the identity \(\sum_{n\ge1}\operatorname{tr}(M^n)z^n=-z\,d\log\det(I-zM)/dz\) establishes the displayed rational generating function. The coefficients at \(n=1,2\) cancel, so the series starts at \(n=3\).

**4. Growth and cross-palette comparison.** Descartes' rule and exact rational polynomial-sign bracketing give unique positive roots with \(2.335<\lambda<2.336\) and \(1.839<\mu<1.840\). To bound the nonleading quintic roots at the scale of the *different* root \(\mu\), write the quintic as \((X-\lambda)Q(X)\), where
\[
Q(X)=X^4+a_1X^3+a_2X^2+a_3X+a_4,
\qquad a_4=1/\lambda,\quad \lambda a_3=1+a_4,\quad
\lambda a_2=2+a_3,\quad \lambda a_1=2+a_2.
\]
These identities follow by comparing coefficients from the constant term upward. They give \(0<a_4<a_3<a_2<a_1\); the coefficient of \(X^4\) in the quintic also gives \(a_1=\lambda-1\). By the Eneström–Kakeya bound, each root of \(Q\) has modulus at most \(\max(a_4/a_3,a_3/a_2,a_2/a_1,a_1)=\lambda-1<\mu\). The cubic \(X^3-X^2-X-1\) has a primitive nonnegative companion matrix, so its roots have modulus at most \(\mu\). The factor \(X^2+1\) contributes only bounded oscillations. Thus the trace difference satisfies \(O_n=\lambda^n+O(\mu^n)\).

The earlier three-state wheel formula is \(P_n=\operatorname{tr}(T_3^n)-1\), with \(\det(XI-T_3)=X^4(X^2+X+1)(X^3-2X^2-1)\). The cubic has a primitive nonnegative companion matrix (its directed cycle lengths include 1 and 3), yielding \(P_n\sim\rho^n\), with \(2.205<\rho<2.206\) by rational bracketing. Since \(\lambda>\rho\) but \(\lambda/4<\rho/3\), both limits in the finding follow. The use of this earlier three-state result is explicitly credited, not claimed as a new theorem.

## Verification
`python3 checks/verify_transfer.py` reconstructs the two transfer matrices with exact integer entries; computes their characteristic polynomials by exact integer Faddeev–LeVerrier steps; verifies the final Cayley–Hamilton identities; and prints/compares the all-length sequence through rim length fourteen. `python3 checks/verify_direct.py` independently evolves **all** \(4^{n+1}\) labelled configurations for each rim length \(3\le n\le8\) through four updates, and separately counts fixed points, period-two states and primitive period-four states. It agrees with the transfer sequence and finds only the all-zero fixed state and no period-two state. Direct enumeration is finite supporting evidence, not the argument that establishes all \(n\). The algebraic transfer proof establishes all circumferences.

## Relationship to prior work
Durrett–Griffeath (1993) and Greenberg–Hastings (1978) provide the underlying excitable-medium framework, including persistent waves. Gravner–Lyu–Sivakoff (2016 preprint, 2018 journal) give three-color arbitrary-graph behavior, not this four-color finite-wheel enumerator. The public result *Two spectral scales in three-state excitation on wheel graphs* [4] supplies the three-state comparator and its spectral root; its rule uses **three** states and does not imply the four-state quintic. The prior complete tripartite result [5] already covers \(W_4=K_{1,2,2}\); its Greenberg–Hastings formula gives 81 four-step returns including the all-rest fixed point, hence \(O_4=20\). The companion cyclic cellular automaton enumeration [7] also gives 20 primitive four-cycles, because the successor-phase predicate for primitive four-cycles is shared even though fixed points differ. This entry is not new. Those tripartite graphs do not cover the whole wheel family (in a complete multipartite graph the hub is a singleton shore, and among the simple cycles only \(C_3,C_4\) are complete multipartite; \(W_3=K_4\) has four shores). The complete bipartite censuses exclude wheels, which contain triangles. The threshold-two wheel extinction result changes the excitation requirement and has no primitive cycles. The original 1978 full text remains uninspected, leaving a residual historical-priority risk.

## Limitations
The theorem enumerates *initially* primitive temporal four-cycles, not the total set of states eventually attracted to them, nor possible recurrent periods other than four. It applies to an intact wheel, synchronous threshold-one excitation, and four colors. Exact integer certificates and small-graph exhaustive checks provide same-package reproducibility but not independent external validation. Literature searches, including exact parameter and algebraic aliases, cannot rule out all unindexed historical calculations; the 1978 original remains uninspected in full. The comparison with three colors is limited to immediately periodic populations and uniform-product probabilities, not complete basins.

## References
1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523, DOI:10.1137/0134040.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first public submission 1993-03-22).
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first public submission 2016-10-24), Annals of Applied Probability 28 (2018), 3324–3357, DOI:10.1214/17-AAP1350.
4. *Two spectral scales in three-state excitation on wheel graphs*, publicly accessible scientific research record `c503df57632e` (2026).
5. *Four-state excitation on tripartite graphs: identical four-cycle orbits, different transients, and exact extinction*, publicly accessible scientific research record `6411c0882be0` (2026).
6. *Two motif channels control the sharp extinction shell of multistate excitable wheels*, publicly accessible scientific research record `45299ac945e0` (2026).
7. *Sharp three-step period collapse and exact orbit counts for four-color cyclic dynamics on tripartite graphs*, publicly accessible scientific research record `a56bc883e0df` (2026).
