# Sharp three-regime two-swap mixing on merged Johnson graphs \(J(n,3)_{\{1,2\}}\)

## Finding

For each integer \(n\ge6\), let the states be the three-element subsets of \([n]\). A transition may hold or replace exactly one or exactly two elements, but may not replace all three. Over **all** symmetric nonnegative stochastic transition matrices \(P\) with these allowed entries, the minimum second-largest eigenvalue modulus \(\|P-\mathbf1\mathbf1^{\mathsf T}/\binom n3\|_2\) is

\[
\mu_n^*=\begin{cases}
\dfrac{n-4}{7n-4},&6\le n\le9,\\[3pt]
\dfrac{(n-7)(n-2)}{5n^2-25n+14},&10\le n\le12,\\[3pt]
\dfrac{n-9}{3(n-3)},&n\ge13.
\end{cases}
\]

There is a unique optimizer invariant under relabeling the underlying \(n\) symbols. Let \(w_1\) be the total probability of replacing exactly one element, \(w_2\) that of replacing exactly two elements, and \(s=1-w_1-w_2\) the holding probability. This optimizer distributes each distance-class probability uniformly among destinations and has

\[
(w_1,w_2)=\begin{cases}
\left(\dfrac{6(10-n)(n-3)}{(n-2)(7n-4)},\dfrac{12(n-4)(n-3)}{(n-2)(7n-4)}\right),&6\le n\le9,\\[5pt]
\left(0,\dfrac{6(n-4)(n-3)}{5n^2-25n+14}\right),&10\le n\le12,\\[5pt]
(0,1),&n\ge13.
\end{cases}
\]

**Unrestricted rigidity:** Every optimal symmetric stochastic matrix (even one without permutation symmetry) assigns probability zero to every one-element replacement when \(n\ge10\). When \(n\ge13\), every such optimizer also has zero diagonal. The value approaches \(1/3\) as \(n\to\infty\).

## Assumptions and scope

We use the usual Johnson distance \(d(S,T)=3-|S\cap T|\). Set \(A_i(S,T)=\mathbf1_{\{d(S,T)=i\}}\) for \(i=1,2\). Allowed transitions obey \(P_{S,T}=0\) when \(d(S,T)=3\); diagonal entries are allowed. Symmetry is the matrix equality \(P=P^{\mathsf T}\), **not** invariance under all symbol permutations. Because a symmetric stochastic matrix has uniform stationary distribution, the objective is its nontrivial spectral radius, with multiplicities included. No assumption of positive holding or positive mass on every allowed edge is imposed.

The row valencies are \(v_1=3(n-3)\) and \(v_2=3\binom{n-3}{2}\). Averaging an arbitrary feasible \(P\) over all symbol permutations preserves feasibility; convexity of the operator-norm objective makes the average no worse. It therefore suffices to optimize matrices \(sI+(w_1/v_1)A_1+(w_2/v_2)A_2\), with \(w_1,w_2,s\ge0\) and \(w_1+w_2+s=1\).

## Proof

**(1) Exact spectrum.** Each two-step one-element-replacement path is counted by

\[
A_1^2=3(n-3)I+(n-2)A_1+4A_2.
\]

The four coefficients follow by counting common one-swap neighbors of ordered triples at Johnson distances zero, one, two and three. The eigenvalues of \(A_1\), indexed by \(j=0,1,2,3\), are

\[
p_{1,j}=3(n-3)-j(n+1-j).
\]

