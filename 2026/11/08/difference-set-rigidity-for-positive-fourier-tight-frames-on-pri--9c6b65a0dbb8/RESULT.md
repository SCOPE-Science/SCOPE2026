# Difference-set rigidity for positive Fourier tight frames on prime cycles

## Finding
Let \(p\) be any prime and \(\varnothing\ne A\subseteq\mathbb Z/p\mathbb Z\). For each frequency \(\xi\in\mathbb Z/p\mathbb Z\), form the restricted Fourier character \(v_\xi=(e^{2\pi i a\xi/p})_{a\in A}\in\mathbb C^A\). A **positive Parseval design** is a set of distinct frequencies \(S\) and strictly positive real weights \(w_\xi\), \(\xi\in S\), such that
\[
\sum_{\xi\in S}w_\xi v_\xi v_\xi^*=I_{\mathbb C^A}.
\]
Write \(D=A-A\) and \(d=|D|-1\). The exact least number of nodes is
\[
\boxed{\min_{S,w}|S|=|A-A|=d+1.}
\]
Every feasible design with exactly \(|A-A|\) nodes has uniquely determined weights for its prescribed frequency set. For odd \(p\), let \(D_+\) contain one representative from each pair \(\{t,-t\}\subset D\setminus\{0\}\), and define
\[
X_\xi=(\cos(2\pi t\xi/p),\sin(2\pi t\xi/p))_{t\in D_+}\in\mathbb R^d.
\]
Then a set \(S\) of \(d+1\) frequencies is optimal precisely when \(0\) lies in the interior of the \(d\)-simplex \(\operatorname{conv}\{X_\xi:\xi\in S\}\); the unique barycentric coordinates of \(0\) are the weights. For \(p=2\), use \(X_\xi=(-1)^\xi\) when \(d=1\), and the assertion is unchanged.

At fixed spatial cardinality \(k=|A|\), the minimum over all \(A\) is
\[
\boxed{\min_{|A|=k}\min_{S,w}|S|=\min(p,2k-1).}
\]
When \(2\le k\le(p-1)/2\), equality holds exactly for arithmetic progressions in \(\mathbb Z/p\mathbb Z\). When \(k>(p-1)/2\), every \(k\)-point set has \(A-A=\mathbb Z/p\mathbb Z\). Finally, for every \(|A|\ge2\), any Parseval design with **equal positive weights** requires all \(p\) frequencies, even when arbitrary positive weights need only \(|A-A|\) frequencies.

## Assumptions and scope
The prime \(p\) may equal \(2\); the spatial set \(A\) is nonempty. Both node selection and strictly positive real weights are allowed, but a node cannot be repeated. Frequencies and spatial positions lie in the cyclic additive group of order \(p\). The frame operator is normalized to the identity, with character vectors of coordinate modulus one. The empty set of frequencies is never admissible.

## Proof
**1. Moment formulation.** Because every character vector has unit-modulus coordinates, the diagonal entries of a Parseval frame operator all equal \(\sum_{\xi\in S}w_\xi\). Thus normalization forces \(\sum_{\xi\in S}w_\xi=1\). Its \((a,b)\)-entry equals \(\sum_{\xi\in S}w_\xi e^{2\pi i(a-b)\xi/p}\). Hence the operator is the identity if and only if
\[
\sum_{\xi\in S}w_\xi e^{2\pi it\xi/p}=\begin{cases}1&t=0,\\0&t\in D\setminus\{0\}.\end{cases}
\]
This is an exact reformulation, with no generic-position assumption.

**2. Prime-order lower bound.** Let \(r=|S|\). Suppose \(r\le d\). Choose any \(r\) distinct elements \(t\) from \(D\setminus\{0\}\). The corresponding \(r\)-by-\(r\) matrix \((e^{2\pi it\xi/p})_{t,\xi\in S}\) is nonsingular by Chebotarev's prime-order Fourier-minor theorem. The required zero moments would then force every \(w_\xi=0\), contradicting the normalization. Consequently \(r\ge d+1\). When \(d=0\), the same lower bound is immediate from nonemptiness.

**3. Positive existence at the lower bound.** For odd \(p\), \(D\setminus\{0\}\) consists of \(d/2\) opposite pairs. Form the real moment vectors \(X_\xi\in\mathbb R^d\) as above. Orthogonality of nontrivial characters gives \(p^{-1}\sum_{\xi\in\mathbb Z/p\mathbb Z}X_\xi=0\). Carathéodory's convex-hull theorem gives a convex representation of \(0\) using at most \(d+1\) points \(X_\xi\). Discard zero coefficients. The resulting positive weights satisfy all complex moment equations by conjugate symmetry, so they give a Parseval design. Step 2 forces exactly \(d+1\) strictly positive weights. For \(p=2\), either \(A\) is a singleton (one node suffices) or \(A\) is the whole group (the two Fourier nodes with weights \(1/2\) suffice); these cases give the same law.

