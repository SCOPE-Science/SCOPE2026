# Source-selective dephasing optima for complete-bipartite excitation trapping

## Finding

For every two-sided complete-bipartite network \(K_{m,n}\) with \(m,n\geq2\), put a single irreversible trap in the part of size \(m\). An excitation is prepared at one nontrap vertex, with uniform hopping \(J>0\), trap population-loss rate \(\kappa>0\), and site-local Markovian dephasing damping every offdiagonal density-matrix entry at rate \(\gamma>0\). Define \(a=m-1\), \(b=n\), \(N=m+n\), and
\[
 C_N=\frac{N}{\kappa}+\frac{(N-1)\kappa}{4J^2b}.
\]
The unconditional mean time to capture (equivalently, mean integrated survival time) for a source in the trap's own part \(A\) is
\[
 T_A(\gamma)=C_N+\frac{(a-1)(N-2)}{2\gamma+\kappa}
 +\frac{a-1}{\gamma}+\frac{N\gamma}{2J^2b},
\]
and for a source in the opposite part \(B\) it is
\[
 T_B(\gamma)=C_N+\frac{a(N-2)}{2\gamma+\kappa}
 +\frac{b-1}{\gamma}+\frac{(N-1)\gamma}{2J^2b}.
\]
For every \(\gamma>0\), capture occurs with probability one. The \(B\)-source function is strictly convex and has one finite strictly positive optimal dephasing rate. The \(A\)-source function also has one strictly positive optimum when \(m\geq3\), but when \(m=2\) it is strictly increasing and the optimum is at the coherent boundary \(\gamma=0\); in that case capture remains certain.

The unique strictly positive optimizer is the root of
\[
 D_s=\frac{2A_s}{(2\gamma+\kappa)^2}+\frac{B_s}{\gamma^2},
\]
with \((A_A,B_A,D_A)=((a-1)(N-2),a-1,N/(2J^2b))\) and \((A_B,B_B,D_B)=(a(N-2),b-1,(N-1)/(2J^2b))\). For fixed \(a\geq2\), \(J>0\) and \(\kappa>0\), as \(b\to\infty\),
\[
 \frac{\gamma_A^*}{J\sqrt b}\to\sqrt{a-1},\qquad
 \frac{\gamma_B^*}{J\sqrt b}\to\sqrt{a+2},
\]
\[
 \frac{\min_{\gamma>0} T_A(\gamma)-C_N}{\sqrt b}\to\frac{\sqrt{a-1}}{J},\qquad
 \frac{\min_{\gamma>0} T_B(\gamma)-C_N}{\sqrt b}\to\frac{\sqrt{a+2}}{J}.
\]
For \(a=1\), the first formula for \(T_A\) reduces to \(C_N+N\gamma/(2J^2b)\), so the coherent optimum equals \(C_N\). The asymmetric source-specific square-root laws are part of the result, not a statement about finite-time mixing or transport efficiency in the presence of a competing bulk loss channel.

## Assumptions and scope

Let \(V=A\sqcup B\) with \(|A|=m\geq2\), \(|B|=n\geq2\), and choose a trap \(t\in A\). With \(\hbar=1\), the one-excitation Hamiltonian is the zero-diagonal adjacency operator
\[
 H=J\sum_{u\in A,v\in B}(|u\rangle\langle v|+|v\rangle\langle u|).
\]
The surviving, generally subnormalized density operator obeys
\[
 \dot\rho=-i[H,\rho]+\gamma\sum_{v\in V}
 \left(P_v\rho P_v-\tfrac12\{P_v,\rho\}\right)
 -\tfrac\kappa2\{P_t,\rho\},\quad P_v=|v\rangle\langle v|.
\]
There is **no other population-decay mechanism**, no site-energy detuning, and no coherent or correlated initial superposition. An initial pure local state on any nontrap site of either indicated part is permitted. The offdiagonal damping rate is exactly \(\gamma\), and \(\kappa\) is the loss rate of trap *population*. The mean time is \(T=\int_0^\infty\mathrm{tr}\rho(t)\,dt\), which is finite for \(\gamma>0\). Values at \(\gamma=0\) are used only for the proved finite boundary case \(a=1\) with an \(A\)-source. The result does not include a star with a singleton part and does not cover coherent sources delocalized over either part.

## Proof

**1. Certain capture and integrability.** For \(\gamma>0\), the finite-dimensional completely positive surviving evolution preserves positivity and decreases trace. Its squared Hilbert--Schmidt norm obeys
\[
 \frac{d}{dt}\operatorname{tr}(\rho^2)
 =-2\gamma\sum_{u\ne v}|\rho_{uv}|^2
 -2\kappa\sum_v|\rho_{tv}|^2.
\]
The largest invariant subset where this derivative vanishes consists of diagonal density matrices with zero entry at \(t\). For a diagonal matrix to remain diagonal under the Hamiltonian, its diagonal entries must coincide along every edge. Connectivity of \(K_{m,n}\) then forces all entries to be equal; the zero trap entry forces every entry to vanish. LaSalle's principle on the compact positive trace-at-most-one cone gives \(\rho(t)\to0\). Since the generator is finite dimensional and has no nonzero stationary or oscillatory invariant subspace, its surviving semigroup is exponentially stable; consequently all integrals used below exist, \(\int_0^\infty\kappa\rho_{tt}(t)dt=1\), and \(T\) equals the unconditional first-capture mean.

