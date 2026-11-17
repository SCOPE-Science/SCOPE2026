# The sharp entropy lens for simultaneous first and second Cesàro cluster values

## Finding
Let \(x=(x_j)_{j\geq1}\) be an arbitrary infinite binary sequence, and write \(u_n=(Cx)_n\), \(v_n=(C^2x)_n\) for its first and second prefix-Cesàro averages. Define
\[
 L(u)=u+(1-u)\log(1-u),\qquad U(u)=u(1-\log u),\qquad 0\leq u\leq1,
\]
with the continuous convention \(0\log0=0\). The exact universal joint cluster region is
\[
 \mathcal R=\{(u,v):0\leq u\leq1,\ L(u)\leq v\leq U(u)\}.
\]
Every subsequential limit of \((u_n,v_n)\), for every binary input, lies in \(\mathcal R\). Conversely, a dense \(G_\delta\) subset of the compact binary sequence space has **all** of \(\mathcal R\) as its joint cluster set. In particular every point of \(\mathcal R\) is simultaneously attainable as a subsequential limit along a single binary sequence, and no point outside it is attainable.

The vertical width is **exactly binary entropy in natural logarithms**:
\[
 U(u)-L(u)=-u\log u-(1-u)\log(1-u),
\]
with unique maximum \(\log2\) at \(u=1/2\).

There is also a sharp finite-length version. Let \(H_m=\sum_{r=1}^m1/r\) for \(m\geq1\), and \(H_0=0\). At any fixed length \(n\) and exactly \(k\) ones, \(0\leq k\leq n\), the exact minimum and maximum of \(v_n\) are respectively
\[
 v_{n,\min}(k)=\frac{k}{n}-\frac{n-k}{n}(H_n-H_{n-k}),\qquad
 v_{n,\max}(k)=\frac{k}{n}(1+H_n-H_k).
\]
They are attained by putting all ones at the end or at the beginning, respectively; for \(0<k<n\) these arrangements are uniquely extremizing. Writing \(u=k/n\), the uniform continuum-envelope errors satisfy
\[
 0\leq v_{n,\min}(k)-L(u)\leq\frac1n,\qquad
 0\leq U(u)-v_{n,\max}(k)\leq\frac1n.
\]
Thus the finite admissible vertical width differs from the binary-entropy width by at most \(2/n\).

## Assumptions and scope
The input alphabet is exactly \(\{0,1\}\); limits are taken with respect to the coordinate index \(n\to\infty\), with the Cesàro iteration order fixed at one or two. All logarithms are natural. \(\{0,1\}^{\mathbb N}\) has its product (Cantor) topology. A cluster point of \((u_n,v_n)\) is a limit along a strictly increasing sequence of coordinate indices. The formulas for \(k=0\) and \(k=n\) use the displayed harmonic-number conventions.

## Proof
**1. Exact finite weights and extremizers.** Changing the order of summation gives
\[
 v_n=\frac1n\sum_{r=1}^n\frac1r\sum_{j=1}^r x_j
     =\sum_{j=1}^n w_{n,j}x_j,\qquad
 w_{n,j}=\frac{H_n-H_{j-1}}n.
\]
The weights are strictly decreasing in \(j\), since \(w_{n,j}-w_{n,j+1}=1/(nj)>0\). For a binary word containing exactly \(k\) ones, the elementary exchange argument therefore places all ones in the first \(k\) positions to maximize the sum, and in the last \(k\) to minimize it, uniquely for interior \(k\). Direct telescoping yields
\[
 \sum_{j=1}^k w_{n,j}=\frac{k}n(1+H_n-H_k),\quad
 \sum_{j=n-k+1}^n w_{n,j}=\frac{k}n-\frac{n-k}n(H_n-H_{n-k}),
\]
proving both finite formulas.

**2. Uniform logarithmic envelopes.** For integers \(1\leq m\leq n\), comparison of \(1/t\) on consecutive unit intervals gives
\[
 0\leq\log(n/m)-(H_n-H_m)\leq1/m.
\]
For \(u=k/n\), the preceding exact formulas imply, when \(0<k<n\),
\[
 U(u)-v_{n,\max}(k)=\frac{k}n\big[\log(n/k)-(H_n-H_k)\big]\in[0,1/n],
\]
\[
 v_{n,\min}(k)-L(u)=\frac{n-k}n\big[\log(n/(n-k))-(H_n-H_{n-k})\big]\in[0,1/n].
\]
At the endpoints these differences vanish. Consequently every binary word satisfies \(L(u_n)\leq v_n\leq U(u_n)\) **at each finite index**, and therefore every joint cluster point belongs to the closed set \(\mathcal R\).

**3. Every point of the region is approachable after any finite prefix.** For \(0<u<1\) and \(0\leq a\leq1-u\), let
\[
 F_u(a)=\int_a^{a+u}-\log t\,dt
       =U(a+u)-U(a).
\]
This is continuous and strictly decreasing in \(a\), with \(F_u(0)=U(u)\) and \(F_u(1-u)=L(u)\); the last equality follows by integrating the final \(u\)-portion of \([0,1]\). Hence every \((u,v)\in\mathcal R\) admits an interval \([a,a+u]\subseteq[0,1]\) with \(F_u(a)=v\). The cases \(u=0,1\) follow by choosing all zero or all one inputs.

