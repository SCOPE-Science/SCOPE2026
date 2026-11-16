# Six nodes are necessary and sufficient for exact tight cubic Fock sampling

## Finding

Let \(\mathcal P_3=\{f(z)=\sum_{j=0}^3a_jz^j\}\) have the normalized Gaussian Bargmann–Fock norm
\[
\|f\|_{\mathcal F}^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}dA(z)=\sum_{j=0}^3j!|a_j|^2.
\]
An exact positive sampling rule consists of distinct complex points \(z_\nu\) and strictly positive weights \(w_\nu\) with \(\|f\|_{\mathcal F}^2=\sum_\nu w_\nu|f(z_\nu)|^2\) for *every* \(f\in\mathcal P_3\). The smallest possible number of samples is **exactly six**, with no restriction on placement or weights.

Define \(\Delta=\sqrt{17}\), \(u=(5-\Delta)/2\), \(v=(5+\Delta)/2\), \(A=(3\Delta+11)/(8\Delta)\), \(B=(3\Delta-11)/(8\Delta)\). The exact rule is
\[
\boxed{\|f\|_{\mathcal F}^2=\frac A2\bigl(|f(\sqrt u)|^2+|f(-\sqrt u)|^2\bigr)+\frac B2\bigl(|f(\sqrt v)|^2+|f(-\sqrt v)|^2\bigr)+\frac18\bigl(|f(i\sqrt2)|^2+|f(-i\sqrt2)|^2\bigr).}
\]
All six weights are strictly positive. Moreover, up to common rotation and site permutation, **this is the unique centrally symmetric six-node positive exact rule**. Arbitrary nonsymmetric six-node rules are not classified.

## Assumptions and scope

The measure is exactly \(\pi^{-1}e^{-|z|^2}dA(z)\); the monomial squared norms are \(j!\), not a differently rescaled Gaussian. Nodes are finite and pairwise distinct, weights positive and independent of the polynomial. Perfect tightness is exact Parseval equality, not a frame inequality with two unequal constants. The required cubature space consists of the sixteen bidegree monomials \(z^j\bar z^k\) for \(0\le j,k\le3\), *not* every real polynomial of total degree six.

## Proof

**1. Polarized moments.** Gaussian integration gives \(\int z^j\bar z^k\,d\gamma=j!\delta_{jk}\). By polarization, the required identity for all complex cubics is exactly equivalent to
\[
\sum_\nu w_\nu z_\nu^j\overline{z_\nu}^{\,k}=j!\delta_{jk}\quad(0\le j,k\le3).\tag{1}
\]
These sixteen equations are used for both the necessity and sufficiency.

**2. Annihilating quadratic at at most five sites.** The real vector space of real quadratics in the two planar coordinates has dimension six. At any set of \(N\le5\) sites it therefore has a nonzero member \(Q\) vanishing at every site. Write
\[
Q=a z^2+\bar a\bar z^2+b|z|^2+cz+\bar c\bar z+d,
\quad b,d\in\mathbb R,\ a,c\in\mathbb C.
\]
The four products \(Q\), \(Qz\), \(Q\bar z\), and \(Q(|z|^2-1)\) belong to the moment space of (1), and vanish on every node. Thus each has Gaussian integral zero. Using \(\int |z|^2=1\) and \(\int |z|^4=2\) gives, in order, \(b+d=0\), \(\bar c=0\), \(c=0\), and \(b=0\). Therefore \(d=0\) and \(Q=az^2+\bar a\bar z^2\), with \(a\ne0\). The zero locus of this real homogeneous harmonic quadratic consists of **two perpendicular lines through the origin**. After rotation, every node is on a real or imaginary axis.

For nonzero real-axis nodes \(x\) define \(R_k=\sum w_xx^k\), and for nonzero imaginary-axis nodes \(iy\) define \(I_k=\sum w_{iy}y^k\). The moments \((j,k)=(1,0),(2,1),(3,2)\) and their conjugates, and \((2,0),(3,1)\) and the diagonal, imply
\[
R_1=R_3=R_5=I_1=I_3=I_5=0,\quad
R_2=I_2=\tfrac12,\quad R_4=I_4=1,\quad R_6+I_6=6.\tag{2}
\]
An origin atom contributes nothing to these positive-degree moments.

**3. Three odd moments force antipodal pairs.** Consider a positive measure on a real line supported on at most three distinct nonzero sites, whose first, third and fifth moments vanish and whose second moment is positive. Group sites of each squared radius \(s>0\), and put \(D_s=\sum_{x^2=s}wx\). The odd-moment equations become \(\sum_s s^kD_s=0\) for \(k=0,1,2\). With at most three occupied radii the Vandermonde matrix is injective, hence every \(D_s=0\). Positivity forces both opposite sites \(\pm\sqrt s\) with equal weights at each radius. Because there are at most three sites there is exactly one such opposite pair; an origin site is harmless. By \(R_2=I_2=1/2\), both axes of (2) require at least two nonzero sites. Under \(N\le5\), each axis has at most three sites. Thus the preceding lemma applies to each axis. The sole squared radius on either line is \(R_4/R_2=I_4/I_2=2\), giving \(R_6=I_6=2\). This contradicts the last equation in (2), \(R_6+I_6=6\). Consequently **five or fewer positive nodes are impossible**.

