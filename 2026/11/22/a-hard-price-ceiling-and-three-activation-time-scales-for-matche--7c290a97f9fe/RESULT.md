# A hard price ceiling and three activation-time scales for matched bipartite diffusion

## Finding

**Theorem.** Let \(m\ge3\) be an integer, \(B>0\) a conductance-cost budget, \(r>0\) the relative price of a distinguished perfect matching in \(K_{m,m}\), and \(t>0\) an observation horizon. Every nonmatching edge costs one per unit conductance. Independently choose nonnegative rates on **all** \(m^2\) edges, subject to total expenditure at most \(B\), to minimize the full combinatorial-Laplacian heat trace \(H_t=\operatorname{tr}(e^{-tL})\), including the zero eigenvalues when the support is disconnected.

There exists **exactly one global optimizer**. It assigns a common rate \(p_t\) to each matching edge and a common rate \(q_t\) to each nonmatching edge, saturating
\[
mrp_t+m(m-1)q_t=B.
\]
Write
\[
r_c(m)=\frac{2(m-1)}{m-2},\qquad A_m(r)=2(m-1)-(m-2)r.
\]
Its complete edge-support classification is:

1. If \(0<r<1\), the nonmatching edges are deleted precisely for \(0<t\le T_a\), where
\[
T_a=\frac{mr}{2B}\log\frac{2-r}{r}.
\]
For \(t>T_a\) both edge classes are positive. Matching edges are positive at every horizon.
2. If \(r=1\), all \(m^2\) edges have rate \(B/m^2\) at every horizon.
3. If \(1<r<r_c(m)\), matching edges are deleted precisely for \(0<t\le T_b\), where
\[
T_b=\frac{m(m-1)}B x_m(r),
\]
and \(x_m(r)>0\) is the unique solution of
\[
mr e^{-2x}+2(r-1)e^{-mx}=A_m(r).
\tag{1}
\]
For \(t>T_b\), both classes are positive; the nonmatching edges are positive at every horizon.
4. If \(r\ge r_c(m)\), **the matching is deleted at every finite positive horizon**, and every other edge has rate \(B/[m(m-1)]\). Thus increasing the observation horizon never activates an edge above the sharp price ceiling.

In all regimes the two positive rates, when both exist, are characterized *without numerical matrix optimization* by the unique root in \(0<p<B/(mr)\) of
\[
mr e^{-mqt}-A_m(r)e^{-[2p+(m-2)q]t}
+2(r-1)e^{-2[p+(m-1)q]t}=0,
\qquad q=\frac{B/m-rp}{m-1}.
\tag{2}
\]
The endpoint formulas apply whenever the indicated boundary is optimal.

The activation delays have three distinct growing-network behaviors for fixed \(B\):
\[
\begin{aligned}
0<r<1:&\quad T_a=\frac{mr}{2B}\log\frac{2-r}{r}=\Theta(m),\\
1<r<2:&\quad \frac{BT_b}{m(m-1)}\longrightarrow\frac12\log\frac{r}{2-r},\\
r=2:&\quad \frac{BT_b}{m(m-1)\log m}\longrightarrow\frac12.
\end{aligned}
\tag{3}
\]
For every fixed \(r>2\), the matching is permanently deleted once \(m\) is large enough. At fixed \(m\), the activation time diverges logarithmically on approaching the ceiling from below:
\[
\frac{BT_b}{m(m-1)}
=\frac12\log\frac{mr}{(m-2)(r_c(m)-r)}+o(1)
\quad(r\uparrow r_c(m)).
\tag{4}
\]
The ceiling agrees with the *previously established* matching-price boundary for maximizing the asymptotic Laplacian spectral gap, but that equality does not supply the finite-time activation law, the one-sided support intervals, or the three horizon scales.

## Assumptions and scope

The vertex classes are \(U=\{u_1,\ldots,u_m\}\) and \(V=\{v_1,\ldots,v_m\}\), and matching edges are \(u_iv_i\). The weighted graph Laplacian is symmetric and combinatorial, \(L_{uv}=-w_{uv}\) on edges, with diagonal entries equal to weighted degrees. The feasible set explicitly includes **disconnected positive-rate supports**; the heat trace is always finite and counts one zero eigenvalue per connected component. This is an important distinction from steady-state effective-resistance objectives. There are no individual upper bounds on rates and no restrictions to orbit-constant allocations. The classification applies for all real \(r,B,t>0\) and all integers \(m\ge3\), including equality at each threshold. The asymptotics in (3) have fixed price and fixed budget; (4) has fixed graph size.

## Proof

