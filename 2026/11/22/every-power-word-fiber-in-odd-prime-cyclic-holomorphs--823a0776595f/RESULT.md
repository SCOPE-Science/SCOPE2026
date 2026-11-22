# Every power-word fiber in odd-prime cyclic holomorphs

## Finding

Let \(p\) be an odd prime, \(m\geq1\) an integer, \(R=\mathbb Z/p^m\mathbb Z\), and \(G=R^+\rtimes R^\times=\operatorname{Hol}(C_{p^m})\), with multiplication \((b,u)(c,v)=(b+uc,uv)\). For **every** positive integer \(e\) and **every** target \((t,v)\in G\), the complete number of roots
\[
N_e(t,v)=|\{(b,u)\in G:(b,u)^e=(t,v)\}|
\]
is as follows. Write \(e=p^s c\) with \(p\nmid c\), and set
\[
h=\gcd(c,p-1),\quad r=(p-1)/h,\quad d=\min(s,m-1),\quad a=\min(s,m).
\]
Let \(\nu_m(x)\) denote the truncated \(p\)-adic valuation on \(R\), namely the largest \(j\in\{0,\ldots,m\}\) such that \(x\equiv0\pmod{p^j}\). For the target multiplier \(v\), define the two explicit power-membership conditions
\[
\tag{P}v^r\equiv1\pmod p,\qquad v^{p-1}\equiv1\pmod{p^{\min(m,s+1)}}.
\]
If (P) fails, then \(N_e(t,v)=0\). If (P) holds and \(v\not\equiv1\pmod p\), then
\[
\boxed{N_e(t,v)=h p^d\qquad\text{for every }t\in R.}
\]
If (P) holds and \(v\equiv1\pmod p\), put \(\ell=\nu_m(v-1)\) (so \(a\leq\ell\leq m\), and in fact \(\ell\geq\min(s+1,m)\)). Then
\[
\boxed{N_e(t,v)=p^{d+a}\mathbf1_{\{\nu_m(t)\geq a\}}+(h-1)p^{d+\ell}\mathbf1_{\{\nu_m(t)\geq\ell\}}.}
\]
These formulas also include the identity exponent \(e=1\) and exponents divisible by \(p^m\). Thus the complete power-map fiber depends on the exponent only through \(\gcd(e/p^{\nu_p(e)},p-1)\) and \(\min(\nu_p(e),m)\), and no two elements outside the stated target set are powers.

The exact number of distinct \(e\)-th powers is
\[
\boxed{|\{g^e:g\in G\}|=(r-1)p^{2m-1-d}+p^{2m-1-d-a}.}
\]
Its proportion in \(G\) is \(\big((r-1)p^{-d}+p^{-d-a}\big)/(p-1)\). For any fixed exponent \(e\), that proportion is independent of the modulus depth as soon as \(m>\nu_p(e)\).

**Tame-root concentration and terminal collapse.** For \(e=p-1\), the power image is the *entire* normal Sylow \(p\)-subgroup \(\{(t,v):v\equiv1\pmod p\}\), but the root multiplicities vary with \(\nu_m(v-1)\) and \(\nu_m(t)\). In particular, for its identity target \((0,1)\),
\[
N_{p-1}(0,1)=1+(p-2)p^m,
\]
whereas every other target \((t,1)\) with \(t\neq0\) has precisely one root. For \(m\geq2\), the image of the \((p-1)p^{m-1}\)-th power map is exactly the \(p\)-element translation subgroup \(p^{m-1}R\times\{1\}\); the next \(p\)-multiplication, exponent \((p-1)p^m\), reduces its image to the identity. These last two statements are sharp, with the first exponent the final nontrivial image and the second the exponent of \(G\).

## Assumptions and scope

The residue ring is \(R=\mathbb Z/p^m\mathbb Z\), **not** an arbitrary chain ring. The prime \(p\) is odd: the cyclic-unit-group description and valuation of the geometric sum below require this restriction. A target always has \(t\in R\) and unit \(v\in R^\times\); the identity target is \((0,1)\). All congruences use integer representatives modulo the specified powers of \(p\). The convention \(p^0=1\) applies even at \(s=0\); \(\nu_m(0)=m\). Exponents \(e\) are positive integers, with no upper bound. The smallest modulus \(m=1\) is covered, though the nonuniform chain-depth phenomena occur for \(m\geq2\).

