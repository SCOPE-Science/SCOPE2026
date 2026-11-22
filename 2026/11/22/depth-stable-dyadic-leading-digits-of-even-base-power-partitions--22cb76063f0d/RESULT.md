# Depth-stable dyadic leading digits of even-base power partitions

## Finding

For each even integer \(m\ge2\), let \(b_m(N)\) be the number of partitions of \(N\ge0\) into unbounded numbers of parts drawn from \(1,m,m^2,\ldots\), with \(b_m(0)=1\). Put \(a=\nu_2(m)\). For every pair of integers \(r\ge2\) and \(n\ge1\), write \(e_{m,r}=1+(r-1)(a-1)\). Then
\[
 2^{e_{m,r}}\mid b_m(m^r n-1),\qquad
 \frac{b_m(m^r n-1)}{2^{e_{m,r}}}\equiv
  \sum_{j=1}^{n}j\,b_m(n-j)\pmod2.
\]
In particular, the normalized leading binary digit on the left is independent of the depth \(r\). At \(n=1\), the right-hand side is one. Thus the established universal power-of-two divisibility bound is attained at the natural all-ones indices for **every** even base and **every** depth:
\[
 \boxed{\nu_2\bigl(b_m(m^r-1)\bigr)=1+(r-1)(\nu_2(m)-1)}.
\]
The result also determines the parity of the normalized partition number for every additional multiplier \(n\), by a fixed finite convolution in ordinary partition values near \(n\).

## Assumptions and scope

All generating functions are formal power series with integer coefficients. The base \(m\) is even, not necessarily a prime power; \(r\ge2\) and \(n\ge1\) are arbitrary. The \(2\)-adic valuation \(\nu_2\) is the usual exponent of two for a positive integer. The normalized quotient in the congruence is an ordinary integer, as established by the first assertion. No statements about odd bases, colored partitions, or other index families are asserted.

## Proof

**1. Formal extraction identity.** Define \(B(q)=\prod_{i\ge0}(1-q^{m^i})^{-1}\), and let \(U_m(\sum_{j\ge0}c_jq^j)=\sum_{j\ge0}c_{mj}q^j\). Because \(B(q)=B(q^m)/(1-q)\), extraction has the useful property \(U_m(f(q)g(q^m))=(U_m f(q))g(q)\). For \(r\ge1\), set
\[
 G_r(q)=\sum_{n\ge1}b_m(m^rn-1)q^n.
\]
The coefficient recurrence
\[
 b_m(k)-b_m(k-1)=\mathbf1_{m\mid k}\,b_m(k/m)\quad(k\ge1)
\]
follows by separating partitions with at least one part one; on the remaining partitions all parts are multiples of \(m\). Summing this identity over \(k=1,\ldots,mn-1\) gives \(b_m(mn-1)=\sum_{j=0}^{n-1}b_m(j)\). Hence \(G_1(q)=qB(q)/(1-q)\).

Let \(A_1(q)=q/(1-q)\), \(A_{r+1}(q)=U_m(A_r(q)/(1-q))\). Induction using the product-extraction identity gives \(G_r(q)=B(q)A_r(q)\). Write \(a_r(n)=[q^n]A_r(q)\), with \(a_r(0)=0\). Then \(a_1(n)=1\) for \(n\ge1\), \(a_2(n)=mn\), and
\[
 a_{r+1}(n)=\sum_{j=1}^{mn}a_r(j)\qquad(r\ge1,n\ge1).
\]
These are polynomials in the variable \(n\), by repeated polynomial summation.

**2. A dyadically integral summation operator.** For a polynomial \(f\), define
\[
 (T_mf)(x)=\frac2m\sum_{j=1}^{mx}f(j),
\]
where the right-hand side is the unique polynomial agreeing with the sum at all nonnegative integer inputs. We claim \(T_m(\mathbb Z_2[x])\subseteq\mathbb Z_2[x]\) for every even \(m\). By linearity, suffice it to test \(f(x)=x^k\), \(k\ge0\). Faulhaber's identity writes
\[
 \sum_{j=1}^{N}j^k=\sum_{t=1}^{k+1}c_{k,t}N^t,\qquad
 c_{k,t}=\pm\frac1t\binom{k}{t-1}B_{k+1-t}
\]
with the harmless conventional sign choice for the first Bernoulli number; only denominators matter. The elementary Bernoulli denominator theorem gives \(2B_j\in\mathbb Z_2\) for all \(j\ge0\), including \(j=0,1\). Accordingly, the coefficient \(2m^{t-1}c_{k,t}\) of \(x^t\) in \(T_mx^k\) has two-adic valuation at least \((t-1)\nu_2(m)-\nu_2(t)\). This is nonnegative for all \(t\ge1\), because \(\nu_2(t)\le t-1\). The operator therefore preserves dyadically integral polynomials. Finally
\[
 T_mx=x(mx+1)\equiv x\pmod{2^a\mathbb Z_2[x]}.
\]

