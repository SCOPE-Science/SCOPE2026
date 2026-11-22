# Fourier sign rigidity and sharp recovery gaps for involution fixed-point profiles

## Finding
Let \(n\geq1\), let \(G_n=(\mathbb Z/2\mathbb Z)^n\), and let \(f_n:G_n\to\mathbb Z_{\geq0}\) count involutions \(\pi\) of \([n]\) with exactly the fixed-point incidence vector \(x\). Denote by \(T_n\) unnormalized XOR convolution \(T_ng=f_n*g\). For \(S\subseteq[n]\) of size \(k\), define
\[
W_{n,k}=\sum_{\pi^2=\mathrm{id}}(-1)^{|S\cap\operatorname{Fix}(\pi)|}.
\]
These numbers depend only on \(k\); each occurs as a Fourier multiplier with multiplicity \(\binom nk\).

**Exact classification.** The operator \(T_n\) is invertible over \(\mathbb R\) or \(\mathbb C\) exactly for \(n=1\) and every \(n\geq4\). At \(n=2\) it has two zero multipliers (those of weight one), and at \(n=3\) it has six zero multipliers (those of weights one and two). Both exceptional operators have rank two.

**Signs and sharp gap.** For even \(n\geq4\), all \(W_{n,k}\) are strictly positive. For odd \(n\geq5\), \(W_{n,k}\) is strictly positive when \(0\leq k\leq(n-1)/2\) and strictly negative when \((n+1)/2\leq k\leq n\). Put
\[
a_0=1,\qquad a_1=0,\qquad a_{m+1}=2m(a_m+a_{m-1})\quad(m\geq1).
\]
Then \(a_m>0\) for every \(m\geq2\), and for all \(n\geq4\)
\[
\min_{0\leq k\leq n}|W_{n,k}|=a_{\lfloor n/2\rfloor},\qquad
\max_{0\leq k\leq n}|W_{n,k}|=I_n,
\]
where \(I_0=I_1=1\) and \(I_n=I_{n-1}+(n-1)I_{n-2}\) counts involutions. Thus the exact \(\ell^2(G_n)\) spectral condition number of \(T_n\) is \(I_n/a_{\lfloor n/2\rfloor}\). The minimum magnitude occurs at the two central weights for odd \(n\geq5\), uniquely at the central weight for even \(n\geq6\), and at weights \(1,2,3\) when \(n=4\).

The first central gap values \(a_2,a_3,a_4,a_5,a_6\) are \(2,8,60,544,6040\). All claims concern the multiplicity-counting kernel, not the indicator of merely possible fixed-point sets.

## Assumptions and scope
A permutation is an involution if \(\pi^2=\mathrm{id}\); its disjoint cycles have sizes one or two. The count \(f_n(x)\) is zero unless \(n-|x|\) is even, and otherwise it is the number \((n-|x|-1)!!\) of matchings of the remaining vertices (with \((-1)!!=1\)). Fourier transforms are *unnormalized*: \(\widehat f_n(S)=\sum_x f_n(x)(-1)^{\sum_{i\in S}x_i}\). The standard counting-convolution convention is \((f*g)(x)=\sum_y f(y)g(x-y)\). Its orthogonal Walsh eigenbasis yields singular values \(|W_{n,k}|\).

## Proof
**1. Exact multipliers.** Let \(I_j\) be the number of involutions on \(j\) labels. For fixed \(S\) with \(|S|=k\), expand
\[
(-1)^{|S\cap\operatorname{Fix}(\pi)|}=\prod_{i\in S}(1-2\mathbf1_{\{\pi(i)=i\}}).
\]
Fixing an indicated set of \(j\) labelled points leaves \(I_{n-j}\) involutions, so inclusion–exclusion gives
\[
W_{n,k}=\sum_{j=0}^{k}\binom kj(-2)^jI_{n-j}.
\tag{1}
\]
Equivalently, if \(u\) marks selected labels and \(v\) unselected labels, the exponential generating function of their weighted involutions is
\[
\exp\!\left(-u+v+\frac{(u+v)^2}{2}\right).
\tag{2}
\]
Indeed, a fixed singleton contributes \(-u\) or \(+v\), while every transposition contributes one of the unordered two-label terms in \((u+v)^2/2\). It follows that
\[
W_{n,k}=k!(n-k)![u^kv^{n-k}]\exp\!\left(-u+v+\frac{(u+v)^2}{2}\right).
\tag{3}
\]
Let \(Z\) be standard normal. Its moment-generating identity turns (3) into the exact integer identity
\[
W_{n,k}=\mathbb E[(Z-1)^k(Z+1)^{n-k}].
\tag{4}
\]
This use of Gaussian moments is just Wick's pairing formula, so no approximation is involved.

**2. Two fundamental symmetries.** Substituting \(-Z\) for \(Z\) in (4) gives
\[
W_{n,n-k}=(-1)^nW_{n,k}.
\tag{5}
\]
Factoring the difference between consecutive powers gives, for \(0\leq k<n\),
\[
W_{n,k}-W_{n,k+1}=2W_{n-1,k}.
\tag{6}
\]

