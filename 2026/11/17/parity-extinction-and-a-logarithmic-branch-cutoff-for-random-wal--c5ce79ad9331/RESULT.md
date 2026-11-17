# Parity extinction and a logarithmic branch cutoff for random-walk variation on double stars

## Finding

**Theorem.** Let \(T_k\), for every integer \(k\ge1\), be the tree with two adjacent hubs and exactly \(k\) pendant leaves attached to each hub. Let \(P_k\) be the **non-lazy simple-random-walk averaging operator** on real vertex functions,
\[
(P_k f)(v)=\frac1{\deg(v)}\sum_{u\sim v}f(u).
\]
Write \(J(f)=\sum_{uv\in E(T_k)}|f(u)-f(v)|\) for unweighted edge total variation and \(N_k(m)=\sup_{J(f)>0}J(P_k^m f)/J(f)\). For every nonnegative integer \(m\),
\[
\boxed{N_k(m)=\begin{cases}1,&m\text{ even},\\[3pt]1+\dfrac{2}{2k+1}\max\!\left\{0,\,2k\left(\dfrac{k}{k+1}\right)^m-1\right\},&m\text{ odd}.\end{cases}}
\]
All norms are attained by nonnegative binary cut signals: a bridge-cut signal attains the norm on strictly amplifying odd powers, and a leaf-cut signal attains it otherwise. Hence strict variation amplification occurs **exactly** at odd integers satisfying
\[
m<\tau_k:=\frac{\log(2k)}{\log(1+1/k)}=k\log(2k)+O(\log k),
\]
and never at even powers. If \(k\to\infty\) along odd integers \(m_k\) such that \((m_k-\tau_k)/k\to s\in\mathbb R\), then the transition profile is
\[
\lim_{k\to\infty} k\bigl(N_k(m_k)-1\bigr)=\max\{0,e^{-s}-1\}.
\]
The odd-power sharp norm becomes identically one after finitely many steps for each fixed \(k\), while every even-power sharp norm is already one.

## Assumptions and scope

The graph is a simple, undirected, unweighted balanced double star; vertex averages assign equal probability to every neighbor and **do not include holding probability**. Each hub has degree \(k+1\); each leaf has degree one. All powers act on real-valued functions, with the seminorm factored through functions modulo constants. Both signed inputs and nonnegative inputs are covered because the sharp witnesses are indicators of tree-edge cuts. The variable \(m\) is an integer \(m\ge0\), not continuous time. When \(k=1\), the tree is a four-vertex path and every sharp norm equals one.

## Proof

**1. Tree-cut operator-norm identity.** Root any finite tree, orient each edge from a parent to a child, and let \(A_e\) be its descendant component. Every vertex function can be written uniquely modulo constants as \(f=\sum_e a_e\mathbf1_{A_e}\), with \(a_e\) equal to the oriented difference across edge \(e\). Therefore \(J(f)=\sum_e|a_e|\). Every constant-preserving linear operator \(Q\) on vertex functions satisfies
\[
\sup_{J(f)>0}\frac{J(Qf)}{J(f)}=\max_{e\in E}J(Q\mathbf1_{A_e}).
\]
Indeed, the triangle inequality proves \(\le\), and a cut indicator attains the reverse bound. This lemma is exact for arbitrary real inputs; it is not an assertion derived from finite experimental enumeration.

**2. Reduction to two cut orbits.** Automorphisms of \(T_k\) identify all leaf edges; the bridge edge is the other orbit. Put \(q=k/(k+1)\) and \(d=2k+1\). For signals constant on each of the four symmetry classes (left leaves, left hub, right hub, right leaves), let \((X,Y,Z)\) be the oriented differences from left leaf to left hub, left hub to right hub, and right hub to right leaf, respectively. Direct evaluation of neighbor averaging gives
\[
\begin{pmatrix}X'\\Y'\\Z'\end{pmatrix}=\frac1{k+1}\begin{pmatrix}-k&1&0\\k&k-1&k\\0&1&-k\end{pmatrix}\begin{pmatrix}X\\Y\\Z\end{pmatrix}.
\]
The symmetric modes have eigenvalues \(q\) and \(-1\); the antisymmetric leaf mode has eigenvalue \(-q\). If the initial signal is one on the left half and zero on the right half, its difference triple begins at \((0,1,0)\). Solving the recurrence yields, at every integer \(m\ge0\),
\[
X_m=Z_m=\frac{q^m-(-1)^m}{d},\qquad Y_m=\frac{2kq^m+(-1)^m}{d}.
\]
Thus its edge variation is \(2k|X_m|+|Y_m|\). At even \(m\) this is exactly one. At odd \(m\) it is
\[
1+\frac2d\max\{0,2kq^m-1\}.
\]

