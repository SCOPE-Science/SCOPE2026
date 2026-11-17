# Exact ternary residue spectrum and Haar measure of derangement numbers

## Finding
Let \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for \(n\ge1\). Let \(I_k=\{D_n\bmod 3^k:n\ge0\}\) for every integer \(k\ge1\). Define \(S_0=1\), \(S_1=2\), and \(S_m=3^{m-1}+S_{m-2}\) for \(m\ge2\). Then
\[
|I_1|=3,\qquad |I_k|=2\cdot3^{k-1}+2S_{k-2}-3^{\max(k-5,0)}\quad(k\ge2).
\]
The first eight cardinalities are \(3,7,21,61,183,545,1633,4895\). The closure \(\mathcal I\) of the derangement values in \(\mathbb Z_3\) has normalized Haar measure \(\mu(\mathcal I)=725/972\).

More precisely, let \(\mathcal S\subset\mathbb Z_3\) be the set of \(3\)-adic squares. A canonically determined \(3\)-adic unit \(u\equiv2\pmod3\), defined in the proof, satisfies
\[
\mathcal I=(1+3\mathbb Z_3)\cup(-1+3\mathbb Z_3)\cup 9\bigl((9u+\mathcal S)\cup(-9u-\mathcal S)\bigr).
\]
The last two square translates intersect in exactly \(27\mathbb Z_3\), before the outer scaling by \(9\). The least period of the derangement sequence modulo \(3^k\) is \(2\cdot3^k\); periodicity itself was studied previously and is not asserted as the novel contribution.

## Assumptions and scope
All indices are nonnegative integers, all exponents \(k\) are positive integers, and residues are taken in the integer ring \(\mathbb Z/3^k\mathbb Z\). A square in \(\mathbb Z_3\) includes zero. The Haar measure is normalized by \(\mu(\mathbb Z_3)=1\). The invariant concerns the set of attained values, not the distribution of multiplicities within a full period.

## Proof
**Analytic interpolation.** Write \(P_j(X)=\prod_{i=0}^{j-1}(X-i)\), with \(P_0=1\), and put
\[
F(x)=\sum_{j=0}^{\infty}(-1)^jP_j(x),\qquad x\in\mathbb Z_3.
\]
Every block of three consecutive integers contains a multiple of three; hence \(v_3(P_j(x))\ge\lfloor j/3\rfloor\) for all \(x\in\mathbb Z_3\). The bound on each fixed-order derivative is at least \(\lfloor j/3\rfloor-r\) for the \(r\)-th derivative, obtained by differentiating at most \(r\) of the factors. Consequently the series and each fixed-order derivative converge uniformly. On any ball \(a+3\mathbb Z_3\), expansion in \(x-a\) gives integral, convergent Taylor coefficients. In particular, every such expansion is \(1\)-Lipschitz and its higher-degree terms respect the usual divisibility by powers of \(3\). For nonnegative integers \(n\), the sum truncates and \(F(n)=(-1)^nD_n\).

The identity
\[
F(x+1)=1-(x+1)F(x)
\]
holds first for integers and then, by continuity and density, for every \(x\in\mathbb Z_3\). The reductions \(F(0)=1\), \(F(1)=0\), \(F(2)=1\pmod3\) imply that \(F(\mathbb Z_3)\bmod3=\{0,1\}\), with the unique branch reducing to zero being \(1+3\mathbb Z_3\).

**Unit branch.** The derivative at zero is
\[
F'(0)=-\sum_{j=0}^{\infty}j!\equiv-4\equiv2\pmod3.
\]
Thus for \(x,y\in3\mathbb Z_3\), Taylor expansion shows \(v_3(F(x)-F(y))=v_3(x-y)\), and Hensel lifting gives a unique preimage in \(3\mathbb Z_3\) of each element of \(1+3\mathbb Z_3\). Therefore \(F(3\mathbb Z_3)=1+3\mathbb Z_3\). The branch \(F(2+3\mathbb Z_3)\) also reduces to \(1\) and contributes no additional values outside that ball.

