# Reversal-rigid Walsh spectrum of acyclic orientations of \(K_{2,n}\)

## Finding
For every integer \(n\ge2\), the indicator of the acyclic edge orientations of the labelled complete bipartite graph \(K_{2,n}\), encoded in the binary edge group \(G_n=(\mathbb Z/2\mathbb Z)^{2n}\), has a completely explicit signed Walsh transform. Its Fourier zero set consists **exactly** of the characters that are odd under simultaneous reversal of every edge. Thus unnormalized counting convolution by this indicator has rank and nullity both equal to \(2^{2n-1}\). Its least nonzero singular value is exactly \(2\), its largest is \(2\cdot3^n-2^n\), and its sharp Hilbert-space condition number on the recoverable range is \(3^n-2^{n-1}\). The recoverable range comprises exactly reversal-invariant functions, whose orthogonal projection is the positive averaging operator \(g\mapsto(g+g(\cdot+\mathbf1))/2\).

## Assumptions and scope
Let the left vertices be \(u_1,u_2\), and let the right vertices be \(v_1,\ldots,v_n\). For each of the \(2n\) edges, record a bit: \(0\) for direction left to right, and \(1\) for right to left. Each orientation is therefore a vector \(x\in G_n\), with the \(j\)-th column \(x^{(j)}=(x_{1j},x_{2j})\in\{00,10,01,11\}\). Let \(f_n(x)=1\) if the orientation is acyclic and \(0\) otherwise. For \(\xi\in G_n\), set
\[
W_n(\xi)=\sum_{x\in G_n}f_n(x)(-1)^{\langle\xi,x\rangle}.
\]
This is the **unnormalized** Walsh transform. The convolution operator is \((T_ng)(y)=\sum_xf_n(x)g(y+x)\), on real or complex functions on \(G_n\). Let \(a,b,c,d\) be the respective counts of frequency columns \(00,10,01,11\), so \(a+b+c+d=n\). Then the full signed spectrum, including multiplicities, is
\[
\boxed{W_n(\xi)=3^a\big((-1)^b+(-1)^c\big)-2^n\mathbf1_{\{b+c=0\}}.}
\]
Each quadruple \((a,b,c,d)\) occurs with multiplicity \(n!/(a!b!c!d!)\), with coincident numerical eigenvalues combined by adding multiplicities. Explicitly, the value is zero if \(b+c\) is odd; equals \(2(-1)^b3^a\) if \(b+c\) is positive even; and equals \(2\cdot3^a-2^n\) if \(b+c=0\). At \(n=1\) the last branch can vanish, so the stated zero-set and smallest-gap conclusions specifically assume \(n\ge2\).

## Proof
**1. Orientation classification.** Every simple directed cycle in \(K_{2,n}\) must use both left vertices, so it has length four. Such a directed four-cycle occurs if and only if two right vertices have the opposite mixed orientation columns \(10\) and \(01\). Therefore the set of acyclic orientations is the union of the product family that omits column \(10\) and the product family that omits column \(01\); their intersection consists of columns \(00\) and \(11\) only. This also proves the geometric interpretation in terms of lonesum binary matrices.

**2. Exact character sum.** A Walsh character factors over columns. On the column alphabet \(\{00,01,11\}\), its local character sum is respectively \(3,1,-1,1\) when the frequency column is \(00,10,01,11\). On \(\{00,10,11\}\), the corresponding values are \(3,-1,1,1\). On the intersection alphabet \(\{00,11\}\), the local value is \(2\) for frequency \(00\) or \(11\), and zero for \(10\) or \(01\). Applying inclusion–exclusion to the two product families gives the boxed formula, for every frequency and all \(n\ge1\). At zero frequency, it yields the number of orientations \(2\cdot3^n-2^n\).

**3. Exact zero set.** If \(b+c\) is odd, the two signed powers cancel and the intersection product is zero. If \(b+c\ge2\) is even, the multiplier is \(\pm2\cdot3^a\), hence nonzero. If \(b+c=0\), a zero would require \(2\cdot3^a=2^n\); unique prime factorization forces \(a=0\) and \(n=1\), which is excluded. Thus zero occurs precisely when \(b+c\) is odd. Since the Hamming parity of \(\xi\) equals \(b+c\pmod2\), exactly half of the \(4^n\) characters vanish.

