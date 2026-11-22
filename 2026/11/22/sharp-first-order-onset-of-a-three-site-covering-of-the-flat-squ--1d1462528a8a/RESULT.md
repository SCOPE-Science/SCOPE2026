# Sharp first-order onset of a three-site covering of the flat square torus at \(p=1\)

## Finding

On the product of two geodesic circles of circumference one, place three sites \(C=\{(j/3,j/3):j=0,1,2\}\). Let \(R(p)\) denote the least radius of three equal balls *with precisely these centers* in the product metric \(d_p\). Then \(R(1)=1/2\), whereas \(R(p)<1/2\) for every finite \(p>1\). Moreover,

\[ R(1+\varepsilon)=\frac12-\left(\frac{\log12}{4}-\frac{5\log5}{24}\right)\varepsilon+o(\varepsilon),\qquad\varepsilon\downarrow0.\]

The constant is sharp for the prescribed site set. In particular the covering-product inequality can fail for **connected smooth circle factors** at some finite radius, for every \(p>1\). This is a constructive, fixed-site assertion and does not claim a global three-center minimizer.

## Assumptions and scope

Write \(S=\mathbb R/\mathbb Z\), \(\delta(a,b)=\min_{n\in\mathbb Z}|a-b-n|\), and for finite \(p\ge1\), \(d_p((x,y),(u,v))=(\delta(x,u)^p+\delta(y,v)^p)^{1/p}\). Covering balls are closed. The circle's exact covering number at any \(1/4\le r<1/2\) is two; for \(r<1/4\) it can exceed two. The assertion concerns \(R(p)=\max_{(x,y)\in S^2}\min_{j\in\{0,1,2\}}d_p((x,y),(j/3,j/3))\) for fixed sites, not the infimum over arbitrary three sites.

## Proof

**(1) The critical locus for \(p=1\).** Let \(s=\delta(x,y)\in[0,1/2]\) be the length of a shorter arc joining \(x\) and \(y\). Three site coordinates divide the circle into gaps of length \(1/3\). If \(s\ge1/3\), that shorter arc includes some site coordinate \(j/3\), and the sum of distances from \(x,y\) to that coordinate equals \(s\). If \(s<1/3\), the shorter arc either contains a site, or sits in a gap of length \(1/3\); in the latter case some endpoint of that gap is at distance at most \((1/3-s)/2\) from the shorter arc, giving a two-coordinate sum at most \(s+2(1/3-s)/2=1/3\). Thus the fixed-site \(d_1\) covering functional is strictly smaller than \(1/2\) whenever \(s<1/2\). If \(s=1/2\), the two points are antipodal and **for every circle coordinate \(t\)**, \(\delta(x,t)+\delta(y,t)=1/2\). Thus \(R(1)=1/2\), with equality exactly on \(y=x+1/2\pmod1\).

**(2) Strict onset.** At every point away from the antipodal locus, \(d_p\le d_1<1/2\). At an antipodal point, some site has both coordinate distances strictly between zero and \(1/2\). For that site strict \(\ell_p<\ell_1\) yields distance strictly less than \(1/2\), for each \(p>1\). Compactness now implies \(R(p)<1/2\). Since \(R(p)\to1/2\) as \(p\downarrow1\), choose any \(r\) with \(\max(R(p),1/4)\le r<1/2\). Three product balls suffice while each factor circle has covering number exactly two.

**(3) Uniform first variation.** Define for \(0\le a\le1/2\)
\[ H(a)=\tfrac12\log(1/2)-a\log a-(\tfrac12-a)\log(\tfrac12-a),\]
with \(0\log0=0\). For \(a+b=1/2\), the two-coordinate norm has the uniform expansion
\[ (a^{1+\varepsilon}+b^{1+\varepsilon})^{1/(1+\varepsilon)}=1/2-\varepsilon H(a)+o(\varepsilon).\]
Uniformity holds also at \(a=0\) because \(t\mapsto t(\log t)^k\) extends continuously by zero at \(t=0\) for each fixed positive integer \(k\). The general expansion around a perturbed pair with sum \(1/2+O(\varepsilon)\) is \(a+b-\varepsilon H(a_0)+o(\varepsilon)\), where \(a_0\) is the limiting first coordinate distance on the antipodal locus.

