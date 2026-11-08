# The complete eventual Ehrhart sign spectrum at the minimal smooth facet threshold

## Finding

For every integer \(r\ge4\), consider
\[
Q_{r,c}=\left\{(x,z)\in\mathbb R^r\times\mathbb R:\ 0\le z\le1,\ x_i\ge0,\ \sum_{i=1}^{r}x_i\le1+cz\right\}
\]
with integer \(c\ge0\). This is a smooth lattice polytope of dimension \(d=r+1\), with \(d+2=r+3\) facets [1, Proposition 5.1]. Write its ordinary Ehrhart polynomial as
\[
L_{r,c}(t)=\sum_{k=0}^{r+1}e_k(r,c)t^k.
\]
There exists an integer \(c_0(r)\ge0\) such that, for every integer \(c\ge c_0(r)\), its **complete coefficient sign vector** is given by
\[
e_k(r,c)<0\quad\Longleftrightarrow\quad
 k=r+1-4m\ge1\ \text{or}\ k=r-4m\ge1,
\qquad m\in\mathbb Z_{\ge1}.
\]
Every coefficient not covered by the displayed criterion is strictly positive, including \(e_0=1\). The exact eventual number of negative coefficients is
\[
N_r=\left\lfloor\frac r4\right\rfloor+
\left\lfloor\frac{r-1}{4}\right\rfloor.
\]
For example, when \(r=5\) (dimension six), both the linear and quadratic coefficients are negative for all sufficiently large integer twists; at \(r=8\) (dimension nine), degrees one, four and five are negative. Thus the number of simultaneous negative coefficients becomes arbitrarily large even with the minimum possible facet count that permits an Ehrhart sign failure in dimensions at least five.

## Assumptions and scope

The lattice is the standard integer lattice in \(\mathbb R^{r+1}\). Here \(r\ge4\) and \(c\ge0\) are integers. Coefficients are in the ordinary monomial basis, **not** in the Ehrhart-series \(h^*\)-basis or the magic basis. The phrase "sufficiently large" means that, for each fixed \(r\), a finite integer \(c_0(r)\) exists simultaneously for all coefficients. The bounds need not be uniform in dimension. The facet-minimality comparison is the published classification in [1, Theorem 1.3], not a new theorem proved here.

## Proof

**1. Exact counting formula and polynomial dependence.** The slice at integral height \(j\) in \(tQ_{r,c}\) is a dilated standard \(r\)-simplex of size \(t+cj\). Hence [1, Proposition 5.1]
\[
L_{r,c}(t)=\sum_{j=0}^{t}\binom{t+cj+r}{r}.
\tag{1}
\]
For a positive integer \(n\), write \(S_n(t)=\sum_{j=0}^{t}j^n\). The power sums are polynomials in \(t\), and, with Bernoulli numbers normalized by \(B_1=-1/2\),
\[
S_n(t)=\frac1{n+1}\sum_{a=0}^{n}(-1)^a\binom{n+1}{a}B_a t^{n+1-a}.
\tag{2}
\]
The exceptional sum is \(S_0(t)=t+1\). Consequently every \(e_k(r,c)\) is a polynomial in the twist \(c\) over \(\mathbb Q\), with degree at most \(r\).

**2. Two leading powers of the twist.** Expanding the rising-factorial numerator of each binomial in (1) gives, coefficientwise in \(t\) and \(j\),
\[
\binom{t+cj+r}{r}=
\frac{c^rj^r}{r!}+
\frac{c^{r-1}j^{r-1}}{(r-1)!}\left(t+\frac{r+1}{2}\right)
+\mathcal O(c^{r-2}).
\]
Here \(\mathcal O(c^{r-2})\) denotes a *polynomial* in \(c\) whose coefficients, after summation over integral heights, have degree at most \(r-2\) in \(c\); it is not an analytic uniformity assertion in \(t\). Thus
\[
L_{r,c}(t)=\frac{c^r}{r!}S_r(t)+
\frac{c^{r-1}}{(r-1)!}\left(t+\frac{r+1}{2}\right)S_{r-1}(t)
+\mathcal O(c^{r-2}).
\tag{3}
\]
All subsequent coefficient asymptotics are for fixed \(r\) as \(c\) increases through integers.

**3. First sign tier.** For each integer \(h\ge1\) with \(k_+=r+1-2h\ge1\), equation (2) gives
\[
[t^{k_+}]S_r(t)=\frac{\binom{r+1}{2h}B_{2h}}{r+1},
\]
so equation (3) yields
\[
\boxed{e_{r+1-2h}(r,c)=
\frac{\binom{r+1}{2h}B_{2h}}{r!(r+1)}c^r+
\mathcal O_r(c^{r-1}).}
\tag{4}
\]
The leading coefficient is nonzero because every even-index Bernoulli number is nonzero.

