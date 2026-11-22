# A sharp dimension-twelve feasibility boundary for positive Gauss–Padé diffusion on Boolean cubes

## Finding

**Theorem.** For every integer \(d\ge1\), let \(Q_d\) be the unweighted Boolean \(d\)-cube, \(L_d=dI-A_d\) its combinatorial Laplacian, and let the completed two-stage fourth-order Gauss–Legendre heat step at time \(h\ge0\) be
\[
T_d(h)=\left(I+\frac h2L_d+\frac{h^2}{12}L_d^2\right)^{-1}
\left(I-\frac h2L_d+\frac{h^2}{12}L_d^2\right).
\]
The following are equivalent:

1. There exists \(h>0\) such that every entry of \(T_d(h)\) is nonnegative.
2. There exists \(h>0\) such that every entry of \(T_d(h)\) is strictly positive.
3. \(1\le d\le12\).

For every \(1\le d\le12\), the **single rational step** \(h=1/3\) makes every entry strictly positive. For every \(d\ge13\) and every positive step, some entry is negative. In addition, all sufficiently small positive steps are positive entrywise precisely for dimensions \(1\le d\le6\). For all \(d\ge7\) and vertices at Hamming distance seven,
\[
(T_d(h))_{xy}=-\frac{35}{12}h^7+O_d(h^8)\quad(h\downarrow0).
\]
Thus the sharp small-step dimension boundary is six, whereas the sharp *existence of any positive step* boundary is twelve. This is a statement about the completed end-step, not internal stages.

## Assumptions and scope

Vertices of \(Q_d\) are binary words of length \(d\); edges connect words differing in exactly one coordinate, each at unit jump rate. Nonnegativity is entrywise, as required of a stochastic transition matrix, not merely positive semidefiniteness. The step is the exact rational matrix function in the theorem (no finite-precision claims). The positive denominators guarantee it is defined for all \(h\ge0\). Because \(L_d\mathbf1=0\), every row sum of \(T_d(h)\) equals one. All scalar eigenvalues lie in \((0,1]\) for finite \(h\ge0\). The positive-step threshold is not a statement about all \(h\), nor does it assert uniform positive entries across arbitrarily large dimensions.

## Proof

**1. Distance-class formula.** Define
\[
F(z)=\frac{1-z/2+z^2/12}{1+z/2+z^2/12},\qquad z\ge0.
\]
The Walsh eigenvalues of \(L_d\) are \(2k\), with multiplicities \(\binom dk\). If two vertices differ in precisely \(j\) coordinates, their common transition entry is
\[
U_{d,j}(h)=\frac1{2^d}\sum_{k=0}^d K_{d,j}(k)F(2kh),\qquad
K_{d,j}(k)=\sum_{a=0}^k(-1)^a\binom ja\binom{d-j}{k-a},
\]
where out-of-range binomial coefficients are zero. This formula follows by summing Walsh character products over all characters of weight \(k\). It accounts for every entry because the hypercube acts transitively on ordered pairs at each distance.

**2. Exact positivity witness in dimension twelve.** At \(h=1/3\),
\[
F(2k/3)=\frac{k^2-9k+27}{k^2+9k+27}.
\]
Set \(D_{12}=\prod_{k=1}^{12}(k^2+9k+27)=6557648589947835316380717\) and \(G=2786059680768\). The thirteen integers
\[
\left(2^{12}D_{12}U_{12,j}(1/3)/G\right)_{j=0}^{12}
\]
are, in increasing distance order,
\[
\begin{gathered}
953858494850392,\ 1563497388699,\ 43175953868634,\\
12536901704823,\ 3549152148984,\ 1078655625780,\\
353170735740,\ 122750459970,\ 44317433700,\\
16128405915,\ 5623467450,\ 1657493475,\ 193914600.
\end{gathered}
\]
All are positive. These integer identities follow by substitution in Step 1 and are independently reconstructed from rational arithmetic by `verify_cube_pade.py`. In particular, the smallest individual transition probability is \(48478650/2410225524765331>0\). This establishes strict positivity on \(Q_{12}\).

