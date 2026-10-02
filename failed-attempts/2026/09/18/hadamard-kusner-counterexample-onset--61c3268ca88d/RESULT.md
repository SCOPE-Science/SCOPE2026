# Hadamard-order amplification and onset bounds for Kusner counterexamples

## Statement

Write \(e(\ell_p^n)\) for the maximum cardinality of an equilateral set in
\(\ell_p^n\).  For \(p>4\), define the first counterexample dimension
\[
\nu(p)=\min\{n\ge 1:e(\ell_p^n)\ge n+2\}.
\]
Nathan Xiong recently proved that \(\nu(p)<\infty\) for every \(p>4\) by
constructing \(8m\) equilateral points in \(\ell_p^{8m-2}\) for a sufficiently
large power of two \(m\).

For \(a>1\), set
\[
R=a^p+2,\qquad
A=(a+1)^p+(a-1)^p+2,\qquad
B=2a^p+2^p
\]
and
\[
F_p(a)=\frac{2A-B}{2^{p-1}R}.
\]
At
\[
a_0=4^{1/p}
\]
define the explicit positive margin
\[
\Delta(p)=F_p(a_0)-1
=
\frac{
2(1+4^{1/p})^p+2(4^{1/p}-1)^p-4-2^{p+2}
}{
3\,2^p
}.
\tag{1}
\]
Xiong's Lemma 4.1 implies \(\Delta(p)>0\) for every \(p>4\).

**Theorem 1 (Hadamard-order transfer).**
Let \(p>4\). If a real Hadamard matrix of order \(m\) exists and
\[
m>\frac1{\Delta(p)},
\tag{2}
\]
then
\[
\boxed{e(\ell_p^{8m-2})\ge 8m.}
\tag{3}
\]
Thus Xiong's Walsh-matrix construction does not require \(m\) to be a power of
two: every admissible Hadamard order above the same analytic threshold works.

Let
\[
c_4=
\sqrt2\,\log(1+\sqrt2)-\frac74\log2
=0.0334429143005567\ldots .
\tag{4}
\]
Then
\[
\Delta(4+\varepsilon)
=
c_4\varepsilon+O(\varepsilon^2)
\qquad(\varepsilon\downarrow0).
\tag{5}
\]
The asymptotic density of Hadamard orders consequently yields
\[
\boxed{
\nu(4+\varepsilon)
\le
\left(\frac8{c_4}+o(1)\right)\frac1\varepsilon
=
\frac{239.2136022627\ldots+o(1)}{\varepsilon}.
}
\tag{6}
\]

Combining this with Swanepoel's explicit stability interval around \(p=4\)
gives a two-sided onset window:
\[
\boxed{
\frac{8+o(1)}
{\varepsilon\log(1/\varepsilon)}
\le
\nu(4+\varepsilon)
\le
\frac{239.2136022627\ldots+o(1)}{\varepsilon}.
}
\tag{7}
\]
In particular, the minimum dimension of a Kusner counterexample diverges as
\(p\downarrow4\), and its presently available upper and lower scales differ by
only one logarithm.

There is also a quantitative large-\(p\) consequence:
\[
\Delta(p)
=
\frac{2(\log2)^2}{3p}+O(p^{-2}),
\qquad p\to\infty,
\tag{8}
\]
and hence
\[
\boxed{
\nu(p)
\le
\left(\frac{12}{(\log2)^2}+o(1)\right)p
=
(24.9764277721\ldots+o(1))p.
}
\tag{9}
\]

No optimality of the upper bounds (6) or (9) among all equilateral
constructions is asserted.

## Proof of Theorem 1

Let \(H=(h_{sr})\) be a Hadamard matrix of order \(m\), normalized so that a
distinguished column \(r=0\) consists entirely of \(+1\)'s.  Let \(K=H_4\) be
the \(4\times4\) Walsh Hadamard matrix, with rows and columns indexed by
\(\mathbb F_2^2\), and put
\[
G=K\otimes H.
\]

