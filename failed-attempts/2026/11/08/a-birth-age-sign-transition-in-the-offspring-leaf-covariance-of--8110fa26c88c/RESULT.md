# A birth-age sign transition in the offspring–leaf covariance of recursive trees

## Finding

Let \(T_n\) be a uniform random recursive tree on the arrival-labelled vertices \(1,\ldots,n\), with \(n\ge3\). For each \(2\le i\le n\), let \(D_{n,i}\) be the number of children of vertex \(i\), and let \(L_n\) be the total number of vertices with no children. Put \(H_m=\sum_{r=1}^{m}1/r\), with \(H_0=0\). The entire nonroot birth-label covariance profile is

\[
\operatorname{Cov}(D_{n,i},L_n)
=\frac{(n-i)/2-(i-1)(H_{n-2}-H_{i-2})}{n-1}.
\tag{1}
\]

The profile has a **sharp birth-age sign change**. For \(3\le n\le6\), it is strictly negative for every \(2\le i\le n-1\). For \(n\ge7\), it is positive at \(i=2\), negative at \(i=n-1\), and its signs as \(i\) increases through \(2,\ldots,n-1\) consist of an initial positive interval, at most one zero, then a negative interval. At \(i=n\), the covariance is zero because \(D_{n,n}=0\).

Define \(m_n\) for \(n\ge7\) as the last label in \(\{2,\ldots,n-1\}\) with positive covariance. Then

\[
\lim_{n\to\infty}\frac{m_n}{n}=\rho,
\qquad \frac{1-\rho}{2}+\rho\log\rho=0,
\qquad \rho\in(0,1),\quad \rho\approx0.2846681370408384.
\tag{2}
\]

The local mechanism is exact: if \(A_{i,j}=\mathbf1\{j\text{ attaches to }i\}\) for \(2\le i<j\le n\), then

\[
\operatorname{Cov}(A_{i,j},L_n)
=\frac{1/2-(i-1)/(j-2)}{n-1}.
\tag{3}
\]

Hence the covariance for a single future attachment is negative for \(j<2i\), zero for \(j=2i\), and positive for \(j>2i\) (subject to \(j\le n\)). The global sign transition is the aggregate of these opposing influences.

For each fixed \(0<t<1\), with \(i_n/n\to t\), the scaled-profile limit is

\[
\operatorname{Cov}(D_{n,i_n},L_n)\longrightarrow
 g(t):=\frac{1-t}{2}+t\log t.
\tag{4}
\]

Moreover the correlation is of order \(n^{-1/2}\) at proportional birth ages, and specifically

\[
\sqrt n\,\operatorname{Corr}(D_{n,i_n},L_n)
\longrightarrow\frac{\sqrt{12}\,g(t)}{\sqrt{-\log t}}.
\tag{5}
\]

## Assumptions and scope

The model starts with vertex \(1\). For every \(j\in\{2,\ldots,n\}\), independently choose its parent \(P_j\) uniformly from \(\{1,\ldots,j-1\}\). Orient parent edges away from the root. A **leaf** is a vertex of outdegree zero. The root has child \(2\) deterministically, so it is never a leaf for \(n\ge2\). The result concerns the offspring count of each **nonroot** vertex. The root-only covariance has previously been treated separately and is not claimed here as new.

The covariances are population covariances under the uniformly weighted \((n-1)!\) recursive trees. No distributional approximation or independence assumption between leaves is used in the exact formulas.

## Proof

**1. Leaf probabilities.** For \(2\le k\le n\), vertex \(k\) remains childless precisely when none of \(P_{k+1},\ldots,P_n\) equals \(k\). Independence of these parent choices gives

\[
\Pr(k\text{ is a leaf})
=\prod_{r=k+1}^{n}\frac{r-2}{r-1}=\frac{k-1}{n-1}.
\tag{6}
\]

Consequently \(\mathbb EL_n=n/2\).

**2. One forced parent choice.** Fix \(2\le i<j\le n\), and condition on \(A_{i,j}=1\). Vertex \(i\) is no longer a leaf. For any other potential leaf \(k\) with \(2\le k<j\), independence of the parent choices and the exclusion \(P_j\ne k\) multiply its original leaf probability by \((j-1)/(j-2)\). For \(k\ge j\), the leaf probability is unchanged. Thus

\[
\mathbb E[L_n\mid A_{i,j}=1]-\mathbb EL_n
=\frac{\sum_{k=2}^{j-1}(k-1)-(i-1)}{(n-1)(j-2)}
 -\frac{i-1}{n-1}.
\]

Since \(\Pr(A_{i,j}=1)=1/(j-1)\), multiplying this difference by \(1/(j-1)\) and simplifying gives (3). The three-way sign rule follows immediately by comparing \(j\) with \(2i\).

**3. Full covariance.** The identity

\[
D_{n,i}=\sum_{j=i+1}^{n}A_{i,j}
\]

and linearity of covariance give

\[
\operatorname{Cov}(D_{n,i},L_n)
=\frac{1}{n-1}\sum_{j=i+1}^{n}
 \left(\frac12-\frac{i-1}{j-2}\right),
\]

