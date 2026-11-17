# Sharp mesh-ratio control of two-input variation for nonuniform Steffen cubic Hermite interpolation

## Finding

The Steffen shape-preserving cubic interpolant can be variation preserving for each signal yet amplify variation in the difference of two signals. On every fixed nonuniform bi-infinite grid its **sharp two-input variation coefficient** is
\[
\operatorname{Lip}_{\rm TV}(\mathcal H)=1+\frac{16}{27}\sup_{i\in\mathbb Z}\frac{h_{i-1}+h_{i+1}}{h_i}\in[1,+\infty].
\]
For each index the corresponding ratio is achieved by two finite-variation data sequences which differ in only one secant slope. Thus finite two-input variation stability is equivalent to a uniform bound on adjacent mesh ratios. For equal mesh lengths the exact coefficient is \(59/27\); for three consecutive lengths \((2,1,3)\), the local sharp factor is \(107/27\).

## Assumptions and scope

Let \((x_i)_{i\in\mathbb Z}\) be strictly increasing, with \(x_i\to-\infty\) as \(i\to-\infty\), \(x_i\to+\infty\) as \(i\to+\infty\), and finite positive cell lengths \(h_i=x_{i+1}-x_i\). For real nodal data \(y=(y_i)_{i\in\mathbb Z}\), let \(s_i=(y_{i+1}-y_i)/h_i\) and \(V_d(y)=\sum_{i\in\mathbb Z} h_i|s_i|<\infty\).

