# The four-vertex path is the unique small unweighted amplifier of global DeGroot disagreement

## Finding
Consider the synchronous unweighted DeGroot neighbour-averaging rule on a finite connected simple undirected graph with no loops. For every such graph with at most three vertices, the global squared pairwise disagreement does not increase in one update. Of the six connected isomorphism classes on four vertices, only the four-vertex path \(P_4\) admits an increase. Its sharp, attainable one-step multiplicative amplification is
\[
\mathcal A(P_4)=\frac{3+\sqrt5}{4}=1.309016994\ldots.
\]
Of the 38 connected labeled four-vertex graphs, exactly 12 (all labelings of \(P_4\)) admit a strict one-step increase.

## Assumptions and scope
For \(n\ge2\), let \(G=(V,E)\) be a connected simple loopless undirected unweighted graph with \(V=\{0,\ldots,n-1\}\). Put \(d_i=\deg(i)\ge1\), and define \(P_{ij}=1/d_i\) when \(\{i,j\}\in E\), and \(P_{ij}=0\) otherwise; thus \(x'=Px\). Each opinion \(x_i\) lies in \([0,1]\) and all nodes update simultaneously. There is no inertia, self-weight, asynchronous updating, bias term, or external stubbornness. Define the global disagreement index
\[
\Gamma(x)=\sum_{0\le i<j<n}(x_i-x_j)^2,
\quad
\mathcal A(G)=\sup_{x\in[0,1]^n,\ \Gamma(x)>0}\frac{\Gamma(Px)}{\Gamma(x)}.
\]
For \(n=1\) the disagreement is identically zero; this degenerate case cannot show an increase. The theorem concerns one update only. It does not assert monotonicity at later times on graphs with more vertices, and does not refer to the edge-weighted network disagreement index.

## Proof
Put \(J=I-\mathbf 1\mathbf 1^{\mathsf T}/n\). The elementary pairwise-squares identity gives \(\Gamma(x)=n x^{\mathsf T}Jx\). As \(P\mathbf1=\mathbf1\), additive constants do not affect either index, and an arbitrary nonconstant real vector can be affinely rescaled into \([0,1]^n\) without changing the quotient. Thus \(\mathcal A(G)\) is exactly the largest generalized eigenvalue of \((P^{\mathsf T}JP,J)\) on the zero-sum subspace. With \(H=[e_0-e_{n-1},\ldots,e_{n-2}-e_{n-1}]\), this is the largest root of
\[
\det\big(H^{\mathsf T}P^{\mathsf T}JPH-\lambda H^{\mathsf T}H\big)=0.
\]
There is no loss of generality in taking a vertex labeling as in the list below: every connected unlabeled graph with at most four vertices is a representative on the list (this follows by distinguishing trees and graphs containing a cycle).

The complete exact generalized spectrum, together with each class's number of labeled graphs, is:

| Graph | Labeled count | Generalized eigenvalues | \(\mathcal A(G)\) |
|---|---:|---|---|
| \(K_2\) | 1 | \(1\) | \(1\) |
| \(P_3\) | 3 | \(0,1\) | \(1\) |
| \(K_3\) | 1 | \(1/4,1/4\) | \(1/4\) |
| \(P_4\) | 12 | \(1/4,(3-\sqrt5)/4,(3+\sqrt5)/4\) | \((3+\sqrt5)/4\) |
| \(K_{1,3}\) | 4 | \(0,0,1\) | \(1\) |
| \(C_4\) | 3 | \(0,0,1\) | \(1\) |
| Paw (triangle with a pendant vertex) | 12 | \(1/24,1/4,2/3\) | \(2/3\) |
| \(K_4\) minus one edge | 6 | \(0,1/9,4/9\) | \(4/9\) |
| \(K_4\) | 1 | \(1/9,1/9,1/9\) | \(1/9\) |

For an independent hand reduction of the only amplifying class, label the path \(0-1-2-3\). Reflection about its midpoint decomposes the zero-sum space into a one-dimensional symmetric space spanned by \((1,-1,-1,1)\) and a two-dimensional antisymmetric space of vectors \((u,v,-v,-u)\). The first has disagreement quotient \(1/4\). On the latter,
\[
\frac{\Gamma(Px)}{\Gamma(x)}
=\frac{u^2-2uv+5v^2}{4(u^2+v^2)},
\]
whose matrix is \(\frac14\begin{pmatrix}1&-1\\-1&5\end{pmatrix}\). Its eigenvalues are \((3\pm\sqrt5)/4\), proving the sharp maximum. The affine-rescaling argument ensures that an eigenvector attaining it may be taken in \([0,1]^4\).

There is also an elementary rational strict witness: choose \(x=(1/2,1,0,1/2)\), whence \(Px=(1,1/4,3/4,0)\). Directly, \(\Gamma(x)=2\) and \(\Gamma(Px)=5/2\), giving the strict increase \(5/4\). The table excludes strict increase on every other connected graph of size at most four. Exactly \(4!/2=12\) of the 38 connected labeled four-vertex graphs are paths, completing the classification.

## Verification
The dependency-free \(verify.py\) independently enumerates all \(2^{\binom n2}\) labeled simple graphs for \(n=2,3,4\), filters connectivity, canonicalizes by every permutation, reconstructs the rational DeGroot matrix, and checks the exact generalized characteristic polynomial for each of the 43 connected labeled graphs. It verifies all nine graph-class polynomial identities, the class counts, and the witness by exact \(\texttt{fractions.Fraction}\) arithmetic. Run from the directory containing the files with \(\texttt{python3 verify.py}\). The observed check completed successfully. The code is a finite reproducibility check; the argument above and the exact spectrum table prove the universal quantifiers for all opinion vectors.

## Relationship to prior work
DeGroot (1974) introduced iterative opinion averaging. Dandekar, Goel and Lee (arXiv:1209.5998v1, first public 26 September 2012), Sections 2–3 and Appendix B, define the edge-weighted network disagreement index and prove it does not increase under DeGroot updates. They explicitly note that assigning edge weights can make the different global disagreement index \(\Gamma\) increase (Section 3, immediately following Definition 3.1). Thus the existence of global-disagreement amplification **for weighted networks is already known and is not claimed here**. The new statement fixes the stricter natural class of unit-weight, loopless, connected graphs and identifies the smallest possible order, its unique isomorphism class, all four-vertex class factors and the sharp maximum. Bindel, Kleinberg and Oren (arXiv:1203.2973v1) study an intrinsic-opinion Friedkin–Johnsen process and its equilibrium social cost, not the one-step unanchored DeGroot global-disagreement quotient. Relevant exact statements from these sources were compared rather than titles alone.

## Limitations
The result is finite-order, \(n\le4\), and does not classify larger networks, weighted edges, self-confidence, directed links, asynchronous updating or later time steps. It is about a metric of global pairwise differences, not an assertion of lasting sociological polarization. Prior weighted-network amplification is already in the literature. A matching older unweighted four-node census not located in the inspected sources remains a historical-priority risk. No independent external scientific audit has been conducted.

## References
1. M. H. DeGroot, “Reaching a Consensus,” *Journal of the American Statistical Association* **69** (1974), 118–121, https://doi.org/10.1080/01621459.1974.10480137.
2. P. Dandekar, A. Goel and D. T. Lee, “Biased Assimilation, Homophily and the Dynamics of Polarization,” arXiv:1209.5998v1 (26 September 2012), https://arxiv.org/pdf/1209.5998, Sections 2–3, 6 and Appendix B; *PNAS* (2013), https://doi.org/10.1073/pnas.1217220110.
3. D. Bindel, J. Kleinberg and S. Oren, “How Bad is Forming Your Own Opinion?”, arXiv:1203.2973v1 (13 March 2012), https://arxiv.org/pdf/1203.2973.