**4. Singular-value bounds and recovery.** Each Walsh character is an eigenvector of \(T_n\) with real eigenvalue \(W_n(\xi)\), so its singular value is the multiplier's absolute value. Every nonzero value is an even integer, and for \(n\ge2\), a frequency with exactly two columns of type \(10\) and all other columns \(11\) has multiplier \(2\), proving sharpness of the lower bound. The triangle inequality gives \(|W_n(\xi)|\le\sum_x f_n(x)=2\cdot3^n-2^n\), attained by the trivial character. Their ratio is \(3^n-2^{n-1}\). Let \(\mathbf1\in G_n\) be the vector whose every edge coordinate is one. A character is fixed by translation by \(\mathbf1\) exactly when \(b+c\) is even. The Fourier-range of \(T_n\) is therefore the \(+1\)-eigenspace of this translation, with orthogonal projection \(P_ng=(g+g(\cdot+\mathbf1))/2\). In particular, \(\|P_n\|_{\ell^p\to\ell^p}=1\) for every \(1\le p\le\infty\). Inversion on this range is given by dividing the surviving Fourier coefficients by the boxed multiplier; no information about the odd component can be recovered.

## Verification
The standalone standard-library script `verify.py` builds the indicator independently from the forbidden mixed-column condition; for \(2\le n\le5\) it additionally checks acyclicity by an independent directed-cycle search for every orientation. It then performs a full exact-integer Walsh–Hadamard transform for every \(2\le n\le7\), comparing all \(4^n\) coefficients with the closed formula. It verifies the counts, rank, zeros, extreme singular values and parity conditions. It printed `All exact checks passed.` The proof above applies for every integer \(n\ge2\); finite tests are corroboration, not a substitute.

## Relationship to prior work
Stanley established the relationship between acyclic orientations and chromatic polynomial evaluation [1]. West studied the distribution of dependent edges in acyclic orientations of complete bipartite graphs [2]. Kamano, Ohno and Yamamoto studied the ordinary one-variable total-entry-weight enumerator of lonesum matrices [3]. Cameron, Glass, Rekvényi and Schumacher established a complete-bipartite acyclic-orientation count and its poly-Bernoulli interpretation [4], including the bijection with lonesum matrices. These results supply the natural objects, orientation/forbidden-pattern equivalences, and unweighted or total-weight enumeration. They do not state the per-edge \(2n\)-variable Walsh multiplier formula, the absence of additional Fourier zeros, or the exact sharp reconstruction constants. A full multivariate edge-weight enumerator, if previously published, could specialize to these statements; this is the principal remaining priority risk.

## Limitations
The result is for a fixed labelled two-vertex shore and arbitrary opposite-shore size \(n\ge2\), not for general \(K_{m,n}\). The indicator is a Boolean edge-orientation indicator, not a distribution over graph isomorphism classes. The condition number is the ratio of nonzero singular values in the Hilbert/Fourier sense; it is not asserted as the norm of a deconvolution inverse on every \(\ell^p\) space. The exact nullspace is the odd-under-global-reversal component. The absence of a matching statement in the inspected literature does not establish absolute historical novelty. No independent audit has been performed.

## References
[1] R. P. Stanley, *Acyclic Orientations of Graphs*, Discrete Mathematics **5** (1973), 171–178. https://sites.math.washington.edu/~reu/papers/current/jair/acyclic.pdf

[2] D. B. West, *Acyclic Orientations of Complete Bipartite Graphs*, Discrete Mathematics **138** (1995), 393–396. https://dwest.web.illinois.edu/pubs/aobip.pdf

[3] K. Kamano, Y. Ohno and S. Yamamoto, *Weighted Lonesum Matrices and Their Generating Function*, Integers **13** (2013), A25, first public dated version 2013-05-10. https://math.colgate.edu/~integers/n25/n25.pdf

[4] P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic Orientations and Poly-Bernoulli Numbers*, first arXiv version 2014-12-11, arXiv:1412.3685. https://arxiv.org/abs/1412.3685