**3. An exhaustive, all-real-steps obstruction in dimension thirteen.** Introduce the strictly positive polynomial
\[
D_{13}(h)=\prod_{k=1}^{13}(3+3kh+k^2h^2).
\]
Using \(F(2kh)=(3-3kh+k^2h^2)/(3+3kh+k^2h^2)\), define for each distance \(j\) an integer polynomial
\[
N_j(h)=D_{13}(h)+\sum_{k=1}^{13}K_{13,j}(k)
 (3-3kh+k^2h^2)\frac{D_{13}(h)}{3+3kh+k^2h^2}.
\]
Every quotient in this expression is a polynomial. Thus \(U_{13,j}(h)=N_j(h)/(2^{13}D_{13}(h))\). For \(j=1,7,13\), exact polynomial division gives \(N_j(h)=h^jM_j(h)\) with \(M_j\in\mathbb Z[h]\). These explicit factored-sum definitions uniquely specify every coefficient of the certificate polynomials and make their signs reconstructible without approximate roots.

For a real polynomial \(M\), let \(V_M(a)\) be the number of sign changes in its Sturm sequence at \(a\), omitting zero evaluations, and let \(V_M(+\infty)\) use its leading-coefficient signs. Exact rational Sturm division gives:

| Distance \(j\) | Interval in \(h\) | Left Sturm variation | Right variation | Evaluated sign |
|---|---|---:|---:|---|
| 7 | \((0,1/32]\) | \(V_{M_7}(0)=7\) | \(V_{M_7}(1/32)=7\) | \(M_7(1/32)<0\) |
| 13 | \([1/32,1/3]\) | \(V_{M_{13}}(1/32)=1\) | \(V_{M_{13}}(1/3)=1\) | \(M_{13}(1/32)<0\) |
| 1 | \([1/3,\infty)\) | \(V_{M_1}(1/3)=11\) | \(V_{M_1}(+\infty)=11\) | \(M_1(1/3)<0\) |

Equal variations certify that the corresponding polynomial has **no roots in the interval**; the exact negative evaluation fixes its sign throughout, including both finite endpoints. The three closed-overlap intervals exhaust all \(h>0\). Since the denominators and powers \(h^j\) are positive, at least one of \(U_{13,7},U_{13,13},U_{13,1}\) is strictly negative for every \(h>0\). The companion checker regenerates these high-degree polynomials and Sturm sequences from the displayed formulas over the rationals and verifies the stated variations and signs; no step sampling or numerical root estimates are used in this argument.

**4. Extend both statements to every dimension.** Fix \(d\le D\). Regard functions on \(Q_d\) as functions on \(Q_D\) independent of the last \(D-d\) coordinates. The Laplacians commute with this inclusion: \(L_D(f\circ\pi)=(L_df)\circ\pi\). Rational functional calculus therefore yields
\[
\sum_{\pi(y)=z}T_D(h)_{xy}=T_d(h)_{\pi(x),z},
\]
where \(\pi\) forgets the last \(D-d\) coordinates. A positive \(T_{12}(1/3)\) gives a strictly positive \(T_d(1/3)\) for every \(d\le12\). Conversely if a higher-dimensional \(T_D(h)\) were entrywise nonnegative for \(D\ge13\), its marginal to dimension thirteen would be entrywise nonnegative, contradicting Step 3. This proves the main equivalence for every integer \(d\ge1\).

