# A topological Fourier floor for uniform spanning trees of squared cycles

## Finding

Let \(G_n=C_n^2\), the graph on \(\mathbb Z/n\mathbb Z\) with edges \(\{i,i+1\}\) and \(\{i,i+2\}\), for each integer \(n\ge5\). Choose a spanning tree uniformly, and let \(X_{a,i}\in\{0,1\}\) indicate inclusion of the edge \(\{i,i+a\}\), where \(a\in\{1,2\}\). Write \(\Sigma_n=\operatorname{Cov}(X)\) in the order of its two edge-length channels, and define its intrinsic squared Fourier condition ratio \(\kappa_n=\lambda_{\max}(\Sigma_n)/\lambda_{\min}^{+}(\Sigma_n)\).

**Theorem.** The covariance is a two-channel block-circulant matrix with exactly one null direction, the all-edge vector. Its entire finite spectrum is computable from the explicit geometric Green function below. Put
\[
 t=\frac{3-\sqrt5}{2},\quad s=t^2,\quad \alpha=\frac1{\sqrt5},\quad x(\theta)=|\cos(\theta/2)|,
\]
\[
 D(x)=(1+s)^2-4sx^2,\quad \beta=\frac{1-s^2}{5},\quad \gamma=\frac{2(1-t)^2(1-s)}5.
\]
The two Fourier covariance bands converge uniformly, in the sense specified in the proof, to
\[
 E_\pm(\theta)=\alpha-\frac{\beta\mp\gamma x(\theta)}{D(x(\theta))}.
\]
The positive edge of the limiting spectrum and the finite-size smallest positive eigenvalue satisfy
\[
 \lim_{n\to\infty}\lambda_{\max}(\Sigma_n)=\frac4{5\sqrt5},\qquad
 \lim_{n\to\infty}n\lambda_{\min}^{+}(\Sigma_n)=\frac12.
\]
Consequently the **sharp intrinsic conditioning law** is
\[
 \boxed{\lim_{n\to\infty}\frac{\kappa_n}{n}=\frac8{5\sqrt5}.}
\]
The limiting lower band itself vanishes quadratically at zero frequency; the positive \(1/(2n)\) finite-cycle floor instead comes from deletion of the constant Laplacian mode. The theorem does not assert that a particular nonzero finite frequency is an exact extremizer for every \(n\).

## Assumptions and scope

All edges have unit conductance; the graph is simple and \(n\ge5\). Eigenvalues of the covariance are unnormalized Euclidean eigenvalues (no division by \(n\)); Fourier blocks use a unitary discrete transform in the spatial index. The only removed zero eigenvalue is the deterministic total-edge-count constraint. Limits are along all integer cycle lengths, without a parity restriction. The first-public date in the metadata identifies the 2019 weighted-tree enumeration work motivating the determinant method, not the date of this theorem or the date of earlier graph enumeration.

## Proof

**1. Determinantal covariance, including its normalization.** Orient each edge from \(i\) to \(i+a\), let \(B\) be the oriented vertex-edge incidence matrix, and set \(L=BB^*\). The weighted matrix-tree identity, differentiated once and twice in independent edge conductances, gives the transfer-current kernel \(K=B^*L^+B\). For distinct edges \(e,f\),
\[
 \Pr(e\in T)=K_{ee},\quad \Pr(e,f\in T)=K_{ee}K_{ff}-K_{ef}^2,
\]
so \(\operatorname{Cov}(X_e,X_f)=\mathbf1_{e=f}K_{ee}-K_{ef}^2\). These equations may also be recovered from a second logarithmic derivative of a reduced Laplacian determinant, without assuming an infinite-volume limit.

The Laplacian Fourier multiplier at \(\theta\ne0\) is
\[
 \ell(\theta)=4-2\cos\theta-2\cos(2\theta)
 =2(1-\cos\theta)(3+2\cos\theta).
\]
For the two edge channels the current multiplier is, for nonzero Fourier frequencies,
\[
 P(\theta)=\frac1{3+2\cos\theta}
 \begin{pmatrix}1&1+e^{i\theta}\\1+e^{-i\theta}&2(1+\cos\theta)\end{pmatrix}.
\]
At the *discrete zero frequency* the current multiplier is zero, not its continuous limit \(P_0=\frac15\begin{psmallmatrix}1&2\\2&4\end{psmallmatrix}\). This distinction drives the conclusion.

