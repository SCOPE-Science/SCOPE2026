# Moment filtration and rank-one synthesis in critical Gaussian Fock integral shifts

## Finding

Let \(\mathcal F^2\) be the classical one-variable Gaussian Bargmann–Fock Hilbert space. For integers \(m\ge1\) and \(j\ge0\) define on polynomials, then extend boundedly,
\[
A_{m,j}=I^{m+j}M_{z^m}D^j,
\qquad (If)(z)=\int_0^z f(w)\,dw,\qquad Df=f'.
\]
Every \(A_{m,j}\) is a noncompact forward shift by \(2m\) monomial degrees. Fix \(m\ge1\), and for any nonzero, finitely supported complex vector \(c=(c_0,\ldots,c_J)\), put
\[
T_c=\sum_{j=0}^{J}c_jA_{m,j},\qquad
M_r(c)=\sum_{j=0}^{J}c_jj^r\quad(r\ge0),
\]
where the zeroth power is understood to equal one, including at zero. Precisely one of the following holds.

1. If \(M_0(c)\ne0\), then \(T_c\) is noncompact and its essential norm is \(\lvert M_0(c)\rvert\).
2. If \(q\in\{1,\ldots,m\}\) is the smallest index with \(M_q(c)\ne0\), then \(T_c\) is compact and infinite rank, with sharp singular-value law
\[
s_n(T_c)\sim \binom mq\lvert M_q(c)\rvert n^{-q}.
\]
It belongs to the Schatten (quasi-)ideal \(\mathcal S_p\) exactly for \(p>1/q\), for every \(p>0\), and lies in \(\mathcal S_{1/q,\infty}\setminus\mathcal S_{1/q}\). Its logarithmic endpoint coefficient is
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^{N}s_n(T_c)^{1/q}
=\left(\binom mq\lvert M_q(c)\rvert\right)^{1/q}.
\]
3. If \(M_0(c)=\cdots=M_m(c)=0\), then \(T_c\) is nonzero and finite rank. Writing
\[
C_c(t)=\sum_{j=0}^{J}c_jt^j=(1-t)^{m+1}B_c(t),\qquad B_c(t)=\sum_{h\ge0}b_ht^h,
\]
with \(B_c\) a polynomial, its complete nonzero singular-value multiset is
\[
\left\{\frac{m!\lvert b_h\rvert}{\sqrt{(h+1)(h+2)\cdots(h+2m)}}:\ b_h\ne0\right\}.
\]
In particular, \(\operatorname{rank}(T_c)\) equals the number of nonzero coefficients of \(B_c\).

The universal finite-difference family makes each transition explicit. For \(h\ge0\) and \(0\le q\le m+1\), set
\[
B_{m,h,q}=\sum_{r=0}^{q}(-1)^r\binom qr A_{m,h+r}.
\]
For \(0\le q\le m\), its complete monomial action is
\[
B_{m,h,q}e_k=\mathbf1_{k\ge h}
\frac{m!}{(m-q)!}
\frac{\prod_{s=1}^{m-q}(k-h+s)}{\sqrt{\prod_{s=1}^{2m}(k+s)}}\,e_{k+2m},
\]
where empty products are one. At the next difference order the infinite-dimensional tail disappears *exactly*:
\[
\boxed{ B_{m,h,m+1}e_k=\begin{cases}
\displaystyle\frac{m!}{\sqrt{\prod_{s=1}^{2m}(h+s)}}e_{h+2m},&k=h,\\[5pt]
0,&k\ne h.
\end{cases}}
\]
Thus the \((m+1)\)-st difference of noncompact critical integration operators is a nonzero rank-one operator, and these rank-one operators linearly generate every finite-rank element in their fixed-\(m\) finite span.

## Assumptions and scope

Use \(\|f\|_{\mathcal F^2}^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\) and orthonormal monomials \(e_k(z)=z^k/\sqrt{k!}\) for \(k\ge0\). All integrations start at zero, all derivatives are ordinary complex derivatives, and all operator sums are finite. The monomial degree \(m\ge1\) is fixed within each linear span, while the integration order \(m+j\) varies with \(j\). Coefficients may be complex. Singular values are counted with multiplicity and in nonincreasing order; \(p\) can be below one. The theorem is confined to the classical Gaussian Hilbert Fock space, not general Fock–Sobolev norms.