For completeness, on indicator functions \(f_T(S)=\mathbf1_{\{T\subseteq S\}}\) for fixed \(|T|=j\), the operator \(A_1\) acts modulo indicators of smaller subsets as multiplication by \((3-j)(n-3)-j(4-j)=p_{1,j}\). The inclusion-function filtration spans all functions on triples, and its successive quotients have positive dimensions \(\binom nj-\binom n{j-1}\) for \(n\ge6\). Here the required inclusion-rank fact is elementary: if a linear combination of singleton indicators vanishes on every triple, differences between triples with two common elements force all coefficients equal and then zero. For pair indicators, differences between triples \(\{a,u,v\}\) and \(\{b,u,v\}\) force \(c_{au}-c_{bu}+c_{av}-c_{bv}=0\) for every distinct \(a,b,u,v\); since there are at least four choices outside \(\{a,b\}\), each difference vanishes, all pair coefficients are equal, and their sum on each triple forces zero. The indicators for all triples are themselves the standard basis. Thus all four eigenvalues occur and there are no others. By the displayed adjacency-square identity the nontrivial eigenvalues of \(A_2\) are respectively

\[
p_{2,1}=\frac{(n-4)(n-9)}2,\qquad p_{2,2}=11-2n,\qquad p_{2,3}=3.
\]

Consequently the three nontrivial eigenvalues of an invariant chain are \(\lambda_j=1-c_{j1}w_1-c_{j2}w_2\), where the entire coefficient matrix is

\[
C=\begin{pmatrix}
\dfrac{n}{3(n-3)}&\dfrac{2n}{3(n-3)}\\[5pt]
\dfrac{2(n-1)}{3(n-3)}&\dfrac{(n-1)(3n-14)}{3(n-4)(n-3)}\\[5pt]
\dfrac{n-2}{n-3}&\dfrac{(n-5)(n-2)}{(n-4)(n-3)}
\end{pmatrix}.
\]

**(2) Sharp certificate for \(6\le n\le9\).** Define positive weights

\[
\alpha_1=\frac{3(n-4)(n-1)}{(n-3)(7n-4)},\quad
\alpha_2=\frac{3n}{7n-4},\quad
\alpha_3=\frac{n(n-1)}{(n-3)(7n-4)}.
\]

Direct substitution gives \(\sum\alpha_j=1\), both column identities \(\alpha_1C_{1i}-\alpha_2C_{2i}+\alpha_3C_{3i}=0\) for \(i=1,2\), and the **unconditional dual lower bound**

\[
\max_j|\lambda_j|\ge\alpha_1\lambda_1-\alpha_2\lambda_2+\alpha_3\lambda_3
=\frac{n-4}{7n-4}.
\]

The displayed candidate for this range is feasible because \(w_1,w_2>0\) and \(s=(n^2-12n+44)/((n-2)(7n-4))>0\). Its eigenvalues are exactly \((\lambda_1,\lambda_2,\lambda_3)=(\mu_n^*,-\mu_n^*,\mu_n^*)\); hence the bound is sharp. Positive dual weights force all three active equalities in any invariant optimum, uniquely determining \((w_1,w_2)\).

**(3) Sharp certificate for \(10\le n\le12\).** Let \(E=5n^2-25n+14\) and

\[
\beta_1=\frac{(n-1)(3n-14)}E,\qquad
\beta_2=\frac{2n(n-4)}E.
\]

Both are positive, add to one, and cancel the distance-two coefficient. More precisely, for every feasible invariant chain,

\[
\beta_1\lambda_1-\beta_2\lambda_2
=\frac{(n-7)(n-2)}E+
\frac{n(n-2)(n-1)}{3(n-3)E}w_1.
\]

Thus the SLEM is at least the first term, with equality only if \(w_1=0\). The candidate has \(w_2=6(n-4)(n-3)/E\), \(s=-(n^2-17n+58)/E\ge0\) for the three listed integers. It has \(\lambda_1=\mu_n^*\), \(\lambda_2=-\mu_n^*\), and \(\lambda_3=-(n^2-17n+46)/E\). Direct integer substitution at \(n=10,11,12\) gives \(|\lambda_3|\le\mu_n^*\), proving optimality and unique invariant weights.

**(4) Sharp certificate for \(n\ge13\).** Since \(C_{12}=2C_{11}>C_{11}>0\) and \(w_1+w_2\le1\), every invariant feasible chain satisfies