**2. Exact finite Fourier spectrum.** Let \(\rho=-t\). For residues \(r\in\{0,\ldots,n-1\}\), put
\[
 g_n(r)=\frac{\rho^r+\rho^{n-r}}{\sqrt5(1-\rho^n)},
\]
and extend periodically. For two edges of channel types \(a,b\) with initial vertices separated by \(r\), the current coefficients are
\[
 \begin{aligned}
 k_{11}(r)&=g_n(r)-\frac1{5n},\\
 k_{12}(r)&=g_n(r)+g_n(r+1)-\frac2{5n},\\
 k_{21}(r)&=g_n(r)+g_n(r-1)-\frac2{5n},\\
 k_{22}(r)&=2g_n(r)+g_n(r-1)+g_n(r+1)-\frac4{5n}.
 \end{aligned}
\]
This follows by summing the geometric Fourier series of \((3+2\cos\theta)^{-1}\) over residues and deleting the zero Fourier multiplier. Define \(p_a=k_{aa}(0)\). For every \(j\in\{0,\ldots,n-1\}\), the exact \(2\times2\) Hermitian covariance Fourier block is
\[
 C_n(j)_{ab}=\mathbf1_{a=b}p_a-
 \sum_{r=0}^{n-1}k_{ab}(r)^2e^{-2\pi ijr/n}.
\]
The eigenvalues of these \(n\) blocks are precisely all \(2n\) eigenvalues of \(\Sigma_n\). In particular, this is an explicit finite formula, not an asymptotic ansatz. Its consistency with the exact tree count and pair correlations is checked in the accompanying code.

**3. Exact nullspace.** A spanning tree has exactly \(n-1\) edges, so the all-edge vector is null. Conversely suppose an edge weighting has constant sum over all spanning trees. For any three edges in a triangle, two distinct spanning trees can be obtained by exchanging one selected triangle edge for another, with all other selected edges identical: extend the two-edge path in the triangle to a spanning tree, then exchange the omitted triangle edge with either selected edge. Thus weights on triangle edges agree. The triangles \(\{i,i+1,i+2\}\) propagate equality through both edge types around the graph, so every edge weight agrees. Therefore \(\ker\Sigma_n\) is exactly one-dimensional, and all other eigenvalues are strictly positive.

**4. Limiting spectrum and geometric control.** Let \(g(r)=\alpha\rho^{|r|}\) on the integer lattice. Its Fourier transform is \((3+2\cos\theta)^{-1}\). The infinite current kernels have \(k_{11}(r)=g(r)\), \(k_{22}(0)=1-\alpha\), \(k_{22}(r)=-g(r)\) for nonzero \(r\), and \(k_{12}(r)=g(r)+g(r+1)\). Summing their squared Fourier series gives equal diagonal covariance symbols
\[
 h(\theta)=\alpha-\frac{1-s^2}{5(1-2s\cos\theta+s^2)}
\]
and off-diagonal magnitude
\[
 |b(\theta)|=\frac{2(1-t)^2(1-s)|\cos(\theta/2)|}{5(1-2s\cos\theta+s^2)}.
\]
Because \(1-2s\cos\theta+s^2=D(x(\theta))\), the two eigenvalues are \(E_\pm\). The periodized Green kernel differs from its integer-lattice counterpart only by exponentially small tails, uniformly after the squared-kernel Fourier summation.

Since \(\beta=3\gamma/2\), write \(x=|\cos(\theta/2)|\in[0,1]\):
\[
 E_+(x)=\alpha-\frac{\gamma(3/2-x)}{(1+s)^2-4sx^2},\quad
 E_-(x)=\alpha-\frac{\gamma(3/2+x)}{(1+s)^2-4sx^2}.
\]
The derivative of \(E_+\) with respect to \(x\) is a positive multiple of \((1+s)^2+4sx^2-12sx\). This quadratic decreases on \([0,1]\) and at \(x=1\) equals \(s>0\). The derivative of \(E_-\) is negative. Thus the upper branch reaches its strict maximum at \(x=1\) and the lower branch its unique zero there. Direct substitution yields \(E_+(1)=4/(5\sqrt5)\). The lower branch satisfies \(E_-(\theta)>0\) for nonzero \(\theta\) modulo \(2\pi\), and \(E_-(\theta)=O(\theta^2)\) near zero.

