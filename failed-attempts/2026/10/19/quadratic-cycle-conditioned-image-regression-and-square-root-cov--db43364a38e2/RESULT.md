# Quadratic cycle-conditioned image regression and square-root covariance in random mappings

## Finding
Let \(f:[n]\to[n]\) be uniformly random, with independent uniform values \(f(i)\). Write \(C_n\) for the number of vertices lying on directed cycles of \(f\); \(R_n\) for the number of vertices in the image of \(f\); and \(L_n=n-R_n\) for the number of vertices of indegree zero. The following conditional occupancy identity holds **as an equality of distributions**, not merely expectations:

\[
(L_n\mid C_n=c)\;\overset{d}=\;\#\{\text{unhit distinguished boxes}\}
\]

for \(1\le c<n\), when \(n-c-1\) independent balls are placed uniformly in \(n\) boxes, of which \(n-c\) are distinguished. For \(c=n\), \(L_n=0\) deterministically. Thus, for every integer \(0\le s\le n-c\) and \(c<n\),

\[
\mathbb E[(L_n)_s\mid C_n=c]=(n-c)_s\left(1-\frac{s}{n}\right)^{n-c-1},
\qquad
\mathbb E[R_n\mid C_n=c]=n-(n-c)\left(1-\frac1n\right)^{n-c-1}.
\]

The conditional mean is strictly increasing, with **exact neighboring difference**

\[
\mathbb E[R_n\mid C_n=c+1]-\mathbb E[R_n\mid C_n=c]
=\frac{c}{n}\left(1-\frac1n\right)^{n-c-2}>0
\quad(1\le c<n).
\]

Set \(\mu_n=\sum_{j=1}^n(n)_j/n^j\), the expected number of cyclic vertices. Then the **exact finite-size mixed covariance** is

\[
\operatorname{Cov}(C_n,R_n)
=n\left(1-\frac1n\right)^n(\mu_n-\mu_{n-1})>0,
\qquad n\ge2.
\]

Most strikingly, if \(c_n\) is any integer sequence with \(c_n/\sqrt n\to x\ge0\), then the dependence first appears only at **quadratic, second order**:

\[
\mathbb E[R_n\mid C_n=c_n]-\mathbb E R_n
\longrightarrow\frac{x^2-2}{2e}.
\]

As \(n\to\infty\),

\[
\operatorname{Cov}(C_n,R_n)
\sim\frac1e\sqrt{\frac\pi8}\sqrt n,
\qquad
\operatorname{Corr}(C_n,R_n)
\sim\frac{K}{\sqrt n},
\]

where

\[
K=\frac{e^{-1}\sqrt{\pi/8}}{\sqrt{(2-\pi/2)(e^{-1}-2e^{-2})}}
\approx1.12862791585.
\]

The positive unnormalized covariance diverges on a square-root scale, even while correlation tends to zero.

## Assumptions and scope
Throughout, \(n\ge2\) is an integer. The map is sampled uniformly among all \(n^n\) functions; image coordinates are independent and uniform. A cyclic vertex is one belonging to a directed cycle, including a fixed point. An origin is a vertex with indegree zero. The falling factorial \((a)_s=a(a-1)\cdots(a-s+1)\) has value one at \(s=0\). The conditional occupancy construction concerns the origins, not the image vertices. No constraints on fixed points, component counts, or indegrees are imposed. For \(c=n\), the mapping is a permutation and requires the separately stated degenerate case.

## Proof
**1. Conditioning and a forest minor.** Fix the cyclic vertex set \(A\), of cardinality \(c\), and fix the permutation of the cycle edges on \(A\). The other \(m=n-c\) vertices form an oriented forest with its roots in \(A\), with each nonroot pointing toward its parent. The directed matrix-tree theorem, or the standard Cayley rooted-forest identity, gives exactly \(c n^{m-1}\) such forests for \(1\le c<n\); they are equiprobable under the stated conditioning.

