# Sharp five-taxon onset and a phase region for bimodal ultrametric phylogenetic-rarefaction variance

## Finding
For rooted ultrametric phylogenetic trees with strictly positive edge lengths, identical root-to-tip height, and uniform sampling of exactly \(k\) distinct leaves without replacement, the variance of rooted Faith phylogenetic diversity can have two distinct strict local maxima as \(k\) increases **if and only if at least five leaves are available** (existentially over trees). The sharp five-leaf example has its maxima at \(k=2\) and \(k=4\), with an intervening strict minimum at \(k=3\).

There is also an exact open parameter region for this phenomenon on the rooted five-leaf shape \(((1,2),(3,(4,5)))\). With common tip height normalized to one, denote by \(\alpha\) the depth of the ancestor of leaves 1 and 2, by \(\beta\) the depth of the ancestor of leaves 3, 4, and 5, and by \(\gamma\) the depth of the ancestor of leaves 4 and 5. The domain is \(0<\alpha<1\) and \(0<\beta<\gamma<1\). The variance has two strict local maxima precisely when both inequalities hold:
\[
-12\alpha^2+26\alpha\beta+16\alpha\gamma-9\beta^2+6\beta\gamma-12\gamma^2>0,
\]
\[
3\alpha^2+14\alpha\beta-14\alpha\gamma-9\beta^2-6\beta\gamma+3\gamma^2>0.
\]
The claim concerns the entire parameter region for this **specified** topology, not a classification of all five-tip topologies.

## Assumptions and scope
A rooted full binary tree has \(n\) distinctly labelled leaves, all edges of positive length, no root stem, and all root-to-leaf distances equal to the same positive height \(H\). Rooted phylogenetic diversity of a leaf subset \(S\) is the total length of the union of the root-to-leaf paths for leaves in \(S\), with the empty subset assigned zero. For each integer \(k\in\{0,\ldots,n\}\), choose \(S_k\) uniformly among all \(\binom nk\) subsets of size \(k\), and define \(V_k=\operatorname{Var}(\operatorname{PD}(S_k))\). A strict local maximum at \(k\) means \(V_k>V_{k-1}\) and \(V_k>V_{k+1}\), with \(1\le k\le n-1\). All variances are conditional on the fixed tree; there is no species-abundance distribution and no independent-extinction model.

## Proof
**Lower bound.** Ultrametricity makes the diversity of every one-leaf sample equal to \(H\), hence \(V_1=0\). Also \(V_0=V_n=0\), and all variances are nonnegative. Thus \(k=1\) is not a strict local maximum. Two distinct strict local maxima of a finite real sequence cannot be adjacent: at least one intervening index is required. When \(n\le4\), the remaining possible internal sample sizes \(2,\ldots,n-1\) contain at most two adjacent indices. Therefore two strict local maxima cannot occur on fewer than five leaves. This argument does not assume any particular rooted binary topology.

**Five-leaf construction and exact phase calculation.** Normalize \(H=1\) and use the rooted shape \(((1,2),(3,(4,5)))\). The eight edge lengths are: leaf 1 and leaf 2 pendant edges \(1-\alpha\); the stem subtending \(\{1,2\}\) has length \(\alpha\); leaf 3 has pendant length \(1-\beta\); the stem subtending \(\{3,4,5\}\) has length \(\beta\); the stem subtending \(\{4,5\}\) has length \(\gamma-\beta\); and the leaf 4 and leaf 5 pendant edges each have length \(1-\gamma\). The inequalities in the scope guarantee all eight lengths are strictly positive, and all root-to-tip distances are exactly one.

For any selected leaf set \(S\), write \(\mathbf1_E\) for the event indicator. Its rooted diversity is exactly
\[
\begin{aligned}
\operatorname{PD}(S)={}&(1-\alpha)|S\cap\{1,2\}|+(1-\beta)\mathbf1_{3\in S}
 +(1-\gamma)|S\cap\{4,5\}|\\
&+\alpha\mathbf1_{S\cap\{1,2\}\ne\varnothing}
+\beta\mathbf1_{S\cap\{3,4,5\}\ne\varnothing}
+(\gamma-\beta)\mathbf1_{S\cap\{4,5\}\ne\varnothing}.
\end{aligned}
\]
Enumerating each of the \(\binom5k\) equally likely subsets, subtracting its mean, and collecting coefficients gives \(V_0=V_1=V_5=0\) and the following exact quadratic polynomials:
\[
V_2=\frac{9\alpha^2-4\alpha\beta-2\alpha\gamma+16\beta^2-4\beta\gamma+9\gamma^2}{100},
\]
\[
V_3=\frac{21\alpha^2-30\alpha\beta-18\alpha\gamma+25\beta^2-10\beta\gamma+21\gamma^2}{100},
\]
\[
V_4=\frac{2(3\alpha^2-2\alpha\beta-4\alpha\gamma+2\beta^2-2\beta\gamma+3\gamma^2)}{25}.
\]
For five leaves with \(V_0=V_1=V_5=0\), two strict maxima can only occur at sample sizes 2 and 4. These occur exactly when \(V_2>V_3\) and \(V_4>V_3\). Subtraction of the displayed polynomials gives the two necessary-and-sufficient strict inequalities in the Finding section, each divided by the positive factor 100. Thus this is a complete phase criterion on the specified five-leaf shape, including all equality boundaries, where strictness fails.