**3. Depth invariance of normalized coefficients.** For \(r\ge2\), define
\[
 h_r(x)=\frac{2^{r-2}}{m^{r-1}}a_r(x).
\]
The coefficient recursion above yields \(h_2(x)=x\) and \(h_{r+1}=T_mh_r\). The operator lemma proves inductively that \(h_r\in\mathbb Z_2[x]\) for all \(r\ge2\). Moreover, since \(T_m\) preserves \(2^a\mathbb Z_2[x]\) and \(T_mx\equiv x\pmod{2^a}\), induction establishes the stronger congruence
\[
 h_r(x)\equiv x\pmod{2^a\mathbb Z_2[x]}\qquad(r\ge2).
\]
Notice that \(h_3(x)=x(mx+1)\) confirms the first nontrivial step directly.

**4. Recover the partition numbers.** Let \(m=2^a u\), where \(u\) is odd. Extracting coefficient \(q^n\) from \(G_r(q)=B(q)A_r(q)\), and substituting the definition of \(h_r\), gives the exact identity in \(\mathbb Q_2\):
\[
 b_m(m^rn-1)=\frac{m^{r-1}}{2^{r-2}}
 \sum_{j=1}^{n}b_m(n-j)h_r(j)
 =2^{e_{m,r}}u^{r-1}\sum_{j=1}^{n}b_m(n-j)h_r(j).
\]
The last sum is a \(2\)-adic integer because \(h_r(j)\in\mathbb Z_2\); the left side is an ordinary integer. This proves integer divisibility by \(2^{e_{m,r}}\). Dividing by this power and reducing the exact identity modulo two, using \(u^{r-1}\equiv1\pmod2\) and \(h_r(j)\equiv j\pmod2\), gives the announced parity convolution. For \(n=1\), the sum is \(b_m(0)h_r(1)\equiv1\pmod2\), so the valuation is exactly \(e_{m,r}\). This completes the proof for every even base and every depth.

## Verification

Execute `python3 CHECK.py` with the Python 3 standard library. The code computes partition coefficients independently from the one-step recurrence and tests both the predicted divisibility and exact first normalized bit. Complete tests for the sampled finite parameter grid cover 500 triples \((m,r,n)\), with ten even bases from 2 through 20, selected depths up to 11, and multipliers up to 14. Forty all-ones-index witnesses have the predicted exact valuation. The largest enumerated target was below 786,432. These computations corroborate, but cannot replace, the infinite formal-series and dyadic-polynomial proof.

## Relationship to prior work

Rødseth and Sellers (2001) proved the general even-base congruence lower modulus, with the exponent equivalent to \(1+(r-1)(\nu_2(m)-1)\) for the index progression here, but did not give a normalized mod-two profile or prove that the all-ones indices achieve the lower bound at every depth. Żmija (2024) develops broader high-order congruences and extraction methods, supplying a general lower bound rather than this exact leading bit. Two nearby subsequent studies respectively determine the first nonzero base-\(m\) digit at all-ones indices for **odd** bases coprime to six, and exact gcds for four **fixed-depth** branches; neither statement contains this arbitrary-depth even-base law. This result sharpens the older divisibility theorem, rather than claiming originality for the extraction operator.

## Limitations

No formula is asserted for all higher normalized binary digits, for odd bases, or for arbitrary restricted partition alphabets. A polynomial coefficient lemma depends on the classical Bernoulli denominator fact. The exact parity law is an infinite theorem, not simply a finite observation; the independent finite checker does not constitute an independent mathematical audit. Bibliographic comparison cannot exclude every implicit equivalent or unindexed source.

## References

1. Ø. J. Rødseth and J. A. Sellers, *On m-ary Partition Function Congruences: A Fresh Look at a Past Problem*, Journal of Number Theory **87** (2001), 270–281; DOI `10.1006/jnth.2000.2594`; author full text https://www.d.umn.edu/~jsellers/p14.pdf.
2. B. Żmija, *High order congruences for M-ary partitions*, arXiv:2403.04495v1 (first posted **2024-03-07**), https://arxiv.org/abs/2403.04495, Periodica Mathematica Hungarica **89** (2024), 155–167.
3. B. Żmija, *Recurrence sequences connected with the m-ary partition function and their divisibility properties*, arXiv:1710.04303 (2017), https://arxiv.org/abs/1710.04303.
4. M. Ulas and B. Żmija, *On p-adic valuations of colored p-ary partitions*, arXiv:1809.04628 (2018), https://arxiv.org/abs/1809.04628.
5. *Sharp leading m-adic units for all-ones m-ary partition indices*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-leading-m-adic-units-for-all-ones-m-ary-partition-indices--a4362220d5df.
6. *Sharp universal gcds for the four depth-three branches of m-ary partition congruences*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-universal-gcds-for-the-four-depth-three-branches-of-m-ary--9f08fd865d9d.
