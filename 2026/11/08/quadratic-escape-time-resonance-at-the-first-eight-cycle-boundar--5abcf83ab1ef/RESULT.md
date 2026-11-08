# Quadratic escape-time resonance at the first eight-cycle boundary of negative doubling

## Finding

Consider the negative-doubling interval map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1,\end{cases}
\]
with the open hole \(H=(7/17,10/17)\). Let \(X\) be uniformly distributed on \([0,1]\) and write
\[
E_n=\{T^j(X)\notin H\text{ for }0\le j<n\},\qquad n\ge1.
\]
Then for every integer \(n\ge1\) the exact Lebesgue survival probability is
\[
\boxed{\mathbb P(E_n)=\frac{6n^2+12n+39+(-1)^n}{34\,2^n}.}
\]
In particular,
\[
\lim_{n\to\infty}\frac{2^n\mathbb P(E_n)}{n^2}=\frac3{17}.
\]
The exponential escape rate is \(\log2\), but it has a **quadratic**, rather than linear, polynomial prefactor. In contrast, the adjacent four-cycle boundary \(H=(2/5,3/5)\) has the exact linear-prefactor survival law \(4(n+1)/(5\,2^n)\); the ratio of the two survival probabilities is asymptotic to \(15n/68\). The change occurs exactly at the natural first eight-cycle boundary: the endpoints of the \(7/17\) hole lie on one prime eight-cycle.

## Assumptions and scope

The map is defined on both safe branches \([0,7/17]\) and \([10/17,1]\). Its value at the discontinuity \(1/2\), which is contained in the hole, does not matter. The hole is **open** and endpoints survive the current observation; all endpoint conventions have zero effect on Lebesgue probability. Survival at horizon \(n\) means safety at the \(n\) times \(0,\ldots,n-1\), not through time \(n\). All statements apply to every integer \(n\ge1\). No other hole parameters or non-Lebesgue initial laws are claimed.

## Proof

Set \(a=7/17\). The two boundary points iterate through the same prime eight-cycle:
\[
(7,3,11,12,10,14,6,5)/17\longmapsto(3,11,12,10,14,6,5,7)/17.
\]
In particular, splitting the safe set at this finite postboundary orbit gives the following ordered intervals, all with denominator \(17\):
\[
I_1=(0,3),\ I_2=(3,5),\ I_3=(5,6),\ I_4=(6,7),\quad
I_5=(10,11),\ I_6=(11,12),\ I_7=(12,14),\ I_8=(14,17).
\]
Their length vector is
\[
\ell=\frac1{17}(3,2,1,1,1,1,2,3)^\mathsf T.
\]
All open intervals listed in this proof have their endpoints divided by \(17\). The partition endpoints are \(T\)-invariant as a finite set. Since \(T\) is affine with slope \(-2\) on every \(I_i\), each image \(T(I_i)\) is a union of complete safe cells \(I_j\), complete hole cells, or both. The safe-cell adjacency matrix \(B\), whose \((i,j)\) entry is \(1\) precisely when \(T(I_i)\) contains \(I_j\), is
\[
B=\begin{pmatrix}
0&0&0&0&0&1&1&1\\
0&0&0&0&1&0&0&0\\
0&0&1&1&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&1&1&0&0\\
0&0&0&1&0&0&0&0\\
1&1&1&0&0&0&0&0
\end{pmatrix}.
\]
The intervals on which the first \(n\) iterates are safe split into inverse images of safe target cells; every specified inverse step has length contraction \(1/2\). By induction on \(n\), neglecting only finitely many endpoints, the total surviving Lebesgue mass is exactly
\[
\mathbb P(E_n)=2^{-(n-1)}\mathbf 1^\mathsf T B^{n-1}\ell.
\tag{1}
\]
The factors in (1) are essential: the matrix is **source-to-target**, and \(\ell\) supplies the length of the final target cells. A direct solution of \((I-zB)u=\ell\) gives the following eight components (with symmetric pairs \(u_1=u_8\), \(u_2=u_7\), \(u_3=u_6\), \(u_4=u_5\)):
\[
\begin{aligned}
u_1&=\frac{3(1-z^2+z^3)}{17(1-z)^3(1+z)},\\
u_2&=\frac{z+2}{17(1-z)(1+z)},\\
u_3&=\frac{1+z+z^2}{17(1-z)^2(1+z)},\\
u_4&=\frac{1+2z}{17(1-z)(1+z)}.
\end{aligned}
\]
These four expressions and their reflections verify each row of \((I-zB)u=\ell\) by ordinary polynomial multiplication. Summing all eight components yields the exact generating identity
\[
\begin{aligned}
G(z)&:=\sum_{n\ge1}2^{n-1}\mathbb P(E_n)z^{n-1}
=\mathbf1^\mathsf T(I-zB)^{-1}\ell\\
&=\frac{2(7-3z-6z^2+5z^3)}{17(1-z)^3(1+z)}\\
&=\frac{39}{68(1-z)}+\frac{3}{34(1-z)^2}
+\frac{3}{17(1-z)^3}-\frac{1}{68(1+z)}.
\end{aligned}
\]
The coefficient of \(z^{n-1}\) is \((6n^2+12n+39+(-1)^n)/68\). Dividing by \(2^{n-1}\) proves the boxed formula and its quadratic asymptotic. The escape rate is obtained by taking \(-n^{-1}\log\mathbb P(E_n)\), which tends to \(\log2\).

