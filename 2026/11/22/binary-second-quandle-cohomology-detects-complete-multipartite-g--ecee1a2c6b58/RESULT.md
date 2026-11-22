# Binary second quandle cohomology detects complete multipartite graph quandles

## Finding
Let \(G\) be a connected loopless simple graph on \(n\ge2\) vertices, and let \(A\) be its adjacency matrix over \(\mathbb F_2\). For the graph quandle \(Q_G=V(G)\times\mathbb F_2\), use the right action
\[
(i,a)\triangleright(j,b)=(i,a+A_{ij}).
\]
With trivial coefficients \(\mathbb F_2\) and normalized quandle cohomology,
\[
\dim_{\mathbb F_2}H_Q^2(Q_G;\mathbb F_2)
=n(n-1)+n\,\mathbf1_{\operatorname{rank}_{\mathbb F_2}(A)=2}.
\]
A connected simple graph has binary adjacency rank two precisely when it is complete bipartite or complete tripartite, with each part nonempty. Consequently \(\dim H_Q^2=n^2\) exactly for those graphs, and \(n(n-1)\) otherwise. In particular, this cohomological dimension detects a complete multipartite class not apparent from the quandle's cardinality.

## Assumptions and scope
The graph is finite, undirected, simple, connected and has at least two vertices. Its entries \(A_{ij}\) are in \(\mathbb F_2\). All cochains and dimensions are over the field \(\mathbb F_2\). For \(x,y,z\in Q_G\), a normalized \(2\)-cochain \(\phi:Q_G^2\to\mathbb F_2\) obeys \(\phi(x,x)=0\); it is a cocycle when
\[
\phi(x,y)+\phi(x\triangleright y,z)+\phi(x,z)+\phi(x\triangleright z,y\triangleright z)=0.
\]
This is the usual right-quandle cocycle condition, equivalent in characteristic two to Definition 4.8 of Furuki–Tamaru. A coboundary from \(f:Q_G\to\mathbb F_2\) is \(\delta f(x,y)=f(x\triangleright y)+f(x)\). We use \(H_Q^2=Z_Q^2/B_Q^2\), and not unnormalized rack cohomology.

## Proof
Write \(x=(i,a)\), \(y=(j,b)\) with \(a,b\in\mathbb F_2\). Every \(2\)-cochain has a unique expansion
\[
\phi((i,a),(j,b))=u_{ij}+a p_{ij}+b v_{ij}+ab w_{ij}.
\]
The normalization is \(u_{ii}=0\) and \(p_{ii}+v_{ii}+w_{ii}=0\). Substitute this expansion and the right action into the cocycle equation. Its coefficient of the third input's fiber coordinate is \(A_{ij}w_{ik}\); thus \(A_{ij}w_{ik}=0\) for every \(i,j,k\). Every vertex has a neighbor, so \(w_{ik}=0\) for every \(i,k\). The remaining equation is exactly
\[
A_{ij}p_{ik}+A_{ik}p_{ij}+A_{jk}v_{ij}=0
\quad(i,j,k\in V(G)).
\tag{1}
\]
There is no restriction on \(u_{ij}\) except \(u_{ii}=0\), giving \(n(n-1)\) independent parameters.

Fix \(i\). Interchanging \(j,k\) in (1) gives \(A_{jk}(v_{ij}+v_{ik})=0\). Hence \(v_{ij}=v_{ik}\) when \(jk\) is an edge; graph connectivity forces \(v_{ij}=t_i\) independent of \(j\). The condition \(p_{ii}=v_{ii}\) follows already from (1) with \(j=i\) and \(k\) adjacent to \(i\). Write \(\alpha=(A_{ij})_j\ne0\) and \(p=(p_{ij})_j\). Equation (1) becomes the alternating-matrix identity
\[
t_i A=\alpha p^{\mathsf T}+p\alpha^{\mathsf T}.
\tag{2}
\]
When \(t_i=0\), the identity \(\alpha p^{\mathsf T}+p\alpha^{\mathsf T}=0\) forces \(p=c_i\alpha\) for one binary scalar \(c_i\). When \(t_i=1\), (2) forces \(\operatorname{rank}(A)\le2\). Since \(A\ne0\) is alternating, its binary rank is positive and even, so this means rank two. Conversely, for rank-two alternating \(A\), choose any neighbor \(j_0\) of \(i\), and set \(p_j=A_{j_0j}\); because \(A_{ij_0}=1\), every rank-two alternating matrix satisfies \(A=\alpha p^{\mathsf T}+p\alpha^{\mathsf T}\). Thus for every row \(i\), the solution space in \((p_{ij},t_i)\) has dimension one when \(\operatorname{rank}A>2\), and dimension two when \(\operatorname{rank}A=2\). Distinct rows are independent. Accordingly,
\[
\dim Z_Q^2=n(n-1)+n+n\,\mathbf1_{\operatorname{rank}(A)=2}.
\]
For a \(1\)-cochain \(f\), write \(d_i=f(i,0)+f(i,1)\). Then
\[
\delta f((i,a),(j,b))=A_{ij}d_i.
\]
Since no row of \(A\) is zero, the \(n\) parameters \(d_i\) give independent coboundaries, hence \(\dim B_Q^2=n\). Subtraction proves the dimension formula.

