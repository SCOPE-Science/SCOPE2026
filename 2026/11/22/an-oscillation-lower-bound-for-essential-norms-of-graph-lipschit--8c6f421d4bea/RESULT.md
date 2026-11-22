# An oscillation lower bound for essential norms of graph Lipschitz multipliers

## Finding
Let \(G=(V,E)\) be any infinite, connected, locally finite, simple graph, with a distinguished root \(a\). On either its complex big Lipschitz space \(\mathcal L(G)\) or its little Lipschitz space \(\mathcal L_0(G)\), equipped with the root-plus-edge-Lipschitz norm, let \(M_\psi f=\psi f\) be a bounded multiplication operator. Define the radial tail invariants
\[
A(\psi)=\lim_{N\to\infty}\sup_{d(a,v)\ge N}|\psi(v)|,
\qquad
B(\psi)=\lim_{N\to\infty}\sup_{\substack{v\sim w\\d(a,v),d(a,w)\ge N}}d(a,v)|\psi(v)-\psi(w)|.
\]
Then, on **each** of these two Banach spaces,
\[
\boxed{\|M_\psi\|_{\mathrm e}\ge\max\{A(\psi),B(\psi)\}.}
\tag{1}
\]
Together with the published universal upper bound \(\|M_\psi\|_{\mathrm e}\le4A(\psi)+B(\psi)\), this implies the exact identity
\[
\boxed{A(\psi)=0\quad\Longrightarrow\quad
\|M_\psi\|_{\mathrm e}=B(\psi).}
\tag{2}
\]
Both statements hold for graphs with cycles and without any restriction on vertex degrees beyond local finiteness. In (1), the coefficient one in front of \(B(\psi)\) is optimal; in (2), every nonzero value of \(B(\psi)\) is attained by an explicit bounded multiplier with \(A(\psi)=0\).

## Assumptions and scope
The graph metric \(d\) counts unweighted edges. Local finiteness and connectedness ensure every radius-bounded vertex ball is finite. Write
\[
L(f)=\sup_{v\sim w}|f(v)-f(w)|,\qquad
\|f\|=|f(a)|+L(f),
\]
\[
\mathcal L(G)=\{f:V\to\mathbb C:L(f)<\infty\},\qquad
\mathcal L_0(G)=\{f\in\mathcal L(G):\sup_{\substack{v\sim w\\d(a,v),d(a,w)\ge N}}|f(v)-f(w)|\to0\}.
\]
The essential norm is the infimum of \(\|M_\psi-K\|\) over *all* compact linear operators \(K\) on the respective Banach space. The source establishes that boundedness on either space is equivalent to boundedness on both; here boundedness is an assumption, not inferred merely from boundedness of the symbol. The quantities \(A,B\) exist and are finite under this assumption. The definition of \(B\) is orientation-independent in the limit, since adjacent radii differ by at most one and \(\sup_{v\sim w}d(a,v)|\psi(v)-\psi(w)|<\infty\).

## Proof
**1. Weak-null compactly supported test functions.** Choose any orientation of the edges and let \(Df(e)=f(v_e)-f(w_e)\). The difference embedding
\[
J:\mathcal L_0(G)\longrightarrow\mathbb C\oplus_1c_0(E),
\qquad Jf=(f(a),(Df(e))_{e\in E})
\]
is linear and isometric. In particular, if \(f_j\in\mathcal L_0(G)\) have bounded norm, \(f_j(a)\to0\), and \(Df_j(e)\to0\) for each fixed edge, then \(f_j\rightharpoonup0\) weakly in \(\mathcal L_0(G)\): each continuous functional on the isometric image extends by Hahn–Banach to \(\mathbb C\oplus_1c_0(E)\), whose dual is \(\mathbb C\oplus_\infty\ell_1(E)\), and dominated convergence for the resulting absolutely summable edge coefficients proves convergence. The continuous inclusion \(\mathcal L_0(G)\hookrightarrow\mathcal L(G)\) sends this sequence to a weakly null sequence in the big space as well. On either space, every compact linear operator sends a weakly null sequence to one converging to zero in norm.

