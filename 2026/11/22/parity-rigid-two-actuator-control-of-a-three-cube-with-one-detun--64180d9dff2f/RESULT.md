# Parity-rigid two-actuator control of a three-cube with one detuned edge

## Finding

Let the eight vertices of the Boolean cube be binary triples \(x=(x_1,x_2,x_3)\in\{0,1\}^3\). Give the edge \(000\leftrightarrow100\) positive conductance \(t\), and each of the other eleven edges unit conductance. Let \(L(t)\) denote its weighted combinatorial Laplacian. For \(S\subseteq\{0,1\}^3\), put \(B_S=[e_x:x\in S]\) and consider the linear controlled diffusion equation \(\dot z=-L(t)z+B_Su\).

**Theorem.** For every real \(t>0\) with \(t\ne1\), two distinct vertices \(x,y\) provide complete controllability if and only if
\[
 x_2\oplus x_3\ne y_2\oplus y_3.
\]
Here \(\oplus\) denotes binary exclusive-or. Exactly sixteen of the twenty-eight unordered two-vertex sets satisfy the criterion; they are the same sixteen for every positive nonunit \(t\). No single vertex controls the system. Thus the minimum number of independently driven vertices is two for \(t\ne1\), whereas it is three for \(t=1\). At \(t=1\), the three-vertex set \(\{000,100,010\}\) is controllable.

## Assumptions and scope

The edge weights are fixed throughout each experiment; only one edge is detuned. Each chosen vertex receives its own independent scalar input. Controllability means the standard continuous-time, full eight-dimensional Kalman notion over \(\mathbb R\), equivalently the Popov–Belevitch–Hautus (PBH) criterion. In integer labeling \(v=x_1+2x_2+4x_3\), the two parity classes are \(\{0,1,6,7\}\) and \(\{2,3,4,5\}\); an admissible pair contains one vertex from each class. The theorem does not assert anything at zero or negative conductance, nor for independently detuned additional edges.

## Proof

**1. Exact invariant spectral subspaces.** Write \(z_j(x)=(-1)^{x_j}\) and \(\chi_I(x)=\prod_{j\in I}z_j(x)\). For the unweighted cube, the Walsh character \(\chi_I\) has Laplacian eigenvalue \(2|I|\). Put \(b=e_{000}-e_{100}\), so that
\[
L(t)=L(1)+(t-1)bb^{\mathsf T}.
\]
The vector \(b\) is orthogonal to the constant character and to every character omitting coordinate \(1\). Within each of the original eigenvalue levels \(2,4,6\), its projection is nonzero. Thus the following eigenvectors survive at fixed eigenvalues: \(z_2,z_3\) at \(2\), and \(z_1(z_2-z_3),z_2z_3\) at \(4\); the constants remain at zero. The orthogonal complement of these five fixed vectors is
\[
\mathcal A=\operatorname{span}\bigl\{z_1,\ z_1(z_2+z_3),\ z_1z_2z_3\bigr\}.
\]
In an orthonormal Walsh basis of \(\mathcal A\), the restriction of \(L(t)\) is
\[
D+(t-1)rr^{\mathsf T},\qquad
D=\operatorname{diag}(2,4,6),\quad
r=(1/\sqrt2,1,1/\sqrt2)^{\mathsf T}.
\]
Its characteristic polynomial is
\[
Q_t(\lambda)=\lambda^3-(2t+10)\lambda^2+(16t+28)\lambda-(28t+20),
\]
so that
\[
\det(\lambda I-L(t))=\lambda(\lambda-2)^2(\lambda-4)^2Q_t(\lambda).
\]
This identity follows directly by the determinant lemma. Since all coordinates of \(r\) are nonzero and the diagonal entries of \(D\) are distinct, for \(t\ne1\) the secular equation of this symmetric rank-one perturbation has three distinct real roots, none coinciding with \(2,4,6\). In particular, the cubic values at these three levels are \(-4(t-1),4(t-1),-4(t-1)\), respectively; none of its roots can be zero since \(t>0\) gives a connected weighted graph. Each eigenvalue on \(\mathcal A\) therefore has multiplicity one, and the other two nonzero eigenspaces have dimension exactly two.

**2. Necessity of the parity rule.** For a real symmetric state matrix, PBH controllability is equivalent to the coordinate-evaluation map on each eigenspace having full column rank. On the \(2\)-eigenspace \(\operatorname{span}\{z_2,z_3\}\), the two-coordinate evaluation determinant for \(x,y\) is nonzero exactly when \(z_2(x)z_3(x)\ne z_2(y)z_3(y)\), i.e. the two parities differ. Any singleton also fails here. Thus the parity condition is necessary, and at least two sites are required.

**3. Sufficiency at every \(t>0\), \(t\ne1\).** Suppose \(x,y\) have opposite parities. On the fixed \(4\)-eigenspace \(\operatorname{span}\{z_1(z_2-z_3),z_2z_3\}\), the row associated with the even-parity site has first component zero and second component \(1\), whereas the odd-parity site has nonzero first component and second component \(-1\). Therefore the two evaluations have rank two. The constant eigenvector is visible at either site.

