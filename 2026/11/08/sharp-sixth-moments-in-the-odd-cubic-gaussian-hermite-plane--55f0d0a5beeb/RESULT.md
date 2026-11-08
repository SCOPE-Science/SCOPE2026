# Sharp sixth moments in the odd cubic Gaussian Hermite plane

## Finding
Let \(Z\) be standard real Gaussian and let \(\gamma\) denote its law. The entire real two-dimensional space of odd polynomials of degree at most three, regarded as a subspace of \(L^6(\gamma)\), is
\[
\mathcal H_{1,3}=\{aH_1+bH_3:a,b\in\mathbb R\},\quad H_1(z)=z,\quad H_3(z)=z^3-3z.
\]
For nonzero \(f\in\mathcal H_{1,3}\) write \(K(f)=\|f\|_6^6/\|f\|_2^6\), with both norms taken against \(\gamma\). Define
\[
N(t)=15\bigl(1+24t+450t^2+5760t^3+51300t^4+287712t^5+773928t^6\bigr),
\]
\[
P(t)=71928t^6-167832t^5-55620t^4-8100t^3-690t^2-36t-1.
\]
The polynomial \(P\) has exactly two real roots, one \(t_-\in(-0.102,-0.101)\), the other \(t_+\in(2.642,2.643)\). The exact sharp inequalities are
\[
\boxed{\frac{N(t_-)}{(1+6t_-^2)^3}\leq K(f)\leq \frac{N(t_+)}{(1+6t_+^2)^3}}.
\]
The endpoint values are respectively \(4.616867376932281790\ldots\) and \(57613.876096582919347\ldots\), and the corresponding sharp \(L^6/L^2\) norm ratios are their sixth roots. Lower equality holds exactly for nonzero real scalar multiples of \(H_1+t_-H_3\), and upper equality holds exactly for nonzero real scalar multiples of \(H_1+t_+H_3\). All intermediate moment ratios occur. In particular, neither optimizer is a pure Hermite chaos: mixing suppresses the sixth moment below the pure Gaussian value \(15\), whereas the maximizing mixture exceeds the pure cubic value \(53745\).

## Assumptions and scope
The coefficients are real; the Gaussian has mean zero and variance one; the function space contains *all* real odd polynomials of degree at most three and no higher-degree terms. The result is an exact two-dimensional norm statement, not an assertion about arbitrary third-degree polynomials in several Gaussian coordinates, general Wiener-chaos sums, or other moments. Since \(H_1\) and \(H_3\) are orthogonal in \(L^2(\gamma)\), for every \(a,b\in\mathbb R\),
\[
\|aH_1+bH_3\|_2^2=a^2+6b^2.
\]
For \(a\ne0\), the projective parameter is \(t=b/a\). For \(a=0\), use the limiting point \(t=\infty\) in the real projective line; its moment ratio is \(53745\). The pure linear point \(b=0\) has ratio \(15\).

