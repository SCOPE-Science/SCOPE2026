# Two-step stabilization and sharp five-site onset in normalized bipartite heat thresholding

## Finding

Let \(m,n\ge1\), and let \(P\) be the simple random-walk operator on the unweighted complete bipartite graph \(K_{m,n}\), acting on real-valued vertex functions. For every \(t>0\), define the binary heat-threshold map \(F_t:\{0,1\}^{m+n}\to\{0,1\}^{m+n}\) by applying \(H_t=e^{t(P-I)}\), then thresholding each coordinate at \(1/2\), retaining its previous binary value when the diffused value equals \(1/2\).

**Theorem.** For every \(m,n\ge1\) and \(t>0\),
\[
F_t^3=F_t^2.
\]
Thus all binary initial data are fixed after at most two applications, with no nontrivial periodic states. The upper bound two is sharp already on \(K_{2,3}\), whereas every complete bipartite graph with fewer than five vertices has \(F_t^2=F_t\) for every positive time.

There is also an exact first-step and hence full-orbit classification. For an initial state with \(k\) active vertices in the first part and \(\ell\) in the second, set \(\alpha=k/m\), \(\beta=\ell/n\), \(r=e^{-t}\), \(C=(1-r)^2/2\), and \(B=(1-r^2)/2\). If \(\alpha+\beta<1\), no zero becomes one; all active vertices in the first part simultaneously disappear exactly when \(r+C\alpha+B\beta<1/2\), and all active vertices in the second part simultaneously disappear exactly when \(r+C\beta+B\alpha<1/2\). If \(\alpha+\beta>1\), no one becomes zero; all inactive vertices in the first part simultaneously become one exactly when \(C\alpha+B\beta>1/2\), and all inactive vertices in the second part simultaneously become one exactly when \(C\beta+B\alpha>1/2\). At equality \(\alpha+\beta=1\), the entire state is fixed. Reapply these same explicit inequalities at most once for the final state.

For fixed \(0<\alpha+\beta<1\), every nonempty active part has a unique strictly positive critical diffusion time obtained by solving its displayed quadratic equality in \(r\in(0,1)\). The denser part has the smaller diffused value at each active site, hence loses its active vertices first as the diffusion time increases. The complementary statement holds above total density one: the sparser part fills first.

## Assumptions and scope

The graph has two nonempty parts of arbitrary integer sizes \(m,n\ge1\), all cross-edges of unit conductance, no within-part edges and no self-loops. The generator is the **degree-normalized random-walk** generator \(P-I\), not the combinatorial Laplacian. The heat time is any finite \(t>0\). The threshold uses values \(0\) and \(1\), the critical level \(1/2\), and explicit tie preservation. The theorem concerns the induced nonlinear binary map and its iterates, rather than a Lipschitz estimate for the linear heat operator.

## Proof

**1. Exact heat formula.** Write \(\bar x_A\) and \(\bar x_B\) for the averages over the first and second parts. Then \(Px\) takes values \(\bar x_B\) on the first part and \(\bar x_A\) on the second, while \(P^2x\) takes values \(\bar x_A\) and \(\bar x_B\), respectively. Hence \(P^3=P\). Expanding the exponential in even and odd powers gives
\[
 e^{t(P-I)}=rI+\frac{1-r^2}{2}P+\frac{(1-r)^2}{2}P^2,
 \qquad r=e^{-t}\in(0,1).
\]
For an initially active vertex in the first part, the diffused value is \(U_A^1=r+C\alpha+B\beta\), while for an inactive one it is \(U_A^0=C\alpha+B\beta\). Interchange \(\alpha,\beta\) for the second part. Therefore vertices of the same initial binary value in one part necessarily switch simultaneously, if at all.

**2. A strict mass dichotomy.** Put \(q=\alpha+\beta\). Since \(0<C<B<1/2\) for \(0<r<1\), if \(q<1\) then \(U_A^0,U_B^0\le Bq<1/2\); every initially zero vertex stays zero. Furthermore \(U_A^1\) and \(U_B^1\) are strictly increasing functions of \(r\). Indeed,
\[
\frac{dU_A^1}{dr}=1-\alpha+r(\alpha-\beta)>0,
\]
for \(q<1\) and \(0<r<1\), and similarly for the second part. They range from \(q/2<1/2\) at \(r=0\) to \(1\) at \(r=1\), giving unique critical roots for each nonempty active part. Their difference is
\[
 U_A^1-U_B^1=-r(1-r)(\alpha-\beta).
\]
Thus for unequal positive densities the denser part is erased first, at a smaller diffusion time.

The heat map preserves complements, since \(H_t\mathbf1=\mathbf1\). The tie-preserving threshold also commutes with complementation. Applying the preceding analysis to \(\mathbf1-x\), whose total part density is \(2-q\), proves the stated one-sided filling rule for \(q>1\). When \(q=1\), \(U_A^0,U_B^0\le B<1/2\). Directly, \(U_A^1=1-U_A^0(\mathbf1-x)>1/2\) and likewise in the other part; hence no vertex switches.

