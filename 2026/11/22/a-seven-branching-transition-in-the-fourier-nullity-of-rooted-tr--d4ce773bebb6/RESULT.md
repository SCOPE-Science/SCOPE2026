# A seven-branching transition in the Fourier nullity of rooted-tree order ideals

## Finding

Fix an integer \(d\ge2\). Let \(T_{d,h}\) be the complete rooted \(d\)-ary tree of height \(h\ge0\), with root at depth zero, and let \(N_{d,h}=(d^{h+1}-1)/(d-1)\). Regard its vertices as a poset with every ancestor below its descendants. In the binary group \(G_{d,h}=(\mathbb F_2)^{N_{d,h}}\), let \(f_{d,h}\) be the indicator of the incidence vectors of **all** order ideals, including the empty ideal. Let \(T_{f_{d,h}}\) be unnormalized counting convolution by \(f_{d,h}\) on complex-valued functions on \(G_{d,h}\).

Define exact rational numbers by

\[
z_{d,0}=\tfrac12,\qquad z_{d,k+1}=\tfrac12\bigl[1-(1-z_{d,k})^d\bigr]^d\quad(k\ge0).
\]

Then, for every \(h\ge0\),

\[
\operatorname{nullity}(T_{f_{d,h}})=\begin{cases}
0,&h\text{ odd},\\
2^{N_{d,2k}}z_{d,k},&h=2k.
\end{cases}
\]

In particular, every odd-height operator is invertible, while every even-height operator has a nonzero kernel. The normalized nullity on even heights has a sharp branching transition:

\[
\lim_{k\to\infty}z_{d,k}=\begin{cases}
0,&2\le d\le6,\\
r_d>0,&d\ge7,
\end{cases}
\]

where, for each \(d\ge7\), \(r_d\in(2/5,1/2)\) is the unique fixed point in that interval of \(z\mapsto\tfrac12[1-(1-z)^d]^d\). There is exactly one other positive fixed point in \((0,2/5)\). For example, \(z_{2,1}=9/32\), \(z_{3,1}=343/1024\), and \(r_7\) is approximately \(0.4475611150\).

## Assumptions and scope

The group law is componentwise addition modulo two; the full ambient space consists of all \(2^{N_{d,h}}\) binary configurations, not just the order ideals. The Fourier transform is the **unnormalized** transform

\[
W_{d,h}(S)=\sum_{I\in J(T_{d,h})}(-1)^{|I\cap S|},\qquad S\subseteq V(T_{d,h}).
\]

Fourier diagonalization identifies the complex (and real) convolution nullity with the number of subsets \(S\) for which \(W_{d,h}(S)=0\). No weights, boundary conditions, or identification of different tree vertices are imposed. Height zero is the single-vertex tree.

## Proof

**1. Root decomposition.** Let \(\epsilon\in\{-1,1\}\) be the character sign at the root, and let \(W_1,\ldots,W_d\) be the child-subtree Fourier coefficients for the induced frequencies. Every order ideal either is empty or contains the root and independently chooses an order ideal in each of the \(d\) child subtrees. Therefore

\[
W_{d,h}=1+\epsilon\prod_{i=1}^{d}W_{d,h-1}^{(i)},\qquad W_{d,0}=1+\epsilon.
\]

The number of ideals obeys \(J_{d,0}=2\), \(J_{d,h}=1+J_{d,h-1}^{d}\); hence \(J_{d,h}\) is even for even \(h\), odd for odd \(h\). Every Fourier coefficient has the same parity as the number of ideals. Thus all coefficients at odd heights are odd and nonzero; all coefficients at even heights are even.

**2. Exact Fourier-zero recursion.** Write \(Z_h\) for the number of zero coefficients and \(A_h\) for the number of coefficients equal to \(+1\) at height \(h\), with fixed \(d\). At height zero, \(Z_0=1\), \(A_0=0\). Suppose \(h\) is odd. Each child coefficient is even. Since \(d\ge2\), their product is either zero or divisible by four. Consequently \(W_{d,h}=+1\) precisely when at least one child coefficient is zero; no coefficient is \(-1\). There are two choices of the root frequency for each child tuple, giving

\[
Z_h=0,\qquad A_h=2\left[2^{dN_{d,h-1}}-\bigl(2^{N_{d,h-1}}-Z_{h-1}\bigr)^d\right].
\]

If \(h\ge2\) is even, all child coefficients are odd. The product is odd; a zero occurs exactly when each child coefficient has absolute value one and the unique choice of root sign cancels their product. At odd child heights, \(+1\) is the only unit coefficient. Therefore

\[
Z_h=A_{h-1}^{d}.
\]

Dividing by \(2^{N_{d,h}}\) and using \(N_{d,h}=1+dN_{d,h-1}\), the two-step recursion becomes exactly the displayed recurrence for \(z_{d,k}=Z_{2k}/2^{N_{d,2k}}\). The initial value is \(z_{d,0}=1/2\), and every subsequent value satisfies \(0<z_{d,k}<1/2\) for \(k\ge1\).

