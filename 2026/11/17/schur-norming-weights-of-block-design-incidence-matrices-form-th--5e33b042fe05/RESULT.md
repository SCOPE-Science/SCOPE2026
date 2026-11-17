# Schur-norming weights of block-design incidence matrices form the trade polytope

## Finding

Let a finite nontrivial balanced incomplete block design be a \(2\)-\((v,k,\lambda)\) design, with \(2\le k<v\), allowing separately indexed repeated blocks. Its point–block incidence matrix is \(B\in\{0,1\}^{v\times b}\), its replication number is \(r=\lambda(v-1)/(k-1)\), and \(b=vr/k\). Write \(\mathcal{P}\) for the set of unordered pairs of distinct points and define the pair–block incidence matrix \(Q\in\{0,1\}^{\binom v2\times b}\) by \(Q_{\{i,j\},L}=1\) if the block \(L\) contains both points.

For all probability vectors \(w\in\mathbb R^v_{\ge0}\) and \(z\in\mathbb R^b_{\ge0}\), put
\[
\Phi(w,z)=\left\|D_{\sqrt w}B D_{\sqrt z}\right\|_{\mathcal S_1},\qquad
\Gamma=\frac{(v-1)\sqrt{r-\lambda}+\sqrt{rk}}{\sqrt{vb}}.
\]
Then
\[
\boxed{\Phi(w,z)\le\Gamma,\quad
\Phi(w,z)=\Gamma\iff
w=\tfrac1v\mathbf1\ \text{and}\ Qz=\tfrac\lambda b\mathbf1.}
\]
In particular the exact Schur-multiplier norm of the incidence mask \(B\) is \(\Gamma\). The numerical norm follows from the standard polar-factorization bound; the contribution here is **the complete equality classification**. The optimal block-weight vectors form the nonempty polytope
\[
\boxed{\left(\tfrac1b\mathbf1+\ker_{\mathbb R}Q\right)\cap\mathbb R_{\ge0}^{b},\qquad
\dim_{\mathrm{aff}}=b-\operatorname{rank}_{\mathbb R}Q.}
\]
Thus optimal block weights are unique exactly when \(Q\) has full column rank. Every Steiner \(2\)-design (\(\lambda=1\)) has unique optimal weights on both sides. For the complete \(2\)-\((6,3,4)\) triple design the face has dimension \(5\); the uniform weights lie inside a nontrivial family of optimal weights generated, in part, by a signed eight-triple trade.

The same description determines the coordinate moduli of every rank-one trace-dual norming test: point-vector moduli are \(1/\sqrt v\), block-vector squared moduli lie in the displayed polytope, and arbitrary coordinate phases do not affect the optimum. This is not a classification of arbitrary non-rank-one norm-attaining input operators.

## Assumptions and scope

Everything is finite-dimensional and over the complex field (the same weight inequalities apply to real matrices). Blocks are indexed and may repeat; \(\lambda\) is a positive integer. A block has exactly \(k\) distinct points; each pair lies in exactly \(\lambda\) indexed blocks. The nuclear norm \(\|\cdot\|_{\mathcal S_1}\) is the sum of singular values. The Schur multiplier \(S_B\) acts entrywise on \(v\times b\) matrices with the spectral operator norm. A probability vector has nonnegative coordinates summing to one, and zero weights are allowed. The pair–block matrix \(Q\) has one row per unordered pair and one column per indexed block.

## Proof

