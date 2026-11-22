# Universal positive spectral gaps from edge reweighting on locally finite graphs

## Finding

**Theorem.** Every countably infinite, connected, locally finite, simple undirected graph \(G=(V,E)\) admits finite positive edge conductances \(c_e\) satisfying
\[
\sum_{e=\{u,v\}\in E}c_e|f(u)-f(v)|^2\ge\sum_{v\in V}|f(v)|^2
\]
for every \(f\in\ell^2(V)\), where the left side is permitted to be infinite. Finite-support functions have finite energy. The associated selfadjoint weighted graph Laplacian therefore has spectral bottom at least one. The lower bound can be replaced by any prescribed positive number by multiplying all conductances by that number.

If in addition the vertex degrees are uniformly bounded, there exist conductances with **both** a positive lower and finite upper energy bound on \(\ell^2(V)\) if and only if the graph has strictly positive edge-isoperimetric constant. Thus amenable graphs admit the preceding lower spectral bound through unbounded conductances, but no conductance choice can simultaneously produce a bounded quadratic form and a positive lower spectral bound.

Equivalently, for an arbitrary orientation and \(b_e=\mathbf1_u-\mathbf1_v\in\ell^2(V)\), the complete family \((b_e)_{e\in E}\) is always positively reweightable into a lower semi-frame, whereas for bounded degree it is positively reweightable into a frame precisely in the nonamenable case.

## Assumptions and scope

All graphs are countably infinite, connected, locally finite, simple and undirected. Every conductance is a **finite**, strictly positive real, but their supremum need not be finite. The counting measure, not the weighted-degree measure, defines \(\ell^2(V)\). The energy is the full undirected-edge sum, with no factor of \(1/2\). The form domain is \(\mathcal D(\mathcal E_c)=\{f\in\ell^2(V):\mathcal E_c(f)<\infty\}\). The frame assertion requires a uniform maximum-degree bound \(d<\infty\). Nonamenability means that every nonempty finite vertex set has at least \(h|F|\) edges leaving it, for one fixed \(h>0\).

## Proof