Use the same four vectors as in Xiong's construction:
\[
\begin{aligned}
q_{00}&=(a,1,1,0),&
q_{10}&=(1,-a,0,1),\\
q_{01}&=(1,0,-a,-1),&
q_{11}&=(0,1,-1,a).
\end{aligned}
\tag{10}
\]
They satisfy
\[
\|q_i\|_p^p=R
\]
and, for \(i\ne i'\),
\[
\|q_i-q_{i'}\|_p^p
=
\|q_i+q_{i'}\|_p^p
=
\begin{cases}
A,&i+i'\in\{10,01\},\\
B,&i+i'=11.
\end{cases}
\tag{11}
\]

For \(i\in\mathbb F_2^2\) and a row \(s\) of \(H\), define the front block
\[
U_{i,s}
=
(h_{s1}q_i,\ldots,h_{sm}q_i)\in\mathbb R^{4m}.
\tag{12}
\]
For the back block, take row \((i,s)\) of \(G\).  Among the four coordinates
whose \(H\)-column is the distinguished column \(r=0\), delete those with
\(K\)-column \(00\) and \(11\), multiply those with \(K\)-column \(10\) and
\(01\) by \(\beta\), and multiply every other coordinate by \(\alpha\).  This
gives
\[
V_{i,s}\in\mathbb R^{4m-2}.
\tag{13}
\]
Finally set
\[
X_{\sigma,i,s}=(\sigma U_{i,s},V_{i,s}),
\qquad
\sigma\in\{\pm1\}.
\tag{14}
\]
There are \(8m\) such points.

Choose \(a>1\) so that
\[
F_p(a)=1+\frac1m,
\tag{15}
\]
and define
\[
\alpha^p=\frac R4,\qquad
\beta^p=\frac{m(A-B)}{2^p}.
\tag{16}
\]
The positivity of \(\beta\) follows from Xiong's elementary inequality
\(A>B\) for \(p>2\), \(a>1\).

It remains to justify that (15) has a solution and that the distance count is
unchanged when the Walsh matrix of order \(m\) is replaced by \(H\).
First,
\[
F_p(1)=\frac{2+2^{2-p}}3<1,
\]
whereas \(F_p(a_0)=1+\Delta(p)>1+1/m\) by (2).  Continuity therefore gives
a solution \(a\in(1,a_0)\).

Any two distinct rows of a Hadamard matrix agree in exactly \(m/2\) entries
and differ in exactly \(m/2\).  Hence the front-block counts used by Xiong
depend only on orthogonality of rows, not on the Walsh group structure.
Likewise, two distinct rows of \(G=K\otimes H\) differ in exactly \(2m\)
coordinates.  The normalization of the distinguished column makes the four
special coordinates depend only on the \(K\)-row.  Thus, if the \(i\)-indices
are equal, none of the special coordinates differs; if \(i+i'\ne0\), exactly
two of the four special coordinates differ.

The four possible pair types therefore have the following \(p\)-th-power
front and back contributions:
\[
\begin{array}{c|c|c}
\text{pair type}&\text{front}&\text{back}\\ \hline
(i,s)=(i',s')&
2^pmR&0\\
i=i',\ s\ne s'&
2^{p-1}mR&2^{p-1}mR\\
i+i'\in\{10,01\}&
mA&2^{p-1}(m-1)R+m(A-B)\\
i+i'=11&
mB&2^{p-1}(m-1)R+2m(A-B).
\end{array}
\tag{17}
\]
Using (15), equivalently
\[
2A-B=2^{p-1}R\left(1+\frac1m\right),
\tag{18}
\]
each row of (17) sums to \(2^pmR\).  Hence all \(8m\) points in (14) are
equilateral, proving (3).

## Hadamard-order density and the upper asymptotics

Swanepoel and Villa record the standard fact that if \(H(x)\) is the largest
Hadamard order below \(x\), then
\[
\frac{H(x)}x\longrightarrow1.
\tag{19}
\]
Their proof uses the Paley construction together with the prime number theorem
for arithmetic progressions.  Consequently, whenever \(T\to\infty\), there is
a Hadamard order
\[
m>T,\qquad m=(1+o(1))T.
\tag{20}
\]
Apply this with \(T=1/\Delta(p)\).

For \(p=4+\varepsilon\), direct differentiation of (1) at \(p=4\) gives
\[
\Delta(4)=0,\qquad
\Delta'(4)
=
\sqrt2\,\log(1+\sqrt2)-\frac74\log2=c_4>0.
\]
This proves (5), and (20) together with Theorem 1 gives (6).

For completeness, the same expansion can be viewed geometrically through the
unoptimized parameter function.  At \(p=4\),
\[
F_4(a)-1
=
-\frac{3(a^2-2)^2}{4(a^4+2)},
\tag{21}
\]
so \(a=\sqrt2\) is the unique maximizing point and the \(p=4\) construction
is exactly tangent to the equilateral threshold there.

For \(p\to\infty\), write \(L=\log4\) and \(a_0=e^{L/p}\).  Then
\[
\left(\frac{1+a_0}{2}\right)^p
=
2+\frac{(\log2)^2}{p}+O(p^{-2}),
\tag{22}
\]
while \(((a_0-1)/2)^p\) is superpolynomially small.  Substitution into (1)
gives (8), and (20) yields (9).

## Lower bound near \(p=4\)

Swanepoel proved that
\[
|p-4|
<
\frac{4\log(1+2/n)}{\log(n+2)}
\tag{23}
\]
implies
\[
e(\ell_p^n)=n+1.
\]
Therefore a counterexample in dimension \(n\) at \(p=4+\varepsilon\) must
satisfy
\[
\varepsilon
\ge
\frac{4\log(1+2/n)}{\log(n+2)}
=
\frac{8+o(1)}{n\log n}.
\tag{24}
\]
Taking \(n=\nu(4+\varepsilon)\) and inverting (24) gives
\[
\nu(4+\varepsilon)
\ge
\frac{8+o(1)}
{\varepsilon\log(1/\varepsilon)}.
\tag{25}
\]
Together with (6), this proves (7).

## Context and limitations

Xiong's 2026 construction establishes counterexamples for every \(p>4\) but
uses a Sylvester/Walsh order \(m=2^k\) and only asks that it be sufficiently
large.  Theorem 1 isolates the exact feature needed from that matrix:
Hadamard orthogonality plus one normalized column.  This permits the
asymptotically dense family of Hadamard orders to be used and makes the
dimension dependence on \(p\) explicit.

The method of exploiting dense Hadamard orders has a clear precedent in
Swanepoel--Villa's work for \(1\le p<2\).  The present result applies that
principle to the structurally different recent \(p>4\) construction and
combines it with Swanepoel's \(p=4\) stability theorem to quantify the newly
resolved transition from validity to failure of Kusner's conjecture.

The upper and lower bounds in (7) do not match: a logarithmic gap remains.
The constants in (6) and (9) describe this Hadamard-amplified construction,
not the true optimum over all equilateral configurations.  In particular,
Chalmers' certified \(58\)-point configuration in \(\ell_5^{56}\) is a
different construction and can outperform the bounds obtained here at
specific exponents.  No assertion is made that \(\nu(p)\) grows linearly as
\(p\to\infty\).

## References

1. N. Xiong, *Kusner's conjecture is false for \(p>4\)*,
   arXiv:2609.14794 (2026).
   https://arxiv.org/abs/2609.14794
2. K. J. Swanepoel and R. Villa, *Maximal Equilateral Sets*,
   Discrete Comput. Geom. 50 (2013), 354--373.
   https://doi.org/10.1007/s00454-013-9523-z
3. K. J. Swanepoel, *Equilateral Sets and a Schütte Theorem for the
   \(4\)-norm*, Canad. Math. Bull. 57 (2014), 640--647.
   https://doi.org/10.4153/CMB-2013-031-0
4. L. R. Chalmers, *A counterexample to Kusner's conjecture on equilateral
   sets*, arXiv:2608.14013 (2026).
   https://arxiv.org/abs/2608.14013
5. H.-J. Ge, Z. Xu, Y. Zhou, *Kusner's conjecture: Exact values and linear
   bounds*, arXiv:2606.03987 (2026).
   https://arxiv.org/abs/2606.03987