**3. The branching transition.** Put \(g_d(z)=\tfrac12[1-(1-z)^d]^d\) for \(0\le z\le1/2\). It is strictly increasing, fixes zero, and satisfies \(g_d(1/2)<1/2\). Hence the orbit starting at \(1/2\) decreases to a fixed point.

For \(2\le d\le6\), consider the polynomial

\[
Q_d(z)=\frac{2z-[1-(1-z)^d]^d}{z}.
\]

Its apparent singularity at zero is removable. Put \(D=d^2-1\), express \(Q_d(t/2)\) in the degree-\(D\) Bernstein basis on \(0\le t\le1\), and call the resulting coefficients \(B_{d,j}\) (\(0\le j\le D\)). Exact rational expansion gives the following minima:

| \(d\) | Degree \(D\) | \(\min_j B_{d,j}\) |
|---|---:|---|
| 2 | 3 | \(7/8\) |
| 3 | 8 | \(169/256\) |
| 4 | 15 | \(14911/32768\) |
| 5 | 24 | \(79069927/289406976\) |
| 6 | 35 | \(43122177312287/435713694760960\) |

All these exact quantities are positive. Since the Bernstein basis is nonnegative and sums to one, \(Q_d(z)>0\) on \([0,1/2]\). The coefficient generation and every rational sign are independently reproducible in `verify_bernstein.py`: if \(Q_d(t/2)=\sum_{j=0}^{D}c_jt^j\), then \(B_{d,i}=\sum_{j=0}^{i}c_j\binom{i}{j}/\binom{D}{j}\). Thus \(g_d(z)<z\) for positive \(z\le1/2\), and the descending orbit tends to zero.

For \(d\ge7\), Bernoulli's inequality and the elementary monotonicity of \(d(3/5)^d\) for integer \(d\ge7\) give

\[
g_d(2/5)=\tfrac12[1-(3/5)^d]^d\ge\tfrac12[1-d(3/5)^d]\ge\tfrac12[1-7(3/5)^7]>2/5.
\]

Since \(g_d(z)/z\to0\) as \(z\downarrow0\), while \(g_d(1/2)<1/2\), at least two positive fixed points exist, one below and one above \(2/5\). There are no others: for \(0<z<1\), the logarithm of \(g_d(z)/z\) has derivative of the same sign as

\[
d^2(1-z)^{d-1}-\sum_{j=0}^{d-1}(1-z)^j.
\]

The ratio \(d^2t^{d-1}/\sum_{j=0}^{d-1}t^j=d^2/\sum_{j=0}^{d-1}t^{-j}\) is strictly increasing for \(0<t<1\). Consequently the logarithmic ratio has at most one turning point, a maximum, and crosses zero at most twice. The monotone orbit from \(1/2\) therefore converges to the larger fixed point \(r_d\in(2/5,1/2)\), as claimed.

## Verification

`verify_walsh.py` independently enumerates all binary inputs and computes exact in-place Walsh transforms for \((d,h)=(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)\). It verifies the exact number of ideals, zero coefficients, and unit coefficients against the recursion. For example, \((d,h)=(2,2)\) gives 36 zero frequencies among 128 and \((3,2)\) gives 2,744 among 8,192. `verify_bernstein.py` independently recomputes all five exact Bernstein certificates (\(d=2,\ldots,6\)) using exact rational arithmetic in SymPy, and checks the uniform \(d\ge7\) rational inequality. Both programs terminate with explicit PASS records. The all-height statement rests on the structural proof, not on extrapolation from these finite tests.

## Relationship to prior work

Restrepo, Stefankovic, Vera, Vigoda and Yang (arXiv:1007.2255, first posted 2010-07-14) analyze a phase transition for hard-core independent-set Glauber dynamics on complete regular trees. Their underlying configuration space consists of independent vertex sets, not order ideals, and their stated mixing/reconstruction quantities are not the Fourier zeros of order-ideal counting convolution. O'Donnell's *Analysis of Boolean Functions* (2014 first edition; freely readable corrected 2021 arXiv edition) develops Fourier convolution and parity-character methods, which underpin the diagonalization here, but its standard convolution formulas do not specify this rooted-poset zero-density recursion or its branch-seven threshold. The claimed contribution is the exact order-ideal Fourier-nullity recursion and its bifurcation, not general Fourier diagonalization or previously known tree recursions.

## Limitations

No claim is made about irregular rooted trees, independent-set Glauber dynamics, noisy inversion, other character groups, or the singular values of surviving Fourier modes. Positivity for \(2\le d\le6\) is a finite exact rational certificate; it is not replaced by numerical sampling. Publication-priority uncertainty persists for possible unindexed signed tree-poset generating functions. The nonzero limit for \(d\ge7\) is defined implicitly; no closed radical expression is claimed.

## References

- R. Restrepo, D. Stefankovic, J. C. Vera, E. Vigoda, and L. Yang, *Phase Transition for Glauber Dynamics for Independent Sets on Regular Trees*, arXiv:1007.2255, original public posting 2010-07-14. https://arxiv.org/abs/1007.2255
- R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, Chapter 1, particularly probability densities and convolution; corrected open text arXiv:2105.10386 (2021). https://arxiv.org/html/2105.10386v1