**1. Rays with finite edge multiplicities.** Enumerate edges as \(E=\{e_1,e_2,\dots\}\) and vertices as \(V=\{v_1,v_2,\dots\}\). For \(n\ge0\) let \(F_n=\{e_1,\dots,e_n\}\), with \(F_0=\emptyset\). Removing finitely many edges from a connected graph produces at most finitely many components. The union \(B_n\) of the *finite* components of \(G\setminus F_n\) is therefore finite. Every vertex outside \(B_n\) lies in an infinite locally finite connected component and starts an infinite simple ray avoiding \(F_n\) (König's infinity lemma).

For each \(v_j\), let \(k(v_j)\) be the largest integer \(k\le j\) for which \(v_j\notin B_k\), using \(k=0\) if necessary. Choose a ray \(R_{v_j}\) from \(v_j\) in its infinite component of \(G\setminus F_{k(v_j)}\). Fix \(n\). Except for the finite set \(B_n\cup\{v_1,\ldots,v_{n-1}\}\), every vertex has \(k(v)\ge n\). Therefore only finitely many selected rays can use an edge \(e_n\). Define \(m_n=|\{v:e_n\in R_v\}|<\infty\).

**2. Positive conductances and the global-energy estimate.** Choose
\[
r_{e_n}=\frac{2^{-n}}{m_n+1},\qquad c_{e_n}=\frac1{r_{e_n}}=(m_n+1)2^n.
\]
Then every conductance is positive and finite, and
\[
\sum_{v\in V}\sum_{e\in R_v}r_e=\sum_{n\ge1}m_nr_{e_n}\le\sum_{n\ge1}2^{-n}=1.
\]
Let \(f\in\ell^2(V)\) have finite total energy \(\mathcal E_c(f)\). Along the successive distinct vertices of \(R_v\), \(f\) tends to zero, since every \(\ell^2\) function vanishes at infinity. Telescoping over finite prefixes, taking limits, and using weighted Cauchy–Schwarz gives
\[
|f(v)|^2\le\left(\sum_{e\in R_v}r_e\right)
\left(\sum_{e\in R_v}c_e|\nabla_e f|^2\right)
\le \left(\sum_{e\in R_v}r_e\right)\mathcal E_c(f).
\]
Summing over \(v\) and applying the preceding total-resistance bound yields \(\|f\|_2^2\le\mathcal E_c(f)\). When energy is infinite, the same inequality is automatic. Local finiteness gives finite energy to every finite-support function, so the form domain is dense. The energy is closed: the graph-gradient analysis operator from \(\ell^2(V)\) to \(\ell^2(E)\) is closed, because convergence in both spaces implies coordinatewise convergence at every edge. The representation theorem for closed nonnegative forms produces a selfadjoint operator \(L_c\ge I\). No boundedness or essential selfadjointness claim about a separately chosen minimal graph Laplacian is needed.

**3. Frame obstruction on amenable graphs.** Suppose the degrees are at most \(d<\infty\), and positive weights \(w_e\) yield a Bessel upper bound \(B\):
\[
\sum_e w_e^2|f(u)-f(v)|^2\le B\|f\|_2^2
\quad\text{for all }f.
\]
Applying this inequality to \(f=\mathbf1_v\) yields \(\sum_{e\ni v}w_e^2\le B\), so in particular \(w_e^2\le B\) for each edge. Applying the putative positive lower bound \(A\) to \(\mathbf1_F\), for finite nonempty \(F\subset V\), yields
\[
A|F|\le\sum_{e\in\partial F}w_e^2\le B|\partial F|.
\]
Thus \(h(G)\ge A/B>0\). In particular an amenable graph cannot be positively reweighted into a two-sided frame.

**4. Sufficiency on nonamenable bounded-degree graphs.** Suppose \(h(G)>0\) and maximum degree is \(d\). For every finite-support complex-valued \(f\), the discrete coarea identity applied to \(|f(v)|^2\) gives
\[
h\|f\|_2^2\le\sum_{\{u,v\}\in E}\big||f(u)|^2-|f(v)|^2\big|.
\]
By \(\big||a|^2-|b|^2\big|\le |a-b|(|a|+|b|)\), Cauchy–Schwarz and the degree bound, the last sum is at most
\[
\left(\sum_e|f(u)-f(v)|^2\right)^{1/2}
\left(\sum_e(|f(u)|+|f(v)|)^2\right)^{1/2}
\le\sqrt{2d}\,\|f\|_2\left(\sum_e|f(u)-f(v)|^2\right)^{1/2}.
\]
Therefore \(\sum_e|\nabla_e f|^2\ge h^2\|f\|_2^2/(2d)\). On the other hand, \(\sum_e|\nabla_e f|^2\le2d\|f\|_2^2\). Extend both inequalities from finite support to all \(\ell^2(V)\) by density and boundedness of the unweighted gradient. The unweighted edge-difference family itself is a frame with bounds \(h^2/(2d)\) and \(2d\). This proves both directions.

## Verification

The infinite-graph ray construction is exact, not an inference from finite simulations. The central bounds can be verified directly by tracing (i) the finite exceptional set after any finite edge deletion, (ii) the finite ray multiplicities, (iii) the summable incidence-weighted resistances, (iv) the global-energy form of Cauchy–Schwarz, and (v) the finite-set cut tests for the frame criterion. All constants follow with the stated normalization. The proof applies also to complex \(\ell^2\) functions. No computational experiment, formal proof assistant or independently checked certificate is claimed.

## Relationship to prior work

Balazs–Corso–Stoeva (2023), Section 3 and Conjecture 3.1, study positive rescaling of complete Hilbert sequences into lower semi-frames. The present result verifies this property for all locally finite graph incidence sequences using an edge-escape construction; it neither establishes nor claims the general conjecture. Their Sections 3–4 establish other sufficient hypotheses, not this graph-specific construction. The weighted graph Laplacian literature studies spectral gaps and unbounded conductances; the additional claim here is the **unrestricted existence** of a positive counting-measure gap on every infinite locally finite graph, coupled with a sharp two-sided frame obstruction for bounded-degree graphs. Standard coarea/Cheeger arguments supply the nonamenable half of the dichotomy; only the universal reweighting and its conjunction with the obstruction are being assessed as potentially new.

## Limitations

The weights depend on global choices of rays and need not be uniformly bounded or computationally efficient. No claim is made about unbounded-degree two-sided frame classification, essential selfadjointness of the minimal Laplacian, quantum-graph variants, or uniqueness/minimality of the weights. The lower bound allows infinite energy for some \(\ell^2\) vectors. Priority against some older spectral-graph literature, particularly general arbitrary-conductance formulations, may remain unresolved until an expert performs an independent literature audit.

## References

1. P. Balazs, R. Corso, D. Stoeva, *Weighted frames, weighted lower semi frames and unconditionally convergent multipliers*, arXiv:2310.18957v1 (first public 2023-10-29), Section 3, https://arxiv.org/html/2310.18957v1.
2. P. Exner, A. Kostenko, M. Malamud, H. Neidhardt, *Spectral Theory of Infinite Quantum Graphs*, arXiv:1705.01831 (first public 2017-05-04), https://arxiv.org/abs/1705.01831.
3. M. Keller, D. Mugnolo, *General Cheeger inequalities for p-Laplacians on graphs*, Nonlinear Analysis 147 (2016), DOI:10.1016/j.na.2016.07.011.
4. A. Kostenko and N. Nicolussi, *Laplacians on Infinite Graphs*, EMS Memoirs in Mathematics 3 (2023), DOI:10.4171/MEMS/3; relevant broad comparison subject to the literature limitation above.
