# Five-vertex positivity boundary for fourth-order Gauss graph-heat steps on cycles

## Finding
Let \(C_n\) be the simple unweighted cycle on \(n\ge3\) vertices, with combinatorial Laplacian \(L_n\). The two-stage Gauss–Legendre Runge–Kutta endpoint update for graph heat diffusion, at any nondimensional timestep \(h\ge0\), is
\[
T_n(h)=F(hL_n),\qquad F(x)=\frac{x^2-6x+12}{x^2+6x+12}.
\]
**Theorem.** The matrix \(T_n(h)\) is entrywise nonnegative for every \(h\ge0\) if and only if \(n\in\{3,4,5\}\). For each of these three cycle sizes, \(T_n(h)\) is entrywise strictly positive for every \(h>0\). More sharply, for every \(n\ge6\), the neighboring-vertex entry \([T_n(8)]_{0,1}\) is strictly negative; the same entry is negative for all sufficiently large \(h\) (with the large-step threshold allowed to depend on \(n\)).

For \(n=6\), the common-step witness has the exact value
\[
[T_6(8)]_{0,1}=-\frac{6584}{580537}.
\]
The transition matrices always have row and column sums equal to one, so the theorem is specifically about entrywise positivity, not mass conservation or spectral stability.

## Assumptions and scope
Vertices are the residue classes modulo \(n\); each vertex is connected to its two neighbors with weight one. The cycle has \(n\ge3\), so there are no multi-edges or loops. Set \(S e_j=e_{j+1}\) with periodic indices, and \(L_n=2I-S-S^{-1}\). The equation is \(u'=-L_nu\), and \(T_n(h)\) is its **completed endpoint** step, not a statement about the intermediate Runge–Kutta stages. The scaling \(h\) absorbs a common edge conductance and spatial mesh factor. Positivity means every matrix entry is nonnegative for all nonnegative initial vectors; stochasticity follows independently from \(F(0)=1\) and symmetry.

## Proof
**1. Exact small-cycle entries.** The denominator \(x^2+6x+12\) is strictly positive for every real nonnegative \(x\), so \(T_n(h)\) exists for \(h\ge0\). For each row, entries depend only on the cyclic distance \(d=\min\{|i-j|,n-|i-j|\}\). Writing \(t_{n,d}(h)\) for that entry, exact rational simplification gives:

For \(n=3\), with \(D_3=3h^2+6h+4\),
\[
t_{3,0}=\frac{3h^2-2h+4}{D_3},\qquad t_{3,1}=\frac{4h}{D_3}.
\]
The diagonal numerator equals \(3(h-1/3)^2+11/3>0\).

For \(n=4\), with \(D_4=(h^2+3h+3)(4h^2+6h+3)\),
\[
\begin{aligned}
t_{4,0}&=\frac{4h^4+3h^3+6h^2+9h+9}{D_4},\\
t_{4,1}&=\frac{3h(h^2+3h+3)}{D_4},\\
t_{4,2}&=\frac{9h^2(h+1)}{D_4}.
\end{aligned}
\]
For \(n=5\), with \(D_5=25h^4+150h^3+360h^2+360h+144\),
\[
\begin{aligned}
t_{5,0}&=\frac{25h^4+30h^3+72h^2+72h+144}{D_5},\\
t_{5,1}&=\frac{72h(h+2)}{D_5},\\
t_{5,2}&=\frac{12h^2(5h+6)}{D_5}.
\end{aligned}
\]
Every listed numerator and denominator is nonnegative on \(h\ge0\), and all numerators are strictly positive when \(h>0\). These identities may be checked algebraically from \(T_n=I-12hL_n((hL_n)^2+6hL_n+12I)^{-1}\). Hence the stated positive cases are proved.

**2. A structural obstruction for every larger cycle.** Let \(L_n^+\) be the Moore–Penrose inverse. The zero-mean cycle Green kernel has exact entries
\[
(L_n^+)_{0,d}=\frac{n^2-1}{12n}-\frac{d(n-d)}{2n},\qquad 0\le d<n.
\]
To verify it, the row sum of the displayed sequence is zero and its cyclic second difference is \(\mathbf 1_{d=0}-1/n\). Thus it is the inverse of \(L_n\) on the orthogonal complement of the constants. At distance one,
\[
(L_n^+)_{0,1}=\frac{(n-1)(n-5)}{12n}.
\]
Since \(F(x)=1-12/x+O(x^{-2})\) as \(x\to+\infty\), spectral calculus on the strictly positive eigenvalues of \(L_n\) gives
\[
T_n(h)=I-\frac{12}{h}L_n^++O_n(h^{-2})\qquad(h\to\infty).
\]
Therefore
\[
[T_n(h)]_{0,1}=-\frac{(n-1)(n-5)}{nh}+O_n(h^{-2})<0
\]
for all sufficiently large \(h\) whenever \(n\ge6\). This proves necessity of \(n\le5\) without finite enumeration.

**3. One common finite witness step for all larger cycles.** For \(n=6\), direct rational evaluation at \(h=8\) gives the displayed negative fraction. For \(n\ge7\) we use the infinite-lattice Fourier coefficients at the same step. Put
\[
\begin{aligned}
s&=3+i\sqrt3,\quad \Delta=\sqrt{s(s+32)}=u+iv,\\
u&=\sqrt{51+2\sqrt{921}},\quad v=\sqrt{2\sqrt{921}-51},\\
r&=\frac{s+16-\Delta}{16},\quad A=\frac{1-i\sqrt3}{2}.
\end{aligned}
\]
Take the square-root branch with positive real part. The resolvent identity for \(s+16-8(z+z^{-1})\), valid for \(0<|r|<1\), and the partial fraction decomposition of \(F\) show that the nonzero-distance Fourier coefficients are
\[
a_j=-24\operatorname{Re}\!\left(\frac{A r^j}{\Delta}\right)\quad(j\ge1).
\]
In particular,
\[
a_1=-\frac{3(22u-4\sqrt{921}-18\sqrt3v)}{16\sqrt{921}}<-0.086.
\]
The elementary rational enclosures
\[
\begin{aligned}
30.34798&<\sqrt{921}<30.34799,\\
1.73205&<\sqrt3<1.73206,\\
10.5686&<u<10.5687,\\
3.1138&<v<3.1139
\end{aligned}
\]
follow from squaring their rational endpoints. They imply \( |r|<0.54\), \(|A/\Delta|<0.091\), and the strict bound on \(a_1\) above. Periodization gives the exact cycle coefficient
\[
[T_n(8)]_{0,1}=a_1+\sum_{k=1}^{\infty}(a_{kn-1}+a_{kn+1}),
\]
where the sum converges absolutely. For \(n\ge7\), its correction obeys
\[
\left|\sum_{k\ge1}(a_{kn-1}+a_{kn+1})\right|
\le24(0.091)\frac{0.54^{n-1}+0.54^{n+1}}{1-0.54^n}
\le24(0.091)\frac{0.54^6+0.54^8}{1-0.54^7}<0.071.
\]
Consequently \([T_n(8)]_{0,1}<-0.015\) for all \(n\ge7\). Together with the exact \(n=6\) calculation, this proves the uniform finite-step assertion and completes the theorem.

## Verification
The accompanying self-contained Python 3 script `verify.py` uses only rational arithmetic and the standard library. It checks all the small-cycle rational identities through exact rational interpolation: clearing denominators gives a polynomial of degree at most \(4n\); agreement at \(4n+1\) different nonnegative rational timesteps proves each identity for every \(h\). The script also verifies the exact \(n=6\) entry, all rational endpoint inequalities supporting the uniform Fourier tail bound, and a family of Green-function identities as supplementary checks. Execute `python verify.py`; the expected output begins `VERIFY_OK`.

## Relationship to prior work
Lóczi and Ketcheson (arXiv:1303.6651, first posted March 26, 2013) established that the \([2/2]\) Padé stability function has zero radius of absolute monotonicity. That global restriction does **not** imply the exact cutoff for the fixed cyclic graph-heat family; it neither identifies positive cycles nor forces the particular neighboring entry to become negative. Fekete, Ketcheson and Lóczi (arXiv:1610.00228, first posted October 2, 2016) analyzed periodic finite-difference heat discretizations using **explicit** Runge–Kutta formulas, not the implicit fourth-order Gauss endpoint operator here. Existing complete-multipartite positivity criteria cover the complete graph \(C_3\) and the complete bipartite graph \(C_4\), but cannot imply the nonmultipartite \(C_5\) case or the all-larger-cycle obstruction. Related studies of backward-Euler-filtered Crank–Nicolson and general Markov-generator Padé positivity concern distinct methods or quantifiers; neither accessible summary established this cycle-specific boundary. No universal priority or independence claim is made.

## Limitations
The finding is for **unweighted undirected cycles**, two-stage Gauss–Legendre **endpoint** updates, and all nonnegative timesteps; it does not establish stagewise positivity, robustness to arbitrary nonuniform edge weights, positivity on paths or other graph families, or a sharp *first* loss-of-positivity timestep for each \(n\ge6\). The common step \(h=8\) is a valid witness, not claimed minimal. The mathematical proof is self-contained, but priority relative to unindexed specialist articles remains uncertain.

## References
1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (March 26, 2013), https://arxiv.org/html/1303.6651v1 .
2. I. Fekete, D. I. Ketcheson and L. Lóczi, *Positivity for convective semi-discretizations*, arXiv:1610.00228v1 (October 2, 2016), https://arxiv.org/abs/1610.00228 .
3. J. F. B. M. Kraaijevanger, *Absolute monotonicity of polynomials occurring in the numerical solution of initial value problems*, Numerische Mathematik 48 (1986), 303–322 (historical background on absolute monotonicity).