Fix \(B\subset[n]\setminus A\) with \(|B|=s\). Requiring that no forest edge target a vertex in \(B\) means that only the \(n-s\) vertices outside \(B\) are permitted parents. Index the forest Laplacian minor by the \(m\) nonroots. Its matrix is \((n-s)I_m-\mathbf1 a^\top\), where \(a_j=1\) when nonroot \(j\notin B\), and zero otherwise. The determinant lemma gives

\[
\det((n-s)I_m-\mathbf1a^\top)
=(n-s)^m\left(1-\frac{m-s}{n-s}\right)
=c(n-s)^{m-1}.
\]

Dividing by \(c n^{m-1}\) yields

\[
\Pr(\text{every element of }B\text{ has indegree zero}\mid C_n=c)
=\left(1-\frac{s}{n}\right)^{m-1}.
\]

No cyclic vertex can have indegree zero, because of its incoming cycle edge. For \(m-1\) independent balls into \(n\) boxes, the chance that a specified \(s\) distinguished boxes are unhit is the same expression. Inclusion–exclusion on every subset of the distinguished boxes identifies the complete binary unhit-indicator law, proving the conditional distribution assertion and every factorial moment. More explicitly, for \(0\le\ell\le m\),

\[
\Pr(L_n=\ell\mid C_n=c)=\binom m\ell
\sum_{j=0}^{m-\ell}(-1)^j\binom{m-\ell}{j}
\left(1-\frac{\ell+j}{n}\right)^{m-1}.
\]

When \(c=n\) there are no noncyclic vertices and every image vertex occurs, so \(L_n=0\).

**2. Exact regression and positivity.** Taking \(s=1\) and using \(R_n=n-L_n\) gives the conditional expectation in the finding. Write \(q=1-1/n\). Direct subtraction at consecutive \(c\) yields \(\frac cn q^{n-c-2}>0\). The conditional distribution of \(C_n\) is nondegenerate for all \(n\ge2\). Since the conditional regression is strictly increasing, \(\operatorname{Cov}(C_n,R_n)=\operatorname{Cov}(C_n,\mathbb E[R_n\mid C_n])>0\) by applying the elementary two-copy covariance identity to the strictly increasing regression function.

**3. Exact mixed covariance.** For a fixed target vertex \(v\), the event \(v\notin f([n])\) has probability \(q^n\). Under this event, the restriction of \(f\) to the other \(n-1\) vertices is a uniform map of that set into itself. Since \(v\) has no incoming edge, it cannot lie on a cycle; its outgoing edge is irrelevant to every other cycle. Consequently,

\[
\mathbb E[C_nL_n]=nq^n\mathbb E C_{n-1}=nq^n\mu_{n-1}.
\]

Also \(\mathbb E L_n=nq^n\), and elementary random-mapping enumeration gives \(\mu_n=\sum_{j=1}^n(n)_j/n^j\). Therefore \(\operatorname{Cov}(C_n,R_n)=-\operatorname{Cov}(C_n,L_n)=nq^n(\mu_n-\mu_{n-1})\), as claimed. The positivity was independently established in step 2.

**4. Quadratic conditional limit.** The unconditional occupancy identity gives \(\mathbb E R_n=n(1-q^n)\). Put \(h_n(c)=\mathbb E[R_n\mid C_n=c]\). A direct evaluation of the case \(c=1\) and telescoping of step 2 yield the exact expression

\[
h_n(c)-\mathbb E R_n=-q^{n-1}
+\sum_{j=1}^{c-1}\frac jn q^{n-j-2}.
\]

For any sequence \(c_n/\sqrt n\to x\in[0,\infty)\), the first term tends to \(-e^{-1}\). Uniformly for \(1\le j<c_n\), the base \(q^{n-j-2}\to e^{-1}\) when \(c_n=O(\sqrt n)\). Hence the sum tends to \(e^{-1}x^2/2\), proving the quadratic limit for all specified integer sequences.

**5. Square-root covariance and correlation.** Counting a cyclic set, its permutation, and the rooted forest gives the exact law

\[
\Pr(C_n=c)=\frac{c(n)_c}{n^{c+1}},
\qquad 1\le c\le n.
\]

