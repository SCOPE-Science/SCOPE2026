# Five-vertex and distance-four positivity barriers for Padé \([0/2]\) graph diffusion

## Finding
Let \(G\) be a finite simple undirected unweighted graph, let \(L=D-A\) be its combinatorial Laplacian, and for every \(s\geq0\) define the second-order, L-stable Padé heat step
\[
R_G(s)=(I+sL+\tfrac12s^2L^2)^{-1}.
\]
Then the following statements hold.

1. **Sharp small-order classification.** If \(|V(G)|\leq5\), the matrix \(R_G(s)\) is entrywise nonnegative for all \(s\geq0\), except when \(G\) is the five-vertex path \(P_5\) and \(0<s<\sigma\). The threshold \(\sigma\) is the unique positive root of
   \[
   5\sigma^4+40\sigma^3+42\sigma^2-4=0,
   \qquad 0.27387026089<\sigma<0.27387026090.
   \]
   On \(P_5\), the update is entrywise nonnegative exactly for \(s=0\) or \(s\geq\sigma\).
2. **Distance-four obstruction for arbitrary order.** If a connected graph has diameter at least four, then some off-diagonal entry of \(R_G(s)\) is negative for every sufficiently small positive \(s\). More precisely, if the graph distance between distinct vertices \(i,j\) equals four, then
   \[
   (R_G(s))_{ij}=-\tfrac14 (L^4)_{ij}s^4+O_G(s^5),\qquad (L^4)_{ij}>0.
   \]
3. **Eventual recovery.** For every finite connected graph, there is a finite graph-dependent \(s_*\) such that \(R_G(s)\) is strictly entrywise positive for all \(s\geq s_*\). This last asymptotic property is included as context, not claimed to be new.

Thus the smallest simple undirected graph on which this L-stable method can lose positivity is \(P_5\); counterintuitively, its only positivity failure occurs for *small*, not large, positive steps. In every graph, \(R_G(s)\) is symmetric positive definite for finite \(s\), and \(R_G(s)\mathbf1=\mathbf1\). These spectral and row-sum properties do not imply entrywise nonnegativity.

## Assumptions and scope
Graphs are finite, simple, unweighted and undirected, with the standard nonnegative Laplacian \(L=D-A\). Multiple connected components are allowed in the five-vertex classification; the update acts block-diagonally, so cross-component entries remain zero. The timestep \(s\) is a nonnegative real number. The statement concerns the **one-step matrix** \(R_G(s)\), and therefore positivity for every nonnegative initial vector. It is not a statement about any nonlinear, multi-stage or fractional-PDE solver that merely uses the same scalar rational approximation.

## Proof
Set
\[
r(z)=\frac{1}{1+z+z^2/2}=1-z+\tfrac12z^2-\tfrac14z^4+O(z^5).
\]
The cubic coefficient vanishes. If \(d_G(i,j)=4\), all \((L^k)_{ij}\) with \(k<4\) vanish, because any nonzero term in such a matrix product requires at least four edge changes. For \(k=4\), only four consecutive off-diagonal factors can contribute. Every shortest four-edge walk contributes \((-1)^4=1\), and at least one exists. Consequently \((L^4)_{ij}>0\), and the series gives the displayed negative leading coefficient. Every graph of diameter at least four contains a pair at exactly distance four along a geodesic.

For the finite classification, write
\[
M_G(s)=2I+2sL+s^2L^2,\qquad R_G(s)=2M_G(s)^{-1}.
\]
Each eigenvalue of \(M_G(s)\) is \(2+2s\lambda+s^2\lambda^2>0\) for a Laplacian eigenvalue \(\lambda\geq0\). Hence \(\det M_G(s)>0\). Thus the signs of entries of \(R_G(s)\) are exactly the signs of the corresponding entries of \(\operatorname{adj}M_G(s)\).

