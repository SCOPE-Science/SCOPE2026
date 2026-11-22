# Parity-controlled reversible-wave clocks on all finite generalized quadrangles

## Finding

Let \(\mathcal Q\) be any finite generalized quadrangle of order \((s,t)\), \(s,t\ge1\), with the convention that every line contains \(s+1\) points and every point lies on \(t+1\) lines. Let \(A\) be the zero-diagonal adjacency matrix of its point–line incidence graph, reduced over \(\mathbb F_2\). Over every field \(\mathbb F_Q\) of cardinality \(Q=2^f\), \(f\ge1\), consider the reversible linear update on ordered pairs of graph signals

\[
T(u,v)=(Au+v,u),\qquad u,v\in\mathbb F_Q^N,
\]

where \(N=|\mathcal P|+|\mathcal L|\). **The exact order of the global update permutation** is

\[
\operatorname{ord}(T)=\begin{cases}8,&s,t\text{ both odd},\\24,&\text{otherwise}.\end{cases}
\]

This holds for every existing generalized quadrangle, including nonclassical, unequal-order, and thin examples. More precisely, the following rank prescription determines every fixed-state count and therefore every primitive temporal-orbit population. All ranks below are over \(\mathbb F_2\), with the same values after extension to \(\mathbb F_Q\). Let \(I\) denote the \(N\)-dimensional identity, set \(E=A^4\), and define

\[
e=\operatorname{rank}(E),\quad c_2=\operatorname{rank}((A+I)E),\quad c_1=e-2c_2,
\]
\[
 d_j=\operatorname{rank}(A^j(I+E))\quad (j=0,1,2,3),
\]
\[
 b_1=d_0-2d_1+d_2,\quad b_2=d_1-2d_2+d_3,\quad b_3=d_2-2d_3,\quad b_4=d_3.
\]

These are nonnegative integers. For every positive integer \(k\), writing \(h=2^{\nu_2(k)}\), define

\[
D(k)=\sum_{j=1}^{4}b_j\min(2j,h)+\mathbf1_{3\mid k}\bigl(2c_1+2c_2\min(2,h)\bigr).
\]

Then

\[
|\operatorname{Fix}(T^k)|=Q^{D(k)},\qquad
\#\{\text{primitive orbits of length }k\}=
\frac1k\sum_{d\mid k}\mu(k/d)Q^{D(d)}.
\]

Only divisors of the stated exact global order can occur as least periods. The universal period is independent of incidence rank, while the exact number of cycles may distinguish geometries of the same order.

## Assumptions and scope

A finite generalized quadrangle means a nonempty point–line incidence structure in which any two points lie on at most one common line, any two lines meet at most once, every line has \(s+1\) points, every point has \(t+1\) incident lines, and for any point \(p\) not on a line \(\ell\) there is precisely one line through \(p\) meeting \(\ell\). We permit \(s=1\) or \(t=1\) and assume \(s,t\ge1\). This is purely a finite graph/linear update theorem; it does not assert existence of quadrangles for any arbitrary pair \((s,t)\).

The graph is bipartite with \(|\mathcal P|=(s+1)(st+1)\) and \(|\mathcal L|=(t+1)(st+1)\). Its adjacency is \(A=\begin{psmallmatrix}0&B\\B^{\mathsf T}&0\end{psmallmatrix}\), where \(B\) is the point-by-line incidence matrix. Field addition and subtraction coincide in characteristic two. Both signal rows are arbitrary. No randomness, graph regularity across the two shores, or Desarguesian hypothesis is assumed.

## Proof

**1. Incidence cubic identity.** Define \(H=\begin{psmallmatrix}0&J_{\mathcal P,\mathcal L}\\J_{\mathcal L,\mathcal P}&0\end{psmallmatrix}\). For a point \(p\) and line \(\ell\), the number of length-three walks from \(p\) to \(\ell\) is \(s+t+1\) if incident (\(t+1\) choices through \(p\) with the return via \(p\), and \(s\) other points of \(\ell\)); otherwise it is one, by the generalized-quadrangle axiom. Therefore the integral matrix identity, and hence its mod-two reduction, is

\[
 A^3=(s+t)A+H. \tag{1}
\]

Writing \(D=AH=HA=\operatorname{diag}((t+1)J_{\mathcal P},(s+1)J_{\mathcal L})\) and \(\delta=(s+t)\bmod2\), equation (1) gives \(A^4=\delta A^2+D\).

**2. Exact primary decomposition.** If \(s,t\) are odd, then \(\delta=0\), \(D=0\), so \(A^4=0\) whereas \(A^3=H\ne0\). Thus \(A\) is nilpotent of exact index four, \(E=0\), and has two size-four Jordan blocks (because \(\operatorname{rank}A^3=2\)).

If \(s,t\) are both even, \(\delta=0\), \(A^3=H\), and \(E=D=\operatorname{diag}(J_{\mathcal P},J_{\mathcal L})\). Both shore cardinalities are odd, so \(E^2=E\); its image consists of the two shore-constant vectors, and \(A\) acts there by swapping them. Moreover \(A^5=A^3\), \(A^2E=E\), and \(A^3(I+E)=0\). On \(\ker E\), \(A^2(I+E)\ne0\): a noncollinear pair of points has a zero off-diagonal entry in \(A^2\) and a one in \(E\). Hence the zero-primary component has a size-three Jordan block.

If \(s,t\) have opposite parity, then \(\delta=1\), precisely one diagonal block of \(D\) is a nonzero all-ones matrix, and \(AD=0\) (each off-diagonal product carries the factor \((s+1)(t+1)=0\) in \(\mathbb F_2\)). Hence \(A^5=A^3\), and \(E=A^4\) satisfies \(E^2=E\), \(A^2E=E\), \(A^3(I+E)=0\). Here \(E\ne0\): otherwise \(A^2=D\) would imply \(A^3=AD=0\), contradicting \(A^3=A+H\ne0\). Further, \(A^2(I+E)=D\ne0\). Thus the zero-primary component again has a size-three Jordan block, while the one-primary component is nonzero.