## Proof

**Multiplier roots.** The unit group \(U=R^\times\) is cyclic of order \((p-1)p^{m-1}\), with canonical direct product of its prime-to-\(p\) torsion and the principal units \(1+pR\). The map \(u\mapsto u^e\) has a kernel of size \(hp^d\). Its image in the residue field \(\mathbb F_p^\times\) has order \(r=(p-1)/h\); hence the residue criterion for the target is \(v^r=1\pmod p\). Its image on principal units is \(1+p^{\min(m,s+1)}R\), since the factor \(c\) is prime to \(p\) and odd-prime principal units are cyclic of order \(p^{m-1}\). Raising a principal unit to \(p-1\) is an automorphism, so the second condition of (P) is equivalent to this image condition. Thus (P) is necessary and sufficient for the existence of multiplier roots. When it holds, there are exactly \(h\) distinct roots modulo \(p\), each with \(p^d\) lifts solving \(u^e=v\) in \(U\).

**Translation coefficient.** Direct induction in the semidirect product yields
\[
(b,u)^e=\left(b S_e(u),u^e\right),\qquad S_e(u)=1+u+\cdots+u^{e-1}.
\]
If \(v\not\equiv1\pmod p\), every multiplier root \(u\) differs from one modulo \(p\), and the exact identity \((u-1)S_e(u)=v-1\) shows that \(S_e(u)\) is a unit. Each of the \(hp^d\) multiplier roots therefore determines a unique translation \(b\) for every \(t\).

If \(v\equiv1\pmod p\), one of the \(h\) residue roots of \(u^e=v\) equals one. Each of its \(p^d\) lifts satisfies \(u\equiv1\pmod p\), and the odd-prime lifting-the-exponent identity
\[
\nu_m\big(1+u+\cdots+u^{e-1}\big)=\min(\nu_p(e),m)=a
\]
holds even for \(u=1\). Each such multiplier lift has exactly \(p^a\) solutions of \(bS_e(u)=t\) if \(\nu_m(t)\geq a\), otherwise none. The other \(h-1\) residue roots are not one; for any lift \(u\) of one of them, \(u-1\) is a unit, so the identity \((u-1)S_e(u)=v-1\) makes the coefficient have truncated valuation \(\ell=\nu_m(v-1)\). There are exactly \(p^\ell\) translation roots for each such \(u\) if and only if \(\nu_m(t)\geq\ell\). Summing disjoint cases gives the boxed target-fiber formula for every \(e,p,m\).

**Images.** The multiplier subgroup of \(e\)-th powers has exactly \(r p^{m-1-d}\) elements: precisely \((r-1)p^{m-1-d}\) have residue different from one and \(p^{m-1-d}\) have residue one. In the former class, every one of the \(p^m\) translations is attained; in the latter, precisely \(p^{m-a}\) translations, those divisible by \(p^a\), are attained. This proves the image formula and, after dividing by \(|G|=(p-1)p^{2m-1}\), the density formula.

For \(e=p-1\), one has \(s=0,h=p-1,r=1,d=a=0\); condition (P) is exactly \(v\equiv1\pmod p\). Thus all of the normal Sylow subgroup is the image. For \(v=1\), \(\ell=m\); the displayed root values at \((0,1)\) and \((t,1)\), \(t\neq0\), follow immediately. For \(e=(p-1)p^{m-1}\), the parameters are \(s=m-1,h=p-1,r=1,d=m-1,a=m-1\), and only \(v=1\), \(t\in p^{m-1}R\) appear. For \(e=(p-1)p^m\), \(a=m\) and only \((0,1)\) remains. The power map cannot become identically trivial earlier because \((1,1)\) has order \(p^m\) and a unit of order \(p-1\) embeds in \(G\), proving the exponent assertion.

## Verification

Run `python3 verify.py` from the directory containing the embedded checker. It directly multiplies affine transformations, forms the complete \(e\)-th power map, and checks **every target** against a separately implemented congruence-and-valuation prediction, including its image cardinality. Its fixed test grid uses \(p=3\) through \(m=4\), \(p=5\) through \(m=3\), and \(p=7,11\) through \(m=2\), with short exponents and both tame/principal large exponents. All 280 parameter cases passed; the exact parameter/output log is supplied as `verification_output.txt`. These finite checks test the implementation and boundary behavior, not the infinite quantifiers in the theorem; those are established by the preceding algebraic proof.

