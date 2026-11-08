# A quadratic height census and exact Pareto tail for near-critical four-runner speeds

## Finding

For a finite set \(V\) of four distinct positive integers, put
\[
\operatorname{ML}(V)=\max_{t\in\mathbb R}\min_{v\in V}\operatorname{dist}(tv,\mathbb Z).
\]
A set is *primitive* when the greatest common divisor of its four entries is \(1\). For real \(H\geq1\), let \(\mathcal F_H\) be the collection of **unordered** primitive four-element sets \(V\subseteq\{1,\ldots,\lfloor H\rfloor\}\) with \(\operatorname{ML}(V)<1/4\), and write \(C(H)=|\mathcal F_H|\). Then
\[
\boxed{C(H)=\frac{H^2}{\pi^2}+O(H\log(2H)).}
\]
The corresponding proportion among all primitive four-element sets with maximum entry at most \(H\) is
\[
\boxed{\frac{4\pi^2}{15H^2}+o(H^{-2}).}
\]
Moreover, if a set is chosen uniformly from \(\mathcal F_H\) and
\[
Z_H=H\left(\frac14-\operatorname{ML}(V)\right),
\]
then \(Z_H\) converges in distribution to an explicitly defined continuous random variable \(Z\). Its tail has the **exact**, rather than merely asymptotic, form
\[
\boxed{\Pr\{Z>z\}=\frac1{24z^2}\qquad(z\geq\tfrac12).}
\]
In particular, its nonnegative real moments are finite exactly for orders \(s<2\). The entire limiting distribution is specified below as an eight-component pushforward of uniform area measure on a fixed triangle.

## Assumptions and scope

The mathematical input is the complete classification and exact value formulas in Theorem 1.1 and Lemma 8.5 of Yi--Gill--Bu, *Four runners that are barely lonely*, arXiv:2610.40694v1 (first publicly submitted 2026-10-28). We use that published theorem as a premise; the classification's extensive underlying finite search is **not independently reproduced** here. The new contributions are the height asymptotic, the normalized gap distribution, the exact tail and its moment threshold.

Let
\[
T=\{(u,v)\in\mathbb R_{>0}^2:u+2v<1\},\qquad |T|=\frac14.
\]
The eight permitted pairs of residues modulo \(4\) are
\[
\mathcal R=\{(0,1),(0,3),(1,0),(1,3),(2,1),(2,3),(3,0),(3,1)\}.
\]
For \(r\in\{1,2,3\}\) define linear forms
\[
A_r(u,v)=\begin{cases}(u+v)/2&r=1,\\(u+3v)/4&r=2,\\(u+3v)/2&r=3,\end{cases}
\]
\[
B_r(u,v)=\begin{cases}(2u+v)/2&r=1,\\(2u+3v)/4&r=2,\\(2u+3v)/2&r=3.\end{cases}
\]
For \((a,b)\in\mathcal R\), let \(r\) and \(s\) be the representatives in \(\{1,2,3\}\) of \(b-a\) and \(b-2a\) modulo \(4\), and set
\[
L_{a,b}(u,v)=\max\bigl(A_r(u,v),B_s(u,v)\bigr),\qquad
P_{a,b}=\{(u,v)\in\mathbb R_{\geq0}^2:L_{a,b}(u,v)\leq1\}.
\]
Choose \((A,B)\) uniformly from \(\mathcal R\), independently choose \((U,W)\) uniformly with respect to area on \(T\), and define
\[
\boxed{Z=\frac{1}{8L_{A,B}(U,W)}.}
\]
For every fixed \(z>0\), this also gives the finite-cutoff counting asymptotic
\[
\#\{V\in\mathcal F_H:Z_H>z\}
=\frac{H^2}{\pi^2}\Pr\{Z>z\}+O_z(H\log(2H)).
\]
Thus the law is specified for all positive \(z\), not only in its tail.

## Proof

