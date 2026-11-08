# Exact parity defect and failure intervals for the symmetric lattice-point lower product on \(D_n\) boxes

## Finding

Let \(n\ge2\) and let
\[
D_n=\{z\in\mathbb Z^n:\sum_{i=1}^n z_i\equiv0\pmod2\},\qquad
K(r)=\prod_{i=1}^n[-r_i,r_i],
\]
where \(r_1\ge\cdots\ge r_n>0\). Set \(\lambda_i=\lambda_i(K(r),D_n)\), the successive minima in increasing order, and let \(I(r)=\#(\operatorname{int}K(r)\cap D_n)\). The following formulas hold **for every positive real side-length vector**:
\[
\lambda_1=\min\left\{\frac2{r_1},\frac1{r_2}\right\},\quad
\lambda_i=\frac1{r_i}\ (2\le i\le n),
\]
\[
I(r)=\frac12\left[\prod_{i=1}^n(2\lceil r_i\rceil-1)
+(-1)^{\sum_i(\lceil r_i\rceil-1)}\right].
\]
In particular, define the signed defect in the proposed symmetric Betke--Henk--Wills interior product bound by
\[
\mathcal D(r)=I(r)-\frac{\operatorname{vol}_nK(r)}{\det D_n}
\prod_{i=1}^n\left(1-\frac{\lambda_i}2\right),\qquad\det D_n=2.
\]
The two displayed formulas give an exact, explicit expression for this defect for all \(r\). The corresponding conjectural product bound is relevant in its original positive-factor regime \(\lambda_n\le2\), equivalently \(r_n\ge1/2\).

For **integer** half-sides \(m_1\ge\cdots\ge m_n\ge1\), write
\[
P=\prod_{i=2}^n(2m_i-1),\quad
\eta=(-1)^{\sum_i(m_i-1)},\quad
A=\min\left\{2,\frac{m_1}{m_2}\right\}.
\]
Then the exact signed defect is
\[
\boxed{\mathcal D(m)=\frac{(A-1)P+\eta}{2}.}
\]
Consequently, the proposed symmetric product bound **fails if and only if**
\[
\boxed{m_1=m_2\quad\text{and}\quad\sum_{i=1}^n(m_i-1)\ \text{is odd}.}
\]
Equivalently, on all these integer boxes one has the **sharp additive correction** \(I(m)\ge \operatorname{vol}_n(K(m))\prod_i(1-\lambda_i/2)/2-1/2\); its constant \(1/2\) is attained in every dimension \(n\ge3\).

Equality holds **if and only if** \(m_1>m_2=\cdots=m_n=1\) and \(m_1\) is even; the bound is strict in all remaining cases where it does not fail. For every \(n\ge3\), the choice \(m_1=m_2=m_3=2\) and \(m_4=\cdots=m_n=1\) yields a counterexample (including every even dimension \(n\ge4\)); for \(n=2\), no such box violates the bound.

For **isotropic real** half-side \(r\ge1/2\), the lower product fails for no even dimension. In odd dimensions \(n\ge3\) it fails precisely in the disjoint intervals
\[
\boxed{r\in\left(\frac{1+((2k+1)^n-1)^{1/n}}2,\ k+1\right],\quad
k=1,3,5,\ldots.}
\]
The interval adjoining an even integer \(k+1\) has length
\[
\frac1{2n(2k+1)^{n-1}}+O_n((2k+1)^{1-2n}).
\]

## Assumptions and scope

The lattice is fixed to the parity root lattice \(D_n\), not \(\mathbb Z^n\). Its covolume is exactly \(2\). The box is centered, closed and full-dimensional. Interior counts use **strict** inequalities \(|z_i|<r_i\); at integer half-sides the boundary convention is essential. The parameter ordering merely permutes coordinates. The proposed product lower bound investigated here is
\[
\#(\operatorname{int}K\cap\Lambda)\ge
\frac{\operatorname{vol}_nK}{\det\Lambda}\prod_i(1-\lambda_i(K,\Lambda)/2)
\]
for centrally symmetric convex bodies when the last minimum does not exceed \(2\). The present result is a complete evaluation and classification **inside the indicated family**, not a claim about arbitrary convex bodies.

## Proof

**1. Successive minima.** Membership in \(D_n\) requires the coordinate sum of a lattice vector to be even. A nonzero vector with only one nonzero coordinate must therefore have magnitude at least \(2\) there. If a vector has at least two nonzero coordinates, its \(K(r)\)-gauge is at least \(1/r_2\). Conversely \(2e_1\) and \(e_1+e_2\) attain the two respective gauges, proving the first formula. For \(j\ge2\), any lattice vector of gauge strictly below \(1/r_j\) has all coordinates \(j,\ldots,n\) equal to zero, so the span has dimension at most \(j-1\). At gauge \(1/r_j\), the vectors \(e_1+e_2\), \(e_1-e_2\), and \(e_1+e_i\) for \(3\le i\le j\) are all available and linearly independent. This proves \(\lambda_j=1/r_j\), including ties and the two-dimensional boundary case.

**2. Exact interior enumeration.** For \(r_i>0\), the integers strictly inside \((-r_i,r_i)\) are \(-b_i,-b_i+1,\ldots,b_i\), with \(b_i=\lceil r_i\rceil-1\). Their number is \(2b_i+1\), and their alternating sum is \((-1)^{b_i}\). The parity indicator of \(D_n\) is \((1+(-1)^{\sum_i z_i})/2\). Expanding the finite product of these coordinate sums gives the asserted formula for \(I(r)\), with no asymptotic argument.

**3. Integer boxes and the sharp classification.** When \(r=m\) is integral, the interior count is \(((2m_1-1)P+\eta)/2\). For \(j\ge2\), the factors \(2m_j(1-\lambda_j/2)\) equal \(2m_j-1\); for the first coordinate the factor is \(2m_1-m_1\lambda_1\). Since \(m_1\lambda_1=A\), subtraction yields the boxed defect identity.

If \(m_1=m_2\), then \(A=1\) and \(\mathcal D=\eta/2\), giving exactly the parity criterion. Suppose \(m_1>m_2\). If \(m_2\ge2\), then \(A-1\ge1/m_2\) and \(P\ge2m_2-1\), so \((A-1)P\ge2-1/m_2>1\). Therefore \(\mathcal D>0\) regardless of \(\eta\). If \(m_2=1\), all \(m_j=1\) for \(j\ge2\), \(A=2\), \(P=1\), and \(\mathcal D=(1+(-1)^{m_1-1})/2\). This is zero precisely when \(m_1\) is even and otherwise positive. It follows that the negative, zero and positive cases stated above are exhaustive. The explicit dimensions follow by choosing three coordinates with half-side \(2\).

**4. Exact isotropic failure bands.** When \(r_1=\cdots=r_n=r\), every minimum equals \(1/r\), so the product expression is \((2r-1)^n/2\). For \(k\ge0\) and \(r\in(k,k+1]\), every \(b_i=k\), hence
\[
I(r)=\frac{(2k+1)^n+(-1)^{nk}}2.
\]
Since \(2r-1\le2k+1\), no failure occurs if \((-1)^{nk}=+1\). If it equals \(-1\), which requires \(n\) and \(k\) both odd, failure is equivalent to \((2r-1)^n>(2k+1)^n-1\). Solving this inequality gives the displayed interval, including its right endpoint and excluding its left endpoint. Taylor expansion of \((1-s)^{1/n}\) at \(s=0\), with \(s=(2k+1)^{-n}\), gives the stated interval-length asymptotic.

## Verification

The accompanying standard-library-only `verify.py` uses exact rational arithmetic. It checks the stated minima against ranks generated by explicit lattice vectors of coordinates at most \(2\) in absolute value for all ordered integer half-side tuples of lengths \(2\)--\(4\), with entries \(1\)--\(4\), and for further rational side lengths. It independently enumerates parity-restricted interior lattice points, checks the signed-defect formula and its sign/equality classification, and compares the isotropic expressions in several dimensions. The script reports 274 passing cases. These finite checks are **corroboration only**; the four analytic steps above prove the general statements.

## Relationship to prior work

Wang and Xue [1], §8, Remark 8.2, show that the symmetric Betke--Henk--Wills interior product inequality already fails for the single three-dimensional example \(K=[-2,2]^3\) over the even-coordinate-sum lattice. The theorem here supplies a dimension-uniform formula, the complete integer rectangular-box failure and equality classifications, and exact real-radius failure intervals. The general upper and linear interior lower estimates in [1] do not imply these sign classifications. Freyer and Lucas [2], Proposition 1.5, prove the symmetric product lower bound for origin-symmetric lattice polygons in dimension two; the nonfailure assertion for two-dimensional parity boxes agrees with their result. The 1993 conjectural framework [3] does not, as far as the inspected sources show, include this family-wide phase diagram.

## Limitations

The result settles this particular parity-lattice family, not the global validity of any replacement lower bound or any other lattice. The sign oscillation is an exact discrepancy of at most one half in the isotropic case; it is not a universal dimension-free lower improvement. Only same-paper/material comparisons stated above and accessible published searches were used for the literature assessment; historical priority may require further specialized scrutiny. No external independent mathematical validation is claimed.

## References

[1] Jun Wang and Fei Xue, *Bounds for lattice points in terms of volume and successive minima*, arXiv:2610.41125v1, first publicly submitted 2026-10-30, especially §1 and Remark 8.2. https://arxiv.org/html/2610.41125v1

[2] Ansgar Freyer and Eduardo Lucas, *Interpolating between volume and lattice point enumerator with successive minima*, Monatshefte für Mathematik 198 (2022), 717–740, Proposition 1.5. https://doi.org/10.1007/s00605-022-01713-1

[3] Ulrich Betke, Martin Henk and Jörg M. Wills, *Successive-minima-type inequalities*, Discrete & Computational Geometry 9 (1993), 165–175. https://doi.org/10.1007/BF02189316
