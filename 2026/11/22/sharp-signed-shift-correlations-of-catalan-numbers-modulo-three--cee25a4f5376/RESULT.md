# Sharp signed shift correlations of Catalan numbers modulo three

## Finding
For the Catalan numbers \(C_n=\frac{1}{n+1}\binom{2n}{n}\), let \(\epsilon(n)\in\{-1,0,1\}\) be the signed representative of \(C_n\pmod 3\). For each integer \(h\ge1\), the normalized signed shift correlation
\[
R(h)=\lim_{r\to\infty}\frac1{2^r}\sum_{n=0}^{3^r-1}\epsilon(n)\epsilon(n+h)
\]
exists and is rational. Define \(\alpha(0)=1\) and, for integers \(q\ge0\),
\[
\alpha(3q) = \alpha(q)\quad(q\ge1),\qquad
\alpha(3q+1)=-\tfrac12\alpha(q),\qquad
\alpha(3q+2)=-\tfrac12\alpha(q+1).
\]
For \(h=3q+t\) with \(t\in\{0,1,2\}\),
\[
\boxed{R(h)=\tfrac12\big((3-t)\alpha(q)+t\alpha(q+1)\big).}
\]
Moreover, the following bounds are sharp, with **all** equality cases:
\[
-\tfrac34\le R(h)\le\tfrac34,\qquad
R(h)=\tfrac34\iff h=1,\qquad
R(h)=-\tfrac34\iff h=3^j\text{ for an integer }j\ge1.
\]

## Assumptions and scope
All indices and shifts are ordinary nonnegative or positive integers as specified, and the limit uses complete ternary blocks of length \(3^r\), normalized by \(2^r\). The result is not a claim about the ordinary density of the nonzero support, which is zero. Signed residues use \(-1\) for the residue \(2\pmod3\). The first public source for the foundational digit rule is the preprint of Deutsch and Sagan, dated July 19, 2004.

## Proof
Let \(s(0)=1\). For \(m>0\), write \(m\) in base three and put \(s(m)=0\) if any digit is \(2\); otherwise put \(s(m)=(-1)^u\) where \(u\) is the number of digits equal to \(1\). The known signed digit congruence for Catalan numbers modulo three [1] states exactly
\[
\epsilon(n)=s\left(\left\lfloor\frac{n+1}{3}\right\rfloor\right).
\]
Thus \(s(3m)=s(m)\), \(s(3m+1)=-s(m)\), and \(s(3m+2)=0\).

For integers \(k\ge0\), \(v\ge0\), let
\[
A_k(v)=2^{-k}\sum_{0\le m<3^k}s(m)s(m+v).
\]
Splitting \(m\) by its last ternary digit proves the exact identities for \(k\ge1\):
\[
A_k(3v)=A_{k-1}(v),\quad
A_k(3v+1)=-\tfrac12 A_{k-1}(v),\quad
A_k(3v+2)=-\tfrac12 A_{k-1}(v+1).
\]
For every \(k\), \(A_k(0)=1\), because exactly \(2^k\) indices in the block have \(s(m)^2=1\). For a fixed \(v\), each recursion reduces the argument to at most \(\lfloor(v+1)/3\rfloor\), so after finitely many iterations it becomes zero. Consequently \(A_k(v)\) eventually stabilizes **exactly** to the unique \(\alpha(v)\) given above.

Write \(x=n+1\). On any complete ternary block of \(x\), the three residue classes \(x\pmod3\) contribute \(3-t\) copies of \(s(m)s(m+q)\) and \(t\) copies of \(s(m)s(m+q+1)\) when \(h=3q+t\). The shift from \(n\in[0,3^r)\) to \(x\in[1,3^r]\) replaces only \(x=0\) by \(x=3^r\). For every fixed \(h\), and all sufficiently large \(r\), the two corresponding products are equal: the high ternary digit in each of the latter two \(s\)-factors changes each sign, and the product is unchanged. Therefore the normalized sum equals
\[
\frac12\big((3-t)A_{r-1}(q)+tA_{r-1}(q+1)\big),
\]
and hence the asserted expression for \(R(h)\); in fact the finite identity with \(\alpha\) itself holds for every sufficiently large \(r\).

Induction in the recursion proves \(|\alpha(v)|\le\frac12\) for every \(v\ge1\). More precisely, equality holds exactly when \(v\) is a power of three, and then \(\alpha(v)=-\frac12\): in the class \(v\equiv0\pmod3\) equality descends to a smaller argument; in the class \(v\equiv1\pmod3\) it occurs only at \(v=1\); and in the class \(v\equiv2\pmod3\), \(|\alpha(v)|\le1/4\). For \(h=3q\) with \(q\ge1\), this yields the lower endpoint precisely when \(q\) is a power of three. When \(h\equiv1,2\pmod3\) and \(q\ge1\), equality in the triangle bound \(|R(h)|\le3/4\) would require both consecutive positive integers \(q\) and \(q+1\) to be powers of three, which is impossible. Finally \(R(1)=3/4\) and \(R(2)=0\). This proves both sharpness classifications.

## Verification
The accompanying standalone `check.py` checks the digit formula against the direct Catalan binomial expression for the first 500 indices, exact finite-block correlations where stabilization applies, and the inequalities/equality patterns for 30,000 shifts. These are regression checks, not replacements for the unrestricted proof. Running it with Python 3 and standard-library modules `math`, `fractions`, and `functools` prints a count of successful assertions.

## Relationship to prior work
Deutsch and Sagan [1] establish the foundational digit congruence, not the evaluated signed all-shift autocorrelation or its extremizers. Burns [2] studies nondivisibility density and repeats the digit description, but a one-point density cannot determine a signed two-point correlation. Rowland and Yassawi [3] give broad automatic-sequence techniques, without the explicit theorem claimed here in the inspected material. In particular, an unsigned progression census of the translated Motzkin support does not provide these signed Catalan correlations.

## Limitations
The correlations are normalized on ternary blocks by \(2^r\), not by \(3^r\). Novelty is qualified: general digit-correlation identities outside the inspected sources might specialize to this result. No independent mathematical audit has been performed. The finite regression suite does not establish the infinitely many shift cases.

## References
[1] E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first posted July 19, 2004), Theorem 5.2. https://arxiv.org/abs/math/0407326

[2] R. Burns, *Asymptotic density of Catalan numbers modulo 3 and powers of 2*, arXiv:1611.03705 (first posted November 11, 2016), Section 3. https://arxiv.org/abs/1611.03705

[3] E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (first posted October 31, 2013). https://arxiv.org/abs/1310.8635
