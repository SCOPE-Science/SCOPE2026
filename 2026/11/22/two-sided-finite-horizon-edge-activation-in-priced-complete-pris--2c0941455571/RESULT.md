# Two-sided finite-horizon edge activation in priced complete prisms

## Finding

Let \(m\ge2\), \(B>0\), \(r>0\), and \(t>0\). On the Cartesian prism \(G_m=K_m\square K_2\), each of the \(m(m-1)\) edges inside the two complete layers has unit price per conductance, and each of the \(m\) edges joining corresponding vertices has price \(r\). Assign individual nonnegative conductances \(w_e\), subject to \(\sum_{e\text{ inside layers}}w_e+r\sum_{e\text{ between layers}}w_e\le B\), and minimize the **full** combinatorial-Laplacian heat trace
\[
H_t(w)=\operatorname{tr}\bigl(e^{-tL(w)}\bigr).
\]
Disconnected allocations are permitted, and contribute all of their zero eigenvalues to this trace.

**Theorem (exact global support diagram).** There is exactly one minimizer over all independently chosen edge weights. It uses the full budget, assigns a common conductance \(a_t\) to all within-layer edges, and a common conductance \(b_t\) to all matching edges. It is classified as follows.

- If \(r>1\), set
  \[
  T_b=\frac{m-1}{B}\log\bigl(1+m(r-1)\bigr).
  \]
  For \(0<t\le T_b\), \((a_t,b_t)=(B/[m(m-1)],0)\), so the two complete layers are disconnected. For \(t>T_b\), both rates are strictly positive.
- If \(0<r<1\), set
  \[
  T_a=\frac{mr}{2B}\log\!\left(\frac{2-r}{r}\right).
  \]
  For \(0<t\le T_a\), \((a_t,b_t)=(0,B/(mr))\), so the graph consists of \(m\) separate matching pairs. For \(t>T_a\), both rates are strictly positive.
- If \(r=1\), both rates are strictly positive for every \(t>0\).

Whenever both rates are positive, they are determined **uniquely** by
\[
(m-1)a_t+rb_t=\frac Bm,
\qquad
\exp(mt a_t)=\frac{mr}{2}\bigl(1+\exp(2tb_t)\bigr)-(m-1).
\]
The optimal trace is
\[
H_t^*=\bigl(1+(m-1)e^{-mt a_t}\bigr)\bigl(1+e^{-2tb_t}\bigr).
\]

**Horizon and size laws.** For every fixed \(m,r,B\), the long-time optimum is connected and satisfies
\[
ma_t-2b_t=\frac1t\log\frac{mr}{2}+o(t^{-1}),
\qquad
\lim_{t\to\infty}\frac{b_t}{a_t}=\frac m2,
\]
with \(\lim_{t\to\infty}ma_t=\lim_{t\to\infty}2b_t=B/\bigl(m-1+mr/2\bigr)\). At equal prices, \(r=1\), the small-time allocation tends to the equal-edge design \(a_t,b_t\to B/m^2\).

For fixed \(B,r\), the size dependence of the exact deletion horizons differs sharply between the price sides:
\[
0<r<1:\quad \frac{BT_a}{m}=\frac r2\log\frac{2-r}{r},
\qquad
r>1:\quad\lim_{m\to\infty}\frac{BT_b}{m\log m}=1.
\]
Thus both the cheap interlayer edges and the expensive interlayer edges can force an **initially disconnected** optimal design, but the reactivation scales are respectively linear and logarithmically enhanced in the layer size.

## Assumptions and scope

Vertices are \((i,s)\) for \(1\le i\le m\), \(s\in\{0,1\}\). Edges join all distinct \((i,s),(j,s)\) in each layer, plus the matching \((i,0),(i,1)\). Every individual edge conductance is an independent real decision variable and may equal zero. The edge prices \(1,r\) and budget \(B\) are strictly positive and constant within each named orbit. The Laplacian is combinatorial (not degree-normalized); \(\operatorname{tr}\exp(-tL)\) includes the constant eigenmode and any additional zero modes from disconnected designs. The theorem applies to every finite \(m\ge2\) and finite \(t>0\); no connectedness constraint is silently imposed. In the network-size limits, price \(r\) and budget \(B\) are fixed.

