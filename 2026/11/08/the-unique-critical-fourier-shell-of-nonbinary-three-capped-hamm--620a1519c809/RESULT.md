# The unique critical Fourier shell of nonbinary three-capped Hamming metrics

## Finding

Let \(q\ge3\) and \(n\ge4\) be integers. On the set of words \(A^n\) over **any** alphabet \(A\) with \(q\) symbols, define the metric
\[
\rho(x,y)=\min\{\#\{i:x_i\ne y_i\},3\}.
\]
Put
\[
k_* =\left\lfloor\frac{(q-1)n+3}{q}\right\rfloor,\qquad
t_*=(q-1)n-qk_*\in\{-3,-2,\ldots,q-4\},
\]
\[
B_* =\frac{t_*^2-(q-2)t_*-(q-1)n}{2},\quad
F_{q,n}(p)=t_*+B_*2^p-(1+t_*+B_*)3^p.
\]
There is a **unique** \(\beta_{q,n}\in(0,1)\) satisfying \(F_{q,n}(\beta_{q,n})=0\). The metric \(\rho\) has \(p\)-negative type exactly for \(0\le p\le\beta_{q,n}\), where \(p=0\) means the discrete nonzero-distance kernel. Negative type is strict for \(0\le p<\beta_{q,n}\). At the endpoint the full centered zero-eigenvalue space is **exactly one Fourier Hamming shell of degree \(k_*\)**, of dimension
\[
M_{q,n}=\binom{n}{k_*}(q-1)^{k_*}.
\]
The minimal real Euclidean embedding dimension of the snowflake metric \(\rho^{p/2}\) is \(q^n-1\) for \(0<p<\beta_{q,n}\), is \(q^n-1-M_{q,n}\) at the endpoint, and no such isometric Hilbert embedding exists for \(p>\beta_{q,n}\). Equivalently, the kernel \(\exp(-s\rho(x,y)^p)\) is positive semidefinite for all \(s>0\) exactly when \(0<p\le\beta_{q,n}\).

In particular, the **worst Fourier degree is independent of \(p\) throughout \(0<p<1\)**. For \(q=4,n=4\), this yields the explicit nonbinary threshold
\[
\beta_{4,4}=\frac{\log(6/5)}{\log(3/2)},\qquad M_{4,4}=108.
\]

There is also a residue-sensitive second-order asymptotic. With
\[
L=\log(3/2),\qquad \alpha_q=\frac{2}{(q-1)L},\qquad
C_q(t)=\frac{t^2-(q-2)t}{2},
\]
\[
\gamma_q(t)=\alpha_q^2\left[\log3\,(1+t)+L\,C_q(t)-\frac{\log3+\log2}{2}\right],
\]
for fixed \(q\) and \(n\to\infty\),
\[
\beta_{q,n}=\frac{\alpha_q}{n}+\frac{\gamma_q(t_*)}{n^2}+O_q(n^{-3}),\qquad
\frac{M_{q,n}}{q^n}\sim\frac{q}{\sqrt{2\pi(q-1)n}}.
\]
The second coefficient is periodic in \(n\bmod q\), via the unique representative \(t_*\in[-3,q-4]\) of \(-n\bmod q\).

## Assumptions and scope

All parameters \(q,n\) are integers in the specified ranges; \(q\) need not be a prime power. To compute Fourier transforms, identify each alphabet with the cyclic group of order \(q\); this changes no Hamming distances. A real symmetric kernel \(\rho(x,y)^p\) is conditionally negative semidefinite when
\[
\sum_{x,y} a_xa_y\rho(x,y)^p\le0
\quad\text{whenever }\sum_x a_x=0.
\]
Strictness means strict inequality for nonzero real centered coefficients. Characters of \((\mathbb Z/q\mathbb Z)^n\) of degree \(k\) have exactly \(k\) nontrivial coordinates and multiplicity \(\binom nk(q-1)^k\). Fourier sums below are **unnormalized**.

## Proof

**1. Exact Fourier multipliers.** Let \(d(x)=\#\{j:x_j\ne0\}\). For \(p>0\), the translation kernel is
\[
\min(d(x),3)^p=3^p(1-\mathbf1_{d=0})+(1-3^p)\mathbf1_{d=1}+(2^p-3^p)\mathbf1_{d=2}.
\]
For a character nontrivial in exactly \(k\ge1\) coordinates, the degree-one Hamming character sum is \(t_k=(q-1)n-qk\). Expanding the square of the sum of coordinate character sums, and subtracting diagonal terms, gives the degree-two sum
\[
B_k=\frac{t_k^2-(q-2)t_k-(q-1)n}{2}.
\]
As a nontrivial character sums to zero over the whole group and to one at the origin, its multiplier is
\[
\lambda_k(p)=-3^p+(1-3^p)t_k+(2^p-3^p)B_k
=t_k+B_k2^p-(1+t_k+B_k)3^p.
\]
Every nonconstant eigenspace has one of these real eigenvalues; the constant eigenvalue is positive.

**2. An exponent-independent maximizing shell.** For \(0<p<1\), set \(R(p)=(3^p-1)/(3^p-2^p)\). Strict concavity of \(u^p\) on positive numbers yields \(2\cdot2^p>1+3^p\), hence \(R(p)>2\). Also \(2\cdot3^p+1>3\cdot2^p\), by differentiation and \(2\log3>3\log2\), so \(R(p)<3\). From the preceding quadratic formula,
\[
\lambda_{k+1}(p)-\lambda_k(p)
=q(3^p-2^p)\big[R(p)+t_k-q+1\big].
\]
Because \(t_k\) is integral, this difference is positive exactly when \(t_k\ge q-3\), and negative exactly when \(t_k\le q-4\). As \(t_k\) falls by \(q\) with each increment of \(k\), there is a unique maximizer over \(1\le k\le n\), namely \(k_*\) above: its \(t_*\) is the unique representative in \([-3,q-4]\). No other Fourier degree ties it at any \(0<p<1\).

**3. Unique crossing and exclusion beyond the crossing.** Write \(A_*=-B_*\). It is nonnegative: if \(t_*\ge0\), use \((q-2)t_*-t_*^2\ge0\); for \(t_*=-1,-2\), direct substitution gives nonnegative values; for \(t_*=-3\), the congruence \(n\equiv3\pmod q\) and \(n\ge4\) give \(n\ge q+3\), hence \(A_*\ge(q-3)(q+2)/2\ge0\).

Moreover
\[
2A_*-6(1+t_*)=(q-1)n+(q-8)t_*-t_*^2-6>0.
\]
Indeed, replacing \(n\) by four decreases this expression, and the resulting concave quadratic has positive endpoint values \(q+5\) and \(6\) at \(t_*=-3\) and \(t_*=q-4\), respectively. Thus \(A_*-(1+t_*)>2A_*/3\). Differentiating gives
\[
F'_{q,n}(p)=\big[A_*-(1+t_*)\big]\log3\,3^p-A_*\log2\,2^p>0,
\]
since \(2\log3>3\log2\); the strict inequality also covers \(A_*=0\). At \(p=0\), \(F_{q,n}(0)=-1\). At \(p=1\),
\[
F_{q,n}(1)=\frac{(q-1)n+(q-6)t_*-t_*^2-6}{2}>0.
\]
The last lower bound follows by replacing \(n\) by four and evaluating the concave quadratic at the two endpoints of \([-3,q-4]\), where it equals \((q-1)/2\) and \(q-1\). Consequently the root \(\beta_{q,n}\in(0,1)\) is unique; below it all nontrivial multipliers are negative, at it only degree \(k_*\) vanishes, and above it the same multiplier is positive, even past \(p=1\). This is exactly the asserted strict/weak negative-type classification.

**4. Embedding and Gaussian statements.** Double-centering the squared-distance matrix yields the positive semidefinite Gram matrix \(-\tfrac12 JD_pJ\) precisely for a conditionally negative metric power, with rank the smallest real Euclidean dimension of the isometric embedding of \(\rho^{p/2}\). Character diagonalization gives its rank \(q^n-1\) below the endpoint and \(q^n-1-M_{q,n}\) at it. Schoenberg's equivalence between conditional negative definiteness and positivity of all Gaussian kernels gives the final equivalence; alternatively the failure above the endpoint follows from the first-order Fourier expansion \(\widehat{e^{-s\rho^p}}(k_*)=-s\lambda_{k_*}(p)+O(s^2)<0\) for small \(s>0\).

**5. Asymptotics.** The bounded value \(t_*\) and the exact multiplier give, uniformly for \(p=O_q(n^{-1})\),
\[
F_{q,n}(p)=-1+\frac{(q-1)nL}{2}p
 +\frac{(q-1)n(\log^2 3-\log^2 2)}4p^2
 -\big[\log3(1+t_*)+L C_q(t_*)\big]p
 +O_q(np^3+p^2).
\]
Bracketing the unique zero at \(p=c/n\) establishes \(n\beta_{q,n}\to\alpha_q\). Substitution of \(p=\alpha_q/n+v/n^2\) yields the displayed periodic coefficient \(v=\gamma_q(t_*)\), and the derivative lower bound near the root supplies the \(O_q(n^{-3})\) remainder. Finally, the local central limit estimate for a binomial variable with success probability \((q-1)/q\), evaluated at \(k_*=n(q-1)/q+O_q(1)\), proves the critical-shell multiplicity asymptotic.

## Verification

`python CHECK.py` independently compares the symbolic Fourier eigenvalues against direct cyclic-character sums and tests the maximizing degree, endpoint simplicity by degree, and asymptotic expansion. Its successful output is

`QARY_CAP_THREE_NEGATIVE_TYPE_PASS parameter_cases=784 direct_characters=701`

The 784 parameter configurations use \(3\le q\le16\), \(4\le n\le59\). Direct Fourier checks cover cyclic alphabets and include composite \(q=4\); they verify 701 nonconstant characters at two exponents each. Numerical root checks are finite corroboration, not an all-parameter proof. The infinite theorem follows from the symbolic inequalities above.

## Relationship to prior work

The Hamming association-scheme Krawtchouk eigenvalues are classical; none of the shell-transform identities is claimed new. Murugan's 2011 paper gives general finite vertex-transitive negative-type criteria and an analysis of ordinary binary Hamming-cube subsets, not this clipped nonbinary metric. Brouwer–Cioabă–Ihringer–McGinnis (2017/2018) optimize individual Hamming relation spectra; optimizing the powered **combined** relation kernel and identifying one fixed critical degree for every exponent is a different question.

Previously analyzed binary three-capped Hamming metrics give a separate \(q=2\) result; the present claim is restricted to \(q\ge3\) and supplies the exact alphabet-dependent threshold, critical eigenspace, and \(q\)-periodic second-order law. Published work on positive-definite Turán mass of radius-three Hamming balls optimizes a different admissible cone and does not assert a negative-type threshold for \(\min\{d,3\}^p\).

## Limitations

There is no assertion about unequal alphabet sizes, arbitrary truncation radii, or positive definiteness at a **single** prescribed Gaussian bandwidth above the critical exponent. The source search is bounded, so unrecognized historical coverage by a general weighted-association-scheme theorem remains possible. The proof is mathematical and finite numerical tests are additional corroboration; no independent validation is represented.

## References

1. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first publicly posted 2011-12-23, https://arxiv.org/abs/1112.5657.
2. Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer, Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, arXiv:1709.09011, first publicly posted 2017-09-26, https://arxiv.org/abs/1709.09011.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, DOI 10.1090/S0002-9947-1938-1501980-0.
