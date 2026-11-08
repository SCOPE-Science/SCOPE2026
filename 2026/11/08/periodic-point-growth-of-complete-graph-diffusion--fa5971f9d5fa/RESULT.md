# Periodic-point growth of complete-graph diffusion

## Finding
Consider synchronous integer diffusion on the labelled complete graph with \(n\geq1\) vertices: each vertex sends one chip to every vertex with a smaller current integer label, simultaneously. Translation by a common integer commutes with the update. Let \(C_n\) be the number of configurations already periodic, counted modulo common integer translation (equivalently, after normalizing the minimum label to zero).

Every such periodic configuration has least period one or two. There is exactly one fixed configuration modulo translation. The complete normalized periodic-point census has exponential generating function
\[
\boxed{\sum_{n\geq1}C_n\frac{z^n}{n!}
=\frac{1-e^{-z}}{1-z+z^2-ze^z}.}
\]
Thus there are exactly \((C_n-1)/2\) primitive two-cycle orbits modulo translation. The initial values are \(C_1,C_2,\ldots,C_8=1,3,19,163,1741,22241,331507,5648119\).

There is also a precise growth law. Let \(\rho\) be the unique positive solution of \(1-\rho+\rho^2-\rho e^\rho=0\), and put
\[
\kappa=\frac{1-e^{-\rho}}{\rho\bigl(1-2\rho+(1+\rho)e^\rho\bigr)}.
\]
Then \(\rho\approx0.4695449931\), \(\kappa\approx0.3309832060\), and
\[
\boxed{C_n\sim\kappa\,n!\rho^{-n}\qquad(n\longrightarrow\infty).}
\]

