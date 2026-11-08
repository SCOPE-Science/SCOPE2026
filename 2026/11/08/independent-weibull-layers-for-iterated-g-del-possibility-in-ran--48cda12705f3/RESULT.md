# Independent Weibull layers for iterated Gödel possibility in random fuzzy frames

## Finding
Fix an integer \(K\ge1\). In an \(n\)-world Gödel Kripke model, choose all \(n^2\) directed accessibility grades independently uniformly on \([0,1]\), and independently choose the grade of one proposition \(p\) at each world uniformly on \([0,1]\). Fix root \(o\). Write \(D_{n,k}=e(o,\Diamond^k p)\), where \(1\le k\le K\) and \(\Diamond\) is the Gödel max–min modality. Then
\[
\big(n^{1/2}(1-D_{n,1}),\ n^{2/3}(1-D_{n,2}),\ldots,\ n^{K/(K+1)}(1-D_{n,K})\big)
\ \xrightarrow{\ d\ }\ (Y_1,\ldots,Y_K),
\]
where the limiting random variables are **independent**, and for every \(x\ge0\),
\[
\Pr(Y_k>x)=\exp(-x^{k+1}).
\]
More quantitatively, for fixed \(K\) and fixed nonnegative \(x_1,\ldots,x_K\), the joint upper-orthant probability differs from \(\exp(-\sum_{k=1}^K x_k^{k+1})\) by \(O_{K,\mathbf x}(n^{-1/(K+1)})\). The statement concerns the same random accessibility grades and the **same** propositional valuation at every depth, not independent resampling between depths.

## Assumptions and scope
The carrier is \(W_n=\{0,\ldots,n-1\}\) with designated root \(o=0\). Each ordered pair, including loops, receives an independent uniform grade \(R(u,v)\in[0,1]\). Grades \(e(v,p)\) are also independent uniform random variables, independent of \(R\). Every model is finite, hence witnessed. For a vector of grades \(z\), \((\Diamond z)(u)=\max_{v\in W_n}\min\{R(u,v),z(v)\}\). Recursively \(\Diamond^k\) means \(k\) iterations of this operator. The convergence is for a **fixed finite set** of depths, not depths growing with \(n\).

## Proof
**1. Max–min walk identity.** Distributivity of minimum over a finite maximum gives, for every \(k\ge1\),
\[
D_{n,k}=\max_{v_1,\ldots,v_k\in W_n}\min\big\{R(o,v_1),R(v_1,v_2),\ldots,R(v_{k-1},v_k),e(v_k,p)\big\}.
\]
Thus the event \(D_{n,k}>1-t\) is exactly the existence of a rooted directed walk of length \(k\) whose \(k\) edge grades and final proposition grade exceed \(1-t\).

**2. Simple-path rare events.** For fixed \(x_k>0\), set \(t_k=x_kn^{-k/(k+1)}\). Let \(I_{P,k}\) be the indicator that all \(k+1\) required grades exceed \(1-t_k\) along a rooted directed **simple path** \(P\) of length \(k\), with root and all other path vertices distinct. Each path has probability \(t_k^{k+1}\). The sum of these indicators across all depths \(1\le k\le K\) has mean
\[
\lambda_n=\sum_{k=1}^K (n-1)_k t_k^{k+1}
=\sum_{k=1}^K x_k^{k+1}+O_{K,\mathbf x}(n^{-1}),
\]
where \((n-1)_k=(n-1)(n-2)\cdots(n-k)\).

**3. Pair-overlap lemma.** Consider two distinct simple rooted paths of lengths \(a\le b\), and suppose their indicators share \(h\ge1\) primitive random variables. A primitive variable is either an ordered edge grade, or the terminal proposition grade. Let \(v\) be the number of shared vertices other than the root. Then \(h\le v\). Indeed, common directed edges split into directed path components. Each component not containing the root has one more shared vertex than shared edges; the root component has equal counts of nonroot vertices and edges. An additional shared terminal proposition variable consumes a spare vertex in a nonroot component (or an isolated shared terminal vertex). It cannot lie in the root component unless the two paths agree from the root through their common terminal and hence are the same path, excluded here. Extra shared vertices only strengthen the inequality.

For sufficiently large \(n\), \(t_b\le t_a\). Once the \(b+1\) constraints of the longer path hold, each of the \(h\) shared constraints of the shorter path is automatic; the remaining \(a+1-h\) short-path constraints are independent. Hence the joint probability is exactly \(t_b^{b+1}t_a^{a+1-h}\). There are \(O_{a,b}(n^{a+b-v})\) ordered pairs with a fixed overlap pattern. With \(\alpha_a=a/(a+1)\), their total contribution has order
\[
O_{K,\mathbf x}\big(n^{a+b-v-\alpha_b(b+1)-\alpha_a(a+1-h)}\big)
=O_{K,\mathbf x}\big(n^{\alpha_a h-v}\big)
=O_{K,\mathbf x}\big(n^{-1/(K+1)}\big).
\]
There are finitely many combinatorial overlap patterns for fixed \(K\). Indicators sharing no primitive variable are independent, even if their paths meet at unmarked vertices. The sum of products of means over dependent indicator pairs is \(O(n^{-1})\) by the same counting (their full individual probabilities are multiplied rather than merged).

