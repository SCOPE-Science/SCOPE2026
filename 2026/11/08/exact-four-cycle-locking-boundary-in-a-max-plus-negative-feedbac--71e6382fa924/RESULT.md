# Exact four-cycle locking boundary in a max-plus negative-feedback map

## Finding

For the normalized finite-step max-plus negative-feedback map
\[
 F_t(x,y)=\left(\max\{x-t,y\},\ \max\{y+1-t,1-\max(0,2x)\}\right),\qquad \frac32<t<2,
\]
let \(N_4(t)\) be the number of distinct primitive periodic orbits of least period four. Then
\[
 N_4(t)=\begin{cases}0&3/2<t<5/3,\\1&t=5/3,\\2&5/3<t<2.\end{cases}
\]
The two cycles for \(5/3<t<2\) are, with each displayed ordered quadruple interpreted cyclically,
\[
\begin{aligned}
\mathcal A_t={}&((2-t,3-2t),(3-2t,2t-3),(2t-3,1),(1,2-t)),\\
\mathcal U_t={}&((1/3,4/3-t),(4/3-t,1/3),(1/3,1),(1,1/3)).
\end{aligned}
\]
The four-step derivative matrices at the indicated initial states are respectively
\[
 D F_t^4(2-t,3-2t)=\begin{pmatrix}0&0\\0&0\end{pmatrix},\qquad
 D F_t^4(1/3,4/3-t)=\begin{pmatrix}4&0\\4&0\end{pmatrix}.
\]
Thus \(\mathcal A_t\) is locally superattracting (the fourth iterate has zero derivative), whereas \(\mathcal U_t\) is unstable in one direction, with return eigenvalues \(4\) and \(0\). At \(t=5/3\) the two cycles coalesce into the one primitive cycle \(((1/3,-1/3),(-1/3,1/3),(1/3,1),(1,1/3))\), which meets a switching boundary. No differentiability of the return map is asserted at the collision.

## Assumptions and scope

The state space is the entire real plane, not a prescribed trapping rectangle. The map is continuous and piecewise affine. Parameters are real and satisfy the strict interval \(3/2<t<2\); the value \(t=5/3\) is included. The period-four count is global: it includes every real initial state, not just points in an observed basin. The rescaling of the unnormalized model from Yamazaki and Ohmori, Eq. (8), uses \(m=2\), \(B>0\), \(T=tB\), \(x=X/B\), and \(y=Y/B\). Their max-plus formula has a separate parameter \(T\) for the logarithm of the discretization step; it is not the parameter called \(T\) in the distinct generalized oscillator of Ohmori and Yamazaki (2024).

## Proof

**1. Global bounds for periodic states.** Consider any orbit of period dividing four. Let \(M_y\) and \(M_x\) be the maximum of its second and first coordinates, respectively. Since \(y'\le\max\{y+1-t,1\}\) and \(t>1\), a periodic maximum \(M_y>1\) is impossible. Thus \(M_y\le1\). Similarly \(x'\le\max\{x-t,y\}\) forces \(M_x\le M_y\le1\). Therefore \(y'\ge 1-\max(0,2x)\ge-1\), whence \(y\ge-1\) at all orbit states; \(x'\ge y\) then gives \(x\ge-1\). Every period-four orbit is contained in \([-1,1]^2\).

