# Sharp localization threshold for a binary-mask three-site Gaussian interpolation matrix

## Finding

For the column-centred Gaussian interpolation matrix on the equally spaced sites \(-h,0,h\) with centre-specific shape parameters \((\alpha,\beta,\alpha)\), \(h>0\) and \(0<\beta<\alpha\), a universal *sharp* finite-width nonsingularity threshold is

\[
\alpha h\ge t_0:=\sqrt{-\log\rho},\qquad
\rho^3+\rho^2+\rho-1=0,\quad 0<\rho<1.
\]

Here \(\rho=0.543689012692\ldots\) and \(t_0=0.780626583864\ldots\). For every \(\alpha h<t_0\), there is exactly one centre shape \(\beta\in(0,\alpha)\) making the matrix singular. In the complementary cases the determinant's sign is classified exactly below. This is a finite-width, binary-shape safety criterion, not merely a singular example or a statement about the idealized delta-column limit.

## Assumptions and scope

Fix \(h>0\), set sites \(s_1=-h,s_2=0,s_3=h\), and let the \(j\)-th Gaussian basis be \(\phi_j(s)=\exp[-\varepsilon_j^2(s-s_j)^2]\). Set \(\varepsilon_1=\varepsilon_3=\alpha>0\), \(\varepsilon_2=\beta\in(0,\alpha)\). The interpolation matrix is \(K_{ij}=\phi_j(s_i)\). Put \(x=\exp(-\alpha^2h^2)\), \(y=\exp(-\beta^2h^2)\), so \(0<x<y<1\). All claims are over exact real arithmetic; finite-precision underflow is not modelled. A binary shape mask \(\psi=(0,1,0)\) in the rule \(\tilde\varepsilon_j=\varepsilon/(c+\psi_j)\), \(c,\varepsilon>0\), gives this arrangement with \(\alpha=\varepsilon/c\), \(\beta=\varepsilon/(1+c)\). Whether an indicator actually realizes this mask is not asserted.

## Proof

**Exact determinant.** At the three sites,

\[
K=\begin{pmatrix}1&y&x^4\\x&1&x\\x^4&y&1\end{pmatrix},\qquad
\det K=(1-x^4)(1+x^4-2xy).
\]

The first factor is strictly positive, so only \(F(x,y)=1+x^4-2xy\) controls invertibility and orientation.

**Sharp uniform localization threshold.** Since \(0<y<1\), we have \(F(x,y)>1+x^4-2x\). The identity

\[
1+x^4-2x=(x-1)(x^3+x^2+x-1)
\]

and strict increase of \(x^3+x^2+x-1\) on \((0,1)\) show that \(1+x^4-2x\ge0\) exactly when \(0<x\le\rho\), where \(\rho\) is the unique root of the stated cubic in \((0,1)\). Consequently \(\det K>0\) for **all** \(0<\beta<\alpha\) whenever \(x\le\rho\), equivalent to \(\alpha h\ge t_0\); strict positivity persists at the endpoint because \(y<1\).

If \(\rho<x<1\), then

\[
y_*(x):=\frac{1+x^4}{2x}
\]

obeys \(x<y_*(x)<1\). The lower inequality is equivalent to \((1-x^2)^2>0\), and the upper to \(x>\rho\). Thus there exists one and only one \(\beta_*\in(0,\alpha)\) with \(\exp(-\beta_*^2 h^2)=y_*(x)\). At \(\beta=\beta_*\) the matrix is singular. For \(0<\beta<\beta_*\) we have \(y>y_*\) and \(\det K<0\); for \(\beta_*<\beta<\alpha\), \(\det K>0\). This proves uniform sharpness and complete sign classification.

**Fixed-ratio uniqueness.** Fix \(R=\alpha/\beta>1\), so \(y=x^{1/R^2}\). Write \(p=1+R^{-2}\in(1,2)\); the determinant sign equals the sign of

\[
f_p(x)=1+x^4-2x^p,\qquad
f_p'(x)=2x^{p-1}(2x^{4-p}-p).
\]

