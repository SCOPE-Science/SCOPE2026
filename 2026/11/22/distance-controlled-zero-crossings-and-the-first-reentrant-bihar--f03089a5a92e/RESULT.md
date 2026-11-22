# Distance-controlled zero crossings and the first reentrant biharmonic heat kernel on Boolean cubes

## Finding
For every integer \(d\ge1\), let \(Q_d\) be the unweighted Boolean cube with vertex set \(\{0,1\}^d\), combinatorial Laplacian \(L_d=dI-A_d\), and squared-Laplacian heat semigroup
\[
H_d(t)=\exp(-tL_d^2),\qquad t\ge0.
\]
For distinct vertices at Hamming distance \(r\in\{1,\ldots,d\}\), their common entry \(h_{d,r}(t)\) has **at most** \(\lfloor r/2\rfloor\) zeros on \((0,\infty)\), **counted with multiplicity**. This bound is independent of cube dimension. At distance one, every entry is positive at every positive time. At each distance two or three, the entry has exactly one simple positive zero, being negative before it and positive after it.

The bound is sharp already for \(d=r=4\): antipodal entries of \(H_4(t)\) change sign **twice**, from positive to negative and back to positive. This is the smallest cube dimension permitting two positive-time zero crossings of a single entry. Define \(x=e^{-4t}\in(0,1)\) and
\[
\begin{aligned}
P_2(x)&=1-2x^4+x^{16},\\
P_3(x)&=1-2x+2x^9-x^{16},\\
P_4(x)&=1-4x+6x^4-4x^9+x^{16}.
\end{aligned}
\]
Then \(h_{4,r}(t)=P_r(x)/16\) for \(r=2,3,4\). Let \(\tau_{4,-}<\tau_{4,+}\) be the two strictly positive zeros of \(P_4(e^{-4t})\), and let \(\tau_2,\tau_3\) be the unique positive zeros of \(P_2(e^{-4t})\), \(P_3(e^{-4t})\). They obey the **strictly ordered** sequence
\[
0<\tau_{4,-}<\tau_2<\tau_3<\tau_{4,+},
\]
with approximate values \(0.0180433350\), \(0.0380861165\), \(0.1722802964\), and \(0.3401695302\), respectively. The antipodal kernel is positive on \((0,\tau_{4,-})\cup(\tau_{4,+},\infty)\), negative on \((\tau_{4,-},\tau_{4,+})\), and zero at the two endpoints.

The **complete entrywise-positivity horizon** for the four-cube is
\[
\boxed{\ H_4(t)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad t=0\ \text{or}\ t\ge\tau_{4,+}.\ }
\]
At \(t=\tau_{4,+}\) only antipodal off-diagonal entries vanish; every other entry is strictly positive. The exact induced norm on both \(\ell^1\) and \(\ell^\infty\) is, for every \(t\ge0\),
\[
\boxed{\ \|H_4(t)\|_{1\to1}=\|H_4(t)\|_{\infty\to\infty}
=1+\frac18\Big(6[-P_2(x)]_++4[-P_3(x)]_++[-P_4(x)]_+\Big),\quad [u]_+=\max(u,0).\ }
\]
In particular this norm is strictly greater than one at every \(0<t<\tau_{4,+}\), and equals one at zero and for all later times.

## Assumptions and scope
Cubes have unit conductances and their **unnormalized** graph Laplacian \(dI-A_d\). Matrix entries refer to the standard vertex indicator basis of \(\ell^2(\{0,1\}^d)\); the induced \(\ell^1\) and \(\ell^\infty\) norms are coordinate endpoint norms. Positivity means entrywise nonnegativity, not positive semidefiniteness (the semigroup is automatically positive semidefinite). All temporal zeros are counted with their analytic multiplicities on the open positive half-line. The global zero bound is an upper bound for distances at least four, not an assertion that all possible zeros always occur. No statement is made for weighted cubes, graph families with other spectra, or fractional powers other than the squared Laplacian.