**Step 1: isotropic factorization and the sharp upper bound.** The standard design counting identities give
\[
BB^*=(r-\lambda)I+\lambda J,
\qquad r(k-1)=\lambda(v-1),\qquad bk=vr.
\]
Put \(a=\sqrt{r-\lambda}>0\), \(d=\sqrt{rk}=\sqrt{r+\lambda(v-1)}>a\), and \(\delta=(d-a)/v=\lambda/(a+d)>0\). Then
\[
S=(BB^*)^{1/2}=aI+\delta J,
\qquad \operatorname{Tr}S=(v-1)a+d.
\]
Let \(U=S^{1/2}\) and \(V=B^*S^{-1/2}\). Thus \(B=UV^*\). All rows of \(U\) have squared Euclidean norm \(K=\operatorname{Tr}S/v\), since \(UU^*=S\) has constant diagonal. All rows of \(V\) have squared Euclidean norm \(H=\operatorname{Tr}S/b\), since
\[
VV^*=B^*S^{-1}B,
\qquad S^{-1}=a^{-1}I+\frac{d^{-1}-a^{-1}}vJ,
\]
and every column of \(B\) has \(k\) ones. Summing the row norms gives the stated \(H\). Set \(X=D_{\sqrt w}U\), \(Y=D_{\sqrt z}V\). Then \(D_{\sqrt w}BD_{\sqrt z}=XY^*\), \(\|X\|_F^2=K\), and \(\|Y\|_F^2=H\). Schatten Hölder yields
\[
\Phi(w,z)\le\|X\|_F\|Y\|_F=\sqrt{KH}=\Gamma.
\]
For \(w=\mathbf1/v\) and \(z=\mathbf1/b\), the weighted incidence matrix equals \(B/\sqrt{vb}\), whose singular values are the eigenvalues of \(S\) divided by \(\sqrt{vb}\). Hence equality holds, and the bound is sharp.

**Step 2: exact equality in Schatten Hölder.** For arbitrary finite matrices \(X,Y\) with the same column count and positive Frobenius norms, equality in \(\|XY^*\|_1\le\|X\|_F\|Y\|_F\) holds if and only if
\[
\frac{X^*X}{\|X\|_F^2}=\frac{Y^*Y}{\|Y\|_F^2}.
\]
Indeed, a contraction \(W\) attains the trace-norm dual pairing and successive Hilbert–Schmidt Cauchy–Schwarz and contraction inequalities. Equality forces \(WX\) to be a positive scalar multiple of \(Y\), with \(\|WX\|_F=\|X\|_F\). The positive operator \(I-W^*W\) therefore annihilates the range of \(X\), implying equality of the normalized Gram matrices. Conversely, if these Gram matrices agree, the polar decompositions of \(X\) and \(Y\) provide a partial isometry attaining Hölder equality.

For our \(X,Y\), conjugating the Gram identity by \(S^{1/2}\) yields the necessary and sufficient condition
\[
\boxed{B D_z B^*=\frac{H}{K}\,S D_w S=\frac vb\,S D_w S.}\tag{1}
\]

**Step 3: rigidity of the point weights.** Write \(M=B D_zB^*\). For every point \(i\), the fixed block size implies
\[
\sum_{j\ne i}M_{ij}=(k-1)M_{ii}.\tag{2}
\]
Since \(\sum_iw_i=1\), direct multiplication gives
\[
(SD_wS)_{ii}=(a^2+2a\delta)w_i+\delta^2,
\qquad (SD_wS)_{ij}=a\delta(w_i+w_j)+\delta^2\quad(i\ne j).
\]
Substituting (1) into (2) and cancelling the positive factor \(v/b\) gives
\[
\big[(k-1)a^2+a\delta(2k-v)\big]w_i
=a\delta+(v-k)\delta^2.\tag{3}
\]
The coefficient on the left is positive. Indeed \((k-1)a^2=\lambda(v-k)\) and \(0<a\delta<\lambda/2\). When \(v\le2k\) positivity is immediate; when \(v>2k\), it exceeds \(\lambda v/2\). Consequently all \(w_i\) coincide; normalization forces \(w=\mathbf1/v\), including at the boundary where some initial weights might vanish.

**Step 4: the trade polytope.** Substituting \(w=\mathbf1/v\) into (1) gives
\[
BD_zB^*=\tfrac1b S^2=\tfrac1b BB^*.\tag{4}
\]
The off-diagonal entries of (4) assert exactly \(Qz=(\lambda/b)\mathbf1\). Conversely these pair identities imply the diagonal entries as well: summing the pair identities involving point \(i\) yields
\[
(k-1)\sum_{L\ni i}z_L=\frac{\lambda(v-1)}b=\frac{r(k-1)}b,
\]
so \(\sum_{L\ni i}z_L=r/b\). This proves (4), hence (1), and thus equality in the sharp bound. Since \(Q\mathbf1=\lambda\mathbf1\), the solution set is \(z=\mathbf1/b+h\), \(Qh=0\), with nonnegative coordinates. Every vector in \(\ker Q\) has coordinate sum zero, because every column of \(Q\) has \(\binom k2>0\) ones. The uniform vector is strictly positive, so the affine dimension is exactly \(\dim\ker Q=b-\operatorname{rank}Q\). For \(\lambda=1\), each pair belongs to exactly one block, so the columns of \(Q\) have pairwise disjoint nonempty supports and are linearly independent: uniqueness follows.