At the knot \(x_i\), define the real Steffen derivative by \(m_i=0\) when \(s_{i-1}s_i\le0\) and otherwise
\[
m_i=\operatorname{sgn}(s_i)\min\!\left(2|s_{i-1}|,2|s_i|,\frac{h_i|s_{i-1}|+h_{i-1}|s_i|}{h_{i-1}+h_i}\right).
\]
On each cell \([x_i,x_{i+1}]\), let \(\mathcal Hy\) be the standard cubic Hermite interpolant with nodal values \(y_i,y_{i+1}\) and derivatives \(m_i,m_{i+1}\). Define \(V_c(f)=\int_{\mathbb R}|f'(x)|\,dx\) for the resulting locally \(C^1\) function, and use the extended-real two-input coefficient \(\sup_{V_d(y-z)>0}V_c(\mathcal Hy-\mathcal Hz)/V_d(y-z)\), taking all real finite-variation sequences \(y,z\). No restriction on the relative sizes of successive \(h_i\) is imposed.

## Proof

**Step 1: the Hermite derivative and its positive cone.** With \(t=(x-x_i)/h_i\), the derivative with respect to \(x\) is
\[
(\mathcal Hy)'(x)=s_i A(t)+m_i B(t)+m_{i+1}C(t),
\quad A=6t(1-t),\ B=3t^2-4t+1,\ C=3t^2-2t.
\]
Direct polynomial integration gives \(\int_0^1 A=1\), \(\int_0^1 B=\int_0^1 C=0\), and \(\int_0^1|B|=\int_0^1|C|=8/27\). If \(a,b\in[0,2]\), the polynomial \(A+aB+bC\) is nonnegative on \([0,1]\): it depends affinely on \((a,b)\), and its four vertices are \(A\), \(2(1-t)\), \(2t\), and \(2-6t+6t^2\ge1/2\). Consequently
\[
\int_0^1|A+aB+bC|\,dt=1\qquad(0\le a,b\le2).
\]
The Steffen limiter has the same sign as each nonzero neighboring secant and obeys \(0\le m_i/s_i\le2\) and \(0\le m_{i+1}/s_i\le2\) when \(s_i\ne0\); when \(s_i=0\) both corresponding derivatives vanish. Therefore the cubic is monotone on every cell, with variation exactly \(h_i|s_i|\). Summing proves \(V_c(\mathcal Hy)=V_d(y)\).

**Step 2: a bound on the variation of any one secant.** Holding all other secants fixed, the Steffen derivative is a continuous piecewise affine function of its two secant arguments. Both partial derivatives exist almost everywhere and belong to \([0,2]\). This follows directly because on a quadrant with same-signed arguments the formula is the minimum of three linear maps (or the maximum of their negative counterparts), with nonnegative partial coefficients bounded by two; the other quadrants have derivative zero and the maps fit continuously along their boundaries.

Changing only \(s_i\) thus differentiates the three affected cell interpolants. Let \(a=\partial m_i/\partial s_i\) and \(b=\partial m_{i+1}/\partial s_i\), both in \([0,2]\). The derivative response on the center cell is \(A+aB+bC\), on the left cell it is \(aC\), and on the right cell it is \(bB\). Hence its *integrated absolute response per unit change in the slope* is exactly
\[
h_i\int_0^1|A+aB+bC|+h_{i-1}a\int_0^1|C|+h_{i+1}b\int_0^1|B|
=h_i+\frac8{27}(h_{i-1}a+h_{i+1}b)
\le h_i+\frac{16}{27}(h_{i-1}+h_{i+1}).
\]
For finitely many changed secants, follow the straight segment joining the two secant vectors, use the almost-everywhere directional derivative, the triangle inequality, and integrate along that segment. Summing the preceding column bounds gives
\[
V_c(\mathcal Hy-\mathcal Hz)\le\sum_i\left[h_i+\frac{16}{27}(h_{i-1}+h_{i+1})\right]|s_i(y)-s_i(z)|
\le K(h)V_d(y-z).
\]
When \(K(h)<\infty\), extend from finite secant changes to all \(V_d\)-summable changes by truncation and the same bound (the local Hermite formula converges on each fixed cell, and Fatou's lemma bounds the global variation). When \(K(h)=\infty\), the finite-column inequality remains valid but gives no finite global uniform bound.

**Step 3: exact sharpness.** Fix any index \(i\). Choose strictly positive neighboring secants \(s_{i-1},s_{i+1}\) sufficiently large compared with \(s_i>0\), with every other secant zero; the resulting nodal data have finite discrete variation. Both neighboring Steffen rules then select precisely \(m_i=m_{i+1}=2s_i\). Perturb only \(s_i\) by a sufficiently small positive amount to remain strictly within these two active linear branches. For this data pair the difference of interpolants has one-center-cell derivative equal to \(\delta s_i(A+2B+2C)\), and derivatives on the adjacent cells \(2\delta s_i C\) and \(2\delta s_i B\). Its total variation is therefore exactly
\[
|\delta s_i|\left(h_i+\frac{16}{27}(h_{i-1}+h_{i+1})\right).
\]
The input-difference variation is \(h_i|\delta s_i|\). Hence the sharp coefficient is at least the displayed local ratio, for every \(i\). Take the supremum over all indices and combine with Step 2 to prove equality, including an infinite supremum. The finiteness criterion follows because \((h_{i-1}+h_{i+1})/h_i\) is bounded precisely when both neighboring-to-center length ratios are uniformly bounded. A supremum over indices need not be attained by a single index.

## Verification

The accompanying standalone `steffen_nonuniform_verify.py` uses exact fractions for the polynomial integral identities and the local three-cell witness, yielding the exact ratio \(107/27\) for consecutive lengths \((2,1,3)\). It also runs 2,500 seeded finite-cell numerical stress tests on irregular grids for one-input variation preservation and two-input variation bounds. To replay, run `python3 steffen_nonuniform_verify.py` with Python's standard library. Finite checks support but do not replace the infinite-grid proof above.

## Relationship to prior work

Steffen (1990) introduced the monotonicity-preserving local cubic Hermite slope rule. Higham (1992) studied a related monotonic interpolation problem, including the possibility of adding knots; it is a different algorithm. Nochetto and Salgado (arXiv:1211.1069) construct a variation-diminishing \(Q_1\) averaging operator on Cartesian meshes, rather than a sharp *two-input* variation norm for Steffen cubic interpolation. Aràndiga, Baeza and Yáñez (arXiv:2102.11564) analyze nonuniform monotone cubic interpolation and order properties. The present assertion concerns a different stability observable, the sharp dependence on **ratios of successive cell lengths**, and the necessity as well as sufficiency of mesh shape regularity. Prior exact results for *uniform-grid* harmonic-mean and conservative minmod Hermite rules do not give the nonuniform Steffen formula: the slope selectors and quantifiers over meshes differ.

## Limitations

The result assumes fixed, bi-infinite strictly increasing knots, real data, no finite boundary conditions, and the specific Steffen rule. It gives no stability estimate when the knot positions vary between inputs. The unbounded-ratio case says that no *uniform* two-input total-variation coefficient exists over all finite-variation data on that fixed grid; it does not mean any particular interpolated signal has infinite variation. Published historical priority is not established conclusively: the original 1990 Steffen article and an adjacent 2013 nonuniform monotone-Hermite paper could not be inspected in full text. The archival source date is the day-verified May 8, 1992 publication date of Higham's related paper, not a claim about the exact day the earlier Steffen article first circulated.

## References

- M. Steffen, “A simple method for monotonic interpolation in one dimension,” *Astronomy & Astrophysics* **239** (1990), 443–450, ADS bibcode `1990A&A...239..443S` (original full text not inspected).
- D. J. Higham, “Monotonic piecewise cubic interpolation, with applications to ODE plotting,” *J. Comput. Appl. Math.* **39** (1992), 287–294, https://doi.org/10.1016/0377-0427(92)90205-C ; publication date May 8, 1992 verified via https://strathprints.strath.ac.uk/203/ .
- R. H. Nochetto and A. J. Salgado, “A Total Variation Diminishing Interpolation Operator and Applications,” arXiv:1211.1069, https://arxiv.org/abs/1211.1069 (2012).
- A. Aràndiga, A. Baeza and F. Yáñez, “Monotone cubic spline interpolation for functions with a strong gradient,” arXiv:2102.11564, https://arxiv.org/abs/2102.11564 (2021).
- A. Aràndiga, “On the Order of Nonuniform Monotone Cubic Hermite Interpolants,” *SIAM J. Numer. Anal.* (2013), https://doi.org/10.1137/12088495X (full text not inspected).
- JuliaMath, `Interpolations.jl`, Steffen knot derivative implementation: https://github.com/JuliaMath/Interpolations.jl/blob/master/src/monotonic/monotonic.jl .
