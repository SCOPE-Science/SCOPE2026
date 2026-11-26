# Record–excedance covariance changes sign at five letters

## Finding

For a uniformly random permutation \(\pi\in S_n\), the joint behavior of left-to-right upper records and ordinary excedances has a precise position-dependent sign structure. The entire two-index cross-covariance kernel admits a closed formula, valid even for arbitrary value thresholds. Its aggregate implication is a sharp finite-size reversal: total records and total excedances have **negative covariance at orders two through four, and strictly positive covariance at every order five or larger**.

For \(2\le i\le n\), \(1\le j\le n\), and \(0\le t\le n\), set
\[
\delta_{n,i,t}=\frac tn-\frac{\binom ti}{\binom ni},
\qquad\binom ti=0\quad\text{if }t<i.
\]
Then
\[
\operatorname{Cov}(R_i,T_{j,t})=
\begin{cases}
-\delta_{n,i,t}/[i(i-1)]&j<i,\\
\delta_{n,i,t}/i&j=i,\\
0&j>i.
\end{cases}
\]
For \(i=1\), the covariance is zero. For \(2\le i\le n\) and \(1\le t<n\), \(\delta_{n,i,t}>0\). Thus earlier-position threshold indicators correlate negatively with a record at \(i\), the current threshold indicator positively, and later positions not at all.

In particular, for \(E_j=\mathbf1\{\pi_j>j\}\), and \(\mathcal R_n=\sum_{i=1}^{n}R_i\),
\[
\operatorname{Cov}(\mathcal R_n,E_j)
=\frac{j}{n^2}-\frac{1}{j\binom nj},\qquad 1\le j\le n-1.
\]
This is negative at \(j=1\) and positive at all \(2\le j\le n-1\). For the total excedance count \(\mathcal E_n=\sum_{j=1}^{n-1}E_j\), write \(B_m=\sum_{j=0}^{m}\binom mj^{-1}\). Then
\[
\boxed{\operatorname{Cov}(\mathcal R_n,\mathcal E_n)
=\frac{n+1-2B_{n-1}}{2n}.}
\]
The values at orders \(2,3,4,5\) are, respectively, \(-1/4\), \(-1/6\), \(-1/24\), and \(1/15\). The covariance increases strictly with \(n\) and converges to \(1/2\), although the correlation tends to zero:
\[
\operatorname{Corr}(\mathcal R_n,\mathcal E_n)
\sim\frac{\sqrt3}{\sqrt{n\log n}}.
\]

## Assumptions and scope

Fix an integer \(n\ge2\). The random permutation is uniform on the \(n!\) permutations of \(\{1,\ldots,n\}\). An upper record at position \(i\) means that the value at that position is strictly larger than every preceding value, including the first position as a deterministic record. For \(1\le j\le n\) and integer \(0\le t\le n\), \(T_{j,t}=\mathbf1\{\pi_j>t\}\); the ordinary excedance indicator is \(E_j=T_{j,j}\), with \(E_n=0\). All covariances are under the uniform permutation law. No independence is assumed between the values of the permutation. Binomial coefficients with upper argument smaller than the lower argument are zero.

The main claims cover all indicated \(n,i,j,t\), including boundary cases. Strict threshold signs are asserted only for \(i\ge2\) and \(1\le t<n\). Correlation asymptotics refer to \(n\to\infty\).

## Proof

**1. Record/threshold cross-covariance.** The relative order of the first \(i\) values is uniform and independent of which unordered \(i\)-element subset \(S\subseteq\{1,\ldots,n\}\) those values form. Thus \(\Pr(R_i=1)=1/i\). Conditioned on \(R_i=1\), the value at \(i\) is the maximum of \(S\), yielding
\[
\Pr(T_{i,t}=1\mid R_i=1)
=1-\frac{\binom ti}{\binom ni}.
\]
Its unconditional probability is \((n-t)/n\), so the difference is exactly \(\delta_{n,i,t}\). Multiplying by \(1/i\) proves the diagonal formula.

For \(j<i\), conditional symmetry makes \(\pi_j\) uniformly distributed over the \(i-1\) **nonmaximum** elements of \(S\). The expected number of elements of \(S\) larger than \(t\) is \(i(n-t)/n\), while the expected number of such elements contributed by the maximum is \(1-\binom ti/\binom ni\). Consequently
\[
\Pr(T_{j,t}=1\mid R_i=1)
=\frac{i(n-t)/n-(1-\binom ti/\binom ni)}{i-1}.
\]
Subtracting \((n-t)/n\) gives \(-\delta_{n,i,t}/(i-1)\). Multiply by \(1/i\) for the earlier-position case. For \(j>i\), the complete vector of values after position \(i\) is independent of the relative order of the first \(i\) positions, and therefore independent of \(R_i\). When \(i=1\), \(R_1=1\) deterministically.

For \(1\le t<n\), \(\binom ti/\binom ni<t/n\) if \(i\ge2\): when \(t<i\) it is zero, otherwise the product \((t/n)((t-1)/(n-1))\cdots\) is strictly smaller than \(t/n\). This proves every strict kernel sign.