**2. Symmetry reduction.** Write \(a=m-1\) and \(b=n\). A source at any one vertex of a given nontrap part has the same mean as the *incoherent uniform mixture* of localized sources in that part: averaging over within-part permutations leaves the survival trace invariant. The averaged density matrices stay in the real eight-coordinate sector
\(p_t=\rho_{tt}\), \(p=\rho_{uu}\) for \(u\in A\setminus\{t\}\), \(q=\rho_{vv}\) for \(v\in B\), \(x=\rho_{tu}\), \(iy=\rho_{tv}\), \(iz=\rho_{uv}\), \(u_0=\rho_{uu'}\) for distinct nontrap \(A\)-sites, and \(v_0=\rho_{vv'}\) for distinct \(B\)-sites. Here \(x,u_0,v_0,y,z\) are real. If \(a=1\), omit the nonexistent \(u_0\) coordinate and every occurrence multiplied by \(a-1\). The exact reduced equations are
\[
\begin{aligned}
 \dot p_t&=-\kappa p_t-2Jby,&\dot p&=-2Jbz,&\dot q&=2J(y+az),\\
 \dot x&=-Jb(y+z)-(\gamma+\kappa/2)x,&
 \dot u_0&=-2Jbz-\gamma u_0,&
 \dot v_0&=2J(y+az)-\gamma v_0,\\
 \dot y&=J[p_t+ax-q-(b-1)v_0]-(\gamma+\kappa/2)y,\\
 \dot z&=J[x+p+(a-1)u_0-q-(b-1)v_0]-\gamma z.
\end{aligned}
\]
These follow entry-by-entry from the specified generator, with the trap damping affecting the trap population at \(\kappa\) and its coherences at \(\kappa/2\).

**3. Integrated equations and exact means.** Let upper-case letters denote time integrals of the corresponding lower-case coordinates. In both preparations, trace conservation with only the trap sink gives \(P_t=1/\kappa\) and integrating \(\dot p_t\) gives \(Y=-1/(2Jb)\). For initial \(B\)-mixture, \(p(0)=0\), \(q(0)=1/b\), the integrated system yields
\[
 Z=U_0=0,\quad X=\frac1{2\gamma+\kappa},\quad V_0=-\frac1{b\gamma},
\]
\[
 P=\frac1\kappa+\frac{a-1}{2\gamma+\kappa}+\frac{\gamma+\kappa/2}{2J^2b},\quad
 Q=\frac1\kappa+\frac a{2\gamma+\kappa}+\frac{b-1}{b\gamma}+\frac{\gamma+\kappa/2}{2J^2b}.
\]
For the initial \(A\setminus\{t\}\) mixture, \(p(0)=1/a\), \(q(0)=0\), the integrated system instead gives
\[
 Z=\frac1{2Jab},\quad X=\frac{a-1}{a(2\gamma+\kappa)},\quad V_0=0,
\]
\[
 Q=\frac1\kappa+aX+\frac{\gamma+\kappa/2}{2J^2b},\qquad
 P=Q-X+\frac{a-1}{a\gamma}+\frac\gamma{2J^2ab}.
\]
For \(a>1\), additionally \(U_0=-1/(a\gamma)\); when \(a=1\), that variable is absent. Substituting into \(T=P_t+aP+bQ\), and collecting the part-independent terms, yields the two displayed formulas exactly.

**4. Optimality and boundary.** Both formulas take the form \(T_s=C_N+A_s/(2\gamma+\kappa)+B_s/\gamma+D_s\gamma\). For \(\gamma>0\),
\[
 T_s'=D_s-\frac{2A_s}{(2\gamma+\kappa)^2}-\frac{B_s}{\gamma^2},\quad
 T_s''=\frac{8A_s}{(2\gamma+\kappa)^3}+\frac{2B_s}{\gamma^3}.
\]
In the stated two-sided family \(b\ge2\), \(B_B=b-1>0\), so the \(B\)-source derivative increases strictly from \(-\infty\) to \(D_B>0\) and has one root, the global minimum. When \(a\ge2\) the same proof applies for \(A\). When \(a=1\), \(A_A=B_A=0\) and \(T_A=C_N+D_A\gamma\) is strictly increasing. At \(\gamma=0\) with \(a=1\), the initial lone nontrap \(A\)-vertex belongs to the three-dimensional invariant Hilbert space spanned by the trap, that nontrap vertex, and the uniform sum over \(B\). This reachable subspace has no Hamiltonian eigenvector orthogonal to the trap: the zero trap entry of an eigenvector forces its uniform \(B\) entry to vanish (by the trap component of the eigenvalue equation), and then its nontrap \(A\) entry to vanish (by the uniform \(B\) equation). Additional zero-sum \(B\)-eigenvectors in the *full* Hilbert space are dark but orthogonal to this initial state and do not affect its capture. Hence the coherent dissipative generator is stable on the reachable sector, and the continuous limit \(T_A(0)=C_N\) is the actual coherent mean.

