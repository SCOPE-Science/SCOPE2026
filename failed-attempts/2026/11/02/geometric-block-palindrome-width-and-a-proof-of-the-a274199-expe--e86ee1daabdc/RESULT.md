# Geometric block-palindrome width and a proof of the A274199 expectation conjecture

## Finding

**Theorem.** Fix an integer alphabet size \(q\ge 2\). Choose a word uniformly from the \(q^n\) words of length \(n\), and let \(W_{n,q}\) denote the width of its largest block-palindrome factorization (the number of nonempty blocks). Write \(u_j(q)\) for the number of unbordered \(q\)-ary words of length \(j\), and set

\[
p_q=\sum_{j\ge1}\frac{u_j(q)}{q^{2j}}.
\]

Then \(0<p_q<1\) and, for every integer \(r\ge0\),

\[
\lim_{n\to\infty}\Pr(W_{n,q}=2r+1)=(1-p_q)p_q^r,
\qquad
\lim_{n\to\infty}\Pr(W_{n,q}\text{ is even})=0.
\]

In particular the expectations converge, with

\[
E_q:=\lim_{n\to\infty}\mathbb E W_{n,q}=\frac{1+p_q}{1-p_q}.
\]

Let \(b_0=1\), and for \(m\ge1\) let \(b_m\) count all ordered compositions \((c_1,\ldots,c_s)\) of \(m\) into positive parts such that \(c_i<2c_{i+1}\) for each adjacent pair. Then, for every integer \(q\ge2\),

\[
\boxed{E_q=1+2\sum_{m\ge1}\frac{b_m}{q^m}.}
\]

The infinite sum converges absolutely, and \((b_m)_{m\ge0}\) is **exactly** OEIS A274199 as defined by the limiting reversed rows of array A274190. This establishes Conjecture 5 of Gabrić and Shallit (2023), not merely a finite-order coefficient agreement. The initial expansion is

\[
E_q=1+\frac2q+\frac4{q^2}+\frac6{q^3}+\frac{10}{q^4}+\frac{16}{q^5}+\frac{24}{q^6}+\frac{38}{q^7}+\cdots.
\]

## Assumptions and scope

A *border* of a nonempty word is a nonempty proper prefix equal to a suffix; a word is *unbordered* if it has no border. A block-palindrome factorization is a representation \(w=v_r\cdots v_1 z v_1\cdots v_r\), where each \(v_i\) is nonempty and the center \(z\) may be empty. Its *width* is \(2r+\mathbf1_{\{|z|>0\}}\). The largest factorization maximizes the width. We use the known shortest-border greedy characterization: repeatedly remove the shortest border simultaneously from both ends, stopping at an unbordered or empty center. The statement concerns uniformly sampled finite words, a fixed alphabet size, and the infinite-length limit; it does not assert the geometric law at finite lengths.

For the OEIS identity, use the array \(g(n,k)\) with \(g(n,0)=1\), \(g(n,k)=0\) if \(k>n\), and \(g(n,k)=g(n-1,k-1)+g(n-1,2k)\) for \(1\le k\le n\). The sequence A274199 is the stabilized value of \(g(n,n-m)\) as \(n\) increases, for each fixed \(m\ge0\).

## Proof

**1. First-border decomposition.** A shortest nonempty border cannot overlap itself: if a border of length \(j>n/2\) exists in a word of length \(n\), then its overlapping copies force a shorter border of length \(2j-n\). Every shortest border is unbordered, since any border of it would also border the whole word. Conversely, if a word begins and ends with the same unbordered word \(v\) in nonoverlapping positions, it has no shorter border, since such a shorter border would border \(v\). Consequently, the \(q\)-ary words of length \(n\) split disjointly into the \(u_n(q)\) unbordered words and, for each \(1\le j\le\lfloor n/2\rfloor\), the words \(v z v\), where \(v\) is any unbordered word of length \(j\) and \(z\) any word of length \(n-2j\). Hence

\[
q^n=u_n(q)+\sum_{j=1}^{\lfloor n/2\rfloor}u_j(q)q^{n-2j}.
\tag{1}
\]

This also makes successive outer greedy blocks independent at the enumeration level: for any fixed positive lengths \(j_1,\ldots,j_r\) whose doubled sum is at most \(n\), choosing independently an unbordered block of each length and an arbitrary remaining center produces precisely the words having those first \(r\) greedy block-pair lengths.

**2. Limit law.** Let \(K_{n,q}\) be the number of greedy block pairs. From (1) and the unique nested decomposition,

