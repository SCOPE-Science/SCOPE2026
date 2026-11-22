# Rooted-subtree rigidity and a sharp \(3/2\) gap for finite Haar variation projections

## Finding
Let \(d\ge1\), \(n=2^d\), and let \(\mathcal D_d\) be the dyadic intervals \(I\subset\{0,\ldots,n-1\}\) of cardinality at least two. For each \(I\), write \(I_L,I_R\) for its equal left and right halves and define its normalized real Haar vector
\[
h_I=|I|^{-1/2}(\mathbf 1_{I_L}-\mathbf 1_{I_R}).
\]
For any subset \(\mathcal M\subseteq\mathcal D_d\), put
\[
P_{\mathcal M}x=\frac{\langle x,\mathbf 1\rangle}{n}\mathbf 1
 +\sum_{I\in\mathcal M}\langle x,h_I\rangle h_I,
\quad V(x)=\sum_{i=0}^{n-2}|x_{i+1}-x_i|,
\quad K(\mathcal M)=\sup_{V(x)>0}\frac{V(P_{\mathcal M}x)}{V(x)}.
\]
Call \(\mathcal M\) *ancestor-closed* when the parent of each nonroot \(I\in\mathcal M\) also belongs to \(\mathcal M\).

**Theorem.** For every \(d\ge1\), the complete total-variation contraction classification is
\[
\begin{array}{ll}
K(\mathcal M)=0,&\mathcal M=\varnothing,\\
K(\mathcal M)=1,&\varnothing\ne\mathcal M\text{ is ancestor-closed},\\
K(\mathcal M)\ge 3/2,&\mathcal M\text{ is not ancestor-closed}.
\end{array}
\]
The universal separation \(3/2\) is sharp for every \(d\ge2\): retaining precisely one child of the root gives \(K(\mathcal M)=3/2\). In particular, \(P_{\mathcal M}\) diminishes variation for all inputs if and only if its retained details are ancestor-closed. A single unit-jump input witnesses the lower bound for every non-ancestor-closed mask.

## Assumptions and scope
The nodes are an ordered finite real path, not a cycle; variation is the unweighted sum of interior adjacent differences, with no artificial exterior boundary jump. The mask is arbitrary but fixed independently of the input. The constant Haar coefficient is always retained. Haar vectors are orthonormal in the ordinary counting-measure Euclidean inner product. The word *sharp* refers to the greatest universal lower bound on the norm of a non-ancestor-closed mask, not a universal exact formula for each such mask.

## Proof
**1. Ancestor-closed masks are exactly dyadic block averaging.** Starting with the root interval, split each node \(I\) if and only if \(I\in\mathcal M\). Ancestor closure makes the final leaves a partition of the path into contiguous dyadic blocks. Splitting a leaf introduces exactly one independent Haar contrast; consequently, the span of the constant vector and the retained contrasts is exactly the space of vectors constant on each final block. Its Euclidean orthogonal projector \(P_{\mathcal M}\) replaces each block by its arithmetic mean.

**2. Their exact variation norm.** Let \(s^{(j)}\) be zero at indices below \(j\) and one at indices at least \(j\), for \(1\le j<n\). Each block average of this nondecreasing step is itself nondecreasing, lies between zero and one, and hence has variation at most one. Every real \(x\) has the decomposition
\[
x=x_0\mathbf1+\sum_{j=1}^{n-1}(x_j-x_{j-1})s^{(j)}.
\]
Linearity and the triangle inequality give \(V(P_{\mathcal M}x)\le V(x)\). If the mask is empty, the output is constant and the norm is zero. Otherwise at least two leaf blocks exist. Taking a step at a boundary between successive leaves leaves that step unchanged under block averaging and gives norm at least one. Thus the second case is exact.

**3. A missing parent costs at least one half.** Suppose \(\mathcal M\) is not ancestor-closed. There is a retained dyadic interval \(I\) whose immediate parent \(J\) is not retained. Set \(L=|I|\) and choose the unit step \(s\) jumping at the midpoint of \(I\). Its input variation is one and its coefficient at \(h_I\) is \(-\sqrt L/2\). Every retained Haar vector other than \(h_I\) that is not a strict ancestor of \(I\) has zero coefficient on this step: its support is disjoint from \(I\) or wholly inside one side of the jump. Because the parent \(J\) is absent, all remaining active ancestor vectors are constant throughout \(J\). The reconstructed values on \(J\) therefore equal a common baseline \(c\), with the additional values \(-1/2\) on \(I_L\), \(+1/2\) on \(I_R\), and zero on the sibling \(J\setminus I\). The jump between \(I_L\) and \(I_R\) has magnitude one, and the interface between \(I\) and its sibling has magnitude one half. These are distinct edges inside \(J\), so \(V(P_{\mathcal M}s)\ge3/2\). The argument applies even when other, more distant Haar coefficients are selected.