At the rational parameter values
\[
(\alpha,\beta,\gamma)=\left(\frac{14}{15},\frac13,\frac25\right)
\]
all edge lengths are strictly positive and the variance sequence is exactly
\[
(V_0,V_1,V_2,V_3,V_4,V_5)=\left(0,0,\frac{32}{375},\frac{317}{4500},\frac{28}{375},0\right).
\]
Both differences are strictly positive: \(V_2-V_3=67/4500\) and \(V_4-V_3=19/4500\). This supplies the required five-leaf witness and finishes the sharp existence threshold. The strict inequalities also imply stability under sufficiently small perturbations of the three interior depths.

## Verification
Run `python3 check.py` using the Python 3 standard library. The checker constructs the eight actual edge-length vectors, enumerates all \(\binom5k\) labelled subsets for every \(k=0,\ldots,5\), and independently computes a symbolic covariance coefficient matrix for the three free interior depths. It compares all six symbolic variance coefficient vectors with the stated formulas, checks the rational witness and strict inequalities exactly, and repeats the direct-versus-polynomial calculation over 44 additional admissible rational parameter triples. Its result is `PASS` without numerical tolerances. No finite experiment is being used as a proof of a claim over arbitrary leaf counts: the global lower bound is combinatorial and the complete five-tip phase formula is a symbolic identity established by finite exhaustive subset expansion.

## Relationship to prior work
Nipperess and Matsen, *The mean and variance of phylogenetic diversity under rarefaction* (first public preprint 2012-08-31, arXiv:1208.6552; published 2013), derive the general edge-indicator covariance formula for rooted and unrooted phylogenetic rarefaction. Their general formula is explicitly acknowledged as the mathematical starting point, not claimed as new. The finding here concerns the earliest possible **non-unimodal variance profile on a strictly ultrametric tree** and a necessary-and-sufficient quadratic phase region for a natural five-tip topology. Their article's main formulas, examples and discussion do not explicitly give this two-maximum onset or these phase inequalities. Chao et al., *Rarefaction and extrapolation of phylogenetic diversity* (2014 first online), study sampling curves, extrapolation and estimator uncertainty, which are not the conditional finite-subset double-mode classification here. Nipperess's 2016 review chapter presents the rarefaction expectation and refers back to the 2013 work for variance. A general variance formula can, after selecting this tree and performing the requisite comparisons, reproduce the displayed instance; no independence from that framework is asserted.

## Limitations
The classification of the two-maxima phase is for the displayed five-tip topology only; other five-leaf topologies and the number of peaks in arbitrary large ultrametric trees are not classified. It concerns uniform leaf-subsampling without replacement, not abundance-weighted individual draws, bootstrap estimation error, or independent extinction. These exact mathematical results do not imply that two peaks typically occur in observed phylogenies. The structural five-tip threshold follows from a short combinatorial obstruction, and the five-tip positive part is an explicit exact calculation. Literature priority beyond the inspected sources remains unverified independently, and the general covariance formula makes the calculations accessible to other researchers.

## References
- Nipperess, D. A., and Matsen IV, F. A. (2012 preprint; 2013 journal). *The mean and variance of phylogenetic diversity under rarefaction*. arXiv:1208.6552v1 (2012-08-31), https://arxiv.org/abs/1208.6552 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3699894/ ; DOI:10.1111/2041-210X.12042.
- Chao, A., Chiu, C.-H., Hsieh, T. C., Davis, T., Nipperess, D. A., and Faith, D. P. (2014 online). *Rarefaction and extrapolation of phylogenetic diversity*. DOI:10.1111/2041-210X.12247, https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12247.
- Nipperess, D. A. (2016). *The Rarefaction of Phylogenetic Diversity: Formulation, Extension and Application*. DOI:10.1007/978-3-319-22461-9_10, https://link.springer.com/chapter/10.1007/978-3-319-22461-9_10.