**1. Classification and injectivity.** Yi--Gill--Bu's Theorem 1.1 says every primitive set with \(\operatorname{ML}<1/4\) is exactly one of: \(\{1,2,3,4k\}\) for an integer \(k\geq1\); \(\{x,y,x+y,x+2y\}\), where \(x,y\) are positive coprime integers satisfying \(y\not\equiv x,2x\pmod4\); or \(\{1,3,4,14\}\). Its only duplication is \(\{1,2,3,4\}\). The second family is injectively parameterized: its two smallest elements are \(x,y\), and interchanging them changes the largest element from \(x+2y\) to \(2x+y\) unless \(x=y\), a forbidden case. Hence its exact height restriction is \(x+2y\leq H\). The other families contribute \(O(H)\) sets.

**2. Local arithmetic density.** For a coprime pair \((x,y)\), the two exclusions modulo \(4\) select exactly the eight residue classes \(\mathcal R\). Each fixed class has, inside a bounded polygonal region \(H\Omega\subseteq\mathbb R_{>0}^2\), the count
\[
\frac{\operatorname{area}(\Omega)}{16}H^2
\sum_{\substack{d\geq1\\d\text{ odd}}}\frac{\mu(d)}{d^2}
+O_\Omega(H\log(2H))
=\frac{\operatorname{area}(\Omega)}{2\pi^2}H^2+O_\Omega(H\log(2H)).
\]
Indeed, apply \(\mathbf1_{\gcd(x,y)=1}=\sum_{d\mid x,y}\mu(d)\), noting that an even divisor cannot occur in an allowed residue class. For each odd \(d\), multiplication by its inverse modulo \(4\) identifies the appropriate unique residue class for the reduced pair. A translate of the lattice \(4\mathbb Z^2\) has \(\operatorname{area}(H\Omega)/16+O_\Omega(H+1)\) points in a fixed polygon. Summing the boundary errors for \(d\leq H\) costs \(O(H\log(2H))\); the omitted tail of the absolutely convergent main series costs \(O(H)\). Finally
\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}=\frac{\zeta(2)^{-1}}{1-2^{-2}}=\frac8{\pi^2}.
\]
With \(\Omega=T\), eight classes and area \(1/4\) yield the first boxed asymptotic. There are \(H^4/(24\zeta(4))+O(H^3)\) primitive unordered four-element subsets of \(\{1,\dots,\lfloor H\rfloor\}\), giving the second boxed formula.