\[
\lambda_1\ge1-C_{12}=\frac{n-9}{3(n-3)}.
\]

Equality forces \(w_1=0,w_2=1\). For this candidate the other two eigenvalues are

\[
\lambda_2=-\frac{4n-22}{3(n-4)(n-3)},\qquad
\lambda_3=\frac2{(n-4)(n-3)}.
\]

Their moduli do not exceed \(\lambda_1\): after clearing positive denominators the inequalities reduce to \(n^2-17n+58\ge0\) and \((n-9)(n-4)\ge6\), both valid for every integer \(n\ge13\). This establishes the final branch and uniqueness within the invariant class.

**(5) Unrestricted support rigidity.** For an arbitrary global optimizer, its permutation average is optimal and, by the preceding equality conditions, is the unique invariant optimizer. For \(n\ge10\), each one-swap entry of this average is zero. It is an average of nonnegative one-swap entries, so every one-swap entry of the original chain must also be zero. For \(n\ge13\), the same argument applied to the zero diagonal of the average proves that every holding entry vanishes. No assertion of uniqueness for unrestricted matrices is required.

## Verification

The included standard-library script `verify.py` exactly checks rational primal values, nonnegativity, nontrivial eigenvalue bounds, and the relevant dual identities for all integers \(6\le n\le1000\). It also independently builds the one-swap adjacency relation on all triples and compares every entry of its square with the combinatorial identity for \(n=6,7,8,9,10\). The actual extraction replay returned `VERIFY_OK`. These are reproducibility checks, not substitutes for the algebraic infinite-family proof above.

## Relationship to prior work

Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, original public version September 6, 2007), §3.3.4, give exact fastest mixing for **distance-one Johnson graphs**. That support forbids all two-element replacements; the present merged graph has a distinct second transition orbit, and the source's one-parameter formula cannot imply the three phases above.

The 2005 paper *Automorphisms and regular embeddings of merged Johnson graphs* defines graphs with distance sets \(\{1,2\}\) and studies their symmetry and embeddings, not this mixing optimum. DeVille's *The generalized distance spectrum of a graph and applications* (arXiv:1708.02294, first posted August 7, 2017), §§3.2 and 4.5, explicitly formulates multi-distance fastest mixing as a finite linear program and reports numerical/asymptotic Johnson phenomena. Those are important structural antecedents; the inspected sections do **not** give the uniform closed-form \(J(n,3)\) optimum, its sharp transitions at \(n=10,13\), or the unrestricted support-rigidity consequence. The current result adds that exact classification, not a claim to having introduced the optimization setup or the qualitative large-size phenomenon.

## Limitations

This theorem addresses symmetric stochastic chains and asymptotic spectral contraction, not arbitrary nonreversible chains, finite-time total-variation mixing, nonuniform stationary distributions, or all subset cardinalities. Invariant optimizers are unique, but unrestricted optimal matrices need not be. The literature comparison is a best-effort originality assessment, not a proof of absolute publication priority; further indexing or specialist sources could change that assessment. The symbolic identities and infinite inequalities are proved in the text; finite replay is not independent certification.

## References

1. Stephen Boyd, Persi Diaconis, Pablo A. Parrilo, and Lin Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955v1 (2007), especially §3.3.4. https://arxiv.org/abs/0709.0955
2. *Automorphisms and regular embeddings of merged Johnson graphs*, European Journal of Combinatorics 26 (2005), 417–435, DOI:10.1016/j.ejc.2004.01.012. https://doi.org/10.1016/j.ejc.2004.01.012
3. Lee DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294 (2017), especially §§3.2,4.5. https://arxiv.org/abs/1708.02294
4. Persi Diaconis and Mehrdad Shahshahani, *Time to Reach Stationarity in the Bernoulli–Laplace Diffusion Model*, SIAM J. Math. Anal. 18 (1987), 208–218, DOI:10.1137/0518016. https://doi.org/10.1137/0518016
