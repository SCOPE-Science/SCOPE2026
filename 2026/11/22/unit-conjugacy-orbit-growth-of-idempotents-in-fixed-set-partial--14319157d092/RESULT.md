# Unit-conjugacy orbit growth of idempotents in fixed-set partial transformation monoids

## Finding

Let \(X=Y\sqcup Z\) be a finite set with \(|Y|=a\ge0\) and \(|Z|=b\ge0\). Define \(P\!\operatorname{Fix}(X,Y)\) as the monoid of partial maps \(f:X\rightharpoonup X\) such that \(f(y)=y\) whenever \(y\in Y\) is in the domain of \(f\). Its unit group is the symmetric group on \(Z\), acting trivially on \(Y\). The following statements hold for every pair of nonnegative integers \((a,b)\).

**Complete orbit and stabilizer classification.** Every composition-idempotent is uniquely specified, up to conjugation by units, by a subset \(J\subseteq Y\), nonnegative integers \((\ell_y:y\in J)\), a nonnegative integer \(h\), and a finite sequence \((t_m:m\ge1)\) of nonnegative integers, subject to
\[
 b=h+\sum_{y\in J}\ell_y+\sum_{m\ge1}m t_m.
\]
Its image rank is \(r=|J|+\sum_{m\ge1}t_m\); the order of its unit stabilizer is
\[
 h!\prod_{y\in J}\ell_y!\prod_{m\ge1}\bigl((m-1)!\bigr)^{t_m}t_m!,
\]
and its conjugacy orbit has size \(b!\) divided by that quantity.

**Rank-refined orbit enumeration.** If \(c_{a,b,r}\) is the number of unit-conjugacy orbits of idempotents of image rank \(r\), then as a formal power series in \(z\), with coefficients polynomial in \(u\),
\[
 \boxed{\sum_{b\ge0}\sum_{r\ge0}c_{a,b,r}z^b u^r
 =\frac{1}{1-z}\left(1+\frac{u}{1-z}\right)^a\prod_{m\ge1}\frac{1}{1-u z^m}.}
\]
For comparison, the number \(e_{a,b,r}\) of *labeled* idempotents of rank \(r\) satisfies
\[
 \boxed{e_{a,b,r}=\sum_{j=\max(0,r-b)}^{\min(a,r)}
 {a\choose j}{b\choose r-j}(r+1)^{b-r+j},}
\]
and its exponential generating function, in the number of elements of \(Z\), is
\[
 \sum_{b\ge0}\sum_{r\ge0}e_{a,b,r}\frac{z^b}{b!}u^r
 =e^z(1+u e^z)^a\exp(u z e^z).
\]

**Fixed-set orbit asymptotics.** Let \(c_{a,b}=\sum_r c_{a,b,r}\) and let \(p(b)\) denote the number of integer partitions of \(b\), with \(p(0)=1\). For each *fixed* nonnegative integer \(a\), as \(b\to\infty\),
\[
 \boxed{c_{a,b}\sim p(b)\left(\frac{\sqrt{6b}}{\pi}\right)^{a+1}.}
\]
For a uniformly sampled unit-conjugacy orbit of such idempotents, the probability that exactly \(k\) prescribed-set points are *not* in its domain, for \(0\le k\le a\), is asymptotic to
\[
 \boxed{{a\choose k}\left(\frac{\pi}{\sqrt{6b}}\right)^k}
\]
when \(k\) is fixed and \(a\) is fixed. In particular, if \(a\ge1\), the probability of omitting at least one point of \(Y\) is asymptotic to \(a\pi/\sqrt{6b}\), so almost all **unlabeled** idempotent classes define every distinguished point. The statement about exactly zero omitted points is interpreted as probability tending to one.

## Assumptions and scope

A partial map may have empty domain. The empty map is the zero element. Composition is usual composition of partial maps. An idempotent satisfies \(f\circ f=f\) as partial maps, including equality of domains. Unit-conjugacy means \(g f g^{-1}\) with \(g\) a unit of the monoid; it is **not** any other semigroup conjugacy relation, and is not conjugation by arbitrary permutations of \(X\). The points of \(Y\) are individually fixed by all units. A root of a partial idempotent is any point of its image, and every root is fixed by that idempotent.

The classifications and generating functions are exact for all \(a,b\ge0\). Only the asymptotic assertions require \(a\) fixed and \(b\to\infty\); they do not assert uniformity for growing \(a\). No assertion about the abstract automorphism group of the entire monoid is needed.

