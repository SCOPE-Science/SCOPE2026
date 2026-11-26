# Exact field staircase and parity-dependent zero-field magnetization of antiferromagnetic Ising rook networks

## Finding

For all integers \(a,b\ge2\), place Ising spins \(\sigma_{ij}\in\{-1,+1\}\) on the rook graph \(R_{a,b}=K_a\square K_b=L(K_{a,b})\). Let all row- and column-interaction edges carry the same antiferromagnetic exchange \(J>0\), and let the uniform field be any \(h\in\mathbb R\). Put \(N=ab\), \(B=ab(a+b-2)/2\). Let \(m\) count \(+1\) spins, and write \(m=aq+r=bu+s\), where \(0\le r<a\), \(0\le s<b\). Define

\[
C_{a,b}(m)=(a-r)q(b-q)+r(q+1)(b-q-1)+(b-s)u(a-u)+s(u+1)(a-u-1).
\]

The exact ground energy at every real field is

\[
E_0(h)=JB+hN-2\max_{0\le m\le N}\bigl(J C_{a,b}(m)+hm\bigr).
\]

The complete ground-state configurations are precisely the binary \(a\times b\) matrices with \(m\) plus entries such that every row contains \(q\) or \(q+1\) plus entries and every column contains \(u\) or \(u+1\) plus entries, with \(m\) maximizing the displayed one-dimensional expression. Each such \(m\) is feasible and no other configuration is a ground state.

The complete set of magnetic-field transition values is

\[
\frac{h}{J}=2\left(\left\lfloor\frac ma\right\rfloor+\left\lfloor\frac mb\right\rfloor\right)-(a+b-2),\qquad m=0,1,\ldots,ab-1.
\]

Its number of **distinct** values is exactly \(a+b-\gcd(a,b)\). Between consecutive distinct transition fields the optimal total number \(m\) of positive spins is unique; at a transition all consecutive sectors spanning the corresponding repeated value are degenerate.

At zero field the exact ground energy and ground-state magnetizations \(M=\sum_{ij}\sigma_{ij}\) are

\[
\frac{E_0(0)}J=-ab+\frac{a(b\bmod2)+b(a\bmod2)}2,
\quad
\mathcal M_0=\begin{cases}
\{-d,-d+2,\ldots,d\},&a,b\text{ both odd},\quad d=\min(a,b),\\
\{0\},&\text{at least one of }a,b\text{ even}.
\end{cases}
\]

Thus when both dimensions are odd, the total magnetization jumps from \(-\min(a,b)\) to \(+\min(a,b)\) as \(h\) passes through zero, whereas for an even dimension there is a nonzero-width zero-magnetization plateau.

## Assumptions and scope

Each rook vertex is one matrix cell \((i,j)\), with \(1\le i\le a\), \(1\le j\le b\). Vertices share an edge exactly when their row or column agrees. All edges are counted once. The Hamiltonian is \(H(\sigma)=J\sum_{vw\in E(R_{a,b})}\sigma_v\sigma_w-h\sum_v\sigma_v\). The result holds for all finite integer dimensions at least two, all uniform \(J>0\) and every real uniform field \(h\), with classical two-state spins. It makes no statement about positive temperature, nonuniform fields, or nonuniform exchange.

## Proof

**1. Energy as a cut problem.** Set \(x_{ij}=(1+\sigma_{ij})/2\) and \(m=\sum_{ij}x_{ij}\). Write \(d_i=\sum_j x_{ij}\) and \(e_j=\sum_i x_{ij}\). Since every row and column is a clique, the number of unlike-spin edges equals

\[
C(x)=\sum_{i=1}^{a}d_i(b-d_i)+\sum_{j=1}^{b}e_j(a-e_j).
\]

Every unlike-spin edge contributes \(-J\) and every like-spin edge \(+J\); furthermore \(\sum\sigma=2m-N\). Therefore \(H=JB+hN-2(JC(x)+hm)\), exactly as claimed.

**2. Sharp fixed-population optimum and simultaneous feasibility.** For fixed \(m\), integer concavity of \(t\mapsto t(b-t)\) says the row sum is maximized exactly when all row counts differ by at most one, namely \(d_i\in\{q,q+1\}\). The same holds for column counts \(e_j\in\{u,u+1\}\). These two constraints are simultaneously attainable for every integer \(0\le m\le ab\): start with any simple bipartite graph (binary matrix) having \(m\) edges. If two rows have counts differing by at least two, some column has an edge to the higher-degree row and no edge to the lower-degree row. Moving that edge balances the pair and leaves every column count unchanged. Repeating strictly decreases the sum of squares of row degrees until all are balanced. Then balance the columns by moving edges between two columns within a row; these moves leave all row counts unchanged, and terminate by the same decreasing-square argument. Hence a matrix simultaneously satisfying both conditions exists. The strictly concave inequalities prove that these and only these matrices attain \(\max C=C_{a,b}(m)\), whose displayed expression follows by counting the \(r\) higher-degree rows and \(s\) higher-degree columns.

**3. Field transitions and their gcd count.** Subtract consecutive fixed-population cut values. Direct integer arithmetic gives for every \(m=0,\ldots,ab-1\):

\[
C_{a,b}(m+1)-C_{a,b}(m)=a+b-2-2\left(\left\lfloor\frac ma\right\rfloor+\left\lfloor\frac mb\right\rfloor\right).
\]

