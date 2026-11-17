# A persistent rational five-sphere cohomology class in symmetric quotients of two-letter injective-word moment-angle spaces

## Finding
Let \(n\ge 2\). The **two-letter injective-word simplicial poset** \(J_n\) consists of an initial element, \(n\) vertices, and one distinct one-cell for each ordered pair of different labels. In particular, the arcs \((i,j)\) and \((j,i)\) give *different edges* with the same endpoints, and no words of length three occur. Set \(Z_n=\mathcal Z_{J_n}(D^2,S^1)\), the moment-angle space of this simplicial poset (not of its folded ordinary graph). Coordinate and word relabeling give an \(S_n\)-action.

For every \(2\le k\le n\), the complete reduced **integral** additive cohomology is
\[
 \widetilde H^{k+2}(Z_n;\mathbb Z)\cong\mathbb Z^{\binom nk (k-1)^2},
\]
with no reduced cohomology in other degrees. Let \(L_k=H^1(|J_k|;\mathbb Z)\) with its natural, geometrically oriented \(S_k\)-action. The **integral symmetry lattice**, not merely its rational character, is
\[
\widetilde H^{k+2}(Z_n;\mathbb Z)\cong
\operatorname{Ind}_{S_k\times S_{n-k}}^{S_n}
\bigl((\operatorname{sgn}_k\otimes L_k)\boxtimes\mathbf1\bigr).
\]
Most notably, for every \(n\ge3\), the permutation quotient \(Z_n/S_n\) has the rational cohomology *ring* of \(S^5\):
\[
H^q(Z_n/S_n;\mathbb Q)\cong
\begin{cases}\mathbb Q&q=0,5,\\0&\text{otherwise},\end{cases}
\]
and the product of two positive-degree classes vanishes. For \(n=2\), the quotient is rationally acyclic in all positive degrees. The assertion concerns rational cohomology, **not** the homotopy type of the quotient.

## Assumptions and scope
For \(I\subseteq[n]\), the full subposet \((J_n)_I\) has all vertices in \(I\) and exactly two edges between each unordered pair in \(I\). This is the *rank-two truncation* (one-skeleton) of the ordered complex of injective words. The full injective-word complex and the simplicial complex obtained by forgetting arc directions are different input spaces.

The moment-angle construction is the simplicial-poset colimit of products of \(D^2\) on the support of a face and \(S^1\) on its complement, with the canonical homotopy-invariant cellular interpretation. Relabeling acts both on the poset and on the disk/circle coordinates. The integer group \(L_k\) is the first cellular cohomology of a connected graph with \(k\) vertices and \(k(k-1)\) edges, with orientations chosen consistently from smaller to larger endpoints; the word index distinguishes the two parallel edges.

## Proof
**1. Full-subposet topology.** For \(|I|=k\ge2\), the connected one-dimensional complex \(|(J_n)_I|\) has \(k(k-1)\) edges and \(k\) vertices, hence integral first cohomology of rank \(k(k-1)-k+1=(k-1)^2\) and no other reduced integral cohomology. For a singleton the reduced cohomology is zero. The empty full subposet has conventional reduced cohomology \(\widetilde H^{-1}(\varnothing;\mathbb Z)=\mathbb Z\).

**2. Hochster grading.** The integral Hochster decomposition for simplicial posets (Lü–Panov, Corollary 3.8) gives, with \(p\) a cohomological degree,
\[
H^p(Z_n;\mathbb Z)\cong
\bigoplus_{I\subseteq[n]}\widetilde H^{p-|I|-1}(|(J_n)_I|;\mathbb Z).
\]
The empty subset contributes \(H^0\). Every nonempty contribution with \(|I|=k\ge2\) lies precisely in degree \(p=k+2\), yielding the stated integer ranks and no torsion.

**3. Integral equivariance and signs.** In the cellular Koszul model of Lü–Panov, the multidegree-\(I\) summand has cochains \(u_{I\setminus V(\sigma)}v_\sigma\) indexed by cells \(\sigma\) supported in \(I\). The exterior generators \(u_i\) anticommute and have degree one; \(v_\sigma\) has degree twice the number of vertices in \(\sigma\). If a permutation preserves \(I\), reordering the exterior factors contributes the sign of its restriction to \(I\), relative to the ordinary simplicial-poset cellular cochain action. Consequently this summand's integral cohomology is \(\operatorname{sgn}_I\otimes H^1(|(J_n)_I|;\mathbb Z)\). The subspaces indexed by the \(k\)-subsets form one transitive permutation orbit with stabilizer \(S_k\times S_{n-k}\), proving the induced **integral**, rather than merely rational, representation. The sign is essential: for two letters, their swap reverses the orientation of \(Z_2\simeq S^4\).

