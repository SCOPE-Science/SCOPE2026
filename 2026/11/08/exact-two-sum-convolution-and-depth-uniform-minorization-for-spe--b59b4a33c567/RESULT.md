# Exact two-sum convolution and depth-uniform minorization for special-linear matrices over odd prime-power rings

## Finding

Let \(p\ge3\) be prime, \(k\ge2\), and \(R_k=\mathbb Z/p^k\mathbb Z\). Put \(G_k=\mathrm{SL}_2(R_k)\), viewed as a subset of the *additive* four-dimensional group \(M_2(R_k)\), and define the ordered pair-sum representation function
\[
r_k(S)=\#\{(A,B)\in G_k^2:A+B=S\}.
\]
The theorem below determines \(r_k(S)\) at **every matrix** in terms of the valuation of its entries, the determinant of its primitive reduction, and explicit quadratic-root counts. Its sharp global consequence is
\[
\min_{S\in M_2(R_k)} r_k(S)=p^{2k-1}(p-1)>0,
\]
and the exact number of matrices attaining the minimum is
\[
\frac{(p-1)(p+1)(p^2+p+2)}2\,p^{4k-4}.
\]
Consequently the two-sum set is the **whole** matrix ring. More sharply, if \(\mu_k\) is uniform probability on \(G_k\) and \(u_k\) uniform probability on \(M_2(R_k)\), then
\[
\mu_k*\mu_k(S)\ge \frac{p^3}{(p-1)(p+1)^2}\,u_k(S)
\]
for all \(S\), with the constant sharp and independent of depth \(k\).

## Assumptions and scope

For \(a\in R_k\), let \(v_p(a)\in\{0,\ldots,k\}\) be the largest \(s\) such that \(p^s\mid a\), with \(v_p(0)=k\). Let \(\chi_p\) denote the Legendre symbol, with \(\chi_p(a)=0\) if \(p\mid a\). For a target \(S\in M_2(R_k)\), define \(j\) as the minimum valuation of its four entries. If \(j=k\), then \(S=0\). Otherwise put \(m=k-j\), choose the uniquely defined primitive matrix \(S_0\in M_2(R_m)\) satisfying \(S=p^jS_0\pmod {p^k}\), and write \(\delta=\det S_0\in R_m\). The function \(r_k(S)\) is
\[
\boxed{r_k(S)=
\begin{cases}
p^{3k-2}(p^2-1),& j=k,\\
p^{2k+j-1}(p-1),&j<k,\ p\mid\delta,\\
p^{2k+j-1}(p+\chi_p(-\delta)),&1\le j<k,\ p\nmid\delta,\\
\varphi(p^k)\sum_{h=0}^{k-1}p^{k-h}\rho_h(D)+p^k\rho_k(D),&j=0,\ p\nmid\delta,
\end{cases}}
\]
where \(D=1-4\delta^{-1}\in R_k\), \(\varphi(p^k)=p^k-p^{k-1}\), and \(\rho_0(D)=1\). For \(h\ge1\), \(\rho_h(D)\) is the number of square roots of \(D\) modulo \(p^h\), computed **without enumeration** as follows. Let \(v=\min(v_p(D),h)\). If \(v=h\), then \(\rho_h(D)=p^{\lfloor h/2\rfloor}\). If \(v<h\) is odd, then \(\rho_h(D)=0\). If \(v=2s<h\), let \(u=p^{-2s}D\pmod p\) be the associated unit; then
\[
\rho_h(D)=\begin{cases}2p^s,&\chi_p(u)=1,\\0,&\chi_p(u)=-1.\end{cases}
\]
This gives an explicit valuation-level formula for every possible target. In the final case, if \(D\not\equiv0\pmod p\), it simplifies to \(p^{2k-1}(p+\chi_p(D))\).

## Proof

**1. Lifting and the determinant polarization.** The determinant-one hypersurface is smooth over \(R_k\), since a matrix of unit determinant has a unit entry and thus a unit cofactor. Reduction \(G_k\to G_m\) therefore has exactly \(p^{3(k-m)}\) lifts of each point. Its cardinality is
\[
|G_k|=p^{3k-2}(p^2-1).
\]
For a fixed target \(S\) and a matrix \(A\in G_k\), the identity
\[
\det(S-A)=\det S+\det A-\operatorname{tr}(\operatorname{adj}(S)A)
\]
shows that \(S-A\in G_k\) precisely when \(\operatorname{tr}(\operatorname{adj}(S)A)=\det S\). For \(S=0\) every \(A\in G_k\) works, proving the first case.

