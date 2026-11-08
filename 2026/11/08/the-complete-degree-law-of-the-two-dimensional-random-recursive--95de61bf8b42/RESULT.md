# The complete degree law of the two-dimensional random recursive simplicial complex

## Finding

In the RRSC(2) process defined below, let \(N_k(n)\) be the number of vertices of graph degree exactly \(k\) after \(n\) vertices have arrived, and put \(\varphi=(1+\sqrt5)/2\). **Almost surely, simultaneously for all integers \(k\ge1\),**

\[
\frac{N_k(n)}{n}\longrightarrow p_k,
\qquad
p_1=\frac1{\varphi+3}=\frac{7-\sqrt5}{22},
\qquad
p_2=\frac{\varphi+2p_1}{\varphi+4}=\frac{45+14\sqrt5}{209},
\]
\[
p_k=\frac{k}{\varphi+k+2}p_{k-1}\quad(k\ge3),
\qquad
p_k=\frac{p_2\,\Gamma(\varphi+5)}{2}
\frac{\Gamma(k+1)}{\Gamma(k+\varphi+3)}\quad(k\ge2).
\]

These limits form a probability distribution, \(\sum_{k\ge1}p_k=1\), and the full empirical degree distribution converges to it almost surely in total variation. Its tail has the explicit **positive** prefactor

\[
p_k\sim\frac{p_2\,\Gamma(\varphi+5)}{2}
\,k^{-(\varphi+2)}\quad(k\to\infty).
\]

The exponent \(\varphi+2=(5+\sqrt5)/2\) was previously predicted for this model. The contribution here is the complete, normalized degree-frequency law, its almost-sure convergence and the exact tail prefactor, not a claim to have first guessed that exponent.

## Assumptions and scope

Start at \(n=1\) with a single vertex. To grow from \(n\) to \(n+1\), choose uniformly among **all existing vertices and all existing edges**. If a vertex is chosen, introduce a new vertex adjacent only to it. If an edge is chosen, introduce a new vertex adjacent to both endpoints and fill in the resulting triangle and its faces. All earlier vertices, edges and triangles persist. This is precisely the random recursive simplicial complex RRSC(2) of Krapivsky and Lucas [1]; degrees count edges in its one-dimensional skeleton. Let \(E_n\) be its number of edges and let \(\mathcal F_n\) be the history through the \(n\)-vertex state. The theorem concerns \(n\to\infty\) followed, separately, by \(k\to\infty\). It does not assert a joint moving-degree estimate at \(k=k(n)\).

## Proof

**1. Exact incidence drift.** A present vertex of degree \(k\) belongs to exactly one eligible zero-simplex (itself) and exactly \(k\) eligible one-simplices (its incident edges). Thus its probability of increasing by one on the next step, conditional on \(\mathcal F_n\), is exactly

\[
\frac{k+1}{n+E_n}.
\]

The newborn vertex has degree one when a vertex is selected and degree two when an edge is selected. Consequently, for every \(n\ge2\),

\[
\begin{aligned}
\mathbb E[E_{n+1}-E_n\mid\mathcal F_n]&=1+\frac{E_n}{n+E_n},\\
\mathbb E[N_1(n+1)-N_1(n)\mid\mathcal F_n]&=\frac{n-2N_1(n)}{n+E_n},\\
\mathbb E[N_2(n+1)-N_2(n)\mid\mathcal F_n]&=\frac{E_n+2N_1(n)-3N_2(n)}{n+E_n},\\
\mathbb E[N_k(n+1)-N_k(n)\mid\mathcal F_n]&=\frac{kN_{k-1}(n)-(k+1)N_k(n)}{n+E_n}\quad(k\ge3).
\end{aligned}
\]

These identities are exact despite the simultaneous degree changes of both endpoints of a selected edge: linearity of conditional expectation needs no independence between those endpoint changes. Every degree-class increment has absolute value at most three, and the edge increment is either one or two.

**2. Elementary stochastic stability lemma.** Suppose a bounded adapted scalar sequence satisfies

\[
e_{n+1}=\left(1-\frac{a_n}{n+1}\right)e_n+\frac{\epsilon_n+\xi_{n+1}}{n+1},
\]

where eventually \(0<c\le a_n\le C<\infty\), \(\epsilon_n\to0\) almost surely, and \(\xi_{n+1}\) is a uniformly bounded martingale difference. Then \(e_n\to0\) almost surely. To prove this, discard finitely many indices until all multipliers lie in \((0,1)\), and iterate. Products of multipliers tend to zero since \(\sum a_n/(n+1)=\infty\). If \(w_{n,j}=\prod_{i=j+1}^{n-1}(1-a_i/(i+1))\), then \(0\le w_{n,j}\le1\) and \(\sum_jw_{n,j}a_j/(j+1)\le1\). The weighted \(\epsilon\)-sum tends to zero by splitting at a large fixed index and bounding its tail by \(\sup_{j\ge J}|\epsilon_j|/c\). The series \(\sum_j\xi_{j+1}/(j+1)\) converges almost surely because its martingale differences have summable second moments. For each fixed \(n\), \(w_{n,j}\) is nondecreasing in \(j\); Abel summation bounds the weighted tail by twice the supremum of the unweighted tail partial sums, which tends to zero as \(J\to\infty\). This proves the lemma without assuming future multipliers are independent of earlier noise.