**4. Poisson zero-event approximation.** Put a dependency edge between any two distinct simple-path indicators that share a primitive variable. The Arratia–Goldstein–Gordon dependency-graph Poisson bound (with its conditional-dependence term zero here) and Step 3 show that the total simple-path count differs in total variation from \(\operatorname{Poisson}(\lambda_n)\) by \(O_{K,\mathbf x}(n^{-1/(K+1)})\). In particular, its zero-event probability is \(\exp(-\lambda_n)+O_{K,\mathbf x}(n^{-1/(K+1)})\).

**5. Nonsimple walks are negligible.** A length-\(k\) rooted walk with \(m<k\) distinct nonroot vertices must traverse at least \(m\) distinct directed edges: each first arrival at a new vertex uses a new edge. Its terminal proposition is a further independent random variable. For any fixed repetition pattern, there are \(O_k(n^m)\) such walks, each satisfying the threshold event with probability at most \(t_k^{m+1}\). Their expected number is therefore
\[
O_{k,x_k}\big(n^m t_k^{m+1}\big)
=O_{k,x_k}\big(n^{(m-k)/(k+1)}\big)
=O_{k,x_k}\big(n^{-1/(k+1)}\big).
\]
There are finitely many repetition patterns at each fixed \(k\). By the union bound, allowing all walks instead of simple paths changes the joint zero-event probability by at most \(O_{K,\mathbf x}(n^{-1/(K+1)})\).

**6. Identification of the joint law.** By Step 1, absence of every qualifying rooted walk at depths \(1,\ldots,K\) is the event
\[
\bigcap_{k=1}^K\{n^{k/(k+1)}(1-D_{n,k})\ge x_k\}.
\]
Steps 2–5 give its probability as \(\exp(-\sum_k x_k^{k+1})+O_{K,\mathbf x}(n^{-1/(K+1)})\). This factors as the product of the desired Weibull upper tails, determining their independent joint limit. Zero thresholds follow by omission and continuity. \(\square\)

## Verification
The standalone `checker.py` uses only the Python standard library. Run `python checker.py` in the directory containing this document. It exhaustively checks the Gödel max–min walk identity for every binary-valued \(n\)-world model with \(n\in\{1,2,3\}\), four modal depths, and every root; checks additional continuous-weight samples; and enumerates canonical overlap patterns for two simple rooted paths of lengths at most five. It verifies the crucial \(h\le v\) inequality and the strictly negative overlap exponent for every sampled abstract shape. The actual run reported `SEMANTIC_WALK_CHECKS 50580`, `DISTINCT_PATH_OVERLAP_CHECKS 2586`, and `ROOTED_GODEL_DIAMOND_CHECKS_OK`. These are finite sanity checks. The all-depth theorem relies on the preceding proof and the cited Poisson approximation inequality.

## Relationship to prior work
Ferrari, Fiorentini, Giardini and Rodriguez (2026) define the witnessed Gödel Kripke semantics and establish a proof calculus, finite model property, and complexity results. The present result studies a different question: probabilistic extremes of iterated possibility in a canonical random finite model. Eliazar, Metzler and Reuveni (2019) analyze independent-entry row/column max–min matrix extremes; their model has neither shared graph paths across iterations nor shared endpoint valuations across depths. The general Poisson approximation bound of Arratia, Goldstein and Gordon (1989) supplies a technique, but its application here requires the shared-path overlap lemma and separate treatment of nonsimple walks. Mallein and Tesemnikov (2022) give Poisson path-count limits between fixed endpoints of sparse ordered acyclic digraphs, using a related method but different source/target constraints and no shared-valued modal depths. No independence between layers is assumed.

## Limitations
This is a mathematical result about one explicit random-model ensemble, not a validity or satisfiability theorem for all Gödel frames. Only fixed depths are covered; no growing-depth scaling, correlated edges, other grade distributions, or necessity-modality counterpart is claimed. The Poisson inequality is used as a published theorem rather than reproved. The finite checker does not certify the infinite asymptotic argument. Historical priority outside inspected material remains subject to independent literature review.

## References
1. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906, first separate version 2026-06-30, https://arxiv.org/abs/2606.31906; the AiML 2026 conference proceedings collecting this paper were publicly submitted as arXiv:2606.29444 on 2026-06-28, https://arxiv.org/abs/2606.29444.
2. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25, https://projecteuclid.org/euclid.aop/1176991491.
3. I. Eliazar, R. Metzler and S. Reuveni, *Poisson-process limit laws yield Gumbel max-min and min-max*, Physical Review E 100 (2019), 022129, https://doi.org/10.1103/PhysRevE.100.022129.
4. B. Mallein and P. Tesemnikov, *On the length of the shortest path in a sparse Barak–Erdős graph*, Statistics & Probability Letters 190 (2022), 109634, https://arxiv.org/abs/2112.14932.
5. D. Diaconescu, J. Kleijn, L. Leuștean and D. Lucanu, *Modal Equivalence and Bisimilarity in Many-valued Modal Logics with Many-valued Accessibility Relations*, Fundamenta Informaticae 173 (2020), 177–189, https://doi.org/10.3233/FI-2020-1920.
