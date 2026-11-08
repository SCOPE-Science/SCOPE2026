# Thirteen vertices are the sharp Radau IIA positivity boundary on conference graphs

## Finding
Let \(G\) be a simple undirected conference graph on \(N=4t+1\) vertices, \(t\in\mathbb Z_{\ge1}\), with degree \(2t\), \(t-1\) common neighbors for adjacent pairs, and \(t\) common neighbors for nonadjacent pairs. Let \(L\) be its unweighted combinatorial Laplacian. Apply the two-stage, third-order Radau IIA method to \(u'(s)=-Lu(s)\). Its completed one-step matrix is
\[
T_t(h)=(6I-2hL)(h^2L^2+4hL+6I)^{-1},\qquad h\ge0.
\]
Write
\[
P_t(h)=t^2(4t+1)h^4-4t(t-1)(4t+1)h^3+(-8t^2+40t+6)h^2+(24t+24)h+36.
\]
Then the following exact classification holds for **every graph with these parameters**, without assuming vertex transitivity:

1. If \(t=1\) or \(t=2\), every entry of \(T_t(h)\) is nonnegative for every \(h\ge0\) and strictly positive for every \(h>0\).
2. If \(t\ge3\), the polynomial \(P_t\) has exactly two distinct simple positive roots \(h_-(t)<2<h_+(t)\). The matrix \(T_t(h)\) is entrywise nonnegative **exactly** for \(h\in[0,h_-(t)]\cup[h_+(t),\infty)\). On \((h_-(t),h_+(t))\), every diagonal entry is negative, while every off-diagonal entry stays strictly positive. At the two endpoints, the diagonals vanish and the off-diagonals are positive.
3. Along any sequence of existing conference graphs with \(t\to\infty\),
\[
\lim_{t\to\infty}t h_-(t)=\frac32,\qquad \lim_{t\to\infty} h_+(t)=4.
\]
All matrices \(T_t(h)\) are symmetric and have row and column sums one, regardless of entrywise sign. Conference graphs exist for \(t=1,2,3\) (on five, nine, and thirteen vertices, respectively), and for arbitrarily large \(t\) (Paley graphs of suitable prime-power orders). Thus the nine-to-thirteen-vertex transition is attained rather than merely formal.

## Assumptions and scope
The graph is an unweighted, loopless, undirected conference graph with the specified strongly regular parameters. Only *completed endpoint* positivity of the indicated Radau IIA one-step map is considered; positivity of internal Runge--Kutta stages or arbitrary nonautonomous systems is not claimed. The parameter \(h\) is the physical heat timestep with generator \(-L\) (not rescaled by graph degree). No graph exists for every integer \(t\); statements with \(t\) are conditional on existence, and the polynomial assertions hold algebraically for all integers \(t\ge1\).

## Proof
**1. Three-eigenvalue reduction.** Write \(A\) for adjacency and \(J\) for the all-ones matrix. The conference parameters imply
\[
A^2=tI-A+tJ,\quad L=2tI-A,\quad L^2=dL-pI+tJ,
\quad d=4t+1,\quad p=t(4t+1).
\]
Consequently the two nonzero Laplacian eigenvalues are the distinct positive roots \(u,v\) of \(z^2-dz+p=0\), explicitly \((4t+1\pm\sqrt{4t+1})/2\); the remaining eigenvalue is zero. The denominator \(h^2z^2+4hz+6\) is positive for each nonnegative eigenvalue and every \(h\ge0\). Hence the matrix inverse in the statement exists.

**2. Exact interpolation.** For \(R(z)=(6-2z)/(z^2+4z+6)\), interpolation on the three spectral values yields
\[
R(hL)=I-\alpha L+\beta L^2,
\quad \alpha=\frac{h[h^3pd+h^2(6d^2-2p)+24hd+36]}{D},
\quad \beta=\frac{h^2[h^2p+6hd+18]}{D},
\]
where
\[
D=h^4p^2+4h^3pd+h^2(6d^2+4p)+24hd+36.
\]
To verify, substitute separately \(z=0,u,v\) into \(R(hz)=1-\alpha z+\beta z^2\), use \(u+v=d\) and \(uv=p\), and multiply through by the two strictly positive scalar denominators. Those products equal \(D\). In particular \(D>0\), \(\alpha>0\) for \(h>0\), and \(\beta>0\) for \(h>0\).

**3. Entry signs.** The diagonal, adjacent off-diagonal, and nonadjacent off-diagonal entries of \(L^2\) are, respectively, \(4t^2+2t\), \(-3t-1\), and \(t\). Therefore, every diagonal entry of \(T_t(h)\) equals \(P_t(h)/D\). Every adjacent entry equals
\[
\frac{h Q_t(h)}D,\quad Q_t(h)=36+(42t+6)h+4t(4t+1)h^2+t^2(4t+1)h^3,
\]
and every nonadjacent entry equals
\[
\frac{t h^2[h^2p+6hd+18]}D.
\]
Both off-diagonal expressions are strictly positive for \(h>0\). Thus entrywise positivity is governed entirely by the diagonal polynomial \(P_t\). The identity \(L\mathbf1=0\) and \(R(0)=1\) give \(T_t(h)\mathbf1=\mathbf1\), and symmetry gives the column-sum assertion.

**4. Sharp threshold and exact root count.** When \(t=1\),
\[
P_1(h)=5h^4+38h^2+48h+36>0\qquad(h\ge0).
\]
When \(t=2\),
\[
P_2(h)=18\{h^2[2(h-1)^2+1]+4h+2\}>0\qquad(h\ge0).
\]
For each integer \(t\ge3\),
\[
P_t(0)=36>0,\quad P_t(2)=-4(4t+3)(4t^2-8t-9)<0,
\]
and \(P_t(h)\to+\infty\) as \(h\to+\infty\). There are therefore at least two distinct positive roots, one on either side of \(2\). The signs of the ordered quartic coefficients are \((+,-,+,+,+)\) for \(3\le t\le5\), and \((+,-,-,+,+)\) for \(t\ge6\). Both have exactly two sign changes. Descartes' rule permits at most two positive roots, counting multiplicity. Thus the two roots are simple and there are no others. Their signs determine the claimed exact positivity intervals.

**5. Endpoint asymptotics.** For every fixed real \(x\),
\[
\lim_{t\to\infty}P_t(x/t)=-4(2x-3)(2x^2+4x+3).
\]
The only positive zero of the limit is \(x=3/2\), with a strict sign change. Using fixed brackets around that zero, and uniqueness of the root below \(2\), gives \(t h_-(t)\to3/2\). For every fixed \(h>0\),
\[
\lim_{t\to\infty}P_t(h)/t^3=4h^3(h-4).
\]
Strict sign changes at fixed positive points on both sides of \(4\), together with uniqueness of the larger positive root, imply \(h_+(t)\to4\). This proves both limits without assuming monotonicity of the roots.

## Verification
Run `python verify.py` from the same directory as this file. It uses only the Python standard library and exact `fractions.Fraction` arithmetic. On the concrete conference graphs of orders \(5,9,13,17,29\), it constructs \(L\), independently inverts the denominator matrix by rational Gauss--Jordan elimination at eight rational timesteps per graph, and compares all entries with the three polynomial formulas. It also checks the unit row sums and finite parameter sign identities. The expected success output reports 40 exact matrix inversions, 11,240 exact entry identities, 300 exact cutoff witnesses, and 700 diagonal identities. These tests do not replace the infinite proof or establish a literature novelty claim.

## Relationship to prior work
Hairer and Wanner explain Radau IIA collocation and its subdiagonal Padé stability functions; the calculation here resolves a graph-specific *entrywise* sign question rather than scalar \(A\)-stability. Bonaventura and Della Rocca study positivity and absolute monotonicity for TR-BDF2 and other Runge--Kutta methods, not the conference-graph endpoint formula here. Zappavigna, Colaneri, Kirkland and Shorten analyze positivity failures for diagonal Padé approximants and general positive matrices, with no result implying the parameter-specific Radau IIA classification here. The known nine-vertex rook/Hamming case is covered by other graph-family Radau analyses, but no such family includes all larger conference graphs; a Gauss--Legendre classification on strongly regular graphs uses a **different rational function**. The new result isolates a first realized thirteen-vertex failure, a single negative diagonal band, and two sharp large-order scales.

## Limitations
This is a graph-family theorem, not a universal property of Radau IIA on all graphs. The proof does not assert the existence of a conference graph for each parameter or any practical necessity of taking timesteps inside the negative band. The asymptotic is along existing graphs only. No stagewise positivity, higher-order Radau IIA claim, or independent mathematical audit is asserted. A possible prior equivalent treatment in unindexed numerical graph-diffusion or association-scheme literature is not excluded by searches alone.

## References
1. E. Hairer and G. Wanner, *Radau Methods*, in *Encyclopedia of Applied and Computational Mathematics* (2015), DOI: 10.1007/978-3-540-70529-1_139. Public author-provided full text: https://www.researchgate.net/publication/302467919_Radau_Methods
2. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303, first posted 2015-10-14. https://arxiv.org/abs/1510.04303
3. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, preprint dated 2012-01-03. https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf
4. E. W. Weisstein, *Conference Graph*, MathWorld, for standard strongly regular graph parameters and examples. https://mathworld.wolfram.com/ConferenceGraph.html