The derivative is negative then positive, with its unique zero in \((0,1)\), since \(p/2\in(1/2,1)\). Moreover \(f_p(0^+)=1\), \(f_p(1)=0\), \(f_p'(1)=4-2p>0\), so the strict minimum is negative and there is exactly one zero \(x_R\in(0,1)\) other than the excluded boundary \(x=1\). As \(f_p(\rho)>1+\rho^4-2\rho=0\), this zero satisfies \(\rho<x_R<1\). In terms of the physical parameter, \(\det K<0\) for \(0<\alpha h<\sqrt{-\log x_R}\), equals zero at that threshold, and is positive above it. Continuity and the preceding uniform result imply \(x_R\downarrow\rho\) as \(R\to\infty\), while \(x_R\uparrow1\) as \(R\downarrow1\).

**Exact singular example.** Take \(x=3/4\), \(y=337/384\). Then \(0<x<y<1\), \(2xy=1+x^4\), and

\[
K=\begin{pmatrix}1&337/384&81/256\\3/4&1&3/4\\81/256&337/384&1\end{pmatrix},\quad
K\begin{pmatrix}1\\-3/2\\1\end{pmatrix}=0.
\]

The upper-left \(2\times2\) minor \(1-xy\) is positive, so the rank is exactly two. These entries correspond to finite positive shapes \(\alpha h=\sqrt{\log(4/3)}\), \(\beta h=\sqrt{\log(384/337)}\). All matrices with one or two distinct sites and strictly positive Gaussian column widths are nonsingular, because the two-site determinant is \(1-\exp[-(\varepsilon_1^2+\varepsilon_2^2)h^2]>0\) for separation \(h>0\); three sites is the first dimension admitting singularity, although three-site singularity in the general variable-shape setting is known [2].

## Verification

The attached `verify.py` uses exact rational arithmetic and the Python standard library to check the determinant identity on many rational inputs, the rational rank-two singular certificate, strict rational isolating bounds for \(\rho\), and rational sign representatives across the two regimes. These finite checks support, but do not replace, the full real-parameter monotonicity and sign arguments above. Run `python3 verify.py` from its containing folder.

## Relationship to prior work

Kuruc, Levin, Mulet, Ruiz-Álvarez and Yáñez [1], Sections 2–4, introduce a binary-modified data-dependent Gaussian shape parameter and prove nonsingularity for *exactly replaced delta-like columns*. Their exact column-replacement statement does not itself give a uniform finite-width threshold for the original column-wise Gaussian matrix. Chiu, Ling and McCourt [2], Section 2 and Example 2.1, already explicitly demonstrate singularity in generic three-site variable-shape Gaussian matrices, so **the existence of a three-node singularity is not claimed as new**. Their almost-everywhere invertibility statement is also compatible with a codimension-one singular curve. The added result is the complete symmetric two-level finite-width phase diagram, its universal cubic safety boundary, and the fixed-ratio one-crossing classification, none of which follows from simply knowing that some three-node examples are singular. Bozzini, Lenarduzzi, Rossini and Schaback [3] give general sufficient perturbation conditions for differently scaled bases, but not this exact two-level threshold. Literature searches did not establish historical exclusivity; the possibility of an earlier equivalent special-case factorization remains.

## Limitations

The theorem concerns exactly three equally spaced sites, symmetric outer widths and a flatter middle Gaussian. It neither proves nor disputes all parameter settings of the cited adaptive method, and the indicator-to-mask mapping is not established. Its threshold guarantees invertibility, not a uniform numerical condition-number bound: as the singular curve is approached, inverse sensitivity diverges. The claims do not extend automatically to arbitrary nodes, other kernels, more than three sites, or to idealized delta-column algebra. Historical priority is not exhaustively settled.

## References

[1] J. Kuruc, D. Levin, P. Mulet, J. Ruiz-Álvarez and D. F. Yáñez, *Data-dependent approximation through RBF*, arXiv:2603.23074v1 (first publicly submitted 2026-03-24), https://arxiv.org/html/2603.23074v1 ; Sections 2–4.

[2] S. N. Chiu, L. Ling and M. McCourt, *On variable and random shape Gaussian interpolations*, *Applied Mathematics and Computation* (2020), DOI: 10.1016/j.amc.2020.125159, https://www.math.hkbu.edu.hk/~lling/PDF/VariableShape2020.pdf ; especially Section 2, Example 2.1 and Theorem 2.2.

[3] M. Bozzini, L. Lenarduzzi, M. Rossini and R. Schaback, *Interpolation by Basis Functions of Different Scales and Shapes*, *Calcolo* (2004), https://num.math.uni-goettingen.de/schaback/research/papers/IbBFoDSaS.pdf ; Sections 1–3.
