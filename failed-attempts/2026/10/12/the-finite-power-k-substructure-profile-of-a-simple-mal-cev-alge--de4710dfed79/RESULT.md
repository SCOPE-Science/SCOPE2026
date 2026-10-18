# The finite-power \(K\)-substructure profile of a simple Mal'cev algebra is an \(r\)-Whitney triangle

## Finding

Let \(\mathbf A\) be a finite simple non-abelian Mal'cev algebra. Write
\[
a=|\operatorname{Aut}\mathbf A|,
\qquad
c=|E|,
\]
where \(E\) is the set of idempotents of \(\mathbf A\), equivalently the constant endomorphisms. For integers \(v\ge 0\) and \(u\ge 0\), let \(N_{v,u}\) denote the number of subalgebras of \(\mathbf A^v\) that are isomorphic to \(\mathbf A^u\), with \(\mathbf A^0\) interpreted as a one-element algebra. Then
\[
\boxed{N_{v,u}=W_{a,c}(v,u),}
\]
where \(W_{m,r}(n,k)\) is the \(r\)-Whitney number of the second kind. Equivalently,
\[
\boxed{
N_{v,u}=
\frac{1}{u!a^u}
\sum_{j=0}^{u}(-1)^{u-j}\binom uj(c+aj)^v
}
\]
for \(u\ge1\), while \(N_{v,0}=c^v\). Hence the exact number of embeddings is
\[
\boxed{
|\operatorname{Emb}(\mathbf A^u,\mathbf A^v)|
= u!a^u W_{a,c}(v,u)
=\sum_{j=0}^{u}(-1)^{u-j}\binom uj(c+aj)^v.
}
\]

Thus the finite members \(\{\mathbf A^u:u\ge1\}\) used by Mayr and Ruškuc as a generalized Fraïssé class have a completely explicit rank profile inside every finite power. The profile satisfies
\[
N_{v+1,u}=N_{v,u-1}+(c+au)N_{v,u}
\]
and has column exponential generating functions
\[
\boxed{
\sum_{v\ge0}N_{v,u}\frac{z^v}{v!}
=\frac{e^{cz}}{u!}\left(\frac{e^{az}-1}{a}\right)^u.
}
\]

For a finite non-abelian simple group \(S\), one has \(c=1\), so the profile specializes to the ordinary Dowling-lattice Whitney triangle with group-size parameter \(|\operatorname{Aut}S|\). For example, since \(|\operatorname{Aut}A_5|=120\), the direct square \(A_5^2\) contains exactly
\[
W_{120,1}(2,1)=122
\]
subgroups isomorphic to \(A_5\): the two coordinate factors and the \(120\) automorphism diagonals.

## Assumptions and scope

Only subalgebras isomorphic to direct powers \(\mathbf A^u\) are counted. A finite power \(\mathbf A^v\) can have other subalgebras, and Mayr--Ruškuc explicitly note that the class of direct powers need not have the hereditary property. The parameter \(c\) may be zero if \(\mathbf A\) has no idempotents. The formula for \(u=0\) merely records the \(c^v\) one-element subalgebras arising from idempotent tuples.

## Proof

Mayr and Ruškuc use the Foster--Pixley theorem in their proof of amalgamation. For an embedding
\[
\varphi:\mathbf A^u\longrightarrow\mathbf A^v,
\]
each target coordinate has the form
\[
(a_1,\ldots,a_u)\longmapsto \alpha(a_j),
\]
where \(j\in[u]\) and \(\alpha\) is either an automorphism of \(\mathbf A\) or a constant endomorphism determined by an idempotent. They further observe that every source coordinate \(j\) must occur at least once with \(\alpha\in\operatorname{Aut}\mathbf A\).

As actual coordinate maps, there are exactly \(au+c\) choices: \(au\) nonconstant maps \(\alpha\circ\pi_j\), and \(c\) constant maps. These maps are distinct. Two different automorphisms on the same source coordinate differ on some input; maps using different source coordinates can be separated by varying one coordinate while holding the other fixed; and different idempotents give different constants.

Conversely, a tuple of \(v\) such coordinate maps is injective exactly when every one of the \(u\) source coordinates occurs among the nonconstant choices. Sufficiency is immediate because one automorphic output coordinate recovers each source coordinate. Therefore inclusion--exclusion over the source coordinates that are omitted gives
\[
E_{v,u}:=|\operatorname{Emb}(\mathbf A^u,\mathbf A^v)|
=\sum_{j=0}^{u}(-1)^{u-j}\binom uj(c+aj)^v.
\]

