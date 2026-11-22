# Sharp all-exponent Fourier synthesis on unequal finite-abelian coordinate crosses

## Finding
Let \(A\) and \(B\) be finite abelian groups of orders \(m,n\ge 2\), with identities denoted by \(0\). On \(G=A\times B\) let
\[
S=(A\times\{0\})\cup(\{0\}\times B).
\]
For every real \(1<r<\infty\), define the normalized Fourier transform on \(G\) by
\[
\widehat f(\chi,\psi)=\frac1{\sqrt{mn}}\sum_{(x,y)\in G}f(x,y)\overline{\chi(x)\psi(y)},
\quad (\chi,\psi)\in\widehat A\times\widehat B.
\]
All norms on finite sets use counting measure. The sharp synthesis ratio for nonzero functions supported in \(S\) is
\[
\boxed{\mathcal C_r(S):=\sup_{\substack{0\ne f:G\to\mathbb C\\\operatorname{supp}f\subseteq S}}
\frac{\|\widehat f\|_\infty}{\|\widehat f\|_r}
=\left(1+\frac{(m-1)(n-1)}{\bigl(1+(m-1)^{1/(r-1)}+(n-1)^{1/(r-1)}\bigr)^{r-1}}\right)^{-1/r}.}
\]
Put \(\alpha=(m-1)^{1/(r-1)}\), \(\beta=(n-1)^{1/(r-1)}\), and \(D=1+\alpha+\beta\). All nonzero complex extremizers, and only those, arise by multiplying the following function by a nonzero scalar and by an arbitrary product character of \(G\):
\[
\begin{aligned}
 f(0,0)&=\frac{m+n-mn+n\alpha+m\beta}{mnD},\\
 f(x,0)&=\frac{1+\alpha}{mD}\quad(x\in A\setminus\{0\}),\\
 f(0,y)&=\frac{1+\beta}{nD}\quad(y\in B\setminus\{0\}),\\
 f(x,y)&=0\quad(x\ne0,\ y\ne0).
\end{aligned}
\]
There is also a sharp **sign-transition classification**. If \((m-2)(n-2)\le 4\), the distinguished intersection coefficient is positive at every finite \(r>1\). If \((m-2)(n-2)>4\), it changes from positive to negative at exactly one exponent \(r_*>2\), defined uniquely by
\[
n(m-1)^{1/(r_*-1)}+m(n-1)^{1/(r_*-1)}=mn-m-n.
\]
At \(r=r_*\) it is zero, although both arms remain nonzero. For equal orders \(m=n=q\ge5\),
\[
r_*=1+\frac{\log(q-1)}{\log((q-2)/2)}.
\]

## Assumptions and scope
Both factors can be any finite abelian groups, not necessarily cyclic, isomorphic, or of equal order. Their nonidentity dual indices have multiplicities \(m-1\) and \(n-1\). The origin is counted once in the support. The theorem applies to every real exponent strictly between one and infinity; its uniqueness assertion does not include the endpoint exponents. A character modulation means \(f(x,y)\mapsto\chi_0(x)\psi_0(y)f(x,y)\). The unitary Fourier factor cancels between the numerator and denominator, while counting-measure norms must be retained on both sides of the ratio.

## Proof
**Step 1: Fourier image of the cross.** Strip the common Fourier normalization and write \(F=\sqrt{mn}\widehat f\). A function has support in \(S\) if and only if its Fourier array is additive:
\[
F(\chi,\psi)=u(\chi)+v(\psi).
\]
Indeed, each of the two axis contributions depends on only its corresponding dual variable; conversely, every such sum has inverse transform supported on the two axes. The redundancy from splitting the intersection coefficient does not affect this characterization.

For nonzero \(f\), the maximum \(\|F\|_\infty\) is positive. Modulation translates a maximizing dual index to the trivial-character pair, and complex rescaling makes \(F(1,1)=1\). Therefore the reciprocal of the sharp ratio is the minimum of \(\|F\|_r\) over additive arrays satisfying this one affine constraint.

**Step 2: Symmetry and unique minimizer.** The objective \(\sum_{\chi,\psi}|F(\chi,\psi)|^r\) is strictly convex for \(r>1\), and is coercive on this finite-dimensional affine subspace; hence a unique minimizer exists. Independently permuting the \(m-1\) nontrivial characters of \(A\) and the \(n-1\) nontrivial characters of \(B\) preserves the additive subspace and the value at \((1,1)\). Uniqueness forces the minimizer to be constant on the four corresponding Cartesian blocks. Complex conjugation also preserves the constraints and objective, so these block values are real.

Let \(a\) be the value at \((1,\psi)\) for \(\psi\ne1\), and \(b\) at \((\chi,1)\) for \(\chi\ne1\). Additivity forces the value at \((\chi,\psi)\), for both nontrivial, to be \(t=a+b-1\). Thus the entire problem reduces, without relaxation, to the strictly convex real function
\[
Q(a,b)=1+(n-1)|a|^r+(m-1)|b|^r+(m-1)(n-1)|a+b-1|^r.
\]

