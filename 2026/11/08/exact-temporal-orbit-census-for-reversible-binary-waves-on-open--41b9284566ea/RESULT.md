# Exact temporal orbit census for reversible binary waves on open paths

## Finding

Consider a binary, two-time-level wave automaton on a path of \(n\ge 2\) sites with fixed-zero boundary values. Let \(F_n\) update the pair of rows \((u(t),u(t-1))\) to \((u(t+1),u(t))\), where
\[
u_i(t+1)=u_{i-1}(t)+u_{i+1}(t)+u_i(t-1)\pmod 2,
\qquad u_0(t)=u_{n+1}(t)=0.
\]
For positive integers \(t\), put \(q=n+1=2^a u\) and \(t=2^b v\), with \(u,v\) odd, and \(h=\gcd(u,v)\). Define
\[
D_n(t)=(h-1)\min\{2^{a+1},2^b\}+\min\{2^{a+1}-2,2^b\}.
\]
Then the **complete temporal fixed-point census** is
\[
\boxed{\#\operatorname{Fix}(F_n^t)=2^{D_n(t)}\quad(n\ge2,\ t\ge1).}
\]
Every configuration is periodic from time zero, and the permutation order of \(F_n\) is **exactly** \(2(n+1)\). For each positive divisor \(s\mid 2(n+1)\), the population \(P_n(s)\) of states of **least** period \(s\), and the number \(O_n(s)\) of primitive cycles of length \(s\), are
\[
P_n(s)=\sum_{d\mid s}\mu(s/d)2^{D_n(d)},\qquad O_n(s)=P_n(s)/s.
\]
The counts vanish for temporal periods not dividing \(2(n+1)\). This also determines the dynamical zeta function \(\exp(\sum_{t\ge1}\#\operatorname{Fix}(F_n^t)z^t/t)\), equivalently the product over primitive cycles.

## Assumptions and scope

The site alphabet is precisely \(\mathbb F_2\). All sites are labelled, with **open Dirichlet** rather than periodic or reflecting spatial boundaries. The state is the *ordered pair* of consecutive time rows; counting one row alone would lose reversibility. Let \(A_n\) be the adjacency matrix of the path on \(n\) vertices over \(\mathbb F_2\). Then
\[
M_n=\begin{pmatrix}A_n&I_n\\ I_n&0\end{pmatrix}
\]
represents \(F_n\) on \(\mathbb F_2^{2n}\). A state of least period \(s\) satisfies \(M_n^s w=w\) and no earlier positive iterate fixes it. All assertions quantify over every integer \(n\ge2\) and every integer \(t\ge1\).

## Proof

**1. Reversibility.** From the next-row/current-row pair \((v,u)\), one recovers the preceding row as \(v+A_nu\). Thus \(M_n\) is invertible and every finite state is periodic without any transient.

**2. Characteristic polynomial.** Let \(p_j(Y)=\det(YI_j-A_j)\) and \(p_0=1\). The tridiagonal determinant recurrence in characteristic two is \(p_j(Y)=Yp_{j-1}(Y)+p_{j-2}(Y)\), with \(p_1(Y)=Y\). For an indeterminate \(X\), the Schur-complement identity gives
\[
\chi_n(X)=\det(XI_{2n}-M_n)=X^np_n(X+X^{-1}).
\]
Set \(r_j(X)=X^jp_j(X+X^{-1})\). The recurrence becomes
\[
r_0=1,\quad r_1=X^2+1,\quad
r_j=(X^2+1)r_{j-1}+X^2r_{j-2}.
\]
Induction identifies \(r_j=1+X^2+\cdots+X^{2j}\). In particular
\[
\boxed{\chi_n(X)=(1+X+\cdots+X^n)^2=\frac{(X^{n+1}+1)^2}{(X+1)^2}.}
\]
The quotient is a polynomial identity in characteristic two; the displayed rational form should be read after cancellation.

**3. Cyclicity.** Work temporarily over an algebraic closure of \(\mathbb F_2\). A nonzero eigenvector \((v,w)\) of \(M_n\) of eigenvalue \(\lambda\) satisfies \(w=\lambda^{-1}v\), where \(v\) is an eigenvector of \(A_n\) with eigenvalue \(\lambda+\lambda^{-1}\). Each eigenspace of \(A_n\) is **exactly one-dimensional**: writing \(v_0=0\), the recurrence \(v_{i+1}=\alpha v_i+v_{i-1}\) forces every component from \(v_1\), and an eigenvalue supplies a nonzero solution. Hence every eigenvalue of \(M_n\) has geometric multiplicity one, so its Jordan decomposition has exactly one block per distinct eigenvalue. Consequently the minimal and characteristic polynomials coincide and \(M_n\) is a cyclic linear operator.

**4. Kernel dimension.** If a cyclic matrix has characteristic polynomial \(c(X)\), its underlying module is \(\mathbb F_2[X]/(c(X))\). The kernel of multiplication by \(f(X)\) has dimension \(\deg\gcd(c,f)\); this follows directly by writing \(c=g c_1\), \(f=g f_1\) with \(\gcd(c_1,f_1)=1\), and observing that \(c\mid fz\) precisely when \(c_1\mid z\). Thus
\[
\dim_{\mathbb F_2}\ker(M_n^t-I)=\deg\gcd(\chi_n(X),X^t+1).
\]
Write \(n+1=2^a u\) with odd \(u\). In an algebraic closure, \(\chi_n\) has multiplicity \(2^{a+1}\) at each nontrivial \(u\)-th root of unity and multiplicity \(2^{a+1}-2\) at \(1\); the latter is zero when \(a=0\). Also \(X^t+1=(X^v+1)^{2^b}\) for odd \(v\), with multiplicity \(2^b\) at each \(v\)-th root of unity. Exactly \(h=\gcd(u,v)\) common roots occur, one of them \(1\). Taking minimum multiplicities proves that the kernel dimension is \(D_n(t)\), and the fixed-point count is \(2^{D_n(t)}\).

**5. Exact order and least periods.** The characteristic polynomial divides \(X^{2(n+1)}+1\); cyclicity proves \(M_n^{2(n+1)}=I\). If \(u>1\), a primitive \(u\)-th root of unity occurs with a Jordan block of size \(2^{a+1}\), whose multiplicative order is \(u2^{a+1}=2(n+1)\). If \(u=1\), the hypothesis \(n\ge2\) forces \(a\ge2\); the single Jordan block at eigenvalue \(1\) has size \(2^{a+1}-2\), strictly greater than \(2^a\), hence has order \(2^{a+1}=2(n+1)\). This proves the exact global order. Möbius inversion on the divisor lattice gives the least-period and primitive-cycle formulas claimed above. No state can have a period outside the divisor set.

## Verification

Two self-contained, standard-library Python programs are included. `direct_matrix_check.py` constructs the exact binary matrix and computes ranks of \(M_n^t-I\); it found agreement in 1,116 cases for \(2\le n\le32\) and \(1\le t\le2(n+1)\), and checked exact matrix order for all 31 sizes. `orbit_enumeration_check.py` independently iterates and classifies all \(2^{2n}\) states for each \(2\le n\le8\), comparing temporal fixed points and primitive orbits in 33 divisor cases. Their captured outputs accompany the programs; run either file using a standard Python 3 interpreter. The infinite theorem follows from the proof above, not from extrapolation.

## Relationship to prior work

Macfarlane [1] develops reversible second-order binary cellular automata using matrix representations and analyzes weights of single-seed evolutions, including related rules on half-infinite or bi-infinite arrays. That method and the concept of reversing a two-time-level rule are prior work. Its displayed RCA3 rule **also includes the present-time center cell** and is not the same local rule. The present finding instead determines the **full, finite open-path orbit-count distribution for arbitrary paired initial rows**. Tadaki [2], including its discussion of the earlier 1993 rule-90 Dirichlet case, analyzes orbits of **first-order** finite linear automata; its update is \(u(t+1)=A_nu(t)\) and can exhibit transient relaxation, whereas the present paired-row update is invertible. Bhattacharjee and Das [3] examine finite first-order automata with periodic boundaries, not this open-boundary reversible wave permutation. These sources do not assert the displayed all-size fixed-point formula or its primitive-orbit inversion. The formula may nevertheless be derivable from well-established cyclic-module techniques, and undiscovered equivalent statements are a priority risk.

## Limitations

The claim concerns \(\mathbb F_2\), open paths, and the specific neighbor-only second-order rule. It makes no assertion for periodic spatial boundaries, higher alphabets, or center-coupled variants. The exact formula is mathematically proved and finite checks are corroborative. The closest primary paper uses a different local rule and different initial-state/question regime. The historical literature search cannot exclude every unindexed equivalent formulation. No independent audit has been performed.

## References

[1] A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General **37** (2004), 10791–10814, DOI: 10.1088/0305-4470/37/45/006. First published 2004-10-28. Full text: https://www.electronicsandbooks.com/edt/manual/Magazine/J/Journal%20of%20Physics%20A%20Mathematical%20and%20Theoretical/2004%20Volume%2037/0305-4470_37_45_006.pdf

[2] S. Tadaki, *Orbits in one-dimensional finite linear cellular automata*, arXiv:cond-mat/9305012v1 (first public version 1993-05-14); Physical Review E **49** (1994), 1168–1173, DOI: 10.1103/PhysRevE.49.1168. https://arxiv.org/abs/cond-mat/9305012

[3] K. Bhattacharjee and S. Das, *Reversibility of d-State Finite Cellular Automata*, arXiv:1502.01187 (first version 2015-02-04). https://arxiv.org/abs/1502.01187