For comparison at \(a=2/5\), the safe partition into \((0,1/5),(1/5,2/5),(3/5,4/5),(4/5,1)\) has the transition matrix
\[
B_4=\begin{pmatrix}0&0&1&1\\0&1&0&0\\0&0&1&0\\1&1&0&0\end{pmatrix}
\]
and final-target length vector \(\ell_4=(1,1,1,1)^\mathsf T/5\). Thus
\[
\mathbf1^\mathsf T(I-zB_4)^{-1}\ell_4=\frac{2(2-z)}{5(1-z)^2},
\]
which by coefficient extraction proves the exact survival law \(4(n+1)/(5\,2^n)\). Taking the quotient of the two exact expressions yields \(\mathbb P_{7/17}(E_n)/\mathbb P_{2/5}(E_n)\sim15n/68\). This comparison highlights a genuine change in the order of the pole at the same exponential rate; it does not assert a continuous parameter limit.

## Verification

`verify_escape17.py` uses exact rational arithmetic to (i) reconstruct the eight safe Markov cells and their adjacency, (ii) verify the eight generating-function row identities, and (iii) independently enumerate inverse images of the safe intervals and compare exact lengths against the closed formula for horizons \(1\le n\le15\). The finite enumeration is a consistency check. The all-\(n\) theorem follows from the finite matrix relation and formal power series identity, not the sampled horizons.

## Relationship to prior work

Ding, Steiner, and Sun [1] develop symbolic admissibility and survivor-set plateau theory for negative-doubling holes, emphasizing entropy and Hausdorff dimension. Their theorems do not calculate the finite-horizon Lebesgue escape law at \((7/17,10/17)\). The public orbit-spectrum calculation [2] classifies the adjacent subcritical range through \(a=2/5\); the present orbit computation concerns the next eight-cycle boundary. Orbit counts and zeta data do **not** determine finite-time survivor mass. The published treatment of Markov holes by Haritha and Agarwal [3] explains how finite-state symbolic methods calculate escape rates for other systems; it does not report this exact quadratic prefactor for the present negative-doubling hole. In particular, simply knowing the common exponential rate \(\log2\) does not predict the pole order or amplitude.

## Limitations

This is an exact fact for the single natural eight-cycle threshold, not a classification of all symmetric holes. The polynomial factor is attached to Lebesgue initial distribution and the specified escape-time convention. The eight-state transfer computation does not assert that the same degree or coefficient persists under hole perturbation. General Markov-hole transfer techniques are classical, so the methodological novelty is limited; the specific sharp threshold law and contrast are the claimed result. Independent assessment of historical priority remains necessary.

## References

[1] Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first public 2026-10-02, https://arxiv.org/html/2610.03327v1 .

[2] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes*, public mathematical result dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c . This reference covers the lower \(a\le2/5\) periodic-orbit phase only.

[3] C. Haritha and N. Agarwal, *Product of expansive Markov maps with hole*, Discrete and Continuous Dynamical Systems 39 (2019), 5743–5774, https://doi.org/10.3934/dcds.2019252 .
