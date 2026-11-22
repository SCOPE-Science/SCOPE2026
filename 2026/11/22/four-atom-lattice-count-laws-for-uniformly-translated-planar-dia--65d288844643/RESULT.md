# Four-atom lattice-count laws for uniformly translated planar diamonds

## Finding
For a unit-area random shift of the integer lattice and a fixed-orientation planar taxicab ball, the *complete finite-radius count distribution* has at most four atoms. The probabilities and support depend explicitly only on an integer radius component and its fractional phase, and the large-radius centered law is a two-Bernoulli sum, rather than a Gaussian.

Let \(n\ge1\) be an integer, \(0\le s<1\), \(R=n+s\), and \(U_1,U_2\) be independent uniform variables on \([0,1)\). Set
\[
N_R=\#\{(j,k)\in\mathbb Z^2:|j-U_1|+|k-U_2|\le R\}.
\]
For \(0\le s\le1/2\), the complete mass function is

| Value of \(N_R\) | Probability |
|---|---|
| \(2n^2\) | \((1-2s)^2\) |
| \(2n^2+n\) | \(4s(1-2s)\) |
| \(2n^2+2n\) | \(2s^2\) |
| \(2n^2+2n+1\) | \(2s^2\) |

For \(1/2\le s<1\), put \(t=1-s\). The complete mass function is

| Value of \(N_R\) | Probability |
|---|---|
| \(2n^2+2n\) | \(2t^2\) |
| \(2n^2+2n+1\) | \(2t^2\) |
| \(2n^2+3n+1\) | \(4t(1-2t)\) |
| \(2n^2+4n+2\) | \((1-2t)^2\) |

Zero-probability entries may be omitted. Both formulas agree at \(s=1/2\). The mean is exactly \(\mathbb EN_R=2R^2\). For any fixed \(s\in[0,1)\), let \(\delta=\{2s\}\), and let \(B_1,B_2\) be independent Bernoulli\((\delta)\). Then
\[
\frac{N_{n+s}-2(n+s)^2}{n+s}\ \Longrightarrow\ B_1+B_2-2\delta
\qquad(n\to\infty).
\]
The limiting variance is \(2\delta(1-\delta)\). It vanishes at integral and half-integral radii even though, at half-integral radii, the unscaled count retains a fair two-atom fluctuation.

## Assumptions and scope
The centre is uniform modulo \(\mathbb Z^2\). The diamond's sides remain at slopes \(\pm1\), with no random orientation. The integer \(n\) is at least one; all stated probability assertions are insensitive to choices of inclusion or exclusion on the boundary because the random centre hits boundary coincidences with probability zero. No assertion is made for other slopes, general convex bodies or random rotations.

## Proof
The elementary identity \(|x|+|y|=\max\{|x+y|,|x-y|\}\) sends the diamond to the square
\[
|p-a|\le R,\quad |q-b|\le R,
\quad p=j+k,\ q=j-k,\ a=U_1+U_2,\ b=U_1-U_2.
\]
The image of \(\mathbb Z^2\) is exactly the parity sublattice \(\{(p,q)\in\mathbb Z^2:p\equiv q\pmod2\}\). Thus \(N_R\) counts pairs of integers in two length-\(2R\) intervals with matching parity.

First let \(0\le s<1/2\). Each interval contains \(2n\) integers generically, exactly \(n\) of each parity, except when its centre is within distance \(s\) of an integer, when it contains one additional integer of one parity. The fractional parts of \(a\) and \(b\) are independent and uniform: the map \((u,v)\mapsto(u+v,u-v)\) is a surjective torus homomorphism with determinant \(-2\) and therefore pushes normalized Haar measure to normalized Haar measure. Hence the two extra-integer events are independent, each with probability \(2s\).

If neither interval has an extra, there are \(2n^2\) matching-parity pairs. If only one has an extra, there are \(2n^2+n\). If both have extras, matching parities produce \(2n^2+2n+1\) and opposite parities produce \(2n^2+2n\). Their joint probabilities are each \(2s^2\), as follows. Write \(a\) and \(b\) within \(s\) of nearby integers \(k\) and \(l\). Their nearest integer parities agree precisely when \(k\equiv l\pmod2\). In original centre coordinates, this describes the image modulo \(\mathbb Z^2\) of one \(\ell^1\) diamond \(\{|u-u_0|+|v-v_0|<s\}\) centered at an integer pair \((u_0,v_0)\). Its total area on the unit torus is \(2s^2\). Opposite parities similarly give a diamond centered at \((1/2,1/2)\), also of area \(2s^2\). Thus the first table follows, including \(s=0\) by continuity.

Now let \(1/2<s<1\) and \(t=1-s\). Each interval generically contains \(2n+2\) integers, \(n+1\) of each parity, except when its centre is within distance \(t\) of an integer: then it has \(2n+1\), with one parity count \(n\). Each deficient event occurs with probability \(2t\), independently. With no deficiencies the count is \(2(n+1)^2=2n^2+4n+2\). With one it is \(2n^2+3n+1\). With two the answer is \(2n^2+2n\) or \(2n^2+2n+1\), according to the parity alignment of their missing integers. The same two torus diamonds of area \(2t^2\) give the two equal probabilities. This proves the second table. At \(s=1/2\) the expressions coincide by direct substitution.

The mean follows either by multiplying the four atom probabilities and values, or by tiling the plane and applying Fubini: \(\mathbb E N_R=\operatorname{area}(\{|x|+|y|\le R\})=2R^2\).

For the limit, each one-dimensional interval has \(2n+\lfloor2s\rfloor+H\) points with \(H\sim\operatorname{Bernoulli}(\delta)\), \(\delta=\{2s\}\). The two extra indicators \(H_1,H_2\) are independent by the torus argument. The matching-parity count equals
\[
N_R=2n^2+n\big(2\lfloor2s\rfloor+H_1+H_2\big)+C_{n,s},
\]
where \(0\le C_{n,s}\le2\), as parity counts differ by at most one. After subtracting \(2(n+s)^2\) and dividing by \(n+s\), the result differs uniformly by \(O(1/n)\) from \(H_1+H_2-2\delta\). Since their common law is already binomial, convergence in distribution, in all bounded moments and of the variance follows. The special cases \(s=0\) and \(s=1/2\) have \(\delta=0\), and the finite tables give their residual fluctuations exactly.

## Verification
The bundled `checker.py` checks the probability totals and exact mean and variance identities using rational arithmetic over multiple integer radii and fractional phases; it also independently enumerates lattice points at deterministic rational centre grids and compares the observed frequencies with the exact mass function. The proof above is analytic and does not use finite numerical enumeration for an infinite assertion.

## Relationship to prior work
Schlie's 2026 survey motivates finite and asymptotic distribution questions for randomized lattice counts, but does not give this particular fixed-orientation diamond four-atom law. Rosen (1989) already computed the *variance* for general rationally inclined rectangles, which includes a square rotated by \(45^\circ\), so **no claim of novelty for the variance** is made. Holgate (1990) gives a general fixed-angle parallelogram variance formula and discusses conditional line counts; the two-page text does not state this four-atom distribution. The 1965 de Bruijn solution to Weissblum's random-rectangle problem concerns a very thin rectangle with *uniformly random orientation*, rather than this fixed-angle expanding diamond. The claimed contribution is the explicit *complete finite probability law* and the resulting phase-dependent two-Bernoulli fluctuation spectrum, not variance bounds or generic equidistribution.

## Limitations
This is a special rational-angle model whose parity structure permits an exact four-atom classification; it does not generalize automatically to a smooth body or to random angles. Earlier lattice-digitalization literature not located in the comparison could contain an equivalent probability table. The normed limit is degenerate at integer and half-integer radius phases, and no universal continuous limit over all phases is asserted. Independent external mathematical validation has not been performed.

## References
- S. Schlie, *On the randomized lattice-point count problem*, arXiv:2611.16769v1 (first submitted 2026-11-12), https://arxiv.org/abs/2611.16769.
- D. Rosen, *Coverage of a square lattice by an inclined rectangle*, *Advances in Applied Probability* **21** (1989), 705–707, https://doi.org/10.2307/1427644.
- P. Holgate, *Lattice points in a random parallelogram*, *Advances in Applied Probability* **22** (1990), 484–485, https://doi.org/10.2307/1427547.
- N. G. de Bruijn, *Solution to Problem 63-6: Asymptotic Distribution of Lattice Points in a Random Rectangle*, *SIAM Review* **7** (1965), 274–276, https://doi.org/10.1137/1007043.
