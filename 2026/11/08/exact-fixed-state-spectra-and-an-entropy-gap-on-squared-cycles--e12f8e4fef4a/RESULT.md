# Exact fixed-state spectra and an entropy gap on squared cycles

## Finding

For each integer \(n\ge 5\), let \(G_n=C_n^2\) be the simple graph on \(\mathbb Z/n\mathbb Z\) with edges at offsets \(\pm1\) and \(\pm2\). Consider two separate synchronous binary update maps. At every vertex the **minority map** selects the less frequent opinion among its four neighbors, retaining the old opinion in a two-to-two tie; the **majority map** similarly selects the more frequent neighboring opinion, retaining the old opinion on ties. Let \(U_n\) and \(V_n\) be their respective numbers of fixed labelled binary configurations.

For a monic polynomial \(f\), put \(S_f(n)=\sum_{f(\zeta)=0}\zeta^n\), with roots counted with multiplicity. Set
\[
\begin{aligned}
p(X)&=X^5-X^3-2X^2-X-1, &q(X)&=X^5+X^3+X-1,\\
a(X)&=X^3-X^2-1, &b(X)&=X^3-X^2+1.
\end{aligned}
\]
Then, **exactly for every \(n\ge5\)**,
\[
\boxed{U_n=1+(-1)^n+S_p(n)+S_q(n),\qquad
V_n=1+(-1)^n+S_a(n)+S_b(n).}
\]
Let \(\lambda_-\) be the unique positive root of \(p\), and \(\lambda_+\) the unique positive root of \(a\). Their values are \(\lambda_-=1.66630193731293\ldots\) and \(\lambda_+=1.46557123187677\ldots\). Both roots are simple and strictly dominate the other roots in the corresponding formulas. Consequently,
\[
U_n\sim\lambda_-^n,\quad V_n\sim\lambda_+^n,
\quad\text{and}\quad \frac{U_n}{V_n}\sim
\left(\frac{\lambda_-}{\lambda_+}\right)^n,
\]
where \(\lambda_-/\lambda_+=1.136964141401\ldots>1\). Thus the two fixed-state entropy densities are \(\log\lambda_-\) and \(\log\lambda_+\), respectively: the anti-coordination rule has exponentially more fixed configurations than the coordination rule **on the same four-regular graph**.

## Assumptions and scope

Vertices and states are labelled, and distinct binary assignments are counted distinctly; rotational and color-complement equivalences are **not** factored out. Both update maps act simultaneously on all vertices. The degree is exactly four because \(n\ge5\), and a tie retains the original bit. Only one-step fixed states are counted: neither transient trajectories nor primitive two-cycles are claimed to be enumerated. The rule is the graph-neighborhood rule, not majority on the five-site neighborhood including the center as an additional vote.

## Proof

**Local fixed-point test.** For a cyclic word \(s=(s_0,\dots,s_{n-1})\), let \(h_i\) be the number of the four bits at offsets \(\pm1,\pm2\) that equal \(s_i\). At a vertex the minority map fixes \(s_i\) exactly if \(h_i\le2\); the majority map fixes it exactly if \(h_i\ge2\). These statements also cover the tied case \(h_i=2\).

**Closed-word transfer bijection.** Index the sixteen binary words of length four by their usual binary integers \(j\in\{0,\ldots,15\}\). For a word \((u,v,w,z)\) at state \(j=8u+4v+2w+z\) and a new bit \(t\in\{0,1\}\), put \(k= (2j+t)\bmod 16\). Let \(h=\mathbf1_{u=w}+\mathbf1_{v=w}+\mathbf1_{z=w}+\mathbf1_{t=w}\). Define \(T_-\) by \((T_-)_{jk}=1\) if \(h\le2\), and \(T_+\) analogously by \((T_+)_{jk}=1\) if \(h\ge2\), summing the two candidate transitions if necessary (there are no duplicates at \(n\ge5\)). Other entries are zero. A closed walk of length \(n\) specifies the unique cyclic sequence of overlapping four-windows, including its labelled origin; its local constraints are precisely the fixed-point tests at the central bit. Conversely every fixed cyclic word gives a unique such walk. Therefore \(U_n=\operatorname{tr}(T_-^n)\) and \(V_n=\operatorname{tr}(T_+^n)\).

**Exact characteristic factors.** Binary complementation sends state \(j\) to \(15-j\) and commutes with either transfer operator. Use symmetric and antisymmetric bases \(e_j\pm e_{15-j}\), \(0\le j<8\), to split each operator into \(8\times8\) blocks \(P\) and \(N\) with entries \(P_{jk}=T_{jk}+T_{j,15-k}\) and \(N_{jk}=T_{jk}-T_{j,15-k}\). Row-indexed nonzero target sets for the **minority symmetric block** are

`[], [3], [4,5], [6,7], [6], [4,5], [2,3], [1]`.

For the minority antisymmetric block the same targets have signs \(+,+,+,+,-,-,-,-\) by source row \(0,1,2,3,4,5,6,7\), respectively (the empty row is zero). For the **majority symmetric block**, the row-indexed target sets are

`[0,1], [2,3], [], [7], [6,7], [5], [2], [0,1]`.

