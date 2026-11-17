# A hidden third-moment transition after suppression of gelation

## Finding

In the discrete product-kernel coagulation model with constant-rate spontaneous shattering, preventing gelation at rate \(\lambda=4\) does not guarantee a finite stationary third moment. For the mass-one stationary sequence at every fixed \(\lambda>4\), put \(M_j=\sum_{k\geq1}k^j n_k\) and
\[
m_\lambda=\frac{\lambda-\sqrt{\lambda(\lambda-4)}}2.
\]
Then the **sharp third-moment transition** is
\[
M_3=\begin{cases}
+\infty,&4<\lambda\leq 9/2,\\
\displaystyle\frac{\lambda}{\lambda-3m_\lambda},&\lambda>9/2.
\end{cases}
\]
At the critical point \(\lambda=9/2\), the divergence has the precise logarithmic constant
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{k=1}^Nk^3 n_k=3.
\]
On approach from the finite-moment side,
\[
\lim_{\lambda\downarrow9/2}(\lambda-9/2)M_3=\frac94.
\]
These are statements about stationary distributions, not the third moment at a fixed finite evolution time.

## Assumptions and scope

For each fixed real \(\lambda>4\), use the nonnegative mass-one stationary concentration sequence defined uniquely coefficientwise by
\[
n_1=\frac{\lambda}{1+\lambda},\qquad
n_k=\frac{1}{2(k+\lambda)}\sum_{i=1}^{k-1}i(k-i)n_i n_{k-i}\quad(k\geq2).
\]
In the non-gelling regime the source establishes \(\sum_{k\geq1}kn_k=1\) and the finite second moment \(M_2=m_\lambda\); these two source-established properties are explicit premises of the theorem. No uniformity is claimed at \(\lambda=4\) or as \(\lambda\to\infty\). The unweighted stationary particle number \(M_0\) and the finite \(M_2\) are prior results, not findings claimed here.

## Proof

