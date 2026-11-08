# Exact inverse-tail floors for reciprocal squares of Jacobsthal numbers

## Finding
Let \(J_0=0\), \(J_1=1\), and \(J_{k+2}=J_{k+1}+2J_k\). For each integer \(n\ge1\), put
\[
S_n=\sum_{k=n}^{\infty}\frac{1}{J_k^2},\qquad
A_n=\frac{3\cdot4^n-4(-2)^n}{36}.
\]
Then the exact all-index formula is
\[
\boxed{\left\lfloor S_n^{-1}\right\rfloor=\left\lfloor A_n\right\rfloor\qquad(n\ge1).}
\]
For every integer \(n\ge3\), the stronger strict inequality
\[
\boxed{A_n-\frac19<S_n^{-1}<A_n}
\]
holds. The difference has a definite nonzero limit:
\[
\boxed{\lim_{n\to\infty}(A_n-S_n^{-1})=\frac7{135}.}
\]
The fractional part of \(A_n\) is respectively \(5/9\), \(8/9\), or \(2/9\), according as \(n\equiv1,2,0\pmod3\). Thus the formula is a genuinely explicit integer answer without needing the original infinite tail.

## Assumptions and scope
The series is over all integer indices \(k\ge n\) and converges absolutely. We use the standard Jacobsthal normalization with \(J_0=0,J_1=1\), so that \(J_k=(2^k-(-1)^k)/3\). The floor is the greatest integer not exceeding a real number. No restriction on the parity or residue class of \(n\) is imposed. The strict gap is claimed for \(n\ge3\), while \(n=1,2\) are addressed separately.

## Proof
**1. Exact convergent expansion.** Set \(x=2^{-n}\) and \(\varepsilon=(-1)^n\). The closed Jacobsthal formula gives
\[
S_n=9\sum_{h=0}^{\infty}\frac{x^2 4^{-h}}{(1-\varepsilon(-1)^h x2^{-h})^2}.
\]
Since \(0<x\le1/2\), expand each squared denominator using \((1-z)^{-2}=\sum_{j\ge0}(j+1)z^j\). Absolute convergence allows summation first in \(h\). The resulting exact series is
\[
S_n=\sum_{j=0}^{\infty}a_j\varepsilon^j x^{j+2},\qquad
 a_j=\frac{9(j+1)}{1-(-1)^j2^{-(j+2)}}.
\]
In particular,
\[
a_0=12,\qquad a_1=16,\qquad a_2=\frac{144}{5},\qquad a_3=\frac{384}{11}.
\]

**2. Uniform remainder at every \(n\ge3\).** Here \(x\le1/8\). For \(j\ge4\), the displayed coefficient satisfies \(0<a_j\le12(j+1)\). Write
\[
S_n=12x^2+16\varepsilon x^3+\frac{144}{5}x^4+
\frac{384}{11}\varepsilon x^5+R_n.
\]
The exact geometric tail estimate gives
\[
|R_n|\le12x^6\left(\frac5{1-x}+\frac{x}{(1-x)^2}\right)
\le\frac{3456}{49}x^6<71x^6.
\]
Since \(A_n=(1-\tfrac43\varepsilon x)/(12x^2)\), multiplication and collection of the first four terms yield
\[
A_nS_n-1=\frac{28}{45}x^2-\frac{16}{55}\varepsilon x^3
-\frac{128}{33}x^4+A_nR_n.
\]
The same parameter bound implies \(0<A_n\le7/(72x^2)\) and therefore \(|A_nR_n|\le(497/72)x^4\). Put \(C=8539/792=128/33+497/72\). For every \(0<x\le1/8\),
\[
x^2\left(\frac{28}{45}-\frac{16}{55}x-Cx^2\right)
\le A_nS_n-1\le
x^2\left(\frac{28}{45}+\frac{16}{55}x+Cx^2\right).
\]
The lower bracket is decreasing in \(x\) and equals \(21157/50688>0\) at \(x=1/8\). The upper bracket is increasing and equals \(69869/84480<256/243\) at \(x=1/8\). Thus these are explicit exact rational bounds for the entire parameter interval, independent of numerical testing.

On the other hand, \(|\varepsilon(-1)^h x2^{-h}|\le x\) in the exact series from Step 1, hence
\[
S_n\ge\frac{9x^2}{(1+x)^2}\sum_{h=0}^{\infty}4^{-h}
=\frac{12x^2}{(1+x)^2}
\ge\frac{256}{27}x^2.
\]
Consequently \(0<A_nS_n-1<S_n/9\), and division by the positive \(S_n\) proves
\[
0<A_n-S_n^{-1}<\frac19\qquad(n\ge3).
\]