**4. Character and quotient.** For \(g\in S_k\) with \(f\) fixed letters, the oriented cellular chain spaces of \(|J_k|\) give \(\operatorname{tr}(g\mid C_1)=f(f-1)\), \(\operatorname{tr}(g\mid C_0)=f\), and \(\operatorname{tr}(g\mid H_0)=1\). The first cohomology character is therefore \((f-1)^2\). Its sign-isotypic multiplicity is computed using the exact equivariant cellular sequence. The edge module is the permutation module on ordered pairs, induced from \(S_{k-2}\); the vertex module is induced from \(S_{k-1}\). By Frobenius reciprocity, the sign multiplicity in the edge module is one exactly for \(k=2,3\), while in the vertex module it is one exactly for \(k=2\). Hence the sign multiplicity in \(H^1(|J_k|;\mathbb Q)\) equals one for \(k=3\) and zero for every other \(k\ge2\). Frobenius reciprocity applied to the induced module in step 3 therefore leaves precisely one invariant class, in degree \(k+2=5\), for all \(n\ge3\). For a finite group acting on a finite CW complex, rational cohomology of the orbit space equals the invariant part of the original rational cohomology. Since there is only one positive degree, its square vanishes, giving the rational cohomology *ring* of the five-sphere.

For completeness, if \(g\in S_n\) has \(f\) fixed letters and \(c_j\) cycles of length \(j\ge2\), the full graded positive-degree character is given by the coefficient of \(z^k\) in
\[
\left((1+z)^f-fz(1+z)^{f-1}+f(f-1)z^2(1+z)^{f-2}\right)
\prod_{j\ge2}\left(1+(-1)^{j-1}z^j\right)^{c_j}-1.
\]
Terms multiplied by \(f\) or \(f(f-1)\) are understood as zero for small \(f\); the constant subtraction removes the empty multidegree. This expression follows by summing the signed character \((f_I-1)^2\operatorname{sgn}(g|_I)\) over \(g\)-invariant subsets \(I\) of size \(k\).

## Verification
The standalone `verify.py` constructs the oriented doubled-edge cellular boundary, checks its exact rational ranks, constructs the complete local Lü–Panov multidegree cellular Koszul differentials, checks their compositions vanish, and checks exact rational ranks \(1\), \(k-1\) and \((k-1)^2\). Independently, it computes signed traces from the oriented graph cellular actions, cycle-type trace formulas, and the Koszul cellular action, over all permutations for sizes from two through six. The invariant multiplicity is calculated by exact averaging; no floating-point or probabilistic computations enter. Its output is embedded in `verification_output.txt` and may be reproduced with `python3 verify.py`. These finite checks support, but do not replace, the arbitrary-\(n\) structural proof.

## Relationship to prior work
Lü and Panov establish the moment-angle construction and Hochster decomposition for arbitrary simplicial posets, and explicitly analyze the two-vertex/two-edge example giving \(S^4\). Conceição calculates a homotopy decomposition of the **full** injective-word moment-angle complex (with all word lengths) using derangement numbers. Neither states the all-size integral symmetry module or the persistent degree-five rational class of the **rank-two truncation** quotient. The full-complex symmetric quotient has separately been studied and has vanishing positive rational cohomology; this contrasts with the rank-two truncation rather than implying it. The general Hochster theorem already contains the nonequivariant rank computation as a formal consequence; novelty is claimed only for the combined explicit integral symmetry description and symmetric-quotient stabilization. Overlap with unindexed or equivalently formulated equivariant Hochster examples remains possible.

## Limitations
No equivariant homotopy decomposition of \(Z_n\) and no integral cohomology calculation for \(Z_n/S_n\) are asserted. The rational cohomology-ring comparison to \(S^5\) is **not** a rational homotopy equivalence, and does not exclude torsion or nontrivial fundamental groups in the orbit space. The calculation uses the full permutation action and the one-skeleton only; higher word-length truncations are not covered.

## References
1. Pedro Conceição, *The homotopy type of the moment-angle complex associated to the complex of injective words*, arXiv:2603.09491, first submitted 2026-03-10, §§1–2 (Definition 1.1 and Theorem 2.10). https://arxiv.org/abs/2603.09491
2. Zhi Lü and Taras Panov, *Moment-angle complexes from simplicial posets*, arXiv:0912.2219, §§2–3, especially Theorem 3.6, Corollary 3.8 and Example 3.9. https://arxiv.org/abs/0912.2219
3. *Symmetric-group cohomology and rationally acyclic quotients of injective-word moment-angle complexes*, publicly indexed 2026-10-11, for the full-word comparison. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-symmetric-group-cohomology-and-rationally-acyclic-quotients-of-i--59fb07600ff9
