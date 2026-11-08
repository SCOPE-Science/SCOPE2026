# Quartic transfer and square-root periodic-point growth for cyclic diffusion

## Finding

Let \(C_n\), \(n\ge3\), be the labelled simple cycle with vertices \(0,\ldots,n-1\). In synchronous integer diffusion, each vertex transfers one unit to each neighbor whose label is smaller, with all transfers made simultaneously. Two integer label vectors are identified exactly when they differ by the same integer constant at every vertex. Let \(R_n\) be the number of equivalence classes that are **already periodic at time zero**, not classes merely destined to become periodic. The following three assertions hold for every \(n\ge3\).

**Exact finite transfer law.** Put \(\Sigma=\{-1,0,1\}\). For \(a,b,c\in\Sigma\), set \(h=2b-a-c\), and let
\[
D(a,b,c)=\begin{cases}
\{0\},&b=0,\ h=0,\\
\{1,\ldots,h-1\},&b=1,\\
\{h+1,\ldots,-1\},&b=-1,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
(The displayed cases with a positive or negative middle sign may produce an empty set.) Define a nine-by-nine Laurent-polynomial matrix \(M(z)\) indexed by the ordered pairs in \(\Sigma^2\) by
\[
M(z)_{(a,b),(u,c)}=\mathbf1_{\{u=b\}}\sum_{d\in D(a,b,c)}z^d.
\]
Then
\[
\boxed{R_n=[z^0]\operatorname{tr}(M(z)^n).}
\]
All nonconstant periodic states have least period two; hence there are exactly \((R_n-1)/2\) distinct primitive-two temporal orbits modulo translation.

**Quartic spectral reduction.** Write \(s=1+z+z^{-1}\). The characteristic polynomial factors identically as
\[
\det(\lambda I-M(z))=(\lambda-1)
(\lambda^4-s\lambda^3-2\lambda^2-\lambda+1)
(\lambda^4+s\lambda^3+2\lambda^2-\lambda+1).
\]
Let \(A_n(s)\) and \(B_n(s)\) denote the power sums of the roots, counted with multiplicity, of the first and second displayed quartic respectively. Equivalently, they are the integer polynomials determined by Newton sums. If \(T_k\) is the central trinomial number
\[
T_k=\sum_{j=0}^{\lfloor k/2\rfloor}\frac{k!}{j!j!(k-2j)!},
\]
then a polynomial-only formula is
\[
\boxed{R_n=1+\sum_{k\ge0}T_k[s^k]\big(A_n(s)+B_n(s)\big).}
\]
In particular, for \(3\le n\le13\), the counts are
\[
19,\ 47,\ 171,\ 517,\ 1793,\ 5927,\ 20287,\ 69307,\ 238283,\ 823865,\ 2854021.
\]

**Sharp asymptotic.** Let \(\rho\) be the largest real root of
\[\rho^4-3\rho^3-2\rho^2-\rho+1=0,\]
and define
\[
\sigma^2=\frac{2\rho^2}{4\rho^3-9\rho^2-4\rho-1}.
\]
Numerically, \(\rho=3.6095709022238956\ldots\) and \(\sigma^2=0.4702157360865868\ldots\). Then
\[
\boxed{R_n\sim \frac{\rho^n}{\sqrt{2\pi\sigma^2 n}}
=0.5817836156008666\ldots\,\frac{\rho^n}{\sqrt n}.}
\]

## Assumptions and scope

The underlying graph has no loops or multiple edges, and \(n\ge3\). Labels are arbitrary integers, not restricted to nonnegative values, and the equivalence relation is *only* common integral translation; distinct labelings related by a graph automorphism remain distinct. The periodic-point count excludes the transient basin. The one all-equal state is the only fixed state modulo translation. Statements about primitive-two orbits use the established general period-at-most-two theorem for graph diffusion [2]; the transfer identity itself enumerates the states satisfying two-step return directly and does not require this external theorem.

## Proof

**1. The edge-reversal criterion.** Fix an arbitrary orientation on every edge of a finite graph, let \(B\) be its incidence matrix, and put \(\epsilon=\operatorname{sgn}(B^{\mathsf T}x)\), coordinatewise. The diffusion update is \(F(x)=x-B\epsilon\). At the next step set \(x'=F(x)\) and \(\epsilon'=\operatorname{sgn}(B^{\mathsf T}x')\). If \(F^2(x)=x\), then \(B(\epsilon+\epsilon')=0\). Taking the dot product with \(x+x'\) gives
\[
0=\sum_e (d_e+d'_e)(\epsilon_e+\epsilon'_e),
\qquad d_e=(B^{\mathsf T}x)_e,\quad d'_e=(B^{\mathsf T}x')_e.
\]
Each summand is nonnegative and is strictly positive whenever \(\epsilon_e+\epsilon'_e\ne0\), because \(\epsilon_e\) and \(\epsilon'_e\) are the signs of \(d_e,d'_e\). Thus \(\epsilon'=-\epsilon\) on every edge. Conversely this sign reversal implies \(F^2(x)=x\). Consequently a two-step-return point has each nonzero oriented gap change sign and each zero gap remain zero. This establishes the criterion without assuming that the incidence matrix has trivial cycle space.

**2. Cyclic local intervals.** Set \(\delta_i=x_i-x_{i+1}\), \(\epsilon_i=\operatorname{sgn}(\delta_i)\), subscripts modulo \(n\). The update becomes
\[
F(x)_i=x_i+\epsilon_{i-1}-\epsilon_i,
\qquad
\delta'_i=\delta_i-(2\epsilon_i-\epsilon_{i-1}-\epsilon_{i+1}).
\]
The edge-reversal criterion therefore says precisely that \(\delta_i\in D(\epsilon_{i-1},\epsilon_i,\epsilon_{i+1})\). In particular, every two-step-return point has \(|\delta_i|\le3\). Conversely, these local choices guarantee the sign reversal and hence the two-step return. A cyclic sequence of integer gaps integrates to a vertex labelling if and only if \(\sum_i\delta_i=0\), and in that case integration is unique modulo a common additive integer. The trace of the transfer matrix imposes cyclic consistency of the consecutive sign pairs, while extracting \([z^0]\) imposes the single global gap-sum constraint. This proves the first identity.

**3. Quartic reduction and polynomial formula.** Order the transfer states as
\[
(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1).
\]
The state \((0,0)\) has one isolated unit-weight loop. On the other eight states, entries follow from the three possible signs and the finite intervals in Step 2. Taking the determinant after deleting this isolated state and simplifying with \(s=1+z+z^{-1}\) yields the displayed two quartics. This is a finite nine-by-nine Laurent-polynomial identity; the standalone `verify_transfer.py` independently constructs its entries and checks the determinant symbolically. The trace of the \(n\)-th matrix power equals the sum of the \(n\)-th powers of all eigenvalues, including repeated roots. Thus it equals \(1+A_n(s)+B_n(s)\). Finally, \([z^0](1+z+z^{-1})^k=T_k\), giving the second exact count formula. Newton's identities, or the recurrence code in the verification artifact, compute the integer polynomials without numerical eigenvalue approximations.

**4. Dominant saddle and asymptotic.** The eight-state transfer component is irreducible and aperiodic: it admits closed walks of lengths two and three, and all eight states communicate. Its matrix at \(z=1\) is nonnegative and primitive. By Perron–Frobenius its Perron eigenvalue \(\rho>1\) is simple; substituting \(s=3\) into the quartic factorization identifies \(\rho\) as the specified root. For \(z=e^{i\theta}\) with \(0<|\theta|\le\pi\), the modulus of every transfer entry is bounded by the corresponding entry at \(1\), and one edge in the irreducible component has weight \(z+z^2+z^3\), of modulus strictly less than \(3\). The strict Perron comparison therefore gives spectral radius strictly less than \(\rho\) away from \(\theta=0\).

Let \(\lambda(\theta)\) be the analytic leading branch near zero. From
\[
\lambda^4-(1+2\cos\theta)\lambda^3-2\lambda^2-\lambda+1=0
\]
implicit differentiation gives \(\lambda'(0)=0\) and
\[
-\left.\frac{d^2}{d\theta^2}\log\lambda(\theta)\right|_{\theta=0}
=\frac{2\rho^2}{4\rho^3-9\rho^2-4\rho-1}=\sigma^2>0.
\]
Using the coefficient integral
\[
R_n=\frac1{2\pi}\int_{-\pi}^{\pi}\operatorname{tr}(M(e^{i\theta})^n)\,d\theta,
\]
the isolated eigenvalue contributes exactly one, the other spectral branches are exponentially smaller, and the nondegenerate Gaussian saddle at zero yields the stated asymptotic, with leading multiplicity one. Standard uniform spectral perturbation on a small arc and compactness on its complement make the error estimate rigorous.

**5. Periods and orbit counts.** By the period-one-or-two theorem for diffusion on finite graphs [2, Theorem 1.1], the initially periodic states are exactly those counted by the two-step-return identity. An all-equal configuration is fixed, and any fixed configuration on a connected graph must be all-equal (equivalently, every edge has no transfer, by dotting the fixed-state equation with its label vector). Thus the other \(R_n-1\) states form disjoint pairs, one per primitive-two temporal orbit.

## Verification

The executable `verify_direct.py` enumerates **all** cyclic gap sequences with \(|\delta_i|\le3\) and \(\sum_i\delta_i=0\) for \(3\le n\le8\), reconstructs the unique representative with its first vertex set to zero, and checks the diffusion map twice. This is exhaustive for the stated ranges because Step 2 proves the gap bound for every two-step-return configuration. Its output is in `direct_output.txt`.

The independent executable `verify_transfer.py` constructs the nine-state transfer operator, computes Laurent coefficients through \(n=17\), and checks them against the separate quartic-Newton/central-trinomial recurrence. It additionally performs the exact symbolic determinant comparison when SymPy is installed. Its output is in `transfer_output.txt`. These computations verify finite and symbolic steps, but do not by themselves establish the asymptotic claim, which follows from Step 4.

Run from the package directory using `python verify_direct.py` and `python verify_transfer.py`. No external datasets are required. The second script uses SymPy only for the optional exact determinant check; all enumerative tests use the Python standard library.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski [1] introduced the diffusion game and proved eventual periodicity for cycles, paths and several other graph families; the cycle result addresses boundedness and eventual recurrence, not a count of states **already** periodic. Long and Narayanan [2] subsequently proved the period-one-or-two theorem for every finite graph and developed an edge-sign potential argument; their result implies no larger least period and provides a known version of the sign-reversal behavior, but supplies no cycle periodic-point enumerator, quartic transfer reduction or periodic-point asymptotic. This result does not claim either prior general periodicity theorem as new.

## Limitations

Labels are identified only under common translation, not rotations or reflections. Counts do not describe sizes of attraction basins or transient durations. The transfer calculation is specific to one-dimensional simple cycles and does not automatically extend to higher-degree graphs. Independent mathematical peer review or external validation has not been performed. Priority remains conditional on the accessible literature, including the possibility of unindexed enumeration results.

## References

[1] C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, first posted September 19, 2016, arXiv:1609.05792; subsequently Discrete Mathematics & Theoretical Computer Science 20(1), 2018, article 4. https://arxiv.org/abs/1609.05792

[2] J. Long, B. Narayanan, *Diffusion on graphs is eventually periodic*, first posted April 13, 2017, arXiv:1704.04295; subsequently Journal of Combinatorics 10(2) (2019), 235–241. https://arxiv.org/abs/1704.04295
