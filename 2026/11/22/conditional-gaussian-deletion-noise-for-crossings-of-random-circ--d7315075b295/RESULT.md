# Conditional Gaussian deletion noise for crossings of random circular chords

## Finding

Sample \(n\ge2\) independent chords of a circle, each joining two independent uniformly distributed endpoints. Let \(C_n\) be the number of unordered crossing pairs and let \(D_n\) be the number of chords crossing chord 1, hence the number of crossings lost if chord 1 is deleted. If the positively oriented arc from its first endpoint to its second has length \(T\in[0,1]\) as a fraction of circumference, define \(Q=2T(1-T)\). Then \(T\) is uniform, and \(\mathbb E[D_n\mid T]=(n-1)Q\).

Define the global crossing fluctuation and the *conditionally centered* one-chord deletion fluctuation by
\[
Z_n=\frac{C_n-n(n-1)/6}{n^{3/2}},\qquad W_n=\frac{D_n-(n-1)Q}{\sqrt n}.
\]
As \(n\to\infty\),
\[
(T,Z_n,W_n)\xrightarrow{\mathrm d}(T,Z,W),
\]
where, **conditional on \(T=t\)**, the pair \((Z,W)\) is centered bivariate normal with covariance matrix
\[
\boxed{\Sigma(t)=\begin{pmatrix}
1/45 & q(t)^2/6\\
q(t)^2/6 & q(t)(1-q(t))
\end{pmatrix},\qquad q(t)=2t(1-t).}
\]
Equivalently the joint conditional characteristic function is \(\exp\{-\tfrac12[u^2/45+uvq(t)^2/3+v^2q(t)(1-q(t))]\}\). The first limit coordinate \(Z\) is independent of \(T\) (and of \(Q\)); nevertheless \(Z\) and the second-order deletion noise \(W\) are **not independent**: \(\operatorname{Cov}(Z,W)=1/45>0\). Their limiting conditional covariance is positive for every nondegenerate chord. The unconditional law of \(W\) is a non-Gaussian centered normal scale mixture.

A finite-sample identity, valid for all \(n\ge2\), quantifies the same coupling:
\[
\mathbb E\left[(C_n-\mathbb E C_n)\{D_n-(n-1)Q\}\right]=\frac{(n-1)(n+7)}{45}.
\]
The known one-chord degree limit \(D_n/n\xrightarrow{\mathrm d}Q\), with \(\Pr(Q\le y)=1-\sqrt{1-2y}\) for \(0\le y\le1/2\), and the classical marginal crossing CLT are background, not novelty claims.

## Assumptions and scope

The \(2n\) chord endpoints are independent and uniform in circular arclength, with probability zero of ties. Crossings mean alternating endpoints. Ordering all endpoints and forgetting physical locations gives the uniform perfect-matching chord diagram, so classical fixed-endpoint enumeration applies. The *distinguished chord* is fixed by its sampling label before seeing data; by exchangeability, selecting a chord uniformly afterward gives the same law. All finite formulas below hold for every \(n\ge2\); the weak limit concerns \(n\to\infty\) and is distributional, jointly with the actual first-chord geometry. No claim is made for chords selected according to length-biased or nonuniform rules, spatially dependent chords, or random lines sampled according to a different geometric measure.

## Proof

**1. Conditional crossing kernel.** Represent a chord \(x\) by two unit-circle endpoint coordinates \(u,v\). With \(t=(v-u)\bmod 1\), a second independent chord \(Y\) crosses \(x\) exactly when one of its endpoints belongs to the positively oriented open arc of fraction \(t\) and the other lies outside it. For the symmetric crossing indicator \(H(x,Y)\),
\[
q(t)=\mathbb E[H(x,Y)\mid x]=2t(1-t),\qquad\theta=\mathbb EH(X_1,X_2)=1/3.
\]
The first Hoeffding projection is \(h_1(x)=q(t)-1/3\). Because \(t\) is uniform on \([0,1]\), direct polynomial integration gives
\[
\mathbb Eh_1(X)^2=\int_0^1(2t(1-t)-1/3)^2\,dt=1/45.
\]

**2. The nonstandard conditional cross-projection integral.** Given that a random second chord has oriented endpoint separation \(s\), its starting endpoint is uniform. The probability that it crosses a fixed chord of arc fraction \(t\) is exactly
\[
\Pr(H(x,Y)=1\mid t,s)=2\min\{t,1-t,s,1-s\}.
\]
This follows by measuring the symmetric difference of a length-\(t\) arc and its translate through \(s\). Thus the covariance between the random global first projection and the conditionally centered local indicator is
\[
\begin{aligned}
 a(t)&=\mathbb E[(H(x,Y)-q(t))h_1(Y)]\\
 &=\int_0^1 2\min\{t,1-t,s,1-s\}\bigl(2s(1-s)-1/3\bigr)\,ds\\
 &=\frac23 t^2(1-t)^2=\frac{q(t)^2}{6}.
\end{aligned}
\]
For the last equality, by symmetry take \(0\le t\le1/2\), split the integral at \(s=t\) and \(s=1/2\), and integrate the resulting polynomials. In addition, \(\operatorname{Var}(H(x,Y)\mid x)=q(t)(1-q(t))\).

