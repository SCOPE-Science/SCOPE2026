# Sharp mean-zero Sobolev evaluation on metric flower graphs

## Finding

Let \(r,p\ge1\). Form a compact connected metric graph \(F\) by attaching \(r\) loops of arbitrary lengths \(L_1,\ldots,L_r>0\) and \(p\) pendant intervals of arbitrary lengths \(h_1,\ldots,h_p>0\) to the same central vertex. Equip all edges with ordinary unweighted arclength. Put
\[
T=\sum_{i=1}^r L_i+\sum_{j=1}^p h_j,\qquad
M=\max_i L_i,\qquad H=\max_j h_j,\qquad
B=\frac{\sum_i L_i^3/12+\sum_j h_j^3/3}{T^2}.
\]
Every real continuous edgewise-\(H^1\) function with zero arclength mean satisfies the sharp inequality
\[
\|f\|_{L^\infty(F)}^2\le \mathcal K(F)\int_F|f'|^2\,ds,
\qquad
\boxed{\mathcal K(F)=B+\frac1T\max\!\left\{H(T-H),\frac{M(T-M)}4\right\}.}
\]
The squared evaluation norm at coordinate \(s\) on loop \(i\), respectively coordinate \(s\) on pendant interval \(j\), both measured from the common vertex, is exactly
\[
Q_{\mathrm{loop},i}(s)=B+\frac{T-L_i}{T L_i}s(L_i-s),\quad 0\le s\le L_i,
\]
\[
Q_{\mathrm{pend},j}(s)=B+\frac{s^2+(T-2h_j)s}{T},\quad 0\le s\le h_j.
\]
All global maximizers are among the midpoints of loops of length \(M\) and the free tips of pendant intervals of length \(H\). Precisely the longest-loop midpoints maximize when \(M(T-M)/4>H(T-H)\); precisely the longest pendant tips maximize when this inequality reverses; and both sets maximize at equality. No other points maximize. The nonzero equality functions are exactly the nonzero scalar multiples of the centered energy Green representers for these maximizing evaluation points.

For a **single pendant** of length \(h\), write \(A=\sum_iL_i\). If \(r\ge2\), the localization switches exactly once, at
\[
h_c=\frac{M(A-M)}{4A-M}.
\]
For \(0<h<h_c\) the longest-loop midpoints maximize, for \(h=h_c\) these and the free tip tie, and for \(h>h_c\) only the free tip maximizes. If \(r=1\), the tip is the unique maximizer for every \(h>0\). Moreover, the following **universal sharp length-budget threshold** holds for every \(r\ge2\):
\[
0<h_c\le (7-4\sqrt3)A.
\]
Equality in the upper bound occurs precisely when \(M/A=4-2\sqrt3\). In particular, whenever \(h>(7-4\sqrt3)A\), the free tip is the unique maximizing point regardless of the number and individual lengths of loops. The universal bound is attainable by a two-loop bouquet with the displayed longest-loop length ratio.

## Assumptions and scope