**Critical branch.** Direct differentiation at one gives
\[
F'(1)=-1+\sum_{j=0}^{\infty}j!\equiv9\pmod{27}.
\]
The coefficient of \(X^2\) at zero equals
\[
\frac{F''(0)}2=\sum_{n=1}^{\infty}n!H_n\equiv1+3+11+50+274=339\equiv0\pmod3,
\]
where \(H_n=\sum_{i=1}^{n}1/i\) and the displayed products \(n!H_n\) are integers; all subsequent summands are divisible by \(3\). Differentiating the functional identity twice yields \(F''(1)=-2F'(0)-F''(0)\equiv2\pmod3\), so \(F''(1)/2\equiv1\pmod3\).

As \(F'(1)\equiv0\pmod3\) and \(F''(1)\) is a unit, Hensel's lemma applied to \(F'\) gives a unique critical point \(c\in1+3\mathbb Z_3\). The congruence \(F'(1)\equiv9\pmod{27}\) shows \(c=1+9w\) with \(w\equiv1\pmod3\). Taylor expansion at one gives
\[
F(c)=9wF'(1)+(9w)^2\frac{F''(1)}2+O(3^6)=81u,
\]
where \(u\in\mathbb Z_3^\times\) and \(u\equiv1+1\equiv2\pmod3\).

For each \(h\in3\mathbb Z_3\), Taylor expansion at \(c\) gives \(F(c+h)=F(c)+h^2A(h)\), where \(A(h)\in1+3\mathbb Z_3\) is analytic. Every unit in \(1+3\mathbb Z_3\) has a unique square root there. The map \(h\mapsto h\sqrt{A(h)}\) is an isometric analytic bijection of \(3\mathbb Z_3\): its derivative is \(1\pmod3\) and its higher terms have integral coefficients on this ball. Therefore
\[
F(1+3\mathbb Z_3)=81u+9\mathcal S.
\]
Because even and odd nonnegative integers are separately dense in \(\mathbb Z_3\), the closure of \(\{D_n\}\) equals \(F(\mathbb Z_3)\cup -F(\mathbb Z_3)\). This proves the asserted three-part decomposition.

**Intersection and counting.** Consider \(W=(9u+\mathcal S)\cup(-9u-\mathcal S)\). A value in the intersection must be a nonunit: unit squares are \(1\pmod3\), whereas negative unit squares are \(2\pmod3\). It cannot have valuation exactly one, since the shift \(9u\) does not affect this valuation. For a multiple \(y=9z\), simultaneous membership is equivalent to \(z-u\in\mathcal S\) and \(-z-u\in\mathcal S\). Since \(u\equiv2\pmod3\), both conditions hold precisely when \(z\equiv0\pmod3\); the two differences are then unit squares congruent to one. Thus the intersection is \(27\mathbb Z_3\).

The number \(S_m\) of squares modulo \(3^m\) satisfies the displayed recursion: the \(3^{m-1}\) unit squares and the multiples of \(9\) that are squares form disjoint groups, and the latter reduce to squares modulo \(3^{m-2}\). The intersection of the two square translates modulo \(3^m\) has \(3^{\max(m-3,0)}\) elements. The two unit residue balls together account for \(2\cdot 3^{k-1}\) elements modulo \(3^k\); for \(k\ge2\) the remaining, disjoint image modulo \(3^k\) consists of the scaled images of \(W\bmod3^{k-2}\). Therefore
\[
|I_k|=2\cdot3^{k-1}+2S_{k-2}-3^{\max(k-5,0)}.
\]
The case \(k=1\) follows directly from the reductions of \(F\) and \(-F\).

The square-set measure satisfies \(\mu(\mathcal S)=1/3+\mu(\mathcal S)/9\), hence \(\mu(\mathcal S)=3/8\). The intersection has measure \(1/27\), giving \(\mu(W)=2(3/8)-1/27=77/108\). Finally \(\mu(\mathcal I)=2/3+\mu(W)/9=725/972\).

**Exact least period.** The interpolation makes \(2\cdot 3^k\) a period modulo \(3^k\). A period \(T\) cannot be odd: \(D_T=D_0\pmod3\) would require \(F(T)\equiv-1\pmod3\), but \(F\) attains only zero or one modulo three. For even \(T\), the equality \(D_{T+1}=D_1\pmod3\) forces \(T\equiv0\pmod3\). The equality \(D_T=D_0\pmod{3^k}\) and the isometry on \(3\mathbb Z_3\) imply \(3^k\mid T\). Hence the least period is \(2\cdot3^k\).

## Verification
Run `python3 verify.py` from the extracted files. The program independently enumerates the recurrence through one full proved period for exponents \(1\le k\le8\), compares with the square-count formula, checks both the signed parity branches, and checks 3-adic derivative and critical-value certificates at finite precision. These tests are finite consistency checks; the proof above establishes every exponent.

## Relationship to prior work
Sun, Wu, and Zhuang (2010) establish finite-field congruences for derangements (including modulo an odd prime), not the complete image cardinality modulo every power of three. Miska (2015) proves general periodicity and studies valuations and 3-adic interpolations, giving important tools but not the explicit square-image decomposition, image-cardinality formula, or Haar measure computed here. O'Desky and Richman (2020) further study 3-adic analytic interpolation of derangement-related functions but do not provide this complete ternary value spectrum. The least-period assertion is included as a by-product, not claimed as an original period theorem. This comparison is based on material inspected in the cited primary texts, not merely their titles. No claim of exhaustive historical uniqueness or independent review is made.

## Limitations
The theorem applies only to the standard derangement sequence and the prime three. It does not determine multiplicities of residues within a period, their discrepancy, or images for other primes. Unindexed equivalent work remains possible; published results on analytic interpolation and periodicity may overlap with proof ingredients.

## References
1. Y. Sun, X. Wu, J. Zhuang, "Congruences on the Bell polynomials and the derangement polynomials," arXiv:1009.2929v1 (2010-09-15), https://arxiv.org/abs/1009.2929.
2. P. Miska, "Arithmetic Properties of the Sequence of Derangements and its Generalizations," arXiv:1508.01987 (2015-08-09), https://arxiv.org/abs/1508.01987.
3. A. O'Desky and D. H. Richman, "Derangements and the p-adic incomplete gamma function," arXiv:2012.04615v1 (2020-12-08), https://arxiv.org/abs/2012.04615.
