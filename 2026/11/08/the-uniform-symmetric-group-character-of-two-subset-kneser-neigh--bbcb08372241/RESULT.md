# The uniform symmetric-group character of two-subset Kneser neighborhood homology

## Finding

For each integer \(n\ge5\), let \(G_n=\operatorname{KG}(n,2)\) denote the Kneser graph on the two-element subsets of \([n]=\{1,\ldots,n\}\), adjacent when disjoint. Let \(K_n=\mathcal N(G_n)\) be its **ordinary open Lovász neighborhood complex**. The natural relabeling action of \(S_n\) on \(K_n\) induces an action on rational reduced homology. If \(f(\sigma)\) is the number of fixed points of \(\sigma\in S_n\), the only nonzero reduced rational homology is in degree \(n-4\), and its character is

\[
\operatorname{tr}\bigl(\sigma\mid\widetilde H_{n-4}(K_n;\mathbb Q)\bigr)
=\operatorname{sgn}(\sigma)\bigl(f(\sigma)^2-3f(\sigma)+1\bigr).
\]

Equivalently, in the notation of rational Specht modules indexed by partitions of \(n\),

\[
\widetilde H_{n-4}(K_n;\mathbb Q)
\cong S^{(3,1^{n-3})}\oplus S^{(2,2,1^{n-4})}
\quad\text{as }\mathbb Q[S_n]\text{-modules}.
\]

Each irreducible occurs with multiplicity one. In particular,

\[
\dim\widetilde H_{n-4}(K_n;\mathbb Q)=n^2-3n+1,
\qquad
\widetilde H_*(K_n/S_n;\mathbb Q)=
\widetilde H_*(K_n/A_n;\mathbb Q)=0.
\]

The nonequivariant homotopy type and resulting rank were already known; the new finding is the **uniform full-group homology character, representation decomposition, and quotient consequence**. The instance \(n=6\) was also previously obtained separately, and is not claimed as a new isolated case.

## Assumptions and scope

All graphs are finite, loopless and undirected. The open neighborhood complex \(\mathcal N(G)\) has a nonempty simplex \(F\subseteq V(G)\) precisely when there exists a vertex adjacent to every member of \(F\); the empty face is included for reduced chains. Two vertices of \(G_n\) are unordered two-subsets of \([n]\). Hence the vertices of \(K_n\) are naturally the edges of the abstract complete graph on \([n]\).

A set \(F\) of these edges is a face of \(K_n\) exactly when the graph \(([n],F)\) has **at least two isolated vertices**: the two absent labels form a common neighbor in \(G_n\). This equivalence is literal and equivariant under \(S_n\). We use reduced simplicial chains with their standard orientation signs, coefficient field \(\mathbb Q\), and the natural coordinate-relabeling action. We do not assert a classification of integral \(S_n\)-lattices or equivariant homotopy types.

The previously proved nonequivariant theorem of Nilakantan and Singh [3, Theorem 1.3] states

\[
K_n\simeq\bigvee^{n^2-3n+1} S^{n-4}\quad (n\ge5).
\]

It supplies the homology-concentration premise. The remaining representation computation below is independent of the discrete-Morse choices in that theorem.

## Proof

**1. Alternating simplex traces.** Fix \(\sigma\in S_n\), write its disjoint vertex cycles as \(C_1,\ldots,C_c\), and let \(f\) count its one-element cycles. For a \(\sigma\)-invariant set \(F\) of edges, let \(o(F)\) be the number of orbits of \(\sigma\) on the edges belonging to \(F\). A simplex on \(F\) contributes to the alternating trace of its simplicial chain complex only if it is fixed setwise. Its orientation sign is \((-1)^{|F|-o(F)}\), since each orbit of length \(r\) has permutation sign \((-1)^{r-1}\). Including the dimension factor \((-1)^{|F|-1}\), its contribution is \((-1)^{o(F)-1}\). The augmentation chain in degree \(-1\) contributes \(-1\). Consequently, writing the empty set as a fixed face with \(o(\varnothing)=0\), the **reduced** Lefschetz number is

