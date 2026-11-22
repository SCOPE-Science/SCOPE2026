# Quadratic vacancy-coexistence spike and exact correlations on even folded hypercubes

## Finding

For every **even** integer \(n\ge4\), the classical zero-field antiferromagnetic spin-one Blume–Capel model on the \(2^n\)-vertex folded hypercube has just one crystal-field threshold:
\[
D_* = \frac{n-1}{2}J.
\]
Below \(D_*\), all ground states are fully occupied; above \(D_*\), the only ground state is completely vacant. **Precisely at \(D_*\), and not on a positive-width interval, additional half-occupied ground states appear.** The exact counts of labeled spin assignments are
\[
\begin{array}{c|ccc|c}
 & K=0 & K=2^{n-1} & K=2^n & \text{total} \\
D<D_* & 0 & 0 & 2(n+1) & 2(n+1)\\
D=D_* & 1 & 2n(n+1) & 2(n+1) & 1+2(n+1)^2\\
D>D_* & 1 & 0 & 0 & 1
\end{array}
\]
where \(K=\sum_x s_x^2\) is the number of occupied vertices. The exact ground energy for every \(D\in\mathbb R\) is
\[
E_0=2^n\min\left\{D-\frac{n-1}{2}J,\ 0\right\}.
\]

At the threshold, take the uniform probability measure on all \(1+2(n+1)^2\) labeled ground states. For any sites \(x,y\) at Hamming distance \(r\in\{0,\ldots,n\}\), its spin expectation is zero and its exact two-point correlation is
\[
\boxed{\mathbb E[s_xs_y]=\frac{(n+2)(-1)^r(n+1-2r)}{1+2(n+1)^2}.}
\]
In particular, on the \(16\)-vertex Clebsch graph (the folded four-cube), the transition is at \(D=3J/2\), with exactly **51** minimizing spin configurations: one empty, 40 half-occupied and ten fully occupied. This is a finite-cluster zero-temperature statement; no nonzero-temperature or infinite-volume phase transition is implied.

## Assumptions and scope

Fix an even integer \(n\ge4\). The folded hypercube \(FQ_n\) has vertex set \(V=\mathbb F_2^n\). Each vertex \(x\) is adjacent to the \(n\) vertices \(x+e_i\), and to its antipode \(x+\mathbf 1\), with addition modulo two. These \(n+1\) neighbors are distinct. Hence \(|V|=2^n\), the graph is \((n+1)\)-regular, and every unoriented edge is counted once.

The classical spin variable at each vertex takes one of the three numerical values \(s_x\in\{-1,0,+1\}\). With uniform antiferromagnetic exchange \(J>0\), arbitrary crystal field \(D\in\mathbb R\) and **zero external magnetic field**, set
\[
\mathcal H(s)=J\sum_{\{x,y\}\in E(FQ_n)}s_xs_y+D\sum_{x\in V}s_x^2.
\]
The occupied-site count is \(K(s)=\sum_x s_x^2\). Multiplicities distinguish labeled spin assignments; the global spin reversal and graph automorphisms are not factored out. The critical correlation is the finite uniform mixture over exactly the minimizing assignments at \(D=D_*\).

For \(S\subseteq[n]\), define the Boolean character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\). Write
\[
\phi_0=\chi_{[n]},\qquad \phi_i=\chi_{[n]\setminus\{i\}}\quad(1\le i\le n).
\]
These are \(n+1\) distinct functions taking values \(\pm1\).

## Proof

**1. Spectral lower bound with equality.** The graph adjacency matrix \(A\) is diagonal in the Boolean-character basis. The eigenvalue of the character of Hamming weight \(k\) is
\[
\lambda_k=n-2k+(-1)^k.
\]
For even \(n\ge4\), its minimum is \(1-n\), attained exactly for weights \(k=n\) and \(k=n-1\). These have a total of \(n+1\) linearly independent characters, \(\phi_0,\ldots,\phi_n\). In particular,
\[
\sum_{\{x,y\}\in E}s_xs_y=\frac12s^{\mathsf T}As
\ge-\frac{n-1}{2}\sum_xs_x^2,
\]
with equality **if and only if** \(s\) lies in the span of those \(n+1\) characters. Consequently,
\[
\mathcal H(s)\ge(D-D_*)K(s),\qquad 0\le K(s)\le 2^n.
\]
Every \(\pm\phi_i\) has \(K=2^n\) and attains this bound; the zero function has \(K=0\) and energy zero. For \(D<D_*\), equality at the lower endpoint forces \(K=2^n\), and for \(D>D_*\) it forces \(K=0\). At equality \(D=D_*\), every and only ternary-valued function in the minimum eigenspace minimizes energy. This proves the stated energy envelope and reduces the full state classification to a finite-valued affine-function lemma.