**3. Passing to integer parts.** Define \(u_n=3\cdot4^n-4(-2)^n\). For every \(n\ge1\),
\[
u_{n+3}-u_n=189\cdot4^n+36(-2)^n\equiv0\pmod{36}.
\]
Directly \(u_1\equiv20\), \(u_2\equiv32\), and \(u_3\equiv8\pmod{36}\). Thus \(\{A_n\}\in\{5/9,8/9,2/9\}\), always at least \(2/9\) above the preceding integer. Since \(S_n^{-1}\) lies strictly between \(A_n-1/9\) and \(A_n\), the two have identical floors for all \(n\ge3\). For \(n=1,2\), the series contains a unit summand and at least one other positive summand, so \(0<S_n^{-1}<1\). Also \(A_1=5/9\) and \(A_2=8/9\), proving the remaining cases.

**4. Limit.** The exact series gives \(S_n=12x^2+O(x^3)\), and Step 2 gives \(A_nS_n-1=(28/45)x^2+O(x^3)\), as \(x\to0\). Therefore
\[
A_n-S_n^{-1}=\frac{A_nS_n-1}{S_n}\longrightarrow
\frac{28/45}{12}=\frac7{135}.
\]
Every step uses convergent series and rational inequalities, not experimental extrapolation.

## Verification
The standalone `checker.py` evaluates exact rational enclosures for \(S_n^{-1}\) at every integer \(1\le n\le64\). Positivity gives a lower bound from a finite partial sum and an upper bound from a geometric error. The floors of both rational enclosures match the formula, and for \(n\ge3\) the enclosures also verify the strict gap. Exact rational assertions check the uniform constants and the three-term residue cycle. Run with `python3 checker.py`; the expected terminal output begins `VERIFY_OK`. This computational range is only corroboration; Steps 1–4 establish the theorem for all indices.

## Relationship to prior work
Ahmed Gaber's *On the reciprocal sum of Jacobsthal numbers* (publicly available on 19 July 2022, arXiv:2207.12857v1) studies precisely these reciprocal-square tails. Its Theorem 2.2 prints a one-sided bound at odd indices rather than the exact all-index floor. As printed, its stated direction is incompatible with the direct case \(n=3\): it would put the floor at most \(J_2J_3=3\), whereas the present exact formula gives \(6\). The present theorem independently establishes the corrected exact value without using that bound. It is therefore not a corollary of Theorem 2.2 as stated.

Koshy and Gao's 2024 *Sums Involving a Class of Jacobsthal Polynomial Squares* and *Sums Involving a Family of Jacobsthal Polynomial Squares* were also inspected. Their principal identities use weighted telescoping expressions with quadratic denominators at sparse indices; neither inspected document gives the integer part of the inverse of the unweighted reciprocal-square tail above. Related published results for reciprocal powers of Fibonacci and balancing sequences likewise concern different sequences or powers.

## Limitations
This theorem concerns the ordinary Jacobsthal sequence only, not arbitrary parameter Jacobsthal polynomials, alternating reciprocal-square sums, higher reciprocal powers, or Jacobsthal–Lucas tails. The strict \(1/9\) error bound is sufficient to determine floors, not claimed best possible. The constant \(7/135\) is the proven asymptotic error limit. No result about the published literature beyond the named inspected texts is claimed; unindexed or inaccessible equivalent work remains an originality risk. No independent scientific audit has been performed.

## References
- Ahmed Gaber, *On the reciprocal sum of Jacobsthal numbers*, arXiv:2207.12857v1 (19 July 2022), https://arxiv.org/abs/2207.12857 . Particularly Theorem 2.2 and Section 3.
- Thomas Koshy and Zhenguang Gao, *Sums Involving a Class of Jacobsthal Polynomial Squares*, Fibonacci Quarterly 62 (2024), 40–44, https://www.fq.math.ca/Papers/62-1/koshy09122023.pdf .
- Thomas Koshy and Zhenguang Gao, *Sums Involving a Family of Jacobsthal Polynomial Squares*, Fibonacci Quarterly 62 (2024), 130–135, https://www.fq.math.ca/Papers/62-2/koshy12202023.pdf .
