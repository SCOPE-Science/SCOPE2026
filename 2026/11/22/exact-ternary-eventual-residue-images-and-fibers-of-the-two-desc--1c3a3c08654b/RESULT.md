# Exact ternary eventual residue images and fibers of the two-descent Eulerian column

## Finding

Let \(E_n\) denote the Eulerian number counting permutations of \(\{1,\ldots,n\}\) with exactly two descents, with \(E_0=0\). Thus, for every integer \(n\ge0\),
\[
E_n=3^n-(n+1)2^n+\binom{n+1}{2}.
\]
For every integer \(k\ge1\), the sequence \((E_n\bmod3^k)_{n\ge0}\) has least eventual period \(2\cdot3^k\). Write \(I_k\) for its **eventual value image**, equivalently the set of residues occurring infinitely often (rather than a claim about all initial indices).

There is a uniquely determined \(\beta\in1+3\mathbb Z_3\) solving
\[
4\beta+3-4\,4^\beta\bigl(1+(\beta+1)\log4\bigr)=0,
\qquad A=(\beta+1)\bigl(2\beta+1-4\cdot4^\beta\bigr)\equiv1\pmod9.
\]
Here \(4^t=\exp(t\log4)\) for \(t\in\mathbb Z_3\). The complete infinite-occurrence closure is the disjoint union
\[
\boxed{I=3\mathbb Z_3\;\sqcup\;(2+3\mathbb Z_3)\;\sqcup\;(A+18\mathbb Z_3^2).}
\]
Its reduction modulo \(3^k\) is precisely \(I_k\). Defining \(S_0=1\) and, for \(j\ge1\),
\[
S_j=1+\sum_{a=0}^{\lfloor(j-1)/2\rfloor}3^{j-2a-1},
\]
which counts distinct squares modulo \(3^j\), the exact image sizes are
\[
\boxed{|I_1|=3,\quad |I_k|=2\cdot3^{k-1}+S_{k-2}\quad(k\ge2).}
\]
The normalized Haar measure of \(I\) is exactly \(17/24\).

There is also a complete residue-by-residue fiber law. Define
\[
R_m(w)=\#\{z\bmod3^m:z^2\equiv w\pmod{3^m}\},\quad R_0(w)=1.
\]
For \(k\ge2\), let \(V_k(y)\) be the number of indices in any single eventual least period \(2\cdot3^k\) yielding \(y\bmod3^k\). Then
\[
\begin{aligned}
V_k(y)={}&2\,\mathbf1_{\{y\equiv0,2\pmod3\}}\\
&+3\,\mathbf1_{\{y\equiv0\pmod9\}}
 R_{k-2}\!\left(\frac{y}{18}\right)\\
&+3\,\mathbf1_{\{y\equiv A\pmod9\}}
 R_{k-2}\!\left(\frac{y-A}{18}\right).
\end{aligned}
\]
The arguments in the last two lines mean the **well-defined residues modulo \(3^{k-2}\)** obtained by first dividing by nine and then multiplying by the inverse of two; those terms are evaluated only when their indicators are one. At \(k=1\), \((V_1(0),V_1(1),V_1(2))=(3,1,2)\). In particular,
\[
\boxed{V_k(0)=2+3^{\lfloor k/2\rfloor}\quad(k\ge1).}
\]

## Assumptions and scope

All index variables \(n\) are nonnegative integers; all depth variables \(k\) are positive integers. The term **eventual** is essential: for any \(k\), the reduction of \(E_n\) for \(n\ge k\) is modeled by two analytic branches. The theorem counts fibers within that periodic tail, not arbitrary finite-prefix occurrences. The value \(A\) is given by a unique convergent \(3\)-adic critical-point equation, not by a finite decimal approximation. The notation \(\mathbb Z_3^2=\{z^2:z\in\mathbb Z_3\}\) denotes squares, not a Cartesian product.

## Proof

