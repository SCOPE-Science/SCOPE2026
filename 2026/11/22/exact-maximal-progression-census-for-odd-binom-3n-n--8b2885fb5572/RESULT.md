# Exact maximal-progression census for odd \(\binom{3n}{n}\)

## Finding
For each integer \(n\ge0\), let \(B(n)=\binom{3n}{n}\), and define
\[
E=\{n\ge0:B(n)\text{ is odd}\}.
\]
For every integer \(r\ge0\), let
\[
A_r=\#\{(a,d)\in\mathbb Z_{\ge0}\times\mathbb Z_{>0}:a+2d<2^r,\ a,a+d,a+2d\in E\}.
\]
Then the complete counting series for **all** positive common differences is
\[
\boxed{\sum_{r\ge0}A_r z^r=\frac{z^2}{(1-z-z^2)(1-z-3z^2+2z^4)}.}
\]
Its initial coefficients (at \(r=0,1,\ldots,14\)) are
\[
0,0,1,2,7,16,40,92,211,476,1063,2362,5218,11496,25257.
\]
There is no nonconstant four-term arithmetic progression in \(E\). Consequently every counted triple is of the **maximum possible progression length**; this bound is attained by the positive triples \((4^j,5\cdot4^j,9\cdot4^j)\) for every \(j\ge0\).

## Assumptions and scope
All progressions are increasing ordinary integer progressions and are counted once by their ordered pair \((a,d)\), where \(a\ge0\) and \(d\ge1\). The upper cutoff \(2^r\) is exclusive. We include \(n=0\), for which \(B(0)=1\); no claim is made for negative indices. The formula applies to **every** integer \(r\ge0\), not only asymptotically. For fixed \(r\), each counted progression lies wholly below \(2^r\).

The set \(E\) coincides with the fibbinary integers (OEIS A003714): the nonnegative integers whose binary expansions contain no adjacent one-bits. Indeed, by Kummer's theorem the 2-adic valuation of \(B(n)\) is the number of carries in the addition \(n+2n\). Zero carries occur exactly when the binary expansion of \(n\) has no adjacent ones.

## Proof
**Four-term obstruction.** Suppose \(a,a+d,a+2d,a+3d\) are four distinct terms with \(d>0\), and write \(d=2^t e\) for some \(t\ge0\) and odd \(e\). Writing \(a=2^t q+s\), where \(0\le s<2^t\), the four quotients \(q, q+e,q+2e,q+3e\) exhaust all residue classes modulo \(4\). One is \(3\pmod4\). The corresponding term has both bits at positions \(t\) and \(t+1\) equal to one, so it cannot lie in \(E\). Conversely, \((1,5,9)\) is a three-term progression in \(E\); multiplying by any power of four preserves the property. Hence three is the maximum length.

**Counting by binary addition.** Define \(H_r\) to count *all* pairs \((a,d)\) of nonnegative integers with \(a+2d<2^r\), allowing \(d=0\), for which \(a,a+d,a+2d\in E\). We read the \(r\) low binary digits of \(a\) and \(d\), from least to most significant. Set \(y=a+d\), \(w=y+d=a+2d\). The addition carries \(c_1,c_2\in\{0,1\}\) and previous output bits \((p_a,p_y,p_w)\in\{0,1\}^3\) form a state \((c_1,c_2,p_a,p_y,p_w)\), initially \((0,0,0,0,0)\).

For one new choice \((\alpha,\delta)\in\{0,1\}^2\) of the input bits, calculate
\[
\beta\equiv\alpha+\delta+c_1\pmod2,\qquad
c_1'=\left\lfloor\frac{\alpha+\delta+c_1}{2}\right\rfloor,
\]
\[
\gamma\equiv\beta+\delta+c_2\pmod2,\qquad
c_2'=\left\lfloor\frac{\beta+\delta+c_2}{2}\right\rfloor.
\]
Keep the transition to \((c_1',c_2',\alpha,\beta,\gamma)\) if \(p_a\alpha=p_y\beta=p_w\gamma=0\); otherwise discard it. Every valid pair of length-\(r\) digit strings has exactly one path, and the condition prevents adjacent ones in all three numbers. An endpoint is accepted precisely when \(c_1=c_2=0\), ensuring all three numbers are below \(2^r\); leading zero-bits impose no extra restriction.

Only eight states are reachable. In the following order they are
\[
\begin{aligned}
&(0,0,0,0,0),\ (0,0,0,0,1),\ (0,0,1,1,1),\ (0,1,0,1,0),\\
&(1,0,1,0,1),\ (1,1,0,0,0),\ (1,1,1,0,0),\ (1,1,1,1,1).
\end{aligned}
\]
The resulting transition-count matrix (rows are old states and columns new states) is
\[
M=\begin{pmatrix}
1&0&1&1&1&0&0&0\\
1&0&0&1&0&0&0&0\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&1&0\\
0&0&0&0&0&0&0&0\\
0&0&0&1&1&1&0&1\\
0&0&0&1&0&1&0&0\\
0&0&0&0&0&1&0&0
\end{pmatrix}.
\]
Let \(u=(1,0,0,0,0,0,0,0)\), and let \(v=(1,1,1,0,0,0,0,0)^{\mathsf T}\). Thus \(H_r=uM^rv\) for every \(r\ge0\).

