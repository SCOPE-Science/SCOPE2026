# Two-extremum rigidity and a persistent boundary overshoot for Bernstein Boolean sums

## Finding

For every integer \(n\ge2\), the degree-\(n\) classical Bernstein operator on \([0,1]\) is
\[
B_nf(x)=\sum_{k=0}^n f(k/n)\binom nk x^k(1-x)^{n-k}.
\]
The second Boolean sum is \(T_n=2B_n-B_n^2\). Write \(s_j(k/n)=\mathbf1_{\{k\ge j\}}\) and \(g_{n,j}=T_ns_j\), for \(1\le j\le n\). Then **every interior step response** \(g_{n,j}\) with \(1<j<n\) has exactly two critical points in \((0,1)\), a strict minimum below zero followed by a strict maximum above one. Each boundary step response has exactly one critical point: a strict maximum above one for \(j=1\), or a strict minimum below zero for \(j=n\).

Consequently the exact (attained) operator coefficient on real functions of bounded variation is the finite algebraic extremal formula
\[
K_n:=\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(T_nf)}{\operatorname{Var}(f)}
=2\max_{1\le j\le n}\left(\max_{0\le x\le1}g_{n,j}(x)-\min_{0\le x\le1}g_{n,j}(x)\right)-1.
\]
The extrema on the right are obtained by finding at most two real roots in \((0,1)\) of explicitly given degree-\(n-1\) polynomials; step data attain the sharp coefficient. In particular \(K_2=13/12\).

For the first step \(j=1\), let \(a=1-e^{-1}\) and \(u_*=e\log(2/a)\). Its unique maximizing point \(x_n\) obeys \(nx_n\to u_*\), and the boundary-step amplification has the exact nonvanishing limit
\[
\lim_{n\to\infty}\operatorname{Var}(g_{n,1})
=1+\frac2e\left(\frac{1-e^{-1}}2\right)^{e-1}
=1.101671506045\ldots.
\]
Hence \(\liminf_{n\to\infty}K_n\) is at least this constant. This is **not** a claimed asymptotic formula for the global maximization over all jump positions.

## Assumptions and scope

All inputs are real-valued functions on \([0,1]\) of finite classical total variation, with their actual values at the \(n+1\) grid nodes used in the Bernstein sum. The operator acts on this seminormed space modulo constants; no continuity of the input is required. The notation \(B_n^2\) means composition \(B_n\circ B_n\), not polynomial squaring. At interpolation nodes, the step convention is \(s_j(k/n)=1\) precisely for \(k\ge j\). For \(1\le j\le n\) and \(0\le k\le n\), put
\[
q_{j,k}=\sum_{\ell=j}^n\binom n\ell(k/n)^\ell(1-k/n)^{n-\ell},\qquad
b_{n,k}(x)=\binom nk x^k(1-x)^{n-k}.
\]
At \(k=0,n\), the binomial expression has its usual deterministic interpretation.

## Proof

**1. Exact jump polynomial.** Since \(B_ns_j(k/n)=q_{j,k}\), linearity yields
\[
g_{n,j}(x)=\sum_{k=0}^n\left(2\mathbf1_{\{k\ge j\}}-q_{j,k}\right)b_{n,k}(x).
\]
The binomial tail is strictly increasing in its success probability in \((0,1)\). Thus \(\Delta q_{j,k}:=q_{j,k+1}-q_{j,k}\in(0,1)\) for every \(0\le k<n\). The Bernstein derivative identity consequently gives
\[
g'_{n,j}(x)=n\sum_{k=0}^{n-1}\left(2\mathbf1_{\{k=j-1\}}-\Delta q_{j,k}\right)b_{n-1,k}(x).
\]
Every coefficient is strictly negative except the one at \(k=j-1\), which is strictly positive.

**2. All-degree critical-point classification.** Substitute \(t=x/(1-x)>0\) and divide the derivative by \(n(1-x)^{n-1}\). The result is a real polynomial in \(t\) whose coefficient signs are negative, positive, negative for an interior jump and positive, negative or negative, positive for the respective endpoint jumps. Descartes' sign rule gives at most two positive roots in the first case and at most one in the endpoint cases, counting multiplicities. For interior \(j\), both endpoint derivatives are strictly negative. However \(g_{n,j}(1)-g_{n,j}(0)=1\), so \(g'\) is positive somewhere. Continuity forces at least two crossings; consequently there are exactly two simple roots and the sign pattern is negative, positive, negative. Since the endpoint values are zero and one, the local minimum lies below zero and the later maximum above one. For \(j=1\), the left endpoint derivative is positive and the right endpoint derivative negative, which gives one simple positive-to-negative crossing and maximum above one; for \(j=n\) reflect the grid. There can be no other critical points.

**3. Sharp variation norm.** For nodal data \(f_k=f(k/n)\), the telescoping representation is \(f_k=f_0+\sum_{j=1}^n(f_j-f_{j-1})s_j(k/n)\). Because \(T_n1=1\), we have \(T_nf=f_0+\sum_j(f_j-f_{j-1})g_{n,j}\). The variation triangle inequality shows \(\operatorname{Var}(T_nf)\le(\max_j\operatorname{Var}(g_{n,j}))\sum_j|f_j-f_{j-1}|\le(\max_j\operatorname{Var}(g_{n,j}))\operatorname{Var}(f)\). Each step input has variation one, proving equality for the operator norm. With the derivative signs from step 2, the path starts at zero, visits its minimum and then maximum, and finishes at one (with degenerate endpoint cases). Summing its three monotone increments gives \(\operatorname{Var}(g_{n,j})=2(\max g_{n,j}-\min g_{n,j})-1\). The extrema are algebraic because the derivative coefficients are rational; this yields the asserted exact finite prescription. For \(n=2\), \(g_{2,1}(x)=\tfrac52x-\tfrac32x^2\), whose maximum \(25/24\) at \(5/6\) gives \(K_2=13/12\) by symmetry.