Fix an arbitrary binary prefix of length \(M\). For any sufficiently large \(N\), fill the remaining positions with ones precisely where \(j/N\in(a,a+u]\) and zeros elsewhere. The arbitrary prefix contributes at most \(M/N\) to \(u_N\) and at most
\[
 \sum_{j=1}^M w_{N,j}=\frac{M}N(1+H_N-H_M)
 \leq\frac MN\big(1+\log(N/M)\big)
\]
to \(v_N\) for \(M\geq1\). Both contributions tend to zero. On the chosen interval, the exact upper-prefix identity in Step 1 and its \(1/N\) envelope from Step 2 show that the second average tends to
\(U(a+u)-U(a)=v\); simultaneously the fraction of chosen sites tends to \(u\). Thus arbitrarily late pairs can approach \((u,v)\) as accurately as desired without altering any prescribed initial digits.

**4. One residual set attains the whole region.** Let \((q_s)_{s\geq1}\) be a countable dense subset of \(\mathcal R\). For positive integers \(s,m,N_0\), the set of binary sequences having some \(n\geq N_0\) with \(\|(u_n,v_n)-q_s\|_\infty<1/m\) is open: it depends on only finitely many digits for each fixed \(n\). It is dense by Step 3. By the Baire category theorem their countable intersection is a dense \(G_\delta\). Every sequence in that intersection has every \(q_s\) as a subsequential cluster point, and its cluster set is closed because \((u_n,v_n)\) lies in the compact square \([0,1]^2\). Step 2 confines that set to \(\mathcal R\), so it equals \(\mathcal R\).

**5. Entropy width.** Subtracting the definitions gives \(U(u)-L(u)=-u\log u-(1-u)\log(1-u)\); its derivative is \(\log((1-u)/u)\), and its second derivative is \(-1/u-1/(1-u)<0\). Therefore the unique maximizer is \(u=1/2\), with maximum \(\log2\). The finite error in the extremal width is at most \(2/n\) by Step 2. This finishes the proof.

## Verification
The included Python checker uses exact rational arithmetic to enumerate all \(65,534\) binary words of lengths \(1\) through \(15\), checks the harmonic-number extrema, and tests the finite envelope inequalities. It also checks contiguous interval approximations and the entropy-width identity numerically for selected larger sizes. Run `python check_cesaro_joint_region.py` with Python 3 and no external packages. The infinite-sequence and dense-\(G_\delta\) assertions follow analytically from Steps 1–5, not from the enumerations.

## Relationship to prior work
Douvropoulos, *Simultaneous generic approximation by the iterates of the Cesaro operator* (2012), proves separate dense-approximation properties for bounded alphabets and simultaneous unrestricted target approximation when the alphabet's convex hull is dense in the ambient vector space. Its Proposition 4.12 gives a **nonsharp bounded-alphabet obstruction**, namely that a small first Cesàro average prevents the second from lying near one. The present statement instead computes the entire **sharp binary two-coordinate attainable region**, both exact finite extrema and joint residual attainability; it does not claim the general result for arbitrary vector alphabets or all iteration orders.

Olsen and West (2020) establish generic maximal oscillation of separately averaged digit-frequency vectors for general averaging systems, including higher-order Cesàro systems. Their individual-order oscillation conclusions do not identify the joint first-versus-second coordinate compatibility lens. Galaz-Fontes and Solis (2008) study convergence as the **iteration order** tends to infinity, a different limit than the fixed-order, growing-coordinate cluster values here; only its accessible abstract was compared, not its full text.

## Limitations
The sharp lens is proved only for two fixed Cesàro orders and binary inputs. The first/second compatibility for a general finite alphabet, three or more simultaneous orders, or arbitrary averaging matrices is not determined. Unindexed equivalent work remains a historical-priority risk. The generic result is topological and does not describe the probability measure of its residual set.

## References
1. T. Douvropoulos, *Simultaneous generic approximation by the iterates of the Cesaro operator*, arXiv:1211.0783v1 (first publicly submitted 2012-11-05), especially Introduction, Proposition 2.1 and Proposition 4.12. https://arxiv.org/html/1211.0783v1
2. L. Olsen and M. West, *Average frequencies of digits in infinite IFS’s and applications to continued fractions and Lüroth expansions*, Monatshefte für Mathematik 193 (2020), 441–478, DOI 10.1007/s00605-020-01457-w. https://link.springer.com/article/10.1007/s00605-020-01457-w
3. F. Galaz-Fontes and F. J. Solis, *Iterating the Cesàro operators*, Proceedings of the American Mathematical Society 136 (2008), 2147–2153, DOI 10.1090/S0002-9939-08-09197-1. (Abstract-only comparison.)