## Proof

**1. Strict unrestricted convexity and symmetry.** Write \(L(w)=\sum_e w_e v_ev_e^{\mathsf T}\), with \(v_e\) the edge incidence vector. The map from the individual edge weights to \(L(w)\) is injective because each off-diagonal entry for an allowed edge equals minus its unique weight. For symmetric matrices \(A\), the trace exponential has second directional derivative
\[
D^2\operatorname{tr}(e^A)[X,X]
=\int_0^1\operatorname{tr}\!\left(e^{(1-s)A}Xe^{sA}X\right)\,ds>0
\]
for every nonzero symmetric \(X\): in an eigenbasis of \(A\), the integrand is a sum of positive coefficients times \(|X_{ij}|^2\). Consequently, \(H_t(w)\) is strictly convex in all individual edge weights for \(t>0\). The feasible price simplex is compact and nonempty, so the minimizer exists and is unique. Moreover, for any existing edge \(e\),
\[
\frac{\partial H_t}{\partial w_e}=-t\,v_e^{\mathsf T}e^{-tL(w)}v_e<0,
\]
so the price budget must be saturated. Simultaneous permutations of vertices within both layers and layer interchange preserve the objective and price classes. The unique minimizer is invariant under this group, which is transitive separately on the \(m(m-1)\) within-layer edges and on the \(m\) matching edges. Therefore the unique unrestricted optimum has weights \((a,b)\) constant on these two classes. This conclusion holds even on the boundary where the graph disconnects.

**2. Product spectrum and one-variable optimality.** The Laplacian is a tensor sum \(aL(K_m)\otimes I_2+bI_m\otimes L(K_2)\). Its spectrum is \(0\) once, \(2b\) once, \(ma\) repeated \(m-1\) times, and \(ma+2b\) repeated \(m-1\) times. Hence
\[
H_t(a,b)=(1+(m-1)e^{-mta})(1+e^{-2tb}),
\qquad (m-1)a+rb=B/m.
\]
Let \(x=mta\), \(y=2tb\). The logarithm of the objective equals
\[
\log(1+(m-1)e^{-x})+\log(1+e^{-y}),
\]
a strictly convex function along the budget line. Its interior first-order equation, after dividing the two partial derivatives by the corresponding budget costs, is
\[
\frac1{e^x+m-1}=\frac{2}{mr(e^y+1)},
\]
which is precisely the displayed exponential equation. Strict convexity makes any feasible interior solution the unique optimum.

**3. Both boundary activation laws.** At \(b=0\), \(a=B/[m(m-1)]\), differentiating the log-objective in the feasible direction of increasing \(b\) yields
\[
\left.\frac{d}{db}\log H_t\right|_{b=0+}
=t\left[\frac{mr}{e^{Bt/(m-1)}+m-1}-1\right].
\]
This derivative is nonnegative exactly when \(r>1\) and \(t\le T_b\). For \(r\le1\) and \(t>0\), it is strictly negative.

At \(a=0\), \(b=B/(mr)\), the corresponding feasible derivative with respect to increasing \(a\) is
\[
\left.\frac{d}{da}\log H_t\right|_{a=0+}
=(m-1)t\left[-1+\frac{2}{r(1+e^{2Bt/(mr)})}\right].
\]
It is nonnegative exactly when \(0<r<1\) and \(t\le T_a\); for \(r\ge1\) it is strictly negative. Convexity and the mutually exclusive price regimes then give the complete phase diagram, including equality at the transition times. For every finite \(r>0\) the appropriate boundary derivative becomes negative at large times, proving eventual connectivity.