Taking \(v=u\), injectivity forces each source coordinate to appear exactly once and forbids constant outputs. Hence
\[
|\operatorname{Aut}(\mathbf A^u)|=E_{u,u}=u!a^u.
\]
Every image subalgebra is counted by exactly \(|\operatorname{Aut}(\mathbf A^u)|\) embeddings, since any two isomorphisms from \(\mathbf A^u\) onto the same image differ by a unique domain automorphism. Thus
\[
N_{v,u}=\frac{E_{v,u}}{u!a^u}.
\]
The standard explicit formula for \(r\)-Whitney numbers of the second kind is
\[
W_{m,r}(n,k)=\frac{1}{k!m^k}
\sum_{j=0}^{k}(-1)^{k-j}\binom kj(r+mj)^n,
\]
so \(N_{v,u}=W_{a,c}(v,u)\). Their standard recurrence and exponential generating function then give the displayed profile recurrence and generating function. They can also be obtained directly by differentiating the generating function or by adjoining one target coordinate.

## Verification

The script `verify_whitney_subpowers.py` performs three independent exact checks.

First, it verifies the \(r\)-Whitney recurrence against the inclusion--exclusion formula for \(1\le a\le6\), \(0\le c\le4\), and all entries through \(v=11\). Second, it exhaustively enumerates symbolic Foster--Pixley coordinate descriptors for small \((a,c,u,v)\) and confirms both the embedding formula and division by \(u!a^u\). Third, it checks a concrete algebra from Mayr--Ruškuc Example 1.2,
\[
\mathbf A=(\mathbb Z_2,x-y+z,\cdot),
\]
for which \(a=1\) and \(c=2\). It independently enumerates every map \(\mathbf A^u\to\mathbf A\) for \(u\le3\), tests preservation of both basic operations, then exhaustively enumerates embeddings into \(\mathbf A^v\) for \(v\le4\) and counts distinct image subalgebras. The recorded output is

```text
VERIFY_OK 2841 exact assertions
```

The first nontrivial image-count rows for this concrete algebra are
\[
(5,1),\qquad (19,9,1),\qquad (65,55,14,1)
\]
for \(v=2,3,4\), respectively, agreeing with \(W_{1,2}(v,u)\).

## Relationship to prior work

Mayr and Ruškuc prove that \(K=\{\mathbf A^k:k\ge1\}\) has JEP and AP and identify its generalized Fraïssé limit as a filtered Boolean power. Their amalgamation proof records exactly the Foster--Pixley normal form for embeddings needed above, but the paper does not enumerate embeddings or \(K\)-subalgebras; full-text searches for “Whitney” and “count” return no such result.

The numbers \(W_{m,r}(n,k)\) themselves are classical. Mező introduced the \(r\)-Whitney numbers, and Cheon--Jung developed their Dowling-lattice interpretation. In the group case \(c=1\), the formula therefore recovers the familiar Dowling Whitney numbers numerically. The contribution here is the identification of the entire finite-power \(K\)-substructure profile of an arbitrary finite simple non-abelian Mal'cev algebra with the \(r\)-Whitney triangle having parameters \((|\operatorname{Aut}\mathbf A|,|E|)\), including the multi-idempotent cases that occur in the filtered-Boolean-power setting.

Candidate-specific searches for direct-power embedding counts, diagonal-subgroup/Dowling formulations, few-subpower enumeration, and Whitney-number formulations did not locate this general Mal'cev-algebra statement.

## Limitations

The result is an enumerative corollary of a strong structural theorem already used explicitly by Mayr and Ruškuc; it does not strengthen their amalgamation or Fraïssé-limit theorem. In the special case of groups, the same numbers are classical Dowling Whitney numbers and closely related diagonal-subgroup descriptions may be folklore. The claim is therefore best viewed as an exact quantitative synthesis for the finite-power age, with the strongest novelty in the general Mal'cev and multiple-idempotent setting.

## References

P. Mayr and N. Ruškuc, “Filtered Boolean powers of finite simple non-abelian Mal'cev algebras,” arXiv:2404.17322, first posted 26 April 2024, primary MSC 03C05. See Theorem 1.1 and the proof in Section 3, especially the Foster--Pixley embedding normal form.

I. Mező, “A new formula for the Bernoulli polynomials,” *Results in Mathematics* 58 (2010), 329--335, DOI 10.1007/s00025-010-0039-z.

G.-S. Cheon and J.-H. Jung, “r-Whitney numbers of Dowling lattices,” *Discrete Mathematics* 312 (2012), 2337--2348, DOI 10.1016/j.disc.2012.04.001.
