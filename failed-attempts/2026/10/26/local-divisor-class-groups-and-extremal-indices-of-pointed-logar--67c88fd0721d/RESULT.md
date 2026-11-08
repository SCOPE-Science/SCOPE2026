# Local divisor class groups and extremal indices of pointed logarithmic Hilbert schemes

## Finding
For every integer \(n\ge2\), let \(X_n\) be the coarse toric variety of the logarithmic Hilbert stack \(\operatorname{Hilb}^{n}(\mathbb P^1_{\mathbb C}\mid0)\) of Arena–Song. Its \(2^n\) torus fixed points admit a canonical binary labeling \(b=(b_0,\ldots,b_{n-1})\), described below. If the positions of the ones are \(0\le i_1<\cdots<i_r\le n-1\), define the positive gap lengths \(g_t=i_{t+1}-i_t\) for \(t<r\) and \(g_r=n-i_r\). If there are no ones, take the empty list. Then the local Weil divisor class group is, as an abstract finite abelian group,
\[
\operatorname{Cl}(\mathcal O_{X_n,x_b})\cong\bigoplus_{t=1}^r\mathbb Z/g_t\mathbb Z.
\]
Here a summand of order one is zero. In particular, its order, equivalently the multiplicity of the corresponding simplicial cone, is \(\prod_{t=1}^r g_t\), with the empty product equal to one.

The largest such order is
\[
B(n)=\begin{cases}
3^{n/3},&n\equiv0\pmod3,\\
4\cdot3^{(n-4)/3},&n\equiv1\pmod3,\\
2\cdot3^{(n-2)/3},&n\equiv2\pmod3.
\end{cases}
\]
The respective numbers of fixed points achieving this maximum are \(1\) when \(n=3a\), \(a+1\) when \(n=3a+2\), and \(a(a+3)/2\) when \(n=3a+1\) (the last case has \(a\ge1\)). This classifies every torus-fixed local divisor group and all maximizers, not merely their determinant orders.

## Assumptions and scope
Work over \(\mathbb C\) and let \(N=\mathbb Z^n\) have basis \(e_1,\ldots,e_n\). Use the complete simplicial fan described in Definition 4.2 and Lemma 4.3 of Arena–Song: its old rays are \(u=-\sum_{i=1}^n e_i\) and the \(e_i\), and its inserted rays are
\[
\rho_j=\sum_{k=n-j+1}^{n}(k+j-n)e_k\quad(2\le j\le n).
\]
These arise by successive stellar subdivisions in descending order of \(j\). The maximal cones make one choice from each pair
\[
(u,\rho_n),\quad(e_j,\rho_{n-j})\ (1\le j\le n-2),\quad(e_{n-1},e_n).
\]
This binary choice is \(b_i=0\) for the first ray in its pair and \(b_i=1\) for the second. The invariant concerns the coarse scheme, its closed torus orbits, and the algebraic local class groups. It does not claim the entire class-group structure at nonfixed orbits, or the class groups of the smooth stack itself.

## Proof
**Fan combinatorics.** A star subdivision of the maximal-coordinate face \(\operatorname{cone}(e_1,\ldots,e_n)\) inserts \(\rho_n\), after which the facet inside the cone spanned by the last \(n-1\) coordinate rays is subdivided along \(\rho_{n-1}\), and so on. Induction on this nested sequence shows that each maximal cone selects exactly one ray from each listed pair; there are exactly \(2^n\) cones. This is also compatible with the Stanley–Reisner nonface relations of Lemma 4.3 in the cited paper.

**Integral change of coordinates.** Define a lattice automorphism \(T:N\to N\) by \((Tv)_k=v_k-2v_{k-1}+v_{k-2}\), where \(v_0=v_{-1}=0\). Its matrix is lower unitriangular, hence integral unimodular. In the target basis \(f_k\), it gives
\[
T(u)=-f_1+f_2,\quad T(\rho_{n-j})=f_{j+1}\ (0\le j\le n-2),
\]
\[
T(e_j)=f_j-2f_{j+1}+f_{j+2}\ (1\le j\le n-2),\quad T(e_{n-1})=f_{n-1}-2f_n,\quad T(e_n)=f_n.
\]
For each cone, compute the quotient lattice \(N/\sum_{v\in\sigma(1)}\mathbb Zv\) by generators \(z_1,\ldots,z_n\) representing the \(f_i\). Set formally \(z_{n+1}=0\). A one at position \(i\) imposes \(z_{i+1}=0\). A zero at position \(i\ge1\) imposes the discrete second-difference recurrence \(z_i-2z_{i+1}+z_{i+2}=0\), valid also at \(i=n-1\). A zero at position \(0\) imposes \(z_1=z_2\).

