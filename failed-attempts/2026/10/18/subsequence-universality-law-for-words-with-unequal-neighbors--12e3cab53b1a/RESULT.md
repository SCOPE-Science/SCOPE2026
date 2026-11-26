# Subsequence-universality law for words with unequal neighbors

## Finding
Fix an alphabet \(\Sigma\) with \(q\ge 2\) letters. A word is *proper* if consecutive letters are different. Write \(I(w)\) for the largest integer \(k\) for which every word in \(\Sigma^k\) occurs as a scattered subsequence of \(w\). Let \(a_q(n,k)\) count proper words of length \(n\) with \(I(w)=k\), including the empty word at \(n=0\).

For \(1\le j\le q-1\) define
\[
D_j(t)=\prod_{r=0}^{j-1}(1-rt),\qquad
V_q(t)=\sum_{j=1}^{q-1}\frac{(q-1)!}{(q-j)!}\frac{t^j}{D_j(t)}.
\]
Then the **entire length-and-index distribution**, simultaneously for all alphabet sizes, is the rational function
\[
\boxed{\sum_{n,k\ge0}a_q(n,k)t^nu^k
=1+qV_q(t)+
\frac{u q!t^q\bigl(1+(q-1)V_q(t)\bigr)}
{D_{q-1}(t)-u(q-1)(q-1)!t^q}.}
\]
In particular the ternary case is
\[
\boxed{\sum_{n,k\ge0}a_3(n,k)t^nu^k=
\frac{1+2t+3t^2}{1-t}+
\frac{6ut^3(1+t+2t^2)}{(1-t)(1-t-4ut^3)}.}
\]

Let \(W_n\) be uniform over all proper words of length \(n\). For \(q\ge3\), put
\[
\mu_q=1+(q-1)H_{q-1},\qquad
v_q=(q-1)^2H_{q-1}^{(2)}-(q-1)H_{q-1},
\]
where \(H_m=\sum_{h=1}^m1/h\) and \(H_m^{(2)}=\sum_{h=1}^m1/h^2\). Then \(v_q>0\) and
\[
\mathbb E I(W_n)=\frac{n}{\mu_q}+O_q(1),\qquad
\operatorname{Var}(I(W_n))=\frac{v_q}{\mu_q^3}n+O_q(1),
\]
\[
\boxed{\frac{I(W_n)-n/\mu_q}{\sqrt{v_q n/\mu_q^3}}\ \Longrightarrow\ N(0,1).}
\]
For \(q=3\), the limiting mean is \(n/4\) and the leading variance is \(n/32\). The binary boundary case is deterministic: \(I(w)=\lfloor n/2\rfloor\) for every proper binary word.

## Assumptions and scope
The alphabet is labeled and fixed. A subsequence is order-preserving and need not be contiguous. The index of the empty word is zero. The bivariate generating series is a formal power series in \(t\) with polynomial coefficients in \(u\). Uniform sampling means each of the \(q(q-1)^{n-1}\) proper words has equal probability for \(n\ge1\). The Gaussian assertion concerns each fixed integer \(q\ge3\) as \(n\to\infty\).

## Proof
**Arch characterization.** Factor a word greedily into the shortest successive factors containing every alphabet symbol, followed by a suffix missing a symbol. If there are \(k\) completed factors (arches), then all length-\(k\) patterns are subsequences, by choosing one prescribed letter from each arch. To see that the index is not larger, let \(c_i\) be the terminal letter newly completing arch \(i\), and select \(c_{k+1}\) absent from the final suffix. To match the subsequence \(c_1\cdots c_kc_{k+1}\) greedily, one cannot choose \(c_i\) before the end of arch \(i\), inductively, so the last required letter is absent. Thus \(I(w)=k\).

**One-arch counts.** Within an incomplete arch, suppose exactly \(j\) distinct letters have appeared. The last letter is already among them. Properness gives exactly \(j-1\) choices for the next previously seen letter and \(q-j\) choices for a new one. Before the first letter there are \(q\) choices for an initial arch, or \(q-1\) when the preceding arch's terminal letter is fixed. For each \(j\), the generating factor for any number of old-letter steps is \(1/(1-(j-1)t)\). The numbers of words completing an arch are therefore
\[
A_0(t)=\frac{q!t^q}{D_{q-1}(t)},\qquad
A(t)=\frac{(q-1)(q-1)!t^q}{D_{q-1}(t)},
\]
respectively for the initial arch and an arch following a fixed preceding symbol. The generating functions of incomplete terminal pieces are
\[
B_0(t)=1+qV_q(t),\qquad B(t)=1+(q-1)V_q(t).
\]
The coefficient of \(t^j/D_j(t)\) in a piece visiting exactly \(j\) symbols is the product of the \(j-1\) new-symbol transition counts after its first letter; this establishes both terminal-piece formulas, including the empty piece.