\[
\widetilde L(\sigma;K_n)
=-\sum_{\substack{F\subseteq\binom{[n]}2:\ \sigma F=F\\
\left|[n]\setminus\operatorname{supp}(F)\right|\ge2}}
(-1)^{o(F)},
\]

where \(\operatorname{supp}(F)\) is the set of endpoints of edges in \(F\). The condition permits \(F=\varnothing\). The same Lefschetz number is the alternating sum of traces on reduced homology, by equivariant Euler–Poincaré.

**2. Cancellation on supports.** If \(F\) is \(\sigma\)-invariant, its support is a union of some vertex cycles \(C_i\). For \(I\subseteq[c]\), put \(V_I=\bigcup_{i\in I}C_i\), let \(f_I\) be the number of singleton cycles indexed by \(I\), and let

\[
w(I)=\sum_{\substack{F:\ \sigma F=F\\\operatorname{supp}(F)=V_I}}
(-1)^{o(F)}.
\]

First sum over fixed edge subsets with support **contained in** \(V_J\). Such subsets are arbitrary unions of orbits of \(\sigma\) on the edges of the complete graph on \(V_J\). Their weight sum is \((1-1)^m\), where \(m\) is the number of these edge orbits. It equals \(1\) if \(|V_J|\le1\) and \(0\) otherwise. Möbius inversion on the Boolean lattice of cycle subsets therefore gives

\[
\begin{aligned}
w(I)
&=\sum_{J\subseteq I}(-1)^{|I|-|J|}
\mathbf 1_{\{|V_J|\le1\}}\\
&=(-1)^{|I|}(1-f_I).
\end{aligned}
\]

The only contributing \(J\) are the empty index set and the \(f_I\) singleton fixed-point cycles. This argument is finite but works symbolically for **every** \(n\), rather than extrapolating a finite enumeration.

The weight over **all** \(\sigma\)-invariant subsets of edges of the complete graph is zero, because the complete graph has at least one edge orbit and the sum of weights over its orbit choices is \((1-1)^m=0\). An edge set is **excluded** from the neighborhood complex precisely when it has at most one isolated vertex. By invariance, that occurs if its support is \(V_{[c]}\), or \(V_{[c]\setminus\{j\}}\) for one of the \(f\) singleton cycles. Thus the total weight of excluded sets is

\[
\begin{aligned}
w([c])+\sum_{j:\ |C_j|=1}w([c]\setminus\{j\})
&=(-1)^c(1-f)+f(-1)^{c-1}(2-f)\\
&=(-1)^c(f^2-3f+1).
\end{aligned}
\]

The allowed weight is its negative; applying the minus sign in the reduced Lefschetz formula yields

\[
\widetilde L(\sigma;K_n)=(-1)^c(f^2-3f+1).
\]

**3. The actual homology character.** The previously established sphere-wedge theorem [3] implies that reduced rational homology is concentrated in degree \(n-4\). Therefore

\[
\operatorname{tr}(\sigma\mid\widetilde H_{n-4}(K_n;\mathbb Q))
=(-1)^{n-4}\widetilde L(\sigma;K_n)
=(-1)^{n+c}(f^2-3f+1).
\]

A permutation of \(n\) symbols with \(c\) cycles has sign \((-1)^{n-c}=(-1)^{n+c}\). This proves the character formula.

**4. Specht constituents.** Let \(U\) be the \((n-1)\)-dimensional standard representation of \(S_n\), with character \(f-1\), and let \(t\) count two-cycles of \(\sigma\). The permutation representation on unordered pairs has character \(\binom f2+t\) and decomposes as

\[
\mathbf1\oplus U\oplus S^{(n-2,2)}.
\]

Hence the character of \(S^{(n-2,2)}\) is \(\binom f2+t-f\). Also \(\bigwedge^2U\cong S^{(n-2,1,1)}\), whose character is

\[
\tfrac12\bigl((f-1)^2-(f+2t-1)\bigr)=\tfrac12(f^2-3f+2-2t).
\]