## Proof

### 1. Unit group and rooted-star normal form

A unit has a total inverse, so is a permutation of \(X\); the fixed-set condition forces it to fix every element of \(Y\), and its restriction to \(Z\) may be any permutation. Thus the unit group is \(\operatorname{Sym}(Z)\).

For an idempotent partial map \(f\), the image is contained in its domain and each image point is fixed: if \(s=f(x)\), then \(f(s)=f(f(x))=f(x)=s\). Conversely, a partial map with every image point in its domain and fixed is idempotent. Put \(J=\operatorname{im}(f)\cap Y\). Each \(y\in J\) has a rooted star of \(\ell_y\) distinct points of \(Z\) mapped to it. Every remaining root belongs to \(Z\), with a rooted star of size \(m\ge1\), counting the root itself; write \(t_m\) for the number of these rooted stars of size \(m\). Finally, exactly \(h\) elements of \(Z\) are outside the domain. These pieces partition \(Z\), giving the required equation for \(b\) and the rank formula. The distinguished points not in \(J\) have undefined image and cannot be targets of any arrow, because every target must be a fixed image point.

Every permutation of \(Z\) preserving the resulting partial map must separately permute the \(h\) undefined points, the \(\ell_y\) leaves over each individually named \(y\), the \(m-1\) leaves in each size-\(m\) free-root star, and the \(t_m\) indistinguishable size-\(m\) free-root stars. Conversely these permutations always commute with \(f\). This proves the stabilizer product, and orbit-stabilizer yields the orbit size. Two maps with identical displayed data can be matched by a permutation of \(Z\); distinct data are invariant under every such permutation. Thus the classification is both necessary and sufficient.

### 2. Ordinary and exponential generating functions

For each distinguished point \(y\in Y\), either it is not in the domain (contribution \(1\)) or it is a fixed root with an arbitrary nonnegative number of *unlabeled* free-point leaves (contribution \(u/(1-z)\)). The undefined free points contribute \(1/(1-z)\). Unlabeled multisets of free-root stars contribute \(\prod_{m\ge1}(1-u z^m)^{-1}\), because a star of size \(m\) contributes \(u z^m\). Multiplying these independent factors proves the rank-refined ordinary generating function. In any coefficient of \(z^b\) only factors with \(m\le b\) matter.

For the labeled count, choose \(j\) of the \(a\) distinguished points as fixed roots, and choose \(r-j\) of the \(b\) free points as fixed roots. Each of the remaining \(b-r+j\) free points is either outside the domain or maps to one of the \(r\) chosen roots, hence has exactly \(r+1\) choices, independently. This yields the stated finite sum. Alternatively, on labeled free points, an undefined singleton contributes \(e^z\), each distinguished point contributes \(1+u e^z\), and a set of rooted free stars contributes \(\exp(u z e^z)\), giving the labeled exponential generating function.

### 3. Partition asymptotics

Set \(P(z)=\prod_{m\ge1}(1-z^m)^{-1}=\sum_{b\ge0}p(b)z^b\). Specializing the orbit series to \(u=1\) gives
\[
 \sum_{b\ge0}c_{a,b}z^b
 =P(z)\frac{(2-z)^a}{(1-z)^{a+1}}
 =P(z)\sum_{j=0}^a {a\choose j}(1-z)^{-(a+1-j)}.
\]
For any fixed positive integer \(s\), put \(G_{s,b}=[z^b]P(z)(1-z)^{-s}\). The classical Hardy–Ramanujan partition asymptotic, \(p(b)\sim (4\sqrt3\,b)^{-1}\exp(\pi\sqrt{2b/3})\), implies
\[
 \frac{G_{s,b}}{p(b)}\sim\left(\frac{\sqrt{6b}}{\pi}\right)^s.
\]
Here is a direct coefficient argument for that transfer. Expanding the pole gives \(G_{s,b}=\sum_{j=0}^b {j+s-1\choose s-1}p(b-j)\). For \(j=O(\sqrt b)\), the partition asymptotic gives uniformly \(p(b-j)/p(b)=\exp(-\pi j/\sqrt{6b})(1+o(1))\). The remaining terms are negligible after first restricting to \(j\le b/2\) and using exponential upper bounds of the form \(C\exp(-c j/\sqrt b)\), then bounding \(j>b/2\) by the exponentially small ratio \(p(\lfloor b/2\rfloor)/p(b)\) times a polynomial. The resulting Riemann sum is \((s-1)!^{-1}\int_0^\infty x^{s-1}e^{-x}\,dx=1\) after scaling by \((\sqrt{6b}/\pi)^s\). In the finite expansion for \(c_{a,b}\), the term with \(s=a+1\) dominates all others by powers of \(b^{1/2}\), establishing the class-count asymptotic.