**2. Excedance-position profile.** Specializing \(t=j\), the covariance for \(2\le i\le n\) is
\[
\operatorname{Cov}(R_i,E_j)=
\begin{cases}
-j/[ni(i-1)]&j<i,\\
1/n-1/[i\binom ni]&j=i,\\
0&j>i.
\end{cases}
\]
The formula for the diagonal also gives zero when \(i=j=1\). Summing over \(i\) and using \(\sum_{i=j+1}^{n}1/[i(i-1)]=1/j-1/n\) yields
\[
 c_{n,j}:=\operatorname{Cov}(\mathcal R_n,E_j)
=\frac1n-\frac1{j\binom nj}-\frac jn\left(\frac1j-\frac1n\right)
=\frac{j}{n^2}-\frac{1}{j\binom nj}.
\]
Here \(j=1\) gives \(-(n-1)/n^2\). For \(2\le j\le n-1\), rewrite the expression as \((j-n/\binom{n-1}{j-1})/n^2\). Since \(\binom{n-1}{j-1}\ge n-1\) and \(j(n-1)>n\), it is strictly positive.

**3. Aggregation and a sharp threshold.** Summing over \(1\le j\le n-1\) gives
\[
\sum_{j=1}^{n-1}\frac j{n^2}=\frac{n-1}{2n},\qquad
\sum_{j=1}^{n-1}\frac1{j\binom nj}
=\frac1n\sum_{j=1}^{n-1}\frac1{\binom{n-1}{j-1}}
=\frac{B_{n-1}-1}{n}.
\]
Equivalently, and directly from the expression for \(c_{n,j}\),
\[
\operatorname{Cov}(\mathcal R_n,\mathcal E_n)
=\frac{n+1-2B_{n-1}}{2n}.
\]
(The identity \(j\binom nj=n\binom{n-1}{j-1}\) is used in the sum.)

The inverse-binomial sums obey, for \(m\ge1\),
\[
 B_{m+1}=2+\frac{m+2}{2(m+1)}(B_m-2)+\frac1{m+1}.
\]
To verify it directly, write \(B_m-2=\sum_{j=1}^{m-1}\binom mj^{-1}\). For each \(1\le j\le m\), Pascal's factorial identity gives \(\binom{m+1}{j}^{-1}=\frac{m+1-j}{m+1}\binom mj^{-1}\), where the \(j=m\) term is \(1/(m+1)\). Symmetry of the inner summands implies \(\sum_{j=1}^{m-1}(m+1-j)\binom mj^{-1}=(m+2)(B_m-2)/2\). Adding the two endpoints gives the recurrence.

The initial values are \(B_1=2\), \(B_2=5/2\), and \(B_3=B_4=8/3\). Since the recurrence maps every \(B_m\le8/3\), for \(m\ge3\), to a value at most \(8/3\), we have \(B_m\le8/3\) for all \(m\ge3\). Hence \(n+1-2B_{n-1}>0\) for \(n\ge5\). Direct substitution shows the three negative cases at \(n=2,3,4\).

The same recurrence gives the first difference
\[
\operatorname{Cov}(\mathcal R_{n+1},\mathcal E_{n+1})-
\operatorname{Cov}(\mathcal R_n,\mathcal E_n)
=\frac{(n+1)B_{n-1}-2n-1}{2n(n+1)}>0,
\]
using \(B_{n-1}\ge2\). The elementary expansion \(B_m=2+2/m+O(m^{-2})\) implies the covariance tends to \(1/2\). Finally \(\operatorname{Var}(\mathcal R_n)=H_n-H_n^{(2)}\) from independent rank-record indicators, and \(\operatorname{Var}(\mathcal E_n)=(n+1)/12\) from the Eulerian excedance distribution. Together they yield the stated correlation asymptotic.

## Verification

The included `verify.py` uses only standard Python integer and rational arithmetic. Running `python verify.py` enumerates every permutation through size eight and independently checks every record/threshold covariance entry, each local excedance contribution, and each aggregate covariance. It also verifies the inverse-binomial recurrence, sharp signs, and strict monotonicity for orders below 400. The program passes **2,524 exact comparisons**. Finite enumeration does not prove the general formulas; the argument above establishes them for all admissible indices and orders.

## Relationship to prior work

The object and marginal record viewpoint are classical; Gnedin studies coherent permutation laws determined by record statistics. Ehrenborg and Steingrímsson enumerate specified excedance sets. Brändén and Claesson put both record and excedance statistics in a common mesh-pattern framework. Baril gives a joint-statistics-preserving correspondence between ordinary and cyclic permutations involving weak excedances and left-to-right maxima. These are genuine broader statistical frameworks and are not claimed as new. The result here is the evaluated **mixed threshold-by-position covariance kernel**, the consequent exact local profile for ordinary excedances, and its strict order-five covariance sign transition. None of the inspected passages directly gives these evaluated formulas; earlier implicit coverage through a joint enumerator remains a priority risk.

## Limitations

The covariance and correlation assertions concern the uniformly sampled symmetric group, not arbitrary nonuniform permutation laws. The kernel determines only mixed second moments, not the complete joint distribution. The limiting correlation is zero even though limiting covariance is positive. Exhaustive checks stop at eight letters, and the mathematical proof handles unrestricted order. Earlier comprehensive joint generating functions could implicitly imply the theorem, so the historical-priority assessment is not a claim of independent certification.

## References

1. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538v1 (first public version 17 November 2006), https://arxiv.org/abs/math/0611538.
2. R. Ehrenborg and E. Steingrímsson, *The Excedance Set of a Permutation*, *Advances in Applied Mathematics* **24** (2000), 284–299, https://www.ms.uky.edu/~jrge/papers/Excedance.pdf.
3. P. Brändén and A. Claesson, *Mesh patterns and the expansion of permutation statistics as sums of permutation patterns*, *Electronic Journal of Combinatorics* **18** (2011), P5, https://arxiv.org/abs/1102.4226.
4. J.-L. Baril, *Statistics-preserving bijections between classical and cyclic permutations*, *Information Processing Letters* **113** (2013), 17–22, https://jl.baril.u-bourgogne.fr/statistics.pdf.
