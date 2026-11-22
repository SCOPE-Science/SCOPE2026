# Uniform-kernel universality and exact absorption laws for corank-one matrix products

## Finding

Fix a prime power \(q\ge2\) and \(n\ge2\). Put \(V=\mathbb F_q^n\). At step \(k\ge1\), independently of all earlier steps, choose a random linear operator \(M_k:V\to V\) with rank exactly \(n-1\) such that \(\ker M_k\) is uniform among the lines of \(V\). The laws of the \(M_k\) need not be identical and their images or nonzero eigenvalues are unrestricted. Set
\[
P_0=I_n,\qquad P_k=M_kP_{k-1},\qquad R_k=\operatorname{rank}P_k,\qquad T_n=\min\{k\ge0:R_k=0\}.
\]

**Universal rank chain and exact stopping law.** At rank \(r>0\), \(R_k\) decreases to \(r-1\) with probability
\[
p_r=\frac{q^r-1}{q^n-1},\qquad 1\le r\le n,
\]
and otherwise remains \(r\), conditional even on the entire past matrix-valued history. Let \(G_r\) be independent geometric variables taking values in \(\{1,2,\ldots\}\), with \(\Pr(G_r=j)=(1-p_r)^{j-1}p_r\). Then
\[
T_n\ \overset{d}{=}\ \sum_{r=1}^n G_r,
\qquad
\mathbb E[z^{T_n}]=\prod_{r=1}^n\frac{p_rz}{1-(1-p_r)z}.
\]
In particular, for all integers \(k\ge0\),
\[
\boxed{\Pr(T_n>k)=\sum_{j=1}^{n} c_{n,j}\lambda_{n,j}^k,\quad
c_{n,j}=\prod_{\substack{1\le r\le n\\r\ne j}}\frac{q^r-1}{q^r-q^j},\quad
\lambda_{n,j}=\frac{q^n-q^j}{q^n-1}.}
\]
For this expression at \(k=0\), the term \(\lambda_{n,n}^0=0^0\) means \(1\); for \(k>0\) that term is zero. All denominators in \(c_{n,j}\) are nonzero. The mean and variance are
\[
\mathbb ET_n=(q^n-1)\sum_{r=1}^n\frac1{q^r-1},
\quad
\operatorname{Var}(T_n)=\sum_{r=1}^n\left(\frac{(q^n-1)^2}{(q^r-1)^2}-\frac{q^n-1}{q^r-1}\right).
\]
The spectral pole closest to one has coefficient \(c_{n,1}=(1-q^{-n})/(1-q^{-1})\); all other nonzero bases are strictly smaller. Consequently
\[
\boxed{\lim_{k\to\infty}\frac{\Pr(T_n>k)}{\left(1-\frac{q-1}{q^n-1}\right)^k}=\frac{1-q^{-n}}{1-q^{-1}}.}
\]

**A nondegenerate large-dimension law.** For fixed \(q\) as \(n\to\infty\),
\[
\frac{T_n}{q^n-1}\ \Longrightarrow\ S_q=\sum_{r=1}^{\infty} E_r,
\quad E_r\text{ independent with }E_r\sim\operatorname{Exp}(q^r-1),
\]
where \(\operatorname{Exp}(a)\) means exponential with rate \(a\). The series converges almost surely and in \(L^1\). For each real \(s\ge0\),
\[
\mathbb E e^{-sS_q}=\prod_{r=1}^{\infty}\frac{q^r-1}{q^r-1+s},\quad
\mathbb ES_q=\sum_{r\ge1}\frac1{q^r-1},\quad
\operatorname{Var}(S_q)=\sum_{r\ge1}\frac1{(q^r-1)^2},
\]
and the exact leading tail constant is
\[
\boxed{\lim_{t\to\infty} e^{(q-1)t}\Pr(S_q>t)=\frac{q}{q-1}.}
\]
In particular, uniformly distributed rank-\(n-1\) idempotents and uniformly distributed regular nilpotent operators (one Jordan block of size \(n\)) lead to *identical rank-path and stopping-time laws*, despite having different possible eigenstructures.

