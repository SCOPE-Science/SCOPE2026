# Sharp variation gain and parity obstruction for periodic quadratic spline interpolation

## Finding

Let \(n\ge3\) be an integer and let \(y=(y_0,\ldots,y_{n-1})\in\mathbb R^n\) be periodic nodal data. On the circle of circumference \(n\), consider a \(C^1\) function \(Q\) which is a polynomial of degree at most two on each interval \([i,i+1]\) and interpolates \(Q(i)=y_i\) with cyclic indexing.

**Odd-cycle theorem.** For every odd \(n\ge3\), there is a unique such interpolant \(Q_n y\) for every real datum, and its exact sharp norm between the cyclic discrete and continuous variation seminorms is

\[
\boxed{\sup_{V_d(y)>0}\frac{\operatorname{Var}_{\mathbb R/n\mathbb Z}(Q_ny)}{V_d(y)}=\frac n2},\qquad V_d(y)=\sum_{i=0}^{n-1}|y_{i+1}-y_i|.
\]

Equality is attained by any one-site spike, that is, data with value one at a single knot and zero at all other knots; its discrete variation is two, whereas its spline variation is exactly \(n\).

**Even-cycle obstruction.** For each even \(n\ge4\), an interpolant exists exactly for those data satisfying \(\sum_{i=0}^{n-1}(-1)^iy_i=0\), and for every compatible datum the interpolant is nonunique with a one-dimensional affine space of solutions. For incompatible data no interpolant exists. This obstruction and the odd-cycle sharp norm together classify the nodal periodic quadratic scheme for all \(n\ge3\).

## Assumptions and scope

Knots are \(0,1,\ldots,n-1\), with the last unit cell joining knot \(n-1\) to knot \(n\equiv0\). All data, splines and derivatives are real, and both continuity and matching of first derivatives are imposed at every knot, including the seam. The physical circumference is \(n\); an affine rescaling to a circle of circumference one leaves both variation seminorms and their ratio unchanged. The norm is considered modulo constants, since both seminorms vanish on constant data.

The claim concerns ordinary exact knot interpolation by the *entire* space of \(C^1\) periodic piecewise quadratic splines, without extra slope prescriptions, smoothing, least-squares fitting or midpoint relocation of interpolation sites.

## Proof