**4. All minimal designs.** For any \(S\) with \(|S|=d+1\), the square Fourier submatrix with rows indexed by \(D\) and columns by \(S\) is nonsingular by the same prime-order minor theorem. The normalized moment system therefore has a unique complex solution. If it is positive, it is the unique Parseval weighting. In the real coordinate system, adding the normalization row to the \(d\) moment coordinates is an invertible row transformation of this square complex matrix. Thus the \(d+1\) points \(X_\xi\) are affinely independent and define a full-dimensional simplex. All its barycentric coordinates for \(0\) are positive exactly when \(0\) lies in its interior. This proves the stated optimizer criterion. The elementary \(p=2\) case is identical with the sign coordinate.

**5. Spatial optimization.** The Cauchy–Davenport inequality applied to \(A+(-A)\) gives \(|A-A|\ge\min(p,2k-1)\). Any length-\(k\) arithmetic progression with nonzero step attains equality. For \(2\le k\le(p-1)/2\), equality lies at most \(p-2\), so Vosper's equality theorem with the two sets \(A\) and \(-A\) forces \(A\) to be an arithmetic progression. If \(k>(p-1)/2\), every translate of \(A\) meets \(A\) by pigeonhole, hence \(A-A\) is the full group.

**6. Equal-weight contrast.** If \(|A|\ge2\), choose any nonzero \(t\in D\). Equal weights on a nonempty design \(S\) demand \(\sum_{\xi\in S}\zeta_p^{t\xi}=0\), where \(\zeta_p=e^{2\pi i/p}\). Because multiplication by \(t\) permutes the residues, the indicator polynomial \(P(z)=\sum_{\xi\in S}z^{t\xi\bmod p}\), with coefficients zero or one and degree at most \(p-1\), vanishes at \(\zeta_p\). Its minimal polynomial is \(1+z+\cdots+z^{p-1}\), so \(P\) is precisely that polynomial and \(S\) must be all \(p\) frequencies. Their uniform weights \(1/p\) give Parseval by Fourier orthogonality.

The primality hypothesis cannot simply be dropped: for \(\mathbb Z/6\mathbb Z\) and \(A=\{0,1,2\}\), the difference set has five elements, while the three frequencies \(\{0,2,4\}\), each of weight \(1/3\), already give a Parseval design.

## Verification
The accompanying `CHECK.py` performs numerical feasibility and exact-cardinality checks for all nonempty spatial sets in prime orders \(2,3,5,7\), and for systematic/random spatial families in prime orders \(11,13,17,19\). It checks the actual complex frame matrices and moment equations. Numerical tests do not prove existence or optimality in all primes; those follow from Chebotarev's theorem, Carathéodory's theorem, Cauchy–Davenport and Vosper as used above. Run `python CHECK.py` with the dependencies in `requirements.txt`.

## Relationship to prior work
The exact prime-order Fourier-minor theorem and equivalent support-sum uncertainty principle are classical (Chebotarev; Tao); convex representation by at most \(d+1\) vectors is the classical Carathéodory theorem. Both are explicitly invoked, not claimed as new. The recent finite Gabor-frame study by Asipchuk, De Carli and Rodriguez addresses block-equivalent frame operators under subgroup translation/modulation sets and does not state the present minimum positive-frequency design for arbitrary spatial subsets. An indexed previous result established the optimal positive frequency budget for three consecutive cyclic sites, including its prime-order five-frequency case; this is a special case of the present all-support law, not a converse. A previous unweighted prime-power tight-frame result imposes equal weights and can require the full prime-order spectrum, unlike the positive-weighted designs here. An earlier statement in equivalent quadrature, scalable frame or convex-design language may exist; no universal priority claim is made.

## Limitations
No numerical conditioning or lower bound on the smallest optimal weight is claimed. A desired prescribed frequency set of optimal cardinality need not admit positive weights; the simplex criterion decides admissibility. The exact budget and Fourier-minor rigidity rely on prime cyclic order, and the explicit composite-order example shows they fail for arbitrary composite orders. The result does not address stability under noisy measurements or arbitrary complex-valued nonpositive weights. Its novelty is assessed relative to inspected literature; the proof deliberately combines well-established theorems.

## References
1. O. Asipchuk, L. De Carli, and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first submitted 15 May 2026; https://arxiv.org/abs/2605.16139 (sections 1, 3–5).
2. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, https://arxiv.org/abs/math/0308286 (prime Fourier-minor theorem and uncertainty principle).
3. M. Loukaki, *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle*, Bulletin of the London Mathematical Society (2025), https://doi.org/10.1112/blms.70192 (Introduction, Theorem 1, proof comparison).
4. A. G. Vosper, *The critical pairs of subsets of a group of prime order*, Journal of the London Mathematical Society (1956), Parts I–II (critical-pair equality case).
5. Cauchy–Davenport theorem and Carathéodory convex-hull theorem (classical, in the forms explicitly stated and applied in the proof).