**5. The sharp local boundary.** The Taylor coefficients of \(F(z)\) through degree seven are those of \(e^{-z}\) through degree four, with fifth coefficient \(-1/144\), sixth coefficient zero and seventh coefficient \(+1/1728\). For two cube vertices at distance \(j\), \((L_d^k)_{xy}=0\) for \(k<j\) and \((L_d^j)_{xy}=(-1)^j j!\), so every distance \(1\le j\le5\) has a positive leading \(h^j\) entry. At distance six, the first nonzero term is degree seven; inserting one diagonal stay in a length-six shortest path gives \((L_d^7)_{xy}=7d\,6!>0\), hence a positive leading term \((35d/12)h^7\). At distance seven, the seventh Taylor coefficient times \((L_d^7)_{xy}=-7!\) is \(-35h^7/12\). Every diagonal is \(1+O(h)\). Thus all entries of each cube of dimension at most six are positive for sufficiently small positive \(h\), while cubes of dimension seven or higher have negative distance-seven entries at arbitrarily small positive \(h\). This completes the proof.

## Verification

Run `python3 verify_cube_pade.py` with Python 3 and SymPy installed. It reconstructs the exact rational \(Q_{12}\) transition shells, their common integer denominator certificate, the \(Q_{13}\) Sturm polynomials and rational sign/variation tests, the order-seven Taylor obstruction, and supplementary dimension checks. Its executed output was `VERIFY_OK exact_checks=116; Q12_positive_at_1/3; Q13_all_h_obstructed`. The finite rational checks provide inspectable certificates; the proof covers all real \(h>0\) by Sturm's theorem, and all dimensions by exact marginalization, not by sample enumeration. No external proof assistant or independent mathematical review is claimed.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2012) demonstrated positivity failures of Padé discretizations and the negative seventh series coefficient, including a nonconservative eight-state example. That is prior art for the method-wide small-step obstruction, not a dimension-twelve feasibility classification for undirected Boolean cubes. Lóczi and Ketcheson (2013) studied rational absolute-monotonicity radii; such method-wide bounds do not settle whether an individual finite graph admits **some** positive step.

The already published *Hypercube dimension barriers and a sharp three-cube threshold for Gauss–Legendre heat steps* proves eventual adjacent-entry negativity for even-stage Gauss methods on \(Q_d\), \(d\ge3\), and determines the full \(Q_3\) interval. The published *Sharp all-step Gauss positivity on Cartesian products of complete graphs* characterizes **all-step** rather than **existence-of-any-positive-step** positivity. These findings cover the context and some boundary cases, but do not imply the dimension twelve/thirteen existence cutoff: sufficiently large steps are negative for every \(d\ge3\), yet an intermediate strictly positive step still exists through \(d=12\). The present theorem separates these quantifiers and supplies a complete all-real-steps obstruction from three exactly certified Walsh shells. Published strongly-regular graph results concern another graph class; \(Q_d\) is not strongly regular for \(d\ge3\). Equivalent unindexed specialist work cannot be ruled out and would affect priority.

## Limitations

The theorem is confined to unit-weight Boolean hypercubes, the exact two-stage Gauss–Legendre completed step, and entrywise nonnegativity. It does not classify the full set of positive steps for dimensions four through twelve, internal-stage positivity, alternate integration orders, weighted hypercubes, or floating-point implementations. The Sturm certificate requires a symbolic rational polynomial library or independently implemented exact arithmetic. This is a self-review; no independent validation has occurred.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, preprint deposited 19 June 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ (full text inspected, especially the fourth-order Padé positivity counterexample).
2. L. Lóczi and D. I. Ketcheson, *Rational Functions with Maximal Radius of Absolute Monotonicity*, first posted 26 March 2013, https://arxiv.org/abs/1303.6651 .
3. *Hypercube dimension barriers and a sharp three-cube threshold for Gauss–Legendre heat steps*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-hypercube-dimension-barriers-and-a-sharp-three-cube-threshold-fo--d5410a2c25f5 .
4. *Sharp all-step Gauss positivity on Cartesian products of complete graphs*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-all-step-gauss-positivity-on-cartesian-products-of-complet--e93fc3196dc7 .
5. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
6. *Exact positivity intervals for fourth-order Padé diffusion on strongly regular graphs*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-positivity-intervals-for-fourth-order-pad-diffusion-on-str--4defdf9c32e5 .