**3. Edge-density law.** Put \(x_n=E_n/n\in[0,2]\), \(\psi=(1-\sqrt5)/2\), and let \(\xi_{n+1}\) be the centered edge increment. The first exact drift yields

\[
x_{n+1}-\varphi
=\left(1-\frac{a(x_n)}{n+1}\right)(x_n-\varphi)+\frac{\xi_{n+1}}{n+1},
\qquad
a(x)=\frac{x-\psi}{1+x}.
\]

The function \(a(x)\) is bounded above and bounded strictly away from zero on \([0,2]\). The stability lemma therefore gives

\[
\frac{E_n}{n}\longrightarrow\varphi\quad\text{almost surely}.
\]

**4. Every fixed degree class.** Set \(z_{k,n}=N_k(n)/n\). Subtract the conditional drift's equilibrium from the normalized version of the exact relations in step 1. For \(k=1\), the coefficient of \(z_{1,n}\) is \(1+2/(1+x_n)\), and the forcing tends to \(1/(1+\varphi)\). The stability lemma gives \(z_{1,n}\to1/(\varphi+3)\). For \(k=2\), the coefficient is \(1+3/(1+x_n)\), and the forcing is \((x_n+2z_{1,n})/(1+x_n)\), giving the displayed \(p_2\). For each fixed \(k\ge3\), the coefficient is \(1+(k+1)/(1+x_n)\) and the forcing is \(kz_{k-1,n}/(1+x_n)\). Induction using the same lemma proves the recurrence for all \(p_k\). Intersection of the countably many probability-one events yields simultaneous almost-sure convergence.

**5. Normalization and tail.** Multiplying the fixed-point equations by \(1+\varphi\) and summing over degree classes \(1,\ldots,K\) for \(K\ge2\) cancels the interior degree transfers:

\[
(1+\varphi)\sum_{k=1}^{K}p_k
=1+\varphi-(K+1)p_K.
\]

The product of the recurrence for \(k\ge3\) is the displayed gamma ratio. Stirling's gamma-ratio asymptotic gives \(p_K=O(K^{-(\varphi+2)})\), so \((K+1)p_K\to0\). Hence the limiting frequencies sum to one. Pointwise convergence of the empirical probability masses and normalization on both sides imply total-variation convergence: truncate both distributions at a common large \(K\), then let \(n\) and \(K\) tend to infinity in that order. The gamma asymptotic also gives the exact positive tail prefactor.

## Verification

The standalone `VERIFY.py` reconstructs the finite graph histories from the attachment rule. For every reachable labeled graph at sizes \(2\le n\le7\), it checks every incidence-drift identity by exact rational averaging over all permitted next attachments. It independently tests the gamma recurrence and mass identity numerically and simulates a 90,000-vertex realization using fixed-seed random choices. Run with `python3 VERIFY.py`; only the Python standard library is needed. Exact enumeration and finite simulation are diagnostic checks, not proofs of the asymptotic theorem.

## Relationship to prior work

Krapivsky and Lucas [1], Section VI, give the leaf density \(p_1=(7-\sqrt5)/22\), propose investigating the degree-two density, and describe the computation of higher degrees as a challenge. Their Section V anticipates the same tail exponent via an assumption about first-vertex and maximum-degree growth; Section VII emphasizes the heuristic nature of that argument. The present exact incidence drift determines **every** degree density and proves the exponent rigorously, with the full gamma prefactor and almost-sure empirical-law convergence.

Fountoulakis, Iyer, Mailler and Sulzbach [2], Theorem 1.4, treat growth by selection of faces of a **single fixed dimension** and provide a general degree distribution under their model's assumptions. In contrast, RRSC(2) selects from both vertices and edges, creating newborns of two different initial degrees with state-dependent mixing weights. Their fixed-dimensional Theorem 1.4 does not directly supply the formula above; their Remark 3 identifies mixed-dimensional selection as a possible generalization, rather than presenting that generalization's degree law. The stochastic-stability argument used here is elementary and does not assert priority for the general method.

## Limitations

The theorem gives fixed-degree almost-sure frequencies and the resulting probability law, not joint asymptotics for degrees growing with \(n\), the maximum degree, a central limit theorem for class counts, or the joint distribution of degree and incident triangles. It does not address RRSC models of dimension at least three. The primary-paper comparison and other literature searches do not establish comprehensive historical novelty; a broader random-graph theorem under another formulation may still imply this special case.

## References

[1] P. L. Krapivsky and M. Lucas, *Random Recursive Simplicial Complexes*, arXiv:2608.26547, version first posted 2026-08-27, https://arxiv.org/abs/2608.26547 (especially Sections I, IV, V, VI, VII, Appendix A).

[2] N. Fountoulakis, T. Iyer, C. Mailler and H. Sulzbach, *Dynamical Models for Random Simplicial Complexes*, arXiv:1910.12715, first posted 2019-10-28, https://arxiv.org/html/1910.12715v3 (especially Sections 1.1, 1.4, 2.1).