\[
\Pr(K_{n,q}\ge r)=
\sum_{\substack{j_1,\ldots,j_r\ge1\\2(j_1+\cdots+j_r)\le n}}
\prod_{h=1}^{r}\frac{u_{j_h}(q)}{q^{2j_h}},
\qquad r\ge1.
\tag{2}
\]

Since \(u_j(q)\le q^j\), we have \(p_q\le\sum_{j\ge1}q^{-j}=1/(q-1)\). For \(q\ge3\), this is strictly less than one. For \(q=2\), the strict defect \(u_2(2)=2<4\) yields \(p_2\le1-1/8<1\). Also \(p_q>0\). Monotone convergence of the nonnegative sums in (2) gives \(\Pr(K_{n,q}\ge r)\to p_q^r\) for fixed \(r\), so \(K_{n,q}\) converges to the geometric distribution \(\Pr(K=r)=(1-p_q)p_q^r\).

A word has even width exactly when the final center is empty. Fix \(R\ge0\). Among words with at most \(R\) block pairs, the probability of an empty center is a finite sum of coefficients at degree \(n/2\) of the absolutely summable generating functions \(P_q(t)^r\) for \(0\le r\le R\), where \(P_q(t)=\sum_{j\ge1}u_j(q)q^{-2j}t^j\); each such coefficient tends to zero. The probability of more than \(R\) pairs is at most \(p_q^{R+1}\) by (2). First letting \(n\to\infty\) and then \(R\to\infty\) proves vanishing even-width probability. Thus \(W_{n,q}\) tends in distribution to \(2K+1\).

Finally \(\mathbb E K_{n,q}=\sum_{r\ge1}\Pr(K_{n,q}\ge r)\), with the uniform summable majorant \(p_q^r\). Dominated convergence shows \(\mathbb E K_{n,q}\to p_q/(1-p_q)\). Since \(W_{n,q}=2K_{n,q}+\mathbf1_{\{|z|>0\}}\) and the last indicator tends to one in probability and expectation, the stated expectation formula follows.

**3. Formal power-series identity.** Put \(x=q^{-1}\) provisionally, and define the integer polynomials \(a_n(x)=x^n u_n(x^{-1})\) for \(n\ge1\) (also \(a_0=1\)). Equation (1), first viewed as a polynomial identity in \(q\), yields

\[
a_n(x)=1-\sum_{j=1}^{\lfloor n/2\rfloor}x^j a_j(x).
\tag{3}
\]

Let \(C(x)=\sum_{m\ge0}b_m x^m\). We show the *formal* identity

\[
C(x)=\left(1-\sum_{j\ge1}x^j a_j(x)\right)^{-1}.
\tag{4}
\]

For a finite bound \(M\ge1\), let \(C_M(x)\) count the same constrained compositions with all parts at most \(M\). Define an \(M\)-by-\(M\) matrix, column and row vectors by

\[
T_{ij}=x^j\mathbf1_{\{i<2j\}},\quad
v_j=x^j,\quad \boldsymbol1=(1,\ldots,1)^{\mathsf T},
\qquad 1\le i,j\le M.
\]

Successive matrix steps append composition parts and enforce exactly the adjacent-part inequality. Therefore, formally,

\[
C_M=1+v^{\mathsf T}(I-T)^{-1}\boldsymbol1
=\frac{\det(I-T+\boldsymbol1v^{\mathsf T})}{\det(I-T)}.
\tag{5}
\]

Set \(H=I-T+\boldsymbol1v^{\mathsf T}\). Its entries are

\[
H_{ij}=\delta_{ij}+x^j\mathbf1_{\{i\ge2j\}},
\]

so \(H\) is unit lower triangular, and \(\det H=1\). If \(y=H^{-1}\boldsymbol1\), its triangular equations are

\[
y_i=1-\sum_{j=1}^{\lfloor i/2\rfloor}x^j y_j.
\]

Comparing with (3) inductively gives \(y_i=a_i(x)\). The determinant lemma now gives

\[
\det(I-T)=\det(H-\boldsymbol1v^{\mathsf T})
=1-v^{\mathsf T}H^{-1}\boldsymbol1
=1-\sum_{j=1}^{M}x^j a_j(x).
\]

Together with (5), this proves

\[
C_M(x)=\left(1-\sum_{j=1}^{M}x^j a_j(x)\right)^{-1}.
\]

