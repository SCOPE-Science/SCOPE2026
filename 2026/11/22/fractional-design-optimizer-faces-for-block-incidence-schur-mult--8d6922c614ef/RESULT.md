# Fractional-design optimizer faces for block-incidence Schur multipliers

## Finding
For the \(v\times b\) point–block incidence matrix \(B\) of any balanced \(2\)-\((v,k,\lambda)\) design, fix the point-side weights at \(1/v\) in the weighted nuclear-norm characterization of its Schur multiplier norm. The **entire** set of maximizing block probability distributions is the polytope of fractional \(2\)-designs preserving pair incidences. If \(A\) is the pair-by-block incidence matrix, this face is
\[
\mathcal F=\{z\in\mathbb R_{\ge0}^b:Az=(\lambda/b)\mathbf1\},\quad
\dim_{\mathrm{aff}}\mathcal F=b-\operatorname{rank}A.
\]
For the complete \(k\)-uniform block system, its dimension is \(\binom vk-\binom v2\) when \(2\le k\le v-2\), and zero when \(k=v-1\). The numerical Schur norm is known from general results; **the present claim is the exact equality face and dimension**, not that scalar value.

## Assumptions and scope
Let \(v\ge3\), \(2\le k<v\), and \(\lambda\ge1\). Blocks may repeat as labeled columns. Each point lies in \(r\) of the \(b\) blocks and each pair lies in \(\lambda\), so \(bk=vr\) and \(r(k-1)=\lambda(v-1)\). Write \(c_s\in\{0,1\}^v\) for column \(s\). The Schur idempotent acts on \(\mathcal B(\mathbb C^b,\mathbb C^v)\) by \(X\mapsto B\circ X\). We classify block weights with **uniform point weights**, not every joint optimizer.
Define \(H(z)=\sum_s z_s c_sc_s^{\mathsf T}\) and \(F(z)=v^{-1/2}\operatorname{tr}\sqrt{H(z)}\) for \(z\ge0\), \(\sum z_s=1\). The weighted nuclear-norm variational principle of Levene identifies the global Schur norm as the supremum of such values with both row and column weights allowed to vary.

## Proof
**Global attainment at the uniform weights.** The design identities yield \(Q=BB^{\mathsf T}=(r-\lambda)I+\lambda J\) with eigenvalues \(\alpha=r(v-k)/(v-1)>0\) on \(\mathbf1^\perp\) and \(\beta=rk>0\) on \(\mathbf1\). Write \(N=\operatorname{tr}\sqrt Q\). Factor \(B=Q^{1/4}Q^{-1/4}B\). Every row of the first factor has squared norm \(N/v\) because \(\sqrt Q\) has constant diagonal. Every column of the second has squared norm \(c_s^{\mathsf T}Q^{-1/2}c_s=N/b\): this quantity is independent of \(s\) because all columns have \(k\) ones, and its sum is \(N\). The factorization inequality bounds the Schur norm by \(N/\sqrt{vb}\), while uniform weights have weighted nuclear norm exactly \(N/\sqrt{vb}\). Thus \(z^0=\mathbf1/b\) is indeed **globally norming**, not merely optimal after restricting rows.

**Exact equality.** Put \(H_0=H(z^0)=Q/b>0\). The strictly concave function \(H\mapsto\operatorname{tr}\sqrt H\) satisfies
\[
\operatorname{tr}\sqrt{H(z)}\le\operatorname{tr}\sqrt{H_0}+\tfrac12\operatorname{tr}[H_0^{-1/2}(H(z)-H_0)],
\]
with equality only if \(H(z)=H_0\). The tangent term vanishes: each coefficient \(c_s^{\mathsf T}H_0^{-1/2}c_s\) is the same, since \(H_0^{-1/2}\) is a linear combination of \(I\) and \(J\), and all columns have squared norm \(k\) and sum \(k\). Hence \(F(z)\) attains the global Schur norm exactly when \(H(z)=Q/b\).

**Moment equivalence and dimension.** Off-diagonal entries of \(H(z)=Q/b\) are precisely \(Az=(\lambda/b)\mathbf1\). Summing pair equations containing point \(i\) yields \((k-1)\sum_{s:i\in s}z_s=(v-1)\lambda/b=(k-1)r/b\), giving the diagonal equations. Summing all pair equations gives \(\binom k2\sum_s z_s=\binom v2\lambda/b=\binom k2\), giving normalization. The uniform vector is strictly positive, so the affine dimension of the nonnegative solution set equals \(b-\operatorname{rank}A\).

**Complete family.** For \(2\le k\le v-2\), suppose numbers \(a_{ij}\) on pairs have zero sum on every \(k\)-subset. Fix distinct \(i,j\), and subtract equations on \(T\cup\{i\}\) and \(T\cup\{j\}\) as \(T\) runs over the \((k-1)\)-subsets of the other \(v-2\) points. Then \(\sum_{t\in T}(a_{it}-a_{jt})=0\). Since \(1\le k-1<v-2\), comparing equal-sized subsets shows every difference \(a_{it}-a_{jt}=0\). Thus all \(a_{ij}\) equal one constant, forced to zero by any original \(k\)-subset equation. Therefore \(A\) has full row rank \(\binom v2\). If \(k=v-1\), the \(v\) columns are complements of distinct points and their pair-incidence columns are linearly independent (subtract equations for pairs sharing a point), so rank \(v=b\). This completes the classification.

## Verification
The standalone standard-library Python program `verify_design_optimizer_face.py` performs exact rational Gaussian elimination on the pair-incidence matrices for complete designs and constructs positive nonuniform block distributions with unchanged pair marginals whenever the moment kernel is nontrivial. It passed 1,584 exact checks. Finite checks supplement, rather than establish, the infinite-family theorem.

## Relationship to prior work
Levene (2026) supplies the Schur norm variational characterization and automorphism-averaging principle. Shramchenko–Shramchenko (2023) supply the design-incidence spectral structure. The **numerical norm** \((k+\sqrt{(v-1)k(v-k)})/v\) is implied by known constant-polar-diagonal Schur factorization results; no novelty is claimed for it. The new statement is the whole canonical equality face and its exact dimension without automorphism assumptions. Neither inspected source states this. An older general equality-case theorem could imply the result and is a bibliographic risk.

## Limitations
The theorem does not classify simultaneous nonuniform point-side and block-side maximizers, or the vertices of the fractional-design polytope. The general affine-dimension formula depends on the actual incidence rank; only the complete-design family has a parameter-only rank formula here. No independent audit is claimed.

## References
1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (5 November 2026), https://arxiv.org/html/2611.08419v1, especially Lemmas 2.3 and 2.5.
2. A. Shramchenko and V. Shramchenko, *Mutual incidence matrix of two balanced incomplete block designs*, arXiv:2312.03937v1 (6 December 2023), https://arxiv.org/html/2312.03937v1, Sections 1–3.
3. E. Christensen, *Norm optimal factorizations of scalar and block matrices*, arXiv:2211.00591, https://arxiv.org/abs/2211.00591 (abstract checked; complete text not verified).