**2. Removing the content of \(S\).** For \(j<k\), write \(S=p^jS_0\), \(m=k-j\). Since the adjugate is degree one in a two-by-two matrix, the second determinant constraint reduces exactly to
\[
\operatorname{tr}(\operatorname{adj}(S_0)A)\equiv p^j\det S_0\pmod {p^m}.
\]
Each solution \(A\pmod {p^m}\) with unit determinant lifts to \(p^{3j}\) choices modulo \(p^k\). Therefore \(r_k(S)\) is \(p^{3j}\) times a trace-and-determinant count over \(R_m\).

**3. Primitive singular determinant.** Suppose \(p\mid\delta\), with \(S_0\) primitive. Elementary row and column elimination over the local ring, using determinant-one elementary matrices and a determinant-one diagonal scaling, takes \(S_0\) to \(\operatorname{diag}(1,\delta)\). The pair-sum constraints are invariant under \(S\mapsto PSQ\) when \(\det P\det Q=1\). Write \(A=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\). The trace equation forces \(d=\delta(p^j-a)\). The determinant equation becomes
\[
bc=\delta a(p^j-a)-1.
\]
The right-hand side is a unit. For each of the \(p^m\) choices of \(a\), there are exactly \(\varphi(p^m)\) ordered pairs \((b,c)\). Multiplying by the lifting factor \(p^{3j}\) gives \(p^{2k+j-1}(p-1)\).

**4. Primitive invertible determinant.** Now suppose \(\delta\) is a unit. The substitution \(B=S_0^{-1}A\) transforms the constraints into
\[
\det B=\delta^{-1},\qquad\operatorname{tr} B=p^j\pmod {p^m}.
\]
For a general modulus \(q=p^m\), trace \(t\) and unit determinant \(d\), put \(B=\begin{psmallmatrix}a&b\\c&t-a\end{psmallmatrix}\). Then \(bc=a(t-a)-d\). Let \(F_m(z)\) count factorizations \(bc=z\) modulo \(p^m\). Directly counting the valuations of \(b\) yields
\[
F_m(z)=\varphi(p^m)\sum_{h=0}^{m-1}\mathbf1_{p^h\mid z}+p^m\mathbf1_{z=0}.
\]
Indeed a nonzero \(z\) of valuation \(s<m\) has \((s+1)\varphi(p^m)\) factorizations, and \(z=0\) has \(m\varphi(p^m)+p^m\). Summing over \(a\), and completing the square via
\[
4(a(t-a)-d)=t^2-4d-(2a-t)^2,
\]
where multiplication by two is invertible, gives
\[
H_m(t,d)=\varphi(p^m)\sum_{h=0}^{m-1}p^{m-h}\rho_h(t^2-4d)+p^m\rho_m(t^2-4d).
\]
If \(j=0\), set \(t=1\) and \(d=\delta^{-1}\) to obtain the last case of the theorem. If \(j\ge1\), the discriminant \(p^{2j}-4\delta^{-1}\) is a unit modulo \(p\). Every quadratic congruence has exactly two Hensel-lifted roots at each depth when its reduction is a square, and no roots otherwise. Therefore \(H_m(p^j,\delta^{-1})=p^{2m-1}(p+\chi_p(-\delta))\); multiplying by \(p^{3j}\) completes the classification.

**5. Explicit square-root counts.** A congruence \(x^2=D\pmod {p^h}\) with \(D\equiv0\pmod {p^h}\) requires \(p^{\lceil h/2\rceil}\mid x\), producing \(p^{\lfloor h/2\rfloor}\) roots. If \(v_p(D)=v<h\), a square requires \(v=2s\); writing \(x=p^sy\), the unit equation has either zero or two Hensel roots modulo \(p^{h-2s}\), and each lifts to \(p^s\) solutions for \(x\) modulo \(p^h\). This proves all displayed cases for \(\rho_h\).

