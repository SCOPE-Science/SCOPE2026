# Exact nonbinary three-cap Hamming negative type and its critical Fourier layer

## Finding
For integers \(q\ge3\) and \(n\ge4\), equip the finite abelian group \(G=(\mathbb Z/q\mathbb Z)^n\) with
\[
 d(x,y)=\min\{\operatorname{wt}(x-y),3\},
\]
where weight counts nonzero coordinates. Put
\[
 k=\left\lfloor\frac{(q-1)n+3}{q}\right\rfloor
 =n-\left\lceil\frac{n-3}{q}\right\rceil,\quad
 t=(q-1)n-qk,\quad
 u=\frac{t^2-(q-2)t-n(q-1)}2.
\]
There is a unique \(\beta_{n,q}\in(0,1)\) satisfying
\[
 -3^{\beta_{n,q}}+(1-3^{\beta_{n,q}})t
 +(2^{\beta_{n,q}}-3^{\beta_{n,q}})u=0.
\]
For every real \(p>0\), \(d^p\) is conditionally negative definite if and only if \(0<p\le\beta_{n,q}\). It is strictly conditionally negative definite when \(0<p<\beta_{n,q}\). At the endpoint its entire centered nullspace is the Fourier-character layer of weight \(k\), of dimension
\[
 M_{n,q}=\binom nk(q-1)^k.
\]
Thus the minimum Euclidean embedding dimension of \((G,d^{p/2})\) is \(q^n-1\) below the threshold and \(q^n-1-M_{n,q}\) at the threshold; no isometric Hilbert embedding exists for the powered distances above it. Equivalently, \(\exp(-s d(x,y)^p)\) is positive semidefinite for every \(s>0\) exactly in this range.

There are two distinct sharp asymptotic regimes:
\[
 \lim_{n\to\infty}n\beta_{n,q}
 =\frac{2}{(q-1)\log(3/2)}\quad(q\ge3\text{ fixed}),
\]
\[
 \lim_{q\to\infty}q\beta_{n,q}
 =\frac1{(n-2)\log3-(n-1)\log2}\quad(n\ge4\text{ fixed}).
\]
Here the second limit runs through arbitrary integers \(q\), not just prime powers. No joint limit in both parameters is claimed.

## Assumptions and scope
The metric is capped at distance three, not the original Hamming distance or a graph-power shortest-path distance. The coordinate alphabet is the cyclic group of arbitrary integer order \(q\ge3\); a field structure is neither assumed nor used. A kernel \(d^p\) is conditionally negative definite (CND) when, for every real vector \((c_x)_{x\in G}\) with \(\sum_xc_x=0\),
\[\sum_{x,y\in G}c_xc_y d(x,y)^p\le0.\]
Strict CND means strict inequality for every nonzero such vector. The convention at \(x=y\) is \(d(x,x)^p=0\) for \(p>0\). All Fourier transforms are unnormalized sums and all character levels include all characters with exactly the stated number of nontrivial coordinates. Dimension is over the real numbers for centered metric Gram matrices.

## Proof
**1. Complete character spectrum.** Fix a nontrivial character \(\chi\) with exactly \(j\in\{1,\ldots,n\}\) nontrivial coordinate factors. The character sums over weight-one and weight-two vectors are respectively
\[
 T_j=(q-1)n-qj,
 \qquad U_j=\binom{n-j}{2}(q-1)^2-j(n-j)(q-1)+\binom j2.
\]
These follow by choosing zero, one, or two of the nontrivial character coordinates, each of whose nonzero-coordinate character sum is \(-1\). Elementary expansion gives
\[
 U_j=\frac{T_j^2-(q-2)T_j-n(q-1)}2.
\]
Since the unnormalized sum of \(\chi\) over \(G\) is zero, the sum over vectors of weight at least three is \(-1-T_j-U_j\). Therefore the \(p\)-distance matrix has eigenvalue
\[
 \lambda_j(p)=T_j+2^pU_j+3^p(-1-T_j-U_j)
 =-3^p+(1-3^p)T_j+(2^p-3^p)U_j
\]
on that layer. Its real multiplicity is \(\binom nj(q-1)^j\), because conjugate characters have the same real eigenvalue. The constant character has a strictly positive eigenvalue for \(p>0\). Thus CND is equivalent to \(\lambda_j(p)\le0\) for every \(j\ge1\).

**2. A universal critical degree.** For \(0<p<1\), regard the preceding expression as a quadratic in \(T\). Its leading coefficient \((2^p-3^p)/2\) is strictly negative, so its real maximum occurs at
\[
 T_* =\frac{q-2}{2}-R(p),\qquad R(p)=\frac{3^p-1}{3^p-2^p}.
\]
Strict concavity of \(v\mapsto v^p\) on \((0,\infty)\), applied at \(1,2,3\), gives \(1+3^p<2^{p+1}\), equivalently \(R(p)>2\). Also \(R(p)<3\), because \(2\cdot3^p-3\cdot2^p+1>0\): the latter vanishes at zero and its derivative is \(2^p[2(3/2)^p\log3-3\log2]>0\), using \(2\log3>3\log2\). Hence \(2<R(p)<3\).

The allowed values \(T_j=(q-1)n-qj\) form a lattice with step \(q\). The closest one to \(T_*\) has index
\[
 \left\lfloor\frac{(q-1)n+1+R(p)}q\right\rfloor
 =\left\lfloor\frac{(q-1)n+3}q\right\rfloor=k.
\]
The equality holds because \(1+R(p)\in(3,4)\), and the numerator preceding it is an integer plus a number strictly between zero and one. No tie is possible. For \(n\ge4\), \(1\le k\le n-1\), so \(\lambda_k(p)>\lambda_j(p)\) for all \(j\ne k\) and all \(0<p<1\).

