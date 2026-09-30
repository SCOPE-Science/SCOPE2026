# Hadamard-order refinement of Kusner counterexamples near \(p=4\)

## Statement

Let \(e(\ell_p^n)\) denote the largest cardinality of an equilateral subset of \(\ell_p^n\). For \(p>4\), define the first failure dimension
\[
d_*(p)=\min\{n\ge 1:e(\ell_p^n)\ge n+2\}.
\]
Nathan Xiong proved that \(d_*(p)\) is finite for every \(p>4\) by constructing \(8m\) equilateral points in \(\ell_p^{8m-2}\) for a sufficiently large power of two \(m\).

For \(p>4\) and \(a>1\), set
\[
R=a^p+2,\qquad
A=(a+1)^p+(a-1)^p+2,\qquad
B=2a^p+2^p,
\]
and
\[
\Phi_p(a)=\frac{2A-B}{2^{p-1}R},\qquad
a_0(p)=4^{1/p},\qquad
\Delta(p)=\Phi_p(a_0(p))-1.
\]
Xiong's argument gives \(\Delta(p)>0\) for \(p>4\).

**Theorem.** If an \(m\times m\) Hadamard matrix exists and
\[
m>\frac{1}{\Delta(p)},
\]
then there is an equilateral set of \(8m\) points in \(\ell_p^{8m-2}\). Consequently,
\[
d_*(p)\le 8m-2
\]
for every Hadamard order \(m>1/\Delta(p)\).

Moreover, as \(\delta\downarrow0\),
\[
\boxed{
\frac{8+o(1)}{\delta\log(1/\delta)}
\le d_*(4+\delta)
\le
\frac{8/c+o(1)}{\delta}
}
\]
where
\[
c=\sqrt2\,\log(1+\sqrt2)-\frac74\log2
   =0.0334429143005567\ldots,
\]
so
\[
\frac8c=239.213602262732\ldots.
\]

Thus the first dimension in which Kusner's conjecture can fail diverges as \(p\downarrow4\), and the currently available upper and lower bounds are within one logarithmic factor.

## Proof of the Hadamard-order extension

Xiong's construction uses a Walsh Hadamard matrix \(H_k\) of order \(m=2^k\) for the front coordinates and the tensor-product Walsh matrix \(H_{k+2}=H_2\otimes H_k\) for the back coordinates. The distance calculation only needs the Hadamard incidence properties, not the group structure of the Walsh matrix.

Let \(H\) be an arbitrary Hadamard matrix of order \(m\). Normalize it so that a distinguished column \(t_0\) consists entirely of \(+1\)'s. Let \(K\) be the \(4\times4\) character Hadamard matrix indexed by \(\mathbb F_2^2\), with
\[
K_{i,j}=(-1)^{i\cdot j}.
\]

Keep Xiong's four front vectors \(q_i\), \(i\in\mathbb F_2^2\), and the parameters \(R,A,B\) above. If \(h_s\) is row \(s\) of \(H\), replace Xiong's front vector by
\[
U_{i,s}=h_s\otimes q_i.
\]
For the back coordinates, replace \(H_{k+2}\) by \(K\otimes H\). In each row \((i,s)\), delete the two entries in columns \((00,t_0)\) and \((11,t_0)\), multiply the entries in columns \((10,t_0)\) and \((01,t_0)\) by \(\beta\), and multiply all remaining \(4m-4\) entries by \(\alpha\), exactly as in Xiong's construction. Take
\[
\alpha^p=\frac R4,\qquad
\beta^p=\frac{m(A-B)}{2^p}.
\]

The four distance cases in Xiong's proof are unchanged:

1. Distinct rows of \(H\) agree in exactly \(m/2\) positions and differ in exactly \(m/2\). Hence the front-coordinate calculation for equal \(i\) is unchanged.

2. Every pair of distinct rows of \(K\otimes H\), of order \(4m\), differs in exactly \(2m\) positions. If \(i=i'\), the four distinguished \(t_0\)-columns agree because \(H_{s,t_0}=H_{s',t_0}=1\); therefore all \(2m\) differences occur among the ordinary \(\alpha\)-coordinates.

3. If \(i\ne i'\), exactly two of the four distinguished \(t_0\)-columns differ, because distinct rows of \(K\) differ in two positions. Hence exactly \(2m-2\) ordinary \(\alpha\)-coordinates differ. When \(i+i'\in\{10,01\}\), exactly one of the two \(\beta\)-coordinates differs; when \(i+i'=11\), both differ. These are precisely the counts used in Xiong's Cases 3 and 4.

Thus the four \(p\)-th power distances are the same expressions as in the original proof. They all equal \(2^p mR\) once
\[
2A-B=2^{p-1}R\left(1+\frac1m\right),
\]
equivalently
\[
\Phi_p(a)=1+\frac1m.
\]

Xiong's existence argument for \(a\) does not use that \(m\) is a power of two. It shows
\[
\Phi_p(1)<1,\qquad \Phi_p(a_0(p))=1+\Delta(p)>1.
\]
If \(m>1/\Delta(p)\), then
\[
1<1+\frac1m<1+\Delta(p),
\]
so continuity supplies \(a\in(1,a_0(p))\) satisfying the required equation. This proves the theorem.

## Asymptotics at \(p=4\)

At \(p=4\), direct simplification gives
\[
\Phi_4(a)-1
=
-\frac{3(a^2-2)^2}{4(a^4+2)}.
\]
Hence \(a=\sqrt2=a_0(4)\) is the unique equality point and is stationary in the \(a\)-direction. Differentiating
\(\Delta(p)=\Phi_p(4^{1/p})-1\) at \(p=4\) therefore gives
\[
\Delta(4+\delta)=c\,\delta+O(\delta^2),
\]
with
\[
c=\sqrt2\,\log(1+\sqrt2)-\frac74\log2>0.
\]

Swanepoel and Villa proved that Hadamard orders are asymptotically dense: if \(H(x)\) is the largest Hadamard order below \(x\), then \(H(x)/x\to1\). Their proof uses Paley Hadamard matrices and the prime number theorem for arithmetic progressions. This also implies that the least available Hadamard order above \(x\) is \(x(1+o(1))\): for any fixed \(\varepsilon>0\), \(H((1+\varepsilon)x)>x\) for all sufficiently large \(x\).

Applying the theorem with \(x=1/\Delta(4+\delta)\) gives
\[
d_*(4+\delta)
\le
\frac{8/c+o(1)}{\delta}.
\]

For the lower bound, Swanepoel's Corollary 1.4 states that
\[
|p-4|<
\frac{4\log(1+2/n)}{\log(n+2)}
\quad\Longrightarrow\quad
e(\ell_p^n)=n+1.
\]
Therefore, with \(d=d_*(4+\delta)\),
\[
\delta\ge
\frac{4\log(1+2/d)}{\log(d+2)}
=
\frac{8+o(1)}{d\log d}.
\]
As \(\delta\downarrow0\), this forces \(d\to\infty\); inversion yields
\[
d_*(4+\delta)\ge
\frac{8+o(1)}{\delta\log(1/\delta)}.
\]

## Significance and limitations

The Hadamard-density mechanism itself is not new: Swanepoel and Villa used arbitrary Hadamard matrices and asymptotic density of Hadamard orders in a different equilateral-set construction for \(1\le p<2\). The contribution here is that Xiong's new \(p>4\) construction also admits arbitrary Hadamard orders, which removes the power-of-two restriction and sharpens the natural near-\(4\) dimensional upper bound by a factor of two relative to dyadic rounding.

The bounds do not determine the true order of \(d_*(4+\delta)\); a logarithmic gap remains. The originality claim is only to the best of our knowledge, and the source construction is very recent.

## References

1. Nathan Xiong, *Kusner's conjecture is false for \(p>4\)*, arXiv:2609.14794 (2026). https://arxiv.org/abs/2609.14794
2. Konrad J. Swanepoel, *Equilateral Sets and a Schütte Theorem for the 4-norm*, Canadian Mathematical Bulletin 57 (2014), 640–647. https://doi.org/10.4153/CMB-2013-031-0
3. Konrad J. Swanepoel and Rafael Villa, *Maximal Equilateral Sets*, Discrete & Computational Geometry 50 (2013), 354–373. https://doi.org/10.1007/s00454-013-9523-z
