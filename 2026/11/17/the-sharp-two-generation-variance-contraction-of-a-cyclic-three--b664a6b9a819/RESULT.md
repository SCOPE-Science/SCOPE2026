# The sharp two-generation variance contraction of a cyclic three-type quadratic population map

## Finding
For the closed probability simplex \(\Delta=\{(x_1,x_2,x_3)\in[0,1]^3:x_1+x_2+x_3=1\}\), consider the quadratic stochastic map
\[
(Vx)_i=\frac{x_1^2+x_2^2+x_3^2}{3}+2x_i x_{i+1},\qquad i\in\{1,2,3\},\quad x_4=x_1.
\]
Let \(c=(1/3,1/3,1/3)\) and \(D(x)=\sum_{i=1}^3(x_i-1/3)^2\). Then the **optimal two-generation mean-square imbalance coefficient** is
\[
\boxed{D(V^2x)\leq\rho_*D(x),\qquad
\rho_* =\frac{57968+10912\sqrt{22}}{531441}\approx0.2053846368104705.}
\]
For every \(x\ne c\), equality holds if and only if \(x\) is a permutation of \((a_*,a_*,1-2a_*)\), where \(a_*=(2+\sqrt{22})/18\). By contrast, the sharp one-generation inequality is only \(D(Vx)\le D(x)\), with equality away from \(c\) precisely at the three edge midpoints. Consequently every trajectory converges to \(c\), with the explicit global estimate
\[
D(V^nx)\le\rho_*^{\lfloor n/2\rfloor}D(x)\qquad(n=0,1,2,\ldots).
\]
The optimizing state is strictly interior and nonuniform; the sharp two-generation factor exceeds the linearized two-generation factor \(16/81\) at equilibrium.

## Assumptions and scope
All states belong to the **closed** two-simplex, including edges and vertices. Time is discrete, and the same polynomial map acts at each generation. The variance \(D\) is unnormalized squared Euclidean distance to the barycenter; multiplying it by a fixed positive constant leaves every contraction factor unchanged. The stated optimality concerns **two generations**, not the asymptotic spectral rate, and does not assert a contraction for the distance between two arbitrary trajectories.

## Proof
Put \(p=x_1x_2+x_2x_3+x_3x_1\) and \(q=x_1x_2x_3\). They satisfy \(0\le p\le1/3\), \(q\ge0\), and \(D(x)=2/3-2p\). Every output coordinate is the common number \((1-2p)/3\) plus twice one of the pair products \(x_1x_2,x_2x_3,x_3x_1\); in particular, the unordered output coordinates depend only on \(p,q\). Direct elementary-symmetric calculation gives
\[
p'=\frac13-\frac43p^2+4q,\qquad
q'=\frac{16p^3-12p^2-72pq+216q^2+36q+1}{27}.
\]
The exact one-step and two-step variances are
\[
D(Vx)=\frac83p^2-8q,\qquad
D(V^2x)=\frac{32}{27}\bigl(4p^4-4p^3-24p^2q+p^2+18pq-18q^2-3q\bigr).
\]
For fixed \(p\), the latter is nonincreasing in \(q\), because
\[
\frac{\partial D(V^2x)}{\partial q}=-\frac{32}{9}(8p^2-6p+12q+1)\le0.
\]
Indeed, when \(p\le1/4\), the expression in parentheses is bounded below by \((4p-1)(2p-1)\ge0\). When \(p\ge1/4\), Schur's inequality \(1+9q\ge4p\) gives the lower bound \((24p^2-2p-1)/3\ge0\). Since \(D(x)\) depends only on \(p\), maximizing the variance ratio at a fixed \(p<1/3\) reduces to minimizing \(q\) among states with that value of \(p\).

For \(0\le p\le1/4\), the minimum \(q=0\) occurs on an edge (the two nonzero coordinates are roots of \(t(1-t)=p\)); there
\[
\frac{D(V^2x)}{D(x)}=R_{\mathrm{edge}}(p)=\frac{16p^2(1-2p)^2}{9(1-3p)}.
\]
Differentiation yields
\[
R'_{\mathrm{edge}}(p)=\frac{-16p(2p-1)(18p^2-11p+2)}{9(3p-1)^2}\ge0;
\]
the quadratic factor is everywhere positive, so the maximum on this interval is \(R_{\mathrm{edge}}(1/4)=1/9\).