## Proof
**Exact Gaussian integration.** For every nonnegative integer \(j\), \(\mathbb E Z^{2j}=(2j-1)!!\) and \(\mathbb E Z^{2j+1}=0\), with \((-1)!!=1\). Expanding \((Z+t(Z^3-3Z))^6\) by the binomial theorem yields
\[
\mathbb E[\bigl(Z+tH_3(Z)\bigr)^6]=N(t),\qquad
\mathbb E[\bigl(Z+tH_3(Z)\bigr)^2]=1+6t^2.
\]
Hence the exact moment ratio is \(K(t)=N(t)/(1+6t^2)^3\). Direct differentiation gives the polynomial identity
\[
\boxed{K'(t)=-\frac{360P(t)}{(1+6t^2)^4}}.
\]

**Exhaustive real-root certificate.** The descending coefficient sequence of \(P\) has one sign change. Descartes' rule and the signs \(P(0)<0\), \(P(t)>0\) for sufficiently large positive \(t\), prove that \(P\) has exactly one positive root, counted with multiplicity. To deal with negative roots, set \(Q(u)=P(-u)\). Its coefficients are not themselves a one-change sequence. For \(u\ge1/8\), write \(u=1/8+v\) and observe the exact identity
\[
8^6Q(1/8+v)=8(2356936704v^6+7267221504v^5+2167050240v^4+305510400v^3+22102080v^2+874896v+11671),
\]
which is strictly positive for \(v\ge0\). For \(0<u<1/8\), substitute \(u=w/[8(1+w)]\), \(w>0\). The exact identity is
\[
8^6(1+w)^6Q\bigl(w/[8(1+w)]\bigr)=8(11671w^6-39336w^5-26400w^4-75520w^3-107520w^2-49152w-32768).
\]
The descending coefficient sequence on the right has exactly one sign change; the expression is negative at \(w=0\) and positive for large positive \(w\). Descartes' rule proves that it has exactly one positive real root, also counted with multiplicity. Thus \(P\) has exactly one negative root. Substituting the rational endpoints \(-102/1000,-101/1000,2642/1000,2643/1000\) in \(P\) gives the indicated disjoint isolating intervals.

**Global extrema and equality.** The two critical roots are simple by the sign-change argument. Since \(P\) has positive leading coefficient and \(P(0)=-1\), \(K'(t)<0\) before \(t_-\), \(K'(t)>0\) between the two roots, and \(K'(t)<0\) after \(t_+\). Also \(\lim_{t\to\pm\infty}K(t)=53745\). Therefore the unique finite global minimum is \(K(t_-)\) and the unique finite global maximum is \(K(t_+)\); the projective point at infinity cannot be extremal. For any nonzero \((a,b)\), scale invariance reduces the ratio to one of these projective values. The exact equality descriptions and the fact that all intermediate values occur follow by continuity of \(K\) and its strict monotonicity between the roots.

## Verification
Run \(\texttt{python3 verify.py}\) from a directory containing the standalone checker provided with this result. Its exact integer-and-rational computations independently expand the Gaussian sixth moment, check Hermite orthogonality and the derivative identity, verify both Descartes-transform coefficient identities, and isolate the two roots by rational bisection. It checks the normalized endpoint expressions and the values at the pure-Hermite cases. Its printed decimal values are diagnostic presentations of rational brackets: finite numeric checks are not used to infer absence of additional roots. That universal step follows from the two exact sign-change identities above.

## Relationship to prior work
Nourdin, Peccati and Reinert (arXiv:0904.1153, first submitted 2009-04-07), Section 2, define Gaussian chaos and give the general hypercontractive estimate for finite sums (Proposition 2.6). Bakry, Bolley and Gentil (arXiv:1003.5072, first submitted 2010-03-26) treat dimension-dependent Ornstein–Uhlenbeck hypercontractivity. These source results are broad norm controls, not the exact two-sided sixth-moment optimization or equality classification in \(\mathcal H_{1,3}\). The moment formula itself follows from classical Gaussian moments; novelty is claimed only for the sharp two-sided coefficient optimization and mixed-chaos extremizer classification, subject to the bibliographic risk noted below.

## Limitations
The conclusion is not dimension-free hypercontractivity for arbitrary cubic polynomial functions and does not determine the optimal norm comparison for the full polynomial space of degree at most three without the odd restriction. The constants are algebraic rather than elementary radicals. No claim is made about global novelty beyond the inspected prior sources and indexed mathematical findings; a not-yet-indexed equivalent result remains possible. Independent mathematical audit has not been performed.

## References
1. I. Nourdin, G. Peccati and G. Reinert, *Invariance principles for homogeneous sums: Universality of Gaussian Wiener chaos*, arXiv:0904.1153, first public version 2009-04-07; https://arxiv.org/html/0904.1153v2 and https://arxiv.org/abs/0904.1153 .
2. D. Bakry, F. Bolley and I. Gentil, *Dimension dependent hypercontractivity for Gaussian kernels*, arXiv:1003.5072, first public version 2010-03-26; https://arxiv.org/abs/1003.5072 .
3. NIST Digital Library of Mathematical Functions, Chapter 18, classical orthogonal-polynomial definitions, https://dlmf.nist.gov/18.3 .
