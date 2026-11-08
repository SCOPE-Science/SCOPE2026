# Periodic zeta transfer for cyclically coupled interval maps

## Finding
For every integer \(s\ge2\), let \(I_1,\ldots,I_s\) be compact intervals, and let continuous maps \(f_i:I_i\to I_{i+1}\) be given, reading subscripts cyclically. Define the cyclically coupled map
\[
F(x_1,\ldots,x_s)=(f_s(x_s),f_1(x_1),\ldots,f_{s-1}(x_{s-1})),
\]
and the one-coordinate return map \(g=f_s\circ\cdots\circ f_1:I_1\to I_1\). Assume \(a_n=\#\operatorname{Fix}(g^n)<\infty\) for every \(n\ge1\). Then all fixed-point sets of iterates of \(F\) are finite, and their **complete exact census** is
\[
\boxed{\#\operatorname{Fix}(F^m)=a_{m/d}^{\,d},\qquad d=\gcd(m,s),\quad m\ge1.}
\]
Thus the Artin--Mazur zeta series of the coupled system is determined by the one-dimensional counts:
\[
\boxed{\zeta_F(z)=\exp\!\left(\sum_{m\ge1}\frac{a_{m/\gcd(m,s)}^{\gcd(m,s)}}{m}z^m\right).}
\]
If, moreover, there is a finite \(r\times r\) complex matrix \(A\) with \(a_n=\operatorname{tr}(A^n)\) for every \(n\ge1\), form the cyclic tensor operator \(B\) on \((\mathbb C^r)^{\otimes s}\) by
\[
B(v_1\otimes\cdots\otimes v_s)=Av_s\otimes v_1\otimes\cdots\otimes v_{s-1}.
\]
Then \(\operatorname{tr}(B^m)=\#\operatorname{Fix}(F^m)\) for every \(m\), and therefore
\[
\boxed{\zeta_F(z)=\det(I-zB)^{-1}.}
\]
For the Cournot case \(s=2\) this reduces to the much smaller exterior-square formula
\[
\boxed{\zeta_F(z)=\frac{1}{\det(I-zA)\det(I-z^2\bigwedge^2 A)}.}
\]
Even without a trace matrix, the zeta function of a two-coordinate Cournot map is rational whenever \(\zeta_g\) is rational: if, over \(\mathbb C\),
\[
\zeta_g(z)=\prod_{i=1}^t(1-\alpha_i z)^{-e_i},
\]
with distinct nonzero \(\alpha_i\) and integers \(e_i\), then
\[
\boxed{\zeta_F(z)=\zeta_g(z)\prod_i(1-\alpha_i^2z^2)^{-\binom{e_i}{2}}\prod_{i<j}(1-\alpha_i\alpha_jz^2)^{-e_ie_j}.}
\]
All zeta identities are identities of formal power series, without an assumption of analytic convergence.

## Assumptions and scope
The continuity assumption places the result in the standard interval-map setting; the counting proof itself only needs composable maps between sets. In particular, no reaction map must be injective, surjective, expanding or monotone. The sole finiteness hypothesis is \(a_n<\infty\) for every positive integer \(n\); this also guarantees the coupled zeta series is defined. For the matrix result the trace identity for **all** \(n\) is required, not an approximate or finite-range identity. The determinant/exterior-square formula does not follow from an arbitrary transition matrix unless its traces exactly count the original map's periodic points, including any boundary identifications.

## Proof
**1. Periodic-point transport among coordinates.** Let \(g_i=f_{i-1}\circ\cdots\circ f_i:I_i\to I_i\) denote the full-length composition starting at coordinate \(i\), with the cyclic order of application. The maps \(f_i\) intertwine \(g_i\) and \(g_{i+1}\). For every \(n\ge1\), restriction of \(f_i\) gives a bijection \(\operatorname{Fix}(g_i^n)\to\operatorname{Fix}(g_{i+1}^n)\): the composition of the remaining \(s-1\) maps, followed by \(g_{i+1}^{n-1}\), is a two-sided inverse on these fixed-point sets. Consequently, every \(g_i^n\) has exactly \(a_n\) fixed points.

**2. Count all iterates.** Write \(d=\gcd(m,s)\). The permutation of coordinates induced by \(F^m\) has exactly \(d\) cycles, each of length \(s/d\). For each coordinate cycle, the equations defining \(F^m(x)=x\) determine every other coordinate uniquely from a chosen representative by forward composition. Closing the equations around the cycle is equivalent to applying the corresponding full-length map \(g_i\) exactly \(m/d\) times to the representative. Thus this cycle contributes exactly \(a_{m/d}\) independent choices. Different coordinate cycles impose disjoint sets of conditions, giving \(a_{m/d}^d\). This argument counts points exactly, not symbolic itineraries, so there is no boundary overcounting.

**3. Tensor trace and rationality.** The operator \(B^m\) is a tensor permutation with \(d\) permutation cycles. Around each cycle the single nontrivial factor \(A\) is encountered exactly \(m/d\) times. The standard trace contraction along a permutation cycle gives \(\operatorname{tr}(A^{m/d})\), so
\[
\operatorname{tr}(B^m)=\operatorname{tr}(A^{m/d})^d=a_{m/d}^d.
\]
The formal identity \(\exp(\sum_{m\ge1}\operatorname{tr}(B^m)z^m/m)=\det(I-zB)^{-1}\) proves the matrix formula. For \(s=2\), write \(d=\gcd(m,2)\). If \(m\) is odd the count is \(a_m\), and if \(m=2n\) it is \(a_n^2\). Hence
\[
\log\zeta_F(z)-\log\zeta_g(z)=\sum_{n\ge1}\frac{a_n^2-a_{2n}}{2n}z^{2n}.
\]
For \(a_n=\operatorname{tr}(A^n)\), the numerator satisfies \((a_n^2-a_{2n})/2=\operatorname{tr}((\bigwedge^2 A)^n)\), proving the exterior-square expression. Finally, substitute \(a_n=\sum_i e_i\alpha_i^n\) into this last logarithmic identity, and group diagonal and off-diagonal terms; exponentiating gives the signed-multiplicity rational product displayed above. No positivity of the \(e_i\) is required.

**4. A continuous interval example with a genuinely new zeta factor.** On \([0,1]\), define
\[
g(x)=\begin{cases}2x,&0\le x\le1/4,\\1-2x,&1/4\le x\le1/2,\\2x-1,&1/2\le x\le1.\end{cases}
\]
This map is continuous. The invariant interval \([0,1/2]\) supports the full two-branch tent map, with exactly \(2^n\) distinct fixed points for the \(n\)-th iterate; none lies at a branch boundary except \(0\). Every point in \((1/2,1)\) eventually enters \([0,1/2]\), and \(1\) is the only additional periodic point. Thus \(a_n=2^n+1\), represented by \(A=\operatorname{diag}(2,1)\). Taking \(f_1=\mathrm{id}\) and \(f_2=g\) gives the continuous Cournot map \(F(x,y)=(g(y),x)\) with
\[
\boxed{\zeta_F(z)=\frac{1}{(1-2z)(1-z)(1-2z^2)}.}
\]
In particular, \(\#\operatorname{Fix}(F)=3\), \(\#\operatorname{Fix}(F^2)=9\), and \(F\) has exactly \(3\) primitive two-cycles, whereas \(g\) has only \(1\). The extra quadratic factor is a concrete coupling effect, not a restatement of the single-coordinate zeta function.

## Verification
The standalone standard-library script `verify.py` computes exact periodic-point counts for every family of finite maps with \(2\), \(3\), or \(4\) states in selected coordinate lengths \(s\in\{2,3,4\}\), and compares with the gcd formula for multiple iterate lengths. It also independently builds the tensor-permutation matrix for several small matrices and checks its iterate traces against the predicted formula. The supplied run returned `VERIFY_OK checks=605563`. These finite tests corroborate the formulas but do not prove their universal validity; the proof is the cycle-decomposition and trace argument above.

## Relationship to prior work
García Guirao's 2026 study of connected \(\omega\)-limit sets for Cournot maps explicitly defines the two-coordinate map and studies the geometry of its limit sets, including cases involving periodic orbits. The cyclic iterate decomposition and transport of periodic points are also established ideas in earlier work on cyclically permuted products (Linero Bas and Soler López, 2016; Li and Lu, 2020). The present claim is specifically the **all-iterate fixed-point census, Artin--Mazur zeta transfer, trace-model determinant construction and rationality/exterior-square criterion**, which were not stated in the inspected primary material. Pakapongpun and Ward studied zeta functions of Cartesian products in 2014; these provide related methods but are not, by themselves, an identification of the zeta series of the cyclically permuted map. This distinction is about logical implication, not title similarity. A broader uninspected general periodic-orbit identity remains an originality risk.

## Limitations
The result needs finite sets of fixed points for all iterates. A symbolic matrix only represents the actual Artin--Mazur zeta function if its traces are exact periodic-point counts, not merely counts of distinct symbolic paths. This is a statement about periodic data; it does not determine attractor basins, stability or \(\omega\)-limit-set geometry. The literature comparison has not independently established historical priority against every earlier work on cyclic products; full text of the 2016 Topology and its Applications article and the 2014 product-zeta paper was unavailable through the tested access routes. Independent scientific validation has not been performed.

## References
1. J. L. García Guirao, *Connected \(\omega\)-limit sets of Cournot maps: periodic orbits, realization and almost every point*, arXiv:2610.27229v1 (first public 2026-10-19), https://arxiv.org/abs/2610.27229.
2. A. Linero Bas and G. Soler López, *A note on the dynamics of cyclically permuted direct product maps*, Topology and its Applications 203 (2016), 147–158, DOI:10.1016/j.topol.2015.12.083.
3. R. Li and T. Lu, *The Topological Entropy of Cyclic Permutation Maps and Some Chaotic Properties on Their MPE sets*, Complexity (2020), DOI:10.1155/2020/9379628.
4. A. Pakapongpun and T. Ward, *Orbits for products of maps*, Thai Journal of Mathematics 12 (2014), 33–44, https://eprints.whiterose.ac.uk/id/eprint/103802/.
5. M. Artin and B. Mazur, *On periodic points*, Annals of Mathematics 81 (1965), 82–99, DOI:10.2307/1970384.