For exactly \(k\) missing distinguished points, choose them in \({a\choose k}\) ways; the remaining \(a-k\) distinguished roots each carry arbitrary leaves, and the undefined free points contribute an additional pole. The corresponding series is \({a\choose k}P(z)(1-z)^{-(a-k+1)}\). Taking the ratio of its \(z^b\)-coefficient to \(c_{a,b}\) proves the stated asymptotic. Summing the terms with \(k\ge1\), the \(k=1\) term dominates, yielding the probability of omitting at least one distinguished point.

## Verification

The standalone program `scripts/check.py` independently enumerates every partial map satisfying the fixed-set rule, filters by the equation \(f\circ f=f\), computes its root-star signature, and directly constructs actual conjugacy orbits under every permutation of \(Z\). It compares each orbit size, each rank count, and each coefficient of the rank-unrefined generating series to the stated formulas for \(0\le a\le3\) and \(0\le b\le4\). The final output line is `FIXED_POINT_PARTIAL_RETRACTION_ORBITS_VERIFIED`. It uses Python standard-library modules only. This exhaustive check covers the stated finite parameter ranges, not the infinite theorem; the proof above supplies the latter.

## Relationship to prior work

Wijarajak and Chaiya established Green relations and regularity of the partial fixed-point-set monoid in 2022 and abundance, unit regularity, and coregularity in 2023. The latter open-access paper identifies the unit group and describes idempotent representatives, but does not state the rank-refined unit-conjugacy orbit series or fixed-distinguished-set orbit asymptotics. Earlier work of Chaiya, Honyam, and Sanwong concerns the *full* transformation monoid fixing the prescribed set and its natural partial order; it does not treat partial-map orbit enumeration.

Araújo, Bentz, Kinyon, Konieczny, Malheiro, and Mercier show that permutation conjugacy in a finite partial transformation monoid can be recognized by functional-digraph isomorphism; the rooted-star invariants in the present classification are a colored specialization of that general principle, **not** a new general conjugacy criterion. The exact simultaneous rank/orbit/stabilizer formulas and the fixed-set partition asymptotics are the specific additions assessed here. Classical integer-partition asymptotics are used as a known input.

## Limitations

The results concern conjugation by the **unit group**, not semigroup natural conjugacy or conjugation by all permutations of \(X\). They classify only idempotents, not arbitrary partial transformations. Asymptotics require fixed \(a\). An earlier 2022 paper on this precise monoid was available only through abstract-level access during comparison, so an uninspected statement might still overlap with an exact enumeration; historical priority is therefore provisional. The general digraph-isomorphism criterion already covers the non-numerical skeleton of the classification. The verification program is finite and is not an independent audit.

## References

1. R. Wijarajak and Y. Chaiya, *Green's relations and regularity on semigroups of partial transformations with fixed sets*, Communications in Algebra (online 22 April 2022). DOI: https://doi.org/10.1080/00927872.2022.2045606.
2. R. Wijarajak and Y. Chaiya, *A Note on the Abundance of Partial Transformation Semigroups with Fixed Point Sets*, Discussiones Mathematicae—General Algebra and Applications 43 (2023), 241–247. DOI: https://doi.org/10.7151/dmgaa.1438. Open text: https://bibliotekanauki.pl/articles/59445249.pdf.
3. Y. Chaiya, P. Honyam and J. Sanwong, *Natural Partial Orders on Transformation Semigroups with Fixed Sets*, International Journal of Mathematics and Mathematical Sciences (2016), article 2759090. DOI: https://doi.org/10.1155/2016/2759090.
4. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro and V. Mercier, *Conjugacy in Abstract Semigroups, Transformation and Diagram Monoids, and Conjugacy Growth*, arXiv:2301.04252 (initial submission 11 January 2023; later revisions). URL: https://arxiv.org/abs/2301.04252.
5. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, Proceedings of the London Mathematical Society, 1918 (classical partition asymptotic).