**2. A weak-null family that reads an edge oscillation.** If \(B(\psi)=0\), its contribution to (1) is immediate. Otherwise choose adjacent vertices \(v_j,w_j\) with \(r_j=\min\{d(a,v_j),d(a,w_j)\}\to\infty\) and
\[
r_j|\psi(v_j)-\psi(w_j)|\longrightarrow B(\psi).
\tag{3}
\]
Such edges exist by the tail-supremum definition; replacing \(d(a,v_j)\) with \(r_j\) affects the product by at most \(|\psi(v_j)-\psi(w_j)|=O(1/r_j)\). Put
\[
q_j=\lceil\sqrt{r_j}\rceil,\qquad
h_j=r_j-q_j,\qquad
S_j=\{v_j,w_j\},\qquad
f_j(z)=\max\{0,h_j-d(z,S_j)\}.
\tag{4}
\]
Ignore finitely many indices to ensure \(h_j\ge1\). The distance to a set is one-Lipschitz, so \(L(f_j)\le1\). The function is supported in the finite \(h_j\)-neighborhood of \(S_j\), and therefore belongs to \(\mathcal L_0(G)\). Also \(d(a,S_j)=r_j>h_j\), hence \(f_j(a)=0\). Since the graph is infinite and connected, a geodesic from \(S_j\) to a vertex farther than \(h_j\) provides an edge across which \(f_j\) changes by one; therefore \(L(f_j)=1\) and \(\|f_j\|=1\).

At either endpoint of the selected edge, \(f_j\) equals \(h_j\). For each fixed vertex \(z\), the triangle inequality gives \(d(z,S_j)\ge r_j-d(a,z)\), whence
\[
f_j(z)\le\max\{0,d(a,z)-q_j\}=0
\]
for all sufficiently large \(j\). Thus \(Df_j(e)\to0\) for every fixed edge; step 1 shows \(f_j\rightharpoonup0\) in both spaces. For any compact \(K\), \(\|Kf_j\|\to0\), whereas at the chosen edge the two test values are equal, so
\[
\|M_\psi f_j\|\ge
|\psi(v_j)f_j(v_j)-\psi(w_j)f_j(w_j)|
=h_j|\psi(v_j)-\psi(w_j)|.
\]
Consequently
\[
\|M_\psi-K\|\ge\limsup_j(\|M_\psi f_j\|-\|Kf_j\|)
\ge\lim_j\frac{h_j}{r_j}\,r_j|\psi(v_j)-\psi(w_j)|=B(\psi),
\]
since \(h_j/r_j\to1\). Infimizing over compact \(K\) proves the new \(B\) lower bound.

**3. The amplitude bound.** If \(A(\psi)>0\), choose distinct vertices \(u_j\) whose radii diverge and whose symbol moduli tend to \(A(\psi)\). The singleton indicators \(g_j=\mathbf1_{\{u_j\}}\) have norm one for all large \(j\), lie in \(\mathcal L_0(G)\), and their edge gradients are eventually zero at each fixed edge. Thus step 1 makes them weakly null in both spaces. For every compact \(K\), the product \(M_\psi g_j\) has norm \(|\psi(u_j)|\), and \(\|Kg_j\|\to0\); this proves \(\|M_\psi\|_{\mathrm e}\ge A(\psi)\). Together with step 2 it proves (1).

**4. Exactness on vanishing symbols.** Proposition 8.3 of Issa-Barbará and Martínez-Avendaño (2026) supplies the upper estimate \(\|M_\psi\|_{\mathrm e}\le4A(\psi)+B(\psi)\) on each space. If \(A(\psi)=0\), the upper estimate and (1) coincide and prove (2). No inference is made about a general exact formula when \(A(\psi)>0\).

**5. A cyclic, non-tree sharpness example.** On the infinite ladder with vertices \((k,i)\) for integers \(k\ge0\), \(i\in\{0,1\}\), horizontal edges between successive levels and vertical edges within a level, root \((0,0)\), put
\[
\psi(k,i)=\frac{(-1)^k}{k+1}.
\]
This is a bounded multiplier: the symbol is bounded and its distance-weighted edge differences are uniformly bounded, by the boundedness criterion in the source. It satisfies \(A(\psi)=0\); on horizontal edges its weighted difference tends to \(2\), while vertical differences vanish. Hence \(B(\psi)=2\) and the *exact essential norm* is \(2\) on both big and little spaces. This cyclic example shows that the coefficient one in (1) cannot be increased, and that the non-tree scope is substantive rather than a formal reformulation of a rooted-tree formula. Multiplying this symbol by a positive scalar realizes any prescribed positive value of \(B(\psi)\) with equality in (1) and (2).