## Proof

**1. Exact shift formula.** Differentiating, multiplying and integrating an orthonormal monomial gives, for every \(k\ge0\),
\[
A_{m,j}e_k=w_{m,j}(k)e_{k+2m},\quad
w_{m,j}(k)=\begin{cases}
\displaystyle\frac{\prod_{s=1}^{m}(k-j+s)}{\sqrt{\prod_{s=1}^{2m}(k+s)}},&k\ge j,\\[5pt]
0,&k<j.
\end{cases}
\]
The weights are bounded and tend to one as \(k\to\infty\). Their output indices are distinct for distinct inputs. Thus the polynomial restriction has a unique bounded extension, and each \(A_{m,j}\) is noncompact. This exact individual-weight identity is also part of the starting literature, not claimed as new.

**2. A polynomial controls the entire high-degree tail.** Define
\[
P_m(X)=\prod_{s=1}^m(X+s),\qquad
Q_c(X)=\sum_{j=0}^{J}c_jP_m(X-j),\qquad
H_m(k)=\sqrt{\prod_{s=1}^{2m}(k+s)}.
\]
For \(k\ge J\), the weighted-shift coefficient of \(T_c\) is exactly \(Q_c(k)/H_m(k)\). Expand \(P_m(X-j)\) as a polynomial in \(X\) and \(j\). Its coefficient of \(X^{m-r}\) is a polynomial in \(j\) of degree at most \(r\), with leading coefficient \((-1)^r\binom mr\). If \(M_0(c),\ldots,M_{q-1}(c)\) vanish and \(M_q(c)\ne0\) for \(q\le m\), the polynomial \(Q_c\) has degree precisely \(m-q\), with leading coefficient \((-1)^q\binom mq M_q(c)\). Since \(H_m(k)=k^m(1+O(k^{-1}))\),
\[
\frac{Q_c(k)}{H_m(k)}=(-1)^q\binom mq M_q(c)k^{-q}+O(k^{-q-1}).
\]
This argument is exact polynomial algebra and does not assume that the weights at low indices equal the polynomial continuation.

**3. Essential norm and Schatten thresholds.** For any diagonal-coordinate forward shift \(We_k=d_ke_{k+2m}\), one has \(W^*We_k=|d_k|^2e_k\). Therefore the singular values are exactly the decreasing rearrangement of \((|d_k|)\), and its essential norm is \(\limsup_{k\to\infty}|d_k|\). When \(q=0\), the tail tends to \(M_0(c)\), proving case 1. For \(1\le q\le m\), the tail is nonzero and asymptotic in modulus to \(\binom mq|M_q(c)|k^{-q}\); rearrangement preserves that asymptotic, by comparison of counting functions with power sequences. Summing its \(p\)-th powers gives the sharp \(p>1/q\) cutoff. At \(p=1/q\), its critical powers are asymptotic to a positive constant divided by \(k\); the harmonic-sum limit gives the stated coefficient.

**4. Finite differences, including the low-degree boundary.** For integers \(h\ge0\) and \(0\le q\le m\), the polynomial identity
\[
\sum_{r=0}^{q}(-1)^r\binom qr P_m(X-r)
=\frac{m!}{(m-q)!}\prod_{s=1}^{m-q}(X+s)
\]
is the elementary backward-difference identity for rising factorials. Substituting \(X=k-h\) yields the displayed formula whenever all derivative terms exist. When \(k\ge h\) but some \(r>k-h\) has \(h+r>k\), the omitted term \(P_m(k-h-r)\) is zero whenever \(1\le r-(k-h)\le m\). This includes all omitted terms for \(q\le m\), so the identity is valid at **every** input degree. When \(q=m+1\), its polynomial difference is identically zero for \(k\ge h+1\); at \(k=h\), only the first term remains and equals \(P_m(0)=m!\); for \(k<h\), every derivative vanishes. The announced rank-one identity follows without any limiting argument.

