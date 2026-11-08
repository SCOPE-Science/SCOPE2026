# A sharp active-site switch for Crank–Nicolson positivity on a mirrored weighted path

## Finding
Let \(t>0\). On the five-vertex path with consecutively ordered vertices \(1,2,3,4,5\), assign successive edge conductances \((1,t,t,1)\), and let \(L_t\) be its combinatorial weighted graph Laplacian. For every time step \(h\geq0\), the Crank–Nicolson end-step matrix is
\[
C_t(h)=\bigl(I+\tfrac h2L_t\bigr)^{-1}\bigl(I-\tfrac h2L_t\bigr).
\]
Write \(H(t)=\sup\{h\geq0:C_t(h)\text{ is entrywise nonnegative}\}\). Set
\[
H_c(t)=\frac{2-t+\sqrt{t^2+8t+4}}{3t}
\]
and let \(H_f(t)\) be the unique positive root, as a function of \(h\), of
\[
\begin{aligned}
F(h,t)={}&3h^4t^2+8h^3t^2+4h^3t+4h^2t^2\\
&-8h^2t-16ht-16h-16=0.
\end{aligned}
\]
Then the exact step-size threshold is
\[
\boxed{H(t)=\begin{cases}H_f(t),&0<t<3/4,\\2,&t=3/4,\\H_c(t),&t>3/4.\end{cases}}
\]
Moreover \(C_t(h)\) is entrywise nonnegative **if and only if** \(0\leq h\leq H(t)\). For \(t<3/4\), the first negative entries beyond the threshold are the two shoulder diagonal entries \((2,2)\) and \((4,4)\). For \(t>3/4\), the first negative entry is the central diagonal \((3,3)\). At \(t=3/4\), all three become zero simultaneously when \(h=2\). No off-diagonal entry is negative at any positive step.

The singular weak-coupling limit is
\[
\boxed{H(t)=\frac{2}{\sqrt t}-\sqrt t+O(t)\quad (t\downarrow0).}
\]
Thus each positive interior conductance ratio has a finite admissible step, although at \(t=0\) the disconnected chain has an entrywise nonnegative Crank–Nicolson step for every \(h\geq0\). The switching phenomenon cannot occur on a shorter reflection-symmetric path with positive edge conductances: on three and four vertices the central site or sites always control positivity.