For \(1/4<p<1/3\), minimizers of \(q\) subject to fixed \(p\) are among points with two equal coordinates, by Lagrange multipliers or the discriminant boundary of the cubic with roots \(x_1,x_2,x_3\). Explicitly, write the two equal entries as \(a_+=(1+\sqrt{1-3p})/3\), with the remaining coordinate \(1-2a_+\). This has smaller product than the alternative two-equal branch \(a_-=(1-\sqrt{1-3p})/3\), since the two products differ by \(4(1-3p)^{3/2}/27\). Here \(a_+\in(1/3,1/2)\), and direct substitution gives
\[
R_{\mathrm{eq}}(a)=\frac{D(V^2(a,a,1-2a))}{D(a,a,1-2a)}=\frac{16}{9}a^2(6a^2-2a-1)^2.
\]
This ratio extends continuously to \(a=1/3\) with value \(16/81\), and at \(a=1/2\) has value \(1/9\). Its derivative is
\[
R'_{\mathrm{eq}}(a)=\frac{32}{9}a(6a^2-2a-1)(18a^2-4a-1).
\]
The first quadratic factor is negative throughout \([1/3,1/2]\), and the second changes sign once, from negative to positive, at \(a_*=(2+\sqrt{22})/18\). Thus the unique maximum is
\[
R_{\mathrm{eq}}(a_*)=\frac{57968+10912\sqrt{22}}{531441}>\frac{16}{81}>\frac19.
\]
Strict decrease of \(D(V^2x)\) in \(q\) away from the minor boundary degeneracy establishes the stated equality classification. At \(c\), both sides vanish.

For completeness, the one-step sharp coefficient is obtained from the same \(q\)-minimizing argument: on \(q=0\), \(D(Vx)/D(x)=4p^2/(1-3p)\), which increases to \(1\) at \(p=1/4\); on the two-equal minimizing branch, it equals \(4a_+^2\le1\), with equality only as \(a_+\to1/2\). Equality therefore holds away from \(c\) only at the edge midpoints. Iterating the two-step inequality and applying the one-step inequality for odd indices proves the global decay estimate and convergence. The exact linearization at \(c\) has tangent eigenvalues \((2/3)e^{\pm i\pi/3}\); hence its two-step variance factor is \(16/81\), strictly below the global optimum.

## Verification
The standalone `verify.py` checks the claimed one-step and two-step symmetric-polynomial identities by exact symbolic expansion, the derivative identity, the radical optimizer and its sharp equality, and 285 rational-grid states in the closed simplex. Invoke `python verify.py` with Python 3 and SymPy installed. The symbolic checks verify the essential algebra; the global maximization is the analytic argument above, **not** a conclusion drawn from sampled states.

## Relationship to prior work
Mamurov introduced this exact cyclic non-Volterra quadratic stochastic operator and established its globally attracting barycenter, using a product of coordinate gaps as a Lyapunov function. The present theorem does not reassert that qualitative result as new. Instead it determines the best possible finite-horizon quadratic-variance contraction in exactly two generations, its unique nontrivial maximizing compositions, and the contrast with the sharp one-generation factor. The relevant prior paper's mathematical statement and main argument were inspected; no optimal two-step variance coefficient was found there. Jamilov's permutation-indexed quadratic stochastic family, and general stability results for other nonlinear stochastic operators, concern different maps or qualitative dynamics, not this precise extremum.

## Limitations
This is a theorem for this particular three-type map; it does not classify general quadratic stochastic operators, arbitrary pairwise trajectory distances, random switching, or optimal constants for every number of iterates. The factor \(\rho_*\) is a sharp *two-step transient* factor, not the asymptotic spectral rate. Priority relative to unindexed general contraction results remains uncertain. The earliest identified source is a conference abstract in proceedings dated May 11–12, 2022; its individual presentation day and online upload timestamp could not be separately determined. Independent mathematical review has not been performed.

## References
1. B. J. Mamurov, *Regularity of a Non-Volterra Quadratic Stochastic Operator on the 2D Simplex*, Ilm Sarchashmalari 11 (2022), 29–31; publicly accessible full article: https://uniwork.buxdu.uz/resurs/12848_1_9048BBB21456EB56BEF38A64C05BED225AE03842.pdf.
2. B. J. Mamurov, paper of the same title in the *International Scientific and Practical Conference: Modern Problems of Applied Mathematics and Information Technologies*, Bukhara, proceedings dated May 11–12, 2022, p. 13: https://uniwork.buxdu.uz/resurs/13348_1_95F69686F3563813FDBCE24AE88879AE0FD79285.pdf.
3. U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, Communications in Mathematics 31 (2023), 31–41, arXiv:2210.05107, first version October 11, 2022: https://arxiv.org/abs/2210.05107.
4. U. U. Jamilov et al., *Dynamics of nonlinear stochastic operators and associated Markov measures*, Mathematical Methods in the Applied Sciences 47 (2024), 13300–13312: https://doi.org/10.1002/mma.10191.
