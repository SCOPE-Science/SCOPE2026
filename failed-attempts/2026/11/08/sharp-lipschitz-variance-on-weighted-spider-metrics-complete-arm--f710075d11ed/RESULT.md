# Sharp Lipschitz variance on weighted spider metrics: complete arm rigidity and signed radial discrepancy

## Finding

Let \(T\) be a finite spider tree whose central vertex \(c\) meets \(r\geq3\) nonempty, mutually disjoint path arms \(A_1,\ldots,A_r\). Give every edge a positive length and every vertex strictly positive probability \(\mu(v)\), with total probability one. Write \(\rho(v)=d_T(c,v)\), and define the radial moments
\[
q_i=\sum_{v\in A_i}\mu(v)\rho(v),\quad R=\sum_{v\in V(T)}\mu(v)\rho(v)^2,\quad
\delta=\min_{\varepsilon\in\{-1,1\}^r}\left|\sum_{i=1}^r\varepsilon_i q_i\right|.
\]
Then the **exact sharp centered Lipschitz variance**, or the squared norm of the canonical real Lipschitz-modulo-constants to centered \(L^2(\mu)\) map, is
\[
\boxed{\displaystyle\sup_{\operatorname{Lip}(f)\leq1}\operatorname{Var}_\mu f=R-\delta^2.}
\]
**Every maximizer**, and no other function, has (up to translation) the form
\[
f(c)=0,\qquad f(v)=\varepsilon_i\rho(v)\quad(v\in A_i),
\]
where \(\varepsilon\) realizes the displayed minimum. In particular, the result classifies all optimizer ties and shows that no reversal of slope inside an arm can maximize variance. The sharp value depends only on \(R\) and on the multiset of arm first moments \(\{q_i\}\), not on individual arm subdivisions.

For the unit-edge spider with \(r\) arms of common length \(L\), with uniform probability on all \(N=1+rL\) vertices, the formula becomes
\[
\boxed{\displaystyle \frac{rL(L+1)(2L+1)}{6N}
-\frac{(r\bmod2)L^2(L+1)^2}{4N^2}.}
\]
Every optimizer splits the arms into sign classes whose cardinalities differ by at most one.

For a star with hub probability \(1/2\) and strictly positive rational leaf probabilities summing to \(1/2\), the sharp spread is \(1/2\) precisely when its leaf masses admit a perfect equal-sum partition. Thus deciding whether its sharp Lipschitz variance equals \(1/2\) is NP-complete for binary-encoded rational probability inputs (in the weak, PARTITION sense).

## Assumptions and scope

The metric on \(T\) is the weighted shortest-path metric. The arm \(A_i\) consists of ordered vertices \(v_{i1},\ldots,v_{im_i}\), with edge lengths \(\ell_{ij}>0\) between the hub or preceding vertex and \(v_{ij}\). Each vertex has strictly positive mass, including the hub. All functions are real-valued; the Lipschitz bound is \(1\). Variance means \(\mathbb E_\mu f^2-(\mathbb E_\mu f)^2\), not uncentered second moment or sub-Gaussian constant. The theorem works for arbitrary positive real edge lengths and positive real probabilities; the complexity statement is restricted to binary-encoded rational probabilities.

## Proof

**Step 1: every maximizing edge increment is saturated.** Normalize \(f(c)=0\). On a tree the directed edge increments \(t_{ij}=f(v_{ij})-f(v_{i,j-1})\) are independent and range over closed intervals \([-\ell_{ij},\ell_{ij}]\), with \(v_{i0}=c\). Fix every increment except \(t_{ij}\). Changing it adds the same amount to all vertices in the strict descendant suffix \(B_{ij}=\{v_{ik}:k\geq j\}\). If \(a_{ij}=\mu(B_{ij})\), the coefficient of \(t_{ij}^2\) in variance is \(a_{ij}(1-a_{ij})>0\). The strict inequality follows from positive mass both inside the suffix and at the hub. Thus a maximum over that interval occurs only at an endpoint; every global maximizer has \(t_{ij}=\sigma_{ij}\ell_{ij}\) with \(\sigma_{ij}\in\{-1,1\}\).

**Step 2: sign rigidity along each arm.** Fix an arm \(A_i\), fix all other arms, and keep \(f(c)=0\). Write \(a_j=\mu(B_{ij})\), and \(M=\sum_{v\notin A_i}\mu(v)f(v)\). The contributions of this arm to its own value and to the global mean are
\[
 f(v_{ik})=\sum_{j\leq k} t_{ij},\qquad
 \sum_{v\in A_i}\mu(v)f(v)=\sum_j a_jt_{ij}.
\]
Expanding variance after inserting \(t_{ij}=\sigma_j\ell_{ij}\) leaves, apart from a term independent of the signs,
\[
 2\sum_{j<k}a_k(1-a_j)\ell_{ij}\ell_{ik}\sigma_j\sigma_k
 -2M\sum_j a_j\ell_{ij}\sigma_j.
\]
Every pair coefficient is strictly positive. If \(M>0\), the unique maximizer is the all-negative sign vector: it simultaneously maximizes every pair coupling and every linear term. If \(M<0\), it is the all-positive vector. If \(M=0\), the only maximizing choices are the two constant sign vectors (the assertion is also trivial for a one-edge arm). This proves that in any global maximizing potential the slope is constant in sign along **each** arm. In particular, no other extremal edge-sign configurations can tie.