## Assumptions and scope
The graph is the unweighted-in-mass, five-state diffusion discretization \(u'=-L_tu\) with unit outer-edge conductances and identical inner-edge conductances \(t>0\). There is no Dirichlet killing; the row sums of \(L_t\) vanish. All assertions concern exact end-step matrix entrywise nonnegativity, equivalent to preservation of every nonnegative initial vector, not internal stage positivity or error magnitude. At \(t=0\) the graph splits into two two-vertex components and one isolated vertex; that singular case is described separately and is not part of the positive-ratio theorem.

A physical chain with outer conductance \(a>0\), inner conductance \(b>0\), and physical step \(\tau\) is covered by the substitutions \(t=b/a\) and \(h=a\tau\). The graph sizes and all parameter quantifiers are exact; the finding is not an asymptotic assertion except for the displayed weak-coupling expansion.

## Proof
**1. Reduce positivity to three resolvent return probabilities.** Put
\[
R_t(h)=\bigl(I+\tfrac h2 L_t\bigr)^{-1}.
\]
The matrix being inverted is an irreducible nonsingular \(M\)-matrix for \(h>0\); therefore every entry of \(R_t(h)\) is strictly positive. Since \(C_t(h)=2R_t(h)-I\), all off-diagonal entries of \(C_t(h)\) are positive and its diagonal entry at site \(i\) is nonnegative exactly when \((R_t(h))_{ii}\geq1/2\). Reflection about vertex \(3\) reduces the five diagonal entries to an outer, a shoulder, and a center type.

**2. Exact inverse by reflection sectors.** In the orthonormal even basis \((e_1+e_5)/\sqrt2,(e_2+e_4)/\sqrt2,e_3\) and odd basis \((e_1-e_5)/\sqrt2,(e_2-e_4)/\sqrt2\), respectively, the weighted Laplacian has blocks
\[
L_+=\begin{pmatrix}1&-1&0\\-1&1+t&-\sqrt2t\\0&-\sqrt2t&2t\end{pmatrix},\qquad
L_-=\begin{pmatrix}1&-1\\-1&1+t\end{pmatrix}.
\]
Define the strictly positive polynomials
\[
D_1=h^2t+2ht+4h+4,\qquad
D_2=5h^2t+6ht+4h+4.
\]
The determinants of \(I+hL_-/2\) and \(I+hL_+/2\) are \(D_1/4\) and \(D_2/4\). Their cofactors yield, for the center and either shoulder,
\[
r_c=(R_t(h))_{33}=\frac{D_1}{D_2},\qquad
r_f=(R_t(h))_{22}=(R_t(h))_{44}=(h+2)\left(\frac{1+ht}{D_2}+\frac1{D_1}\right).
\]
For an endpoint \(r_e=(R_t(h))_{11}=(R_t(h))_{55}\), the same cofactor calculation gives
\[
r_e-r_f=\frac{2ht(3h^2t+4ht+4h+4)}{D_1D_2}>0
\quad(h,t>0).
\]
Thus endpoints can never trigger the first loss of positivity. Direct simplification gives
\[
r_f-r_c=\frac{2h\{t(h+2)^2-4(h+1)\}}{D_1D_2},
\]
\[
2r_c-1=-\frac{3h^2t+2ht-4h-4}{D_2},
\qquad 2r_f-1=-\frac{F(h,t)}{D_1D_2}.
\]
Each identity can also be replayed symbolically using the included checker.

**3. Each diagonal return probability crosses once.** The Laplacian is symmetric positive semidefinite, has a one-dimensional zero eigenspace spanned by the constant vector, and has four positive eigenvalues. Its orthonormal eigenbasis gives, for every vertex \(i\),
\[
(R_t(h))_{ii}=\frac15+\sum_{k=1}^4\frac{v_{k,i}^2}{1+h\lambda_k/2}.
\]
Because \(\sum_{k=1}^4v_{k,i}^2=4/5\), every diagonal return probability is strictly decreasing from \(1\) to \(1/5\). Hence \(r_f\) and \(r_c\) each cross \(1/2\) exactly once, giving unique positive roots \(H_f(t)\) and \(H_c(t)\). Solving the quadratic center equation gives the displayed radical \(H_c(t)\); the shoulder equation is exactly \(F(h,t)=0\).

**4. Determine the unique switching ratio.** At the center crossing \(h=H_c(t)\), the center equation is equivalent to
\[
t=\frac{4(h+1)}{h(3h+2)}.
\]
The right side decreases strictly from infinity to zero as \(h\) increases. Substituting this into the numerator of \(r_f-r_c\) gives
\[
t(h+2)^2-4(h+1)=\frac{-8(h+1)^2(h-2)}{h(3h+2)}.
\]
Therefore if \(H_c(t)>2\), the shoulder return is smaller than \(1/2\) at the center crossing, so the shoulder crossed earlier. If \(H_c(t)<2\), the shoulder return is larger than \(1/2\) at the center crossing, so the center crossed earlier. The equality \(H_c(t)=2\) holds exactly at \(t=3/4\), where direct substitution also gives \(F(2,3/4)=0\). This proves the piecewise formula, including all boundary equalities. The strict decrease in step size proves that no later positivity window occurs.

**5. Weak-coupling singularity.** For \(t<3/4\), let \(\varepsilon=\sqrt t\), \(z=\varepsilon H_f(t)\). Multiplying the shoulder equation by \(\varepsilon\) yields
\[
\begin{aligned}
0={}&4z^3-16z+\varepsilon(3z^4-8z^2-16)\\
&+\varepsilon^2(8z^3-16z)+4\varepsilon^3z^2.
\end{aligned}
\]
At \((z,\varepsilon)=(2,0)\), this polynomial vanishes and its \(z\)-derivative is \(32\). The implicit function theorem supplies a unique analytic positive root near \(2\). Its first derivative at zero vanishes and its second derivative is \(-2\), so \(z=2-\varepsilon^2+O(\varepsilon^3)\). The positive shoulder root must be this branch (by positivity and the single crossing), proving \(H_f(t)=2t^{-1/2}-t^{1/2}+O(t)\). At \(t=0\) the two isolated two-state components each have a balanced two-state Crank–Nicolson map, which is nonnegative for all steps; the singleton is unchanged.

**6. Minimality under reflection symmetry.** On the three-vertex mirror-symmetric path with conductances \((1,1)\), the endpoint return minus the center return is \(2h/((h+2)(3h+2))>0\). On the four-vertex mirror-symmetric path with conductances \((1,t,1)\), the endpoint return minus an interior return is \(ht/(h^2t+2ht+2h+2)>0\). Scaling the common outer conductance changes only the time unit. Thus no positive-weight reflection-symmetric path of at most four vertices has competing active center and shoulder diagonals, establishing the claimed minimal size.

## Verification
The standalone `verify.py` uses exact fractions and Gaussian elimination to reconstruct the full five-by-five resolvent for 1,782 positive rational parameter pairs; it checks all reflected diagonal identities, rational sign factorizations, stochastic row sums, off-diagonal positivity and the exact threshold criterion. Additional numerical root comparisons over thirteen positive conductance ratios and exact rational boundary checks give `VERIFY_OK 1797`. The separate `verify_symbolic.py`, requiring SymPy, checks the inverse/cofactor identities and the singular-limit polynomial identity, giving `SYMBOLIC_VERIFY_OK 12`. Both scripts are included in the package and were executed from their actual paths.

The symbolic calculations confirm algebra but do not substitute for the analytic all-parameter monotonicity, comparison, minimality and implicit-function arguments above. The two scripts check the exact specified matrix, not arbitrarily weighted longer paths.

## Relationship to prior work
Horváth's work on Runge–Kutta positivity provides general step-size and absolute-monotonicity theory for positive initial-value problems, rather than a conductance-dependent local controlling-site transition on one reflected weighted graph. Kovács, Li and Lubich (2015) prove uniform discrete maximal regularity for A-stable methods including Crank–Nicolson; maximal regularity is not end-step entrywise positivity. Their dated preprint motivates the distinction.

Higueras and Roldán (2023) give exact Crank–Nicolson positivity/contractivity thresholds for uniform **Dirichlet** one-dimensional heat discretizations with a different tridiagonal operator. Their all-mesh results, including their use of hyperbolic or Chebyshev functions, are not claimed here. Faragó, Korotov and Szabó (2010) similarly analyze finite-difference positivity under uniform Dirichlet discretization and related finite-element schemes.

The published mathematical note *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026) establishes the general identity \(C=2R-I\) and the abstract, generator-specific diagonal threshold principle; these facts are explicitly taken as prior work. Its theorem supplies a spectral/implicit threshold for any fixed reversible chain, but does not evaluate the two-parameter complete mirrored five-site family, identify the exact switch at \(t=3/4\), prove minimality of the active-site switch, or derive the \(t^{-1/2}\) weak-coupling law. Those jointly constitute the claim here, rather than the Cayley or general diagonal criterion itself.