**3. Central moments.** Write \(Y=Z^2-1\) and \(a_m=\mathbb E[Y^m]\). Clearly \(a_0=1\) and \(a_1=0\). Apply Gaussian integration by parts \(\mathbb E[Zh(Z)]=\mathbb E[h'(Z)]\) to \(h(Z)=ZY^m\):
\[
\mathbb E[Z^2Y^m]=a_m+2m\mathbb E[Z^2Y^{m-1}]
=a_m+2m(a_m+a_{m-1}).
\]
But the left side equals \(a_{m+1}+a_m\), yielding the recurrence in the finding. Hence \(a_2=2\), and induction proves \(a_m>0\) for all \(m\geq2\). From (4), for every \(m\geq0\),
\[
W_{2m,m}=a_m,\qquad W_{2m+1,m}=a_m,\qquad W_{2m+1,m+1}=-a_m.
\tag{7}
\]
For the odd case the term involving the odd factor \(Z\) has zero expectation.

**4. All-order sign and minimum proof.** At order four, formula (1) gives the exact row \((10,2,2,2,10)\), establishing positivity and the asserted exceptional three-weight minimum. Assume that an even row of order \(2m\geq4\) is positive. Equation (6) then makes the following odd row of order \(2m+1\) strictly decreasing. Equations (5) and (7), together with \(a_m>0\), show that this odd row changes sign strictly between its two central weights and has least absolute magnitude \(a_m\). Conversely, if this odd row has the established sign pattern, equation (6) makes the next even row decrease to its unique middle weight and then increase. Equation (7) makes that middle value \(a_{m+1}>0\). Therefore the whole even row is positive and its least value is \(a_{m+1}\). Alternating these implications proves the claim for all \(n\geq4\).

**5. Exceptional orders and condition numbers.** Directly from (1) the rows at \(n=1,2,3\) are \((1,-1)\), \((2,0,2)\), and \((4,0,0,-4)\). The multiplicities \(\binom nk\) give the stated ranks and nullities. Since each Walsh multiplier is a sum of \(I_n\) signs, its magnitude is at most \(I_n\); the empty frequency attains equality. Walsh diagonalization and the least-magnitude theorem give the claimed sharp \(\ell^2\) condition numbers.

## Verification
The included standalone Python 3 program `verify.py` builds the fixed-point mask kernel by a direct recursive involution enumeration, applies an independent integer Walsh–Hadamard transform, and compares all characters with formula (1). It checks every one of \(2^1+\cdots+2^{11}=4094\) characters through order eleven, verifies the exact ranks at orders two and three, and tests the recurrence, signed symmetry, nonvanishing and sharp minima through order sixty using exact integer arithmetic. The program returned `PASS`. These finite tests are reproducibility checks, not the proof of the unbounded statements; Steps 1–5 provide the full proof.

## Relationship to prior work
Involutions and their partial-matching representation, including ordinary and fixed-point-refined enumeration, are classical. Lugo (2009), especially Sections 1, 4 and 6, discusses partial matchings, fixed-point counts and associated exponential generating functions, but not the positional signed Walsh multipliers here. Chow and Mansour (2010), Section 4 and Proposition 7, give scalar involution enumerators and their generating functions in wreath products; these supply the counting backbone but not the parity-dependent all-frequency sign law or sharp minimum. An existing Fourier analysis of fixed-position indicators of **unrestricted permutations** uses factorial counts rather than the involution counts in (1), and does not imply the present sign transition or central chi-square moment gap. Likewise, work on edge-incidence spectra of complete-graph matchings concerns transposition edges, not the positions left unmatched. The central-moment integer sequence \(1,0,2,8,60,544,\ldots\) is already tabulated as OEIS A053871; only its role as the *sharp least Fourier multiplier* in the present involution-profile theorem is asserted here. The present result does not claim the standard involution generating function, its scalar counts, the central-moment recurrence, or Gaussian integration by parts as new.

## Limitations
This is a theorem for involutions of the full symmetric group and the multiplicity-weighted distribution of *labelled fixed-point sets*. It does not address descent sets, arbitrary restricted involution classes, or edge-incidence Fourier spectra. No sharp \(\ell^1\) or \(\ell^\infty\) inverse norm or all-order combinatorial signed-frequency bijection is asserted. Historical-priority risk remains for an unindexed equivalent positionwise signed-enumerator treatment. Independent audit has not been performed.

## References
- M. Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604 (first public posting 2009-11-18), https://arxiv.org/abs/0911.3604 . Full text inspected, especially Sections 1, 4 and 6.
- OEIS Foundation, *A053871*, https://oeis.org/A053871 (known integer sequence of centered chi-square moments; original record date was not verified).
- C.-O. Chow and T. Mansour, *Counting derangements, involutions and unimodal elements in the wreath product \(C_r\wr S_n\)*, Israel Journal of Mathematics **179** (2010), 425–448, https://doi.org/10.1007/s11856-010-0088-8 . Section 4, Proposition 7 and proof inspected in the author-provided full-text rendition.
