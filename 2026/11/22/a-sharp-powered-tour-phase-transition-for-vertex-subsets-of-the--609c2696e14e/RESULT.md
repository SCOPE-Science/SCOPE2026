# A sharp powered-tour phase transition for vertex subsets of the three-cube

## Finding

Let \(Q=\{0,1\}^{3}\), equipped with Euclidean distance. For every real \(p\ge2\) and every subset \(X\subseteq Q\) with at least two distinct points, define \(L_p(X)\) as the minimum of \(\sum_{i=1}^{|X|}\|x_i-x_{i+1}\|_2^p\) over cyclic orderings of \(X\), with \(x_{|X|+1}=x_1\). The two-point tour traverses its single edge twice. Put

\[
p_* = \frac{2\log 2}{\log(3/2)}=3.4190225827\ldots.
\]

Then the complete extremal spectrum over **all** vertex subsets, simultaneously for every real exponent \(p\ge2\), is

\[
\max_{X\subseteq Q,\ |X|\ge2}L_p(X)
=\max\bigl\{4\cdot2^{p/2},\ 2\cdot3^{p/2}\bigr\}.
\]

For \(2<p<p_*\), exactly the two parity tetrahedra \(\{000,011,101,110\}\) and \(\{001,010,100,111\}\) attain equality. At \(p=p_*\), those two and the four antipodal vertex pairs are precisely the maximizers. For \(p>p_*\), precisely the four antipodal pairs maximize. No uniqueness classification is asserted for \(p=2\).

This statement concerns only subsets of the eight cube vertices, **not** arbitrary points in the continuous unit cube, and does not resolve the corresponding unrestricted geometric traveling-salesman conjecture.

## Assumptions and scope

All distances are Euclidean. Exponents are real and satisfy \(p\ge2\). The domain consists of all \(\sum_{n=2}^{8}\binom{8}{n}=247\) distinct subsets with at least two vertices. Vertex \(j\in\{0,\ldots,7\}\) is indexed by its three-digit binary representation. The cost is unscaled; taking the \(p\)-th root yields the corresponding scaled Hamiltonian-cycle constant.

## Proof

**Finite geometric lemma.** Every subset \(X\subseteq Q\) with at least two elements has a tour whose successive squared Euclidean distances \(d_1,\ldots,d_m\in\{1,2,3\}\) satisfy simultaneously

\[
A:=\sum_i d_i\le8,\qquad B:=\sum_i\phi(d_i)\le12,
\quad \phi(1)=1,\ \phi(2)=3,\ \phi(3)=6.
\]

For the finite lemma, list the orbit representatives under all coordinate permutations and coordinate-bit reflections. The complete list of twenty representatives and witness tours is below. A two-character tour denotes the closed two-point walk, with both edge traversals counted.

| Representative | Witness tour | Squared-distance steps | \(A\) | \(B\) |
|---|---|---|---:|---:|
| 01 | 01 | 11 | 2 | 2 |
| 03 | 03 | 22 | 4 | 6 |
| 07 | 07 | 33 | 6 | 12 |
| 012 | 012 | 121 | 4 | 5 |
| 016 | 016 | 132 | 6 | 10 |
| 035 | 035 | 222 | 6 | 9 |
| 0123 | 0132 | 1111 | 4 | 4 |
| 0124 | 0124 | 1221 | 6 | 8 |
| 0125 | 0215 | 1212 | 6 | 8 |
| 0127 | 0172 | 1221 | 6 | 8 |
| 0167 | 0176 | 1212 | 6 | 8 |
| 0356 | 0356 | 2222 | 8 | 12 |
| 01234 | 01324 | 11121 | 6 | 7 |
| 01247 | 01274 | 12221 | 8 | 11 |
| 01256 | 01562 | 11211 | 6 | 7 |
| 012345 | 023154 | 111111 | 6 | 6 |
| 012347 | 012374 | 121121 | 8 | 10 |
| 012567 | 015762 | 111111 | 6 | 6 |
| 0123456 | 0132645 | 1111112 | 8 | 9 |
| 01234567 | 01326754 | 11111111 | 8 | 8 |

The accompanying self-contained `check_certificate.py` exactly constructs the 48 cube isometries, verifies the twenty representatives exhaust all 247 relevant subsets, and recomputes every edge and both integer bounds. Thus the finite lemma is exhaustive, rather than a partial numerical experiment.