**6. Sharp minimum, multiplicity and uniform lower bound.** Every term of the factorization formula is nonnegative, so the invertible-determinant case has at least \(p^m\varphi(p^m)\) solutions. The singular primitive case has exactly that many. Thus every nonzero target has at least \(p^{2k-1}(p-1)\) representations, with strict inequality whenever \(j\ge1\); the zero target is larger as well. At \(j=0\), invertible targets attain the minimum precisely when \(D\) is a nonsquare modulo \(p\); this is immediate from \(\rho_1(D)=0\). There are \((p-1)/2\) nonsquare discriminant residues, and the map \(\delta\mapsto1-4\delta^{-1}\) maps the units of \(\mathbb F_p\) bijectively onto \(\mathbb F_p\setminus\{1\}\). Every determinant unit \(\delta\in R_k\) has exactly \(|G_k|\) inverse images in \(\mathrm{GL}_2(R_k)\). The number of primitive targets with determinant divisible by \(p\) equals the number \((p-1)(p+1)^2\) of rank-one nonzero matrices modulo \(p\), times \(p^{4k-4}\). Adding the nonsquare-discriminant targets gives
\[
(p-1)(p+1)^2p^{4k-4}+\frac{p-1}{2}p^{k-1}|G_k|=\frac{(p-1)(p+1)(p^2+p+2)}2p^{4k-4}.
\]
Finally, the mean of \(r_k(S)\) over all \(p^{4k}\) target matrices is \(|G_k|^2/p^{4k}=p^{2k-4}(p^2-1)^2\). Dividing the sharp minimum by this mean yields \(p^3/((p-1)(p+1)^2)\). Dividing by \(|G_k|^2\) gives the stated pointwise probability minorization.

## Verification

The included standard-library `check.py` computes \(r_k\) by the independent definition \(\#\{A\in G_k:\det(S-A)=1\}\), separately from the displayed formula. It checks all targets for \((p,k)=(3,2),(5,1)\) and sampled targets for \((3,3),(5,2)\), as well as the rank-one and discriminant strata and sharp-minimum count. It also verifies the root-count routine against direct square enumeration. The 2025 finite-field theorem supplies an independent comparison at depth one, which the new all-depth formula recovers. These experiments corroborate but do not prove the infinite quantified statement.

## Relationship to prior work

Ferguson–Hoffman–Luca–Ostafe–Shparlinski [1] study additive matrix-ring distributions over finite **fields**, motivating the additive setting. Li–Hu [2] give Fourier/Gauss sums over general and special linear groups over finite **fields**, not residue rings. Karabulut [3] establishes twofold coverage and studies Cayley spectra over finite fields. Luo–Ji [4] proves an exact general finite-field matrix-sum representation theorem; consequently the depth-one specialization is prior work and **not claimed as new**. None of these inspected primary statements covers the higher-depth local-ring discriminant fibers, their singular lifting contribution, or the exact depth-uniform minorization/multiplicity law. Other unlocated local-ring additive representation formulas remain a possible priority risk.

## Limitations

The theorem concerns two-by-two determinant-one matrices over \(\mathbb Z/p^k\mathbb Z\) for odd primes and \(k\ge2\). It does not treat even primes, general finite chain rings, higher matrix size or more than two summands. The minorization is a pointwise two-step additive estimate, not a nonlinear mixing-time assertion. Historical priority is bounded by actual inspected published sources and searches; an unknown more general local-ring identity could subsume the theorem. Independent mathematical audit has not been performed.

## References

1. R. Ferguson, C. Hoffman, F. Luca, A. Ostafe and I. Shparlinski, *Some Additive Combinatorics Problems in Matrix Rings*, arXiv:0902.3482v1, first public 19 February 2009, https://arxiv.org/abs/0902.3482.
2. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1, first public 23 May 2011, https://arxiv.org/abs/1105.4513.
3. Y. Demiroğlu Karabulut, *Cayley Digraphs of Matrix Rings over Finite Fields*, arXiv:1710.08872v1, first public 24 October 2017, https://arxiv.org/abs/1710.08872.
4. Y. Luo and Q. Ji, *On the sum of matrices of special linear group over finite field*, AIMS Mathematics 10 (2025), 3642–3651, https://doi.org/10.3934/math.2025168.