**Step 3: exact sharp value and all equality cases.** Consequently, after translation every maximizer must be \(f(v)=\varepsilon_i\rho(v)\) on each arm. Conversely, every such signed radial potential is feasible because the tree distance is the sum of edge lengths along the unique connecting path. Its second moment is exactly \(R\) and its mean is \(\sum_i\varepsilon_iq_i\). Its variance is therefore \(R-(\sum_i\varepsilon_iq_i)^2\). Maximizing over the finitely many choices of arm signs proves both the formula and the complete equality classification. Since all \(q_i>0\), signs are determined solely by a finite, positive-weight number-partition problem.

**Step 4: balanced-arm specialization.** For common integer length \(L\), uniform mass and \(N=1+rL\), each arm has first moment \(q_i=L(L+1)/(2N)\), and the radial second moment is \(R=rL(L+1)(2L+1)/(6N)\). The minimum signed first moment has absolute value \(0\) for even \(r\) and \(q_i\) for odd \(r\); substitution gives the stated parity formula and exactly the balanced sign counts.

**Step 5: threshold complexity.** Begin with a positive-integer PARTITION instance \(a_1,\ldots,a_r\), with total \(A\). Give a unit star hub mass \(1/2\), leaf \(i\) mass \(a_i/(2A)\), and no other vertices. The total leaf mass is \(1/2\), so \(R=1/2\). The discrepancy term is \(\delta=\min_\varepsilon|\sum_i\varepsilon_i a_i|/(2A)\). Therefore the spread equals \(1/2\) if and only if the original positive integers partition equally. The reduction has polynomial binary encoding; a leaf-sign vector is a polynomial-time verifiable yes certificate. This proves NP-completeness for that compact rational star representation. It does **not** assert strong NP-hardness or hardness for explicitly replicated/unary-weight inputs.

## Verification

The accompanying `check_spider.py` uses exact integer arithmetic: if the positive vertex masses are normalized from integers of sum \(W\), it compares \(W^2\operatorname{Var}_\mu(f)\) for **all** saturated edge-sign potentials with \(W\sum_v w_v\rho(v)^2-(\min_\varepsilon|\sum_i\varepsilon_i\sum_{v\in A_i}w_v\rho(v)|)^2\). It checks the predicted value and that every maximizing edge-sign profile is constant along its arm on 180 seeded heterogeneous configurations, then checks 16 equal-arm cases and four partition-threshold examples. All tests passed on the embedded standalone script.

Finite enumeration supports the proof but does not certify the infinite class of real lengths and probabilities. That class is handled by the strict-convexity and positive-coupling argument above.

## Relationship to prior work

The spread functional and earlier graph-extremizer principles were developed by Alon, Boppana and Spencer (1998). Their account treats general finite metric spaces and graph path spread; the signed radial-moment identity for arbitrary probabilities and positive lengths on spider trees is not a statement recovered from their inspected sections. Addario-Berry, Janson and McDiarmid (arXiv first public 2009-02-06) study spread of random graph models, including models with edge lengths, not this all-parameter spider equality classification. Bobkov, Houdré and Tetali (2006) study exponential concentration/sub-Gaussian constants, a distinct optimization. Other indexed studies concern Dudley dual norms on stars, curvature of spider trees, and zonotope width variance; none of the inspected material gives the same squared centered-Lipschitz norm or its full weighted-arm optimizer characterization. Those index-only comparisons are explicitly weaker than full-text exclusions.

The PARTITION reduction uses the classical decision problem; NP-completeness of PARTITION itself is not new. The claim is the exact translation from that problem to the sharp embedding-norm threshold, not a stronger complexity classification.

## Limitations

The arm-rigidity proof uses the **path-arm** structure, strict positivity of all masses and lengths, and a tree metric. Arbitrary branching inside arms, zero-mass vertices, general graphs, complex-valued potentials, nonuniform Lipschitz constants varying with direction, other moments, and exact algorithms under arbitrary real-input encodings are not covered. The finite verifier has a bounded search domain, and novelty may be limited by equivalent results in unindexed literature or sources available only by abstract.

## References

1. N. Alon, R. Boppana, and J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis 8 (1998), 411–436, DOI 10.1007/s000390050062. Author-accessible text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf.
2. S. G. Bobkov, C. Houdré, and P. Tetali, *The subgaussian constant and concentration inequalities*, Israel Journal of Mathematics 156 (2006), 255–283, DOI 10.1007/BF02773835. Author-accessible text: https://houdre.math.gatech.edu/research/papers/BHT_SUB7.pdf.
3. L. Addario-Berry, S. Janson, and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first public 2009-02-06), https://arxiv.org/abs/0902.1156.
4. Classical PARTITION decision problem, as in R. M. Karp's original NP-completeness framework and standard complexity references. Only the standard weak-NP-completeness of binary-input PARTITION is used.