This difference is nonincreasing in \(m\). Consequently \(J C_{a,b}(m)+hm\) is a concave discrete function and its maximizing populations are exactly the sectors determined by the slopes of the upper envelope. Two adjacent sectors tie precisely when \(h/J\) is the negative of their cut difference, yielding the stated complete transition set. It is not necessary to assume distinct adjacent slopes: a repeated slope generates a larger degenerate consecutive block. The floor sum increases at positive multiples of \(a\) below \(ab\) and positive multiples of \(b\) below \(ab\). Those are \(b-1\) and \(a-1\) multiples, and \(\gcd(a,b)-1\) coincide, because their common positive multiples are the multiples of \(\mathrm{lcm}(a,b)\) below \(ab\). Therefore the count of slope changes is \(a+b-\gcd(a,b)-1\), and the count of distinct values is \(a+b-\gcd(a,b)\).

**4. Exact zero-field magnetization.** Each row has at most \(\lfloor b^2/4\rfloor\) unlike-spin edges; each column at most \(\lfloor a^2/4\rfloor\). The simultaneously balanced construction attains both sums, so \(C_{\max}=a\lfloor b^2/4\rfloor+b\lfloor a^2/4\rfloor\), yielding the stated energy after substituting \(B\). Equality holds exactly when every row count belongs to \(\{\lfloor b/2\rfloor,\lceil b/2\rceil\}\) and every column count belongs to \(\{\lfloor a/2\rfloor,\lceil a/2\rceil\}\). Feasible \(m\) lie in the intersection

\[
\left[a\left\lfloor\frac b2\right\rfloor,\ a\left\lceil\frac b2\right\rceil\right]\cap
\left[b\left\lfloor\frac a2\right\rfloor,\ b\left\lceil\frac a2\right\rceil\right]
\]

of integer intervals, and each such \(m\) is feasible by Step 2. If either dimension is even, this intersection is the singleton \(\{ab/2\}\). If both are odd, it is the full integer interval \([(ab-\min(a,b))/2,(ab+\min(a,b))/2]\). Thus the zero-field magnetizations \(M=2m-ab\) are exactly those claimed. At sufficiently small positive or negative nonzero \(h\), the unique optimal population at zero-field boundary is respectively the largest or smallest zero-field optimal \(m\); hence the jump or plateau statement follows.

## Verification

The standalone checker `verification/check_rook.py` enumerates all \(2^{ab}\) configurations on eight rectangles with \(ab\le16\), comparing every fixed-population optimum, its full equality characterization, seven rational magnetic fields, and zero-field magnetization sectors. It also checks 323 larger rectangular instances of the discrete concavity and exact maximum-cut formula, and independently checks the gcd count of distinct transition values for 361 rectangles. Execute with Python 3: `python verification/check_rook.py`. These finite computations are corroboration, not a replacement for the all-parameter proof above.

## Relationship to prior work

The antiferromagnetic Ising-to-maximum-cut reduction and polynomial-time solvability of maximum cuts on line graphs are previously established. Mohar and Poljak (1990, Section 4, Proposition 4.3) specifically prove exactness of the maximum-cut eigenvalue bound for line graphs of bipartite semiregular graphs with both class degrees even, a statement covering the zero-field even-by-even rook special case. The present zero-field formula is **not claimed as new** in that covered subfamily. The additional finite-field staircase, its exact gcd-controlled number of distinct transitions, simultaneous classification of all fixed-population ground states and parity-selected zero-field magnetization sectors are the specific claims here. Dyer and coauthors analyze the antiferromagnetic Ising partition function on general line graphs, a much broader computational setting, but their inspected theoretical objectives do not supply this explicit rectangular finite-field formula. The nearby model on line graphs of complete graphs in Betre and Lewis is not the line graph of a complete bipartite graph, so a balanced-degree argument there does not itself state the present two-degree-class formula. Krawczyk studies ground-state state-space structure on other frustrated geometries.

## Limitations

No claim is made about novelty of the generic Ising/cut equivalence, balanced-clique upper bounds, even-even maximum-cut special cases, or general polynomial-time algorithms on line graphs. Historical priority of the new **joint** all-field and gcd-classification statement remains subject to older literature that could employ different terminology or an unpublished degree-constrained-cut formulation. The Oxford institutional request for a full paper on line-graph maximum cuts could not be completed because the authorized connection was unavailable. This does not make an uninspected text a negative result. No positive-temperature, thermodynamic-limit or nonuniform-field generalization is asserted. This is a self-review, not an independent audit.

## References

1. M. J. Krawczyk, *Topology of space of periodic ground states in antiferromagnetic Ising and Potts models in selected spatial structures*, first publicly posted 2010-04-07, https://arxiv.org/abs/1004.1070.
2. B. Mohar and S. Poljak, *Eigenvalues and the max-cut problem*, Czechoslovak Mathematical Journal 40 (1990), 343–352, https://dml.cz/dmlcz/102386; also https://ieomsociety.org/ieom2019/papers/504.pdf for related discussion of exact graphs.
3. M. Dyer et al., *The Antiferromagnetic Ising Model on Line Graphs*, 2020, https://arxiv.org/abs/2005.07944; authorized open manuscript https://eprints.whiterose.ac.uk/id/eprint/162602/1/2005.07944.pdf.
4. V. Guruswami, *Maximum Cut on Line and Total Graphs*, Discrete Applied Mathematics (1999), https://doi.org/10.1016/S0166-218X(99)00056-6.
5. C. Arbib, *A Polynomial Characterization of Some Graph Partitioning Problems* (1988), https://doi.org/10.1016/0020-0190(88)90144-5.
6. K. H. Betre and N. Lewis, *Dynamical Quantum Multigraphs*, 2025, https://arxiv.org/abs/2509.08296.
