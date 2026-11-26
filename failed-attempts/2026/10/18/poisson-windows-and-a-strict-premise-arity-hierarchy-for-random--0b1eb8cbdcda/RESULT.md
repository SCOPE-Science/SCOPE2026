# Poisson windows and a strict premise-arity hierarchy for random attribute implications

## Finding
For every **fixed integer** \(k\ge2\), take an \(n\)-object, \(m=m_n\)-attribute formal context whose incidences are mutually independent fair Bernoulli bits. Let \(W_{n,k}\) count the labelled single-conclusion valid implications \(A\to b\) with exactly \(k\) distinct attributes in the premise \(A\) and \(b\notin A\). Set
\[
q_k=1-2^{-(k+1)},\quad \rho_k=q_k^{-1/(k+1)},\quad \lambda_{n,k}=\binom{m}{k}(m-k)q_k^n.
\]
Then the following statements hold.

1. **Critical Poisson window:** If \(m_n/\rho_k^n\to t\in(0,\infty)\), then
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(W_{n,k}),\operatorname{Poisson}(\lambda_{n,k})\bigr)\to0,
 \qquad W_{n,k}\Rightarrow\operatorname{Poisson}(t^{k+1}/k!).
\]
In particular the probability of at least one such implication tends to \(1-\exp(-t^{k+1}/k!)\).
2. **Sharp threshold:** If \(m_n/\rho_k^n\to0\), then \(W_{n,k}=0\) with probability tending to one; if \(m_n/\rho_k^n\to\infty\), then \(W_{n,k}>0\) with probability tending to one.
3. **Strict premise hierarchy and nonvacuity:** In the critical window, with probability tending to one, there is **no** valid implication with any strictly smaller premise (including the empty premise), and every \(k\)-element premise has a nonempty object support. Thus every implication counted by \(W_{n,k}\) has positive support and an inclusion-minimal premise. Furthermore \(\rho_1>\rho_2>\cdots>1\), so successively larger fixed premises appear at strictly smaller exponential attribute scales.

## Assumptions and scope
The number \(k\) is fixed independently of \(n\); \(n\to\infty\), and the labelled attribute count \(m_n\ge k+1\) is arbitrary in the threshold statements. Each row of the context is an independent uniformly random bit vector, and rows are independent. A valid implication \(A\to b\) means that for every object, if all attributes of \(A\) are present, then \(b\) is present. It is **nontrivial** because \(b\notin A\). Its premise is *proper* when no strict subset of \(A\) implies \(b\). Positive support means some object possesses all attributes of \(A\). Identical attribute columns are allowed. The assertion about absence of all smaller-arity implications is **only** made in the finite-\(t\) critical window; it is not asserted above the critical window.

## Proof
Put \(r=k+1\), \(a=2^{-r}\), and \(q=1-a\). Index candidate rules by \(\alpha=(A,b)\), where \(|A|=k\), \(b\notin A\), and \(T_\alpha=A\cup\{b\}\) has size \(r\). A rule fails at a specified object only when all its premise coordinates equal one and its head equals zero; this event has probability \(a\). It follows from independence between objects that
\[
 \mathbb P(E_\alpha)=q^n,\qquad \mathbb EW_{n,k}=\binom mk(m-k)q^n=\lambda_{n,k}.
\]
For distinct rules \(\alpha,\beta\), write \(s=|T_\alpha\cap T_\beta|\). If \(s=0\), the events are independent. If \(1\le s<r\), both forbidden row patterns can occur simultaneously with probability at most \(2^{-(2r-s)}=a^2 2^s\): they are either incompatible or agree on every common coordinate and then fix all \(2r-s\) involved bits. Therefore
\[
 \mathbb P(E_\alpha\cap E_\beta)\le v_s^n,\qquad v_s:=1-2a+a^2 2^s.
\]
For \(s=r\), distinct rules have distinct heads on the same support and their forbidden patterns are incompatible, giving the exact joint probability \((1-2a)^n\). The key strict overlap inequalities are
\[
 v_s<q^{2-s/r}\quad(1\le s<r),\qquad 1-2a<q.
\]
Indeed \(f(x)=\log(1-2a+a^2 2^x)\) is strictly convex for real \(x\in[0,r]\), while \(f(0)=2\log q\) and \(f(r)=\log q\). Strict convexity puts \(f(s)\) below its chord for all interior integer \(s\).