**3. The leaf-cut orbit.** Begin with the indicator of one left leaf. At time zero its variation is one. After one averaging step, the values are zero at all leaves and the right hub, while the left hub has value \(1/(k+1)\); hence its four-class difference triple at time one is \((-1/(k+1),1/(k+1),0)\). The preceding recurrence then gives, for odd \(m\ge1\),
\[
X_m=-\frac{1+q^m}{d},\quad Y_m=\frac{1+q^m}{d},\quad Z_m=-\frac{1-q^{m-1}}{d},
\]
and for even \(m\ge2\),
\[
X_m=\frac{1+q^{m-1}}{d},\quad Y_m=-\frac{1-q^m}{d},\quad Z_m=\frac{1-q^m}{d}.
\]
The identity \((k+1)q^m=kq^{m-1}\) shows in both cases that \(k|X_m|+|Y_m|+k|Z_m|=1\). All leaf cuts have norm exactly one at every power. Comparing this value with the bridge orbit in Step 2 and invoking Step 1 proves the sharp formula, nonnegative attainment, and the parity classification.

**4. Sharp threshold and profile.** At an odd power strict amplification is equivalent to \(2kq^m>1\), equivalently \(m<\tau_k=\log(2k)/\log((k+1)/k)\). Taylor expansion of \(\log(1+1/k)\) gives the asserted large-\(k\) threshold. If \((m_k-\tau_k)/k\to s\), then \(2kq^{m_k}=q^{m_k-\tau_k}\to e^{-s}\); multiplying the norm formula by \(k\) and using \(2k/(2k+1)\to1\) gives the claimed limiting cutoff profile. No uniform real-time interpolation is asserted.

## Verification

The accompanying self-contained Python standard-library program `check.py` computes all cut-orbit norms with **exact fractions** on \(T_k\) for \(1\le k\le14\) and \(0\le m\le64\), verifying every relevant input cut and the exact formula (910 graph/power pairs). It additionally checks 12,320 signed-input power inequalities and 3,162 exact odd-threshold instances. Run `python check.py` in this package. The all-\(k\), all-\(m\) proof is the tree-cut identity and solved recurrence above; the finite diagnostics are corroborative rather than an infinite proof.

## Relationship to prior work

Ollivier's 2007 random-walk curvature work relates Markov averaging to **graph-Lipschitz** and Wasserstein contraction, including its Proposition 28 (the Lipschitz statement) and Proposition 29 (a spectral consequence); these are distinct from the edge-\(\ell^1\) variation norm evaluated here. Sandryhaila and Moura (2013) use a graph-shift total-variation functional of the form \(\|f-A_{\mathrm{norm}}f\|_1\), not the sum of absolute differences along every edge. Feneuil (2014) treats Littlewood–Paley functionals and Markov iterates on graphs, rather than the present exact finite-branch parity window. Related published finite-tree heat-flow results use **continuous-time** semigroups with different generators, or the graph-Lipschitz (edge-maximum) seminorm; those statements do not imply the discrete-time edge-total-variation norm of every power on balanced double stars. Full text from the most relevant available sources was compared, but the absence of an earlier unindexed equivalent calculation cannot be certified.

## Limitations

The result is specific to finite balanced double stars, equal neighbor probabilities and the non-lazy discrete-time simple random walk. The exact parity law relies essentially on bipartiteness, and the degree-dependent formula uses symmetry of the equal two branches. No claim is made for irregular trees, unequal double stars, lazy walks, weighted edges, or heat semigroups. The calculation is a self-reviewed mathematical claim, not an independently validated theorem.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, first arXiv submission 2007-01-30, arXiv:math/0701886; especially §2.5, Propositions 28–29. https://arxiv.org/abs/math/0701886
2. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, first arXiv submission 2013-07-01, arXiv:1307.0468. https://arxiv.org/abs/1307.0468
3. J. Feneuil, *Littlewood–Paley functionals on graphs*, first arXiv submission 2014-04-04, arXiv:1404.1353. https://arxiv.org/abs/1404.1353