**1. Generating identity with convergent derivatives.** Let \(G(z)=\sum_{k\geq1}n_kz^k\) and \(H(z)=zG'(z)=\sum_{k\geq1}kn_kz^k\) for \(0<z<1\). The stationary recurrence gives, by absolutely convergent products for \(0<z<1\),
\[
\frac12H(z)^2-H(z)-\lambda G(z)+\lambda z=0.
\]
Differentiation is justified on each compact subinterval of \((0,1)\). Consequently
\[
(H-1)H'=\lambda(H/z-1).
\tag{1}
\]
Mass conservation and the finite second moment give \(H(z)\uparrow1\), \(H'(z)\uparrow m_\lambda\), and
\[
1-H(z)\sim m_\lambda(1-z)\qquad(z\uparrow1).
\tag{2}
\]
Moreover \(H(z)<1\), \(H''(z)>0\), \(H'''(z)>0\) for \(0<z<1\), because every coefficient is strictly positive.

**2. A first-order equation for the third-moment generating derivative.** Differentiating (1) twice, writing \(Y=H''\), yields the exact identity
\[
(1-H)Y'=B-A Y,
\quad
A(z)=\frac{\lambda}{z}-3H'(z),\qquad
B(z)=\frac{2\lambda}{z^2}\left(H'(z)-\frac{H(z)}z\right).
\tag{3}
\]
Here \(Y'\geq0\), \(B(z)>0\), and
\[
A(z)\longrightarrow a_\lambda=\lambda-3m_\lambda,\qquad
B(z)\longrightarrow b_\lambda=2\lambda(m_\lambda-1)>0.
\tag{4}
\]
The inequality \(m_\lambda>1\) follows directly from its displayed expression for every finite \(\lambda>4\).

**3. The finite side.** If \(a_\lambda>0\), then \(A(z)>a_\lambda/2\) for \(z\) close enough to one. As \(Y'\geq0\), equation (3) implies \(A(z)Y(z)\leq B(z)\). Thus the nondecreasing \(Y\) has a finite limit \(L\). If \(b_\lambda-a_\lambda L\ne0\), equation (3) and (2) would force \(Y'(z)\) to have a fixed nonzero multiple of \((1-z)^{-1}\) asymptotically, contradicting the finite limit. Hence
\[
L=\frac{b_\lambda}{a_\lambda}
=\frac{2\lambda(m_\lambda-1)}{\lambda-3m_\lambda}.
\]
Since \(H''(1-)=\sum_{k\geq1}(k^3-k^2)n_k=M_3-M_2\), and \(m_\lambda^2=\lambda(m_\lambda-1)\), this simplifies exactly to
\[
M_3=m_\lambda+L=\frac\lambda{\lambda-3m_\lambda}.
\tag{5}
\]

**4. The divergent side.** If \(a_\lambda<0\), then for all sufficiently large \(z<1\), \(A(z)<0\) while \(B(z)>b_\lambda/2\). Equation (3), together with \(Y\geq0\) and (2), forces \(Y'(z)\geq c/(1-z)\) for some \(c>0\). Therefore \(Y(1-)=+\infty\), and so \(M_3=+\infty\). If \(a_\lambda=0\) but \(Y\) were bounded, (3)–(4) would again give \(Y'(z)\geq c/(1-z)\) near one, a contradiction. Thus \(M_3\) also diverges at equality. Direct algebra gives
\[
\lambda-3m_\lambda\begin{cases}<0,&4<\lambda<9/2,\\=0,&\lambda=9/2,\\>0,&\lambda>9/2.\end{cases}
\]
This proves the complete finite/divergent classification.

**5. Sharp boundary coefficient.** Set \(\lambda=9/2\), so \(m_\lambda=3/2\), \(a_\lambda=0\), and \(b_\lambda=9/2\). Then for every \(z<1\),
\[
A(z)=\lambda(1/z-1)+3(m_\lambda-H'(z))>0.
\]
Equation (3) implies \(0\leq Y'(z)\leq B(z)/(1-H(z))\), so by (2), \(Y(z)=O(\log(1/(1-z)))\). Since \(H'(1-)=m_\lambda\), integration gives
\[
m_\lambda-H'(z)=\int_z^1Y(t)\,dt
=O((1-z)\log(1/(1-z))).
\]
Therefore \(A(z)Y(z)=O((1-z)\log^2(1/(1-z)))=o(1)\). Returning to (3) yields
\[
\lim_{z\uparrow1}(1-z)Y'(z)=\frac{b_\lambda}{m_\lambda}=3,
\qquad Y(z)\sim3\log\frac1{1-z}.
\tag{6}
\]
Now \(z^2Y(z)=\sum_{k\geq2}(k^3-k^2)n_kz^k\) has nonnegative coefficients. The index-zero Hardy–Littlewood–Karamata Tauberian theorem applied to (6) gives
\[
\sum_{k\leq N}(k^3-k^2)n_k\sim3\log N.
\]
The \(k^2\)-sum is finite and equals \(3/2\), so the asserted sharp truncated \(M_3\) law follows.

**6. Approaching the boundary from above.** The derivative of \(\lambda-3m_\lambda\) at \(\lambda=9/2\) is exactly \(2\). Equation (5) therefore yields \((\lambda-9/2)M_3\to(9/2)/2=9/4\).

## Verification

The identities (1)–(6) are exact analytical deductions; no finite enumeration is used as a proof of divergence, finiteness, or the logarithmic limit. The accompanying self-contained `verify.py` reproduces initial coefficients via rational arithmetic, numerically checks the predicted finite-moment formula and the growth in the divergent regimes, and prints its finite-sample limitations. To reproduce, run `python verify.py` with Python 3 and NumPy installed. The script generates its coefficients from the recurrence in this result and does not rely on files from another package.

## Relationship to prior work

Matveev [1], equations (8)–(12), proves the stationary generating identity and recurrence for the non-gelling product-kernel shattering model and computes the finite second moment. The new contribution is the **separate sharp third-moment boundary** \(\lambda=9/2\), its explicit finite branch, the logarithmic critical coefficient, and the simple-pole approach from above. The presence of a finite second moment for all \(\lambda>4\) does not imply the finite third moment determined here.

Classical work on multiplicative coagulation and different fragmentation laws, including Laurençot–van Roessel [2], motivates comparison but does not, from inspected material, establish the stationary third-moment threshold for the specific constant-rate discrete shattering recurrence [1]. The broader review [3] describes other aggregation/fragmentation constructions; complete historical priority has not been established. The classical index-zero positive-coefficient Tauberian theorem is used only to transfer a proved generating-function asymptotic to the cumulative moment.

## Limitations

Only the mass-one stationary branch with \(\lambda>4\) is treated. This does not establish a higher-moment hierarchy, pointwise particle-size tail constants, the third moment for transient solutions, or uniform estimates as \(\lambda\downarrow4\). The coefficient statement at \(\lambda=9/2\) concerns truncated stationary sums, not a finite full third moment. All historical-priority conclusions remain conditional on the inspected literature; no independent audit was performed.

## References

[1] S. Matveev, *Suppression of gel formation by spontaneous fragmentation*, arXiv:2611.09537v1, 6 November 2026, sections 1–3, especially equations (5), (8), (11), (12). https://arxiv.org/html/2611.09537v1

[2] P. Laurençot and H. van Roessel, *Absence of gelation and self-similar behavior for a coagulation-fragmentation equation*, arXiv:1407.1596v1 (2014); SIAM J. Math. Anal. 47 (2015), 2355–2374. Different singular-fragmentation mechanism. https://arxiv.org/abs/1407.1596

[3] S. A. Matveev, *Generating functions for aggregation and fragmentation: review*, arXiv:2606.10785 (2026). https://arxiv.org/abs/2606.10785

[4] G. H. Hardy and J. E. Littlewood, classical Tauberian theorems for nonnegative power-series coefficients; or the index-zero regular-variation formulation of Karamata's Tauberian theorem. Used for the final implication in step 5.
