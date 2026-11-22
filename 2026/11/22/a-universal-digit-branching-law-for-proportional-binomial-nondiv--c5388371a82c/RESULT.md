# A universal digit-branching law for proportional binomial nondivisibility

## Finding

Fix an **odd prime** \(p\) and an integer \(m\ge2\) satisfying \(p\nmid m(m-1)\). Set
\[
\mathcal A_{p,m}=\left\{n\in\mathbb Z_{\ge0}:p\nmid\binom{mn}{n}\right\},\qquad a_p=\frac{p+1}{2}.
\]
For every integer \(r\ge0\), the exact count is
\[
\boxed{\#(\mathcal A_{p,m}\cap[0,p^r))=a_p^r.}
\]
More precisely, for every \(s\ge0\), every integer \(0\le u<p^s\), and every \(r\ge0\),
\[
\boxed{\#\big\{0\le v<p^r:\ u+p^s v\in\mathcal A_{p,m}\big\}
=\mathbf1_{\{u\in\mathcal A_{p,m}\}}a_p^r.}
\]
Thus **every admissible base-\(p\) suffix has exactly \(a_p\) possible next digits**, regardless of the multiplier \(m\) and of the multiplication carry state. The admissible suffixes form a regular \(a_p\)-branching subtree of the rooted \(p\)-ary tree.

Let \(K_{p,m}\) be the closure of \(\mathcal A_{p,m}\) in \(\mathbb Z_p\). With the standard \(p\)-adic distance \(|x-y|_p=p^{-\nu_p(x-y)}\),
\[
\boxed{\dim_H K_{p,m}=\dim_B K_{p,m}=\delta_p:=\frac{\log((p+1)/2)}{\log p}.}
\]
Indeed, the canonical probability measure \(\mu_{p,m}\) on this tree satisfies the **exact cylinder law**
\[
\boxed{\mu_{p,m}(x+p^r\mathbb Z_p)=a_p^{-r}=p^{-r\delta_p}\quad
(x\in K_{p,m},\ r\ge0).}
\]
In particular \(\mu_{p,m}\) is \(\delta_p\)-Ahlfors regular, \(K_{p,m}\) has Haar measure zero, and its ordinary nonnegative-index counting function obeys \(\#(\mathcal A_{p,m}\cap[0,X))=\Theta_{p}(X^{\delta_p})\) for real \(X\ge1\). The exponent, exact prime-power count, and exact cylinder masses do not depend on the nonexceptional slope \(m\).

## Assumptions and scope

The prime \(p\) is odd, \(m\ge2\) is an arbitrary **fixed** positive integer satisfying \(m\not\equiv0,1\pmod p\), and \(r,s\) are arbitrary nonnegative integers. A suffix of length \(s\) is a residue class \(u\pmod{p^s}\), represented by \(0\le u<p^s\). The displayed suffix count does not assert equidistribution of the *values* of the binomial coefficient. For \(s=0\), the unique suffix is \(u=0\).

The restriction on \(m\) is essential: when \(p\mid m\), the only nondivisible index is \(n=0\), while \(m=p+1\) gives \(p\) admissible first digits, not \((p+1)/2\). No claim is made that all exceptional slopes behave alike.

## Proof

**1. A balanced affine-digit lemma.** Write \([t]_p\) for the representative of an integer \(t\) in \(\{0,1,\ldots,p-1\}\). Let \(b\in\mathbb Z\) satisfy \(b\not\equiv0,1\pmod p\). For any integer \(c\), define
\[
F_b(c)=\#\big\{d\in\{0,\ldots,p-1\}:d\le[bd+c]_p\big\}.
\]
We claim that
\[
\boxed{F_b(c)=(p+1)/2\quad\text{for every integer }c.}\tag{1}
\]
It is enough to consider \(c\pmod p\). As \(c\) increases to \(c+1\), an individual output \([bd+c]_p\) increases by one unless it is \(p-1\), in which case it wraps to zero. Thus a digit \(d\ge1\) enters the counted set exactly when \([bd+c]_p=d-1\); a digit \(d\ge1\) leaves exactly when \([bd+c]_p=p-1\). The first congruence has the unique solution
\[
(b-1)d\equiv-c-1\pmod p,
\]
and the second the unique solution
\[
bd\equiv-c-1\pmod p.
\]
Both solutions are \(d=0\) exactly when \(c\equiv-1\pmod p\). Otherwise both are nonzero, so there is exactly one entry and one exit. Consequently \(F_b(c+1)=F_b(c)\) for every \(c\), including the wrap-around case. To determine the constant, average over all \(p\) residues \(c\). For each fixed digit \(d\), the outputs \([bd+c]_p\) run through all \(p\) digits, of which exactly \(p-d\) satisfy \(d\le[bd+c]_p\). Therefore
\[
pF_b(c)=\sum_{d=0}^{p-1}(p-d)=\frac{p(p+1)}2,
\]
proving (1). In particular the count is independent of \(c\) even though the *set* of allowed digits generally varies with \(c\).

**2. Multiplication carries and Lucas's criterion.** Express \(n\ge0\) in base \(p\) as \(n=\sum_{i\ge0}d_ip^i\), with \(0\le d_i<p\) and all high digits zero. Multiplication by \(m\) is described from low digits upward by
\[
c_0=0,\qquad e_i=[m d_i+c_i]_p,\qquad c_{i+1}=\left\lfloor\frac{m d_i+c_i}{p}\right\rfloor.
\]
Here \(e_i\) is the digit of \(mn\) at position \(i\). Each carry \(c_i\) is a nonnegative integer, with no assumption that it is below \(p\). Once the digits of \(n\) end, its remaining digits are zero. Those higher positions automatically satisfy \(0\le e_i\), whatever carries remain; hence no extra terminal constraint is needed.

By Lucas's theorem, \(p\nmid\binom{mn}{n}\) exactly when \(d_i\le e_i\) at **every** position. By (1), from each carry state \(c_i\), exactly \(a_p\) digits \(d_i\) satisfy this inequality, because \(m\) is invertible and distinct from one modulo \(p\).

**3. Exact counts and suffix uniformity.** Starting from \(c_0=0\), every legal word of length \(s\) is an admissible suffix; and the next digit has exactly \(a_p\) legal choices, for every possible resulting carry state. Induction therefore yields \(a_p^r\) legal words of length \(r\), proving the first formula. If \(u\) is not legal, no extension can repair its first violating digit. If it is legal, the same induction from its terminal multiplication carry shows that exactly \(a_p^r\) length-\(r\) extensions exist. Trailing zeros in a finite extension cause no violation at higher positions, by Step 2. This proves the suffix formula in full, including \(r=0\) and \(s=0\).

**4. Counting-growth bounds.** Put \(A(X)=\#(\mathcal A_{p,m}\cap[0,X))\) and \(\delta_p=\log_p a_p\). If \(p^r\le X<p^{r+1}\), then
\[
a_p^r\le A(X)\le a_p^{r+1},\qquad a_p^r\le X^{\delta_p}<a_p^{r+1}.
\]
Consequently \(a_p^{-1}X^{\delta_p}\le A(X)\le a_p X^{\delta_p}\). Since \(a_p<p\), ordinary natural density is zero. No limiting leading coefficient is asserted for arbitrary \(X\).

**5. Closure, measure, and dimensions.** An infinite base-\(p\) digit word belongs to \(K_{p,m}\) exactly when every finite initial suffix satisfies Lucas's digit inequalities. Each such prefix has a finite nonnegative integer representative obtained by setting all later digits to zero. The exact branching law shows that precisely \(a_p^r\) cylinders of radius \(p^{-r}\) meet \(K_{p,m}\), proving its upper box dimension and an upper bound \(\log_p a_p\) on Hausdorff dimension. Assign each legal cylinder at depth \(r\) mass \(a_p^{-r}\). The assignments are consistent because every legal cylinder has exactly \(a_p\) legal children. They define a probability measure \(\mu_{p,m}\) with the displayed exact cylinder law. Since every \(p\)-adic ball is such a cylinder, the mass-distribution principle gives the matching Hausdorff lower bound, and the uniform cylinder law gives \(\delta_p\)-Ahlfors regularity. The box dimensions agree because the number of nonempty radius-\(p^{-r}\) balls is exactly \(a_p^r\). The normalized Haar measure of \(K_{p,m}\) is at most \(a_p^r p^{-r}\to0\).

**6. Boundary checks.** If \(p\mid m\) and \(n>0\), at the least nonzero base-\(p\) digit of \(n\), the corresponding digit of \(mn\) is zero, forcing divisibility. For \(m=p+1\), the first multiplication digit agrees with the first digit of \(n\), so all \(p\) one-digit indices are admissible. These examples show why neither excluded residue class of \(m\) can simply be absorbed into the universal formula.

## Verification

The accompanying standalone `verify.py`, requiring only Python's standard library, checks the following independently of the textual proof: the balanced-digit lemma for every carry \(0\le c<m\) and many eligible primes/multipliers; the exact length-\(r\) and prescribed-suffix counts; the digit criterion against direct Lucas digit comparisons; direct full integer binomial divisibility for small instances; and both excluded multiplier boundary behaviors. Run `python3 verify.py` in the extracted directory. The expected output is `VERIFY_OK 14130 exact assertions`. Finite computations alone do not certify the infinite formulas: those follow from Steps 1–5.

## Relationship to prior work

Lucas's classical digit congruence (1878) is the divisibility criterion in Step 2, not a new assertion. Fine's row-wise nonzero coefficient formula (1947) counts all choices of lower index within a fixed Pascal row, whereas the present problem fixes the **slope** \(\binom{mn}{n}\) and varies \(n\). Barat and Grabner (published online January 30, 2002) studied distributions of binomial coefficients and digital functions over the two-dimensional Pascal triangle, not the exact number in each affine multiplier-digit carry state. Rowland (arXiv initial January 12, 2010) extended the row-wise nonzero-counting problem to prime powers. Their methods make digit automata natural but do not state the balanced affine-digit lemma (1) or the resulting multiplier-independent exact suffix law.

More recent studies of spatial equidistribution of Pascal-triangle entries describe a two-dimensional gasket, not a fixed proportional line with its atypically uniform branching. Abram and Lagarias provide a general spectral-radius formula for dimensions of p-adic path-set fractals, which applies once a digit automaton is known; they do not establish the affine-digit balancing identity (1) that evaluates the spectral radius as the same number for every eligible binomial slope. Closest directly comparable results on prescribed central-binomial index suffixes classify possible coefficient **values**, rather than counting **indices** on every proportional binomial ray. A published treatment of the exceptional \(m=p+1\) Fuss–Catalan line uses the different adjacency constraint \(d_i+d_{i+1}\le p-1\) and has a different nonintegral growth eigenvalue; it does not cover the generic case here.

## Limitations

The theorem applies only to odd primes and multipliers \(m\not\equiv0,1\pmod p\). It does not determine nonzero coefficient residues, the \(p\)-adic valuation distribution beyond zero valuation, or leading asymptotic constants at arbitrary cutoffs. The uniform branching law is an exact arithmetic result, but an earlier implicit equivalent hidden in broader Lucas/digital-function literature remains possible. Originality is assessed from the identified sources, not guaranteed solely by unsuccessful searches. Independent validation has not been performed.

## References

1. É. Lucas, *Sur les congruences des nombres eulériens et les coefficients différentiels des fonctions trigonométriques suivant un module premier*, 1878. Classical Lucas congruence, as cited in Rowland [4].
2. N. J. Fine, *Binomial coefficients modulo a prime*, 1947. Classical nonzero row-count result, cited in Rowland [4].
3. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, *Journal of the London Mathematical Society* 64 (2001), 523–547, DOI https://doi.org/10.1112/S0024610701002630, publisher's first online display January 30, 2002. Lawful author preprint: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
4. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783, https://arxiv.org/abs/1001.1783 (initially submitted January 12, 2010).
5. R. Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878–2014)*, arXiv:1409.3820, https://arxiv.org/abs/1409.3820.
6. G. Barat and P. J. Grabner, *Spatial Equidistribution of Binomial Coefficients Modulo Prime Powers*, DOI https://doi.org/10.1515/udt-2016-0017; author preprint: https://www.applied.math.tugraz.at/~grabner/Publications/Binomial-spatial.pdf (a later comparison, not the age-defining source).
7. *Prime-relative Fuss–Catalan nondivisibility: exact spectra and p-adic dimension*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-prime-relative-fuss-catalan-nondivisibility-exact-spectra-and-p--fca5ba9f3d60 (exceptional-slope comparison).
8. *The full odd-prime p-adic index–value closure of central binomial coefficients*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-full-odd-prime-p-adic-index-value-closure-of-central-binomia--c0f80e993a75 (different index–value image question).
9. W. C. Abram and J. C. Lagarias, *p-adic path set fractals and arithmetic*, arXiv:1210.2478 (initial public submission October 9, 2012), https://arxiv.org/abs/1210.2478.
