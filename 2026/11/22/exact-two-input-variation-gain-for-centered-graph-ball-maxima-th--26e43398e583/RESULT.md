# Exact two-input variation gain for centered graph-ball maxima through the six-cycle

## Finding
For each simple unweighted cycle \(C_n\), \(n\in\{3,4,5,6\}\), identify its vertices with \(\mathbb Z/n\mathbb Z\). For a nonnegative real vector \(f\), define its **centered graph-ball maximal average** by
\[
(M_nf)_i=\max_{0\le r\le\lfloor n/2\rfloor}\frac1{|B(i,r)|}\sum_{j\in B(i,r)}f_j,
\qquad B(i,r)=\{j:\operatorname{dist}_{C_n}(i,j)\le r\}.
\]
For any real vector \(h\), define cyclic edge variation \(V_n(h)=\sum_{i=0}^{n-1}|h_{i+1}-h_i|\), with subscripts modulo \(n\). The **exact attained two-input seminorm Lipschitz constants** are
\[
\boxed{\sup_{\substack{f,g\in[0,\infty)^n\\V_n(f-g)>0}}
\frac{V_n(M_nf-M_ng)}{V_n(f-g)}=
\begin{cases}
1,&n=3,\\[2pt]
\frac54,&n=4,\\[2pt]
\frac75,&n=5,\\[2pt]
\frac{19}{10},&n=6.
\end{cases}}
\]
At \(n=6\), the unconstrained radius-choice envelope is \(2\), but all three masks exceeding \(19/10\) are impossible as strict maximizing branches: they demand opposite vertices select full-cycle averages and the other four select singleton averages. This feasibility obstruction makes \(19/10\) sharp, not merely a numerical lower bound.

## Assumptions and scope
The graph is a simple cycle with three through six vertices, unit edge lengths, uniform counting measure and **centered** closed balls only; balls with a different center but containing the evaluation vertex are not allowed. The inputs \(f,g\) are coordinatewise nonnegative. Their difference can have either sign, and the output difference need not be nonnegative. The nonlinear map is a maximum of linear *averages*, not the absolute-value maximal operator evaluated on arbitrary signed inputs. The input and output variation are measured around the entire cycle. If \(V_n(f-g)=0\), translation equivariance gives \(V_n(M_nf-M_ng)=0\).

The result is classified primarily under MSC2020 `47H09`, concerning sharp Lipschitz behavior of a nonlinear operator in a variation seminorm; the closely related harmonic-analytic subject `42B25` is secondary.

## Proof
**1. Piecewise-linear reduction.** At every vertex \(i\) there are exactly \(R=\lfloor n/2\rfloor+1\) different centered balls, with averaging row vectors \(a_{i,r}\). For a radius mask \(m=(m_0,\ldots,m_{n-1})\in\{0,\ldots,R-1\}^n\), define the row-stochastic matrix \(A_m\) by placing \(a_{i,m_i}\) in its \(i\)-th row. Call a mask *strictly feasible* if some real vector \(x\) satisfies \(a_{i,m_i}x>a_{i,r}x\) for every \(i\) and \(r\ne m_i\). Adding a common sufficiently large constant makes any such \(x\) nonnegative without changing the selected rows.

The coordinatewise maximum of finitely many linear forms is continuous and piecewise linear. On the complement of finitely many equal-average hyperplanes, every point lies in a strict branch region. Along a generic line segment joining two nonnegative vectors, the derivative is \(A_m(g-f)\) for a strictly feasible mask at all but finitely many switching parameters. Since \(V_n\) is convex and homogeneous, a uniform bound \(V_n(A_mh)\le L V_n(h)\) on the strictly feasible masks implies \(V_n(M_ng-M_nf)\le L V_n(g-f)\). Continuity extends this conclusion to arbitrary segments and boundary points. Conversely, at a strict feasible baseline \(x\), a sufficiently small perturbation \(\varepsilon h\) satisfies \(M_n(x+\varepsilon h)-M_nx=\varepsilon A_mh\) when both vectors are nonnegative. Hence the nonlinear Lipschitz modulus equals the supremum of the corresponding strict-branch operator seminorms.

**2. Exact reduction to indicator cuts.** Every \(A_m\) preserves constants. For arbitrary real \(h\), subtract its minimum and use the finite coarea identity
\[
h-\min_jh_j=\int_{\min h}^{\max h}\mathbf1_{\{h>t\}}\,dt,
\qquad V_n(h)=\int_{\min h}^{\max h}V_n(\mathbf1_{\{h>t\}})\,dt.
\]
Linearity, the triangle inequality and preservation of constants give
\[
\sup_{V_n(h)>0}\frac{V_n(A_mh)}{V_n(h)}
=\max_{\varnothing\ne E\subsetneq\mathbb Z/n\mathbb Z}
\frac{V_n(A_m\mathbf1_E)}{V_n(\mathbf1_E)}.
\]
The reverse inequality is attained by the indicated binary vector. There are exactly \(2^n-2\) nonempty proper labeled cuts; no assumption that a cut is connected is needed.