**Concatenation and rationality.** Every proper word has one and only one greedy decomposition. Words with no arch contribute \(B_0(t)\); those with exactly \(k\ge1\) arches contribute \(A_0(t)A(t)^{k-1}B(t)\). After each completed arch, relabeling symmetry makes the counts depend only on the fact that the preceding letter is fixed, not on its identity. Hence
\[
\sum_{n,k\ge0}a_q(n,k)t^nu^k=B_0(t)+\frac{uA_0(t)B(t)}{1-uA(t)},
\]
which reduces algebraically to the boxed formula. Taking \(q=3\) gives the displayed specialization.

**Renewal law and Gaussian limit.** Sample an infinite proper word by choosing its initial letter uniformly and then choosing each successive letter uniformly among the \(q-1\) alternatives. The completed arch lengths are independent and identically distributed: the first new letter of each arch takes one step; after \(j\) letters have been seen, each further choice reveals a new letter with probability \((q-j)/(q-1)\), independent of which particular letters have been seen. Strong Markov restarting at completed arches makes the waiting lengths independent. Thus an arch length has the exact distribution
\[
L\ \stackrel{d}{=}\ 1+\sum_{j=1}^{q-1}G_j,\qquad
G_1=1\ \text{ almost surely},\qquad\mathbb P(G_j=s)=\frac{q-j}{q-1}\left(\frac{j-1}{q-1}\right)^{s-1},\quad 2\le j\le q-1,\ s\ge1,
\]
with independent geometric variables (the term for \(j=1\) is identically one). Its mean and variance are exactly \(\mu_q\) and \(v_q\). The index \(I(W_n)\) is the renewal count \(\max\{k:L_1+\cdots+L_k\le n\}\). For \(q\ge3\) the increments have exponential moments, finite positive variance, and span one; the elementary lattice renewal mean/variance expansions and renewal central limit theorem give the stated limits. At \(q=2\), each arch has length two, yielding the deterministic boundary statement.

## Verification
A standalone program, `verify.py`, computes coefficients independently in two ways. It (i) enumerates all proper words and determines their indices through greedy factorization, with direct scattered-subsequence verification at short lengths, and (ii) builds exact integer generating-function coefficients from the \(j-1\) old-letter and \(q-j\) new-letter transitions. Both methods agree for \(q=2\) through \(n=10\), \(q=3\) through \(n=12\), \(q=4\) through \(n=9\), and \(q=5\) through \(n=7\). In particular, the ternary histograms at \(n=3\) and \(n=6\) are \((6,6)\) and \((6,66,24)\). Run using `python verify.py`. These finite computations test the derivation but are not used as a proof for all lengths or alphabet sizes.

## Relationship to prior work
Arch factorization and its equality with subsequence-universality index are classical; Schnoebelen and Veron explicitly summarize this in their 2023 work. Adamson and coauthors provide general algorithms to count subsequence-universal words accepted by automata for regular languages (2023), and Adamson studies the unrestricted counting problem (2023). Since proper words form a regular language, those algorithms can in principle compute individual numerical entries here. The additional statements established here are the compact closed symbolic formula uniform in \(q\), the regeneration of arches under the no-equal-neighbors constraint, and explicit all-\(q\) probabilistic constants. The displayed formula is not an assertion that general regular-language counting was previously impossible.

## Limitations
This result applies only to the homogeneous adjacency restriction forbidding equal neighboring letters. It does not give corresponding formulas for arbitrary directed transition restrictions or nonuniform Markov transition probabilities. The scientific claim concerns the stated exact generating function and renewal consequences; no independent external audit is claimed. A prior equivalent reformulation outside the inspected literature cannot be excluded.

## References
1. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932, first public version April 24, 2023. https://arxiv.org/abs/2304.11932
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first public version November 17, 2023. https://arxiv.org/abs/2311.10658
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, first public version April 10, 2023. https://arxiv.org/abs/2304.04583