**4. Long-time and large-network limits.** A feasible design with \(a,b>0\) has heat trace tending to one. By optimality, \(H_t^*\to1\) as \(t\to\infty\), since every Laplacian contributes at least its constant eigenvalue. Thus \(e^{-mta_t}\to0\) and \(e^{-2tb_t}\to0\). Dividing the exact interior equation by \(e^{2tb_t}\) yields
\[
e^{t(ma_t-2b_t)}=\frac{mr}{2}+\left(\frac{mr}{2}-m+1\right)e^{-2tb_t}\longrightarrow\frac{mr}{2}>0.
\]
Taking logarithms proves the displayed first correction. Inserting \(ma_t-2b_t\to0\) into the exact budget line gives the limiting rates. At \(r=1\), the interior equation divided by \(t\) and the exact budget give the small-time common rate, or equivalently the second-order heat-trace coefficient minimizes \((m-1)a^2+b^2\) under \((m-1)a+b=B/m\), uniquely at \(a=b=B/m^2\). The two network-size activation laws follow directly from the exact threshold formulas by logarithmic division.

## Verification

With Python, NumPy, and SciPy's dependencies installed for matrix operations (NumPy alone is used directly), run `python3 verify.py` from the directory containing this result. The supplied deterministic checker constructs complete \(2m\)-vertex Laplacians independently of the product-spectrum formulas, verifies eigenvalues and the heat trace, tests the exact allocation against all symmetric budget-grid competitors, and tests independent random asymmetric allocations and both threshold sides. Its actual output is `VERIFY_OK 15520`. These finite checks cover selected sizes, prices, budgets and times; they are not substitutes for the strict-convexity and exact spectral arguments establishing the full continuous and infinite-size claims.

## Relationship to prior work

Boyd's 2006 treatment gives the general convex spectral-weight optimization framework, with weighted Laplacians, symmetry reduction and a continuous-time Markov diffusion model, but does not give the present heat-trace support transitions on priced complete prisms. Ghosh, Boyd, and Saberi optimize **total effective resistance**, not the pointwise finite-time heat trace; their two-clique example is joined by a *single bridge* rather than a perfect matching. A later publicly available complete-prism resistance theorem does study this same two-layer/matching graph with the same two price classes. In that theorem every edge receives strictly positive conductance for each fixed positive price; its three allocation scales concern inverse eigenvalue sums and do not imply the present **two-sided finite-time deletion and activation** results. The distinction is substantive: unlike inverse-trace objectives, the finite-time exponential trace is finite at disconnected allocations. These background results and the standard product spectrum motivate this question, but none of the inspected stated results directly yields the exact two-sided horizon diagram and its unequal size scales.

## Limitations

The assertion applies to exactly two complete layers with a full corresponding-vertex matching, uniform price on each orbit and an unconstrained nonnegative conductance budget. It is not a classification for unequal layer sizes, partial matchings, vertex-dependent prices, degree-normalized diffusion or an objective integrated over time. The long-time expansion is for each fixed size and fixed price, not uniform in a simultaneous size/time limit. The matrix checker is finite, and originality relative to literature that is inaccessible or not indexed cannot be ruled out conclusively. The 2006 dated presentation serves as the first-public-date focal anchor; the earlier conference meeting dates for the related resistance paper do not establish a separately verified release day for its text. No independent mathematical audit is claimed.

## References

1. Stephen Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, ICM 2006 presentation, Madrid, August 29, 2006. https://web.stanford.edu/~boyd/papers/pdf/icm06_talk.pdf (weighted Laplacian, convex spectral functions, symmetry, and continuous-time Markov sections).
2. Arpita Ghosh, Stephen Boyd, Amin Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf (Sections I, II, V and VII).
3. *Three allocation scales in priced complete prisms*, publicly available research record, November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-allocation-scales-in-priced-complete-prisms--ab8d476367b2 (complete Finding, Proof and Relationship to Prior Work sections).