**5. Large opposite-part size.** Hold \(a,J,\kappa\) fixed and let \(b\to\infty\). For \(\gamma=x\sqrt b\) with fixed \(x>0\), the first and second derivatives and the excess objective converge uniformly on compact \(x\)-intervals. Explicitly,
\[
 \frac{T_A(x\sqrt b)-C_N}{\sqrt b}\to\frac{a-1}{2x}+\frac{x}{2J^2}
\]
for \(a\ge2\), and
\[
 \frac{T_B(x\sqrt b)-C_N}{\sqrt b}\to\frac{a+2}{2x}+\frac{x}{2J^2}.
\]
The positive minimizers of these strictly convex limits are respectively \(x=J\sqrt{a-1}\) and \(x=J\sqrt{a+2}\). To justify convergence of minimizers, insert \(\gamma=x\sqrt b\) into the *exact* derivative equations. The right-hand sides are strictly decreasing in \(x>0\), tend to infinity at zero and to zero at infinity, while their left-hand sides tend to \(1/(2J^2)\). A pair of fixed positive bounds therefore brackets each unique root, and every subsequential limit solves the corresponding unique limiting equation. Evaluating the objective at the roots proves the two excess limits. This also establishes that these \(\sqrt b\) corrections are distinct even though the common baseline \(C_N\) is of order \(b\).

## Verification

The standalone checker `verify.py` constructs the *unreduced* \(N^2\)-dimensional complex Lindblad linear system, solves its integrated-density equation by direct complex Gaussian elimination, and compares the resulting trace against both formulas. It also independently tests uniqueness of the derivative root, source asymmetry and the large-\(b\) constants. Run `python verify.py` from the directory containing this manuscript. On the packaged code, 106 finite-matrix, optimization, and asymptotic checks passed. The finite calculations are evidence for implementation and normalization; the statements for every size and the limiting laws follow from the five proof steps above.

## Relationship to prior work

The general phenomenon of dephasing-assisted exciton transport is established in the work of Plenio and Huelga (2008), Caruso and collaborators (2009), and Kassal and Aspuru-Guzik (2012). The latter analyzes Markovian dephasing on ordered chains and rings, not the two-part complete-bipartite family. Caruso and collaborators and the later exact complete-network analysis of Alterman, Berman and Strauch concern fully connected graphs with edges *within* every class, while the present model deletes all intrapart edges. Their universal Liouvillian or resolvent methods motivate the derivation but do not supply the present two-part formula, source-dependent boundary, or \(\sqrt b\)-optimum constants. Previously calculated star-network examples correspond to a singleton bipartite side and are **excluded** here; those examples are not claimed as new. No priority or independence claim beyond the examined comparisons is asserted.

## Limitations

The transport objective is mean first capture with no competing bulk recombination. The model assumes uniform hopping, dephasing and site energies; asymmetric site energies or coherent initial superpositions need different reductions. The result does not imply a finite-time mixing bound, robustness to disorder, or optimization of an externally lossy transfer *efficiency*. Historical priority remains provisional: a relevant early 2004 Haken--Strobl connectivity paper was bibliographically identified, but its primary full text could not be examined; an equivalent unindexed calculation cannot be excluded. Independent scientific validation has not been performed.

## References

1. M. B. Plenio and S. F. Huelga, *Dephasing-assisted transport: quantum networks and biomolecules* (2008), arXiv:0807.4902, https://arxiv.org/abs/0807.4902.
2. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: the fundamental role of noise-assisted transport* (2009), arXiv:0901.4454, https://arxiv.org/abs/0901.4454.
3. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems* (first posted 2012-01-25), arXiv:1201.5202, https://arxiv.org/html/1201.5202v2.
4. S. Alterman, J. Berman and F. W. Strauch, *Optimal conditions for environment-assisted quantum transport on the fully connected network* (2023 preprint; 2024 journal), arXiv:2309.00164, https://arxiv.org/abs/2309.00164.
5. K. M. Gaab and C. J. Bardeen, *The effects of connectivity, coherence, and trapping on energy transfer in simple light-harvesting systems studied using the Haken--Strobl model with diagonal disorder*, *J. Chem. Phys.* 121 (2004) 7813--7820, https://doi.org/10.1063/1.1786922 (priority risk; full text not inspected).