## Proof
**1. Walsh spectral expansion.** For each subset \(S\subseteq\{1,\ldots,d\}\), its character \(\chi_S(u)=(-1)^{\sum_{i\in S}u_i}\) is a Laplacian eigenvector with eigenvalue \(2|S|\). Consequently for vertices \(u,v\) at distance \(r\), writing \(x=e^{-4t}\),
\[
2^d h_{d,r}(t)=P_{d,r}(x)=\sum_{k=0}^{d}c_{d,r,k}x^{k^2},\qquad
c_{d,r,k}=\sum_j(-1)^j\binom rj\binom{d-r}{k-j}.
\]
Here binomial coefficients outside their natural ranges are zero. In particular \(c_{d,r,0}=1\), so \(h_{d,r}(t)\to2^{-d}>0\) as \(t\to\infty\), and \(P_{d,r}(1)=0\) for \(r>0\).

**2. Dimension-independent variation bound.** The elementary counting identity
\[
\binom rj\binom{d-r}{k-j}
=\frac{\binom dk}{\binom dr}\binom kj\binom{d-k}{r-j}
\]
shows that \(c_{d,r,k}=\binom dk K_r(k)/\binom dr\), where
\[
K_r(y)=\sum_{j=0}^r(-1)^j\binom yj\binom{d-y}{r-j}
\]
is a polynomial of **degree exactly \(r\)** in the real variable \(y\): its leading coefficient is \((-2)^r/r!\). Since the prefactor is positive for \(0\le k\le d\), the nonzero coefficient sequence \(c_{d,r,0},\ldots,c_{d,r,d}\) has at most \(r\) sign changes. Indeed each successive sign reversal gives a distinct real zero of the degree-\(r\) polynomial between the corresponding integer arguments, even if intermediate coefficient values are zero. By Descartes' rule of signs, the ordinary polynomial \(P_{d,r}(x)\) has at most \(r\) positive roots counted with multiplicity; missing powers contribute no sign changes.

**3. The known zero at time zero has exact multiplicity.** Put \(m=\lceil r/2\rceil\). The Taylor expansion
\[
h_{d,r}(t)=\sum_{j\ge0}\frac{(-t)^j}{j!}(L_d^{2j})_{uv}
\]
vanishes termwise for \(2j<r\), because the Laplacian has nonzero entries only on the diagonal and between adjacent vertices. If \(r=2q\), the first nonzero term comes from a shortest adjacency walk of length \(2q\), of which there are \((2q)!\), and
\[
h_{d,2q}(t)=(-1)^q\frac{(2q)!}{q!}\,t^q+O_d(t^{q+1}).
\]
If \(r=2q+1\), parity excludes an adjacency walk of length \(r+1=2q+2\), while the unique contribution in \((dI-A_d)^{r+1}\) of adjacency degree \(r\) is \(-(r+1)dA_d^r\). Thus
\[
h_{d,2q+1}(t)=(-1)^q\frac{2d(2q+1)!}{q!}\,t^{q+1}+O_d(t^{q+2}).
\]
Both leading coefficients are nonzero. Hence \(x=1\), corresponding to \(t=0\), is a positive root of \(P_{d,r}\) of multiplicity exactly \(m\). Subtracting this multiplicity from the Descartes bound yields at most \(r-\lceil r/2\rceil=\lfloor r/2\rfloor\) other positive roots, hence the claimed bound on \(t>0\).

At distance one, this bound is zero and the small-time sign is positive, so positivity holds at every positive time. For distances two and three the small-time sign is negative, while the limiting value at infinity is positive. The bound permits at most one positive zero counted with multiplicity, and the intermediate value theorem supplies at least one; it must be simple and the asserted sign pattern follows.