## Assumptions and scope
For each integer \(n\ge1\), the graph is the simple labelled complete graph on \(\{1,\ldots,n\}\). States are arbitrary \(c\in\mathbb Z^n\); no nonnegativity or fixed-mass restriction is imposed. Write \(F_n(c)_i=c_i+\#\{j:c_j>c_i\}-\#\{j:c_j<c_i\}\). A state is **initially periodic** if \(F_n^p(c)=c\) for some positive integer \(p\). All counts are for the quotient by the diagonal translation action \(c\mapsto c+k\mathbf1\), with the unique normalized representative satisfying \(\min_i c_i=0\). The number of primitive two-cycle orbits counts labelled states but does not identify vertex permutations.

A useful equivalent finite census is
\[
C_n=\sum_{r=1}^n\ \sum_{\substack{a_1+\cdots+a_r=n\\a_i\ge1}}
\frac{n!}{a_1!\cdots a_r!}\prod_{i=1}^{r-1}(a_i+a_{i+1}-1),
\]
where an empty product equals one.

## Proof
**1. Strict reversal on every edge.** Put \(x=c\), \(y=F_n(x)\), \(w=F_n(y)\), and let \(s_{ij}(x)=\operatorname{sgn}(x_i-x_j)\). Directly expanding the update gives
\[
\sum_i y_i(w_i-x_i)
=\sum_{i<j}\bigl(s_{ij}(x)+s_{ij}(y)\bigr)(y_j-y_i)\le0.
\]
Every summand is nonpositive, because when \(y_i\ne y_j\), its sign is opposite the sign of \(y_i-y_j\). If \(w=x\), the left side is zero, so each summand vanishes. Tied labels remain tied after an update on a complete graph. Conversely, if \(x_i\ne x_j\) yet \(y_i=y_j\), the complete-graph symmetry forces \(w_i=w_j\), contradicting \(w=x\). Thus each pair of distinct labels remains distinct after the first update, and its strict order must reverse. Conversely, if all pairwise strict orders reverse and all ties persist, each edge transfers a chip back in the second step, giving \(F_n^2(x)=x\).

For completeness, every initially periodic state has period at most two: the global eventual-period theorem of Long and Narayanan (2017) establishes this for diffusion on any finite graph. An initially periodic point therefore has least period one or two. The same conclusion can also be obtained by iterating the nonincreasing two-time potential above. The fixed points on a connected complete graph are precisely the constant vectors: a nonconstant vector has a maximal label whose vertex sends a chip but receives none, so it cannot be fixed.

**2. Level-block characterization.** Suppose \(x\) takes precisely \(r\) distinct values \(h_1<\cdots<h_r\), with positive multiplicities \(a_1,\ldots,a_r\) summing to \(n\). The new value of each vertex in level \(i\) is
\[
h_i+\sum_{j>i}a_j-\sum_{j<i}a_j.
\]
The difference between the new values of successive old levels is
\[
(h_{i+1}-h_i)-(a_i+a_{i+1}).
\]
All strict comparisons reverse if and only if each adjacent old gap \(d_i=h_{i+1}-h_i\) satisfies
\[
1\le d_i\le a_i+a_{i+1}-1.
\]
These conditions are necessary and sufficient for initial periodicity. Given the ordered multiplicities, there are \(n!/(a_1!\cdots a_r!)\) labelled assignments to the levels. Normalization fixes \(h_1=0\), and the \(r-1\) positive gaps are independent, yielding the stated finite sum. All states have a unique normalized representative. Conservation of total chip mass ensures that taking the quotient by common translation does not introduce spurious shorter periods.

**3. Rank-two generating function.** Set \(u_a(z)=z^a/a!\) for positive \(a\). For weighted positive compositions with exactly \(r\) parts, let \(A_r(z)\) sum the weights \(u_{a_1}\cdots u_{a_r}\prod_{i<r}(a_i+a_{i+1}-1)\), and let \(B_r(z)\) be the same sum multiplied by \(a_r-1\). Directly appending a final part \(b\) uses \(a_r+b-1=(a_r-1)+b\), so
\[
\binom{A_{r+1}}{B_{r+1}}=
\begin{pmatrix}
ze^z&e^z-1\\
z^2e^z&(z-1)e^z+1
\end{pmatrix}
\binom{A_r}{B_r},
\qquad
\binom{A_1}{B_1}=
\binom{e^z-1}{(z-1)e^z+1}.
\]
All series are formal with zero constant term in every transfer-matrix entry. Summing the geometric series in this matrix gives
\[
\sum_{r\ge1}A_r(z)=
\frac{e^z-1}{\det(I-M(z))}
=\frac{e^z-1}{e^z(1-z+z^2-ze^z)},
\]
which is the claimed generating function.

**4. Orbit count and asymptotics.** The only fixed class is the constant class; every other periodic class belongs to a two-cycle, hence the orbit count is \((C_n-1)/2\). Define \(D(z)=1-z+z^2-ze^z\). It satisfies \(D(0)=1\), \(D(z)\to-\infty\) for positive real \(z\to\infty\), and
\[
D'(z)=-1+2z-(1+z)e^z<0\qquad(z>0).
\]
Thus it has a unique simple positive zero \(\rho\). The matrix \(M(\rho)\) above has strictly positive entries and Perron eigenvalue one (its determinant equation \(\det(I-M)=e^zD(z)\) vanishes first there). For \(|z|=\rho\) with \(z\ne\rho\), the power series of \(e^z-1\) has strictly smaller modulus than its value at \(\rho\); all matrix entries have nonnegative coefficients. Therefore the strict Perron comparison gives spectral radius \(\operatorname{spr}(|M(z)|)<1\), so \(\det(I-M(z))\ne0\) off \(\rho\) on this circle. Hence \(\rho\) is the unique dominant pole of the generating function. Its residue is \((1-e^{-\rho})/D'(\rho)\), and the coefficient of its simple pole is asymptotic to \(\kappa\rho^{-n}\), proving the growth formula after multiplication by \(n!\).

## Verification
Two independent executable checks are included as `verify_direct.py` and `verify_egf.py`, with captured standard output. Direct labelled-state enumeration examines every normalized integer state in the box \([0,2n]^n\) for \(1\le n\le5\) and checks initial two-periodicity against the level-gap criterion, together with the fixed-class census and the composition formula. This covers every possible initially periodic state in those dimensions, since the level-gap criterion gives span at most \(2n-3\) for \(n\ge2\). The formal-series program derives coefficients from the displayed rational-exponential identity using exact rational arithmetic and independently computes the composition sum for \(1\le n\le13\). Both report success. These finite checks support, but do not replace, the all-size proof.

## Relationship to prior work
Duffy, Lidbetter, Messinger and Nowakowski introduced the integer diffusion rule in a preprint first posted 19 September 2016; their Theorems 2.10 and 3.1 concern complete-graph eventual periodicity and a general strict-reversal criterion. Long and Narayanan (2017), Theorem 1.1, established eventual period at most two on all finite graphs. Those are already known and are used only as context; neither inspected primary text gives the normalized complete-graph periodic-point sequence, the closed rank-two generating function, or its factorial-exponential growth constant. The present contribution is precisely this enumerative periodic-point result, not a new proof of eventual periodicity or of the general strict-reversal criterion. Literature searches cannot exclude unindexed independent enumerations.

## Limitations
The result counts states already periodic, not their attraction basins or entrance-time distributions. It identifies configurations up to a global additive integer shift but keeps vertex labels distinct. It does not cover other graphs, weighted edges, asynchronous updates, or non-integer diffusion rules. The asymptotic describes \(n\to\infty\), not chip-mass limits at fixed \(n\). Historical priority beyond the inspected sources is not independently certified.

## References
1. C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the Diffusion Game*, arXiv:1609.05792, initial posting 2016-09-19; see complete-graph dynamics and periodicity criteria. https://arxiv.org/abs/1609.05792
2. J. Long and B. Narayanan, *Diffusion on Graphs Is Eventually Periodic*, arXiv:1704.04295, initial posting 2017-04-13; Theorem 1.1. https://arxiv.org/abs/1704.04295
