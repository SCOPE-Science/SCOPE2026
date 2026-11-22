# Exact Boolean Fourier spectrum and sharp range projection for the nine-point affine matroid

## Finding

Let \(V=\mathbb F_3^2\), let \(\mathcal L\) be its 12 three-point affine lines, and let \(\mathcal B=\binom{V}{3}\setminus\mathcal L\) be the 72 bases of the rank-three affine-plane matroid. Identify subsets of \(V\) with vectors in \(G=\mathbb F_2^V\). Put \(b(x)=1\) when \(x\) is the incidence vector of a member of \(\mathcal B\), and \(b(x)=0\) otherwise. Consider unnormalized convolution \(T_bf(x)=\sum_{y\in G}b(y)f(x+y)\) on real or complex functions on \(G\).

For every \(U\subseteq V\), its Walsh multiplier is \(\lambda(U)=\sum_{B\in\mathcal B}(-1)^{|U\cap B|}\). The complete signed spectrum, with multiplicity, is

| Multiplier | Multiplicity |
|---:|---:|
| \(-72\) | 1 |
| \(-24\) | 9 |
| \(-8\) | 126 |
| \(0\) | 240 |
| \(8\) | 126 |
| \(24\) | 9 |
| \(72\) | 1 |

Thus \(T_b\) has rank \(272\), nullity \(240\), and positive and negative inertia \(136\) each. Its smallest positive singular value is \(8\), its largest is \(72\), its sharp \(\ell^2\) condition number on the recoverable subspace is \(9\), and the norm of its Moore--Penrose inverse there is \(1/8\). Every surviving multiplier has exact 2-adic valuation \(3\), so the product of all nonzero eigenvalues has 2-adic valuation \(816\).

Write \(W=\operatorname{ran}(T_b)\). The unique translation-invariant projection \(P\) onto \(W\) has convolution kernel \(p\), whose complete classification is:

| Condition on \(z\subseteq V\) | \(512p(z)\) | Count |
|---|---:|---:|
| \(z=\varnothing\) | 272 | 1 |
| \(|z|=4\), containing an affine line | 16 | 72 |
| \(|z|=4\), containing no affine line | -16 | 54 |
| \(|z|=6\), whose complement is an affine line | 32 | 12 |
| \(|z|=8\) | -48 | 9 |
| All other subsets | 0 | 364 |

Among **all** bounded linear projections from \(\ell^1(G)\) onto \(W\), including non-translation-invariant ones, the least possible operator norm equals \(97/16\). Exactly the same sharp constant holds for projections from \(\ell^\infty(G)\) onto \(W\). It is attained by \(P\).

## Assumptions and scope

The ground set is precisely the nine labelled points \(\mathbb F_3^2\), with the standard affine lines, not the ternary projective plane or a binary matroid. No orientations or multiplicity weights are introduced. All Fourier transforms and convolution operators use the unnormalized counting convention. The range and norms refer to functions on the entire Boolean group of size \(512\). The statement is a complete finite classification, not a claim about other affine planes or a uniform infinite family.

## Proof

**1. Signed basis multipliers.** For \(U\subseteq V\) with \(k=|U|\), let \(\ell(U)\) denote the number of lines wholly inside \(U\), and set
\[
K_r(k)=\sum_{j=0}^{r}(-1)^j\binom{k}{j}\binom{9-k}{r-j},
\]
where inadmissible binomial coefficients are zero. The sum over all three-element subsets is \(K_3(k)\). Let \(n_j\) be the number of affine lines meeting \(U\) in exactly \(j\) points. Since there are 12 lines, every point lies on four lines, and every pair lies on exactly one line,
\[
\sum_{j=0}^{3}n_j=12,\qquad n_1+2n_2+3n_3=4k,\qquad n_2+3n_3=\binom{k}{2},\qquad n_3=\ell(U).
\]
Consequently the signed line sum is
\[
L(U)=\sum_{\ell\in\mathcal L}(-1)^{|U\cap\ell|}
=12-8k+4\binom{k}{2}-8\ell(U),
\]
and subtraction of the lines from the complete triple family gives the exact identity
\[
\boxed{\lambda(U)=K_3(k)-12+8k-4\binom{k}{2}+8\ell(U).}
\]
At sizes \(k=0,1,2,3,4\), this simplifies respectively to \(72,24,0,-8+8\ell(U),-8+8\ell(U)\). A three-set contains a line exactly when it *is* a line. A four-set contains at most one line, because two different lines in an affine plane have union of at least five points. Of the \(\binom94=126\) four-sets, exactly \(12(9-3)=72\) contain a line; the other \(54\) are four-caps. There are \(12\) three-point lines and \(72\) noncollinear triples. Since every basis has three elements, \(\lambda(V\setminus U)=-\lambda(U)\). These facts yield the table for every one of the \(512\) frequencies and all its rank, sign, gap, condition and valuation consequences.

In particular, for \(|U|\le4\) the zero multipliers occur precisely when \(|U|=2\), when \(U\) is a three-point line, or when \(U\) is a four-set containing a line. For larger \(U\), apply complementation. This describes every unrecoverable character geometrically.