The graph has exactly one central junction, with \(r\ge1\) genuine self-loops and \(p\ge1\) genuine pendant intervals; all edge lengths are finite and strictly positive. The endpoint coordinates \(0\) and \(L_i\) of each loop represent the same central vertex, while \(0\) is the central endpoint of each pendant edge. Functions are real, globally continuous, and belong to \(H^1\) on each edge. There are no point masses or weighted densities. The mean constraint uses unnormalized arclength, \(\int_Ff\,ds=0\), and the energy uses \(\int_F|f'|^2\,ds\), with no extra factors. Equivalently, this is the norm-squared of the embedding of the mean-zero energy Hilbert space into \(C(F)\). The parameter range includes ties in loop and pendant lengths, and the critical equality cases.

## Proof

1. **Hilbert-space decomposition.** Write \(c=f(v)\) for the common-vertex value and \(f=c+g\) edgewise. On loop \(i\), \(g_i(0)=g_i(L_i)=0\), so \(g_i\in H^1_0(0,L_i)\); on pendant \(j\), \(g_j(0)=0\) with no condition at its free tip. The zero-mean constraint fixes
   \[
   c=-\frac1T\left(\sum_i\int_0^{L_i}g_i\,ds+\sum_j\int_0^{h_j}g_j\,ds\right).
   \]
   The squared energy is exactly the direct sum \(\sum\int|g_e'|^2\). Conversely, every such family of anchored functions determines one admissible \(f\). Hence evaluation at a point of edge \(e\) is \(g_e(s)-T^{-1}\sum_a\int g_a\).

2. **Exact kernels.** The evaluation reproducing kernel in \(H^1_0(0,L_i)\) is \(D_i(s,t)=\min(s,t)-st/L_i\). The anchored pendant space \(\{g\in H^1(0,h_j):g(0)=0\}\) has kernel \(N_j(s,t)=\min(s,t)\). The following identities are direct one-variable integrations:
   \[
   D_i(s,s)=\frac{s(L_i-s)}{L_i},\quad
   \int_0^{L_i}D_i(s,t)dt=\frac{s(L_i-s)}2,\quad
   \int_0^{L_i}\!\int_0^{L_i}D_i(s,t)\,ds\,dt=\frac{L_i^3}{12},
   \]
   \[
   N_j(s,s)=s,\quad
   \int_0^{h_j}N_j(s,t)dt=h_js-\frac{s^2}{2},\quad
   \int_0^{h_j}\!\int_0^{h_j}N_j(s,t)\,ds\,dt=\frac{h_j^3}{3}.
   \]
   Taking the squared norm of \(g_e(s)-T^{-1}\sum_a\int g_a\) in the orthogonal sum of these Hilbert spaces gives the two stated evaluation formulas, with the common term \(B\). The underlying energy Hilbert space is complete and has no nonzero zero-energy element because of its mean constraint. Thus the squared evaluation norm is attained by the corresponding Riesz representer.

3. **Exact optimization.** On a loop, \(T-L_i>0\), and \(s(L_i-s)\) is strictly maximized at \(L_i/2\). On pendant \(j\), the evaluation profile is strictly convex in \(s\). Its value at the free tip exceeds its value at the junction by \(h_j(T-h_j)/T>0\); hence only that tip can maximize along its edge. If \(L_i>L_k\), then
   \[
   L_i(T-L_i)-L_k(T-L_k)=(L_i-L_k)(T-L_i-L_k)>0,
   \]
   as the pendant length is positive. The same factorization proves that among pendant tips, longer intervals have strictly larger norms because the loop length is positive. Thus only longest loops and longest pendants can be globally maximal, and comparison of their displayed values proves the exact norm and all equality-point classifications. The vertex itself has squared evaluation norm \(B\), strictly below the global maximum.

4. **Quantified deficit and equality functions.** Define \(D=\max\{H(T-H),M(T-M)/4\}\). On loop \(i\),
   \[
   \mathcal K(F)-Q_{\mathrm{loop},i}(s)=
   \frac{D-L_i(T-L_i)/4}{T}+
   \frac{T-L_i}{T L_i}\left(s-\frac{L_i}{2}\right)^2.
   \]
   On pendant \(j\),
   \[
   \mathcal K(F)-Q_{\mathrm{pend},j}(s)=
   \frac{D-h_j(T-h_j)}{T}+
   \frac{(h_j-s)(T-h_j+s)}{T}.
   \]
   All terms are nonnegative, and the zero sets give exactly the asserted maximizing points. Cauchy--Schwarz in the energy Hilbert space gives the sharp inequality. Equality for any nonzero function forces proportionality to an evaluation Riesz representer at a maximizing point, and each such representer indeed gives equality.

5. **Sharp one-pendant transition.** When \(p=1\), \(T=A+h\), the tip contribution is \(Ah\) and the competing longest-loop contribution is \(M(A+h-M)/4\). Their difference has positive \(h\)-slope \(A-M/4\), and solving equality gives \(h_c=M(A-M)/(4A-M)\). With one loop, \(A=M\) so \(h_c=0\). With at least two loops, \(A>M\) so the unique threshold is positive. For \(t=M/A\in(0,1)\),
   \[
   \frac{h_c}{A}=\frac{t(1-t)}{4-t}.
   \]
   Its derivative has the sign of \(t^2-8t+4\); the unique maximizer on \((0,1)\) is \(t=4-2\sqrt3\), with maximum \(7-4\sqrt3\). Taking two loops with lengths \((4-2\sqrt3)A\) and \((2\sqrt3-3)A\) attains the bound. This proves sharpness, the universal dominance claim, and the critical ties.

## Verification

A standalone standard-library Python checker, `CHECKER.py`, derives the squared diagonal a second way from exact effective-resistance integrals: \(Q(x)=T^{-1}\int_F R(x,y)dy-(2T^2)^{-1}\int_F\int_F R(y,z)dy\,dz\). It enumerates rational edge-length choices, rational sample points, both edge types, and the exact critical case of two equal loops with one pendant of length \(1/7\). The checker uses `fractions.Fraction` and requires no external packages. Run `python CHECKER.py`; the expected final line is `ALL_FLOWER_SOBOLEV_DIAGNOSTICS_PASSED`. Its finite tests corroborate, but do not substitute for, the universal analytical proof above.

## Relationship to prior work

General Laplacian, effective-resistance and Green-kernel methods on metric graphs were established by Baker and Faber (arXiv:math/0407428, first public version July 25, 2004), including series and junction decompositions of resistance. Solomyak (arXiv:math/0206235, first public June 23, 2002) studied Sobolev spaces and approximation numbers on arbitrary compact metric graphs. Cinkir (arXiv:0901.0407, first public January 5, 2009; arXiv:0902.3401, first public February 19, 2009) treated graph operations and Green/resistance formulas primarily for the **canonical-measure tau constant**, which is distinct from the present **unnormalized-arclength, mean-zero sharp evaluation norm**. Those general techniques are not claimed as new. Closely related special graph calculations include a rose without pendants and a banana graph with one pendant; neither supplies the simultaneous arbitrary-loop/arbitrary-pendant evaluation profiles, their all-parameter maximizer classification, or the sharp universal one-pendant threshold. Equivalence through an older specialized result not identified in the inspected literature remains possible.

## Limitations

The theorem requires all loops and pendant intervals to meet at one vertex. It does not apply to multiple hubs, attached nontrivial trees, cycles meeting at multiple vertices, vertex atoms, nonconstant edge densities, or higher-order energies. The classification is only for real first-order mean-zero Sobolev energy. The numerical checker tests finitely many positive rational lengths and points; it cannot establish all-dimensional or all-real-parameter statements. The priority assessment is necessarily conditional on the literature searched; an unindexed prior formula may exist.

## References

- M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, first publicly posted 2002-06-23. https://arxiv.org/abs/math/0206235
- M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first publicly posted 2004-07-25. https://arxiv.org/abs/math/0407428
- Z. Cinkir, *The tau constant of a metrized graph and its behavior under graph operations*, arXiv:0901.0407, first publicly posted 2009-01-05. https://arxiv.org/abs/0901.0407
- Z. Cinkir, *The tau constant and the discrete Laplacian matrix of a metrized graph*, arXiv:0902.3401, first publicly posted 2009-02-19. https://arxiv.org/abs/0902.3401