**3. Universal two-update bound.** If \(q<1\), every update can only erase originally active vertices, simultaneously in whole within-part active blocks. There are at most two such blocks. If the first update erases neither, it is fixed; if it erases both, it is all zero; if it erases exactly one, the next update either erases the remaining block or leaves it unchanged and fixed. Thus the second updated state is always fixed. Complementation gives the identical conclusion for \(q>1\), and \(q=1\) was handled above. This proves \(F_t^3=F_t^2\).

**4. Sharpness and smallest graph.** On \(K_{2,3}\), take one active vertex in each part and \(r=3/20\), equivalently \(t=\log(20/3)\). Thus \(\alpha=1/2\), \(\beta=1/3\), \(C=289/800\), and \(B=391/800\). The active values on the respective parts are
\[
 U_A^1=2369/4800<1/2,\qquad U_B^1=2471/4800>1/2.
\]
The first update therefore erases only the active vertex in the two-vertex part. The remaining active vertex has diffused value \(r+C/3=649/2400<1/2\) at the second update, and so disappears then. The first and second iterates are distinct, proving sharpness of the bound two.

For a star \(K_{1,n}\), its singleton part starts uniformly zero or uniformly one. In the former case only the opposite part can lose ones, and in the latter only the opposite part can gain ones; hence one update always suffices. The only biclique with both part sizes at least two and fewer than five vertices is \(K_{2,2}\). Its possible part densities are \(0,1/2,1\). If their sum is below one, both parts cannot contain active vertices; if above one, both parts cannot contain inactive vertices; at equality the state is fixed. Therefore \(F_t^2=F_t\) for all bicliques with at most four vertices.

## Verification

Run `python3 check_biclique_mbo.py` with Python 3 standard library. The checker independently evaluates \(H_t\) through the \(P\)-\(P^2\) representation and the part-density formula using exact rational values of \(r\). It checks all binary data on \(K_{m,n}\) for \(1\le m,n\le5\) and six rational heat parameters, all one-step count rules, and \(F_t^3=F_t^2\). It additionally excludes two-step behavior at a dense rational sample of times on all bicliques with at most four vertices and checks the exact five-site witness. These computations test the proof but do not substitute for its universal quantifiers.

## Relationship to prior work

The graph MBO framework and general finite convergence were studied by van Gennip, Guillen, Osting and Bertozzi. Their 2014 work discusses general pinning and trivialization bounds. A 2019 corrective sequel by van Gennip revisits the star example, explicitly corrects some earlier one-node change conditions, and treats star graphs and regular trees. Its inspected star results concern one-step membership changes, not the arbitrary-initial-state normalized-biclique two-update identity. The present proof is independent of the earlier one-node criteria. The early graph MBO algorithms of Merkurjev, Kostić and Bertozzi study segmentation and computational acceleration rather than this exact nonlinear iteration identity. Budd and van Gennip relate graph MBO to Allen–Cahn discretization and its convergence; this does not imply a two-step bound on the specified family. These comparisons distinguish the present nonlinear threshold-map statement from previously studied linear heat norms and other synchronous binary threshold rules.

## Limitations

No conclusion is made about combinatorial, symmetric, or signless Laplacian variants; weighted or incomplete bipartite graphs; nonbinary levels; thresholds other than \(1/2\); arbitrary finite graphs; or heat flows with fidelity forcing. The classification concerns a single fixed diffusion time reused at each iteration, not a varying-time schedule. This is an analytical result with exact finite corroborations; the available literature comparisons do not establish absolute historical priority.

## References

1. Y. van Gennip, N. Guillen, B. Osting and A. L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045 (first posted 28 June 2013); *Milan J. Math.* 82 (2014), 3–65, DOI: 10.1007/s00032-014-0216-8. In particular Sections 4.2–4.3 and 6.1–6.2.
2. E. Merkurjev, T. Kostić and A. L. Bertozzi, *An MBO scheme on graphs for classification and image processing*, *SIAM J. Imaging Sci.* 6 (2013), 1903–1930, DOI: 10.1137/120886935; open manuscript at https://www.math.ucla.edu/~bertozzi/papers/MKB12.pdf.
3. Y. van Gennip, *Graph MBO on Star Graphs and Regular Trees. With Corrections to DOI 10.1007/s00032-014-0216-8*, *Milan J. Math.* 87 (2019), 141–168, DOI: 10.1007/s00032-019-00296-1.
4. J. Budd and Y. van Gennip, *Graph MBO as a semi-discrete implicit Euler scheme for graph Allen–Cahn flow*, arXiv:1907.10774 (first posted 24 July 2019).
