# Oscillation-by-opening and exact two-cycle entropy on majority fan graphs

## Finding

Let \(F_n=K_1\vee P_n\), with \(n\ge3\) labelled path vertices, carry synchronous binary open-neighbor majority, retaining a bit on a tie. Let \(C_n\) be the number of distinct **primitive temporal two-cycles** (not the number of initial states). Then
\[
C_n=\sum_{k=\lfloor n/2\rfloor+1}^{n-1}\ \sum_{\substack{1\le r\le\min(\lfloor k/2\rfloor,n-k)\\2(k-r)<n}}
\frac nr\binom{k-r-1}{r-1}\binom{n-k-1}{r-1}.
\]
There are precisely two fixed configurations, both constant. Primitive two-cycles exist for all \(n\ge3\) except \(n=4\). Every primitive two-cycle **flips the universal vertex**. With \(\lambda\in(1,2)\) the unique real root larger than one of \(\lambda^3-2\lambda^2+\lambda-1=0\), there is \(\eta<\lambda\) such that
\[
2C_n=2\lambda^n+O(\eta^n),\qquad
\lim_{n\to\infty}\frac1n\log(2C_n)=\log\lambda.
\]
The exact counts \(2C_n\) for \(n=3,4,5,6,7,8,9,10\) are respectively \(6,0,10,6,42,32,132,130\).

## Assumptions and scope

The graph is simple, undirected, with one hub \(h\), a path \(v_1,\dots,v_n\), every path vertex joined to \(h\), and no edge \(v_1v_n\). Configuration bits lie in \(\{0,1\}^{n+1}\). All vertices update simultaneously; a vertex takes the strict majority of its neighbors, or retains its current bit if their votes are tied. Write \(M\) for the update. Primitive-two states satisfy \(M^2z=z\) and \(Mz\ne z\), and two such states comprise each orbit. The formulas count period-two behavior from time zero, not eventual attractor basins.

## Proof

**Step 1: the hub must flip.** Suppose a configuration has period dividing two and the hub stays at zero. In each update the path has the map \(E\) defined by
\[
(Ex)_1=x_1x_2,\quad(Ex)_i=x_{i-1}x_{i+1}\ (2\le i<n),\quad(Ex)_n=x_{n-1}x_n.
\]
This is Boolean AND over the neighbors of a path with an added loop at each endpoint. In a two-cycle, \(x=E^2x\). If \(x_i=1\), all vertices reachable from \(i\) by an even-length walk in this looped path have value one. The even-walk relation is connected: append an endpoint loop to change any walk's parity. Thus \(x\) is all ones; that would make the hub switch from zero, a contradiction. The only permissible constant-zero hub state is all zero and fixed. Complementation gives the analogous statement for a constant-one hub: only the all-one fixed state. Therefore every other period-two state flips the hub.

**Step 2: an opening on an auxiliary cycle.** Select the unique member of each two-cycle with hub zero, and write its path bits \(x\). At the next time the hub is one and the path bits are \(y=Ex\). On the return, path bits are \(Dy\), where \(D\) is Boolean OR over precisely the same neighbor sets. The condition is \(x=DEx\). Index these sets as
\[
N_1=\{1,2\},\quad N_i=\{i-1,i+1\}\ (2\le i<n),\quad N_n=\{n-1,n\}.
\]
As two-element sets, these are exactly the edges of a simple \(n\)-cycle \(H_n\) on the labelled path positions: the distance-two chains of each parity are joined at both ends. The equality \(x=DEx\) holds exactly when every vertex carrying bit one is incident to an edge of \(H_n\) whose two endpoints both carry one. Equivalently, the cyclic word obtained by reading \(x\) around \(H_n\) has no isolated one. This includes the constant words, but they will fail the hub-flip inequalities.

Let \(k\) be the number of ones in \(x\), and let \(e\) be the number of edges of \(H_n\) with two one endpoints. By the definition of \(E\), \(e=|Ex|=|y|\). The hub flips from zero to one exactly when \(2k>n\); it flips back from one to zero exactly when \(2e<n\). Thus there is a bijection between primitive two-cycles and cyclic binary words on \(H_n\) with no isolated ones and \(2k>n>2e\).

**Step 3: exact enumeration.** Such a word must contain both digits. Let \(r\) be the number of runs of ones. No isolated ones means the \(r\) positive one-run lengths are at least two, while the \(r\) zero-run lengths are at least one. Hence \(1\le r\le\min(\lfloor k/2\rfloor,n-k)\), and the number of one-one edges is \(e=k-r\). The \(r\) ordered one-run lengths can be chosen in \(\binom{k-r-1}{r-1}\) ways; zero-run lengths in \(\binom{n-k-1}{r-1}\) ways. Choosing a marked run start among \(n\) labelled positions and dividing by the \(r\) possible marked runs gives exactly
\[
\frac nr\binom{k-r-1}{r-1}\binom{n-k-1}{r-1}
\]
configurations with parameters \((k,r)\), proving the asserted finite sum. For odd \(n=2m+1\ge3\), the choice \(k=m+1,r=1\) is admissible. For even \(n=2m\ge6\), \(k=m+1,r=2\) is admissible. For \(n=4\) no \((k,r)\) meets the bounds.