For the majority antisymmetric block, the same targets have signs \(+,+,0,+,-,-,-,-\) by row. Direct integer determinant expansion of these explicitly given blocks yields
\[
\begin{aligned}
\det(XI-P_-)&=X^2(X-1)p(X), &\det(XI-N_-)&=X^2(X+1)q(X),\\
\det(XI-P_+)&=X^4(X-1)a(X), &\det(XI-N_+)&=X^4(X+1)b(X).
\end{aligned}
\]
The determinant identities can be checked independently by constructing the blocks from the local rule; `verify_symbolic.py` does this with exact integer arithmetic. Their products equal the full characteristic polynomials
\[
\det(XI-T_-)=X^4(X-1)(X+1)p(X)q(X),\quad
\det(XI-T_+)=X^8(X-1)(X+1)a(X)b(X).
\]
Since the trace of each power is the sum of the corresponding eigenvalue powers, the exact counting formulas follow, including any repeated roots.

**Dominant roots.** By Descartes' rule of signs, each of \(p\) and \(a\) has exactly one positive real root; direct sign evaluations give \(1.66<\lambda_-<1.67\) and \(1.46<\lambda_+<1.47\). The minority positive block has a single strongly connected nontrivial component on states \(1,\ldots,7\), with a self-loop at state \(5\); hence its spectral radius is simple and strictly larger in modulus than its remaining eigenvalues by Perron–Frobenius. Its characteristic factor is \((X-1)p(X)\), and the positive root exceeds one, so its Perron root is \(\lambda_-\). Every root of \(q\) has modulus less than \(3/2\): when \(\lvert z\rvert\ge3/2\), \(\lvert z\rvert^5>\lvert z\rvert^3+\lvert z\rvert+1\), contradicting \(q(z)=0\). Thus \(\lambda_-\) uniquely dominates the minority spectrum.

For the majority, \(a\) has one real positive root \(\lambda_+\); the other two conjugate roots have modulus \(\lambda_+^{-1/2}<1\) by Vieta. The polynomial \(b\) has exactly one negative real root \(t\in(-0.76,-0.75)\), since its only nonnegative local extrema are positive, and hence its conjugate pair has modulus \(\lvert t\rvert^{-1/2}<\sqrt{4/3}<\lambda_+\). The remaining roots are \(0,1,-1\). This proves the majority root is uniquely dominant. In each case its multiplicity is one, giving the announced asymptotics with coefficient one. The corresponding entropy statements follow by logarithms.

## Verification

Two executable checks accompany this statement. `verify_direct.py` independently enumerates every one of the \(2^n\) labelled bit strings, tests the update rule at all vertices and compares the count to an integer transfer-matrix trace for each \(5\le n\le16\) and each rule. Its output ends with `VERIFY_DIRECT_OK`. `verify_symbolic.py` independently constructs the sixteen-state matrices and complement blocks, checks all six characteristic factorizations exactly, checks trace decomposition at thirteen lengths and reports the two positive root approximations; its output ends with `VERIFY_SYMBOLIC_OK`.

For \(n=5,6,7,8,9,10,11,12\), the minority populations are \(20,26,28,62,96,172,286,450\); the corresponding majority populations are \(2,10,16,28,38,54,68,94\). The certificates establish the finite checks; the transfer bijection and determinant identities establish the infinite formulas. Computed root decimals are descriptive and not used as proofs of root dominance.

## Relationship to prior work

General transfer-graph approaches to cellular-automaton fixed points were described by Banks and Djirar (1993), and the radius-one majority fixed-point population was studied by Agur, Fraenkel, and Klein (1988). Those methods make finite-state enumeration conceptually available, but neither inspected example supplies the present explicit degree-five minority spectral factor, degree-three majority factor or their same-graph entropy comparison. Moran (1994) studies radius-\(r\) majority patterns and is a plausible prior source for the majority half of the statement; complete text was not accessible. Nakar and Ron (2022) characterize structural classes of majority and minority configurations on cyclic rings and do not state the exact spectral comparison in inspected material. Wacław and Burda (2008) motivate fixed anti-coordination configurations through metastability, but their random-interaction treatment does not give this deterministic uniform-lattice census. The novelty claim is limited to the **joint explicit fixed-state spectral law and asymptotic entropy gap**, not the transfer-matrix technique or the general fact that these are cellular automata.

## Limitations

The result does not count basins, transients, period-two points, or nonuniform couplings. It requires \(n\ge5\), labelled sites, synchronous updates, and a precise tie-retention convention. The comparison is limited to the squared-cycle family and does not imply analogous ordering on arbitrary regular graphs. A general 1994 radius-\(r\) majority analysis was not fully inspected, so historical priority for the majority half is qualified; a yet-unindexed equivalent exact census cannot be excluded. The computations are reproducibility checks, not a substitute for the transfer proof. No independent scientific audit has been performed.

## References

- S. P. Banks and S. Djirar, *On the Existence and the Number of Fixed Points of Dynamical Systems Defined by Cellular Automata*, Research Report 491 (1993), University of Sheffield. Public full text: https://eprints.whiterose.ac.uk/id/eprint/79491/ .
- Z. Agur, A. S. Fraenkel, and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302. Full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
- G. Moran, *The r-majority vote action on 0–1 sequences*, Discrete Mathematics **132** (1994), 145–174.
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (first posted 2022-05-18). https://arxiv.org/abs/2205.08972 .
- B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224 (first posted 2008-01-08). https://arxiv.org/abs/0801.1224 .