**2. Classification of ternary affine functions.** Since \(\phi_i(x)=\phi_0(x)(-1)^{x_i}\), any vector in the lowest adjacency eigenspace has the form
\[
s(x)=\phi_0(x)g(\epsilon),\quad
 g(\epsilon)=a_0+\sum_{i=1}^na_i\epsilon_i,
 \quad \epsilon_i=(-1)^{x_i}.
\]
The sign map \(\epsilon\mapsto x\) is a bijection, and \(s(x)\in\{-1,0,1\}\) is equivalent to \(g(\epsilon)\in\{-1,0,1\}\) for all sign vectors \(\epsilon\in\{-1,1\}^n\).

Suppose precisely \(q\) of \(a_1,\ldots,a_n\) are nonzero. After absorbing their signs into the independent \(\epsilon_i\), the possible values of \(g\) include at least \(q+1\) **distinct** ordered partial sums: start with all signs negative and successively flip each of the \(q\) coordinates to positive, strictly increasing the value each time. Since \(g\) takes at most three values, \(q\le2\).

- If \(q=0\), then \(g\equiv-1,0,\) or \(+1\): three configurations.
- If \(q=1\), the two distinct values \(a_0+a_i\) and \(a_0-a_i\) are any ordered distinct pair from \(\{-1,0,+1\}\). There are six assignments for each coordinate, hence \(6n\) states. Two give full occupation; four give occupation \(2^{n-1}\).
- If \(q=2\), the four subset-sign sums can take at most three values only if \(|a_i|=|a_j|\). Their three values then form \(a_0-2|a_i|,a_0,a_0+2|a_i|\), which must be exactly \(-1,0,+1\). Therefore \(a_0=0\) and \(|a_i|=|a_j|=1/2\), giving four states per unordered coordinate pair, each occupied at exactly \(2^{n-1}\) vertices.

Distinct affine coefficients define distinct functions, because the constant and coordinate Walsh characters are linearly independent. Therefore the total number of critical states is
\[
3+6n+4\binom n2=1+2(n+1)^2,
\]
with occupation counts \(1\), \(4n+4\binom n2=2n(n+1)\), and \(2+2n=2(n+1)\). This proves the entire state classification, including all coexistence cases and all occupancy exclusions.

Equivalently, the **complete critical minimizer set** admits the concise description
\[
\mathcal G_* = \{0\}\cup\{\pm\phi_i:0\le i\le n\}
\cup\left\{\frac{\eta\phi_i+\zeta\phi_j}{2}:
0\le i<j\le n,\ \eta,\zeta\in\{-1,1\}\right\}.
\]
All states in the second union are fully occupied, and all states in the third union are half occupied; the latter fact follows from orthogonality of the two different binary characters.

**3. Critical two-point function.** Let \(d=n+1\). Both the empty state and the global spin-reversal pairs give zero mean at each vertex. Summing spin products over the entire critical state set gives
\[
\sum_{s\in\mathcal G_*}s_xs_y
=2\sum_{i=0}^n\phi_i(x)\phi_i(y)
+\sum_{0\le i<j\le n}\sum_{\eta,\zeta=\pm1}
 \frac{(\eta\phi_i(x)+\zeta\phi_j(x))(\eta\phi_i(y)+\zeta\phi_j(y))}{4}
=(n+2)\sum_{i=0}^n\phi_i(x)\phi_i(y).
\]
The pair-sign sum cancels mixed contributions and adds one copy of each mode for every pair containing it. When \(x\) and \(y\) have Hamming distance \(r\), the character sum equals
\[
\sum_{i=0}^n\phi_i(x)\phi_i(y)=(-1)^r\big(1+(n-r)-r\big)=(-1)^r(n+1-2r).
\]
Dividing by \(|\mathcal G_*|=1+2(n+1)^2\) proves the displayed correlation formula. In the fully occupied regime the corresponding uniform ensemble covariance is \((-1)^r(n+1-2r)/(n+1)\), and in the vacant regime it is zero.