**1. Branch interpolation and eventual period.** The classical Eulerian inclusion-exclusion formula displayed above is exact for all \(n\ge0\). For \(n\ge k\), its first term vanishes modulo \(3^k\). On writing \(n=2t+\varepsilon\), \(\varepsilon\in\{0,1\}\), the remainder becomes the two integral analytic functions
\[
g_0(t)=(2t+1)(t-4^t),\qquad
g_1(t)=(t+1)(2t+1-4\cdot4^t).
\]
For each \(k\), both are compatible modulo \(3^k\) on \(\mathbb Z_3\), and the tail of \(E_n\) is exactly their interlacing. Consequently its period divides \(2\cdot3^k\).

**2. Two regular balls in each parity branch.** Since \(\log4\in3\mathbb Z_3\), direct differentiation gives, for both \(\varepsilon\in\{0,1\}\),
\[
g_\varepsilon'(t)\equiv t-1\pmod3,
\qquad g_\varepsilon''(t)\equiv1\pmod3.
\]
On \(t\equiv0,2\pmod3\), \(g_\varepsilon'\) is a unit. Analytic difference quotients equal that unit modulo three, so each restricted map is a bijective isometry from the corresponding index ball onto its value ball (the onto statement follows by successive Hensel digit lifting). Direct substitution gives
\[
g_0(0)\equiv g_0(2)\equiv2\pmod3,
\qquad g_1(0)\equiv g_1(2)\equiv0\pmod3.
\]
Thus each residue in \(2+3\mathbb Z_3\) has two regular even-branch preimages, and each residue in \(3\mathbb Z_3\) has two regular odd-branch preimages.

**3. The two critical balls.** The derivative modulo three has the unique root \(t\equiv1\pmod3\), with second derivative a unit, so each branch has a unique critical point \(\beta_\varepsilon\in1+3\mathbb Z_3\), by Hensel lifting. For the even branch one checks exactly
\[
\beta_0=-\tfrac12,\quad 4^{\beta_0}=-\tfrac12,\quad g_0(\beta_0)=0.
\]
The square-root identity is the \(3\)-adic root in \(1+3\mathbb Z_3\). For the odd branch the defining derivative equation is the one in the Finding; \(\beta_1=\beta\), and \(g_1(1)=-26\equiv1\pmod9\). Since \(\beta-1\in3\mathbb Z_3\) and \(g_1'(1)\equiv0\pmod3\), Taylor expansion shows \(A\equiv g_1(1)\equiv1\pmod9\).

Expanding around either critical point, with \(t=\beta_\varepsilon+3s\), gives an integral convergent expansion
\[
g_\varepsilon(t)=A_\varepsilon+9U_\varepsilon s^2(1+3h_\varepsilon(s)),
\quad U_\varepsilon=\frac{g_\varepsilon''(\beta_\varepsilon)}2\equiv2\pmod3,
\]
where \(h_\varepsilon\) is integral and Lipschitz on \(\mathbb Z_3\). The unique square root of \(1+3h_\varepsilon(s)\) congruent to one modulo three yields an isometric coordinate \(H_\varepsilon(s)=s\sqrt{1+3h_\varepsilon(s)}\). Since \(U_\varepsilon/2\equiv1\pmod3\) is a unit square, the exact critical image is \(A_\varepsilon+18\mathbb Z_3^2\). The even critical image \(18\mathbb Z_3^2\) lies in the regular odd image \(3\mathbb Z_3\). The odd critical image \(A+18\mathbb Z_3^2\) lies in \(1+9\mathbb Z_3\), disjoint from both regular balls. This proves the claimed union.

**4. Complete fibers.** A regular isometry between a ball of radius \(1/3\) and its image ball contributes exactly one preimage modulo \(3^k\). For \(k\ge2\), a critical branch evaluates \(t=\beta_\varepsilon+3s\), with \(s\) modulo \(3^{k-1}\), while the square condition is only modulo \(3^{k-2}\); thus each square root counted by \(R_{k-2}\) lifts to three original indices per branch. Adding both regular contributions gives the displayed exact formula. For \(k=1\), direct evaluation of both three-element index branches gives \((3,1,2)\). The zero fiber is \(2+3R_{k-2}(0)=2+3^{\lfloor k/2\rfloor}\).

**5. Image size, measure, and least period.** The two full residue balls contribute \(2\cdot3^{k-1}\) values. The disjoint odd critical sheet contributes exactly \(S_{k-2}\) values for \(k\ge2\). Squares in \(\mathbb Z_3\) have Haar measure \(\sum_{a\ge0}(1/3)\cdot3^{-2a}=3/8\); its affine sheet \(A+18\mathbb Z_3^2\) has measure \((1/9)(3/8)=1/24\). Total measure is \(2/3+1/24=17/24\).

Modulo three the tail on indices \(n=0,1,\ldots,5\pmod6\) has pattern \((2,0,0,1,2,0)\), of least period six. Any eventual period \(T\) must therefore be even, with \(T/2\) divisible by three. The regular even branch is an isometry on \(t\equiv0\pmod3\), hence equality of its values after shifting by \(T/2\) modulo \(3^k\) forces \(3^k\mid T/2\). Therefore the upper bound \(2\cdot3^k\) on period is sharp.

## Verification

The accompanying standalone `check.py` uses only the Python standard library. It verifies the Eulerian closed form against the Eulerian recurrence for 90 initial indices; independently computes the odd critical point and value from the convergent logarithm and Hensel lifting; exhaustively checks every residue fiber and support size for \(1\le k\le8\); and independently compares each eventual period with the original integer formula. It passed 29,634 exact assertions. These finite checks corroborate, but do not replace, the analytic proofs for all depths.

## Relationship to prior work

Xiong, Tsao and Hall (2013) give the Eulerian recurrence and explicit counting formulas, which establish the object but not a \(3\)-adic value-set classification. Krattenthaler and Müller (2013) study ternary congruences of several recursively defined sequences; their Eulerian application concerns central Eulerian numbers rather than the fixed two-descent column. Castro, González and Medina (2015) study the \(p\)-adic valuations of Eulerian numbers. Their abstract does not imply the complete ternary image-and-fiber law here; their full text was not available for comparison, leaving a genuine historical-priority risk. The OEIS entry A000460 lists the underlying two-descent sequence but not the present all-depth sheet-and-fiber theorem. The explicitly related two-descent dyadic result describes a different prime, whose residue conclusions do not imply these ternary assertions. No assertion of independently certified novelty is made.

## Limitations

The classification concerns all residues attained infinitely often in the eventually periodic tail, not necessarily every value attained at isolated initial indices. The critical value \(A\) is defined uniquely analytically and can be computed modulo any prescribed power, but no simpler closed form is asserted. The proof is specific to the fixed two-descent Eulerian column at the prime three. Finite checker tests are not infinite proof. The closest valuation-focused paper's full text could not be inspected; a previously implicit theorem cannot be ruled out. Independent mathematical validation has not been performed.

## References

1. T. Xiong, H.-P. Tsao and J. I. Hall, “General Eulerian Numbers and Eulerian Polynomials,” *Journal of Mathematics* (first published 31 January 2013), DOI: https://doi.org/10.1155/2013/629132.
2. C. Krattenthaler and T. W. Müller, “A method for determining the mod-\(3^k\) behaviour of recursive sequences,” arXiv:1308.2856 (first submitted 13 August 2013), https://arxiv.org/abs/1308.2856.
3. F. N. Castro, O. E. González and L. A. Medina, “The p-adic Valuation of Eulerian Numbers: Trees and Bernoulli Numbers,” *Experimental Mathematics* 24 (2015), 183–195, DOI: https://doi.org/10.1080/10586458.2014.981899 (abstract and bibliography inspected; full text unavailable).
4. OEIS A000460, “Eulerian numbers (Euler's triangle),” https://oeis.org/A000460 (underlying sequence only).
