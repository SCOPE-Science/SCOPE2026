# Core boxes and a sharp Shapley-entry threshold in interpolated directed trust stars

## Finding

Fix an integer \(m\ge 2\), a directed in-star with leaves \(1,\ldots,m\) pointing toward its sole hub \(h\), and strictly positive edge weights \(0<w_1\le\cdots\le w_m\le1\). Define the internal value \(I(S)\) as the total weight of edges entirely in \(S\), and the external value \(E(S)\) as the sum, over members of \(S\), of their minimum incoming weight from outside \(S\), taking an empty minimum contribution to be zero. For every \(\alpha\in[0,1]\) let
\[
v_\alpha(S)=\alpha I(S)+(1-\alpha)E(S).
\]

**Core phase diagram.** The transferable-utility core is empty for \(\alpha<1/2\). For \(\alpha\ge1/2\) it is exactly
\[
C(v_\alpha)=\left\{x:\ 0\le x_i\le(2\alpha-1)w_i\ (1\le i\le m),\quad x_h=\alpha\sum_{i=1}^m w_i-\sum_{i=1}^m x_i\right\}.
\]
It is a singleton when \(\alpha=1/2\), and an \(m\)-dimensional rectangular parallelotope with exactly \(2^m\) vertices when \(\alpha>1/2\).

**Fairness–stability threshold.** Write \(w_0=0\), \(d_t=w_t-w_{t-1}\), and
\[
b_i=\sum_{t=i+1}^m\frac{d_t}{t}-\frac{w_m}{m+1},\qquad r_i=\frac{b_i}{w_i}.
\]
The Shapley value lies in this core if and only if
\[
\alpha\ge\alpha_*:=\frac{1+r_1}{3/2+r_1}.
\]
Moreover, \(r_1\ge r_2\ge\cdots\ge r_m\ge-1/(m+1)\), so
\[
\frac{2m}{3m+1}\le\alpha_*<1,
\]
with equality on the left exactly when all incoming weights are equal. For two leaves, the threshold simplifies to
\[
\alpha_* = \frac{w_2+3w_1}{w_2+6w_1}.
\]
Consequently weight asymmetry can push Shapley-core entry arbitrarily close to \(1\), while the core first becomes nonempty at the universal value \(1/2\). For every \(\alpha<1\) these games are non-supermodular; hence throughout \([\alpha_*,1)\) the Shapley value is coalitionally stable despite failure of supermodularity.

## Assumptions and scope

The graph has exactly \(m+1\) players, with no other arcs or self-loops. All edge weights are strictly positive and at most one; their order fixes labels but allows ties. Coalition worth uses the minimum-incoming-edge external term of the directed trust model, not an average, maximum, or outward-looking externality. The core consists of vectors \(x\in\mathbb R^{m+1}\) satisfying efficiency \(x(N)=v_\alpha(N)\) and every coalition inequality \(x(S)\ge v_\alpha(S)\). The Shapley value is the expectation of marginal contributions over uniformly random player permutations. The theorem covers all real \(\alpha\in[0,1]\) and all permitted real weights; no generic-position or distinctness assumption is needed.

## Proof

**1. Coalition formula and exact core.** A coalition without \(h\) has worth zero. A coalition containing \(h\) and exactly the leaves in \(K\subseteq\{1,\ldots,m\}\) has worth
\[
v_\alpha(\{h\}\cup K)=\alpha\sum_{i\in K}w_i+(1-\alpha)\begin{cases}\min_{j\notin K}w_j,&K\ne\{1,\ldots,m\},\\0,&K=\{1,\ldots,m\}.\end{cases}
\]
In particular \(v_\alpha(N)=\alpha W\) with \(W=\sum_iw_i\). Each leaf singleton forces \(x_i\ge0\), while the coalition omitting that leaf forces
\[
x_i\le v_\alpha(N)-v_\alpha(N\setminus\{i\})=(2\alpha-1)w_i.
\]
Since \(w_i>0\), these inequalities contradict each other when \(\alpha<1/2\).

For \(\alpha\ge1/2\), suppose all leaf coordinates satisfy the claimed intervals and define the hub coordinate by efficiency. Coalitions without the hub have nonnegative allocated sum and zero worth. For a hub-containing proper coalition omitting the nonempty set \(R\) of leaves, its allocated sum is at least
\[
\alpha W-(2\alpha-1)\sum_{j\in R}w_j
=\alpha\sum_{i\notin R}w_i+(1-\alpha)\sum_{j\in R}w_j
\ge\alpha\sum_{i\notin R}w_i+(1-\alpha)\min_{j\in R}w_j.
\]
This is precisely its coalition inequality. The grand coalition holds with equality. Thus the specified box is both necessary and sufficient. For positive weights it collapses to one point at \(\alpha=1/2\) and otherwise has dimension \(m\) and \(2^m\) distinct vertices.