## Relationship to prior work

Kovács and Nedela (arXiv:1511.07252v1, 23 November 2015; primary MSC `20D15`) classify skew-morphisms of odd-prime cyclic groups and give an order lemma for split metacyclic \(p\)-groups (Lemma 4). That lemma supplies familiar order behavior of the principal \(p\)-part, but does not determine arbitrary target fibers for every exponent across the full holomorph. Becker's archival holomorph presentations (2006) and Deaconescu--Walls' conjugacy/orbit partition for cyclic holomorphs (2013) likewise concern different invariants. Pradhan--Sury (2021) treat irreducible representations of the same holomorph family; Spaggiari (2022) classifies regular subgroups and mutual normalizations. Neither inspected statement is a power-word root census. A general character formula could in principle be combined with detailed power-conjugacy data, but the existing representation results alone do not give the evaluated target-by-target valuation law.

Two nearby publicly available mathematical results provide especially useful boundaries: the finite-chain-ring affine-group conjugacy and character-table theorem (published-finding corpus, 2026/10/18, `0a4181d7ad6d`) fixes classes and ordinary representations, not the solutions of \(x^e=y\); the complete power-map fiber theorem for *radical-square-zero finite-field quiver unit groups* (published-finding corpus, 2026/10/25, `1c150d6b326e`) has a distinct square-zero coefficient algebra and does not cover the higher prime-power affine holomorphs in this theorem. The field-level \(m=1\) case is not asserted as the source of originality; the unrestricted \(m\ge2\) congruence-depth fibers and terminal jumps are the substantive part. Familiar general results about powerful or regular \(p\)-groups explain parts of the principal-Sylow power image, but do not yield the nonuniform contribution of the \(h-1\) nonprincipal residue roots in the full group without an additional analysis.

## Limitations

The theorem makes no assertion for \(p=2\), arbitrary finite chain rings, or noncyclic translation groups. It is an exact count for elements, not a classification of conjugacy classes of roots or a representation-theoretic inversion formula. The finite checker does not prove the general statement. An equivalent evaluation in unindexed historical metacyclic-group or word-map literature could exist, and no independent audit has been performed. The elementary semidirect-product and lifting ingredients are standard; originality concerns their all-exponent prescribed-target combination and resulting sharp image classification, not these ingredients in isolation.

## References

1. I. Kovács and R. Nedela, *Skew-morphisms of cyclic \(p\)-groups*, arXiv:1511.07252v1, first submitted 23 November 2015, especially Lemma 4 and Sections 1--4; https://arxiv.org/pdf/1511.07252 . Primary MSC2010: `20D15`.
2. W. Becker, *Some observations regarding the holomorphs of finite abelian groups*, arXiv:math/0609571v1, first submitted 20 September 2006; https://arxiv.org/pdf/math/0609571 .
3. M. Deaconescu and G. Walls, *The Y factor*, *Bull. Math. Soc. Sci. Math. Roumanie* **56** (2013), 331--334; https://ssmr.ro/bulletin/pdf/56-3/articol_6.pdf . Primary MSC2010: `20D60`.
4. S. S. Pradhan and B. Sury, *Rational and quasi-permutation representations of holomorph of cyclic \(p\)-groups*, arXiv:2106.12781v1, first submitted 24 June 2021; https://arxiv.org/pdf/2106.12781 .
5. F. Spaggiari, *The mutually normalizing regular subgroups of the holomorph of a cyclic group of prime power order*, arXiv:2203.09316v1, first submitted 17 March 2022; https://arxiv.org/abs/2203.09316 .
6. *Conjugacy and ordinary character spectra of affine groups over finite chain rings*, published-finding corpus (2026), record `2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d`; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d .
7. *Complete power-map fibers in radical-square-zero quiver unit groups*, published-finding corpus (2026), record `2026/10/25/SCOPE-complete-power-map-fibers-in-radical-square-zero-quiver-unit-gro--1c150d6b326e`; https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-power-map-fibers-in-radical-square-zero-quiver-unit-gro--1c150d6b326e .