**4. Boundary-layer limit.** For \(j=1\), the tail simplifies to \(q_{1,k}=1-(1-k/n)^n\), so
\[
g_{n,1}(x)=1-2(1-x)^n+\sum_{k=0}^n(1-k/n)^n b_{n,k}(x).
\]
For fixed \(u\ge0\), the binomial weights \(b_{n,k}(u/n)\) converge to \(e^{-u}u^k/k!\) for each fixed \(k\); the factors \((1-k/n)^n\) converge to \(e^{-k}\). Their values lie in \([0,1]\), so Poisson tightness yields convergence, uniformly for \(u\) on compact sets, to
\[
G(u)=1-2e^{-u}+e^{-a u},\qquad a=1-e^{-1}.
\]
The derivative coefficients from step 1, together with \(n^{-1}g'_{n,1}(u/n)\), converge by the same binomial-to-Poisson argument uniformly on compact sets to \(G'(u)=2e^{-u}-ae^{-a u}\). The latter changes sign once, positive to negative, at \(u_*=\log(2/a)/(1-a)=e\log(2/a)\). Choose any positive \(u_-<u_*<u_+\). For all sufficiently large \(n\) the two rescaled derivatives have opposite signs at \(u_-\) and \(u_+\); by the unique finite-degree derivative zero, \(u_-<nx_n<u_+\). Letting these choices approach \(u_*\) gives \(nx_n\to u_*\) and \(g_{n,1}(x_n)\to G(u_*)\). Since \(e^{-u_*}=(a/2)^e\) and \(e^{-au_*}=(a/2)^{e-1}\), the overshoot is \(G(u_*)-1=e^{-1}(a/2)^{e-1}\). The one-maximum variation identity from step 3 proves the stated limit.

## Verification

The accompanying standalone Python program `check_boolean.py` uses exact rational arithmetic to construct the step coefficients, validates their signed derivative patterns for every jump at degrees 2 through 16, and checks explicit low-degree formulas. Numerical root isolation independently compares all step-response variation identities through degree 10 and tracks the first-step boundary extremum for degrees 20, 50, 100, and 200. The program prints `ALL_BERNSTEIN_BOOLEAN_SUM_CHECKS_PASS` on successful completion. These bounded computations corroborate but do not establish the all-degree or limit statements; those follow from the proof above.

## Relationship to prior work

Bernstein iterated Boolean sums and their approximation-error advantages are classical. Raşa (2006) analyzes semigroup-related iterated Boolean sums and convergence rates; Draganov (2014) studies weighted and unweighted simultaneous approximation rates for Bernstein Boolean sums. The result here concerns the exact structure of **discontinuous jump responses in total variation**, their algebraically computable sharp norms, and a nonvanishing microscopic boundary layer. These are not consequences of the cited smoothness/error estimates without additional arguments. Cheng–Zhou (2019) and Draganov (2022) subsequently give strong/direct/converse approximation inequalities for the same Boolean-sum family on continuous functions, not a discontinuous-step sharp BV norm. Earlier approximation papers of Agrawal–Kasana (1984) and Gonska–Zhou (1994) are identified as potentially relevant historical sources; their full texts were not available for decisive comparison.

## Limitations

The formula for each finite-degree sharp coefficient is an algorithmic algebraic characterization, not an elementary closed expression in \(n\). The explicit limiting constant concerns only the first (and reflected last) jump and yields a lower bound for the global limiting norm, not its sharp asymptotic. This result does not address complex-valued variation or more than twofold Boolean sums. Historical priority is qualified by inaccessible early full texts; no independent audit has been performed.

## References

1. I. Raşa, “Iterated boolean sums of Bernstein and related operators,” *Rev. Anal. Numér. Théor. Approx.* **35** (2006), 111–115, https://doi.org/10.33993/jnaat351-1018 (lawful open full text: https://ictp.acad.ro/jnaat/journal/article/download/2006-vol35-no1-art15/Rasa-pdf/1018).
2. B. R. Draganov, “On Simultaneous Approximation by Iterated Boolean Sums of Bernstein Operators,” *Results in Mathematics* **66** (2014), 21–41, published online 20 May 2014, https://doi.org/10.1007/s00025-014-0389-z (author full text: https://fmi.uni-sofia.bg/sites/default/files/users/u847/bernsim10.pdf).
3. P. N. Agrawal and H. S. Kasana, “On the iterative combinations of Bernstein polynomials,” *Demonstratio Mathematica* **17** (1984), 777–783, https://doi.org/10.1515/dema-1984-0320 (bibliographic evidence; full text not inspected).
4. H. H. Gonska and X.-L. Zhou, “Approximation theorems for the iterated Boolean sums of Bernstein operators,” *Journal of Computational and Applied Mathematics* **53** (1994), 21–31, https://doi.org/10.1016/0377-0427(92)00133-T (bibliographic evidence; full text not inspected).
5. L. Cheng and X. Zhou, “Strong inequalities for the iterated Boolean sums of Bernstein operators,” *Studia Universitatis Babeș-Bolyai Mathematica* **64** (2019), 299–304, https://doi.org/10.24193/subbmath.2019.3.01 (abstract and theorem description available; full text not inspected).
6. B. R. Draganov, “A strong converse inequality for the iterated Boolean sums of the Bernstein operator,” *Studia Universitatis Babeș-Bolyai Mathematica* **67** (2022), 591–598, https://doi.org/10.24193/subbmath.2022.3.10 (open full text: https://www.cs.ubbcluj.ro/journal/studia-mathematica/journal/article/view/772/pdf_1).
