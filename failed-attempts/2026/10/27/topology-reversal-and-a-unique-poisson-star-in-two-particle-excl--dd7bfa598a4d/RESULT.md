# Topology reversal and a unique Poisson star in two-particle exclusion activity

## Finding

For integers \(m,n\geq 1\) with \(N=m+n\geq3\), consider the continuous-time, symmetric, two-particle exclusion process on the complete bipartite graph \(K_{m,n}\). Each occupied vertex attempts a jump to each vacant neighboring vertex at rate one per directed edge. Start the process in its uniform equilibrium measure on the \(\binom{N}{2}\) unordered two-particle configurations. Write \(C_T\) for the total number of **successful** jumps over \([0,T]\), and put \(\delta=m-n\). Its exact long-time mean jump rate and variance-to-mean ratio are

\[
\lim_{T\to\infty}\frac{\mathbb EC_T}{T}
=\mu_{m,n}=\frac{4mn(N-2)}{N(N-1)},
\qquad
F_{m,n}:=\lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{\mathbb EC_T}
=1+\frac{N^2+\delta^2(N^2-6N+4)}{N^2(N-1)^2}.
\]

For fixed \(N\), the topology ordering reverses sharply: for \(N=4,5\), **stars minimize** \(F_{m,n}\) and the most balanced partitions maximize it; for every \(N\ge6\), the most balanced partitions minimize \(F_{m,n}\) and **stars maximize** it. There is only one isomorphism type when \(N=3\). The inequality \(F_{m,n}\ge1\) is strict for every graph in this family except \(K_{1,3}\cong K_{3,1}\). At that graph the entire counting process, not just its asymptotic moments, is Poisson with rate \(2\). At fixed \(N\to\infty\), the minimum excess noise is of order \(N^{-2}\), while the excess noise on stars tends to \(1\) and their Fano ratio tends to \(2\).

The distinguishing assertion is the evaluated two-particle, all-bipartitions counting-noise law and its complete topology ordering; the general tilted-generator method and undirected exclusion dynamics are not new.

## Assumptions and scope

\(K_{m,n}\) has disjoint vertex classes \(A,B\) of sizes \(m,n\); every possible edge between them is present and there are no within-class edges. Two indistinguishable hard-core particles occupy distinct vertices. For each ordered occupied-to-vacant adjacent pair, the particle jumps at rate \(1\); failed attempts are **not** counted. The process is finite and irreducible when \(N\ge3\), with reversible equilibrium uniform on the unordered occupancy pairs. Its jump process is stationary from the stated initial condition. The expression for \(F_{m,n}\) is a time-asymptotic variance-to-mean ratio and makes no claim about finite-time equality to a Poisson law outside \(K_{1,3}\).

## Proof

**1. Symmetry reduction.** Let \(I_t\in\{0,1,2\}\) count occupied vertices in \(A\); omit states impossible because of a class size. The only nonzero transition rates are
\[
0\longrightarrow1:2m,\qquad
1\longrightarrow0:n-1,\qquad
1\longrightarrow2:m-1,\qquad
2\longrightarrow1:2n.
\]
The \(3\)-by-\(3\) row generator, when all three states are admissible, is
\[
Q=\begin{pmatrix}
-2m&2m&0\\ n-1&-(N-2)&m-1\\0&2n&-2n
\end{pmatrix}.
\]
The class-count stationary weights and total successful-jump intensities are
\[
\pi_0=\frac{n(n-1)}{N(N-1)},\quad
\pi_1=\frac{2mn}{N(N-1)},\quad
\pi_2=\frac{m(m-1)}{N(N-1)},\qquad
\lambda=(2m,N-2,2n).
\]
Zero-weight inadmissible endpoints contribute nothing. The detailed-balance identities \(2m\pi_0=(n-1)\pi_1\) and \(2n\pi_2=(m-1)\pi_1\) follow immediately. Therefore \(\mu=\pi\lambda=4mn(N-2)/(N(N-1))\). This is also the exact value of \(\mathbb EC_T/T\) at every \(T>0\), by stationarity.