**3. Scaled gap.** The source's exact formula for a permitted \((x,y)\) is
\[
\operatorname{ML}(x,y,x+y,x+2y)=\frac{m}{4m+2},
\quad m=\max(m_1,m_3),
\]
where \(m_1\) is respectively \((x+y-1)/2\), \((x+3y-2)/4\), or \((x+3y-1)/2\) according as \(y-x\equiv1,2,3\pmod4\); and \(m_3\) is respectively \((2x+y-1)/2\), \((2x+3y-2)/4\), or \((2x+3y-1)/2\) according as \(y-2x\equiv1,2,3\pmod4\). Uniformly on the permitted classes,
\[
\frac mH=L_{a,b}(x/H,y/H)+O(H^{-1}),
\qquad
Z_H=\frac{H}{8m+4}.
\]
The count from step 2 applies to every polygon obtained by intersecting \(T\) with a sublevel set of \(L_{a,b}\). Threshold shifts of \(O(H^{-1})\) move its polygonal boundary only by a strip of area \(O_z(H^{-1})\). Consequently, for every fixed \(z>0\),
\[
\lim_{H\to\infty}\frac{\#\{V\in\mathcal F_H:Z_H>z\}}{C(H)}
=\frac12\sum_{(a,b)\in\mathcal R}
\operatorname{area}\left(T\cap\frac1{8z}P_{a,b}\right).
\]
The right side is precisely \(\Pr\{Z>z\}\). Since all level sets of the positive piecewise-linear forms have zero area, this distribution is continuous. The one-parameter family and isolated exception contribute only \(O(H)\) sets and do not change any limit.

**4. Exact tail.** Direct intersection of the two positive half-planes defining each \(P_{a,b}\) gives the following exact areas:

| \((a,b)\) | \(\operatorname{area}(P_{a,b})\) |
| --- | ---: |
| \((0,1)\) | \(1\) |
| \((0,3)\) | \(1/3\) |
| \((1,0)\) | \(2/3\) |
| \((1,3)\) | \(13/15\) |
| \((2,1)\) | \(7/15\) |
| \((2,3)\) | \(1/3\) |
| \((3,0)\) | \(4/3\) |
| \((3,1)\) | \(1/3\) |

The sum is \(16/3\). For example, \(P_{1,3}\) has vertices \((0,0),(1,0),(2/5,6/5),(0,4/3)\) and area \(13/15\); \(P_{2,1}\) has vertices \((0,0),(1,0),(4/5,2/5),(0,2/3)\) and area \(7/15\). The other six regions are triangles. For every listed region, \(\max_{(u,v)\in P_{a,b}}(u+2v)\leq4\), with equality for \((a,b)=(0,1)\). Hence \(cP_{a,b}\subseteq\overline T\) when \(c\leq1/4\). Taking \(c=1/(8z)\) for \(z\geq1/2\) in the preceding area formula gives
\[
\Pr\{Z>z\}=\frac12\left(\frac1{8z}\right)^2\frac{16}{3}
=\frac1{24z^2}.
\]
For nonnegative \(s\), the layer-cake identity \(\mathbb E[Z^s]=s\int_0^\infty z^{s-1}\Pr\{Z>z\}\,dz\) (for \(s>0\)) and this exact tail prove the stated second-moment threshold.

## Verification

Run `python3 verify.py` using Python 3 and the standard library. It recomputes the eight allowed residue classes, constructs all eight rational polygons by half-plane clipping, checks the individual and summed areas and the sharp height bound, and checks the precise finite count for cutoffs \(H=200,400,800\). It independently maximizes four-runner loneliness using exact affine-cell breakpoints for every qualifying parameter pair with \(1\leq x,y\leq8\); this checks \(31\) source-formula instances. It also records empirical gap-tail counts at \(z=1/2,1,2\). No floating-point or sampled grid is used for these logical comparisons. The limiting frequency and entire tail remain proven by the sieve and polygon argument, not by the finite tests.

## Relationship to prior work

Yi--Gill--Bu, arXiv:2610.40694v1, Theorem 1.1, equation (2), and Lemma 8.5 provide the complete classification and exact *individual* loneliness formulas; their Section 7 includes finite censuses, notably \(4{,}125\) primitive near-critical quadruples with maximum speed at most \(200\). Jain--Kravitz, arXiv:2411.12684v2, characterize *values* of relative loneliness spectra up to finitely many exceptions and analyze residue sectors, not the height-distributed population of all primitive quadruples. Beck--Everett, arXiv:2609.06259v2, give general short linear relations and qualitative genericity rather than the specific sharp coefficient or an empirical gap law. The present arithmetic-area computation supplies the new height-density constant, the eight-sector probability law, the exact \(1/(24z^2)\) tail, and its sharp moment transition. These should not be confused with a new proof of the underlying four-runner classification.

## Limitations

The result concerns **primitive, unordered, distinct positive** four-speed sets and a maximum-coordinate height cutoff. Other sampling conventions (for example, Euclidean norm) lead to different constants. The exact tail applies to the *limiting* random variable for \(z\geq1/2\), not to the finite-cutoff empirical distribution without an error. The \(O_z\) constant may depend on the fixed threshold. The classification is taken from an October 2026 preprint and has not been independently mathematically audited here. Historical priority of the derived height and tail laws is subject to external verification, especially against non-indexed work on primitive near-tight runner populations.

## References

1. Hyunjun Yi, Karam Gill and Bryan Bu, *Four runners that are barely lonely*, arXiv:2610.40694v1, submitted 28 October 2026, https://arxiv.org/html/2610.40694v1.
2. Vanshika Jain and Noah Kravitz, *Relative Lonely Runner spectra*, arXiv:2411.12684v2, original submission 19 November 2024, https://arxiv.org/html/2411.12684v2.
3. Matthias Beck and Samuel Everett, *Lonely Runner Relations*, arXiv:2609.06259v2, original submission 5 September 2026, https://arxiv.org/abs/2609.06259.