For each fixed degree, all coefficients stabilize as \(M\to\infty\), yielding (4). For the numerical specialization \(x=1/q\) with \(q\ge2\), each finite nonnegative matrix \(T\) has row sums below one (at \(q=2\), the first row sum is \(1-2^{-M}<1\)), so (5) is an absolutely convergent generating series. Since \(\sum_{j\ge1}q^{-j}a_j(1/q)=p_q<1\), the finite identity and monotone convergence yield

\[
C(1/q)=\frac1{1-p_q}.
\]

Combining this equality with the limit expectation proves \(E_q=2C(1/q)-1=1+2\sum_{m\ge1}b_m/q^m\), including absolute convergence.

**4. Identification with the specified OEIS sequence.** For \(n\ge k\ge0\), let \(h(n,k)\) count compositions of \(n-k\) satisfying the same adjacent inequality and whose *last* part is at most \(k+1\). The empty composition is allowed when \(n=k\). With \(k=0\) there is exactly one: all parts must equal one (and the empty case at \(n=0\)). For \(k>n\) set \(h(n,k)=0\). When \(1\le k\le n\), split the compositions by whether their last part is at most \(k\) or is exactly \(k+1\). The first class is counted by \(h(n-1,k-1)\). Removing the final \(k+1\) from the second class leaves a composition of \(n-2k-1\) with last part at most \(2k+1\), hence counted by \(h(n-1,2k)\); the removal is reversible because the preceding part is strictly less than \(2(k+1)\). Thus \(h\) obeys the *exact defining recurrence and boundary conditions* of \(g\), so \(h(n,k)=g(n,k)\) for every \(n,k\). For any fixed \(m\), if \(n-m+1\ge m\), the last-part restriction for \(h(n,n-m)\) is vacuous, and consequently

\[
\lim_{n\to\infty}g(n,n-m)=b_m.
\]

This proves the identity with A274199 from its defining array, independently of matching any finite list.

## Verification

The standalone \(\texttt{verify.py}\) uses only Python 3's standard library. Run \(\texttt{python3 verify.py}\) to check the greedy definition against exact counting for every word of the tested lengths over alphabets of sizes two, three and four, the normalized-unbordered inverse-series identity through degree 75, stabilized OEIS array rows through index 80, and the published four- and five-decimal expectation benchmarks. The output is \(\texttt{VERIFY\_OK}\), with 84,133 exhaustively enumerated words and a separate 116,901-word direct comparison between greedy width and the maximum over every possible outer-border choice. These finite checks support, but do not replace, the all-length proof, the limit interchange and the determinant identity.

Numerical examples computed from the rapidly convergent unbordered series are \(E_2\approx6.4686269063\), \(E_3\approx2.5907942392\), and \(E_4\approx1.9080418480\), agreeing with the reported source values.

## Relationship to prior work

Gabrić and Shallit (2023), *Smallest and Largest Block Palindrome Factorizations*, give the finite distribution recurrence, establish convergence of mean largest width, and state the specific A274199 expansion as **Conjecture 5**. Their proved ingredients, including the shortest-border decomposition and recurrence for unbordered words, are acknowledged. The present theorem supplies an exact geometric limit law, an evaluation of the mean by a return probability, and a formal determinant identity proving the conjectured coefficients at every order and every alphabet size, rather than claiming previously known existence or the unbordered-word recurrence as new.

OEIS A274199 defines the sequence as stabilized reversed rows of A274190; its webpage suggested the adjacent-part composition interpretation as apparent. Here an explicit last-part-bounded composition interpretation establishes that identification rigorously. The classical literature on locally restricted compositions gives general background, not this claimed equality with the block-palindrome expectation.

## Limitations

The limiting geometric law is not a claim of exact geometric behavior at finite word lengths. The result concerns the *largest* block-palindrome factorization, not the differently defined smallest factorization. The proof relies on the known correctness of greedy shortest-border factorization, which is explicitly cited. A search of accessible indexed records and relevant primary material found no prior proof of this exact expectation identity or the stated limit law; unindexed or inaccessible equivalent work may still exist. No independent external validation is claimed.

## References

1. D. Gabrić and J. Shallit, *Smallest and Largest Block Palindrome Factorizations*, arXiv:2302.13147, first posted 2023-02-25; especially Theorems 2 and 4, Conjecture 5. https://arxiv.org/abs/2302.13147 ; https://arxiv.org/html/2302.13147v2
2. OEIS A274199, *Limiting reverse row of the array A274190*, including the tentative restricted-composition observation. https://oeis.org/A274199
3. OEIS A274190, *Triangular array read by rows*, recurrence defining the array. https://oeis.org/A274190
4. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12 (2005), R57. https://doi.org/10.37236/1954
