# A five-dimensional positivity frontier for cubic inverse-Taylor heat stepping on Boolean cubes

## Finding
Let \(Q_d\) be the unweighted Boolean cube of dimension \(d\geq1\), and let \(L_d\) denote its combinatorial graph Laplacian. Define the cubic inverse-Taylor (the \([0/3]\) Padé) heat update
\[
T_d(h)=\left(I+hL_d+\frac{h^2}{2}L_d^2+\frac{h^3}{6}L_d^3\right)^{-1},\qquad h\geq0.
\]
For **every** \(1\leq d\leq5\), and **every** real \(h>0\), all entries of \(T_d(h)\) are strictly positive. In contrast, on \(Q_6\), for antipodal vertices \(x,y\) (Hamming distance six),
\[
(T_6(1/6))_{xy}=-\frac{26706475}{4942948029056}<0.
\]
This is the smallest cube dimension exhibiting a negative entry at any positive step. For this same antipodal entry, as \(h\downarrow0\),
\[
(T_6(h))_{xy}=50h^6-1260h^7+O(h^8)>0,
\]
and \(\lim_{h\to\infty}(T_6(h))_{xy}=1/64>0\). Thus its sign changes at least twice as a function of the step size. No assertion about all entries, or about positivity throughout a neighborhood, follows solely from the sign of this one entry.

## Assumptions and scope
The graph \(Q_d\) has vertex set \(\{0,1\}^d\); two vertices are adjacent when they differ in precisely one coordinate. All edges have unit conductance and the combinatorial Laplacian is \(L_d=dI-A(Q_d)\), not a normalized Laplacian. The update is the inverse of the cubic Taylor polynomial in \(hL_d\), not the third-degree explicit Taylor polynomial, nor the two-stage Radau or Gauss–Legendre approximation. Invertibility follows since \(1+z+z^2/2+z^3/6>0\) for \(z\geq0\). The claim is restricted to unweighted Boolean cubes, and does not classify other Hamming alphabets or dimensions seven and higher. At \(h=0\), the update is the identity, which has zero off-diagonal entries.

## Proof
**Walsh reduction.** Every Walsh character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) is an eigenvector of \(L_d\), with eigenvalue \(2|S|\). Thus an update entry depends only on Hamming distance \(j=d_H(x,y)\), and its exact expression is
\[
F_{d,j}(h)=\frac1{2^d}\sum_{k=0}^{d}\frac{K_{d,j}(k)}{1+2kh+2k^2h^2+\frac43 k^3h^3},\quad
K_{d,j}(k)=\sum_{\ell=\max(0,k-d+j)}^{\min(j,k)}(-1)^\ell\binom j\ell\binom{d-j}{k-\ell}.
\]
All following transformations are identities in the rational function field \(\mathbb Q(h)\), so no grid of tested step sizes is being extrapolated.

**All six distance classes of \(Q_5\).** Set \(D(h)=\prod_{a=1}^{5}D_a(h)\), with factors
\[
\begin{aligned}
D_1&=4h^3+6h^2+6h+3,\\
D_2&=32h^3+24h^2+12h+3,\\
D_3&=36h^3+18h^2+6h+1,\\
D_4&=256h^3+96h^2+24h+3,\\
D_5&=500h^3+150h^2+30h+3.
\end{aligned}
\]
All factors are strictly positive on \(h\geq0\). Exact rational simplification of the preceding Walsh formula gives
\[
F_{5,j}(h)=\frac{h^jP_j(h)}{D(h)},\qquad j=0,1,\ldots,5.
\]
For \(j=0,1,2,3,4\), **every coefficient** of the polynomial \(P_j\) is a strictly positive integer. The `CHECKER.py` script builds these coefficients from the Walsh formula using exact arithmetic; all coefficient arrays are also supplied in `CERTIFICATE.json`.

For the only non-coefficientwise-positive class, \(j=5\), the exact polynomial is
\[
\begin{split}
P_5(h)={}&810+4050h-16200h^2-364500h^3-774360h^4\\
&+5108400h^5+38066400h^6+93888000h^7\\
&+118225920h^8+63129600h^9+18432000h^{10}.
\end{split}
\]
It is nonetheless strictly positive on the whole half-line. To certify this **without** a numerical-root or sampling argument, write \(t\geq0\). The two degree-ten polynomials
\[
(1+t)^{10}P_5\left(\frac{t}{6(1+t)}\right),\qquad P_5\left(t+\frac16\right)
\]
both have every coefficient strictly positive. Their exact rational coefficient lists (ascending powers) are recorded in `CERTIFICATE.json` and reproduced by `CHECKER.py`. The first covers every \(0\leq h<1/6\) through \(h=t/[6(1+t)]\); the second covers every \(h\geq1/6\) through \(h=t+1/6\). Therefore \(P_5(h)>0\) for all \(h\geq0\). Since \(h^j>0\) for positive \(h\), all \(F_{5,j}(h)>0\) for \(h>0\), proving the full \(32\)-vertex update is strictly positive.