**Step 4: asymptotic.** Read cyclic words in the auxiliary cycle order. Use length-two states \((a,b)\in\{0,1\}^2\) and an edge \((a,b)\to(b,c)\) unless \((a,b,c)=(0,1,0)\). Give this edge weight \(u^bv^{bc}\); the resulting explicit \(4\times4\) matrix is
\[
T(u,v)=\begin{pmatrix}1&1&0&0\\0&0&0&uv\\1&1&0&0\\0&0&u&uv\end{pmatrix}.
\]
The trace \(\operatorname{tr}(T(u,v)^n)\) enumerates cyclic words with no isolated ones, weighted by \(u^kv^e\). Direct determinant expansion gives
\[
\det(zI-T(u,v))=z\{z^3-(1+uv)z^2+uvz-u^2v\}.
\]
At \(u=v=1\), the nonnegative matrix is primitive (its directed graph is strongly connected and has a self-loop). Let \(\lambda>1\) be its Perron eigenvalue, the unique root in \((1,2)\) of \(z^3-2z^2+z-1\). Other eigenvalues have strictly smaller modulus. Implicit differentiation at \(u=v=1\) yields the limiting means per position of \(k\) and \(e\):
\[
\mu_k=\frac{\lambda^2-\lambda+2}{\lambda(3\lambda^2-4\lambda+1)},\qquad
\mu_e=\frac{\lambda^2-\lambda+1}{\lambda(3\lambda^2-4\lambda+1)}.
\]
Using \(\lambda^3=2\lambda^2-\lambda+1\), these satisfy \(\mu_k+\mu_e=1\) and \(\mu_k-\mu_e=1/[\lambda(3\lambda^2-4\lambda+1)]>0\). Hence \(\mu_k>1/2>\mu_e\). By positivity of the weighted transfer and continuity/differentiability of its simple Perron eigenvalue, for sufficiently small \(t>0\) both \(e^{t/2}\rho(T(e^{-t},1))\) and \(e^{-t/2}\rho(T(1,e^t))\) are strictly below \(\lambda\). Exponential tilting then bounds the numbers of words with respectively \(2k\le n\) and \(2e\ge n\) by \(O(\eta^n)\) for some \(\eta<\lambda\); for example, a four-dimensional matrix has \(\operatorname{tr}(T^n)\le4\rho(T)^n\) for nonnegative weights. Removing these violations from \(\operatorname{tr}(T(1,1)^n)=\lambda^n+O(\eta_0^n)\) proves \(C_n=\lambda^n+O(\eta^n)\). The factor two converts orbits into states.

## Verification

The standalone programs `verify_fan.py` and `verify_spectral.py` and their recorded outputs are embedded with this result. The first directly simulates all \(2^{n+1}\) initial states for each \(3\le n\le13\), validates the hub-flip and cycle-word bijection, and compares every count to the binomial sum. The second independently checks the symbolic determinant using a four-by-four Leibniz expansion over integer monomials and exhaustively enumerates cyclic words for \(3\le n\le13\). Both completed successfully. Neither finite experiment is used to infer the all-size theorem.

## Relationship to prior work

Agur, Fraenkel and Klein (1988) enumerate fixed words for the one-dimensional majority automaton; their cyclic no-isolated-bit enumerator is closely related to the cyclic words in Step 2, but does not supply the fan-graph dynamical bijection, hub threshold inequalities or the two-cycle entropy. Goles--Olivos' foundational period-one-or-two theorem and the voting-time analysis of Kaaser, Mallmann-Trenn and Natale establish the period bound but not this fan census. Turau's full text treats fixed points and pure two-cycles on trees, not the cone over a path. Nakar and Ron treat radius-majority dynamics on a single cyclic ring; the fan hub has a degree growing with \(n\) and a different open-neighbor rule. Exact results for the **wheel** (a cone over a cycle) give related weighted cyclic-word distributions but do not specialize to the fan, whose rim endpoints have degree two and a different interaction structure.

## Limitations

This determines initially periodic configurations only; it does not enumerate transient basins or their entry times. The rate constant \(\eta<\lambda\) is not optimized. Related weighted cyclic-word and wheel calculations are close, so priority for the unindexed exact fan formula requires further independent literature scrutiny. An independent scientific audit has not been performed.

## References

- Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, doi:10.1016/0012-365X(88)90005-2; lawful author manuscript: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
- D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first posted 2015-08-14, https://arxiv.org/abs/1508.03519.
- V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769, first posted 2023-12-21, https://arxiv.org/abs/2312.13769.
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972, first posted 2022-05-18, https://arxiv.org/abs/2205.08972.