**1. Derivative equations and parity.** Write the secant difference and the derivative at knot \(i\) as \(\Delta_i=y_{i+1}-y_i\) and \(m_i=Q'(i)\). On the cell \(x=i+t\), \(0\le t\le1\), the unique candidate having value \(y_i\), initial derivative \(m_i\), and final value \(y_{i+1}\) is

\[
Q(i+t)=y_i+m_it+(\Delta_i-m_i)t^2.
\]

The derivative from the left at the next knot is \(2\Delta_i-m_i\), so global \(C^1\) matching is precisely the cyclic system

\[
m_i+m_{i+1}=2\Delta_i,\qquad i\in\mathbb Z/n\mathbb Z.
\]

Let \(S\) be the cyclic forward shift, \((Sm)_i=m_{i+1}\). When \(n\) is odd, \((I+S)\sum_{k=0}^{n-1}(-S)^k=2I\) because \(S^n=I\). Hence the unique nodal derivatives are

\[
m_i=\sum_{k=0}^{n-1}(-1)^k\Delta_{i+k}.
\]

When \(n\) is even, the alternating vector lies in the left and right nullspace of \(I+S\); therefore solvability is equivalent to \(\sum_i(-1)^i\Delta_i=0\), equivalently \(\sum_i(-1)^iy_i=0\), since \(\sum_i(-1)^i\Delta_i=-2\sum_i(-1)^iy_i\). The nullspace is one-dimensional: \(m_i=c(-1)^i\). The associated zero-data spline is \(Q(i+t)=c(-1)^i t(1-t)\), which is nonzero when \(c\ne0\). This proves the even case, including nonuniqueness.

**2. Two-edge atoms and an all-cell bound.** Fix odd \(n\). Consider a cyclic difference vector \(\Delta=e_p-e_q\), where \(p\ne q\) and the components sum to zero. The inverse formula gives \(m_i\in\{-2,0,2\}\). On any cell with \(\Delta_i=0\), the derivative matching relation implies \(m_{i+1}=-m_i\). The cell quadratic has equal endpoint values and, at worst, a midpoint excursion of magnitude \(|m_i|/4\). Thus that cell contributes precisely \(|m_i|/2\le1\) to its continuous variation.

On a cell with \(\Delta_i=1\), the slope pair \((m_i,m_{i+1})\) must be \((2,0)\) or \((0,2)\), so the derivative remains nonnegative and the cell's variation equals one. For \(\Delta_i=-1\), the analogous slope pair is \((-2,0)\) or \((0,-2)\), giving variation one. Summing the contributions of the \(n\) cells yields \(\operatorname{Var}(Q_ny)\le n\) for any data whose cyclic difference equals \(e_p-e_q\).

**3. Extension to all real data.** For an arbitrary cyclic difference vector \(\Delta\) with \(\sum_i\Delta_i=0\), pair its positive and negative masses (a finite transport decomposition):

\[
\Delta=\sum_{p,q}\alpha_{pq}(e_p-e_q),\qquad \alpha_{pq}\ge0,\qquad \sum_{p,q}\alpha_{pq}=\frac12\sum_i|\Delta_i|.
\]

The odd-cycle interpolant is linear, and adding a constant to the data does not change its variation. Triangle inequality for total variation, followed by the two-edge bound, gives

\[
\operatorname{Var}(Q_ny)\le n\sum_{p,q}\alpha_{pq}=\frac n2 V_d(y).
\]

This covers every real datum, not just step data.

**4. Sharpness.** Choose \(y_0=1\) and \(y_i=0\) for \(1\le i<n\). Then \(\Delta_0=-1\), \(\Delta_{n-1}=1\), and all other differences vanish. The inverse formula gives \(m_0=0\), and, for \(1\le i<n\), \(m_i=2(-1)^i\) (the sign convention may be shifted by cyclic relabelling). Every one of the \(n\) cells has total variation one: the two cells adjacent to the spike are monotone and each intervening flat-data cell makes an excursion of size \(1/2\). Therefore \(\operatorname{Var}(Q_ny)=n\) and \(V_d(y)=2\), attaining the bound \(n/2\). The existence, obstruction, all-data upper bound and attainment prove the theorem.

## Verification

The formula for the derivatives is verified by multiplying the finite geometric series for \(I+S\). The local variation calculation splits a quadratic at its only possible stationary point, \(t=-m_i/[2(\Delta_i-m_i)]\) when this point is strictly inside the cell. The transport argument is an exact finite-dimensional decomposition and not a finite-enumeration assumption.

The accompanying standalone \(\texttt{check\_periodic\_quadratic.py}\) uses only Python's standard library and exact rational arithmetic. It checks all ordered two-edge atoms for each odd \(n=3,5,\ldots,41\), single-site extremizers, 1,800 additional rational examples, and the even-cycle compatibility and null-spline construction for each even \(n=4,6,\ldots,64\). Run it with \(\texttt{python3 check\_periodic\_quadratic.py}\). These tests corroborate, rather than replace, the proof for all integer \(n\).

## Relationship to prior work

Schoenberg's 1968 work on cardinal spline interpolation considers splines of odd polynomial degree and the full integer line, not this finite-circle \(C^1\) degree-two knot-interpolation norm [1]. Goodman (1983; online record dated 2011) treats broad conditions for spline interpolation solvability, so the parity obstruction must not be regarded as independent novelty; the available synopsis does not establish the present sharp \(BV\) amplification [2]. Albasiny and Hoskins (1973) study periodic uniform-mesh spline interpolation error bounds via circulant matrices, so their uninspected full text remains particularly relevant to historical priority [3]. Nochetto and Salgado construct an averaging-based total-variation-diminishing interpolation scheme, not this exact nodal quadratic map [4].

The distinctive conclusion here is the **sharp and attained \(n/2\) variation norm for every odd cycle**, tied to a fully explicit knot-interpolation solvability dichotomy. It does not follow from generic uniqueness criteria, smooth-input error estimates, or the \(L^\infty\) norms of orthogonal projections onto different spline spaces.

## Limitations

The theorem assumes unit-spaced cyclic knots and degree at most two with \(C^1\) continuity. It provides neither a stable norm for even cycles (the unrestricted interpolant is not uniquely defined) nor a bound uniform in the number of odd sites. No claim is made for open intervals, nonuniform knots, odd-degree splines, higher dimensions, smoothing splines or other boundary conditions. Historical novelty remains subject to unavailable full texts of some older periodic-spline work; this affects priority assessment, not the algebraic proof.

The first_public_date metadata value is the day-verifiable online availability of the Goodman source (14 November 2011); it is **not** an assertion that the original 1983 work was first made public on that day. The underlying literature is substantially older, with the original issue dates provided separately.

## References

[1] I. J. Schoenberg, *On spline interpolation at all integer points of the real axis*, Mathematica 10 (1968), 151–170. Full text: https://ictp.acad.ro/popoviciu/about/Schoenberg%201968%20-%20Mathematica%20-%20On%20spline%20interpolation.pdf

[2] T. N. T. Goodman, *Solvability of cardinal spline interpolation problems*, Proceedings of the Royal Society of Edinburgh Section A 95 (1983), 39–57. DOI: https://doi.org/10.1017/S030821050001578X . Publisher's online record dated 2011-11-14.

[3] E. L. Albasiny and W. D. Hoskins, *Explicit error bounds for periodic splines of odd order on a uniform mesh*, IMA Journal of Applied Mathematics 12 (1973), 303–318. DOI: https://doi.org/10.1093/imamat/12.3.303 .

[4] R. H. Nochetto and A. J. Salgado, *A total variation diminishing interpolation operator and applications*, arXiv:1211.1069 (first posted 2012-11-05). https://arxiv.org/abs/1211.1069