**2. No first-coordinate self-delay on a four-cycle.** Suppose a point \((x,y)\) in such an orbit satisfies \(x-t\ge y\), so that its next first coordinate is \(u=x-t\). Because \(y\ge-1\), we have \(x\ge t-1>1/2\). Thus \(u<0\), and the next second coordinate \(v=\max\{y+1-t,1-2x\}\) is strictly negative. Applying the map successively gives
\[
(x,y)\longmapsto(u,v)\longmapsto(v,1)\longmapsto(1,1)\longmapsto(1,2-t).
\]
The second arrow follows from \(u-t<-1\le v\), the third from \(v<0\), and the fourth from \(t<2\). A four-cycle would therefore require \(y=2-t>0\), contradicting \(y\le x-t<0\). Hence the branch \(x-t\ge y\) never occurs on a period-four orbit. We conclude \(x'=y\) at every state of any such orbit.

**3. Exact scalar branch reduction.** Write successive first coordinates \(a_k\), with indices modulo four. The planar state is \((a_k,a_{k+1})\), and
\[
 a_{k+2}=\max\{a_{k+1}+1-t,1-\max(0,2a_k)\}.
\]
Each step has one of three exhaustive (possibly boundary-overlapping) affine modes:
\[
\begin{array}{c|c|l}
\text{mode}&\text{equation}&\text{inequalities}\\\hline
D&a_{k+2}=a_{k+1}+1-t&a_k\ge0,\quad 2a_k+a_{k+1}-t\ge0\\
S&a_{k+2}=1&a_k\le0,\quad a_{k+1}\le t\\
H&a_{k+2}=1-2a_k&a_k\ge0,\quad 2a_k+a_{k+1}-t\le0.
\end{array}
\]
When \(a_k<0\), the \(D\) mode cannot dominate because \(a_{k+1}\le1<t\); hence these modes cover all possibilities. Also impose the proven bounds \(-1\le a_k\le1\).

**4. Exhaustive parametric elimination.** There are exactly \(3^4=81\) mode words. For each word, its four affine equations are a linear system in the four unknowns \(a_0,a_1,a_2,a_3\), with right-hand sides affine in \(t\). The coefficient matrix is nonsingular for every word other than \(DDDD\). That singular word is inconsistent when \(t>1\): summing its four equations yields \(0=4(1-t)\). For each of the other 80 words, rational Gaussian elimination produces four rational affine functions of \(t\). Intersecting the resulting exact rational linear inequalities, including \(-1\le a_k\le1\), with \(3/2<t<2\) gives *precisely* the following feasible words:

| Mode words | Feasible parameters | Scalar cycle |
|---|---|---|
| `HHHH` | \(3/2<t<2\) | \((1/3,1/3,1/3,1/3)\) |
| `HSDD` and its three cyclic rotations | \(5/3\le t<2\) | \((2-t,3-2t,2t-3,1)\) up to cyclic rotation |
| `HSHD` and its three cyclic rotations | \(5/3\le t<2\) | \((1/3,4/3-t,1/3,1)\) up to cyclic rotation |

For a transparent fully exhaustive certificate, the accompanying standard-library-only program `check_exact_phase.py` constructs all 81 systems, solves the nonsingular ones with `fractions.Fraction`, intersects all symbolic affine inequalities and confirms exactly the nine feasible words above. It also reconstructs each physical orbit by direct iteration of the original planar map. This is an exhaustive finite algebraic branch classification **for every real parameter in the stated interval**, not numerical parameter sampling.

The `HHHH` word yields the only period-one state (and no nontrivial period-two state). For \(t>5/3\), the other eight words represent exactly two inequivalent primitive four-cycles. At \(t=5/3\) those cycles coincide and remain primitive. Below that threshold no primitive four-cycle exists.

**5. Return spectra.** On a strict \(H,S,D\) branch, the Jacobian is respectively
\[
 J_H=\begin{pmatrix}0&1\\-2&0\end{pmatrix},\qquad
 J_S=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 J_D=\begin{pmatrix}0&1\\0&1\end{pmatrix}.
\]
The two strict four-cycle words `HSDD` and `HSHD` have ordered products \(J_DJ_DJ_SJ_H=0\) and \(J_DJ_HJ_SJ_H=\begin{psmallmatrix}4&0\\4&0\end{psmallmatrix}\). Their spectra give the claimed local stability statements. At the collision, one of the branches is tied and this smooth Jacobian argument is intentionally not applied.

## Verification

Run `python3 check_exact_phase.py` with Python 3.9 or newer. The checker uses only the Python standard library. It verifies exact rational elimination for all 81 words, rejects the sole singular word, verifies the nine feasible mode words and their entire symbolic parameter ranges, checks the primitive orbit count on both sides and at the boundary, and reproduces both four-step return matrices. Representative parameter evaluations are auxiliary consistency checks; the completeness certificate is the exact symbolic elimination across all possible mode words.

## Relationship to prior work

Yamazaki and Ohmori (2023, arXiv:2306.00733, published as *Progress of Theoretical and Experimental Physics* 081A01) explicitly give the unnormalized max-plus negative-feedback map as their Eq. (8) and report numerical four-state locking and an apparent bifurcation. Their numerical observations do not establish the precise universal threshold, exhaustive count of primitive four-cycles, or parameter-independent exact return spectra in the stated interval. This result makes those particular assertions exact and global. The bifurcation of the piecewise-affine max-plus map is a switching-border collision, not the smooth saddle-node mechanism of the paper's separate differentiable finite-discretization model. The numerical smooth threshold must not be identified with this theorem's exact max-plus threshold.

Ohmori and Yamazaki (2023, arXiv:2305.05908) derive a simpler max-plus limit obtained after taking the discretization step to infinity, corresponding to dropping the finite-step competition term. Ohmori and Yamazaki (2024, arXiv:2402.06230) examine another generalized two-dimensional max-plus oscillator \(X'=Y+\max(0,TX)\), \(Y'=B-\max(0,DX)\); its formula differs from the finite-step map considered here. Gibo and Ito (2015) originate the underlying tropical negative-feedback discretization and its oscillatory mechanism, but their full 2015 article could not be inspected; it remains a residual priority risk.

## Limitations

The theorem classifies least period four only, in \(3/2<t<2\); it makes no claim about all higher-period dynamics, global basins, or other parameter regions. At \(t=5/3\), a classical smooth Floquet multiplier is not asserted because the orbit lies on a switching line. Generality in the Hill exponent beyond \(m=2\) and persistence under smoothing are unproved. Independent mathematical validation is not yet available. Older or unindexed sources could contain equivalent results.

## References

1. Y. Yamazaki and S. Ohmori, *Emergence of ultradiscrete states due to phase lock caused by saddle-node bifurcation in discrete limit cycles*, arXiv:2306.00733 (first publicly posted 2023-06-02); *Prog. Theor. Exp. Phys.* 2023, 081A01 (2023), DOI: 10.1093/ptep/ptad099. https://arxiv.org/abs/2306.00733
2. S. Ohmori and Y. Yamazaki, *Dynamical properties of discrete negative feedback models*, arXiv:2305.05908 (2023). https://arxiv.org/abs/2305.05908
3. S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230 (2024). https://arxiv.org/abs/2402.06230
4. S. Gibo and H. Ito, *Discrete and ultradiscrete models for biological rhythms comprising a simple negative feedback loop*, *J. Theor. Biol.* 378 (2015), 89–95, DOI: 10.1016/j.jtbi.2015.04.024 (full text not inspected).