**1. Existence, strict convexity, and unrestricted uniqueness.** The price-weighted nonnegative budget simplex is compact. For every real symmetric matrix \(X\), \(\Phi(X)=\operatorname{tr}(e^{-tX})\) is strictly convex: in an eigenbasis of \(X\), its second directional derivative at a nonzero symmetric direction \(Y\) is
\[
D^2\Phi(X)[Y,Y]=\sum_{i,j}
\frac{f'(\lambda_i)-f'(\lambda_j)}{\lambda_i-\lambda_j}|Y_{ij}|^2>0,
\quad f(s)=e^{-ts},
\]
where a repeated-eigenvalue quotient is interpreted as \(f''(\lambda_i)=t^2e^{-t\lambda_i}>0\). All divided differences are positive because \(f'\) is strictly increasing. The linear map from individual edge rates to the Laplacian is injective: an edge rate is the negative off-diagonal entry for its two endpoints. Hence \(H_t\) is strictly convex in the entire vector of independent rates, including at graph-disconnection boundaries. It has a unique minimum.

Any feasible allocation with slack budget and a nonzero rate can be scaled up to strictly decrease \(H_t\), as at least one positive Laplacian eigenvalue strictly increases under scaling. The all-zero allocation is not optimal: a positive rate on any edge decreases the trace below \(2m\). Therefore the budget is saturated. Simultaneous permutations of matched vertex pairs and exchange of the bipartition classes preserve costs and the objective, and form exactly two edge orbits. Uniqueness forces a common matching rate \(p\ge0\) and a common off-matching rate \(q\ge0\). This symmetry is **concluded**, not assumed.

**2. Complete spectral reduction.** The bipartite adjacency-rate block is \(W=(p-q)I_m+q\mathbf1\mathbf1^{\mathsf T}\), and every weighted degree equals \(d=p+(m-1)q\). Diagonalizing on the constant symmetric, constant antisymmetric, zero-sum symmetric, and zero-sum antisymmetric subspaces gives all eigenvalues, with multiplicity:
\[
0\ (1),\quad 2d\ (1),\quad mq\ (m-1),\quad
[2p+(m-2)q]\ (m-1).
\tag{5}
\]
These formulas remain valid at either boundary. Therefore
\[
H_t(p,q)=1+e^{-2dt}+(m-1)e^{-mqt}
+(m-1)e^{-[2p+(m-2)q]t},
\tag{6}
\]
with \(q=(B/m-rp)/(m-1)\) and \(0\le p\le B/(mr)\). Differentiation along this budget line yields
\[
\frac1t\frac{dH_t}{dp}=mr e^{-mqt}-A_m(r)e^{-[2p+(m-2)q]t}
+2(r-1)e^{-2dt}.
\tag{7}
\]
The derivative is strictly increasing along the budget line by step 1. Thus its signs at the two endpoints determine the unique optimizer; any interior stationary point is the unique global minimizer.

**3. Matching-only boundary.** At \(p=B/(mr)\), \(q=0\) and (7) simplifies *exactly* to
\[
\frac1{mt}\frac{dH_t}{dp}=r-(2-r)e^{-2Bt/(mr)}.
\tag{8}
\]
For \(0<r<1\) the right-hand side is negative at \(t=0\), strictly increasing in \(t\), and has the single positive zero \(T_a\) in the theorem; nonmatching rates therefore vanish up to and including \(T_a\), but not beyond. For \(r\ge1\) it is strictly positive at every \(t>0\), so this boundary cannot minimize the objective. Moreover when \(0<r<1\), (7) at \(p=0\) is negative for all \(t>0\): after division by \(e^{-(m-2)qt}\), the positive term \(mr e^{-2qt}\) is at most \(mr\), whereas \(A_m(r)>m\), and \(2(r-1)e^{-mqt}<0\). Therefore the matching rate never vanishes in this price regime.

**4. Nonmatching-only boundary.** At \(p=0\), put \(x=Bt/[m(m-1)]\). Dividing (7) by its positive factor \(e^{-(m-2)x}\) gives exactly
\[
F_m(x;r)=mr e^{-2x}+2(r-1)e^{-mx}-A_m(r).
\tag{9}
\]
For \(1<r<r_c(m)\), \(F_m(0;r)=2m(r-1)>0\), the derivative of \(F_m\) in \(x\) is strictly negative, and \(F_m(x;r)\to-A_m(r)<0\). Thus it has the one positive zero specified by (1), and the optimal matching rate switches from zero to positive precisely after \(T_b\). The other boundary is impossible by (8). For \(r\ge r_c(m)\), \(A_m(r)\le0\) and all three terms in (7) at \(p=0\) have the required nonnegative sign, strictly positive for \(t>0\); hence \(p=0\) always. At \(r=1\), full edge transitivity of the equal-price complete bipartite graph and strict convexity yield \(p=q=B/m^2\). These exhaust all prices, completing the finite-size classification and uniqueness.

**5. Distinct horizon scales and divergence.** In the middle regime \(1<r<2\), divide (1) by \(m\). For every fixed positive \(x\), its left minus right side converges to \(r e^{-2x}-(2-r)\), which has one strictly decreasing positive root \(x_0=\tfrac12\log[r/(2-r)]\). The exact finite-\(m\) functions are strictly decreasing and bracket this root at any fixed points on either side, proving \(x_m(r)\to x_0\). The formula for \(0<r<1\) is already exact. At \(r=2\), (1) becomes \(m e^{-2x}+e^{-mx}=1\). Its unique root satisfies \(x>\tfrac12\log m\), while at \(x=\tfrac12\log m+\varepsilon\) its left side tends to \(e^{-2\varepsilon}<1\) for every fixed \(\varepsilon>0\). Thus \(x_m(2)/(\log m)\to1/2\). As \(r_c(m)\downarrow2\), every fixed \(r>2\) eventually exceeds it. Finally fix \(m\). As \(r\uparrow r_c(m)\), the positive right side \(A_m(r)=(m-2)(r_c(m)-r)\downarrow0\), forcing \(x_m(r)\to\infty\). The ratio of the second left-hand exponential to the first is \(2(r-1)e^{-(m-2)x}/(mr)\to0\); consequently \(e^{-2x_m}=A_m(r)/(mr)(1+o(1))\), proving (4).

## Verification

The standalone `verify.py` uses exact rational matrix arithmetic to verify the four invariant spectral blocks in (5), constructs independent full Laplacians and compares numerical spectra to (5), checks all budget and support conditions across many sizes and prices, and compares optimal traces with independently sampled asymmetric allocations. It also samples the growth limits without claiming to prove them. Invoke `python3 verify.py` with Python 3, NumPy and SymPy. A passing run prints `VERIFY_OK 5289 ...`; the proof above, not finite sampling, supplies the universally quantified conclusion.

For a calibration example, at \(m=3\), \(B=1\), and \(r=3/2\), the unique matching activation time is approximately \(2.19351865374148\). At \(r=1/2\), ordinary edges begin receiving positive conductance only after \(3\log3/4\). At \(r=4\) the matching is never funded, at any positive observation horizon.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) introduce rate-budget optimization of the continuous-time Laplacian spectral gap, and Boyd, Diaconis, Parrilo and Xiao (2007) develop symmetry methods for *discrete-time* fastest mixing and give unmarked complete-bipartite examples. Those methods motivate the setting but optimize different functions. The exact priced-matching continuous-time gap theorem already gives the same permanent deletion frontier \(r_c(m)\), which is **not** claimed new here; it does not determine a full heat-trace optimum or the finite observation times at which supports change. Published matched-bipartite inverse-spectral-moment and resistance results also use the same graph but have no observation-time parameter and distinct support thresholds. Related finite-horizon edge-design calculations on other network families use different spectra; in particular, this family has a high-price regime where the matching remains inactive at *all* finite times. The multiplicity structure in (5) prevents transfer of an activation formula from a two-clique prism or a marked complete graph by a mere price relabeling.

## Limitations

This is a family-specific exact design theorem, not a general formula for arbitrary costs, unequal bipartitions, nonuniform stationary distributions, directed chains or discrete-time transition matrices. An optimum at short horizons can be disconnected because connectivity was not imposed. At \(r=r_c(m)\) there is a continuum of **spectral-gap** optima but a unique **finite-time heat-trace** optimum; these are distinct statements. The scalar interior root (2) is not asserted to have an elementary closed form. Convergence claims in (3) hold with price and budget fixed as stated, and no universal finite-time error bounds are asserted. Independent validation and complete global publication-priority certainty are not claimed.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI `10.1137/S0036144504443821`, first verified electronic publication 2006-11-02. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first submitted 2007-09-06, https://arxiv.org/abs/0709.0955; accessible HTML full text: https://ar5iv.labs.arxiv.org/html/0709.0955.
3. *Exact spectral-gap price transition and all optimal allocations for matching-priced complete bipartite networks*, public theorem: https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-spectral-gap-price-transition-and-all-optimal-allocations--efaad5dd81d4/RESULT.md.
4. *The matching-price deletion frontier for resistance-optimal balanced bicliques*, public theorem: https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-the-matching-price-deletion-frontier-for-resistance-optimal-bala--203ba798113c/RESULT.md.
5. *Three allocation scales in priced complete prisms*, public theorem for a distinct graph and effective-resistance objective: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-three-allocation-scales-in-priced-complete-prisms--ab8d476367b2/RESULT.md.