## Assumptions and scope

Only the kernel-line marginal and independence from the past are assumed. An individual factor may be chosen from any conjugation-invariant probability distribution supported on rank-\(n-1\) matrices; conjugation invariance guarantees a uniform kernel line since \(\mathrm{GL}_n(\mathbb F_q)\) acts transitively on projective lines. In particular the two displayed classes of factors qualify. Full matrix products may have different distributions for different factor ensembles; the equality asserted here concerns their **rank paths** and stopping times, not the matrices themselves. Every finite field, including characteristic two and all extension fields, is included. The convention for \(T_n\) counts factors multiplied after the identity; its minimum is \(n\).

## Proof

**Step 1: a transition determined only by a kernel line.** Suppose the past has produced \(P\) with rank \(r>0\) and image \(W\) of dimension \(r\). For any corank-one \(M\),
\[
\operatorname{rank}(MP)=\dim M(W)=r-\dim(W\cap\ker M).
\]
Since \(\ker M\) is a line, the drop is either zero or one. There are \((q^r-1)/(q-1)\) lines in \(W\) and \((q^n-1)/(q-1)\) lines in \(V\). Thus the conditional drop probability is \(p_r=(q^r-1)/(q^n-1)\), independently of the actual subspace \(W\) or any earlier choices. Once rank zero is reached it stays zero. Since \(p_r>0\), absorption is almost sure.

**Step 2: independent geometric waiting times.** The decreasing rank visits \(n,n-1,\ldots,1,0\) in order, and the conditional survival chance at each positive rank is constantly \(1-p_r\), even given the full past. Repeated conditioning at successive trials shows that the holding time at rank \(r\) is geometric with parameter \(p_r\) and independent of holding times in other levels. Multiplication of the elementary probability-generating functions gives the displayed factorization; sums of geometric means and variances give the two moment formulas. (For \(r=n\), \(p_n=1\), so \(G_n=1\) deterministically.)

**Step 3: complete finite-dimensional survival spectrum.** Put \(\lambda_r=1-p_r\). From the generating function of \(T_n\), the survival generating function equals
\[
\sum_{k\ge0}\Pr(T_n>k)z^k
=\frac{1-\prod_{r=1}^n \frac{p_rz}{1-\lambda_rz}}{1-z}.
\]
The \(\lambda_r\) are pairwise distinct and \(\lambda_n=0\). The simple pole at \(z=1/\lambda_j\), for \(j<n\), has partial-fraction coefficient
\[
c_{n,j}=\prod_{r\ne j}\frac{p_r}{p_r-p_j}
=\prod_{r\ne j}\frac{q^r-1}{q^r-q^j}.
\]
The remaining constant term corresponds to the \(j=n\) term and is fixed by \(\Pr(T_n>0)=1\). Equivalently, direct partial fractions also give its product expression. This proves the exact survival formula for every \(k\ge0\). Since \(\lambda_1>\lambda_2>\cdots>\lambda_n=0\), the unique dominant term is \(j=1\). Its coefficient telescopes:
\[
c_{n,1}=\prod_{r=2}^n\frac{q^r-1}{q^r-q}
=\prod_{r=2}^n\frac{1-q^{-r}}{1-q^{-(r-1)}}
=\frac{1-q^{-n}}{1-q^{-1}}.
\]
This proves the finite-dimensional tail limit.

**Step 4: limiting exponential sum.** Set \(D_n=q^n-1\). For each fixed \(r\ge1\), \(G_r/D_n\) converges to an exponential with rate \(q^r-1\), because its tail is \((1-(q^r-1)/D_n)^{\lfloor tD_n\rfloor}\). Joint convergence for any fixed finite set follows from independence. Uniform control of the remaining higher-rank holding times uses
\[
\mathbb E\sum_{r=R+1}^n\frac{G_r}{D_n}=\sum_{r=R+1}^n\frac1{q^r-1}\le\sum_{r>R}\frac1{q^r-1}\xrightarrow[R\to\infty]{}0.
\]
Markov's inequality and the converging-together argument therefore prove the weak limit, finite mean and Laplace product. The variance formula follows similarly from \(\operatorname{Var}(G_r/D_n)\le(q^r-1)^{-2}\), allowing termwise convergence of the variance sums.