**Step 3: Exact minimization.** Set \(a=\alpha/D\), \(b=\beta/D\), and \(t=-1/D\). The relations \(\alpha^{r-1}=m-1\) and \(\beta^{r-1}=n-1\) imply
\[
\partial_aQ=r(n-1)\bigl(a^{r-1}-(m-1)(-t)^{r-1}\bigr)=0,
\]
\[
\partial_bQ=r(m-1)\bigl(b^{r-1}-(n-1)(-t)^{r-1}\bigr)=0.
\]
These derivatives exist also when \(1<r<2\), since \(a,b,-t\) are strictly positive. By strict convexity this is the unique global minimum. Substitution yields
\[
Q_{\min}=1+\frac{(m-1)(n-1)}{D^{r-1}}.
\]
Since every maximizer can be shifted and normalized as in Step 1, the displayed sharp synthesis constant and all normalized equality cases follow.

**Step 4: Inverting the four block values.** The inverse discrete Fourier transform of the four-block array \(F\), divided by \(mn\), gives the origin coefficient plus constant values on the two punctured axes. At \(x\ne0\), the character identity \(\sum_{\chi\ne1}\chi(x)=-1\) gives
\[
f(x,0)=\frac{1-b}{m}=\frac{1+\alpha}{mD}.
\]
Analogously \(f(0,y)=(1-a)/n=(1+\beta)/(nD)\) for \(y\ne0\). Because \(F(1,1)=\sum f=1\), the origin coefficient is
\[
1-(m-1)\frac{1+\alpha}{mD}-(n-1)\frac{1+\beta}{nD}
=\frac{m+n-mn+n\alpha+m\beta}{mnD}.
\]
Every off-axis coefficient vanishes, since the inverse transform of an additive Fourier array is supported on the axes. This also proves the stated exhaustive complex equality classification by reversing Step 1.

**Step 5: Sign transition.** Let \(H(r)=n\alpha+m\beta-(mn-m-n)\), the sign-controlling numerator. At \(r=2\), \(\alpha=m-1\) and \(\beta=n-1\), giving \(H(2)=mn>0\). For \(1<r<2\), both \(\alpha\ge m-1\) and \(\beta\ge n-1\), so the numerator is positive. If \(m=2\) or \(n=2\), the numerator remains positive directly. If both are greater than two, \(H(r)\) is strictly decreasing on \((2,\infty)\) with limit \(2m+2n-mn\), which is negative exactly when \((m-2)(n-2)>4\). Thus the claimed unique zero, endpoint classification, and strict signs follow by the intermediate value theorem. The equal-size expression follows by solving \(2q(q-1)^{1/(r_*-1)}=q(q-2)\).

The normalization check at \(r=2\) is \(\mathcal C_2(S)=\sqrt{(m+n-1)/(mn)}\), also immediate from Parseval. For \(m=n=q\) and fixed \(r>1\), the formula furthermore gives \(\mathcal C_r(S)\sim 2^{(r-1)/r}q^{-1/r}\) as \(q\to\infty\).

## Verification
Run `python artifacts/check_cross.py` from the directory containing this document using only the Python standard library. It produces `PASS: 4768 supplementary evaluations; all-p, all-group proof is analytic.` It checks the four predicted Fourier levels and their multiplicities, the sharp constant, the normalized coefficient sum, the Parseval case, random complex perturbations, and the sign transition. These are finite supplementary checks; the universal quantifiers and uniqueness rest entirely on the strict-convexity proof above.

## Relationship to prior work
Iosevich, Li and Yu (2026) obtain sharp spectral-synthesis bounds for supports whose affine symmetry acts transitively on support points. The finite coordinate cross has two or three natural point orbits (the intersection and each punctured arm), so that transitive criterion does not determine this sharp constant or equality family. Their broader setup motivates evaluating exact synthesis ratios on nontransitive supports. Bhowmik, Deodhar and Iosevich (2025) give general finite-group synthesis estimates but not the all-exponent rectangular-cross formula.

The publicly indexed results *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* (2026-10-11) and *The order-four endpoint for sharp fourth moments on finite abelian coordinate crosses* (2026-11-08) study the different map from coefficient \(\ell^2\) to Fourier \(L^4\), primarily with equal-size coordinate factors. Their one-axis extremizers and constants neither equal nor imply the present Fourier \(\ell^\infty/\ell^r\) minimization. Earlier exact fourth-power synthesis formulas for a two-axis finite-field cross and for line pencils arise as special cases at \(r=4\), when \(m=n=q\); the contribution here is arbitrary unequal finite-abelian factor orders, every real \(1<r<\infty\), and the complete critical-exponent transition. The novelty comparison is relative to the sources inspected, not an absolute claim that no older result is equivalent.

## Limitations
The result is finite-group, two-axis, and unweighted, with counting-measure Fourier norms. It does not treat arbitrary unions of subgroups with nontrivial intersections, weighted \(\ell^r\) norms, stability of near-extremizers, or the non-strictly-convex endpoints \(r=1,\infty\). Existing general Banach-space results on point evaluation in additive product subspaces might supply an equivalent formula; a complete historical equivalence search is not asserted. The proof is analytic; the numerical checker does not independently certify originality or the infinite family.

## References
1. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, first public 2026-09-21, arXiv:2609.25404, https://arxiv.org/abs/2609.25404.
2. P. Bhowmik, S. Deodhar, A. Iosevich, *On spectral synthesis in \(\mathbb Z_N^d\)*, first public 2025-08-17, arXiv:2508.12194, https://arxiv.org/abs/2508.12194.
3. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc/RESULT.md.
4. *The order-four endpoint for sharp fourth moments on finite abelian coordinate crosses*, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-order-four-endpoint-for-sharp-fourth-moments-on-finite-abeli--a9c611ea59b6/RESULT.md.
