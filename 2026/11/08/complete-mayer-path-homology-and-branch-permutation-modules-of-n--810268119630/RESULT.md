# Complete Mayer path homology and branch-permutation modules of nontransitive directed theta networks

## Finding
For each integer \(m\ge 2\), let \(T_m\) be the finite digraph with vertices \(s,t,a_1,\ldots,a_m\), arcs \(s\to a_i\) and \(a_i\to t\) for each \(i\), and **no** arc \(s\to t\) or other arcs. The branch permutations induce an \(S_m\)-action. Write \(\mathbf1\) for the trivial complex representation and \(U_m=\{(z_1,\ldots,z_m)\in\mathbb C^m:\sum z_i=0\}\) for the standard augmentation representation.

For every integer \(N\ge3\), primitive \(N\)-th root \(\xi\in\mathbb C\), and integer \(1\le q\le N-1\), the complete **unreduced** Mayer path homology representations are:

\[
H_0^{N,q}(T_m)\cong
\begin{cases}
\mathbf1,&q=N-1,\\
\mathbf1^{\oplus3},&q=N-2,\\
\mathbf1^{\oplus3}\oplus U_m,&1\le q\le N-3;
\end{cases}
\]
\[
H_1^{N,q}(T_m)\cong
\begin{cases}
U_m,&q=1,\\
\mathbf1^{\oplus2}\oplus U_m,&q=N-1,\\
\mathbf1^{\oplus2}\oplus U_m^{\oplus2},&2\le q\le N-2;
\end{cases}
\]
\[
H_2^{N,q}(T_m)\cong
\begin{cases}0,&q\le2,\\U_m,&3\le q\le N-1.\end{cases}
\]
Empty intervals are omitted. All \(H_k^{N,q}\) for \(k\ge3\) are zero. At \(N=2\), \(q=1\), one has \(H_0^{2,1}(T_m)\cong\mathbf1\) and \(H_k^{2,1}(T_m)=0\) for \(k\ge1\). These are equivariant isomorphisms over \(\mathbb C\), not claims about integral modules.

## Assumptions and scope
Use the complex-coefficient, primitive-root \(N\)-differential on regular allowed directed paths, \(\partial e_{v_0\cdots v_k}=\sum_{j=0}^k\xi^j e_{v_0\cdots\widehat v_j\cdots v_k}\), and the **fully boundary-invariant** path complex \(\Omega^N\) of Karaguler--Wei. Thus \(H_k^{N,q}=\ker(\partial^q:\Omega_k^N\to\Omega_{k-q}^N)/\operatorname{im}(\partial^{N-q}:\Omega_{k+N-q}^N\to\Omega_k^N)\), with groups at negative or unavailable degrees zero. No paths of positive length three occur in \(T_m\); regular and nonregular differentials agree on its allowed paths.

## Proof
Put \(\alpha_i=e_{s,a_i}\), \(\beta_i=e_{a_i,t}\), and \(u_i=e_{s,a_i,t}\). The allowed chain dimensions are \(\dim\mathcal A_0=m+2\), \(\dim\mathcal A_1=2m\), \(\dim\mathcal A_2=m\), and zero thereafter. The only forbidden face of any \(u_i\) is \(e_{s,t}\), with nonzero coefficient \(\xi\). Hence a combination \(\sum c_i u_i\) is fully boundary-invariant exactly when \(\sum c_i=0\); its second boundary is always a valid zero-chain, and all higher boundaries vanish. Consequently
\[
\Omega_0^N\cong\mathbf1^{\oplus3}\oplus U_m,\qquad
\Omega_1^N\cong\mathbf1^{\oplus2}\oplus U_m^{\oplus2},\qquad
\Omega_2^N\cong U_m,\qquad \Omega_k^N=0\ (k\ge3).
\]
Here and below these identifications use the natural branch action, and the dimension-count identity for \(\Omega_0\) uses \(\mathbb C^m\cong\mathbf1\oplus U_m\).

