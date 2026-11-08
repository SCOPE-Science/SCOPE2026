# Dyadic cubic curve: exact fourth Fourier moments and two-sum support

## Finding

For every integer \(k\ge1\), put \(N=2^k\), \(R=\mathbb Z/N\mathbb Z\), and let \(C_k=\{(x,x^3):x\in R\}\subset R^2\). The ordered two-sum representation function \(r_k(s,t)=\#\{(x,y)\in R^2:x+y=s,\ x^3+y^3=t\}\) has the exact, valuation-stratified description proved below. In particular the additive energy and twofold sumset size are, for **every** \(k\ge1\),

\[
E(C_k)=\sum_{s,t\in R}r_k(s,t)^2=\frac{N^2}{4}(k^2-k+8),
\]

\[
|C_k+C_k|=\begin{cases}
(5N^2+13N-10)/18,&k\text{ odd},\\
(5N^2+14N-10)/18,&k\text{ even}.
\end{cases}
\]

For the unweighted cubic exponential sum \(F_k(a,b)=\sum_{x\in R}\exp(2\pi i(ax+bx^3)/N)\), the same energy is the exact complete fourth Fourier moment with probability normalization on the dual group:

\[
\frac1{N^2}\sum_{a,b\in R}|F_k(a,b)|^4=\frac{N^2}{4}(k^2-k+8).
\]

Thus the normalized energy \(E(C_k)/|C_k|^2\) grows quadratically in \(k\), while \(|C_k+C_k|/N^2\to5/18\).

## Assumptions and scope

Every variable and equality involving \(R\) is interpreted modulo \(N\). The curve has exactly \(N\) points, since its first coordinate is injective. Representation counts include ordered pairs and repetitions. No assumption is made about coefficients for arbitrary-weight Fourier extension: the fourth moment above concerns **unit coefficients** at every point of \(C_k\).

Define, for \(m\ge1\),
\[
\rho_m(z)=\#\{u\bmod2^m:u^2\equiv z\pmod{2^m}\}.
\]

The pointwise two-sum law is:

1. For \(s=0\), \(r_k(0,t)=N\) when \(t=0\), and zero otherwise.
2. For odd \(s\), \(r_k(s,t)=2\) for odd \(t\), and zero for even \(t\).
3. If \(s\ne0\) is even, let \(v=v_2(s)\in\{1,\ldots,k-1\}\), \(m=k-v\), \(u=s/2^v\) (odd), choose \(h\) satisfying \(2h=s\) in \(R\), and put \(c=2h^3\). If \(t-c\not\equiv0\pmod{2^v}\), then \(r_k(s,t)=0\). Otherwise put
\[
 z=\left((t-c)/2^v\right)(3u)^{-1}\pmod{2^m}
\]
 and then \(r_k(s,t)=2^v\rho_m(z)\). The expression is independent of the choice of \(h\).

The square-root fiber is explicit: \(\rho_m(0)=2^{\lfloor m/2\rfloor}\); if \(z\ne0\) has odd \(2\)-adic valuation then \(\rho_m(z)=0\). If \(v_2(z)=2j<m\), let \(\ell=m-2j\) and \(w=z/2^{2j}\) (odd modulo \(2^\ell\)). Then
\[
\rho_m(z)=\begin{cases}
2^j,&\ell=1,\\
2^{j+1},&\ell=2\ \text{and}\ w\equiv1\pmod4,\\
2^{j+2},&\ell\ge3\ \text{and}\ w\equiv1\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]

## Proof

**Step 1 (parity strata).** Fix \(s\). The cubic identity
\[
x^3+(s-x)^3=s^3-3s\,x(s-x)\]
reduces the ordered convolution to one quadratic congruence. If \(s=0\), the cubic terms cancel for all \(x\), proving the first case. If \(s\) is odd, \(x(s-x)\) is always even. For any prescribed even residue \(b\), the equation \(x(s-x)=b\) has one solution of each parity: each of the two roots modulo two lifts uniquely because \(s-2x\) is odd. The factor \(3s\) is a unit, so precisely the odd \(t\) occur, each twice.

If \(s=2^vu\) is even and nonzero, write \(s=2h\), \(x=h+z_0\), \(y=h-z_0\). The exact integer polynomial identity gives
\[
x^3+y^3=2h^3+6hz_0^2=2h^3+3s z_0^2.\]
There is a solution precisely when \(t-c\) is divisible by \(2^v\) and \(z_0^2\equiv z\pmod{2^m}\). Every solution modulo \(2^m\) has \(2^v\) lifts modulo \(2^k\). Changing \(h\) to the other possible half changes it by \(N/2\), and the displayed cubic polynomial changes by a multiple of \(N\); the count is therefore well defined.

**Step 2 (square fibers).** The square roots of an odd unit modulo \(2^\ell\) number respectively \(1,2,4\) for \(\ell=1,2,\ell\ge3\), provided the unit has residues \(1\pmod2\), \(1\pmod4\), \(1\pmod8\); otherwise they are absent. For a nonzero square of valuation \(2j\), extract \(2^j\) from the root, giving \(2^j\) lifts of the unit roots. For the zero square, exactly the multiples of \(2^{\lceil m/2\rceil}\) qualify. These facts give the formula for \(\rho_m\) above.

**Step 3 (the square-fiber second moment).** Let \(B_m=\sum_{z\bmod2^m}\rho_m(z)^2\), the number of pairs of residues having equal squares. Directly \(B_1=2\) and \(B_2=8\). For \(m\ge3\), odd pairs contribute \(2^{m+1}\): the \(2^{m-3}\) odd unit-square values have four roots each. An even pair is obtained by writing both variables as twice a residue; after dividing the equality by four, each lower-modulus pair has four lifts. Hence
\[
 B_m=2^{m+1}+4B_{m-2}=m2^m\quad(m\ge1),
\]
where the final equality follows by induction with the two base cases.

**Step 4 (energy).** The zero slice contributes \(N^2\) and all odd \(s\) together contribute another \(N^2\). For each \(m\in\{1,\ldots,k-1\}\) there are \(2^{m-1}\) values of \(s\) with valuation \(k-m\). The energy of each such slice is \(2^{2(k-m)}B_m\), and consequently the entire valuation stratum contributes
\[
2^{m-1}2^{2(k-m)}B_m=\frac{mN^2}{2}.
\]
Thus \(E(C_k)=2N^2+(N^2/2)\sum_{m=1}^{k-1}m=N^2(k^2-k+8)/4\).

**Step 5 (sumset size).** Write \(Q_m=\#\{u^2\bmod2^m:u\in\mathbb Z\}\). The square-fiber classification gives \(Q_1=Q_2=2\) and \(Q_m=2^{m-3}+Q_{m-2}\) for \(m\ge3\). Thus
\[
Q_m=\begin{cases}
(2^{m-1}+5)/3,&m\text{ odd},\\
(2^{m-1}+4)/3,&m\text{ even}.
\end{cases}
\]
The slices \(s=0\), odd \(s\), and \(v_2(s)=k-m\) contribute respectively \(1\), \(N^2/4\), and \(2^{m-1}Q_m\) elements to the sumset. Therefore
\[
|C_k+C_k|=1+N^2/4+\sum_{m=1}^{k-1}2^{m-1}Q_m.
\]
Substituting the closed forms for \(Q_m\) and summing two geometric progressions yields exactly the stated two parity branches. The formulas hold already at \(k=1\), when the sum is empty.

**Step 6 (Fourier orthogonality).** Expanding the fourth power of \(F_k\) and averaging independently in \(a,b\) counts exactly the ordered quadruples with matching first and cubic-coordinate sums. This is \(E(C_k)\), proving the Fourier identity.

## Verification

A standalone pure-Python checker, `check_cubic_dyadic.py`, first independently enumerates square fibers and compares their sizes and second moments with the closed formulas for \(1\le m\le10\). It then directly enumerates every ordered pair of cubic-curve points, checks **every** target's convolution coefficient against the formula, and compares exact energy and support size for \(1\le k\le10\). Reproduce with `python check_cubic_dyadic.py`. Expected terminal marker: `DYADIC_CUBIC_CURVE_CONVOLUTION_CHECK_PASS`. Finite tests corroborate but do not replace the proof valid for all \(k\).

## Relationship to prior work

Cubic Fourier extension and high-order mean-value problems are developed by Wooley (2014) and Hughes–Wooley (2019), but their inspected results are bounds for integer intervals, not an exact two-sum law on dyadic cyclic rings. Hickman–Wright (2018) formulate Fourier restriction for general residue rings, with principal examples including the paraboloid; their stated estimates do not yield this particular exact global dyadic cubic-curve energy or sumset formula. Dehnavi, Mirzaee Shamsabad and Mahmoodi Rishakani (2019) classify roots of *arbitrary* quadratic congruences modulo powers of two: their general theorem therefore covers the underlying pointwise quadratic solver, and no separate priority is asserted for that solver. The contribution assessed here is the aggregate closed counting law and its Fourier/sumset consequences, which require a valuation-wide fiber summation. No claim of exhaustive historical priority is made.

## Limitations

No unrestricted optimal fourth-moment extension constant or optimizer classification is claimed, and no odd-prime or non-power-of-two modulus is covered. The square-root part is standard arithmetic and not presented as a novel standalone result. Although literature and published-result searches found no formula matching both global identities, an earlier local-density calculation may imply them. Independent mathematical review is not yet performed.

## References

- T. D. Wooley, *Mean value estimates for odd cubic Weyl sums*, arXiv:1401.7152, first public version 2014-01-28. https://arxiv.org/abs/1401.7152
- K. Hughes and T. D. Wooley, *Discrete restriction for (x,x^3) and related topics*, arXiv:1911.12262, first public version 2019-11-27. https://arxiv.org/abs/1911.12262
- J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, Discrete Analysis 2018:11. https://arxiv.org/abs/1801.03176
- S. M. Dehnavi, M. R. Mirzaee Shamsabad, and A. Mahmoodi Rishakani, *Complete solving the quadratic equation mod 2^n*, Notes on Number Theory and Discrete Mathematics 25 (2019), 75–83, doi:10.7546/nntdm.2019.25.1.75-83. https://nntdm.net/papers/nntdm-25/NNTDM-25-1-075-083.pdf