**4. Canceled leading tier and its recovery.** For each integer \(h\ge1\) with \(k_-=r-2h\ge1\), the would-be \(c^r\) coefficient vanishes, since the coefficient of \(t^{r-2h}\) in \(S_r(t)\) is proportional to \(B_{2h+1}=0\). In the next tier, the \(tS_{r-1}\) contribution also vanishes because it has the same odd Bernoulli index; the \((r+1)S_{r-1}/2\) term contributes \(B_{2h}\). Thus
\[
\boxed{e_{r-2h}(r,c)=
\frac{(r+1)\binom r{2h}B_{2h}}{2r(r-1)!}c^{r-1}
+\mathcal O_r(c^{r-2}).}
\tag{5}
\]
Again the leading coefficient is strictly nonzero. This second tier is necessary for determining all signs: the first tier alone leaves roughly half the intermediate coefficients undecided.

**5. Boundary coefficients and complete signs.** From \(S_r(t)\), the coefficients in degrees \(r+1\) and \(r\) have respective leading terms \(c^r/(r!(r+1))\) and \(c^r/(2r!)\), so both are ultimately positive. The constant Ehrhart coefficient is exactly \(e_0(r,c)=1\). Every remaining degree \(1\le k\le r-1\) is uniquely of the form \(r+1-2h\) or \(r-2h\) with \(h\ge1\), and is covered by (4) or (5).

The classical identity \(B_{2h}=(-1)^{h+1}|B_{2h}|\) makes a tier negative exactly when \(h\) is even, equivalently \(h=2m\) for \(m\ge1\). Hence the negative degrees are precisely \(r+1-4m\) and \(r-4m\), provided they are positive. Their numbers are respectively \(\lfloor r/4\rfloor\) and \(\lfloor(r-1)/4\rfloor\). As each of finitely many coefficients has a nonzero leading twist coefficient, their signs stabilize simultaneously beyond one finite integer \(c_0(r)\). This proves the assertion.

## Verification

The supplied `verify_signs.py` uses exact rational arithmetic and the integer-height simplex counts (1), then interpolates the Ehrhart polynomial in the dilation parameter by Newton differences. This is a distinct computational route from extracting Bernoulli coefficients. It checks, for each \(r\) from 4 through 12, the predicted leading power of \(c\), both asymptotic coefficient formulas, the complete negative-degree sets, equality with direct integer-height lattice counts, and large-integer-twist signs. It also compares small instances with a recursive enumeration of lattice points. The run completed 518 exact checks, without any floating-point arithmetic. The finite test range only corroborates the infinite proof above.

## Relationship to prior work

Liu, Tang, Tao, and Zhang [1] introduced precisely the polytopes (1), proved smoothness and the minimum facet threshold, and showed that one fixed coefficient (degree \(r-3\)) is negative when \(c\) is large [1, Theorem 5.2]. Their displayed proof uses the first \(c^r\) tier. The present theorem gives the *entire eventual sign vector*, including the distinct \(c^{r-1}\) cancellation tier, and a dimension-dependent count growing without bound. Castillo, Liu, Nill, and Paffenholz [2] had already constructed smooth polytopes with many or all intermediate Ehrhart coefficients negative, but their construction does not provide this sign spectrum within the facet-minimal \(d+2\)-facet family. Ferroni [3] studies different Ehrhart numerator conditions and smooth Cayley sums, not these monomial sign vectors. No claim is made that having many negative coefficients is itself new.

## Limitations

The theorem identifies eventual signs, **not** exact smallest twist thresholds. It does not determine whether a different smooth polytope with \(d+2\) facets can have more than \(N_{d-1}\) negative coefficients, and it does not assert a sharp general bound on simultaneous negativity. Every proof step is symbolic; the verification script tests only finitely many dimensions. Literature searches cannot independently certify historical priority, and relevant equivalent descriptions might exist under other terminology. Independent mathematical audit has not been performed.

## References

[1] F. Liu, J. Tang, S. Tao, Z. Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819v1 (first publicly posted 2026-10-20), §§2, 5. https://arxiv.org/abs/2610.27819

[2] F. Castillo, F. Liu, B. Nill, A. Paffenholz, *Smooth polytopes with negative Ehrhart coefficients*, arXiv:1704.05532v4 (2018), Theorem 1.2. https://arxiv.org/abs/1704.05532

[3] L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v2 (2026). https://arxiv.org/abs/2609.10513
