# Reentrant Radau IIA positivity windows on \(K_{2,q}\)

## Finding

For the unit-conductance complete bipartite graph \(K_{2,q}\) with an integer \(q\ge2\), let \(L_q\) be the combinatorial Laplacian and apply the completed two-stage, third-order Radau IIA method to the heat equation \(u'=-L_qu\). The endpoint matrix is
\[
T_q(h)=(6I-2hL_q)(h^2L_q^2+4hL_q+6I)^{-1},\quad h\ge0.
\]
Write the quartics
\[
\begin{aligned}
A_q(h)={}&q^2(q+2)^2h^4+(-2q^4+12q^2+8q)h^3\\
&+(-2q^3+22q^2+76q+48)h^2+(12q^2+72q+96)h+36(q+2),\\
B_q(h)={}&2q(q+2)^2h^4+(-2q^4-6q^3+12q^2+32q)h^3\\
&+(3q^4+10q^3+22q^2+28q)h^2+(12q^3+36q^2+24q)h+18q(q+2).
\end{aligned}
\]
For \(q\ge10\), each has exactly two distinct positive roots, \(\alpha_q^-<\alpha_q^+\) for \(A_q\) and \(\beta_q^-<\beta_q^+\) for \(B_q\). Then
\[
\boxed{
\{h\ge0:T_q(h)\ge0\ \text{entrywise}\}=
\begin{cases}
[0,\infty), &2\le q\le9,\\
[0,\alpha_q^-]\cup[\alpha_q^+,\beta_q^-]\cup[\beta_q^+,\infty), &10\le q\le30,\\
[0,\alpha_q^-]\cup[\beta_q^+,\infty), &q\ge31.
\end{cases}}
\]
The three-window to two-window transition is governed by the unique positive zero \(q_*=30.086536465\ldots\) of
\[
F(q)=3q^6-64q^5-708q^4-2388q^3-2375q^2-1776q-576.
\]
The adjacent integer regimes are sharp. For instance, for \(K_{2,10}\) the four boundaries are approximately \(0.561309712\), \(1.097192556\), \(3.053751294\), and \(5.779166349\). In contrast, for \(K_{2,31}\) the two forbidden diagonal intervals overlap, and only two positivity components remain.

## Assumptions and scope

The graph is simple, undirected, connected, unweighted, and has bipartition sizes exactly \(2\) and \(q\). Every real positive step is considered, without local-error, adaptive-control, or internal-stage positivity constraints. Nonnegativity means that the *completed one-step matrix* maps all componentwise nonnegative data to nonnegative data. It is not claimed that the internal Runge--Kutta stages are nonnegative. At each finite positive root boundary, one diagonal class vanishes; all stated endpoints are included.

## Proof

Set \(R(z)=(6-2z)/(z^2+4z+6)\) and \(D(z)=z^2+4z+6\). The orthogonal spectral decomposition of the Laplacian has eigenvalues \(0\), \(q\), \(2\), and \(q+2\), with the latter three eigenvalues in the within-first-part, within-second-part and between-part contrast spaces, respectively. Consequently, the two diagonal classes are
\[
\begin{aligned}
d_A(h)&=\tfrac12R(qh)+\tfrac1{q+2}+\tfrac{q}{2(q+2)}R((q+2)h)\\
&=\frac{A_q(h)}{(q+2)D(qh)D((q+2)h)},\\
d_B(h)&=\tfrac{q-1}{q}R(2h)+\tfrac1{q+2}+\tfrac{2}{q(q+2)}R((q+2)h)\\
&=\frac{2B_q(h)}{q(q+2)D(2h)D((q+2)h)}.
\end{aligned}
\]
Every denominator is strictly positive for \(h\ge0\). For completeness, put \(g(z)=(1-R(z))/z=(z+6)/D(z)\), extended to \(z=0\). Its derivative is \(g'(z)=-(z^2+12z+18)/D(z)^2<0\) on \([0,\infty)\). All cross-part entries equal \(h g((q+2)h)>0\) for \(h>0\). Each within-part off-diagonal entry equals the relevant positive degree-factor times \(h[g(\text{within-part eigenvalue}\cdot h)-g((q+2)h)]\), also strictly positive. Hence only \(A_q\) and \(B_q\) can obstruct positivity.

For each of the eight integers \(2\le q\le9\), exact Sturm sequences give zero strictly positive roots for both quartics. Both quartics are positive at \(h=0\), and therefore positive throughout the nonnegative half-line. These finitely many exact Sturm counts are reproduced by the attached checker, not inferred from floating-point sampling.

Now let \(q\ge10\) be real, which permits the root-order argument to interpolate between integer graph sizes. Each quartic has positive constant and leading coefficients and negative cubic coefficient; its quadratic coefficient may have either sign. Descartes' rule therefore bounds its number of positive roots by two. Directly,
\[
A_q(1)=-(q+2)(q^3-4q^2-42q-108)<0
\]
and
\[
B_q(4)=-2q(q+2)(40q^2-248q-1169)<0.
\]
The inequalities hold for all \(q\ge10\) by expanding each bracket at \(q=10+t\), \(t\ge0\), where the coefficients are positive. Since both quartics are positive at zero and at infinity, each has *exactly* two positive, simple roots. The corresponding negative intervals are precisely \((\alpha_q^-,\alpha_q^+)\) and \((\beta_q^-,\beta_q^+)\); each endpoint depends continuously on real \(q\ge10\).

A direct polynomial Sylvester resultant is
\[
\operatorname{Res}_h(A_q,B_q)=-46656q^4(q-2)^4(q+2)^{10}F(q).
\]
The coefficient sequence of \(F\) has one sign change, so it has at most one positive root. Since \(F(30)=-8347356<0\) and \(F(31)=102913596>0\), it has exactly one, \(q_*\in(30,31)\). At \(q=10\), the exact signs of the two polynomials at \(h=1,2,4\) show \(\alpha^-<\alpha^+<\beta^-<\beta^+\). At \(q=31\), \(A_{31}(1)<0<A_{31}(2)\), \(B_{31}(1)>0>B_{31}(2)\), and *both* are negative at the rational step \(h=44/25\); these signs show \(\alpha^-<\beta^-<\alpha^+<\beta^+\). No relative endpoint ordering can change away from a common root, and the resultant has no further root for real \(q\ge10\). Therefore all integer sizes \(10\le q\le30\) have disjoint negative intervals, whereas all integer sizes \(q\ge31\) have overlapping negative intervals, exactly as claimed. The finite matrix checks in the verifier are corroboration rather than a replacement for the all-size argument.

## Verification

Run \(\texttt{python verify.py}\) in a Python environment with SymPy 1.12 or later. The checker verifies the exact rational diagonal identities, the 16 Sturm root counts for small integer sizes, the all-parameter sign witnesses, the full Sylvester resultant identity, the unique positive root count of \(F\), rational order witnesses at sizes \(10\) and \(31\), and exact full-matrix spectral identities for sizes \(2\) through \(13\) at five rational steps each. The recorded successful replay is \(\texttt{VERIFY\_OK 281}\). No infinite conclusion is inferred solely from those 12 finite matrix instances.

## Relationship to prior work

Brugnano, Iavernaro and Magherini describe Radau IIA methods and efficient implicit-stage solution, not a complete-bipartite endpoint positivity-window classification. Ketcheson, Gottlieb and Macdonald develop strong-stability-preserving two-step methods and the broader motivation for positivity/monotonicity preservation, rather than evaluating these Radau IIA matrices. A prior complete-multipartite calculation already establishes unconditional positivity up to total order \(11\), positivity of off-diagonals, and eventual positivity after diagonal sign loss; those conclusions are not new here. This theorem adds the entire all-step interval topology in the naturally asymmetric degree-two bipartite family and the exact merger threshold between three and two positive-step components.

## Limitations

The claim concerns completed endpoint maps only, not their internal stage vectors. For general \(K_{p,q}\) with both part sizes variable, an analogous topology classification is not established here. The value of \(q_*\) describes continuous algebraic interpolation; only integer \(q\) correspond to actual graph sizes. A matching statement could exist in literature that is not indexed or accessible in the sources inspected; the novelty comparison is not independent certification.

## References

- L. Brugnano, F. Iavernaro, C. Magherini, *Efficient implementation of Radau collocation methods*, arXiv:1302.1037v1, initially public 2013-02-05, https://arxiv.org/abs/1302.1037.
- D. I. Ketcheson, S. Gottlieb, C. B. Macdonald, *Strong stability preserving two-step Runge--Kutta methods*, arXiv:1106.3626v1, initially public 2011-06-18, https://arxiv.org/abs/1106.3626.