which is exactly (1), including the empty sum at \(i=n\).

**4. Exact shape and finite sign threshold.** Define \(F_{n,i}=(n-1)\operatorname{Cov}(D_{n,i},L_n)\). Direct subtraction yields

\[
F_{n,i+1}-F_{n,i}
=\frac12-\sum_{r=i}^{n-2}\frac1r,
\qquad
F_{n,i+2}-2F_{n,i+1}+F_{n,i}=\frac1i>0
\quad(2\le i\le n-2).
\tag{7}
\]

Thus the sequence is strictly discretely convex. Its last two terms are \(F_{n,n-1}=-1/2\) and \(F_{n,n}=0\). The first term is

\[
F_{n,2}=\frac{n-2}{2}-H_{n-2}.
\]

This first term is negative for \(3\le n\le6\), equals \(-1/12\) at \(n=6\), and equals \(13/60>0\) at \(n=7\). Its increment when \(n\) increases to \(n+1\) is \(1/2-1/(n-1)>0\) for \(n\ge4\). For \(n\le6\), strict convexity and the nonpositive endpoint values force every interior \(F_{n,i}\) to be negative. For \(n\ge7\), strict convexity and the positive first, negative penultimate, and zero final values show that an initial positive block gives way to a negative block, with at most one zero between them. (Strictly increasing first differences prohibit a second interior sign reversal.) This proves the full finite classification.

**5. Limiting transition.** For \(i_n/n\to t\in(0,1)\), the harmonic-number difference satisfies \(H_{n-2}-H_{i_n-2}\to-\log t\); dividing (1) by its displayed denominator proves (4). The continuous function \(g(t)=(1-t)/2+t\log t\) is strictly convex because \(g''(t)=1/t>0\); also \(g(0+)=1/2\), \(g(1)=0\), and \(g'(1)=1/2>0\). It therefore has exactly one zero inside \((0,1)\), is positive below it and negative above it until \(1\). Evaluating at two rational interior points brackets that root, and elementary numerical bisection produces the displayed decimal. The finite single-boundary property and pointwise profile convergence on either side of that zero imply \(m_n/n\to\rho\).

**6. Correlation scale.** The independent parent indicators yield

\[
\operatorname{Var}(D_{n,i})
=\sum_{r=i}^{n-1}\left(\frac1r-\frac1{r^2}\right)
\longrightarrow-\log t.
\]

For leaf count, adding vertex \(m+1\) increases the count by one if and only if the selected parent is not a leaf. Conditionally on \(L_m\), the probability of selecting a leaf equals \(L_m/m\). With \(\mathbb EL_m=m/2\), total variance gives

\[
\operatorname{Var}(L_{m+1})
=\left(1-\frac2m\right)\operatorname{Var}(L_m)+\frac14.
\]

Using \(\operatorname{Var}(L_3)=1/4\), induction shows \(\operatorname{Var}(L_n)=n/12\) for every \(n\ge3\). Combining this with (4) proves (5).

## Verification

The included `verify.py` exhaustively enumerates all parent-choice vectors for orders \(3\le n\le8\), computes rational joint moments and covariances, compares with (1) and (3), checks the exact leaf mean and variance, and verifies the strict-convexity and finite sign conditions through order \(150\). It also checks the limiting zero and several asymptotic-profile evaluations. Execute `python3 verify.py` with Python 3 and the standard library. Its output is `VERIFY_OK 11429 exact finite or profile assertions`. The asymptotic numerical checks support rather than replace steps 5–6 of the proof.

## Relationship to prior work

General random recursive tree leaf laws and asymptotic degree-count covariances are classical; Janson studies covariances of **numbers of vertices of given outdegree**, not covariance with the offspring count of a specified birth label. Desmarais–Holmgren–Wagner study urn limits for leaves under broadcasting-induced colourings of attachment trees. Saunders separately computes expected leaf counts and expected root degrees for a model permitting deletion. A publicly indexed result gives the *root-only* covariance \((n-2)/(2(n-1))\), which is not part of the present nonroot claim. The distinctive statements here are the exact all-nonroot-label covariance law, the birth-time local sign rule, the first finite sign transition at order seven, the strictly convex birth-label profile, and the universal limiting threshold \(\rho\).

## Limitations

The result concerns uniform attachment without deletion, not general preferential attachment. The correlation in (5) tends to zero for proportional birth labels even though the sign transition persists at the covariance scale. Earlier work may contain equivalent fixed-birth-label mixed moments under another notation; priority has not been independently established. The exhaustive checks cover only finite test ranges and do not independently certify the mathematical proof. No independent external audit has been performed.

## References

1. C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1 (28 October 2021), https://arxiv.org/abs/2110.15050.
2. S. Janson, *Asymptotic degree distribution in random recursive trees*, *Random Structures & Algorithms* 26 (2005), 69–83, DOI:10.1002/rsa.20046, author preprint https://www2.math.uu.se/~svantejs/papers/sj155.pdf.
3. A. T. Saunders, *A class of random recursive tree algorithms with deletion*, arXiv:1906.02720 (6 June 2019), https://arxiv.org/abs/1906.02720.