**3. Exhaustive rational finite lemma.** For \(n=3,4,5,6\), evaluate the last expression for **all** \(R^n\) radius masks and **all** \(2^n-2\) cuts. All ball sizes divide \(s_n=\operatorname{lcm}_{i,r}|B(i,r)|\), so multiplying every averaging row by \(s_n\) reduces all cut ratios to exact integers divided by \(s_n V_n(\mathbf1_E)\). The standalone `verify_centered_cycle.py` reconstructs the balls independently and performs precisely this complete finite calculation with rational arithmetic, obtaining:

| Cycle | Radius masks | Nontrivial cuts per mask | Unrestricted envelope |
|---|---:|---:|---:|
| \(C_3\) | 8 | 6 | \(1\) |
| \(C_4\) | 81 | 14 | \(5/4\) |
| \(C_5\) | 243 | 30 | \(7/5\) |
| \(C_6\) | 4096 | 62 | \(2\) |

For \(C_6\), the only masks with a cut ratio **strictly larger than** \(19/10\) are exactly
\[
(3,0,0,3,0,0),\quad(0,3,0,0,3,0),\quad(0,0,3,0,0,3),
\]
and each has envelope \(2\). To rule them out as strict branches, rotate any such mask so its full-cycle selectors lie at vertices \(0\) and \(3\). Put \(a=x_5+x_0+x_1\), \(b=x_2+x_3+x_4\). The full-cycle average is \((a+b)/6\), whereas the radius-one averages at the opposite vertices are \(a/3\) and \(b/3\). Strict optimality of the full-cycle branch at both locations requires simultaneously \(b>a\) and \(a>b\), a contradiction. Thus **every** strict feasible \(C_6\) branch has variation norm at most \(19/10\); for smaller cycles the unrestricted envelopes already give the asserted upper bounds.

**4. Exact sharpness.** The table gives a nonnegative baseline \(x\), its unique strictly active radius mask \(m\), and a cut indicator \(h\). For all four rows, the direct branch inequalities hold at both \(x\) and \(y=x+\frac1{100}h\); their ratio is precisely the stated constant:

| Cycle | Baseline \(x\) | Radius mask \(m\) | Perturbation cut \(h\) | Ratio |
|---|---|---|---|---|
| \(C_3\) | \((0,3,3)\) | \((1,0,0)\) | \((1,1,0)\) | \(1\) |
| \(C_4\) | \((0,10,13,13)\) | \((2,0,0,0)\) | \((0,0,1,0)\) | \(5/4\) |
| \(C_5\) | \((11,11,0,14,14)\) | \((1,0,2,0,0)\) | \((0,1,1,1,0)\) | \(7/5\) |
| \(C_6\) | \((0,9,9,8,9,9)\) | \((3,0,0,2,0,0)\) | \((0,0,1,1,1,0)\) | \(19/10\) |

In the six-site case, for example,
\[
M_6y-M_6x=\frac1{100}(1/2,0,1,3/5,1,0),
\quad V_6(y-x)=\frac2{100},
\quad V_6(M_6y-M_6x)=\frac{19}{500}.
\]
Consequently the quotient is \(19/10\). This completes the proof, including both real-input quantifiers.

## Verification
In the directory containing the standalone program, run `python3 verify_centered_cycle.py`; no third-party modules are required. It reconstructs all centered ball rows and checks every one of the \(8\times6+81\times14+243\times30+4096\times62=262{,}424\) branch/cut pairs using integers and exact fractions, reports the three forbidden six-site masks, and verifies all four positive, strict-branch attaining pairs. The exhaustive finite step is backed by the coarea and branch-reduction proofs and the analytic opposing-average obstruction. No numerical sampling is used as a substitute for the finite universal check.

## Relationship to prior work
Bober, Carneiro, Hughes and Pierce (first public 2010) studied discrete maximal variation on the full integer line, proving one-input contraction for **uncentered** maximal functions and an \(\ell^1\)-to-variation estimate in the centered case. Soria and Tradacete (2014) studied centered finite-graph maximal operators in strong and weak \(\ell^p\) norms. González-Riquelme, Kovač and Madrid (2026) determined **one-input** variation gains for finite graphs with at most five vertices, not this two-input Lipschitz modulus.

A published six-cycle calculation for **uncentered** graph-ball maximal averaging has the same numerical two-input coefficient \(19/10\); however, the uncentered operator takes a maximum over all balls *containing* the evaluation vertex. A pointwise ordering between uncentered and centered maxima does **not** order their Lipschitz constants. Its result therefore does not establish the present centered theorem. Published centered six-cycle strong \(\ell^2\) calculations likewise optimize a different norm. For the centered case, the present exact mask exclusion shows a distinct and exceptionally short obstruction to the unattainable upper envelope \(2\).

## Limitations
The theorem is for nonnegative inputs and the precise centered unweighted graph-ball map on the four cycles \(C_3,C_4,C_5,C_6\). The same two-input seminorm bound need not hold for the usual absolute-value maximal operator acting on unrestricted signed inputs. No statement is made for larger cycles, independently weighted balls or other input/output seminorms. The finite certificate is exhaustive for the specified sizes only. Earlier unindexed equivalent results cannot be excluded; no independent historical-priority assessment has been performed.

## References
- J. Bober, E. Carneiro, K. Hughes and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1 (2010-05-17), https://arxiv.org/abs/1005.3030.
- J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (2014-10-22), https://arxiv.org/abs/1410.6204.
- C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (2026-03-12), https://arxiv.org/abs/2603.12462.