**4. Sharpness and full four-cube transitions.** For \(d=4\), the Walsh expansion yields the three polynomials in the finding, together with
\[
P_0(x)=1+4x+6x^4+4x^9+x^{16},\qquad
P_1(x)=1+2x-2x^9-x^{16}.
\]
Both are strictly positive on \(0<x<1\), since \(P_1=(1-x^{16})+2(x-x^9)\). The distance-two and distance-three sign patterns follow from Step 3. For distance four, \(P_4(1)=P_4'(1)=0\), but \(P_4''(1)=24>0\), so the near-zero-time entry is positive. The five nonzero coefficient signs of \(P_4\) are \(+,-,+,-,+\), giving at most four positive real roots; two of them, counted with multiplicity, lie at \(x=1\). Exact rational substitutions show
\[
\begin{aligned}
&P_4(25/100)>0>P_4(26/100),\\
&P_4(93/100)<0<P_4(94/100).
\end{aligned}
\]
The two disjoint brackets therefore contain exactly one simple positive root apiece; there is no room for any other positive root. Because \(x=e^{-4t}\) decreases in time, the larger bracket gives the first crossing and the smaller bracket the last crossing. The other two exact rational brackets
\[
P_2(85/100)>0>P_2(86/100),\qquad
P_3(50/100)>0>P_3(51/100)
\]
place their unique roots strictly between the two distance-four roots in the order claimed. Hence for \(0<t<\tau_{4,+}\) at least one of the distance-two, distance-three, or antipodal classes has a negative entry, while at the final crossing only antipodal entries vanish and all other classes are positive. For later times every class is strictly positive. Since dimensions at most three have distances at most three, the two-crossing phenomenon first appears at dimension four.

**5. Sharp norm formula.** Every row and column of \(H_4(t)\) sums to one, because \(L_4\mathbf1=0\), and symmetry and cube automorphisms make all rows equivalent. Each row has \(\binom4r\) entries at distance \(r\), each equal to \(P_r(x)/16\). For any real row summing to one, the absolute sum equals one plus twice the mass of its negative entries. Only the classes \(r=2,3,4\) can be negative, yielding exactly the displayed norm formula. Symmetry equates column and row norms.

## Verification
The standalone `verify.py` uses only Python's standard library. It reconstructs integer graph Laplacians and Walsh eigenvectors for dimensions one through seven, verifies the binomial spectral coefficients and Taylor support order, evaluates the root-separating rational brackets exactly using `fractions.Fraction`, checks the four-cube polynomials and boundary multiplicities, and compares the displayed norm with independent signed row sums at 200 times. It also checks the kernel formula against direct Walsh-mode sums at six sample times for every ordered pair of four-cube vertices. Execute `python verify.py`; the recorded output is `VERIFY_OK 24179 exact and numerical checks`. The proof of the all-dimensional zero bound is the degree/sign-variation and Taylor argument, **not** the finite checker.

## Relationship to prior work
Arora [1] develops the general theory of locally eventually positive semigroups, with applications including squared Laplacians on domains; those analytic sufficient criteria do not bound positive-time zeros of individual Hamming-cube entries or provide the sharp four-cube phase diagram. Daners–Glück–Mui [2] analyze local eventual positivity for continuous biharmonic heat equations, a different underlying operator. The published rectangular-rook-graph theorem [3] treats \(\exp(-tL^2)\) on \(K_a\square K_b\), proving a single threshold there; although \(Q_2\cong K_2\square K_2\), a four-cube \(Q_4\cong K_2^{\square4}\) is not in that two-factor family and has a five-level spectrum rather than the relevant four-level rook projection structure. A separate published Radau IIA analysis [4] treats \(Q_4\) but evaluates a **rational timestep map of \(L\)**, not the exponential of \(-tL^2\); its positivity intervals do not imply the present sign changes. The contribution is the Hamming-distance zero-count bound for all cube dimensions, the sharp first double crossing, and the complete four-cube norm/positivity classification, not Walsh diagonalization or eventual positivity in general.

## Limitations
The zero bound for distances at least four need not be attained; a full census of crossings for all \(d,r\) is not claimed. The exact multi-stage sign diagram and operator norm are determined only for the unweighted four-cube; no general maximum norm formula for all dimensions is asserted. The isolation decimals are illustrative only; the defining polynomials, rigorous root counts and rational brackets supply exact identification. The source search is non-exhaustive, and equivalent formulas may exist in earlier association-scheme or discrete biharmonic kernel literature. No independent mathematical audit has been performed.

## References
[1] S. Arora, *Locally Eventually Positive Operator Semigroups*, first public arXiv version 2021-01-27, arXiv:2101.11386, https://arxiv.org/abs/2101.11386 .

[2] D. Daners, J. Glück, J. Mui, *Local uniform convergence and eventual positivity of solutions to biharmonic heat equations*, first public arXiv version 2021-11-04, arXiv:2111.02753, https://arxiv.org/abs/2111.02753 .

[3] *Exact positivity horizon and peak amplification of biharmonic heat on rook graphs*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-positivity-horizon-and-peak-amplification-of-biharmonic-he--621e2ef18776 .

[4] *Sharp Radau positivity loss and reentry on Boolean hypercubes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-radau-positivity-loss-and-reentry-on-boolean-hypercubes--093b06a03097 .