Finally, if \(\operatorname{rank}_{\mathbb F_2}A=2\), there exist independent binary vectors \(r,s\) with \(A=rs^{\mathsf T}+sr^{\mathsf T}\). Label vertex \(i\) by the binary pair \((r_i,s_i)\). This label cannot be zero because the vertex is not isolated. Two vertices are adjacent exactly when their nonzero labels are distinct; there are precisely three possible nonzero labels. Hence \(G\) is complete multipartite with two or three nonempty parts. Conversely every complete bipartite or tripartite graph has a binary adjacency matrix of rank two. This gives the stated graph-theoretic characterization.

## Verification
A standalone Python 3 checker, `verify_graph_quandle_h2.py`, builds the normalized cocycle matrix directly from the ternary quandle identity and the coboundary matrix directly from \(\delta f\); it reduces both over \(\mathbb F_2\) without using (1) or (2). The program tests every connected labeled simple graph on two, three and four vertices, and representative paths, complete graphs, stars, cycles and multipartite graphs on five to seven vertices. It verifies 60 cochain systems. Among the 38 connected labeled four-vertex graphs, 13 have binary adjacency rank two and \(\dim H_Q^2=16\); the other 25 have rank four and \(\dim H_Q^2=12\). This finite test corroborates but does not replace the all-graph proof.

## Relationship to prior work
Furuki and Tamaru (2024), Theorem 1.3 and Definition 4.1, construct the graph quandle. Their §4.4 observes that adjacency itself is a \(2\)-cocycle **on the underlying trivial vertex quandle**. That is different from computing normalized \(H_Q^2\) of the expanded graph quandle \(Q_G\), which is the object here. Saito and Sugawara (2024) generalize this construction to weighted directed graphs and classify homogeneous abelian-inner quandles; their theorems do not compute the indicated mod-two cohomology dimension. García Iglesias and Vendramin (2015) develop an explicit formula for **indecomposable** quandles, whereas all \(Q_G\) with \(n\ge2\) are disconnected. Related work on graph-quandle retraction image ranks concerns a different endomorphism invariant and gives no cochain-rank calculation. Exact priority beyond the inspected sources has not been independently established.

## Limitations
The theorem requires connectedness and at least two vertices. It is specific to normalized degree-two quandle cohomology with trivial \(\mathbb F_2\) coefficients; it makes no claim about other degrees, integral torsion, arbitrary coefficient groups, or disconnected graphs. The algebraic proof establishes the dimension, not a canonical explicit basis of cohomology classes. Finite verification does not establish an infinite theorem on its own. Equivalent results might be implicit in more general disconnected-quandle cohomology descriptions not inspected.

## References
- K. Furuki and H. Tamaru, *Homogeneous quandles with abelian inner automorphism groups and vertex-transitive graphs*, arXiv:2403.06209, first public 2024-03-10, especially Definition 4.1 and §4.4, https://arxiv.org/abs/2403.06209.
- T. Saito and S. Sugawara, *Homogeneous quandles with abelian inner automorphism groups*, arXiv:2403.07383, first public 2024-03-12, https://arxiv.org/abs/2403.07383.
- A. García Iglesias and L. Vendramin, *An explicit description of the second cohomology group of a quandle*, arXiv:1512.01262, first public 2015-12-03, https://arxiv.org/abs/1512.01262.
