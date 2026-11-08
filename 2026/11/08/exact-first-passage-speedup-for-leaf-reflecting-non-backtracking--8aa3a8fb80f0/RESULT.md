# Exact first-passage speedup for leaf-reflecting non-backtracking walks on trees

## Finding

**Theorem (exact tree speedup).** Let \(T\) be any finite simple undirected tree with at least two vertices, and let \(s\ne t\) be vertices. Root \(T\) at the target \(t\). For each vertex \(v\), let \(b_v\) be the number of vertices in the descendant subtree rooted at \(v\), including \(v\), and let \(d_v\) be its degree. Write the unique path from source to target as \(v_0=s,v_1,\ldots,v_\ell=t\).

An ordinary simple random walk (SRW) always chooses uniformly among the neighbors. A leaf-reflecting non-backtracking walk (NB) initially does the same; at later steps it chooses uniformly among neighbors other than the vertex visited immediately before, unless its degree is one, when it returns along its only edge. In both cases, stop upon the first visit to \(t\), and write the corresponding expected stopping times as \(H_{\mathrm{SRW}}(s,t)\) and \(H_{\mathrm{NB}}(s,t)\).

Then, **for every** such tree and ordered pair,

\[
\boxed{H_{\mathrm{SRW}}(s,t)-H_{\mathrm{NB}}(s,t)
=2\left(\frac{b_s-1}{d_s}+\sum_{i=1}^{\ell-1}
\frac{b_{v_i}-1+b_{v_{i-1}}}{d_{v_i}}\right).}
\]

The saving is nonnegative, and is exactly zero **if and only if** \(s\) is a leaf adjacent to \(t\). Otherwise it is strictly positive. In particular, this determines the exact quantitative advantage for every source, target, and finite tree, not only its sign.

## Assumptions and scope

- All edge weights are one; \(T\) is finite, connected and acyclic, with no loops or multiple edges.
- The vertex at time zero is \(s\), with no inherited previous position. Both walks use a uniform first step, including when \(s\) is a leaf.
- The non-backtracking rule *reflects* at a degree-one vertex; it does not kill, hold, or restart the walk there. No no-dangling-edge assumption is imposed.
- \(b_v\), \(d_v\) and the path indices are determined by the target-rooted tree, so every denominator in the formula is a positive integer. The intermediate-path sum is empty when \(s\) and \(t\) are adjacent.
- The statement concerns finite mean hitting times, not stochastic domination of entire hitting-time distributions or cover times.

## Proof

Write \(p(v)\) for the parent of each nonroot vertex, \(C(v)\) for its children, \(k_v=|C(v)|=d_v-1\), and \(S_v=\sum_{w\in C(v)}b_w=b_v-1\). The proof uses induction on descendant subtree size.

**Step 1: a non-backtracking branch excursion.** Fix \(v\ne t\). Starting with the oriented arrival \(p(v)\to v\), let \(F_v\) be the expected number of *subsequent* steps to first return to \(p(v)\). We claim

\[
F_v=2b_v-1=1+2S_v.
\]

At a leaf, reversal is forced and \(F_v=1\). Assume the claim for every child \(w\) of \(v\). If the walk departs \(v\to w\), the complete excursion until its next arrival at \(v\) takes expected time

\[
1+F_w=2b_w.
\]

The return to \(v\) has previous vertex \(w\). If \(k=k_v\ge1\), define \(U_w\) as the expected time to first reach \(p(v)\) from this oriented arrival \(w\to v\). Among the \(k\) legal next neighbors, exactly one is \(p(v)\), and the others are the children other than \(w\). Thus

\[
kU_w=1+\sum_{z\in C(v)\setminus\{w\}}(2b_z+U_z).
\]

Let \(Z=\sum_{z\in C(v)}(2b_z+U_z)\). Rearranging gives

\[
(k+1)U_w=1+Z-2b_w.
\]

Summing the equations over children and using \(S_v=\sum_w b_w\) yields \(Z=k(2S_v+1)\). Consequently

\[
\boxed{U_w=1+\frac{2(kS_v-b_w)}{k+1}},\qquad
F_v=\frac Zk=1+2S_v=2b_v-1.
\]

These expectations are finite: by induction every child excursion has finite mean, and from each incoming child direction there is probability \(1/k\) of exiting immediately towards \(p(v)\); hence the expected number of child excursions is finite. This closes the induction.

**Step 2: starting without memory.** From a fresh start at \(v\ne t\), with no preceding vertex, the next step is uniform among its \(k+1\) neighbors. A move directly to \(p(v)\) takes one step; a move to child \(w\) is followed by an expected excursion of \(2b_w\) and then by \(U_w\). Therefore the expected number of steps to first hit \(p(v)\) is

\[
B_v=\frac{1+Z}{k+1}=1+\frac{2kS_v}{k+1}.
\]

For a leaf, this is \(1\), so the formula includes \(k=0\).

**Step 3: ascent along the source-target path.** By the strong Markov property on oriented edges, once the walk first hits \(p(v)\) from \(v\), its preceding vertex is exactly \(v\). Accordingly the first passage to the target factors into successive rootward passages: an initial passage from \(s\), with mean \(B_s\), and for each \(i=1,\ldots,\ell-1\) a passage from \(v_i\) to its parent, arriving with previous vertex \(v_{i-1}\), with mean \(U_{v_{i-1}}\). Thus