**(4) Reduction to a one-variable competition.** Any maximizer for \(R(1+\varepsilon)\) lies within \(O(\varepsilon)\) of the antipodal locus: indeed \(d_{1+\varepsilon}\le d_1\le1/2-|s-1/2|\) when \(s\ge1/3\), while evaluating a fixed antipodal point gives \(R(1+\varepsilon)\ge1/2-O(\varepsilon)\). By diagonal translation by a site, coordinate exchange and simultaneous reflection, write a subsequential limiting antipodal pair as \((x,x+1/2)\) with \(0\le x\le1/6\), and its nearby second coordinate as \(y=x+1/2+\varepsilon t\), with bounded \(t\).

For interior \(0<x<1/6\), the three relevant \(d_1\) sums are \(1/2-\varepsilon t\) at sites zero and \(2/3\), and \(1/2+\varepsilon t\) at site \(1/3\). Their first-variation entropies are respectively \(H(x)\), \(H(1/6-x)\), and \(H(1/3-x)\). Thus the maximum possible limiting first-order coefficient of the covering functional at fixed \(x\) is
\[ \sup_{t\in\mathbb R}\min\{-t-H(x),-t-H(1/6-x),t-H(1/3-x)\}\]
\[ =-\frac{H(1/3-x)+\max\{H(x),H(1/6-x)\}}2.\]
The same bound extends to endpoint values \(x=0,1/6\) by choosing the two sites on the stable opposite branches and taking limits, so site-distance kinks cannot create a larger first-order radius.

**(5) Sharp optimization.** The function \(H\) is symmetric about \(1/4\), strictly concave, and increases on \([0,1/4]\). Hence on \(0\le x\le1/12\), the preceding positive coefficient is \((H(1/6-x)+H(1/6+x))/2\), which is strictly decreasing; for \(1/12\le x\le1/6\), it is \((H(x)+H(1/3-x))/2\), strictly increasing. Its unique minimum occurs at \(x=1/12\). The sharp value is
\[ \kappa=\frac{H(1/12)+H(1/4)}2=\frac14\log12-\frac5{24}\log5.\]
For attainability to first order set \(x=1/12\) and \(y=7/12+\varepsilon(H(1/4)-H(1/12))/2\). Here all three sites have the same norm to first order, namely \(1/2-\kappa\varepsilon+o(\varepsilon)\), giving the matching lower bound. Together with the upper bound this proves the stated limit.

## Verification

A standalone Python script `verify.py` reproduces the entropy identity, the optimizing scalar function at rational grid samples, the exact logarithmic expression, and numerical two-dimensional global optimizations for a sequence of exponents approaching one. Finite computations are corroboration; the proof of global \(d_1\) criticality, all \(p>1\) strictness and the limiting derivative is analytic and independent of finite sampling.

## Relationship to prior work

Cieliebak and Cieliebak, *Covering numbers of metric spaces* (arXiv:2611.15599v1, 11 November 2026), Example 3.4, establish a three-versus-four covering-number failure in a **finite four-point circle** for \(p>1\); their main conjecture is for \(p=1\). The present result instead quantifies the sharp onset of the *continuous canonical three-site covering* of two entire geodesic circles. Joós, *On covering the square flat torus by congruent discs* (2019), proves the unrestricted Euclidean three-disk radius \(5\sqrt2/18\) at \(p=2\), not the limiting \(p\downarrow1\) entropy coefficient. Pre-existing Manhattan-torus covering phases include the \(p=1\) no-three-ball threshold; that endpoint is not claimed as novel.

## Limitations

Only the canonical three cyclic sites are optimized over the torus points; global optimality over arbitrary triples at \(p\ne2\) is unproved. The coefficient describes first order as \(p\downarrow1\), not an exact formula for every finite \(p>1\). Nothing here contradicts the \(p=1\) product-covering conjecture or its small-radius Finsler results. Independent audit has not been carried out.

## References

1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, 2026-11-11, https://arxiv.org/html/2611.15599v1.
2. A. Joós, *On covering the square flat torus by congruent discs*, Australasian Journal of Combinatorics 75 (2019), 113–126, https://ajc.maths.uq.edu.au/pdf/75/ajc_v75_p113.pdf.
3. R. J. McEliece and H. C. Taylor, *Covering tori with squares*, J. Combin. Theory Ser. A 14 (1973), 119–124 (historical \(\ell_\infty\) torus-covering background).
