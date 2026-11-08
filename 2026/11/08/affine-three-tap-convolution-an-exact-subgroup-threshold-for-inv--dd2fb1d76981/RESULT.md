# Affine three-tap convolution: an exact subgroup threshold for invertibility

## Finding
For every prime \(p\ge5\), let \(a\in\mathbb F_p^\times\) have multiplicative order \(m\ge3\), put \(H=\langle a\rangle\), and form the affine Frobenius group \(G=(\mathbb F_p,+)\rtimes H\). For every \(u\in\mathbb F_p^\times\) and \(b\in\mathbb F_p\), the unit-weight three-tap convolution
\[
(Tf)(g)=f(g)+f(g(u,1))+f(g(b,a))
\]
is invertible over \(\mathbb C\) **if and only if** \(-2\notin H\). Its exact complex nullity is
\[
\dim_{\mathbb C}\ker T=\begin{cases}p-1,&-2\in H,\\0,&-2\notin H.\end{cases}
\]
Thus no intermediate ranks occur: the rank equals \(pm-p+1\) or \(pm\). Equivalently, the singularity condition is \(\operatorname{ord}_p(-2)\mid m\). This dichotomy is independent of the two location parameters \(u\) and \(b\). In particular, the full affine group case \(m=p-1\) is always singular, but some proper affine subgroups yield invertible three-tap convolutions.

## Assumptions and scope
The group law is \((x,h)(y,k)=(x+hy,hk)\), for \(x,y\in\mathbb F_p\) and \(h,k\in H\). The operator acts on complex-valued functions on \(G\); it is **right** convolution by the distinct elements \((0,1),(u,1),(b,a)\). For \(m\ge3\), the elements are distinct and the support generates \(G\). The prime is odd, and the theorem makes no assertion for general finite rings, composite additive moduli, or arbitrary coefficient weights. Normalizing \(b=0\) and \(u=1\) below changes only the indexing of the regular representation and hence leaves rank and invertibility unchanged.

## Proof
**Step 1: normalize the support.** Conjugation by a translation \((t,1)\) sends \((b,a)\) to \((b+(1-a)t,a)\), while fixing \((u,1)\). Because \(a\ne1\), choose \(t\) so the first coordinate of the affine tap vanishes. Conjugating further by \((0,u^{-1})\) normalizes the translation tap to \((1,1)\), leaving the dilation \((0,a)\) unchanged. Inner automorphisms induce permutation similarities of regular convolution, so it suffices to use this normalized support. (The symbol \((0,u^{-1})\) refers to an automorphism of the ambient affine group; if \(u^{-1}\notin H\), this is nevertheless an automorphism of \(G\), not necessarily an inner automorphism of \(G\). A pullback by any group automorphism preserves matrix rank.)

**Step 2: Fourier blocks.** The finite Frobenius group has exactly \(m\) one-dimensional representations, each trivial on translations. On each, the multiplier is \(2+\chi(a)\), nonzero since \(|\chi(a)|=1\). The other irreducibles are indexed by the \((p-1)/m\) multiplicative \(H\)-orbits of nonzero additive frequencies. Every such representation has dimension \(m\). Writing \(\zeta=\exp(2\pi i/p)\) and choosing a frequency representative \(k\ne0\), its convolution block is (up to the orientation of a cyclic shift)
\[
B_k=\operatorname{diag}_{h\in H}(1+\zeta^{kh})+P,
\]
where \(P\) is a permutation matrix of one cycle of length \(m\). Since all the diagonal entries are nonzero,
\[
\det B_k=\prod_{h\in H}(1+\zeta^{kh})+(-1)^{m-1}.
\]
Moreover, solving the cyclic one-term recurrence in the nullspace shows that \(\dim\ker B_k\le1\); it is exactly one if and only if
\[
\prod_{h\in H}(1+\zeta^{kh})=(-1)^m.\tag{1}
\]

**Step 3: necessity of the arithmetic condition.** Equality (1) is an algebraic-integer identity. Reducing it modulo the cyclotomic prime ideal \((1-\zeta)\) in \(\mathbb Z[\zeta]\), whose residue field is \(\mathbb F_p\), gives \(2^m\equiv(-1)^m\pmod p\), or \((-2)^m=1\) in \(\mathbb F_p^\times\). Because the latter multiplicative group is cyclic and \(H\) is its unique subgroup of order \(m\), necessarily \(-2\in H\).

**Step 4: sufficiency.** If \(-2\in H\), then \(2H=-H\). For all \(h\in H\), \(1+\zeta^{kh}=(1-\zeta^{2kh})/(1-\zeta^{kh})\). Consequently,
\[
\prod_{h\in H}(1+\zeta^{kh})
=\frac{\prod_{h\in H}(1-\zeta^{-kh})}{\prod_{h\in H}(1-\zeta^{kh})}
=(-1)^m\zeta^{-k\sum_{h\in H}h}=(-1)^m.
\]
The last step uses \(\sum_{h\in H}h=0\) in \(\mathbb F_p\), since \(m>1\). Thus every nontrivial induced block has nullity exactly one. If \(-2\notin H\), the necessity argument shows no such block is singular.

**Step 5: regular-representation multiplicities.** Each irreducible representation of dimension \(d\) appears \(d\) times in the regular representation. The one-dimensional blocks are invertible. If (1) holds, the \((p-1)/m\) distinct \(m\)-dimensional blocks each have one zero mode and repeat \(m\) times, yielding total nullity \(((p-1)/m)m=p-1\). Otherwise the total nullity is zero. The total group dimension is \(|G|=pm\), establishing both possible ranks. This completes the proof.

## Verification
The independent-of-parameters algebraic criterion follows from the proof, not from finite experiments. The accompanying dependency-free script `check_affine.py` evaluates the cyclotomic determinant condition using exact integer cyclic convolutions and checks regular-representation ranks by exact elimination over a finite prime field in bounded examples. Its recorded output is `AFFINE_THREE_TAP_CHECKS_PASS cyclotomic_orbits=281 modular_rank_cases=72`. The finite checks involve \(p\in\{5,7,11,13,17,19,23,31\}\) and do not certify infinitely many cases; the ring-theoretic argument above does.

## Relationship to prior work
The nonabelian Fourier decomposition and the algebraic Gauss/cyclotomic congruence used here are standard tools. Lindenstrauss–Varjú investigate spectral gaps for affine transformation groups, but their theorem does not give this exact three-tap rank dichotomy. Bell–Minei and Minei–Skogman study affine graph spectra and block diagonalization for other generating sets, particularly undirected and inverse-closed operators. Known three-tap classification on an elementary generalized-dihedral group addresses a complement of order two; the present result is restricted to higher-order complements and is not obtained by substituting parameters into that classification. No claim is made that the general representation method is new.

## Limitations
The statement concerns algebraic invertibility and complex nullity only, not a sharp condition number, full singular-value distribution, quantitative mixing, or spectral gap. It requires an odd prime and a cyclic complement of order at least three. A broader historical nonnormal affine Cayley-operator classification may contain this consequence: the full Bell–Minei 2006 article could not be inspected from the available open or institutional routes, so historical priority remains unresolved. Independent mathematical validation has not been performed.

## References
1. E. Lindenstrauss and P. P. Varjú, *Spectral gap in the group of affine transformations over prime fields*, arXiv:1409.3564v1 (first public September 11, 2014), https://arxiv.org/abs/1409.3564 .
2. D. Bell and E. Minei, *Spectral analysis of the affine graph over the finite ring*, Linear Algebra and its Applications 414 (2006), 244–265; https://doi.org/10.1016/j.laa.2005.09.020 . Full text not inspected.
3. E. Minei and E. Skogman, *Block Diagonalization Method for the Covering Graph*, Ars Combinatoria 92 (2009), 321–352; https://combinatorialpress.com/article/ars/Volume%20092/volume-92-paper-23.pdf .
