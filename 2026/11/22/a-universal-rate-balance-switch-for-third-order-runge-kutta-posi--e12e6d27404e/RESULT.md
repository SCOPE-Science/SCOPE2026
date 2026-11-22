# A universal rate-balance switch for third-order Runge–Kutta positivity on bidirected stars

## Finding

**Theorem.** Let \(m\ge2\) be an integer, and let \(a,b>0\). Consider the \((m+1)\)-state continuous-time Markov generator with a hub \(0\) and leaves \(1,\ldots,m\), whose rates from each leaf to the hub equal \(a\) and from the hub to each leaf equal \(b\). Set
\[
 B=mb,\qquad r=\frac{a}{B},\qquad \lambda=a+B,
 \qquad f(z)=1-z+\frac{z^2}{2}-\frac{z^3}{6}.
\]
For the *completed* classical three-stage, third-order Runge–Kutta step
\[
 T(h)=I+hQ+\tfrac12h^2Q^2+\tfrac16h^3Q^3,
\]
let \(u(r)\) be the unique positive real solution of \(f(u)=-r\). Then
\[
\boxed{T(h)\text{ is entrywise nonnegative}\ \Longleftrightarrow\
0\le h\le H=\min\left\{\frac{u(r)}{a+B},\frac3{2a+B}\right\}.}
\]
Exactly one rate-balance threshold decides which obstruction is active, independently of \(m\). Define \(r_*\) as the unique positive root of
\[
 16r^3+9r^2-3r-4=0,\qquad r_*=0.562149661945766\ldots.
\]
When \(0<r<r_*\), a **hub diagonal** first reaches zero at \(H=u(r)/(a+B)\); when \(r>r_*\), all **distinct-leaf transitions** reach zero at \(H=3/(2a+B)\); at \(r=r_*\), both types reach zero simultaneously. No leaf diagonal or hub–leaf transition limits the step. For every \(h>H\), an entry is strictly negative, so positivity cannot return. The switch depends on the ratio of each leaf's return rate to the hub's aggregate departure rate, not on the number of leaves separately.

## Assumptions and scope

The generator acts on row probability distributions. In coordinates,
\[
 Q_{00}=-mb,\quad Q_{0j}=b,\quad Q_{j0}=a,\quad Q_{jj}=-a
 \quad(1\le j\le m),
\]
with all other off-diagonal entries zero. Thus \(Q\mathbf1=0\). The rates and the timestep are real and strictly positive except that \(h=0\) is permitted. The generator is irreducible and reversible, with stationary masses \(\pi_0=a/(a+mb)\), \(\pi_j=b/(a+mb)\). Positivity means nonnegativity of the endpoint matrix applied to *every* nonnegative vector; it does not mean positivity of internal RK stages.

## Proof

**Spectral reduction.** The generator has eigenvalues \(0\), \(-a\) with multiplicity \(m-1\), and \(-\lambda\) with multiplicity one. Decompose leaf vectors into the constant direction, the sum-zero leaf subspace and the hub-versus-leaf direction. For any polynomial \(f\) satisfying \(f(0)=1\), the endpoint matrix \(f(-hQ)\) has exactly four types of entries (here \(f\) is the scalar polynomial in the theorem):
\[
\begin{aligned}
 T_{00}&=\frac{a+B f(\lambda h)}{\lambda},\\
 T_{0j}&=\frac{b}{\lambda}\,[1-f(\lambda h)],
 &T_{j0}&=\frac{a}{\lambda}\,[1-f(\lambda h)],\\
 T_{ij}&=\frac{b}{\lambda}+\frac{a}{m\lambda}f(\lambda h)-\frac1m f(ah)\quad(i\ne j;\ i,j\ge1),\\
 T_{jj}&=\frac{b}{\lambda}+\frac{a}{m\lambda}f(\lambda h)
             +\left(1-\frac1m\right)f(ah).
\end{aligned}
\]
These are also obtained by multiplying \(Q\) three times. The row sums equal one automatically.

**Only two obstructions.** The identity
\[
1-f(z)=z\left(1-\frac z2+\frac{z^2}6\right)>0\quad(z>0)
\]
holds because the bracket has negative discriminant and positive leading coefficient. Thus both hub–leaf directions are strictly positive for every \(h>0\). For distinct leaves,
\[
\boxed{T_{ij}(h)=\frac{ab h^2}{6}[3-(2a+B)h]}. 
\]
These entries are positive for \(0<h<h_L=3/(2a+B)\), zero at \(h_L\) and negative at every \(h>h_L\).