**Lower dimensions.** For \(d<5\), lift any vector on \(Q_d\) to a function on \(Q_5\) constant in its last \(5-d\) coordinates. The cube Laplacians intertwine under this lift, so their rational updates do as well. Consequently every \((x,y)\) entry of \(T_d(h)\) is the sum over all \(2^{5-d}\) extensions \(z\) of \(y\) of the strictly positive entries \((T_5(h))_{(x,0^{5-d}),z}\). Thus all entries of \(T_d(h)\) are strictly positive, for every \(1\leq d\leq5\) and \(h>0\).

**Dimension-six obstruction and sign reentry.** Substitute \(d=j=6\) and \(h=1/6\) in the same finite Walsh sum. Exact fraction arithmetic gives the negative rational value in the finding. Expanding this rational function at zero gives \(50h^6-1260h^7+O(h^8)\). (In fact, the distance-six term first appears in degree six, and the inverse scalar cubic polynomial has coefficient \(5/72\) at degree six.) As \(h\to\infty\), every positive Laplacian eigenmode is annihilated and the constant mode tends to its rank-one projector, hence the antipodal entry tends to \(2^{-6}=1/64\). Continuity implies at least two sign crossings for that entry. This completes the proof.

## Verification
Run `python CHECKER.py` with Python 3 and SymPy. It constructs all six Walsh rational functions in dimension five, tests their exact common denominator and positive coefficient certificates, proves positivity of the two transformed degree-ten polynomials, checks the exact rational negative entry of dimension six, and independently compares the Walsh formula to all \(64\) entries of a directly inverted dimension-three \(8\)-by-\(8\) graph matrix at a rational step. The symbolic expressions in `CERTIFICATE.json` have exactly the stated integer/rational coefficients. These are exact algebraic identity and sign checks, not finite experiments intended to infer positivity for infinitely many steps.

## Relationship to prior work
The cubic rational function is a classical subdiagonal Padé approximation to the exponential, not a new numerical integrator. Zappavigna, Colaneri, Kirkland, and Shorten (2010) analyze positivity-related properties of Padé discretization in positive systems, principally diagonal approximants and co-positive Lyapunov functions; this does not imply the present all-timestep, dimension-five graph-entrywise sign classification. Egert and Rozendaal (2012) develop convergence of subdiagonal Padé approximants to semigroups, which does not assert nonnegativity of individual Boolean-cube transition entries. A previously published exact graph result for the same \([0/3]\) rational function proves positivity on **all** connected unweighted graphs with at most six vertices, and exhibits a negative entry on the seven-vertex path. Its graph-order threshold is compatible with but does not imply the present **cube-dimension** threshold at \(32\) versus \(64\) vertices; the respective first-failure families and sharp questions differ. Published findings for \([0/2]\), two-stage Radau IIA, and Gauss–Legendre heat steps have different rational functions and are not logical implications of this claim.

## Limitations
Only the \([0/3]\) update on ordinary unweighted Boolean cubes is classified here. No assertion is made about the complete set of positive steps in dimension six, about the behavior of every entry after the witnessed failure, or about monotonicity in all larger dimensions. The positivity-side certificate is exact but computer-assisted, using integer and rational polynomial arithmetic. Potential historical mathematical equivalents in specialized positivity literature remain a publication-priority risk. No independent mathematical audit has been performed.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, 2010; public deposit dated 2010-10-15. https://mural.maynoothuniversity.ie/id/eprint/2195/ . Open manuscript: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf .
2. M. Egert and J. Rozendaal, *Convergence of subdiagonal Padé approximations of \(C_0\)-semigroups*, initial arXiv public version 2012, arXiv:1210.8408. https://arxiv.org/abs/1210.8408 .
3. *Seven vertices are sharp for positivity loss of the cubic inverse-Taylor heat step*, publicly indexed mathematical result, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-seven-vertices-are-sharp-for-positivity-loss-of-the-cubic-invers--808c1509a3bb/RESULT.md .
