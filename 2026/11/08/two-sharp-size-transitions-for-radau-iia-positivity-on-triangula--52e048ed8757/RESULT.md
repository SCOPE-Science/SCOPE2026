# Two sharp size transitions for Radau IIA positivity on triangular graph diffusion

## Finding

Let \(n\ge4\) be an integer, and let the vertices of the triangular graph \(T_n=J(n,2)\) be the two-element subsets of \(\{1,\ldots,n\}\), with adjacency when distinct subsets intersect. Let \(L\) be its unweighted combinatorial Laplacian. The completed two-stage, order-three Radau IIA end-step for \(u'=-Lu\), at timestep \(h\ge0\), is
\[
  T_n(h)=R(hL),\qquad R(z)=\frac{6-2z}{z^2+4z+6}.
\]

Write
\[
\begin{aligned}
D_n(h)&=(n^2h^2+4nh+6)\bigl(4(n-1)^2h^2+8(n-1)h+6\bigr),\\
Q_n(h)&=18+48h+(-5n^2+26n+24)h^2\\
&\quad+(-2n^3-2n^2+40n-24)h^3+4n(n-1)h^4,\\
E_n(h)&=36+(18n+60)h-4(n^2-19n+12)h^2+8n(n-1)h^3,\\
H_n(h)&=4h^2\bigl(2n(n-1)h^2+6(3n-2)h+18\bigr).
\end{aligned}
\]

**Exact entry formula and phase diagram.** Every diagonal entry of \(T_n(h)\) is \(2Q_n(h)/D_n(h)\); every entry indexed by adjacent distinct vertices is \(hE_n(h)/D_n(h)\); and every entry indexed by nonadjacent distinct vertices is \(H_n(h)/D_n(h)\). Thus:

1. For \(n=4,5\), \(T_n(h)\) is entrywise nonnegative for all \(h\ge0\).
2. For every \(n\ge6\), \(Q_n\) has exactly two simple positive roots \(0<d_n^-<d_n^+\). The diagonal is negative exactly for \(d_n^-<h<d_n^+\) and nonnegative otherwise.
3. For \(4\le n\le74\), every adjacent-vertex entry is positive at every \(h>0\). For \(n\ge75\), \(E_n\) has exactly two simple positive roots \(0<e_n^-<e_n^+\), and each adjacent-vertex entry is negative exactly for \(e_n^-<h<e_n^+\).
4. Every nonadjacent-vertex entry is positive for all \(n\ge4\), \(h>0\).

Consequently the exact nonnegative-timestep set is
\[
\boxed{\{h\ge0:T_n(h)\ge0\ \text{entrywise}\}=\{h\ge0:Q_n(h)\ge0,\ E_n(h)\ge0\}.}
\]
The two distinct graph-size thresholds are **\(n=6\)** for loss of nonnegative self-transitions and **\(n=75\)** for loss of nonnegative adjacent transitions. The matrices are symmetric and have every row and column sum equal to one at all timesteps, even when some entries are negative.

## Assumptions and scope

The graph is simple, unweighted, undirected, and triangular: \(T_n\) has \(\binom n2\) vertices and degree \(2(n-2)\). The claim concerns the **completed Radau IIA end-step matrix only**, not positivity of either internal Runge–Kutta stage, of an arbitrary semidiscretization, or of a different rational heat filter. The nonnegative-matrix comparison includes zero entries; at \(h=0\), \(T_n(0)=I\). All root thresholds are exact algebraic quantities, not decimal approximations.

## Proof

**1. Spectrum and polynomial interpolation.** Let \(B\) denote the vertex–edge incidence matrix of the complete graph \(K_n\). For the adjacency matrix \(A\) of \(T_n\), \(B^\mathsf TB=2I+A\) and \(BB^\mathsf T=(n-2)I+J\). Its adjacency eigenvalues are therefore \(2(n-2)\), \(n-4\), and \(-2\), with multiplicities \(1\), \(n-1\), and \(n(n-3)/2\) respectively. Thus \(L=2(n-2)I-A\) has precisely the distinct eigenvalues \(0\), \(x=n\), and \(y=2(n-1)\).

Since \(R(0)=1\), interpolation over these three eigenvalues gives \(R(hL)=I+B_hL+C_hL^2\), with
\[
\begin{aligned}
B_h&=-\frac{h\bigl[h^3xy(x+y)+h^2(6x^2+10xy+6y^2)+24h(x+y)+36\bigr]}{(h^2x^2+4hx+6)(h^2y^2+4hy+6)},\\
C_h&=\frac{h^2\bigl[h^2xy+6h(x+y)+18\bigr]}{(h^2x^2+4hx+6)(h^2y^2+4hy+6)}.
\end{aligned}
\]
These expressions follow directly by solving the two linear equations \(B_h+\xi C_h=(R(h\xi)-1)/\xi\) for \(\xi=x,y\). Their denominators are strictly positive for \(h\ge0\).

**2. The three entry types.** The graph is strongly regular with degree \(k=2(n-2)\), adjacent common-neighbor number \(\lambda=n-2\), and nonadjacent common-neighbor number \(\mu=4\). Hence the entries of \(L\) and \(L^2\) are
\[
\begin{array}{c|cc}
&L_{ij}&(L^2)_{ij}\\\hline
 i=j&k&k^2+k\\
 i\sim j&-1&\lambda-2k=-3(n-2)\\
 i\not\sim j,\ i\ne j&0&4.
\end{array}
\]
Substituting \(x=n\), \(y=2(n-1)\) into \(I+B_hL+C_hL^2\), followed by collecting rational-polynomial coefficients, gives the displayed three entry formulas. In particular \(D_n(h)>0\) for all \(h\ge0\), and \(H_n(h)>0\) for \(h>0\). As \(L\mathbf1=0\) and \(R(0)=1\), row sums equal one; symmetry gives column sums.

**3. The first sharp threshold.** For \(n=4\),
\[
Q_4(h)=18+48h+45h^2+3h^2(4h-1)^2>0\qquad(h\ge0).
\]
For \(n=5\), \(Q_5(h)=18+48h+29h^2-124h^3+80h^4\). On \(0\le h\le3/4\),
\[
 Q_5(h)\ge18+48h-64h^2\ge18.
\]
For \(h=t+3/4\) with \(t\ge0\), direct expansion gives
\[
Q_5(h)=80t^4+116t^3+20t^2+\frac{69}{4}t+\frac{693}{16}>0.
\]
For \(n\ge6\), evaluate at the single exact timestep \(h=1\):
\[
Q_n(1)=-2n^3-3n^2+62n+66<0.
\]
The expression is already negative at \(n=6\) and strictly decreases for real \(n\ge6\). The coefficient sequence of \(Q_n\), read from highest to lowest power, has two sign changes: it is \((+,-,-,+,+)\) for \(n\ge7\) and \((+,-,0,+,+)\) for \(n=6\). Descartes' rule permits at most two positive roots counted with multiplicity. Since \(Q_n(0)=18>0\), \(Q_n(1)<0\), and the leading coefficient is positive, the intermediate value theorem supplies at least two distinct positive roots. Thus there are exactly two, both simple, with the asserted signs.

**4. The second sharp threshold.** Put \(z=nh\). A direct expansion yields
\[
E_n(z/n)=36+(18+60/n)z+(-4+76/n-48/n^2)z^2+(8/n-8/n^2)z^3.
\]
For every real \(n\ge4\) and \(z>0\), differentiation with respect to \(n\) gives
\[
\frac{\partial}{\partial n}E_n(z/n)=-\frac{60nz+(76n-96)z^2+(8n-16)z^3}{n^3}<0.
\]
At the largest proposed positive case, \(n=74\),
\[
E_{74}(h)=43216h^3-16328h^2+1392h+36.
\]
Its exact cubic discriminant is \(-24660792741888<0\), so it has exactly one real root. Because the leading coefficient is positive and \(E_{74}(0)=36>0\), that root is negative. Therefore \(E_{74}(h)>0\) for all \(h\ge0\); by the displayed strict decrease after scaling, \(E_n(h)>0\) for all integers \(4\le n\le74\), \(h\ge0\).

In contrast,
\[
E_n(1/5)=-\frac{6}{125}(2n^2-137n-960)<0\qquad(n\ge75).
\]
Here the quadratic factor is positive at \(n=75\) and strictly increasing thereafter. The constant and leading coefficients of \(E_n\) are positive, so the intermediate value theorem gives two distinct positive roots, one on either side of \(1/5\). The coefficient signs of the cubic \(E_n\), highest degree first, are \((+,-,+,+)\) for \(n\ge75\), and Descartes' rule yields at most two positive roots counted with multiplicity. Both roots are therefore simple and give exactly the claimed negative band.

Combining steps 2–4 proves the classification.

## Verification

The standalone standard-library program `check.py` performs exact rational checks of the matrix identity \((h^2L^2+4hL+6I)T_n(h)=6I-2hL\) for \(n=4,\ldots,8\) and five rational positive steps each, using the explicit combinatorial adjacency matrix. It also verifies mass conservation, matrix symmetry, the cubic discriminant at \(n=74\), the exact negative witnesses at \(n\ge75\), and polynomial identities over a broad parameter set. Run `python3 check.py` in the directory containing this document. The general statements rely on the proof above, not on finitely many tests.

## Relationship to prior work

General rational absolute monotonicity and strong-stability-preservation theory supplies important sufficient conditions and restrictions for positivity of time integrators, but not these exact graph-dependent entrywise threshold values. Ketcheson–Macdonald–Gottlieb (2008) analyze implicit SSP Runge–Kutta methods and general linear stability-function theory. Zappavigna–Colaneri–Kirkland–Shorten (2012) give positive-systems counterexamples and sufficient conditions for **diagonal** Padé approximants, not this Radau \([1/2]\) filter. Bonaventura–Della Rocca (2015) examine TR-BDF2, including the general absolute-monotonicity framework and related implicit schemes. The standard triangular-graph spectrum gives the algebraic starting point, but does not itself state either timestep-sign phase diagram. The result is a specialized, direct classification and does **not** claim a new general SSP theorem.

## Limitations

The result concerns the endpoint update only, and exactly the unweighted family \(J(n,2)\). Its proofs do not establish positivity of internal stages, other graph families, differently weighted edges, nonlinear dynamics, or all higher-order methods. Other mathematically equivalent presentations in specialist numerical-analysis or association-scheme literature remain a possible publication-priority risk; no claim of independent external validation is made.

## References

- D. I. Ketcheson, C. B. Macdonald, S. Gottlieb, *Optimal Implicit Strong Stability Preserving Runge–Kutta Methods* (author manuscript dated 21 February 2008), https://www.davidketcheson.info/assets/papers/implicit_ssp_postprint.pdf.
- A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems* (manuscript dated 3 January 2012), https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf.
- L. Bonaventura, A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions* (first arXiv submission 14 October 2015), https://arxiv.org/abs/1510.04303.
- E. W. Weisstein, *Triangular Graph*, MathWorld, https://mathworld.wolfram.com/TriangularGraph.html (standard graph definitions and adjacency parameters).