For every fixed rule \(\alpha\), declare its dependency neighborhood to consist of rules sharing at least one attribute from \(T_\alpha\), together with itself. This is a valid dependency graph because disjoint column sets are independent. The number of ordered distinct rule pairs with \(s\) shared columns is at most \(C_r m^{2r-s}\), and the number for \(s=r\) is at most \(C_r m^r\), for a finite constant depending only on \(r\). The standard dependency-graph Stein–Chen total-variation bound has two sums \(b_1\) and \(b_2\), with terms \(\mathbb P(E_\alpha)\mathbb P(E_\beta)\) and \(\mathbb P(E_\alpha E_\beta)\), respectively. At \(m\asymp q^{-n/r}\),
\[
 b_1\le C_r\sum_{s=1}^{r}m^{2r-s}q^{2n}=o(1),
\]
and
\[
 b_2\le C_r\left(\sum_{s=1}^{r-1}m^{2r-s}v_s^n+m^r(1-2a)^n\right)=o(1)
\]
by the strict overlap inequalities. Since \(\lambda_{n,k}\to t^r/k!\), this proves total-variation Poisson convergence. The mean itself has the claimed limit because \(m\sim t q^{-n/r}\).

Below the window, \(\lambda_{n,k}\to0\), so Markov's inequality gives no rules. Above it, let \(\mu=\mathbb EW_{n,k}\to\infty\). Using the same overlap counts, the variance satisfies
\[
 \frac{\operatorname{Var}(W_{n,k})}{\mu^2}\le\frac1\mu+C_r\sum_{s=1}^{r-1}m^{-s}(v_s/q^2)^n+C_rm^{-r}((1-2a)/q^2)^n.
\]
For \(m/q^{-n/r}\to\infty\), every right-hand term tends to zero by the strict overlap inequalities. Chebyshev's inequality then shows \(\mathbb P(W_{n,k}=0)\to0\).

Finally, for each \(h<k\), the expected count of valid \(h\)-premise implications is
\[
 \binom mh(m-h)\left(1-2^{-(h+1)}\right)^n.
\]
The function \(u\mapsto -\log(1-2^{-u})/u\) is strictly decreasing for positive \(u\): its numerator is positive and strictly decreasing, while the denominator increases. Therefore \(\rho_h>\rho_k\), so in the critical \(k\)-window these expectations vanish. This includes \(h=0\). For each specified \(k\)-element premise, the probability its support is empty equals \((1-2^{-k})^n\). Thus the expected number of empty-support premises equals \(\binom mk(1-2^{-k})^n=o(1)\), since \(\rho_k<\rho_{k-1}=(1-2^{-k})^{-1/k}\). A final union bound proves simultaneous lower-arity absence and positive support. Any remaining valid \(k\)-ary rule therefore has a proper, supported premise.

## Verification
The standalone `verify.py` recomputes exact expectations directly from complete small incidence matrices and independently checks all pair-overlap probabilities and strict convexity bounds for fixed arities \(k=2,3,4\). It returns `FINITE_EXPECTATION_OK 12`, `OVERLAP_OK 1585`, `VERIFY_OK`. These finite checks do not replace the analytic limit proof. To reproduce, use a standard Python 3 interpreter and run `python verify.py`. The checker requires only the standard library.

## Relationship to prior work
Bérczi, Boros, Čepek, Kučera, and Makino (2020) develop structural and algorithmic theory of Horn functions and minimal keys. Neves and collaborators (2020) study extracting proper implications from formal contexts, including synthetic examples. Neither inspected text provides this random-context Poisson window or strict arity hierarchy.

The **unary** case \(k=1\) is deliberately excluded from the claim of novelty: the subset-comparability threshold and Poisson law go back to Rényi and are proved in modern form by Dudley Stark (2004). Stark also sketches the dependency-graph method for other Boolean relations and credits Bognár's earlier general random-set relations; the present proof uses that established technique but supplies the explicit fixed-arity Horn-implication statement, its strict overlap inequality, proper-premise property and separated threshold scales. Since an older general statement may imply part of this result, the claim does not assert absolute priority.

## Limitations
The theorem assumes iid fair incidences and fixed finite premise arity; no claims are made for changing arity, arbitrary dependence, biased incidences, or simultaneous asymptotic counts across multiple growing arities. The literature comparison is best-knowledge, not an exhaustive priority guarantee: Bognár's *On Random Sets* (1962) is a materially relevant older general treatment whose full original text was not inspected, so coverage remains a residual risk. The finite verifier is bounded and supplies no infinite-size certification.

## References
- K. Bérczi, E. Boros, O. Čepek, P. Kučera, K. Makino, *Unique key Horn functions* (first public version 2020-02-17), arXiv:2002.06964, https://arxiv.org/abs/2002.06964.
- J. C. V. Neves et al., *Exploring Different Paradigms to Extract Proper Implications From High Dimensional Formal Contexts* (2020), DOI:10.1109/ACCESS.2020.3010482.
- D. Stark, *Convergence in Distribution for Subset Counts Between Random Sets*, Electronic Journal of Combinatorics 11 (2004), R59, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r59/pdf/.
- K. Bognár, *On Random Sets*, Magyar Tud. Akad. Mat. Kutató Intézetének Közleményei 7 (1962), 425–440; cited in Stark (2004). Original full text not inspected.
