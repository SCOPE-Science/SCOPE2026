# Four vertices are the sharp positivity barrier for symmetrically filtered Euler graph heat steps

## Finding
Let \(L\) be the combinatorial Laplacian of a connected, undirected, simple unweighted graph. For \(h>0\) and \(s>0\) define the symmetrically filtered Euler heat step
\[
M_{h,s}=I-h(I+hsL/2)^{-1}L(I+hsL/2)^{-1}.
\]
For every connected graph with at most three vertices, \(M_{h,s}\) is entrywise nonnegative for all \(h\ge0\) whenever \(s\ge1/2\). On the four-vertex path \(P_4\), no positive \(s\) achieves this: for every \(s>0\), the transition from an endpoint to its neighbor becomes strictly negative when \(h>2\rho/s\), where \(\rho=3.71015054261934\ldots\) is the unique positive root of
\[
2z^3-6z^2-5z-1=0.
\]
Moreover, for \(s\ge1/2\), the **complete** entrywise-positivity range on \(P_4\) is exactly \(0\le h\le 2\rho/s\). For every nonempty graph, the same filtered Euler step is contractive in Euclidean norm at **all** positive step sizes if and only if \(s\ge1/4\). Thus the positive four-state diffusion operator demonstrates a sharp failure of a maximum-principle property even under unconditional energy stability, with arbitrarily strong splitting.

## Assumptions and scope
The graph Laplacian is \(L_{ii}=\deg(i)\), \(L_{ij}=-1\) for edges and zero otherwise. Graphs are finite, connected, undirected and unweighted. The filter is exactly \(J=(I+hsL/2)^{-1}\); the completed update is \(I-hJLJ\). Time is the dimensionless heat rate. The finite graph semidiscretization is \(\dot u=-Lu\), and the splitting operator is \(S=sL\), so the statement applies to the first-order symmetrically filtered explicit–implicit–null step in the cited construction, not to arbitrary filtered Runge–Kutta stages. A stochastic/Markov update means nonnegative entries with row sums one. At \(h=0\), the update is \(I\).

## Proof
Put \(z=hs/2\) and \(H_z=zL(I+zL)^{-2}\). Functional calculus gives
\[
M_{h,s}=I-\frac{2}{s}H_z,\qquad M_{h,s}\mathbf1=\mathbf1.
\]
For each nonnegative Laplacian eigenvalue \(\lambda\), the corresponding eigenvalue of \(H_z\) is \(z\lambda/(1+z\lambda)^2\), which belongs to \([0,1/4]\). Hence \(0\le(H_z)_{ii}\le1/4\) and all diagonal entries of \(M_{h,s}\) are nonnegative when \(s\ge1/2\). The largest attainable eigenvalue of \(H_z\) is \(1/4\) (choose \(z=1/\lambda\) for a positive eigenvalue). Consequently all \(M_{h,s}\) are Euclidean contractions for all \(h\) exactly when \(1-1/(2s)\ge-1\), equivalently \(s\ge1/4\).

For the connected unweighted graphs with at most three vertices, the only nontrivial types are \(P_2\), \(P_3\), and the triangle \(K_3\). Direct inversion yields the following *strictly negative* off-diagonal entries of \(H_z\), for every \(z>0\): on \(P_2\), \((H_z)_{12}=-z/(1+2z)^2\); on \(P_3\), the adjacent entries are \(-z/(1+3z)^2\) and the endpoints satisfy
\[
(H_z)_{13}=-\frac{2z^2(2z+1)}{(1+z)^2(1+3z)^2};
\]
on \(K_3\) all off-diagonal entries are \(-z/(1+3z)^2\). Thus their off-diagonal entries in \(M_{h,s}\) are positive for \(s>0\), and their diagonals are nonnegative for \(s\ge1/2\).

For the unit-rate four-vertex path, inversion of \(I+zL\) and multiplication give
\[
(H_z)_{12}=\frac{z(z+1)(2z^3-6z^2-5z-1)}{(2z+1)^2(2z^2+4z+1)^2}.
\]
The remaining distinct off-diagonal entries, up to reflection symmetry, are
\[
(H_z)_{13}=-\frac{z^2(6z^3+12z^2+9z+2)}{(2z+1)^2(2z^2+4z+1)^2},\qquad
(H_z)_{14}=-\frac{z^3(10z^2+12z+3)}{(2z+1)^2(2z^2+4z+1)^2},
\]
\[
(H_z)_{23}=-\frac{z(z+1)(2z^3+2z^2+3z+1)}{(2z+1)^2(2z^2+4z+1)^2}.
\]
All latter expressions are strictly negative for \(z>0\). The cubic \(2z^3-6z^2-5z-1\) has exactly one positive zero by Descartes' rule of signs and the intermediate value theorem; it is negative below and positive above this zero. Since \((M_{h,s})_{12}=-(2/s)(H_z)_{12}\), the endpoint-neighbor transition switches from positive to zero to negative at \(z=\rho\), independently of \(s\). All other off-diagonals remain positive. Diagonal nonnegativity for \(s\ge1/2\) completes the exact interval and the minimal-vertex assertion. The limit \(z(H_z)_{12}\to1/8\) confirms that the negative entry persists at arbitrarily large steps (and approaches zero from below). \(\square\)

## Verification
Run `python verify.py` (Python 3 and SymPy). It recomputes the rational matrix identities for all graphs named above and checks exact signs at rational parameters on both sides of \(\rho\). It verifies the formula for \(M_{h,s}\) and numerical values but is not a replacement for the analytic all-step proof.

## Relationship to prior work
The Wu–Shu source constructs the symmetrically filtered Euler scheme, proves its unconditional energy dissipation under a splitting bound, and develops higher-order variants. Its published construction gives the matrix formula used here but does not state this graph-topology-dependent sharp positivity boundary. Published graph diffusion analyses for Gauss, Radau, or Padé timesteppers involve different rational stability functions and do not imply the sign of the present resolvent-sandwich map. The negative entry occurs *despite* the source's \(L^2\) guarantee; it does not contradict energy stability. The close relationship to standard resolvent and spectral graph theory means that historical independent rediscovery remains possible.

## Limitations
The minimality assertion is for connected **simple unweighted** graphs and uniform splitting \(S=sL\). Weighted three-vertex graphs and unrelated numerical schemes are not classified. The exact full positivity interval on \(P_4\) is stated for \(s\ge1/2\); for smaller \(s\), diagonal failures may reduce the safe interval. The theorem concerns preservation of entrywise nonnegative semidiscrete heat states, not the local truncation error or accuracy of PDE spatial discretization.

## References
- Wu, Y. and Shu, C.-W., *Unconditionally \(L^2\)-stable explicit–implicit–null filtered Runge–Kutta methods for general nonlinear degenerate parabolic equations*, arXiv:2611.02282, first posted 2026-11-03, https://arxiv.org/abs/2611.02282. The filtered Euler construction is Section 3, Example 3.1; the second-order comparison is Section 4.
