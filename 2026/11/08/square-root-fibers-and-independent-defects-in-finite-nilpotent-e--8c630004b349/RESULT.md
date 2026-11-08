# Square-root fibers and independent defects in finite nilpotent endomorphism rings

## Finding
Let \(q\) be any prime power, \(n\geq1\), and \(R=\mathbb F_q[t]\). Set
\[
M_n=(R/(t^2))^n\oplus (R/(t))^n,\qquad E_n=\operatorname{End}_R(M_n).
\]
The endomorphism \(T\) given by multiplication by \(t\) belongs to the center of \(E_n\). For the quadratic fiber \(\mathcal Q_n=\{X\in E_n:X^2=T\}\), all solutions are nilpotent, and the possible \(\mathbb F_q\)-linear Jordan types of \(X\) are, uniquely,
\[
4^r3^{n-2r}2^s1^{2(r-s)},\qquad 0\leq s\leq r\leq\lfloor n/2\rfloor.
\]
(Exponents here denote multiplicities of Jordan blocks, not powers of an element.) Put \(D_j(q)=\prod_{i=1}^j(1-q^{-i})\), with \(D_0(q)=1\). The exact number of solutions with this Jordan type is
\[
H_{n,r,s}(q)=q^{5n^2-L_{n,r,s}}
\frac{D_n(q)^2}{D_r(q)D_{n-2r}(q)D_s(q)D_{2(r-s)}(q)},
\]
where
\[
L_{n,r,s}=(n+r-s)^2+(n+s-r)^2+(n-r)^2+r^2.
\]
Each such solution has \(\operatorname{rank}(X)=2n-r+s\) and \(\operatorname{rank}(X^3)=r\); therefore these formulas give the entire rank-and-cubic-rank spectrum.

For a uniformly sampled \(X\in\mathcal Q_n\), define its two defects by
\[
U_n=n/2-\operatorname{rank}(X^3),\qquad
V_n=2n-\operatorname{rank}(X).
\]
Fix \(q\), restrict \(n\) to one parity \(\epsilon\in\{0,1\}\), and put
\[
Z_{q,\epsilon}=\sum_{u\in\{\epsilon/2,\epsilon/2+1,\ldots\}}\frac{q^{-2u^2}}{D_{2u}(q)},\qquad
T_q=\sum_{d=0}^{\infty}\frac{q^{-2d^2}}{D_{2d}(q)}.
\]
Then \((U_n,V_n)\) converges in total variation, with error \(O_q(q^{-n/4})\), to two **independent** variables whose respective masses at \(u,d\) are
\[
\frac{q^{-2u^2}}{D_{2u}(q)Z_{q,\epsilon}},\qquad
\frac{q^{-2d^2}}{D_{2d}(q)T_q}.
\]
In particular, for either parity,
\[
\lim_{n\to\infty}\Pr(\operatorname{rank}(X)=2n)=T_q^{-1},
\]
and the total root count is
\[
|\mathcal Q_n|=q^{5n^2/2}Z_{q,\epsilon}T_q\left(1+O_q(q^{-n/4})\right).
\]
The limiting maximal-rank probability is approximately \(0.5954585268\) for \(q=2\) and \(0.8419135286\) for \(q=3\). The exact counting statement and the independent limiting-defect law form one combined result concerning the quadratic fibers of these endomorphism rings.

## Assumptions and scope
All modules, vector spaces, rings, and maps are finite over \(\mathbb F_q\). The endomorphism ring \(E_n\) consists of \(R\)-linear maps, while the ranks and Jordan types are measured on its underlying \(3n\)-dimensional \(\mathbb F_q\)-space. The field characteristic is arbitrary. The parameter \(q\) is fixed in asymptotic assertions. Expressions involving \(n/2\) are ordinary rational or real expressions, allowing half-integer \(U_n\) when \(n\) is odd. The notation \(O_q\) allows constants depending on fixed \(q\) but not on \(n\).

## Proof
**1. Classification of possible types.** If \(X^2=T\), then \(X\) commutes with \(T\) and is already an element of \(E_n\), while \(X^4=T^2=0\). Thus every Jordan block of \(X\) has length at most four. Squaring a nilpotent block of lengths \(1,2,3,4\) gives, respectively, the block types \(1\), \(1+1\), \(2+1\), and \(2+2\). Let \(c_j\) be the number of length-\(j\) blocks of \(X\). The \(n\) length-two and \(n\) length-one blocks of \(T\) force
\[
2c_4+c_3=n,\qquad c_3+2c_2+c_1=n.
\]
Set \(r=c_4\) and \(s=c_2\). The equations give \(c_3=n-2r\), \(c_1=2(r-s)\), and the stated inequalities. Conversely, each such tuple constructs a nilpotent block sum whose square has exactly the type of \(T\). Conjugating this square to \(T\) produces a root in \(E_n\).

**2. A single orbit for each type.** All roots of the same Jordan type are conjugate in \(\operatorname{GL}_{3n}(\mathbb F_q)\), by Jordan normal form. If \(gXg^{-1}=Y\) and \(X^2=Y^2=T\), squaring shows \(gTg^{-1}=T\). Thus the conjugating map belongs to \(E_n^\times\), the units of the endomorphism ring. Conversely, units of \(E_n\) preserve the equation. Hence the roots of each type constitute one \(E_n^\times\)-conjugacy orbit, with stabilizer the full unit centralizer of \(X\).