**5. Complete finite-rank classification.** The change of basis from the ordinary powers \(j^r\) to falling factorials implies that \(M_0(c)=\cdots=M_m(c)=0\) if and only if \(C_c(t)\) has a root of multiplicity at least \(m+1\) at \(t=1\). Therefore \(C_c(t)=(1-t)^{m+1}B_c(t)\) with a *unique polynomial* \(B_c(t)=\sum_h b_ht^h\). Compare coefficients of powers of \(t\) to obtain the exact operator identity
\[
T_c=\sum_{h\ge0}b_hB_{m,h,m+1}.
\]
The rank-one terms have mutually orthogonal input and output monomials. Their nonzero singular values are thus exactly the stated finite list, and their count is the rank. Since \(c\ne0\), also \(B_c\ne0\), hence \(T_c\ne0\). Conversely, if \(T_c\) is compact and has finite rank, its tail is eventually zero. The nonzero polynomial \(Q_c\) cannot vanish at all sufficiently large integers, so \(Q_c\equiv0\), which by the triangular coefficient argument of Step 2 is equivalent to vanishing of all moments through \(m\). This completes the three-way classification.

## Verification

The standalone standard-library program `CHECK.py` verifies the exact finite-difference monomial numerator over all integers \(1\le m\le9\), \(0\le h\le7\), \(0\le q\le m+1\), \(0\le k\le44\) (22,680 identities), and checks 312 moment/degree cancellation instances. It additionally verifies 924 exact-integer polynomial-quotient rank-one synthesis cases. Run `python3 CHECK.py`; it uses exact integer arithmetic and has no external dependencies. These are finite consistency checks only. Every infinite-dimensional and asymptotic assertion follows from the displayed polynomial and spectral arguments above.

## Relationship to prior work

Dong and Hu (2026, arXiv:2611.01959v1, especially their monomial formula (50) and Section 4) establish individual generalized Fock–Sobolev integration weights, boundedness, compactness and essential norms for a **fixed** integration order. The individual-weight formula in Step 1 is therefore known. The present theorem instead combines *different* integration orders \(m+j\), classifies the resulting cancellations at every moment order, gives sharp ideal exponents, and synthesizes explicit rank-one operators. Its conclusion is not furnished by the cited fixed-order classification.

Published work on commutators of two critical Gaussian Fock integration shifts studies singular-value decay of operator **products' commutator**, including a resonance between quadratic and cubic decay. The objects here are linear superpositions, not commutators; the relevant published commutator statement does not provide the polynomial-quotient finite-rank classification. Alpay, Cerejeiras, Kähler and Kling (2022) likewise study Fock commutator calculus rather than these cross-order linear combinations. Mengestie (2017) and Biya (2023) address Schatten properties of individual Volterra/generalized integration operators, without the present complete moment hierarchy in the inspected portions. The present rank-one identity can be checked independently by elementary rising-factorial calculus, so no unverified general symbolic-calculus theorem is needed for correctness.

## Limitations

Only finite linear combinations, a fixed positive monomial degree, and classical Gaussian Fock space are treated. No statement is made about arbitrary entire symbols, multidimensional Fock spaces or infinite coefficient sums. The exact rank-one identity is an algebraic consequence of finite differences, and its potential appearance elsewhere under a different operator-theoretic name is a remaining publication-priority risk. The 2023 thesis was inspected in text form; a separate page-image request did not complete. No independent audit or external mathematical certification has been conducted.

## References

1. J. Dong and S. Hu, *Carleson Measures and Integral Operators on Fock–Sobolev Spaces*, arXiv:2611.01959v1 (first submitted 2026-11-01), especially Section 4 and formula (50). https://arxiv.org/html/2611.01959v1
2. D. Alpay, P. Cerejeiras, U. Kähler, and T. Kling, *Commutators on Fock spaces*, arXiv:2208.03394v1 (2022). https://arxiv.org/html/2208.03394v1
3. T. Mengestie, *Spectral properties of Volterra-type integral operators on Fock–Sobolev spaces*, arXiv:1702.08157v1 (2017). https://arxiv.org/html/1702.08157v1
4. K. Biya, *Schatten Class Generallized Integration Operators on Fock Spaces*, M.Sc. thesis, Jimma University (2023), especially Theorem 4.0.6. https://repository.ju.edu.et/handle/123456789/8787