The scalar derivative is
\[
 f'(z)=-\frac{(z-1)^2+1}{2}<0.
\]
Consequently \(T_{00}\) and \(T_{jj}\) are each strictly decreasing in \(h\), as their scalar-polynomial coefficients are positive. Since \(T_{00}(0)=1\) and \(T_{00}(h)\to-\infty\), the hub diagonal has one positive zero \(h_C=u(r)/\lambda\). We must rule out a leaf diagonal crossing earlier than the first of \(h_C,h_L\).

At the leaf-pair cutoff \(h_L\), direct substitution with \(r=a/B\) yields
\[
\boxed{T_{jj}(h_L)=\frac{r^3+9r^2+6r+2}{2(2r+1)^3}>0.}
\]
By strict monotonicity, every leaf diagonal remains positive throughout \([0,h_L]\). Thus only the hub diagonal and the distinct-leaf transition can limit positivity. Their negative signs persist above their respective zeros, which proves the claimed exact interval and no-reentry assertion.

**Dimension-free rate switch.** At \(h=h_L\), another exact substitution gives
\[
 T_{00}(h_L)=\frac{16r^3+9r^2-3r-4}{2(2r+1)^3}.
\]
The numerator \(F(r)\) satisfies \(F(0)=-4\), \(F(1)=18\), and
\[
 F'(r)=3(2r+1)(8r-1).
\]
It decreases from zero to \(r=1/8\) and then increases strictly, so it has exactly one positive zero. Its sign decides whether the strictly decreasing hub diagonal has already crossed zero by \(h_L\): negative means \(h_C<h_L\), positive means \(h_C>h_L\), and zero means equality. None of the equations defining \(r_*\) depend separately on the number \(m\) of leaves. This proves the phase classification.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The checker confirms the projector-derived entry formulas symbolically, proves the displayed cutoff-substitution and derivative identities by symbolic simplification, and independently compares all matrix-entry types with exact rational powers of \(Q\) for six leaf counts, seven rate pairs and three timesteps. It also checks exact phase witnesses and locates the positive cubic root numerically as a cross-check. Its output is in `verify_output.txt`. These 7,623 exact rational matrix-entry comparisons are finite supplementary evidence; the proof for all \(m,a,b,h\) is the algebra and inequalities above.

For concrete boundary cases, with \(m=2\) and \(a=b=1\), the hub diagonal fails first: \(h_C\approx0.7180571651\), while \(h_L=3/4\). With \(m=2\), \(a=2\) and \(b=1\), the distinct-leaf transitions fail first at \(h_L=1/2\); the completed endpoint matrix at that timestep is
\[
 \begin{pmatrix}1/3&1/3&1/3\\2/3&1/3&0\\2/3&0&1/3\end{pmatrix}.
\]

## Relationship to prior work

General positivity and SSP results give sufficient time-step restrictions for broad ODE classes, and Horváth, Song and Terlaky give a general polynomial-root method for invariance-preserving steps. Blanes, Iserles and Macnamara study positivity of graph-Laplacian ODEs and construct alternative positivity-preserving integrators. Neither inspected paper states this exact rate-balance phase diagram. A published complete-multipartite calculation gives cubic-RK positivity for **common undirected edge conductance**; on a star it includes \(a=b\) but does not allow independent inward and outward rates. Another published bidirected-star calculation covers **fourth-order RK**, where the relevant obstruction is instead a hub–leaf edge. These statements do not imply the cubic phase switch: changing the RK polynomial changes which matrix entries may become negative. The new mathematical content claimed here is the exhaustive dimension-free two-mechanism classification and its sharp rate-ratio crossover, not the polynomial, star eigenvalues, or general polynomial-invariance framework.

## Limitations

The theorem concerns the completed classical cubic RK step for constant-rate homogeneous leaves; it does not cover arbitrary leaf-specific rates, general birth–death networks, nonlinear dynamics or positivity of stages. Positivity at the endpoint is distinct from accuracy and scalar absolute stability. Full historical priority, especially against differently phrased older specialist positivity calculations, is not independently established.

## References

1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242v1 (first public February 16, 2021), later *Positivity-preserving methods for ordinary differential equations*, ESAIM M2AN 56 (2022), 1843–1870, https://arxiv.org/abs/2102.08242 and https://doi.org/10.1051/m2an/2022042.
2. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, Discrete Contin. Dyn. Syst. 35 (2015), 2997–3013, https://doi.org/10.3934/dcds.2015.35.2997.
3. *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, public research note (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-positivity-radii-and-an-order-three-reversal-for-taylor-ru--0aa3ec090e79/RESULT.md.
4. *An exact one-edge positivity horizon for fourth-order Runge–Kutta on bidirected stars*, public research note (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-an-exact-one-edge-positivity-horizon-for-fourth-order-runge-kutt--17dd482823b8/RESULT.md.