**2. Counting-variance identity.** Write \(\Lambda=\operatorname{diag}(\lambda)\), \(W=Q+\Lambda\), and \(Q_z=e^zW-\Lambda\). The principal eigenvalue \(\psi(z)\) is analytic around \(z=0\) because the finite state chain is irreducible. Standard counting-generator differentiation yields \(\psi'(0)=\mu\). If \(h\) solves \(Qh=\mu\mathbf1-\lambda\), with any additive constant, differentiating the right-eigenvalue equation and normalizing its eigenvector to have \(\pi\)-mean one gives
\[
\psi''(0)=\mu+2\langle\lambda-\mu,h\rangle_\pi,
\qquad
F_{m,n}=\frac{\psi''(0)}{\mu}.
\]
This formula is independent of the additive constant in \(h\); analyticity and finite-state exponential convergence justify the limiting cumulant rates.

**3. Explicit Poisson equation.** Choose the harmless normalization \(h_1=0\). The two endpoint equations give
\[
h_0=1-\frac{\mu}{2m},\qquad h_2=1-\frac{\mu}{2n}.
\]
The middle equation follows from \(\pi(\lambda-\mu)=0\) and detailed balance, including when one endpoint state is absent. Since the chain is reversible,
\[
\langle\lambda-\mu,h\rangle_\pi
=\langle-Qh,h\rangle_\pi
=2m\pi_0(h_1-h_0)^2+2n\pi_2(h_1-h_2)^2.
\]
Substituting the expressions above and simplifying the rational expression gives
\[
F_{m,n}-1
=\frac{2}{\mu}\left[2m\pi_0\left(1-\frac{\mu}{2m}\right)^2
+2n\pi_2\left(1-\frac{\mu}{2n}\right)^2\right]
=\frac{N^2+(m-n)^2(N^2-6N+4)}{N^2(N-1)^2}.
\]
This derivation remains valid on the two-state reduced chain for either star orientation, with the inaccessible endpoint term interpreted as zero.

**4. Equality, ordering, limits.** Both square terms are nonnegative. Equality requires every accessible endpoint edge to connect states with identical escape rates. For \(m,n\ge2\), this would require \(\mu=2m=2n\), impossible because \(\mu<2m\) when \(m=n\). For \(m=1\) and \(n\ge2\), the expression reduces to
\[
F_{1,n}-1=\frac{(n-3)^2}{(n+1)^2},
\]
so equality occurs only at \(n=3\), up to part exchange. In \(K_{1,3}\) every two-particle configuration has exactly two possible successful hops, each of rate one, so its successive holding times are independent \(\mathrm{Exp}(2)\) variables. Consequently \(C_T\) is exactly a Poisson process of rate \(2\).

At fixed \(N\), the coefficient of \(\delta^2\) in the formula for \(F_{m,n}\) has the sign of \(N^2-6N+4\), negative for \(N=3,4,5\) and positive for all integers \(N\ge6\). The feasible \(|\delta|\) is largest at the stars and smallest at \(m=\lfloor N/2\rfloor\), \(n=\lceil N/2\rceil\). This gives the stated strict comparisons when both graph shapes exist. For a star with \(m=1\), \(F_{1,N-1}-1=(N-4)^2/N^2\to1\); for the most balanced split \(|\delta|\le1\), the displayed expression is \(\Theta(N^{-2})\). All limits and boundary assertions follow.

## Verification

The standalone `verify.py` constructs the **full** \(\binom{m+n}{2}\)-configuration generator directly from allowed particle jumps, without using the class-count reduction in the generator construction. It then solves its stationary Poisson equation independently and compares both the mean activity and Fano ratio against the formulas for all 35 pairs \(1\le m,n\le6\) with \(m+n\ge3\). Its second part checks the symbolic identity and all topology extrema for each order \(3\le N\le30\). These finite checks corroborate the analytical, unbounded-parameter proof but do not replace it. Run `python verify.py` with NumPy and SymPy installed.

## Relationship to prior work

Appert-Rolland, Derrida, Lecomte, and van Wijland (arXiv:0804.2590, Sec. II and Eqs. 1–12) derive activity cumulants for the symmetric simple exclusion process **on a periodic one-dimensional ring**, supplying the well-established trajectory-counting formalism. Mendonça (arXiv:1207.4106, Secs. 2 and 4) solves the **unmarked** exclusion generator and its eigenvalue spectrum on complete bipartite graphs, including star graphs. That result provides a relevant structural model, but its eigenvalues alone do not evaluate the marked-generator curvature or the exact topology ordering of counted successful jumps. Vanicat, Bertin, Lecomte, and Ragoucy (arXiv:2011.02202, Secs. 2–4) study activity/current large-deviation mappings primarily for one-dimensional chains; their transformations do not supply the present evaluated \(K_{m,n}\) ratio. The square \(K_{2,2}\) is the four-cycle, so its \(F_{2,2}=10/9\) value is a covered special case of earlier finite-graph counting analysis, not separately claimed. The present complete-bipartite graph classification is the proposed additional contribution.

## Limitations

Only two indistinguishable particles, complete bipartite graphs, symmetric unit rates per directed edge, all successful jumps, and stationary long-time counting statistics are treated. The general nonnegativity of the counting-noise excess for finite reversible symmetric jump models is not itself a new principle. An undiscovered published specialization of more general graph-counting formulas could imply the evaluated expression or topology reversal; no exhaustive priority claim is made. Distinct jump attempts that fail are omitted from \(C_T\); counting all attempted hops instead gives a different statistic.

## References

1. C. Appert-Rolland, B. Derrida, V. Lecomte, F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590v1 (first public 2008-04-16), https://arxiv.org/abs/0804.2590.
2. J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106 (first public 2012-07-17), https://arxiv.org/abs/1207.4106.
3. M. Vanicat, E. Bertin, V. Lecomte, E. Ragoucy, *Mapping current and activity fluctuations in exclusion processes: consequences and open questions*, arXiv:2011.02202 (first public 2020-11-06), https://arxiv.org/abs/2011.02202.