## Limitations
This is a complete classification only for the stated reflection-symmetric five-site weighted path, not for arbitrary chains, irregular masses, nonsymmetric generators or stage positivity. The normalization of outer conductance is essential to interpreting the dimensionless time \(h\). At \(t=0\), the chain is disconnected, and it is not legitimate to infer its behavior by substituting into formulas whose derivation assumed \(t>0\). The spectral proof is exact; finite verification does not certify every positive real parameter by exhaustive enumeration.

A specific older result written as nonuniform-mesh diffusion, a tridiagonal Stieltjes resolvent inequality, or a Cayley-transform positivity theorem could conceivably imply the same active-site transition without naming the mirrored five-vertex path. The comparison with accessible sources does not prove universal publication priority. In particular, an older uniform Dirichlet positivity theorem and the general reversible-chain return-resolvent theorem should not be misrepresented as absent or novel.

## References
1. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI: 10.1016/S0168-9274(98)00050-6.
2. I. Faragó, S. Korotov, and T. Szabó, *Non-negativity preservation of the discrete nonstationary heat equation in 1D and 2D*, Aplimat—Journal of Applied Mathematics 3(2) (2010), 61–83.
3. B. Kovács, B. Li, and C. Lubich, *A-stable time discretizations preserve maximal parabolic regularity*, arXiv:1511.07823, first posted 24 November 2015, https://arxiv.org/abs/1511.07823.
4. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066, https://arxiv.org/abs/2301.01066.
5. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, public mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
