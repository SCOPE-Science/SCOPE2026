# Global parity selection and sharp extinction rates in hierarchical May–Leonard chains

## Finding
For every finite directed predation chain with common positive reproduction rate \(r\), common natural mortality \(d\) satisfying \(0<d<r\), and arbitrary strictly positive successive predation rates, every strictly positive biological initial condition converges exponentially to a nonzero equilibrium supported **exactly on the odd-indexed species**. Every even-indexed species has a sharp positive-prefactor extinction asymptotic, whose exponent equals its predation coefficient multiplied by its surviving predecessor's limiting density. Thus positive initial conditions select a single support pattern among the many independent-set equilibria; no interior orbit converges to a different support.

## Assumptions and scope
Fix an integer \(n\ge2\), \(r>d>0\), and \(p_i>0\) for \(1\le i<n\). Let \(x_i(t)\) be the density of species \(i\) in a non-cyclic directed predation path, and set \(S(t)=\sum_{i=1}^n x_i(t)\) and \(q=1-d/r\). The homogeneous well-mixed May–Leonard equations are
\[
\dot x_1=r x_1(q-S),\qquad
\dot x_i=x_i\bigl(r(q-S)-p_{i-1}x_{i-1}\bigr),\quad 2\le i\le n.
\]
We require \(x_i(0)>0\) for all \(i\) and \(S(0)\le1\), so the unoccupied fraction is nonnegative. No equal-predation assumption is made. The result is about this deterministic mean-field system, not individual-based stochastic population extinction or heterogeneous demographic rates.

Define \(w_1(t)=1\) and \(w_i(t)=x_i(t)/x_1(t)\) for \(i\ge2\). For every odd \(j\ge3\), the positive number
\[
L_j=\frac{x_j(0)}{x_1(0)}\exp\!\left(-p_{j-1}\int_0^\infty x_{j-1}(s)\,ds\right)
\]
exists, and put \(L_1=1\). Then
\[
x_j^*=\frac{qL_j}{\sum_{k\le n,\ k\text{ odd}}L_k}>0\quad(j\text{ odd}),
\qquad x_j^*=0\quad(j\text{ even}).
\]
There is \(\eta>0\), depending on parameters and the initial condition, such that \(x_i(t)=x_i^*+O(e^{-\eta t})\) for every \(i\). More sharply, for every even \(j\),
\[
\lim_{t\to\infty}e^{p_{j-1}x_{j-1}^*t}x_j(t)=A_j\in(0,\infty),
\]
with the exact finite positive prefactor
\[
A_j=x_1^*\frac{x_j(0)}{x_1(0)}
\exp\!\left(-p_{j-1}\int_0^\infty[x_{j-1}(s)-x_{j-1}^*]ds\right).
\]
The integrals are ordinary time integrals of the actual solution. The limits depend on initial conditions; the surviving support and the formula for each logarithmic extinction rate do not.

## Proof
**1. Positive invariant domain and a persistent leading species.** Every coordinate remains positive by its multiplicative ODE. At \(S=1\), the total-density derivative is negative, and \(S\) stays in \((0,1]\). Write
\[
T=\sum_{i=1}^{n-1}p_i x_i x_{i+1}\ge0,
\qquad \dot S=rS(q-S)-T.
\]
Let \(P=\max_i p_i\). Since the path is bipartite,
\[
T\le P\Big(\sum_{i\text{ odd}}x_i\Big)\Big(\sum_{i\text{ even}}x_i\Big)
\le\frac P4 S^2.
\]
Consequently, \(\dot S\ge S[rq-(r+P/4)S]\). Scalar comparison gives \(S(t)\ge s_0>0\) for all \(t\ge0\), with, for example, \(s_0=\min\{S(0),rq/(r+P/4)\}\).
The leading species' fraction \(u=x_1/S\) satisfies the exact identity \(\dot u=uT/S\ge0\). Thus \(x_1(t)\ge u(0)s_0>0\) for all time. In particular, \(\int_0^\infty x_1(t)dt=\infty\).

**2. Alternating survival by an exact projective identity.** Direct subtraction of logarithmic per-capita equations yields
\[
\frac{d}{dt}\log w_i=-p_{i-1}x_{i-1},\qquad
w_i(t)=w_i(0)\exp\!\left(-p_{i-1}\int_0^t x_{i-1}(s)ds\right).
\]
As \(x_1\) is bounded below, \(w_2\) decays exponentially; so does \(x_2=x_1w_2\). Then \(\int_0^\infty x_2<\infty\), making \(w_3\) converge exponentially to a strictly positive limit. Consequently \(x_3=w_3x_1\) is bounded below by a positive constant. The same argument applied to \(w_4\), then \(w_5\), and so on proves inductively that every even coordinate is exponentially small and every odd ratio \(w_j\) converges exponentially to \(L_j>0\). This induction works for each finite \(n\), including an even terminal species.