**2. Projection kernel.** Let \(\mathcal F\) consist of the empty set, all singletons, all noncollinear triples, and all four-caps. By the preceding classification, the nonzero Walsh frequencies are exactly \(\mathcal F\sqcup\{V\setminus U:U\in\mathcal F\}\). For \(z\subseteq V\), write \(t=|z|\) and \(s_v=(-1)^{\mathbf1_{v\in z}}\), so \(S=\sum_{v\in V}s_v=9-2t\). Walsh inversion for the projection gives
\[
512p(z)=\sum_{U:\lambda(U)\ne0}(-1)^{|U\cap z|}.
\]
Complement pairing multiplies the contribution of \(\mathcal F\) by \(1+(-1)^t\). The sum over its noncollinear triples is \(K_3(t)-L(z)\). The sum over four-sets containing some line, each occurring once, equals
\[
\sum_{\ell\in\mathcal L}\left(\prod_{v\in\ell}s_v\right)\sum_{w\notin\ell}s_w
=S L(z)-\sum_{\ell\in\mathcal L}\sum_{w\in\ell}\prod_{v\in\ell\setminus\{w\}}s_v
=S L(z)-K_2(t),
\]
since every unordered pair appears in exactly one line. Therefore
\[
\boxed{512p(z)=(1+(-1)^t)\left[\sum_{r=0}^{4}K_r(t)-(10-2t)L(z)\right].}
\]
For even \(t=0,2,4,6,8\), the sum of the first five Krawtchouk terms is \(256,0,0,0,0\), respectively. The line sum is, respectively, \(12,0,4-8\ell(z),8\ell(V\setminus z),-4\), using the signed-complement identity for three-point lines at the last two weights. For odd \(t\) the prefactor vanishes. Substitution proves the displayed projection-kernel classification, without relying on an enumeration certificate.

**3. Unrestricted optimality.** For any projection \(Q\) onto \(W\), average the conjugates \(\tau_a Q\tau_{-a}\) over all translations \(a\in G\). Each conjugate is a projection onto the translation-invariant space \(W\), so their average fixes \(W\), has range contained in \(W\), and is itself a projection. The average commutes with every translation; hence it is a Fourier multiplier. Its multiplier must equal one on the frequencies spanning \(W\) and zero elsewhere, so the average is precisely \(P\). Translation is an isometry in both \(\ell^1\) and \(\ell^\infty\); convexity yields \(\|P\|\le\|Q\|\) in either norm. For a convolution operator, the \(\ell^1\) and \(\ell^\infty\) norms both equal the sum of absolute kernel coefficients, by testing a delta mass in \(\ell^1\) and a matching sign function in \(\ell^\infty\). The kernel table gives
\[
\|P\|_{1\to1}=\|P\|_{\infty\to\infty}
=\frac{272+72(16)+54(16)+12(32)+9(48)}{512}=\boxed{\frac{97}{16}}.
\]
This proves sharp optimality without any assumption of symmetry on competing projections.

## Verification

The standalone file `verify_ag23.py` requires only the Python 3 standard library. Run `python3 verify_ag23.py` in the directory containing the extracted file. It builds the 12 affine lines in two independent ways, constructs the 72 bases, evaluates all 512 signed base sums, checks the incidence/Krawtchouk identities and the complete multiplicity table, computes the Walsh transform of the nonzero-frequency indicator, verifies the projection-kernel formula for every input, and checks Fourier idempotency and the exact endpoint norm. The actual packaged verifier passed 3,123 exact integer assertions. The finite computation is corroboration of the analytic proof, not a substitute for it.

## Relationship to prior work

Merino, Ramírez-Ibáñez and Rodríguez-Sánchez explicitly identify the nine-point affine plane with the unique Steiner triple system \(S(2,3,9)\), exhibit its twelve circuit hyperplanes, and compute its Tutte polynomial. That determines aggregate matroid enumeration but does not supply the signed Walsh sums, their zero-character geometry, or the sharp endpoint projection norm. Goodall develops finite Fourier methods for graph-polynomial and Tutte-Grothendieck invariants, providing general Fourier context without calculating this matroid's Boolean base-indicator spectrum. Separately published results on uniform dyadic nonvanishing for Steiner triple systems of point orders congruent to five or seven modulo eight do not cover the present nine-point order; results on cubic sampling of all labelled affine planes concern a different signal space and observation operator. An indexed pointwise Fourier formula for the containing thirteen-point projective plane can also yield the affine-plane signed multipliers by averaging over the four deleted point coordinates; the signed-spectrum computation is therefore not presented as logically independent of every broader projective calculation. The additional extremal assertion here is the explicitly evaluated range-projection kernel and its sharp norm among arbitrary endpoint projections. These comparisons are not claims of comprehensive historical uniqueness.

## Limitations

The theorem is for the fixed nine-point affine geometry only. It does not classify all Steiner triple systems or all ternary matroids. A complete indexed Fourier formula for the containing projective plane can imply the affine signed spectrum after deletion and summation. The separately evaluated optimal endpoint projection constant is not explicitly established in the sources compared here. An earlier difficult-to-index signed-basis or projection calculation could still give the same finite result; historical priority is therefore not independently certified. The projection optimality is exact for the two endpoints \(\ell^1\) and \(\ell^\infty\), with no general formula asserted for other \(\ell^p\) operator norms. Independent validation has not been performed.

## References

1. C. Merino, M. Ramírez-Ibáñez, and G. Rodríguez-Sánchez, *The Tutte polynomial of some matroids*, arXiv:1203.0090v1, first publicly posted 2012-03-01. Especially Section 3.1 (affine planes), https://arxiv.org/abs/1203.0090 ; journal DOI https://doi.org/10.1155/2012/430859 .
2. A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1, first publicly posted 2008-06-30, especially Section 4, https://arxiv.org/abs/0806.4848 .
3. *Uniform dyadic nonvanishing for the Walsh transform of Steiner matroid bases*, publicly indexed mathematical finding (2026-11-16), identifier `1a9938b7ebb8`. Comparison is confined to its searchable summary because the complete document was not accessible during the comparison.
4. *Cubic Walsh recovery and the exact incidence-sampling spectrum of labelled affine planes of order three*, publicly indexed mathematical finding (2026-11-16), identifier `9b7d5d07cce1`. Comparison is confined to its searchable summary because the complete document was not accessible during the comparison.