**3. Sharp exponent and nullity.** At \(p=0\), interpreted as the off-diagonal indicator limit, all nonconstant eigenvalues equal \(-1\). At \(p=1\), the four-coordinate capped Hamming metric fails CND: in dimension four its character layer \(j=3\) has eigenvalue \(q-1>0\), by direct substitution in the formula. Every dimension \(n\ge4\) contains an isometric four-coordinate copy, so it too fails CND at \(p=1\). Continuity and the strict maximum above show that \(\lambda_k\) has a zero inside \((0,1)\).

The interval property of negative type says that CND at one positive exponent implies CND at every smaller positive exponent. Its strict form for finite metric spaces says that CND at exponent \(b>0\) implies strict CND for every exponent in \((0,b)\) (see Sánchez, Theorem 2.2, citing Li–Weston). Since \(\lambda_k\) strictly dominates all nonconstant eigenvalues throughout \((0,1)\), these facts prove that its zero in this interval is unique, that CND holds precisely up to that zero, and that all other nonconstant eigenvalues remain strictly negative at the zero. The same interval property rules out CND for every \(p>1\).

Centering the powered distance matrix gives the Euclidean Gram matrix \(-\tfrac12 JD_pJ\) with \(J=I-q^{-n}\mathbf1\mathbf1^T\). Its rank is the number of strictly negative nonconstant Fourier eigenvalues, proving both exact embedding dimensions. The characterization of all-time Gaussian positive definiteness is Schoenberg's equivalence for CND kernels.

**4. Two different limits.** For fixed \(q\), the arithmetic formula for \(k\) gives \(-3\le t\le q-4\), hence \(t=O_q(1)\) and \(u=-n(q-1)/2+O_q(1)\). Uniformly for \(c\) in compact subsets of \([0,\infty)\), substitution of \(p=c/n\) gives
\[
 \lambda_k(c/n)=-1+\frac{c(q-1)}2\log(3/2)+O_q(n^{-1}).
\]
Values of \(c\) on either side of the displayed limiting zero bracket the unique root, yielding the first limit.

For fixed \(n\ge4\) and all sufficiently large \(q\), one has \(k=n-1\), \(t=q-n\), and \(u=-(n-1)q+n(n-1)/2\). Substitution of \(p=c/q\) instead gives
\[
 \lambda_k(c/q)=-1+c[(n-2)\log3-(n-1)\log2]+O_n(q^{-1}).
\]
The coefficient is positive for \(n\ge4\), since at \(n=4\) it is \(\log(9/8)>0\) and it increases by \(\log(3/2)\) with \(n\). Bracketing the unique zero yields the second limit.

## Verification
A standalone Python 3 checker, `check.py`, computes the weight-one and weight-two character sums independently from their binomial expressions; it also directly enumerates **all group elements** for twelve cases on cyclic alphabets \(q=3,4,5\) and dimensions four and five, comparing their Fourier character sums at three powers. It tests 144 additional \((n,q)\) parameter cases, all critical-layer inequalities at multiple powers, endpoint signs, and both asymptotic regimes. Its success marker is `QARY_CAP3_INDEPENDENT_FOURIER_CHECKS_PASS`. The direct enumeration is finite and supports, but does not replace, the general argument in the proof. Reproduce by running `python3 check.py` alongside this file with Python 3 and the standard library; no network connection or external package is needed.

For example, when \((q,n)=(3,4)\), the critical equation simplifies to \(3(3^\beta-2^\beta)=1\) and gives \(\beta\approx0.5165843743\). For \((q,n)=(4,5)\), it is \(6(3^\beta-2^\beta)=1\), giving \(\beta\approx0.3109130949\). These approximations are not used as premises.

## Relationship to prior work
Sánchez (2011, arXiv:1108.0451v1) and Murugan (2011, arXiv:1112.5657v1) provide general finite-metric negative-type and vertex-transitive spectral criteria. Classical Hamming-scheme diagonalization supplies the Krawtchouk character sums; Brouwer–Cioabă–Ihringer–McGinnis (2018) study extremal eigenvalues of individual Hamming distance-relation graphs. The theorem here concerns a different *powered capped-distance combination* of those relations; it determines the exact maximizing character layer for every exponent before the threshold, and resolves the corresponding sharp exponent and endpoint multiplicity across all nonbinary alphabet sizes.

## Limitations
The exact threshold statement assumes \(q\ge3\), \(n\ge4\). It does not claim a mixed joint asymptotic when \(n\) and \(q\) both diverge, or results for caps other than three. The original full text of Deza–Maehara (1990), concerning general metric transforms, was not inspected completely; a specialized earlier theorem or an unlocated consequence of general association-scheme theory could overlap with this result. No historical-priority certification or independent validation is claimed.

## References
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (first public version 2011-08-02), https://arxiv.org/abs/1108.0451.
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (2011-12-23), https://arxiv.org/abs/1112.5657.
- A. E. Brouwer, S. M. Cioabă, F. Ihringer, M. McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, J. Combin. Theory Ser. B 133 (2018), 88–121, https://doi.org/10.1016/j.jctb.2018.04.005.
- P. Delsarte, *An algebraic approach to the association schemes of coding theory*, Philips Research Reports Supplements 10 (1973), standard Hamming eigenmatrix background.
- M. Deza, H. Maehara, *Metric transforms and Euclidean embeddings*, Trans. Amer. Math. Soc. 317 (1990), 661–671, https://doi.org/10.1090/S0002-9947-1990-0974513-6 (historical-comparison risk; original full text not inspected).