Set \(T=2^{p_*/2}\). From the defining equality \(2\cdot3^{p_*/2}=4\cdot2^{p_*/2}\), one obtains \(3^{p_*/2}=2T\). Furthermore \(T>3\): the inequality \(256>243\) gives \(p_*>10/3\), and \(2^{5/3}>3\) follows from \(32>27\).

For a witnessing tour write \(a,b,c\) for the numbers of steps with squared lengths \(1,2,3\), respectively. The finite lemma says \(a+2b+3c\le8\) and \(a+3b+6c\le12\). Let \(w=b+2c\), so \(w\le4\) and \(a\le12-3w\). At \(p=p_*\) its tour cost is

\[
a+bT+c(2T)=a+wT\le12+(T-3)w\le4T.
\]

At \(p=2\) its cost is at most \(8\). For \(2\le p\le p_*\), write \(p=(1-\theta)2+\theta p_*\), \(0\le\theta\le1\). Hölder's inequality applied to the fixed witnessing tour yields

\[
\sum_i d_i^{p/2}\le
\left(\sum_i d_i\right)^{1-\theta}
\left(\sum_i d_i^{p_*/2}\right)^\theta
\le8^{1-\theta}(4T)^\theta=4\cdot2^{p/2}.
\]

For \(p\ge p_*\), every \(d_i\le3\) gives

\[
\sum_i d_i^{p/2}\le 3^{(p-p_*)/2}\sum_i d_i^{p_*/2}
\le2\cdot3^{p/2}.
\]

These estimates apply to a specific tour for each subset, hence to its minimum \(L_p(X)\). The even-parity tetrahedron has all six pairwise squared distances equal to \(2\), so every tour costs exactly \(4\cdot2^{p/2}\); the odd-parity tetrahedron is its image under reflection. Any antipodal pair has two tour edges of squared length \(3\), costing exactly \(2\cdot3^{p/2}\). They prove both lower bounds and the sharp transition.

For rigidity when \(p>2\), the twenty-orbit certificate has \(B=12\) only for representatives `07` and `0356`. For the other eighteen representatives the comparison at \(p_*\) is strict, so the inequalities above are strict at every \(p>2\). At `07`, the \(p=2\) bound is strict and at `0356`, for \(p>p_*\) the comparison with squared length \(3\) is strict. This establishes precisely the claimed equality cases.

## Verification

Run `python3 check_certificate.py`. This enumerates exactly the 247 admissible vertex subsets, the 48 isometries, and twenty exhaustive symmetry orbits; verifies every tour and integer inequality; and checks that only the two specified representatives can saturate the \(B\) bound. No floating-point computations or external packages are required. The infinite-exponent conclusion rests on the displayed Hölder and monotonicity arguments, not on finite numerical tests.

## Relationship to prior work

Balogh, Clemen, and Dumitrescu (2024) supply the four-vertex even-parity tetrahedral **lower-bound construction** at exponent three and prove a sufficiently-high-dimensional result for vertex-restricted cycles; their quoted results do not give a sharp three-cube upper bound or the full real-exponent phase transition. The November 2026 length-optimization problem collection discusses the corresponding unrestricted three-dimensional traveling-salesman question, where arbitrary continuous points are allowed. The present sharp spectrum is a finite-vertex restriction, so it does not settle that open question. Prior hypercube-graph Hamiltonicity results involve cycles of cube *edges* rather than complete-graph Euclidean powered-distance costs.

## Limitations

The theorem does not extend to arbitrary \(X\subset[0,1]^3\), to higher-dimensional binary cubes, or to \(0<p<2\). Equality cases at \(p=2\) are not completely enumerated. The classification uses a transparent finite certificate for twenty symmetry classes and an analytic extension over a continuous parameter; it is not a general structural theorem for large configurations. Historical priority is provisional and an independent mathematical audit has not been performed.

## References

1. Y. Teplitskaya et al., *Open problems from the Length Optimization event at MDS 2026*, arXiv:2611.03403v1 (first posted 2 November 2026), Section 4. https://arxiv.org/abs/2611.03403
2. J. Balogh, F. C. Clemen, A. Dumitrescu, *On a Traveling Salesman Problem for Points in the Unit Cube*, Algorithmica 86 (2024), 3054–3078, DOI: 10.1007/s00453-024-01257-w, Sections 2–3. https://link.springer.com/article/10.1007/s00453-024-01257-w