**3. Unit-centralizer order.** For any nilpotent Jordan type with \(c_j\) blocks of size \(j\), set \(m_i=\sum_{j\geq i}c_j\). Its centralizer endomorphism algebra is \(\operatorname{End}_{\mathbb F_q[t]}(\bigoplus_j(R/t^j)^{c_j})\). Since \(\dim_{\mathbb F_q}\operatorname{Hom}_R(R/t^a,R/t^b)=\min(a,b)\), the algebra dimension is \(\sum_i m_i^2\). Its quotient by the Jacobson radical is \(\prod_jM_{c_j}(\mathbb F_q)\): endomorphisms between nonisomorphic indecomposable length blocks are radical, and endomorphisms of a fixed block length reduce to their constant coefficients. An element is a unit precisely when all of its images in these matrix factors are units. Therefore
\[
|C_{\operatorname{GL}}(X)|=q^{\sum_i m_i^2}\prod_jD_{c_j}(q).
\]
For \(T\), the conjugate block-column lengths are \((2n,n)\), so \(|E_n^\times|=q^{5n^2}D_n(q)^2\). For a root indexed by \((r,s)\), the column lengths are
\[
(n+r-s,\ n+s-r,\ n-r,\ r).
\]
Orbit–stabilizer gives exactly \(H_{n,r,s}(q)\). The number of blocks is \(n+r-s\); subtracting this from dimension \(3n\) gives rank \(2n-r+s\). Only length-four blocks survive cubing, giving cubic rank \(r\).

**4. Independent defect asymptotics.** Put \(u=n/2-r\) and \(d=r-s\). These lie in \(u\in\{\epsilon/2,\epsilon/2+1,\ldots\}\), \(d\in\mathbb N_0\), and \(u+d\leq n/2\). Substitution into the exact formula yields
\[
H_{n,u,d}(q)=q^{5n^2/2-2u^2-2d^2}
\frac{D_n(q)^2}{D_{n/2-u}(q)D_{n/2-u-d}(q)D_{2u}(q)D_{2d}(q)}.
\]
The finite product \(D_j(q)\) decreases to the positive constant \(D_\infty(q)=\prod_{i\geq1}(1-q^{-i})\), and \(D_j(q)/D_\infty(q)=1+O_q(q^{-j})\). On the region \(u+d\leq n/4\), both large-denominator indices are at least \(n/4\); uniformly there,
\[
\frac{D_n(q)^2}{D_{n/2-u}(q)D_{n/2-u-d}(q)}=1+O_q(q^{-n/4}).
\]
Every remaining factor of this ratio is uniformly bounded above and below by positive constants depending on \(q\). Outside that region, \(u^2+d^2\geq (u+d)^2/2>n^2/32\), so the total omitted Gaussian-weight tail is \(O_q(q^{-n^2/20})\), including its polynomially many possible terms. Extending the sum over admissible pairs to independent infinite half-lattice sums changes it by the same negligible amount. After dividing by the total mass, we obtain the stated product distribution and total-variation error \(O_q(q^{-n/4})\). Summing without division gives the total-root asymptotic. Because \(d=V_n\), its zero-mass tends to \(T_q^{-1}\), as claimed.

## Verification
The independent standalone file `verify.py` re-derives exact counts by the orbit-centralizer formula and checks that they are integers. Direct exhaustive enumeration of the full commutant checks all roots for \(n=1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and for \(n=2\) over \(\mathbb F_2\). The observed three strata for \(n=2,q=2\) are \((r,s)=(0,0),(1,0),(1,1)\) with multiplicities \(96,192,576\); their sum is \(864\). It additionally computes exact closed-form strata for \(n=3,4\) and \(q=2,3\), and checks convergent-series numerics separately. Execute `python verify.py` using a standard Python 3 interpreter; success prints `VERIFY_OK`. Exhaustive finite cases do not prove the arbitrary-\(n\) or limiting assertions, which are proved above.

## Relationship to prior work
Öztürk (2021), Theorem 1.1, provides general necessary and sufficient conditions for **which Jordan types** admit matrix roots; this supplies prior existence/type theory and does not enumerate distinct root operators or supply a limiting probability law. The current classification of admissible root types follows that established mechanism. Mingueza, Montoro, and Roca (2019) give centralizer structures and dimension/determinant formulas; the unit-centralizer order and orbit-stabilizer argument use standard consequences of that structure rather than claiming a new centralizer theorem. Bogdanić et al. (2022) study nilpotent matrices in centralizers for two equal-size blocks, not square-root fibers for the \((2^n,1^n)\) module family. The evaluated addition is the **exact rank-refined fiber law and independent two-defect asymptotic with quantitative rate**, not the general Jordan-root existence criterion, nilpotent conjugacy, or centralizer-unit formula.

## Limitations
The formulas concern the specific finite-length module family \((R/t^2)^n\oplus(R/t)^n\), the quadratic equation \(X^2=T\), and uniformly sampled **individual endomorphisms**, not conjugacy classes; extensions to arbitrary block multiplicities, other polynomial equations, or growing \(q\) are not established. The independent limits arise only along a fixed parity for the first defect (the rank deficit has the same limit along both parities). A comprehensive priority search cannot exclude a broader finite-field matrix-root enumeration or a general asymptotic orbit theorem implying part of the result. No external independent mathematical audit has been performed.

## References
1. S. Öztürk, *On m-th roots of nilpotent matrices*, Electronic Journal of Linear Algebra **37** (2021), 718–733, DOI: https://doi.org/10.13001/ela.2021.6331 (journal public posting December 14, 2021).
2. D. Mingueza, M. E. Montoro, and A. Roca, *The centralizer of an endomorphism over an arbitrary field*, arXiv:1909.06198 (first posted September 2019), https://arxiv.org/abs/1909.06198.
3. T. Bogdanić et al., *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (2022), https://arxiv.org/abs/2212.08425.