**Step 5: nonunique equality weights beyond Steiner designs.** For the complete triple design on \(\{1,\ldots,6\}\), every triple is a block; \(v=6\), \(k=3\), \(\lambda=4\), \(b=20\). The pair–triple inclusion matrix \(Q\) has rank \(15\), hence kernel dimension \(5\) (see the exact checker). Partition the six points into \(\{1,2\}\), \(\{3,4\}\), \(\{5,6\}\). Assign \(+1\) or \(-1\) to each of the eight triples selecting one point from each pair, according to the parity of second choices; assign zero to the other twelve triples. The resulting nonzero vector \(h\) satisfies \(Qh=0\): each pair drawn from two different parts belongs to two such triples of opposite signs, while a pair within one part belongs to none. Thus \(z=\mathbf1/20+\varepsilon h\) is an optimizer whenever \(|\varepsilon|\le1/20\), providing explicit nonuniform and boundary optimizers.

Finally, the duality identity
\[
\|S_B\|=\sup_{\|u\|_2=\|v\|_2=1}
\big\|B\mathbin\circ(uv^*)\big\|_1
=\sup_{w,z}\Phi(w,z)
\]
follows by writing the spectral norm as a supremum over unit vectors and dualizing the input spectral-norm ball. Here \(\circ\) denotes entrywise multiplication. Multiplying rows and columns by phases leaves nuclear norms unchanged, giving the claimed description of rank-one trace-dual tests.

## Verification

The proof is valid for every finite design satisfying the displayed axioms and does not use an assumption of point or flag transitivity. The accompanying standalone script `check_design.py` verifies with exact rational arithmetic the design identities for the complete \(2\)-\((6,3,4)\) triple system and the affine \(2\)-\((9,3,1)\) plane, the pair–triple incidence rank \(15\), the five-dimensional trade kernel, and the eight-triple signed trade. The script is supplementary: the universal statement follows from the algebraic proof, not from finite enumeration.

## Relationship to prior work

The factorization upper bound and numerical norm formula are consequences of the classical Schur-multiplier theory discussed by Davidson and Donsig, including the Mathias formula. They are not claimed as new. Levene's recent paper concerns the range of idempotent Schur-multiplier norms via tree attachments; it does not provide this rank-one equality-face classification. A previously established result for finite projective planes determines unique uniform optimal weights for that narrower \(\lambda=1\), symmetric family; the present result additionally treats all nonsymmetric designs and identifies the full nonunique trade polytope when \(\lambda>1\). Classical trade theory supplies the meaning of \(\ker Q\), not the asserted Schur-norming equivalence.

## Limitations

The claim concerns only finite \(2\)-design incidence masks and rank-one *dual test* amplitudes; arbitrary norming operators are not classified. The norm formula itself is classical under the factorization criterion. Repeated indexed blocks are allowed. An older treatment of equality in factorization bounds or combinatorial trade models could express the classification equivalently; publication-priority novelty has not been independently established. The finite example's exact-rank computation does not replace the proof for general designs.

## References

- Rupert H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (first public 5 November 2026), primary MSC2020 47A30. https://arxiv.org/html/2611.08419v1
- Kenneth R. Davidson and Allan P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073v1 (2005), especially Proposition 4.1 and Theorem 4.5. https://arxiv.org/html/math/0506073v1
- Rupert H. Levene, *Norms of idempotent Schur multipliers*, New York Journal of Mathematics 20 (2014), 325–352; publicly accessible abstract. https://nyjm.albany.edu/j/2014/20-19.html