## Verification
The standalone `checker.py` constructs finite ladders with genuine four-cycles, computes graph distances by breadth-first search, builds the plateau-tent functions (4), and checks normalization, root vanishing, constancy on the selected edge, the product-jump identity, and vanishing on expanding root neighborhoods. Running `python3 checker.py` produced `GRAPH_LIPSCHITZ_MULTIPLIER_TENT_CHECKS_OK 103`, with edge witness values increasing toward \(2\) at sampled radii \(12,30,100,300\). Those finite tests corroborate the geometry but do not prove weak convergence, generality over infinite graphs, or the sharp limit; all three follow from the written analytic proof and the published upper bound.

## Relationship to prior work
Issa-Barbará and Martínez-Avendaño, arXiv:2602.13534v1 (2026), establish the general locally finite graph setting and the estimates \(A(\psi)\le\|M_\psi\|_{\mathrm e}\le4A(\psi)+B(\psi)\). Immediately after their Proposition 8.2, they explicitly leave finding a lower bound depending on \(B(\psi)\) for future research. Equation (1) supplies such a lower bound with sharp coefficient, simultaneously for both Banach spaces; equation (2) identifies a complete exact-norm subclass. The norm normalization and the two tail invariants agree with that source.

The earlier Colonna–Easley (2010) theory and accessible publicly recorded exact essential-norm formulas for little and big **rooted-tree** Lipschitz multiplier spaces (21 September and 17 November 2026) provide essential-norm estimates or exact row identities under unique-parent tree geometry. Those statements do not cover arbitrary locally finite graphs with cycles. In particular, a bounded graph Lipschitz function on a cyclic graph is not freely specified by independent root-to-vertex edge increments, so a tree \(\ell_\infty\)-coordinate theorem cannot be quoted as a proof of (1). The present direct distance-to-an-edge construction avoids this obstruction. The weak-null \(c_0\) argument is elementary functional analysis and is not by itself claimed as new; its use to obtain a sharp graph-wide lower bound is the mathematical result.

## Limitations
The graph must be simple, connected, infinite and locally finite, and the norm must be the root-plus-edge-Lipschitz norm specified above. Boundedness of the multiplier is required. Equation (2) is exact only when the symbol vanishes at infinity; there is no general exact formula asserted for positive \(A(\psi)\). Public literature comparison and inspected exact tree results support the claimed distinction from prior work but do not logically exclude an unindexed equivalent result. The unpublished Colonna–Locke manuscript and Locke's 2016 dissertation were not available as inspectable complete texts; they remain explicit bibliographic risks. Independent mathematical validation has not been performed.

## References
1. J. A. Issa-Barbará and R. A. Martínez-Avendaño, *Multiplication Operators on the Lipschitz Space of an Infinite Graph*, arXiv:2602.13534v1, first public 14 February 2026, https://arxiv.org/html/2602.13534v1; Sections 2–5 and 8.
2. F. Colonna and G. R. Easley, *Multiplication Operators on the Lipschitz Space of a Tree*, Integral Equations and Operator Theory 68 (2010), 391–411, DOI:10.1007/s00020-010-1824-5.
3. *Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees*, publicly accessible result (21 September 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-exact-essential-norm-little-tree-lipschitz-multipliers--6b05c4d0072a.
4. *Exact essential norms of multipliers on big weighted Lipschitz spaces of rooted trees*, publicly accessible result (17 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-essential-norms-of-multipliers-on-big-weighted-lipschitz-s--d1427342c9b4.
5. *Tail-escape essential norms and a sharp summability transition for weighted tree Lipschitz multipliers*, publicly accessible result (17 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-tail-escape-essential-norms-and-a-sharp-summability-transition-f--2e6f7e5ce734.