It remains to rule out an eigenvector in \(\mathcal A\) vanishing at both sites. Every vector in \(\mathcal A\) has the form
\[
f=z_1\bigl(a+b(z_2+z_3)+c z_2z_3\bigr).
\]
At the odd-parity site, \(z_2=-z_3\) forces \(a=c\). At the even-parity site, let \(z_2=z_3=s\in\{-1,1\}\); vanishing there additionally forces \(b=-sa\). Hence a nonzero such \(f\) is proportional to
\[
z_1(z_2-s)(z_3-s),
\]
which is supported on precisely the two vertices with \(z_2=z_3=-s\), and is zero everywhere else. A vertex obtained from either support vertex by flipping coordinate \(2\) has value zero but is joined by a unit-weight edge to exactly one support vertex. Consequently \((L(t)f)\) is nonzero at that zero-value vertex for every real \(t\), contradicting the eigenvector equation. Thus no nonzero eigenvector in \(\mathcal A\) vanishes at both selected sites. Together with Step 1 and the PBH criterion, this proves full controllability for every admissible pair.

**4. The homogeneous case.** At \(t=1\) the eigenspaces at eigenvalues \(2\) and \(4\) both have dimension three, so two coordinate inputs can never give full rank there. Three inputs at \(000,100,010\) suffice: their evaluation matrices on the Walsh bases \((z_1,z_2,z_3)\) and \((z_1z_2,z_1z_3,z_2z_3)\) both have nonzero determinants of absolute value four. The constant and \(z_1z_2z_3\) modes are also visible. Hence the minimum is three at \(t=1\), completing the proof.

## Verification

Run `python3 verify.py` using Python 3 with the standard library. It constructs the exact rational weighted Laplacian, builds the eight-block Kalman matrix for each of the twenty-eight pairs, and uses rational Gaussian elimination. It checks nine positive nonunit values \(t=1/7,1/4,1/2,2/3,3/2,2,3,7,11\), totaling 252 exact pair-rank comparisons, and confirms that at the homogeneous parameter no pair is full rank whereas \(\{000,100,010\}\) is. The script asserts sixteen rank-eight pairs with precisely the stated parity condition at each nonunit test value. These tests are supplementary; the preceding argument proves the universal real-parameter statement.

## Relationship to prior work

Zhang, Camlibel and Cao (2011) study controllability through graph partitions, notably for distance-regular graphs, and derive necessary and sufficient conditions for multiple leaders; the detuned cube here is not distance regular and their work does not supply its all-weight coordinate-pair classification. Yuan and collaborators (2013) relate the unrestricted minimum input count to the largest eigenvalue multiplicity, but that result alone does not classify which two *coordinate* input sites work for the detuned cube. Monshizadeh, Zhang and Camlibel (2014) characterize strong graph-family controllability using zero forcing, which is a different quantifier from controllability of this fixed one-edge-weight family. Yazıcıoğlu, Abbas and Egerstedt (2016) obtain graph-distance-based lower bounds valid for every edge weighting; such an all-weight lower bound cannot imply full two-site rank in this example, since exactly the same graph with uniform weights fails for every pair. Existing results on unweighted hypercube actuator selections already cover the homogeneous lower bound as a separate special case; originality is sought only for the weight-dependent reduction and its exact parity placement law.

## Limitations

The theorem is a complete result for the eight-state cube with one perturbed edge; it is not an all-dimensional hypercube placement theorem and does not cover multiple edge perturbations, simultaneous shared inputs, actuator energy, or noise robustness. Because controllability is an exact-rank property, it does not imply good conditioning or low control energy; the controllability Gramian can become ill-conditioned as \(t\to1\). The proof is exact but has not been independently mathematically audited. Prior-art searches and inspected primary sources did not identify a covering statement, yet a differently formulated or unindexed weighted-graph controllability theorem might establish the same conclusion, so publication priority remains provisional.

## References

1. S. Zhang, M. K. Camlibel and M. Cao, “Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies,” *50th IEEE CDC-ECC*, pp. 759–764 (2011), DOI: 10.1109/CDC.2011.6160658. Open copy: https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, “Exact controllability of complex networks,” *Nature Communications* **4**, 2447 (2013), DOI: 10.1038/ncomms3447. https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/
3. N. Monshizadeh, S. Zhang and M. K. Camlibel, “Zero forcing sets and controllability of dynamical systems defined on graphs,” arXiv:1403.4868, first submitted March 19, 2014. https://arxiv.org/abs/1403.4868
4. A. Y. Yazıcıoğlu, W. Abbas and M. Egerstedt, “Graph Distances and Controllability of Networks,” *IEEE Transactions on Automatic Control* (2016), DOI: 10.1109/TAC.2016.2546180.