\[
H_{\mathrm{NB}}(s,t)=\ell+\frac{2k_sS_s}{k_s+1}
+2\sum_{i=1}^{\ell-1}\frac{k_{v_i}S_{v_i}-b_{v_{i-1}}}{k_{v_i}+1}.
\]

**Step 4: ordinary walk and exact subtraction.** For simple random walk, let \(A_v\) be the expected time to first hit \(p(v)\) from \(v\). At a leaf \(A_v=1\). At an internal vertex, condition on the first step and use the child induction \(A_w=2b_w-1\):

\[
A_v=1+\frac{1}{k_v+1}\sum_{w\in C(v)}(A_w+A_v).
\]

Solving gives \(A_v=1+2S_v=2b_v-1\). The vertex Markov property therefore yields

\[
H_{\mathrm{SRW}}(s,t)=\sum_{i=0}^{\ell-1}(2b_{v_i}-1)
=\ell+2\sum_{i=0}^{\ell-1}S_{v_i}.
\]

Subtracting the expressions from Steps 3 and 4, with \(k_v+1=d_v\), gives the displayed exact speedup formula.

**Step 5: equality boundary.** Each displayed summand is nonnegative. The initial term vanishes exactly when \(b_s=1\), equivalently when \(s\) is a leaf of the target-rooted tree. Every intermediate-path term is strictly positive, because \(v_{i-1}\) is a descendant of \(v_i\) and \(b_{v_{i-1}}\ge1\). Therefore equality occurs precisely for a source leaf with \(\ell=1\), that is, \(s\) is a leaf adjacent to \(t\). Otherwise the saving is positive. \(\square\)

## Verification

The accompanying dependency-free `verify.py` independently constructs the absorbing transition linear systems for the original first-step simple random walk and for the lifted directed-edge non-backtracking chain. Gaussian elimination over exact `fractions.Fraction` values is used; these independent solutions are compared with the structural formula, including the equality criterion.

Running `python3 verify.py` produced `VERIFY_OK exact independent comparisons = 4202`. The checks include every source-target pair of every recursively labelled tree on two through six vertices, plus path, star, and branched-tree test families at orders seven, eight, and ten. A finite test cannot prove an all-tree result; the induction above is the proof. The checker has no external data or network dependencies.

Two straightforward consequences serve as additional boundary checks. On an endpoint-to-endpoint path of \(n\) vertices, the non-backtracking walk hits in exactly \(n-1\) steps whereas the ordinary walk has mean \((n-1)^2\). On a star with \(d\ge2\) leaves, starting at its center and targeting a leaf, the exact speedup is \(2(d-1)/d\).

## Relationship to prior work

The general **non-backtracking walk is no slower in mean than ordinary simple random walk** is not new: Altisen, Devismes, Gerbaud, and Lafourcade (2012), Corollary 9, prove a stronger comparison on *every* finite simple connected graph for their FIFO1 tabu walk, using precisely the same forced-return convention at degree-one vertices and empty initial memory. Consequently the nonnegativity portion here is contextual rather than the novel contribution. Their cited comparison does not give the exact tree-dependent saving, its subtree coefficients, or the stated equality classification; their tree-specializing Proposition 14 addresses lines and longer tabu lists.

Fasino, Tonetto, and Tudisco (arXiv:2105.14438, first posted 2021-05-30) develop general second-order hitting-time linear systems and identities; their standard pure non-backtracking model disallows dangling edges, and their theorems do not supply this all-tree leaf-reflection formula. Matsuo, Kawagishi, and Ohsaki (2022 advance publication) study random regular graphs and configuration models, not arbitrary target-rooted trees. The present statement therefore isolates a *quantitative structural refinement* rather than claiming the already-established direction of the inequality.

## Limitations

The formula requires a finite **tree**, uniform neighbor transitions, a uniformly chosen first neighbor, and deterministic reflection at leaves. It is not asserted for weighted trees, nonuniform initial-edge distributions, other memory rules, graphs with cycles, or distributional rather than mean comparisons. Searches of relevant literature and research records did not show the exact identity, but absence from those searches does not establish historical priority; in particular, unpublished elementary derivations or equivalent formulas may exist. No independent mathematical audit has been performed.

## References

1. D. Fasino, A. Tonetto, and F. Tudisco, *Hitting times for second-order random walks*, arXiv:2105.14438, first posted 2021-05-30, https://arxiv.org/abs/2105.14438 .
2. K. Altisen, S. Devismes, A. Gerbaud, and P. Lafourcade, *Comparisons of mean hitting times for tabu random walks on finite graphs*, technical report TR-2012-6, particularly Corollary 9 and Proposition 14, https://www-verimag.imag.fr/TR/TR-2012-6.pdf .
3. R. Matsuo, T. Kawagishi, and H. Ohsaki, *On the mean first passage time and mean cover time of a non-backtracking random walk on graphs*, IEICE Communications Express 12 (2023), advance online 2022-11-07, https://doi.org/10.1587/comex.2022XBL0146 .