Adding the two irreducible characters gives \(f^2-3f+1\). Tensoring with the sign representation conjugates partitions. Therefore the character calculated in step 3 is precisely the sum of the two rational Specht characters indexed by \((2,2,1^{n-4})\) and \((3,1^{n-3})\). Semisimplicity of rational \(S_n\)-representations proves the claimed module decomposition. The two dimensions are \(n(n-3)/2\) and \((n-1)(n-2)/2\), whose sum is \(n^2-3n+1\).

**5. Quotients.** Neither Specht constituent is the trivial representation or the sign representation for \(n\ge5\). Thus the top homology contains no \(S_n\)-invariants, nor \(A_n\)-invariants (by Frobenius reciprocity and \(\operatorname{Ind}_{A_n}^{S_n}\mathbf1=\mathbf1\oplus\operatorname{sgn}\)). After barycentric subdivision a finite simplicial group action has no simplex inversions; in characteristic zero, orbit-space cellular chains identify with coinvariants and averaging identifies coinvariants with invariants. The rational homology of each quotient therefore agrees with the invariant homology and is reduced-acyclic. No contractibility assertion is needed or implied.

## Verification

The companion Python standard-library script `verify.py` implements two independent finite checks of the character calculation. It computes fixed-edge-orbit alternating sums by dynamic programming over exact vertex-support bitmasks, testing all \(85\) cycle types for \(5\le n\le9\). For \(n=5,6\), it additionally constructs every nonempty neighborhood simplex directly and evaluates signed chain traces using explicit orientation-permutation inversions. Exact class-size-weighted character inner products confirm the vanishing of trivial and sign constituents, character norm two, and the two hook-length dimensions for each tested \(n\). Its recorded output is `verification_output.txt`.

The general theorem is **not** inferred from these finite tests: the arbitrary-\(n\) support-cancellation proof above establishes the trace identity, and the cited homotopy theorem establishes homology concentration. Reproduction command: `python3 verify.py`. Python 3 standard library suffices.

## Relationship to prior work

Babson, Björner, Linusson, Shareshian and Welker [1] determined a different symmetric-group homology character for the complex of graphs that are not two-connected. That graph complex has much larger homology in degree \(2n-5\); its theorem does not describe the subcomplex of graphs with **two isolated vertices**, which is the present neighborhood complex. Braun and Zeckner [2] considered invariant sphere models for *stable* Kneser graphs and their dihedral symmetries, not the natural full \(S_n\) action on the ordinary Kneser graph. Nilakantan and Singh [3] established the full **nonequivariant** neighborhood-complex homotopy type; it supplies concentration but no full symmetric-group character or Specht decomposition.

A separately recorded computation [4] already identifies the two irreducible constituents at \(n=6\); that instance agrees exactly with the formula here and is explicitly **prior coverage**. A formula uniform over all \(n\ge5\), including the universal fixed-point polynomial, and the rationally acyclic quotients are the claimed new contribution. The independent existence of equivalent unindexed work cannot be ruled out by searches.

## Limitations

Only the rational \(S_n\)-module is classified; integral lattice structure, characteristic-positive decomposition, equivariant homotopy type, and integral homology of the quotients remain open in this work. The quotients are shown to be rationally acyclic, **not** contractible. The nonequivariant sphere-wedge theorem and the \(n=6\) representation are acknowledged as previously established. The work has not undergone independent mathematical audit or definitive publication-priority verification.

## References

1. E. Babson, A. Björner, S. Linusson, J. Shareshian and V. Welker, *Complexes of not i-connected graphs* (1997), arXiv:math/9705219, https://arxiv.org/abs/math/9705219 (first public arXiv version: 1997-05-11).
2. B. Braun and M. Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs* (2011), arXiv:1102.1984, https://arxiv.org/abs/1102.1984 (first public arXiv version: 2011-02-09).
3. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(\mathrm{KG}_{2,k}\)* (2018), arXiv:1802.05848, https://arxiv.org/abs/1802.05848 (Theorem 1.3; first public arXiv version: 2018-02-16).
4. *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rational-symmetry-decomposition-of-the-kneser-neighborhood-compl--6890383e239b (a previously recorded six-point calculation; consulted via indexed claim summary).