In all cases \(E\) is the projector onto the one-primary space, where \((A+I)^2=0\); its complementary space is the zero-primary space, with nilpotency index at most four. The displayed ranks reconstruct its zero-primary Jordan blocks \(J_j(0)\) with multiplicities \(b_j\), while the one-primary blocks \(J_1(1)\) and \(J_2(1)\) have multiplicities \(c_1,c_2\).

**3. Wave blocks and fixed spaces.** The wave is invertible, with \(T^{-1}(u,v)=(v,u+Av)\), and obeys \(T^2+I_{2N}=\widehat A T\), where \(\widehat A=\operatorname{diag}(A,A)\) commutes with \(T\). Restricted to a single spatial \(J_j(0)\) block, its characteristic polynomial is \((z+1)^{2j}\), and its fixed-vector dimension is one: \(T(u,v)=(u,v)\) forces \(u=v\in\ker J_j(0)\). Therefore this wave block is exactly one unipotent Jordan block \(J_{2j}(1)\). Its \(k\)-th fixed-space dimension is \(\min(2j,2^{\nu_2(k)})\).

On a spatial \(J_j(1)\) block, \(j=1,2\), one has \(T^2+T+I=\widehat{(A+I)}T\). Since \(z^2+z+1\) is separable over \(\mathbb F_2\), the temporal block has invariant factor \((z^2+z+1)^j\): over \(\mathbb F_4\), it consists of one Jordan block of size \(j\) at each primitive cubic root. Consequently its \(k\)-th fixed-space dimension is zero unless \(3\mid k\), and otherwise it equals \(2\min(j,2^{\nu_2(k)})\). Adding all block dimensions gives exactly \(D(k)\). Möbius inversion gives the displayed exact primitive-orbit formula.

**4. Sharp global orders.** In the odd-odd case the size-four spatial nilpotent block produces a temporal block of size eight, so the order is exactly eight. Otherwise the size-three zero-primary block produces a temporal block of size six and hence temporal order eight (the next power of two), while the nonzero one-primary space produces a temporal period divisible by three and dividing six. Their least common multiple is exactly twenty-four. This proves both branches without assuming a specific incidence realization.

## Verification

Two standalone Python 3 checkers accompany this result. `verify_symplectic_examples.py` independently constructs symplectic generalized quadrangles of orders \((2,2)\), \((3,3)\), and \((5,5)\) by enumerating totally isotropic projective lines, then compares graph-adjacency powers, the exact wave order, and all predicted fixed-space dimensions against direct bit-matrix ranks. `verify_grid_and_duads.py` uses a different, dense-binary-matrix implementation on the duad–syntheme geometry \(\operatorname{GQ}(2,2)\) and the thin rectangular geometries \(\operatorname{GQ}(2,1)\), \(\operatorname{GQ}(3,1)\). For example, the incidence graphs on 30, 80 and 312 vertices from the symplectic test have ranks \((\operatorname{rank}A,\operatorname{rank}A^2)=(20,10),(50,26),(182,92)\), respectively, and orders \(24,8,8\). The thin mixed-parity test verifies order \(24\) on 15 vertices. All finite checks are examples; the universal assertion follows from the preceding proof, not extrapolation.

Run with Python 3: `python3 verify_symplectic_examples.py` and `python3 verify_grid_and_duads.py`. Neither checker requires third-party packages.

## Relationship to prior work

Steeb and Hardy (2007), §2, discuss reversible second-order cellular automata obtained by retaining the preceding time layer; this establishes the generic reversible mechanism, not a generalized-quadrangle period law. Arrighi, Martiel and Perdrix (2015) develop general reversible graph dynamics at a different abstraction level. Godsil, Guo and Myklebust (2015), §2, examine quantum walks and line-intersection graphs of generalized quadrangles, not the binary incidence adjacency acting in the present reversible two-row rule. Existing characteristic-two reversible-wave classifications of strongly regular graphs concern collinearity/line-intersection graphs, not the bipartite point–line graph (the latter is generally not strongly regular). Likewise projective-plane incidence-wave classifications do not imply the generalized-quadrangle cubic identity (1) or its parity-based global clock. The known cycle-wave classification covers the isolated thin \(\operatorname{GQ}(1,1)\) instance, not the family. These distinctions concern statements and implications, not just titles.

## Limitations

Novelty is assessed against inspected relevant literature and accessible search results, not established as absolute historical priority. The fixed-count formulas are rank-parametric: they do not claim to determine the binary incidence rank of every nonisomorphic generalized quadrangle solely from \((s,t)\). The theorem does not cover odd-characteristic fields, asynchronous updates, nonlinear excitability rules, or hypothetical parameter pairs for which no finite generalized quadrangle exists. No independent external mathematical audit has been performed.

## References

1. W.-H. Steeb and Y. Hardy, *One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations*, Zeitschrift für Naturforschung A **62** (2007), 569–572, DOI: https://doi.org/10.1515/zna-2007-10-1103 (public print date 2007-11-01; §2 gives the second-order reversible construction).
2. P. Arrighi, S. Martiel, and S. Perdrix, *Reversible Causal Graph Dynamics*, arXiv:1502.04368v1, https://arxiv.org/abs/1502.04368 (first posted 2015-02-15).
3. C. Godsil, K. Guo, and T. G. J. Myklebust, *Quantum Walks on Generalized Quadrangles*, arXiv:1511.01962v1, https://arxiv.org/abs/1511.01962 (first posted 2015-11-06).