**4. Sharpness of the universal gap.** Assume \(d\ge2\) and retain only the left child \(I\) of the root. It has length \(L=n/2\), touches the left endpoint and has exactly one exterior interface. Thus \(V(h_I)=3/\sqrt L\). The step decomposition above shows that the maximum absolute coefficient \(|\langle x,h_I\rangle|/V(x)\), over nonconstant inputs, equals \(\sqrt L/2\), attained at the midpoint step. Since the constant projection has zero variation, \(K(\{I\})=(3/\sqrt L)(\sqrt L/2)=3/2\). This proves the sharp universal gap.

## Verification
The standalone checker `check_haar_tree_variation.py` uses integer arithmetic after multiplying each projected step-difference matrix by \(n\). It exhaustively verifies every Haar mask for depths one through four (respectively 2, 8, 128 and 32768 masks), checks the exact norm value for every ancestor-closed mask and the \(3/2\) lower bound for every other mask, and separately verifies single-child sharpness through depth nine. Run `python check_haar_tree_variation.py` with Python 3; no third-party library is required. These are finite checks of the calculations, while the four steps above establish the theorem for every depth.

## Relationship to prior work
Wavelet coefficient selection and total-variation regularization are historically linked: Durand and Froment (2003) replace thresholded coefficients through a total-variation minimization procedure; Steidl and collaborators (2003/2004) analyze multiscale shrinkage and total-variation diffusion. Bechler, DeVore, Kamont, Petrova and Wojtaszczyk (2006/2007) study the boundedness of greedy wavelet approximations in dimensions at least two and exhibit a one-dimensional failure of uniform greedy stability. Cartis and Thompson (2013) study exact Euclidean optimization over rooted wavelet trees. Cohen, DeVore, Petrushev and Xu (1999) show variation contractivity of certain dyadic averaging projectors in two dimensions.

The present one-dimensional result instead classifies **every fixed finite Haar coefficient mask** by exact contractivity versus a dimension-free norm gap. The known dyadic averaging observation accounts for the contractive half, not for the necessity of ancestor closure or the sharp \(3/2\) obstruction. Previous variation bounds for the unrestricted nonlinear Haar soft-threshold map describe the maximum over possible masks, not this structural classification of each mask. No claim of absolute historical priority is made.

## Limitations
No formula is asserted for the exact norm of each non-ancestor-closed mask beyond the lower bound. The theorem does not address non-Haar wavelets, weighted edge variation, cyclic paths, nonbinary partitions, multidimensional BV, or input-dependent nonlinear hard-threshold rules. Historical publication overlap may remain in less searchable signal-processing sources. Independent validation remains outstanding.

## References
1. S. Durand and J. Froment, *Reconstruction of Wavelet Coefficients Using Total Variation Minimization*, SIAM J. Sci. Comput. **24** (2003), 1754–1767, https://doi.org/10.1137/S1064827501397792. The author-distributed full text states electronic publication on April 15, 2003.
2. G. Steidl, J. Weickert, T. Brox, P. Mrázek and M. Welk, *On the Equivalence of Soft Wavelet Shrinkage, Total Variation Diffusion, Total Variation Regularization, and SIDEs*, Saarland University Preprint 94 (August 2003), https://www.mia.uni-saarland.de/Publications/steidl-pp94.pdf; SIAM J. Numer. Anal. **42** (2004), 686–713.
3. P. Bechler, R. DeVore, A. Kamont, G. Petrova and P. Wojtaszczyk, *Greedy Wavelet Projections Are Bounded on BV*, 2004 preprint, https://people.math.sc.edu/devore/publications/BV3.pdf; Trans. Amer. Math. Soc. **359** (2007), 619–635, https://doi.org/10.1090/S0002-9947-06-03903-1.
4. C. Cartis and A. Thompson, *An Exact Tree Projection Algorithm for Wavelets*, arXiv:1304.4570 (April 16, 2013), https://arxiv.org/abs/1304.4570.
5. A. Cohen, R. DeVore, P. Petrushev and H. Xu, *Nonlinear Approximation and the Space BV(\(\mathbb R^2\))*, Amer. J. Math. **121** (1999), 587–628, https://people.math.sc.edu/pencho/Publications/BV9707.pdf.
6. P. Wojtaszczyk, *Projections and Non-Linear Approximation in the Space BV(\(\mathbb R^d\))*, Proc. London Math. Soc. **87** (2003), 471–497, https://doi.org/10.1112/S0024611503014084 (full text not inspected).