The accompanying exact-integer verifier enumerates all \(2^{\binom n2}\) labeled simple graphs for each \(1\leq n\leq5\), retains the connected graphs, and reduces them to isomorphism classes by taking the lexicographically minimum adjacency-bit word over all vertex permutations. The class counts are respectively \(1,1,2,6,21\), with labeled connected-graph counts \(1,1,4,38,728\). No catalog of graph types is assumed. It evaluates all cofactor polynomials via permutation determinants, using integer polynomial arithmetic. Among the 31 connected classes and 644 cofactor entries, every coefficient is nonnegative except in the two symmetric end-to-end cofactor polynomials of the unique diameter-four graph \(P_5\). A nonzero cofactor with nonnegative coefficients is strictly positive for \(s>0\), and a zero cofactor is nonnegative. Exhaustiveness of the labeled enumeration and isomorphism invariance therefore prove the universal small-order assertion.

Numbering the path vertices consecutively, exact determinant elimination yields
\[
(R_{P_5}(s))_{1,5}=
\frac{s^4(5s^4+40s^3+42s^2-4)}
{(s^4+6s^3+18s^2+12s+4)
(25s^4+50s^3+50s^2+20s+4)}.
\]
The verifier independently checks this identity as an integer polynomial identity, together with the remaining cofactor signs. The denominator is positive for \(s\geq0\); the numerator's quartic factor is strictly increasing on \(s>0\), negative at zero and positive for large \(s\). This proves the existence, uniqueness and sharpness of \(\sigma\), including the boundary cases. The rational endpoints quoted above are certified by exact rational substitution into the quartic.

Finally, for connected \(G\) with \(n\) vertices, the real symmetric Laplacian has \(\ker L=\operatorname{span}\{\mathbf1\}\). The spectral theorem gives
\[
\lim_{s\to\infty}R_G(s)=\frac1n\mathbf1\mathbf1^\top.
\]
All limit entries are strictly positive, proving eventual positivity (without any assertion of a uniform bound over all graphs).

## Verification
Run `python3 verify_pade02.py` with Python 3 and the standard library. It reconstructs 31 unlabeled connected classes from the complete labeled search; checks 644 exact cofactor polynomials; confirms that \(P_5\) alone has the two exceptional end-to-end cofactors; verifies the complete exact rational identity above by cross-multiplication; and certifies the rational root interval. The proof of the infinite graph-diameter obstruction and eventual positivity is analytic and does not rely on finite enumeration.

## Relationship to prior work
Earlier work on time stepping and positivity of rational approximations includes Horváth (2005) and Wade–Khaliq–Siddique–Yousuf (first public 2004). The latter considers positivity-preserving Padé combinations for parabolic PDEs, but its complete text could not be inspected here; its abstract does not establish this specific classification and remains a priority caveat. Yousuf–Alshakhoury (2026) explicitly study the \([0/2]\) Padé factor in a Fourier-spectral epidemic diffusion scheme and discuss positivity, but the inspected full article does not give the all-graph five-vertex classification, the graph-distance-four expansion or the \(P_5\) threshold. That PDE discretization and its entire ETD update are not asserted to be identical to the isolated graph-heat matrix studied here. Itkin–Kazbek (2026) discuss eventual positivity of rational approximations on eventually positive generators, so the eventual-positivity observation is not advanced as original. Existing results for the *different* diagonal \([2/2]\) Padé map do not imply the conclusions for \([0/2]\): their scalar rational functions and matrix sign patterns differ.

## Limitations
The all-graph small-order classification is proved only for simple unweighted graphs with at most five vertices. The distance-four obstruction holds in arbitrary finite connected simple unweighted graphs but is not a converse: no assertion is made that all graphs of diameter at most three are unconditionally positive. The result does not cover independently weighted edges or directed Markov generators. The complete text of the particularly relevant 2004 Padé-smoothing study was unavailable, so a residual publication-priority risk remains. 

## References
1. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356. https://doi.org/10.1016/j.apnum.2004.08.026
2. B. A. Wade, A. Q. M. Khaliq, M. Siddique, and M. Yousuf, *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, Numerical Methods for Partial Differential Equations 21 (2005), 553–573; first published 2004-09-29. https://doi.org/10.1002/num.20039
3. M. Yousuf and N. Alshakhoury, *Stability analysis and numerical simulation of nonlocal extended epidemic models using positivity-preserving scheme*, Scientific Reports 16 (2026), 5964. https://doi.org/10.1038/s41598-026-36463-9
4. A. Itkin and R. Kazbek, *Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation* (2026). https://arxiv.org/abs/2608.22703