**Step 5: sharp limiting tail.** Write \(S_q=E_1+W\), where \(W=\sum_{r\ge2}E_r\) is independent of \(E_1\), whose rate is \(a=q-1\). The exponential moment at \(a\) exists and telescopes:
\[
\mathbb E[e^{aW}]=\prod_{r=2}^{\infty}\frac{q^r-1}{q^r-1-a}
=\prod_{r=2}^{\infty}\frac{1-q^{-r}}{1-q^{-(r-1)}}
=\frac{q}{q-1}.
\]
Conditioning on \(W\) gives \(e^{at}\Pr(E_1+W>t)=\mathbb E[e^{a\min(W,t)}]\), which increases to \(\mathbb E[e^{aW}]\) by monotone convergence. The limiting tail constant follows.

## Verification

The accompanying `check.py` uses only Python 3's standard library. It enumerates actual matrices over \(\mathbb F_2\) in dimensions two and three and over \(\mathbb F_3\) in dimension two. For rank-\(n-1\) idempotents it enumerates the whole matrix class; for regular nilpotents in dimension three it enumerates that different conjugacy class. It multiplies actual matrices to verify each rank-drop probability and all rank-distribution probabilities through six factors, then independently compares the survival spectral formula to rational Markov-chain probabilities through thirteen factors. The captured `check_output.txt` lists all passed configurations. These finite checks corroborate the calculation but do not prove the unrestricted finite-field or large-dimension statements; the proof above does.

## Relationship to prior work

Dolinka and East, arXiv:1503.03139 (first posted 2015-03-11), establish the matrix-semigroup and idempotent-generation setting and explicitly count finite-field idempotents by rank (especially §3 and §7). Their results concern semigroup structure, generators and individual idempotent classes, not the stochastic product-to-zero stopping-time distribution. A published result titled *Joint rank distribution for products of two finite-field idempotents* obtains a two-factor joint rank census; a further published result titled *Asymptotic independence of opposite product ranks for fixed-rank finite-field idempotents* studies the two-factor limit at fixed input ranks. Neither asserts the present inhomogeneous all-length kernel-universality law or stopping-time spectral decomposition. Van Peski's *Local limits in p-adic random matrix theory* (2024) studies products of additive-Haar and related random matrices in a distinct ensemble and limiting regime. The projective-line count, geometric waiting-time decomposition and partial-fraction method are standard tools; the claimed contribution is their combined **complete absorption law for arbitrary independent uniform-kernel corank-one matrix factors**, with the sharp finite- and infinite-dimensional tails.

## Limitations

The result tracks only product rank and first attainment of the zero matrix. It does not determine prescribed full-matrix product fibers or stopping times under nonuniform or history-dependent kernel laws. The finite-field matrix checks cover prime fields in small dimensions and do not constitute independent certification. The supplied searches and inspected literature cannot exclude a historical equivalent in an unindexed random-semigroup or matrix-product paper; no independent mathematical audit has been performed.

## References

1. I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139, first public version 2015-03-11, §3 and §7, https://arxiv.org/abs/1503.03139, full text https://arxiv.org/html/1503.03139v2.
2. *Joint rank distribution for products of two finite-field idempotents*, published research record with full result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-joint-rank-distribution-for-products-of-two-finite-field-idempot--3c6fd019df5a/RESULT.md.
3. *Asymptotic independence of opposite product ranks for fixed-rank finite-field idempotents*, published research record with full result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-asymptotic-independence-of-opposite-product-ranks-for-fixed-rank--9fcc1b6d9519/RESULT.md.
4. R. Van Peski, *Local limits in p-adic random matrix theory*, Proc. Lond. Math. Soc. (2024), https://doi.org/10.1112/plms.12626, §1.1–§1.2 (matrix-product ensembles and limiting regimes).