**3. Global crossing decomposition.** Write \(R_n=\sum_{2\le i<j\le n}H(X_i,X_j)\) for crossings not involving chord 1. Then
\[
R_n-\mathbb ER_n=(n-2)\sum_{i=2}^n h_1(X_i)+\sum_{2\le i<j\le n}h_2(X_i,X_j),
\]
where \(h_2(x,y)=H(x,y)-1/3-h_1(x)-h_1(y)\). It is conditionally mean-zero in each argument. Distinct degenerate terms, even those sharing exactly one index, are uncorrelated. Boundedness therefore gives variance \(O(n^2)\) for the remainder; divided by \(n^{3/2}\) it vanishes in \(L^2\). Since \(C_n=R_n+D_n\), \(\mathbb EC_n=n(n-1)/6\), and \(0\le D_n\le n-1\), it follows that
\[
Z_n-\frac1{\sqrt n}\sum_{i=2}^n h_1(X_i)\xrightarrow{L^2}0.
\]

**4. Conditional multivariate CLT and mixing.** Given the first chord \(x\), the \(n-1\) vectors
\[
\bigl(h_1(X_i),\ H(x,X_i)-q(t)\bigr),\qquad 2\le i\le n,
\]
are independent, identically distributed, bounded, centered, and have covariance matrix \(\Sigma(t)\) by Steps 1–2. Their \(n^{-1/2}\)-normalized sum obeys the ordinary bivariate central limit theorem for each fixed chord \(x\). The \(L^2\) approximation in Step 3 and bounded convergence of conditional characteristic functions, integrated against the distribution of the first chord, establish the joint mixed-normal convergence asserted above. The conditional variance of the first coordinate is the constant \(1/45\), proving its independence from \(T\). Its unconditional covariance with the deletion-noise limit equals
\[
\mathbb E[q(T)^2]/6=\frac16\int_0^1 4t^2(1-t)^2\,dt=1/45.
\]
For \(t\in(0,1)\) the diagonal deletion variance is positive; as it varies nontrivially with \(T\), the marginal \(W\) is a nondegenerate variance mixture of normals, not a single normal law.

**5. Exact finite-sample mixed moment.** Conditioning on the distinguished chord \(x\) gives \(D_n\sim\operatorname{Binomial}(n-1,q(t))\). In the conditional covariance of \(C_n\) and \(D_n\), the \(D_n\) term contributes \((n-1)q(t)(1-q(t))\), and each of the \((n-1)(n-2)\) overlapping ordered pairs of remaining crossing indicators contributes \(a(t)=q(t)^2/6\). Therefore
\[
\mathbb E[(C_n-\mathbb EC_n)(D_n-(n-1)Q)]
=(n-1)\mathbb E[Q(1-Q)]+(n-1)(n-2)\mathbb E[Q^2]/6.
\]
Using \(\mathbb EQ=1/3\), \(\mathbb EQ^2=2/15\) proves the stated \((n-1)(n+7)/45\) identity. No asymptotic interchange is needed for this exact identity.

## Verification

Run \(\texttt{python3 verify.py}\) (Python 3 standard library only). The included checker uses exact rational arithmetic to check the integrated cross-projection identity and positive semidefiniteness at representative rational arc fractions, the first two projection moments, the finite centered-deletion identity for \(2\le n<100\), and the exact crossing-count, crossing-degree, and mixed-moment formulas by exhaustive enumeration of every perfect matching on \(2n\) endpoints for \(2\le n\le6\). The recorded run passed **142 exact assertions**. The exhaustive enumeration is finite corroboration; Step 4 is the proof of infinite weak convergence.

## Relationship to prior work

Flajolet and Noy (2000, Section 2, Theorem 3) established the marginal mean, variance, and Gaussian limit for total crossings. Acan (2015, Section 2, Theorem 2.1) established the one-chord macroscopic degree limit, including the density of \(Q\). Paguyo (2021, revised 2023, Theorems 1.1–1.3) gave rates for the marginal Gaussian crossing and Poisson simple-chord limits. Those statements do not specify the **joint conditional second-order fluctuations** of a distinguished chord's degree and the total crossings.

A published exact regression for total crossings conditional on a marked chord's degree, a published conditional crossing-variance identity, and a published joint CLT for total chord span and crossings were examined as particularly close mathematical comparisons. Their first-moment, second-moment, and *two-global-statistic* conclusions do not state the mixed-normal conditional law for a single chord's \(\sqrt n\)-centered deletion noise. The new component here is the conditional covariance function \(q(t)^2/6\) within that joint limit and the resulting separation of macroscopic independence from second-order dependence, not any marginal result, standard multivariate CLT methodology, or an exact conditional mean alone.

## Limitations

The conditional covariance and mixed-normal law specialize standard Hoeffding/CLT tools to the independent-endpoint chord model; they are not a universal statement for arbitrary geometric models. The result provides weak convergence, not a uniform quantitative approximation or a conditional local limit theorem. Historical uniqueness is not established: an earlier, more general conditioned U-statistic theorem or crossing enumerator might imply the same specialization. No independent audit has been performed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914, public report dated March 4, 2000, Section 2, Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (posted January 7, 2015), Section 2, Theorem 2.1. https://arxiv.org/abs/1501.01489
3. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134v1 (posted April 2, 2021), revised 2023. https://arxiv.org/abs/2104.01134
4. *Universal conditional crossing regression for a marked random chord*, published finding (2026), identifier 7c3b3c68ffff.
5. *Sharp conditional crossing-variance inflation from a prescribed chord*, published finding (2026), identifier 3db04d00c97a.
6. *Joint Gaussian fluctuations of total circular chord span and crossings*, published finding (2026), identifier 25d00b41e332.