**4. Exact construction.** The real-axis radial masses \(A,B>0\) at squared radii \(u,v>0\) satisfy exactly
\[
A+B=\tfrac34,\quad Au+Bv=\tfrac12,\quad Au^2+Bv^2=1,\quad Au^3+Bv^3=4.\tag{3}
\]
The imaginary-axis opposite pair has total mass \(1/4\) and squared radius \(2\), contributing \((1/4,1/2,1,2)\) to radial moments of orders zero through three. By (3), total diagonal moments are therefore \((1,1,2,6)\), exactly \(j!\) for \(j=0,1,2,3\). Antipodal pairing cancels every off-diagonal moment of odd angular frequency. The only remaining off-diagonal frequencies are \(j-k=\pm2\), represented by \(z^2\) and \(z^2|z|^2\), which cancel between the real and imaginary axes because both contribute \(1/2\) and \(1\) to second and fourth radial moments. All sixteen equations (1) hold, proving the six-node rule.

**5. Complete central-symmetry rigidity.** For a centrally symmetric six-node support write its pairs as \(\{\pm z_1,\pm z_2,\pm z_3\}\) with \(s_i=|z_i|^2>0\) and pair masses \(W_i=w_{+i}+w_{-i}>0\). The two even off-diagonal moments yield \(\sum_iW_i z_i^2=\sum_iW_i s_i z_i^2=0\). The radii must be pairwise distinct: if two coincide and the third does not, subtraction forces the third nonzero coefficient to vanish; if all coincide, the first two radial moments cannot simultaneously equal \(1\) and \(2\). Order \(s_1<s_2<s_3\). The real rank-two matrix whose rows are \((1,1,1)\) and \((s_1,s_2,s_3)\) has a one-dimensional real kernel with signs \((-,+,-)\). Therefore the three complex numbers \(W_i z_i^2\) share a complex phase up to these alternating signs. The extreme radii lie on one line, while the middle radius lies on the perpendicular line. Rotate so the outer line is real.

Even diagonal and off-diagonal equations force \(W_2s_2=1/2\) and \(W_2s_2^2=1\), so \(s_2=2\), \(W_2=1/4\). On the real line, the remaining positive two-radius measure has moments \((3/4,1/2,1,4)\) in orders zero through three. Its monic annihilating quadratic \(x^2-Sx+P\) is orthogonal to \(1,x\) for these moments; the equations uniquely solve to \(S=5,P=2\). Its roots are exactly \(u,v\), and their positive masses are uniquely \(A,B\).

It remains to prove each pair has equal individual weights, not merely equal total pair mass. Put \(\epsilon_i=w_{+i}-w_{-i}\). The three odd moments \(z|z|^{2k}\), \(k=0,1,2\), give \(\sum_i \epsilon_i z_i s_i^k=0\). Distinct radii make this Vandermonde system invertible, so every \(\epsilon_i z_i=0\), and since \(z_i\ne0\), each \(\epsilon_i=0\). This proves the entire asserted rigidity classification.

## Verification

Run `python CHECK.py` in the same directory with Python 3 and SymPy (see `requirements.txt`). Exact symbolic arithmetic checks each of the 16 complex moments and 16 normalized monomial Gram entries, plus 12 radial auxiliary identities. It prints `EXACT_FOCK_CUBIC_SIX_NODE_CHECKS_PASS 44`. The finite symbolic checker verifies the construction; no-five-node minimality and central-symmetry uniqueness are the universal analytic arguments above, not finite enumeration.

## Relationship to prior work

Bownik–Yu [1] concerns nearly tight discretization of general continuous frames and does not determine finite-degree exact minimal point counts. Gröchenig–Ortega-Cerdà [2] establishes finite Fock sampling and degree-uniform Marcinkiewicz–Zygmund theory, not this fixed-degree positive Parseval minimum. The closest published quadratic Fock result [3] proves four nodes are necessary and sufficient for \(\mathcal P_2\) and explicitly does not address cubics. A separate all-degree circular Fock theorem [4] restricts all sites to one common radius, whereas the present six-node exact sampler has three different positive radii. An–Ge [5] studies cubature on a conic surface, not Gaussian plane bidegree-(3,3) moments.

The existence of Gaussian orthogonal moments and one-dimensional two-node quadrature are classical tools, not discoveries here. The asserted claim is the **global six-node minimum plus an explicit design and central-symmetric rigidity**. It may coincide with an older complex Gaussian cubature table or another formulation not accessible in full; independent priority is not certified.

## Limitations

One complex variable, degree at most three, normalized Gaussian Fock norm, positive weights and exact point evaluations only. Unrestricted uniqueness among all six-node designs, other degrees, infinite-dimensional Fock sampling, and independent mathematical certification are not asserted. The classical cubature-priority caveat is substantial.

## References

[1] M. Bownik and P.-T. Yu, *Uniform discretization of continuous frames*, arXiv:2603.10423v1 (first posted 2026-03-11), https://arxiv.org/html/2603.10423v1.

[2] K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz-Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825v1 (2021-09-24), https://arxiv.org/html/2109.11825v1.

[3] *Four nodes are necessary and sufficient for exact tight sampling of quadratic Fock polynomials*, public mathematical record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-nodes-are-necessary-and-sufficient-for-exact-tight-sampling--df9aaaf372ae.

[4] *Sharp one-circle sampling barrier and design rigidity for truncated Bargmann–Fock spaces*, public mathematical record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-one-circle-sampling-barrier-and-design-rigidity-for-trunca--69240c62b4d5.

[5] C. An and Y. Ge, *Positive Cubature Compression and Optimal Hyperinterpolation Stability on a Conic Surface*, arXiv:2609.36430v1 (2026-09-29), https://arxiv.org/abs/2609.36430.