**3. Total-density convergence.** Every edge has an even endpoint; hence the already established exponential extinction implies \(T(t)=O(e^{-\gamma t})\) for some \(\gamma>0\). Writing \(z=S-q\) gives \(\dot z=-rSz-T\), and \(S\ge s_0\). Variation of constants therefore shows
\[
|S(t)-q|\le |S(0)-q|e^{-rs_0t}
+\int_0^t e^{-rs_0(t-s)}T(s)ds
=O(e^{-\eta t})
\]
for some \(\eta>0\) (a slightly smaller exponent absorbs a possible resonant factor \(t\)). Since \(S=x_1\sum_jw_j\), it follows that \(x_1\to q/(\sum_{j\text{ odd}}L_j)>0\) exponentially, and similarly \(x_j\to x_j^*\) for every odd \(j\). This also proves the displayed equilibrium formula.

**4. Sharp prefactors.** For an even \(j\), the preceding exponential convergence makes \(x_{j-1}(t)-x_{j-1}^*\) absolutely integrable. Separate the linear term \(x_{j-1}^*t\) from the projective integral in step 2 and use \(x_1(t)\to x_1^*>0\). The resulting exact formula has the positive finite limit \(A_j\), proving the stronger exponential equivalence and, in particular,
\[
\lim_{t\to\infty}\frac1t\log x_j(t)=-p_{j-1}x_{j-1}^*.
\]
All assumptions used in the argument are strict; neither uniform rates across species nor positivity of every initially present species can be silently dropped.

## Verification
The standalone `check.py` independently integrates the population equations and cumulative predecessor exposures with fourth-order Runge–Kutta time stepping. Executed with Python 3, it passed 540 finite-time exact-ratio/exposure consistency comparisons and 20 long-time parity-selection and exponential-rate assertions on chains of lengths two through six. These tests are finite numerical consistency checks, not the general proof; the proof is the preceding comparison and induction argument.

## Relationship to prior work
Samanta et al. (2026, arXiv:2609.09027v1) introduce the directed hierarchical May–Leonard dynamics, give their mean-field equations, establish independent-set restrictions on symmetric-demography coexistence equilibria, and report local stability and simulation outcomes. An independent-set equilibrium classification alone does not identify the limit of **every strictly positive trajectory**, rule out other asymptotic supports from the interior, or determine positive extinction prefactors and their exact exponents. The present theorem makes those additional dynamical claims for all finite path lengths and arbitrary positive predation strengths.

Classical May–Leonard cyclic competition (May and Leonard, 1975) and the three-species balance-simplex framework (Baigent and Ching, 2020) provide broader dynamical context, but their inspected descriptions do not state this directed-chain all-interior selection and rate law. No mathematical uniqueness claim is made from search non-detection alone.

## Limitations
The theorem is restricted to common \(r\) and \(d\), strictly positive initial densities, a finite directed path, strictly positive immediate-predecessor predation coefficients, and \(r>d>0\). Extinction in the deterministic system means a limit of zero; populations do not hit exactly zero in finite time. Limiting abundances and prefactors are expressed by convergent solution-dependent integrals rather than elementary closed forms. No claims are made for spatial interactions, stochastic extinctions, environmental perturbations, or arbitrary predation graphs. An independent scientific audit has not been performed.

## References
1. R. Samanta, S. Dawn, S. Jahiruddin, S. Bhattacharyya, C. Hens, and S. Nag Chowdhury, *Selection Rules for Species Coexistence in a Hierarchical May–Leonard Model*, arXiv:2609.09027v1, first public 2026-09-08. https://arxiv.org/html/2609.09027v1
2. R. M. May and W. J. Leonard, *Nonlinear Aspects of Competition Between Three Species*, SIAM Journal on Applied Mathematics 29 (1975), 243–253, DOI:10.1137/0129022. https://doi.org/10.1137/0129022
3. S. Baigent and A. Ching, *Balance simplices of 3-species May–Leonard systems*, Journal of Biological Dynamics 14 (2020), 187–199, DOI:10.1080/17513758.2020.1736656. https://discovery.ucl.ac.uk/id/eprint/10093501/