**Exact polynomial identity.** Direct multiplication of the displayed integer matrix gives
\[
u\bigl(M^6-2M^5-3M^4+4M^3+5M^2-2M-2I\bigr)=0.
\]
It follows for all \(r\ge6\) that \(H_r\) satisfies the degree-six recurrence with reversed coefficients. Direct multiplication supplies \((H_0,\ldots,H_5)=(1,2,4,7,15,29)\). Therefore, as an identity of formal power series,
\[
\sum_{r\ge0}H_rz^r=\frac{1-3z^2-3z^3+2z^4+2z^5}{(1-z-z^2)(1-z-3z^2+2z^4)}.
\]
The pairs with \(d=0\) are exactly the members \(a\in E\) below \(2^r\). Their number \(f_r\) satisfies \(f_0=1,f_1=2,f_r=f_{r-1}+f_{r-2}\) and
\[
\sum_{r\ge0}f_rz^r=\frac{1+z}{1-z-z^2}.
\]
Finally \(A_r=H_r-f_r\) coefficientwise, and subtracting the two rational functions gives precisely the asserted \(z^2\)-numerator. All the calculations are exact over the integers and establish the infinite identity; the finite checks below are corroboration, not an extrapolation.

## Verification
Execute `python3 verify.py` with Python 3 (standard library only). It constructs the eight reachable states and transition matrix directly from the digit rules; verifies the integer row-annihilating polynomial, six initial values and all rational-series coefficient identities; checks 28 depth counts; compares the result with independent direct progression enumeration for every \(0\le r\le12\); and confirms the binomial parity criterion on 80 inputs. All checks passed in the packaged version. In particular the independent direct counts begin \(0,0,1,2,7,16,40,92,211\).

## Relationship to prior work
The fibbinary set and its Zeckendorf correspondence are classical; see OEIS A003714 and Lindroos–Sills–Wang (2014). Mollard (2012) studies Fibonacci cubes, whose vertices have the same forbidden-adjacency digit rule, but its maximal *induced hypercubes* are not arithmetic progressions of the represented integers. Published work on the exact dyadic valuation distribution of \(\binom{3n}{n}\) counts each individual valuation and in particular the total number of odd values; it does **not** count simultaneous oddness along three equally spaced indices. A published arithmetic-progression census for odd positions within *one fixed row* of Pascal's triangle likewise concerns the second index of \(\binom{m}{j}\) at fixed \(m\), not the nonlinear sequence \(\binom{3n}{n}\) as \(n\) varies. The distinction is one of statements and quantifiers, not titles. A separate Baum–Sweet support theorem has a rational three-progression series with the same denominator, but for a different index set and a different numerator; it does not imply the formula here.

The contribution is the evaluated exact all-spacing progression census on \(E\). The elementary maximum-length observation and the fibbinary/odd-binomial equivalence are background, not claimed as new.

## Limitations
The exact count concerns complete dyadic initial intervals and three-term progressions only; it does not prescribe the distribution by a fixed common difference or arbitrary cutoffs. There is no assertion of uniqueness among all possible formulations or independent historical-priority certification. The original 2002 sci.math post is dated in contemporary bibliographic accounts but was not inspected in full. Earlier work with different terminology, especially on Fibonacci-cube additive patterns, could remain undiscovered.

## References
1. OEIS Foundation, A003714, *Fibbinary numbers*, https://oeis.org/A003714 (includes a July 17, 2002 sci.math reference and the parity characterization of \(\binom{3n}{n}\)).
2. L. Lindroos, A. Sills, H. Wang, *Odd Fibbinary Numbers and the Golden Ratio*, Fibonacci Quarterly 52 (2014), 61–65, https://www.fq.math.ca/Papers1/52-1/LindroosSillsWang.pdf.
3. M. Mollard, *Maximal hypercubes in Fibonacci and Lucas cubes*, arXiv:1201.1494, first posted January 6, 2012, https://arxiv.org/abs/1201.1494.
4. *Exact dyadic valuation law for* \(\binom{3n}{n}\), published published-finding corpus finding, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-dyadic-valuation-law-for-binom-3n-n--499526ba814d/RESULT.md.
5. *Exact arithmetic-progression census in odd-binomial Pascal rows*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-arithmetic-progression-census-in-odd-binomial-pascal-rows--50ffd95589d7/RESULT.md.