**5. The finite-size topological floor.** Let \(\theta_j=2\pi j/n\) and let \(\circ\) denote entrywise matrix multiplication. At every \(j\ne0\), subtracting \(P_0/n\) from the periodized current kernel, expanding its square, and bounding the exponentially decaying alias tails yields *uniformly in nonzero* \(j\)
\[
 C_n(j)=E(\theta_j)+\frac1n\Delta(\theta_j)+O(nt^n),
\]
where \(E\) is the Hermitian matrix with the limiting bands and
\[
 \Delta(\theta)=-\operatorname{diag}(1/5,4/5)+2P_0\circ P(\theta).
\]
The error is a matrix operator-norm error with a constant independent of \(n,j\). At zero frequency, this formula requires a further constant-square term; it is *not* valid there. Since
\[
 \Delta(0)=\frac1{25}\begin{pmatrix}-3&8\\8&12\end{pmatrix},
 \qquad u=\frac1{\sqrt2}(1,1)^T,
 \qquad u^*\Delta(0)u=\frac12,
\]
and \(u\) spans the zero eigenspace of \(E(0)\), standard two-by-two simple-eigenvalue perturbation gives, whenever a sequence of nonzero discrete frequencies tends to zero,
\[
 \lambda_-(C_n(j))=E_-(\theta_j)+\frac1{2n}+o(1/n).
\]
Here the little-o is uniform over such sequences; the opposite band has a positive gap at zero. Taking \(j=1\), \(E_-(2\pi/n)=O(n^{-2})\), hence \(\limsup n\lambda_{\min}^{+}\le1/2\). For the reverse inequality, any sequence of spectral minimizers must have frequency tending to zero (the limiting lower band is bounded away from zero outside any fixed neighborhood of zero); there the preceding expansion and \(E_-\ge0\) give \(\liminf n\lambda_{\min}^{+}\ge1/2\). The positive zero-frequency eigenvalue stays bounded away from zero by the nullspace result and the limiting upper-band value. Therefore \(n\lambda_{\min}^{+}\to1/2\).

Finally, uniform convergence of the finite block spectra to \(E_\pm\), including the zero block, yields \(\lambda_{\max}\to4/(5\sqrt5)\), and division proves the claimed condition-ratio limit.

## Verification

The included `check_square_cycle.py` uses exact rational Gaussian elimination to invert grounded graph Laplacians, enumerates every spanning tree for \(n=5,6,7\), and checks each one-edge and two-edge probability against the determinantal formula. It independently checks all current entries against the closed geometric Green function, plus asymptotic finite-size spectra at nine larger cycle lengths. The checks are finite corroboration; the proofs of the all-length nullspace and sharp asymptotic coefficients are analytical above. Reproduce with `python3 check_square_cycle.py` using Python's standard library.

## Relationship to prior work

Kirchhoff's weighted matrix-tree theorem and the transfer-current identity supply the determinant and determinantal foundations; these are not new. Baron, Prodinger, Tichy, Boesch and Wang counted the spanning trees of exactly this graph in 1985, obtaining \(nF_n^2\) and its circulant Laplacian. Klee and Stamps (first public preprint February 27, 2019) develop weighted Laplacian determinant methods in other graph families. The present claim concerns the *edge-occupation two-channel Fourier covariance* and in particular the positive finite-circle spectral floor \(1/(2n)\), whose first-order term arises from the missing zero current mode. Neither the counting theorem nor a general transfer-current identity gives this sharp conditioning law without the additional Fourier and small-frequency analysis here. Some related work studies covariance on wheels, circular ladders, and complete multipartite graphs, rather than squared cycles.

## Limitations

This is a same-authority analytical and computational verification, not independent mathematical validation. The novelty assessment is provisional: an equivalent treatment of transfer-current structure factors of one-dimensional second-neighbor periodic graphs could precede the present derivation. The sharp asymptotic condition ratio is proved, but no exact finite-\(n\) formula for the index attaining the maximum or minimum is claimed. The source-date anchor belongs to the 2019 determinant-method literature, with earlier enumerative and determinantal results explicitly credited.

## References

1. S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575 (v1, February 27, 2019). https://arxiv.org/abs/1903.03575
2. G. Baron, H. Prodinger, R. F. Tichy, F. T. Boesch and J. F. Wang, *The number of spanning trees in the square of a cycle*, Fibonacci Quarterly **23** (1985), 258–263. https://www.mathstat.dal.ca/FQ/Scanned/23-3/baron.pdf
3. L. Avena and A. Gaudillière, *A proof of the transfer-current theorem in absence of reversibility*, Statistics & Probability Letters **142** (2018), 17–22. https://doi.org/10.1016/j.spl.2018.06.007
4. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (2013). https://arxiv.org/abs/1312.2946
