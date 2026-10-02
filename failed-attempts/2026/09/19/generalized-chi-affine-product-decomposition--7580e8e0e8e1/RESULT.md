\
# Affine-class count and inherited linear scaling for generalized chi

## Corrected scope after arXiv v2

Let
\[
n=2^k n_0,\qquad n_0\ \text{odd},
\]
and consider the nondegenerate quadratic shift-invariant permutations classified by
Feng, Wang, Yu and Zhang.  Put
\[
\delta=v-w,\qquad d=\gcd(n,\delta),\qquad \ell=n/d.
\]
In the permutation cases, \(\ell>1\) is odd.

Feng--Wang--Yu--Zhang revised arXiv:2609.19548 on 21 September 2026.  Their v2 explicitly
states the interleaved-track/stretching decomposition into ordinary chi blocks and the elementary
equivalence of the two canonical generalized families.  Those structural facts are therefore
**prior work and are not claimed here**.  The earlier SCOPE record
`2026/09/18/generalized-chi-direct-product-differential-structure--6be99e6e6597`
also already records the inherited order, inverse-degree, DDT, differential-uniformity, and
no-cross-track-diffusion consequences.

The surviving claims here are the exact affine-class count across the complete classified family
and the corresponding exact linear-correlation scaling.

## Theorem 1: exact affine-class count

Every nondegenerate classified permutation with the same effective odd block length \(\ell\) is
affine-equivalent to
\[
\chi_\ell^{\times d},
\qquad d=n/\ell.
\]
As \(\delta\) ranges through the permutation cases, the possible values of \(\ell\) are exactly the
divisors \(\ell>1\) of \(n_0\).  Distinct values of \(\ell\) give distinct affine-equivalence
classes.  Hence the family has exactly
\[
\boxed{\tau(n_0)-1}
\tag{1}
\]
nondegenerate affine classes.

### Proof

The v2 track decomposition and the source's shift equivalences put every map with a fixed
\(\ell\) in the affine class of \(\chi_\ell^{\times n/\ell}\).  Conversely every divisor
\(\ell>1\) of \(n_0\) occurs by choosing \(\delta=n/\ell\).

For ordinary odd chi,
\[
\deg(\chi_\ell^{-1})=\frac{\ell+1}{2}.
\]
A Cartesian product has the same vectorial inverse degree as one block, and invertible affine
maps on either side preserve that degree.  Therefore two distinct block lengths have different
inverse degrees and cannot be affine-equivalent.  This proves (1).

## Theorem 2: exact Walsh scaling

For a vectorial Boolean permutation \(F:\mathbb F_2^\ell\to\mathbb F_2^\ell\), write
\[
W_F(\alpha,\beta)
=
\sum_x(-1)^{\alpha\cdot x+\beta\cdot F(x)}
\]
and
\[
\Lambda(F)=\max_{\beta\ne0,\alpha}|W_F(\alpha,\beta)|.
\]
For the \(d\)-fold Cartesian product \(G=F^{\times d}\),
\[
\boxed{
W_G((\alpha_j)_j,(\beta_j)_j)
=
\prod_{j=1}^d W_F(\alpha_j,\beta_j).
}
\tag{2}
\]
Consequently
\[
\boxed{
\Lambda(G)=2^{\ell(d-1)}\Lambda(F).
}
\tag{3}
\]
Indeed, because at least one output mask block is nonzero, one block contributes at most
\(\Lambda(F)\), while every zero-mask block contributes at most \(2^\ell\).  Equality is attained
by choosing one block that attains \(\Lambda(F)\) and taking zero masks on all others.

Affine input/output changes preserve Walsh magnitudes up to reindexing and signs.  Thus every
nondegenerate classified permutation \(P\) with effective block length \(\ell\) satisfies
\[
\boxed{
\Lambda(P)=2^{n-\ell}\Lambda(\chi_\ell),
\qquad
\frac{\Lambda(P)}{2^n}
=
\frac{\Lambda(\chi_\ell)}{2^\ell}.
}
\tag{4}
\]
The larger ambient state therefore gives no improvement in normalized maximum linear correlation
at the nonlinear-layer level.

For context, the same product argument gives
\[
\Delta(P)=2^{n-\ell}\Delta(\chi_\ell)
\]
for differential uniformity; that differential consequence was already recorded by SCOPE on
18 September and is not claimed as new here.

## Relation to prior work

The revised Feng--Wang--Yu--Zhang paper supplies the track decomposition and equivalence of the
canonical families.  Schoone--Daemen supply the ordinary-chi inverse-degree theorem used to
separate block lengths.  Generic product factorization of Walsh transforms is standard.

The retained contribution is therefore deliberately narrow: combining the source classification
with the ordinary-chi inverse invariant gives the exact divisor-indexed affine classification,
and applying the product structure gives the closed normalized linear-correlation law (4).
No priority is claimed for the decomposition itself, for ordinary-chi invariants, or for generic
product-transform identities.

## Limitations

The statement concerns the newly classified quadratic shift-invariant family, not arbitrary
low-latency permutations.  It characterizes the nonlinear permutation layer only; surrounding
linear diffusion can mix the blocks.  The residual results are short deductions from the v2
structure, so their scientific value is classificatory rather than a cryptanalytic break.