**Independent gap blocks.** If no one occurs, the initial equality and recurrences force every \(z_i\) equal, and the last relation forces their common value to zero. Otherwise, all generators preceding the first forced zero vanish. Between successive forced zeros at \(z_{i_t+1}\) and \(z_{i_{t+1}+1}\), second differences yield an arithmetic progression with common increment \(w_t\), and the terminal equality imposes precisely \((i_{t+1}-i_t)w_t=0\). After the final forced zero, the terminal boundary \(z_{n+1}=0\) imposes \((n-i_r)w_r=0\). The blocks have disjoint generators except for already zero endpoints. Thus the quotient is the claimed direct sum, and the generating rays span finite index \(\prod_t g_t\).

For a full-dimensional simplicial affine toric chart \(U_\sigma\), the standard toric divisor sequence identifies its class group with the finite lattice quotient above, noncanonically as an abstract abelian group. Every invariant divisor of this chart contains the closed orbit; localizing at its torus fixed point preserves this presentation, yielding the formula for \(\operatorname{Cl}(\mathcal O_{X_n,x_b})\).

**Sharp maximum and equality cases.** The gaps are an ordered composition of \(n-i_1\); choosing \(i_1=0\) realizes every ordered composition of \(n\). The largest product of positive parts strictly grows with the total, so any maximizer begins at \(i_1=0\). A part equal to one can be combined with another part to increase the product; a part of size at least five is improved by replacing it with three and its complement. Hence optimum compositions use twos and threes (with fours optionally viewed as two twos), and never three twos, since \(2\cdot2\cdot2<3\cdot3\). This proves the displayed piecewise maximum. If \(n=3a\) there is only the all-three composition. If \(n=3a+2\) there is exactly one two in \(a\) threes, giving \(a+1\) orders. If \(n=3a+1\) there is either one four among \(a-1\) threes (\(a\) placements), or two twos among \(a-1\) threes (\(\binom{a+1}{2}\) placements), for total \(a(a+3)/2\). These ordered compositions correspond bijectively to maximizing fixed points.

## Verification
The standalone `VERIFY.py` constructs every binary maximal-cone ray matrix for \(2\le n\le8\), computes each determinant by exact integer elimination, and checks it against the independently evaluated gap product. It also checks the maximum and its multiplicity. These finite checks test \(\sum_{n=2}^{8}2^n=508\) cones. They are not substituted for the universal lattice presentation and integer-composition arguments.

## Relationship to prior work
Arena and Song construct the weighted blow-up, prove the toric fan presentation in §4.4, and describe stabilizers of boundary strata by weighted symmetric products in §7. Their formula states that cyclic stabilizer factors divide bubble lengths. Those results are used as starting data, not claimed here. The present calculation resolves *every* fixed-chart divisor group by an explicit direct sum of gap-length cyclic groups and gives exact sharp index and equality-case counts for all dimensions. Toric class-group presentations are standard, as is the elementary maximal-product problem for integer compositions; the new geometry is the identification of the entire fixed-point torsion spectrum and extremal classification for this specific log Hilbert family.

## Limitations
The statement is for the coarse toric variety and its torus fixed points, not an assertion that all points have these class groups, nor that this is a classification of abstract quotient singularities beyond their divisor classes. The index maximum concerns order of the local class group (the cone multiplicity), not canonical or Gorenstein index. The originating paper's general stabilizer description is closely related and may imply some parts via additional specialization; priority beyond the inspected source remains a risk. No independent validation has been performed.

## References
1. V. Arena and T. D. Song, *Logarithmic Hilbert schemes of curves as weighted blow-ups and their integral Chow rings*, arXiv:2605.17922v1 (first public 18 May 2026), especially Definition 4.2, Lemma 4.3, and §7. https://arxiv.org/html/2605.17922v1.
2. W. Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies 131, Princeton University Press (1993), toric divisor class groups of affine charts.