## Verification

Two standalone programs accompany this proof. `verify_exhaustive.cpp` is an independently implemented exhaustive integer-state scan of **all \(3^{16}=43{,}046{,}721\) configurations on the folded four-cube**; it verifies the global spectral-energy lower bound, the unique critical occupancy classes and their multiplicities, and both strict-regime ground-state counts. It reports `PASS exhaustive_states=43046721 critical=51 occupied_full=10 occupied_half=40 empty=1 strict_below=10 strict_above=1`.

`verify_walsh.py` uses Python 3 and only its standard library. It independently constructs the adjacency matrix through neighbor lists, checks the claimed eigenvalues and lowest-mode dimensions, enumerates the predicted critical minimizing states and verifies their exact energy and distance correlations on dimensions \(n=4,6,8\). It also performs an independent bounded half-integer-coefficient search for ternary affine functions on \(n=4,6\). The exact critical counts are respectively 51, 99 and 163. The verifiers test finite instances; the proof above, not computational extrapolation, establishes the statement for all even \(n\ge4\).

To reproduce, run `c++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive` and `python3 verify_walsh.py` in the directory containing the two files.

## Relationship to prior work

Xu and Meng (2009) determine the ordinary folded-hypercube adjacency spectrum, including the minimum-band structure used here. The least adjacency eigenvalue and **binary** Ising ground configurations on weighted folded cubes are also established; the count \(2(n+1)\) of fully occupied Ising states is a premise, not a novelty claim. Mosseri (2014) supplies an arbitrary-graph binary-Ising Hadamard/Fourier framework but does not classify ternary spin-one ground states. Pawłowski (2007) investigates competing occupied and vacant antiferromagnetic order in the Blume–Capel model on the **square lattice**; its result does not cover folded-hypercube interactions or the exact coexistence multiplicity and correlation. Related spin-one results on ternary Hamming Cartesian powers and finite wheels treat genuinely different graph families; the wheel triangle case already covers the smallest folded cube \(FQ_2\), which is excluded here.

The contribution assessed as potentially original is precisely the **all-even-dimension spin-one vacancy-threshold classification, quadratic half-occupied coexistence count and critical two-point correlation** on the unweighted folded hypercube. The general spectral method, elementary affine-function decomposition and known binary-Ising conclusions are not claimed separately. No universal literature-uniqueness or independent-priority certification is asserted.

## Limitations

The result is only for uniform antiferromagnetic bonds on the standard folded hypercube, even dimensions at least four, zero magnetic field, strictly classical three-valued spins, and zero-temperature minimizing configurations. It does not treat odd folded dimensions, unequal couplings, nonzero field, finite-temperature thermodynamics, or an infinite-volume phase transition. Historical priority remains provisional because an unindexed equivalent spectral spin-one application may exist. Independent scientific validation has not been performed.

## References

1. G. Pawłowski, *Multiphase structure of finite-temperature phase diagram of the Blume-Capel model. Wang-Landau sampling method*, arXiv:cond-mat/0703299 (first public version 12 March 2007). https://arxiv.org/abs/cond-mat/0703299
2. Y. Xu and J. Meng, *On the Folded Hypercube and Bi-folded Hypercube*, *Ars Combinatoria* **92** (2009), 3–9, Theorem 2.3. https://combinatorialpress.com/article/ars/Volume%20092/volume-92-paper-1.pdf
3. R. Mosseri, *Ising-like models on arbitrary graphs: The Hadamard way*, arXiv:1409.0147 (first public version 30 August 2014). https://arxiv.org/abs/1409.0147
4. *Parity-controlled frustration relocation on weighted folded hypercubes*, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-controlled-frustration-relocation-on-weighted-folded-hype--4e33e4bd452a
5. *Six pure ground-state phases and a flat-band correlation law for ternary Hamming Blume–Capel models*, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-six-pure-ground-state-phases-and-a-flat-band-correlation-law-for--732dcef7635a
6. *Parity-controlled vacancy condensation in antiferromagnetic spin-one wheel graphs*, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-controlled-vacancy-condensation-in-antiferromagnetic-spin--a9d59ac1a17e