**2. Shapley coefficients.** Let \(u_T(S)=1\) if \(T\subseteq S\), and zero otherwise. The external game admits the exact telescoping decomposition
\[
E=\sum_{t=1}^m d_t u_{\{h,1,\ldots,t-1\}}-w_m u_N.
\]
This identity holds whether the hub is absent, at least one leaf is absent, or no leaf is absent. The Shapley value of a unanimity game allocates \(1/|T|\) to each member of \(T\). Therefore leaf \(i\)'s external Shapley component is \(b_i\), while the internal edge-unanimity component is \(w_i/2\). Linearity gives
\[
\phi_i(v_\alpha)=w_i\left[\frac\alpha2+(1-\alpha)r_i\right],\qquad
\phi_h(v_\alpha)=\alpha W-\sum_{i=1}^m\phi_i(v_\alpha).
\]

**3. Ordering of the normalized external coefficients.** Summation by parts yields
\[
b_j=-\frac{w_j}{m+1}+\sum_{t=j+1}^m d_t\left(\frac1t-\frac1{m+1}\right)\ge-\frac{w_j}{m+1},
\]
and also
\[
b_{j+1}=-\frac{w_{j+1}}{j+2}+\sum_{t=j+2}^m\frac{w_t}{t(t+1)}\ge-\frac{w_{j+1}}{j+2}.
\]
For \(j<m\), because \(b_j-b_{j+1}=(w_{j+1}-w_j)/(j+1)\),
\[
r_j-r_{j+1}=\frac{w_{j+1}-w_j}{w_j}\left(\frac1{j+1}+r_{j+1}\right)\ge0.
\]
The parenthesis is strictly positive. Hence the normalized coefficients are decreasing, strictly across any strict increase in edge weight.

**4. Sharp Shapley-core entry.** If \(\alpha\ge1/2\), the lower box inequalities hold automatically since
\[
\frac{\phi_i(v_\alpha)}{w_i}\ge\frac\alpha2-\frac{1-\alpha}{m+1}\ge\frac14-\frac1{2(m+1)}\ge0.
\]
The upper box inequalities are equivalent to
\[
\frac\alpha2+(1-\alpha)r_i\le2\alpha-1
\quad\Longleftrightarrow\quad
\alpha\ge\frac{1+r_i}{3/2+r_i}.
\]
All denominators are positive. The right-hand side increases strictly with \(r_i\), so the first (lowest-weight) leaf is decisive. The minimum possible \(r_1=-1/(m+1)\) occurs exactly when all weights agree (because each positive weight gap enters the displayed nonnegative sum with a positive coefficient). Substituting gives \(2m/(3m+1)\). For \(m\ge2\) this exceeds \(1/2\); for finite positive weights the threshold is strictly below one. For \(m=2\), direct simplification yields the displayed ratio. With \(w_2\) fixed and \(w_1\downarrow0\), this ratio tends to one, proving the asymmetry assertion.

**5. Non-supermodularity.** Choose a leaf \(i\) of maximum weight and another leaf \(j\). Its marginal contribution upon joining \(\{h\}\) equals \(\alpha w_i\): the minimum external missing weight remains unchanged because at least one minimum-weight leaf other than \(i\) is still missing. Its marginal contribution upon joining \(N\setminus\{i\}\) equals \((2\alpha-1)w_i\). These two coalitions are nested, but for every \(\alpha<1\) the latter marginal is strictly smaller. Therefore the game violates the increasing-marginal characterization of supermodularity. This argument also covers tied largest weights.

## Verification

Run `python3 trust_star_check.py` using the enclosed standalone Python standard-library script. It enumerates coalition values directly; calculates Shapley values independently from all subset marginal contributions using exact rational arithmetic; tests every vertex of the asserted core box against all coalition inequalities; and checks the threshold and coefficient ordering. The recorded execution passed 157 rational test cases, 1,596 tested core vertices, and 101,360 coalition inequalities. This is a finite corroboration; the proof above establishes the claim for all admissible real weights and parameters.

## Relationship to prior work

Ryzák and Kroupa (2026) derive Shapley and Banzhaf values, a unique core and total balancedness for the **fixed unscaled sum** \(I+E\), and explicitly propose parameterized convex combinations as a future direction (Section 6). Bandhana, Kroupa and García (2024) introduce the underlying trust game and establish core existence at that fixed sum. The present result is for \(\alpha I+(1-\alpha)E\), including the range in which its core is empty, and proves a complete core-polytope and Shapley-entry classification for every positively weighted directed in-star. General Shapley linearity and classic core inequalities are used as tools; neither prior text inspected states this weighted-star threshold, its uniqueness/equality conditions, or the non-supermodular stable interval. Absence from searched sources does not establish global novelty; unpublished or unindexed equivalent results remain possible.

## Limitations

The core box and fairness threshold are specific to a directed in-star with all arcs entering one hub and strictly positive weights. The claim does not classify more general directed graphs, zero-weight degeneracies, other external aggregation operators, incentives for reporting weights, or an independent peer-review outcome. The computation checks rational finite instances only; completeness is analytic. For \(m=1\), the separate elementary boundary is \(\alpha_*=1/2\), outside the stated \(m\ge2\) theorem.

## References

1. D. Ryzák and T. Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, arXiv:2605.18157v1 (public 2026-05-18), Sections 2–6. https://arxiv.org/html/2605.18157v1
2. A. Bandhana, T. Kroupa and S. García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140, Sections 3–6. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf
