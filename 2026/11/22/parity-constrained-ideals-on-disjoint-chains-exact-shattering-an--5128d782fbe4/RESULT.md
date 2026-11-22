# Parity-constrained ideals on disjoint chains: exact shattering and integral homology

## Finding

Let \(k\geq1\), \(L\geq2\), and \(p\in\{0,1\}\). Let \(P_{k,L}\) be the disjoint union of \(k\) chains of \(L\) elements each. Consider the concept class \(\mathcal I_p(P_{k,L})\) consisting of all order ideals \(I\subseteq P_{k,L}\) with \(|I|\equiv p\pmod 2\), queried by membership of individual elements. Its shattered-support complex \(\Delta_{k,L,p}\) admits an exact face criterion, a full face polynomial, and a complete integral reduced-homology calculation.

Write \(a_{i,j}\) for the element at height \(j\in\{1,\ldots,L\}\) in chain \(i\in\{1,\ldots,k\}\). The shattered supports are precisely:

1. Every set selecting at most one element from each chain and strictly fewer than \(k\) elements.
2. Every full transversal \(S=\{a_{1,j_1},\ldots,a_{k,j_k}\}\) for which some \(j_i\) is interior, namely \(2\leq j_i\leq L-1\).
3. A full transversal with all \(j_i\in\{1,L\}\) precisely when \(p\equiv L\#\{i:j_i=L\}\pmod 2\).

No support containing two elements from one chain is shattered.

Set
\[
M_{k,L,p}=
\begin{cases}
0,& L\text{ even and }p=0,\\
2^k,& L\text{ even and }p=1,\\
2^{k-1},& L\text{ odd }(p=0\text{ or }1).
\end{cases}
\]
Then the complete shattered-support polynomial is
\[
\boxed{\Phi_{k,L,p}(z)=(1+Lz)^k-M_{k,L,p}z^k}.
\]
The VC dimension equals \(k\), except for \(L=2,p=1\), when it equals \(k-1\) (including value zero for \(k=1\)).

The **integral reduced homology** is torsion-free, with the following complete list of nonzero groups (a displayed rank zero means the group is absent):

- If \(L\geq3\), then
  \[
  \widetilde H_{k-1}(\Delta_{k,L,p};\mathbb Z)
  \cong \mathbb Z^{(L-1)^k-M_{k,L,p}},
  \]
  and every other reduced homology group vanishes.
- If \(L=2,p=0\), then \(\Delta_{k,2,0}\) is the boundary complex of a \(k\)-dimensional cross-polytope, and its sole nonzero reduced group is \(\widetilde H_{k-1}\cong\mathbb Z\).
- If \(L=2,p=1\), then \(\Delta_{k,2,1}\) is the \((k-2)\)-skeleton of that boundary complex; its sole nonzero reduced group is
  \[
  \widetilde H_{k-2}(\Delta_{k,2,1};\mathbb Z)
  \cong\mathbb Z^{2^k-1}.
  \]
  For \(k=1\), use the standard augmented-simplicial convention: the complex consists only of the empty face, with \(\widetilde H_{-1}\cong\mathbb Z\).

Thus, for even \(L\geq4\), the two parity classes have the **same VC dimension** \(k\) but their top integral Betti numbers differ by the exact exponential quantity \(2^k\); at \(L=2\) the odd class instead loses a full VC level and moves its only nonzero homology to one lower degree.

## Assumptions and scope

All posets are finite; chains are disjoint and have equal positive length \(L\geq2\). Order ideals are downward closed. Every concept is a complete ideal, not merely an allowed trace on the queried support. The chosen parity \(p\) is the parity of total ideal cardinality, not of the number of nonempty chains. A support is shattered if all \(2^{|S|}\) membership patterns on it arise from some concept of the prescribed parity. Homology is ordinary reduced simplicial homology with integer coefficients and the augmented convention at dimension \(-1\).

## Proof

**1. Parametrization.** An ideal is uniquely determined by integers \((t_1,\ldots,t_k)\), with \(0\leq t_i\leq L\), where chain \(i\) contributes precisely its first \(t_i\) elements. The parity condition is \(\sum_i t_i\equiv p\pmod2\). Membership at \(a_{i,j}\) is the condition \(t_i\geq j\).

**2. Nontransversals and proper transversals.** If a support has two queried elements in one chain, their membership labels must be monotone, so one of four pair patterns is impossible. If a support has at most one query per chain and omits a whole chain, every requested pattern is realized on the queried chains by choosing some prefix lengths within their prescribed intervals; the unused chain can be assigned length zero or one to adjust the total parity freely. Hence every proper transversal is shattered.

**3. Full transversals.** For one query at height \(j\), a negative answer requires \(t\in\{0,\ldots,j-1\}\), and a positive answer requires \(t\in\{j,\ldots,L\}\). An interval containing two consecutive integers realizes both parities. If some queried height is interior, each of its two answer intervals contains two consecutive integers, so every complete answer pattern can be parity-adjusted there. At the bottom endpoint \(j=1\), only the negative interval is a singleton, namely \(\{0\}\). At the top endpoint \(j=L\), only the positive interval is a singleton, namely \(\{L\}\). Thus with all queries at endpoints there is exactly one pattern with no local parity flexibility: it prescribes negative answers at every bottom-endpoint query and positive answers at every top-endpoint query. Its unique prefix vector has coordinate zero at bottom endpoints and \(L\) at top endpoints. This pattern is realizable iff its parity is \(p\), as in item 3 of the finding. All other answer patterns have a flexible interval and occur in both parities. This proves the exact face criterion, including its boundary cases \(k=1\) and \(L=2\).

**4. Counting.** A proper transversal of size \(s<k\) is specified by choosing \(s\) of the \(k\) chains and one of \(L\) elements in each, giving \(\binom{k}{s}L^s\). There are \(L^k\) full transversals. When \(L\) is even, every fully endpoint-restricted rigid trace has even parity, so exactly zero or \(2^k\) top faces are omitted according to \(p\). For odd \(L\), exactly half of the \(2^k\) endpoint transversals have the wrong rigid parity. This proves the polynomial and dimension claims.

**5. Integral homology for \(L\geq3\).** Let \(X\) be the join of \(k\) discrete sets of \(L\) vertices (one set for each chain), so \(X\) consists of *all* transversals. Standard join-chain homology, or the tensor product of augmented simplicial chain complexes, gives
\[
\widetilde H_i(X;\mathbb Z)=
\begin{cases}
\mathbb Z^{(L-1)^k},&i=k-1,\\
0,&i\ne k-1.
\end{cases}
\]
Our complex \(Y=\Delta_{k,L,p}\) contains the full \((k-2)\)-skeleton of \(X\) and omits exactly \(M=M_{k,L,p}\) of its \((k-1)\)-simplices, all endpoint transversals. Consequently the relative simplicial chain complex \(C_\bullet(X,Y)\) is \(\mathbb Z^M\) in degree \(k-1\), with no other relative groups.

For each missing endpoint transversal \(F=\{v_1,\ldots,v_k\}\), choose in chain \(i\) an interior vertex \(w_i\), possible since \(L\geq3\). The simplicial join of zero-cycles \((v_i-w_i)\) is an integral \((k-1)\)-cycle in \(X\). Of the \(2^k\) simplices in its expansion, only \(F\) is an entirely endpoint transversal, so its image in \(H_{k-1}(X,Y)\cong\mathbb Z^M\) is a signed coordinate basis vector. Thus the natural map
\[
\widetilde H_{k-1}(X;\mathbb Z)\longrightarrow
H_{k-1}(X,Y;\mathbb Z)\cong\mathbb Z^M
\]
is surjective, and the relevant long exact sequence of the pair gives \(\widetilde H_{k-1}(Y)\cong\ker(\mathbb Z^{(L-1)^k}\to\mathbb Z^M)\cong\mathbb Z^{(L-1)^k-M}\), with no other reduced groups. The kernel is free because it is a subgroup of a free abelian group. For \(k=1\), this argument is the elementary reduced \(H_0\) calculation for \(L-M\) surviving vertices.

**6. The exceptional length-two boundary.** If \(L=2,p=0\), no full transversal is deleted, and \(X\) is the join of \(k\) two-vertex sets, which is a triangulated \(S^{k-1}\). If \(L=2,p=1\), every full transversal is deleted. The remaining \((k-2)\)-skeleton has no \((k-1)\)-chains, while the original \((k-1)\)-boundary map has rank \(2^k-1\) because its integral kernel is generated by the single fundamental cycle of the cross-polytope sphere. The remaining augmented chain complex therefore has a single reduced homology group, freely generated in degree \(k-2\) with rank \(2^k-1\); this also covers \(k=1\) with the stated convention.

## Verification

The two standalone files `verify.py` and `verify.cpp` enumerate the parity-constrained ideals by independently implemented prefix-state algorithms. Both enumerate every query support of cardinality at most \(k\) and compare all its Boolean traces, for all \(k=1,2,3\), \(L=2,3,4,5\), and both parities: **24 complete finite profiles** in each implementation. The Python file additionally computes binary simplicial boundary ranks, without assuming the claimed integral formula, for \(k=1,2,3\), \(L=2,3,4\), and both parities: **18 topology cases**. All checks passed. `verification_output.txt` contains the captured finite outputs. Sample independently computed results include:
\[
\begin{array}{c|c|c|c}
(k,L,p)&\Phi(z)&\text{nonzero reduced mod-two Betti}\\
(3,2,1)&1+6z+12z^2&\beta_1=7\\
(3,3,0)&1+9z+27z^2+23z^3&\beta_2=4\\
(3,4,1)&1+12z+48z^2+56z^3&\beta_2=19.
\end{array}
\]
Finite binary-rank checks corroborate but do not by themselves establish the all-order or integral homology claims; those depend on Steps 1–6.

## Relationship to prior work

Downset enumeration and disjoint-sum structure are longstanding topics in order theory. Campo and Erné (2018, arXiv:1802.01419) develop general downset enumeration and poset-extension formulas, but neither impose a global cardinality parity restriction nor characterize Boolean trace supports or their integral homology. Early (2019) studies rank-unimodality of ideals in *Cartesian products* of chains (rather than the *disjoint unions* here), with a different primary invariant; its results do not imply this parity-trace theorem. General online learning closure bounds, such as Ghazi–Golowich–Kumar–Manurangsi (2021), do not calculate these face complexes. Previously published analyses of unrestricted order-ideal membership and maximal-antichain membership address other concept classes and do not identify this parity-dependent topological transition. No assertion of absolute priority beyond the inspected literature is made.

## Limitations

The theorem assumes equal chain lengths and parity modulo two, and does not give an online (Littlestone) dimension or a result for arbitrary posets. The homology calculation establishes integral groups, not a complete homotopy type for every parameter. Results were independently reconstructed and finitely corroborated but have not received an external mathematical audit; an unindexed or inaccessible equivalent characterization remains possible.

## References

1. F. A Campo and M. Erné, *Exponential functions of finite posets and the number of extensions with a fixed set of minimal points*, first public 2018-02-05, https://arxiv.org/abs/1802.01419.
2. E. Early, *Order ideals in a product of chains*, Australasian Journal of Combinatorics 73(3) (2019), 478–485; first verified public date 2019-05-23, https://ajc.maths.uq.edu.au/pdf/73/ajc_v73_p478.pdf.
3. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Proceedings of Machine Learning Research 132 (2021), 686–696, https://proceedings.mlr.press/v132/ghazi21a.html.