Let \(D_1:\Omega_1^N\to\Omega_0^N\) and \(D_2:\Omega_2^N\to\Omega_1^N\) be the induced maps. The exact formulas are
\[
D_1\alpha_i=e_{a_i}+\xi e_s,\qquad
D_1\beta_i=e_t+\xi e_{a_i},\qquad
D_2(u_i-u_j)=(\beta_i-\beta_j)+\xi^2(\alpha_i-\alpha_j).
\]
The image of \(D_1\) has dimension \(m+1\): its cokernel is the single trivial line of linear functionals assigning compatible values \(f(a_i)=-\xi f(s)\) and \(f(t)=\xi^2 f(s)\). The map \(D_2\) is injective since its \(\beta\)-component remembers the coefficient vector. Moreover,
\[
D_1D_2(u_i-u_j)=\xi(1+\xi)(e_{a_i}-e_{a_j}).
\]
For \(N=2\), this composition vanishes; for every primitive root with \(N\ge3\), its scalar is nonzero. Thus
\[
\operatorname{rank}(D_1)=m+1,\quad
\operatorname{rank}(D_2)=m-1,\quad
\operatorname{rank}(D_1D_2)=\begin{cases}0&N=2,\\m-1&N\ge3.\end{cases}
\]
More precisely, \(\ker D_1\cong U_m\), \(\operatorname{im} D_2\cong U_m\), and \(\operatorname{im}D_1D_2\cong U_m\) for \(N\ge3\). Also \(\Omega_1^N/\operatorname{im}D_2\cong\mathbf1^{\oplus2}\oplus U_m\) and \(\Omega_0^N/\operatorname{im}D_1D_2\cong\mathbf1^{\oplus3}\). These module identifications follow from equivariance and semisimplicity over \(\mathbb C\).

Only \(\partial\), \(\partial^2\), and the zero higher powers can act nontrivially on this length-two path complex. Substitution in the definition of \(H_k^{N,q}\) yields the displayed piecewise formula in every allowed \(q\), including the classical \(N=2\) cancellation \(\ker D_1=\operatorname{im}D_2\). There are no degrees above two.

## Verification
The standalone `verify.py` constructs all allowed boundary matrices and the square-difference basis, finds primitive roots in finite fields, independently performs modular Gaussian elimination, and tests the full degree-zero, degree-one, and degree-two Betti vectors for every \(m\in[2,9]\), \(N\in[2,8]\), and all \(q\in[1,N-1]\). It checks 224 tuples and independently verifies \(\operatorname{rank}D_1\), \(\operatorname{rank}D_2\), and \(\operatorname{rank}(D_1D_2)\). Exact finite-field agreement is corroboration only; the preceding proof supplies the all-parameter complex-field theorem.

## Relationship to prior work
Karaguler and Wei (2026), arXiv:2605.16525, define Mayer path homology, classify invariant two-path generators, and explicitly calculate the four-node biparallel motif for selected low orders; those statements are prior work. The present theorem concerns every branch count and every primitive order/index, with the entire branch-permutation representation, rather than only selected dimensions. A separately published result on augmentation-block characters for **complete transitively layered** digraphs assumes all forward shortcuts, unlike this network, whose missing \(s\to t\) arc is exactly responsible for the nonzero square-difference space. Existing results on monotone two-row ladders involve a different digraph, with distinct layer and path incidence.

## Limitations
The classification holds for a single common source, a single common target, and an arbitrary number of length-two branches without a direct shortcut. It does not cover unequal intermediate layers, feedback edges, added source-to-target shortcuts, integral coefficient analogues, or general higher-length theta networks. As in any literature-based originality comparison, unindexed equivalent treatments remain possible.

## References
1. D. Karaguler and G.-W. Wei, *Mayer Path Homology*, arXiv:2605.16525 (first posted 2026-05-15), https://arxiv.org/abs/2605.16525. See Definitions 6--8, Theorem 3.2, and Examples 3.1--3.4.
2. *Augmentation-block characters of Mayer path homology on layered digraphs*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-augmentation-block-characters-of-mayer-path-homology-on-layered--b242671c032d (different hypothesis: all transitive forward arcs).