The standard birthday-product bound \((n)_c/n^c\le\exp[-c(c-1)/(2n)]\) supplies Gaussian-decaying tails for \(C_n/\sqrt n\). Therefore these variables converge in distribution with all fixed moments to a Rayleigh random variable \(X\) with density \(xe^{-x^2/2}\) for \(x>0\). In particular, \(\mathbb E X=\sqrt{\pi/2}\), \(\mathbb E X^2=2\), \(\mathbb E X^3=3\sqrt{\pi/2}\), and \(\operatorname{Var}(X)=2-\pi/2\).

The exact telescoping formula in step 4 bounds \(|h_n(c)-\mathbb E R_n|\le1+c^2/(2n)\) for all \(1\le c\le n\). Together with uniform Rayleigh-tail moment bounds, this permits convergence of mixed expectations after replacing \(c\) by \(C_n\). Thus

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,R_n)}{\sqrt n}
=\operatorname{Cov}\left(X,\frac{X^2-2}{2e}\right)
=\frac{\mathbb E X^3-\mathbb E X\,\mathbb E X^2}{2e}
=\frac1e\sqrt{\frac\pi8}.
\]

Finally, \(R_n\) is the number of occupied boxes after \(n\) independent uniform throws into \(n\) boxes. Covariances of the occupancy indicators give \(\operatorname{Var}(R_n)/n\to e^{-1}-2e^{-2}>0\). The Rayleigh limit gives \(\operatorname{Var}(C_n)/n\to2-\pi/2\). Dividing the covariance asymptotic by the square root of these two variances yields the stated correlation coefficient.

## Verification
The included standalone Python standard-library program `verify_mapping.py` exhaustively checks all mappings of sets of sizes two through six against the conditional occupancy distribution, its factorial moments, the exact means, and the mixed covariance formula. It also checks the exact increasing-regression identity at many parameters and compares the covariance to its square-root limit. Run `python3 verify_mapping.py` in the extracted package directory. The exhaustive computation covers only those finite sizes; the determinant argument, telescoping identity, and moment bounds provide the claims for all \(n\ge2\).

## Relationship to prior work
The 2010 paper of Hansen and Jaworski conditions on a prescribed number of cyclic points and studies the sizes and limiting structure of components. Its root-forest representation supplies the natural probabilistic setting here, but its investigated claims do not provide the origin-indicator occupancy law, the exact image-versus-cycles mixed covariance, or the quadratic scale of their conditional dependence. Arney and Bender (1982) provide extensive enumerations of origins and cyclic points under indegree restrictions; their enumerative tools could in principle be specialized to obtain related joint information, and there is no claim that forest enumeration itself is new. Flajolet and Odlyzko (1990) present marginal means and distributional methods for cyclic and terminal vertices. The additional contribution assessed here is the complete conditional occupancy representation combined with a second-order parabolic regression and explicit cross-covariance/correlation coefficients. Published results concerning fixed points and indegree extremes are not directly comparable to the total cyclic-point/image-size pairing.

## Limitations
The theorem concerns uniform random maps with iid uniform outputs; in-degree constrained or exchangeable but nonuniform mapping models are not covered. The conditional quadratic limit assumes \(c_n/\sqrt n\to x<\infty\); it does not assert a uniform approximation for all \(c\) up to \(n\). The asymptotics are not a central limit theorem for the pair. The exact occupancy representation can potentially be recovered from classical rooted-forest enumeration, so prior implicit coverage of parts of the claim is a genuine originality risk. Reproducibility computations are finite corroboration, not a replacement for proof. No independent scientific audit has been performed.

## References
1. J. C. Hansen and J. Jaworski, "Random Mappings with a Given Number of Cyclical Points," *Ars Combinatoria* 94 (2010), pp. 341–359. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ (publisher states January 31, 2010).
2. J. Arney and E. A. Bender, "Random Mappings with Constraints on Coalescence and Number of Origins," *Pacific Journal of Mathematics* 103 (1982), pp. 269–294. https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-p.pdf
3. P. Flajolet and A. M. Odlyzko, "Random Mapping Statistics," *Advances in Cryptology EUROCRYPT '89*, published 1990. https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf
