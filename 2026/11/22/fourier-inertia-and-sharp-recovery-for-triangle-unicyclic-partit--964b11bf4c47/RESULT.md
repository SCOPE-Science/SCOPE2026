# Fourier inertia and sharp recovery for triangle-unicyclic partition profiles

## Finding
For each integer \(n\ge3\), let \(G\) be **any** connected simple graph on \([n]\) whose only cycle is a triangle. Thus \(|E(G)|=n\). For a set partition \(\pi\) of \([n]\), let \(x(\pi)\in\mathbb F_2^{E(G)}\) have coordinate one exactly when an edge's two endpoints belong to the same block. Let \(f_G(x)=|\{\pi:x(\pi)=x\}|\), and let \(T_G\) denote unnormalized convolution by \(f_G\) on \(\ell^2(\mathbb F_2^{E(G)})\).

**Theorem (full inertia and sharp recovery).** Every Walsh multiplier of \(T_G\) is nonzero, so \(T_G\) is invertible for every \(n\ge3\). It is strictly positive definite if and only if \(n\ge10\). For \(3\le n\le9\), its negative index, respectively, equals
\[
(1,2,4,8,11,6,1),
\]
and all other Fourier multipliers are positive. The complete spectrum, negative index, and sharp inverse norm are **independent of the position and shapes of all trees attached to the triangle**.

Write \(B_j\) for the Bell numbers, \(s=n-3\), and define
\[
U_{n,k}=\sum_{j=0}^{k}\binom kj(-2)^j B_{n-j}\quad(0\le k\le n),
\]
\[
V_{s,r}=U_{s+3,r+3}-8\sum_{j=0}^{r}\binom rj(-2)^j(B_{s-j+1}-B_{s-j})\quad(0\le r\le s).
\]
For a Walsh frequency supported on \(H\subseteq E(G)\), its multiplier is \(U_{n,|H|}\) if \(H\) does **not** contain all three triangle edges, and \(V_{s,r}\) if it does, where \(r\) is its number of remaining edges. The latter multiplier has multiplicity \(\binom sr\) among triangle-containing frequencies. This is the complete unnormalized spectrum with multiplicities: the remaining frequencies are indexed directly by their edge subsets \(H\).

Let \(g_n\) be the minimum absolute value of any multiplier. The exact sharp gaps for \(n=3,4,5,6,7,8,9\) are, respectively,
\[
(g_3,g_4,g_5,g_6,g_7,g_8,g_9)=(1,1,2,1,1,26,185).
\]
For every \(n\ge10\), the minimum is attained precisely by the Walsh character selecting **every edge** and is the positive integer
\[
\boxed{g_n=V_{n-3,n-3}=\sum_{j=0}^{n-3}\binom{n-3}{j}(-2)^j\bigl(B_{n-j}-6B_{n-j-1}+4B_{n-j-2}\bigr)}.
\]
All Bell arguments in the displayed finite sum are nonnegative because \(j\le n-3\). Consequently
\[
\|T_G^{-1}\|_{2\to2}=g_n^{-1},\qquad \kappa_2(T_G)=B_n/g_n.
\]
These constants are exact, not asymptotic.

## Assumptions and scope
Set partitions are unordered collections of nonempty blocks, counted once each; several partitions may induce the same profile and their multiplicity is retained. The Walsh character at frequency \(H\) is \((-1)^{\sum_{e\in H}x_e}\). The transform and convolution are **unnormalized**, the graph is labelled and has a unique triangular cycle, and the Fourier space has \(n\) binary edge coordinates, not all \(\binom n2\) pairs. The operator is a real symmetric matrix because the Boolean group has exponent two. The condition number is the ratio of its largest to smallest singular value, without restricting to positive eigenvalues.

## Proof
**1. Contraction and exact spectral sectors.** If \(F\subseteq E(G)\), imposing that every edge of \(F\) have endpoints in the same partition block identifies the connected components of \(([n],F)\). Hence there are exactly \(B_{c(F)}\) compatible set partitions. Inclusion–exclusion in the Walsh product gives
\[
\lambda_G(H)=\sum_{F\subseteq H}(-2)^{|F|}B_{c(F)}.
\]
When \(H\) lacks a triangle edge, every \(F\subseteq H\) is a forest and \(c(F)=n-|F|\), giving \(U_{n,|H|}\). When \(H\) contains the triangle, exactly those subgraphs \(F\) which contain all three triangle edges have \(c(F)=n-|F|+1\), rather than \(n-|F|\). Correcting these terms, with \(r\) edges outside the triangle, gives the stated \(V_{s,r}\). Because only the presence of the unique triangle affects the contraction count, every assertion is independent of attached-tree shape.

**2. Poisson moments and the entire forest sector.** If \(X\) is a Poisson random variable of mean one, the Dobinski identity \(B_j=\mathbb E X^j\) yields
\[
U_{n,k}=\mathbb E[X^{n-k}(X-2)^k].
\]
At the last allowed forest weight, Poisson size-bias \(\mathbb E[Xh(X)]=\mathbb E[h(X+1)]\) gives
\[
U_{n,n-1}=\mathbb E[(X-1)^{n-1}]=A_{n-1},
\]
where \(A_m\) is the known number of partitions of \([m]\) with no singleton blocks (the exponential generating series is \(\exp(e^z-1-z)\)). This is strictly positive for every \(m\ge2\). Moreover, for \(0\le k\le n-2\),
\[
U_{n,k}-U_{n,k+1}=2U_{n-1,k}.
\]
Starting with \((U_{3,0},U_{3,1},U_{3,2})=(5,1,1)\), induction proves every forest-sector multiplier strictly positive and, for \(n\ge4\), strictly decreasing in its weight. Their minimum is \(A_{n-1}\).

**3. Triangle-sector recursion and eventual positivity.** Define the cubic
\[
Q(x)=(x-2)^3-8(x-1)=x(x^2-6x+4).
\]
The contraction correction and Poisson identity give the exact moment representation
\[
V_{s,r}=\mathbb E[X^{s-r}(X-2)^rQ(X)].
\]
For \(0\le r<s\), subtracting adjacent terms gives
\[
V_{s,r}-V_{s,r+1}=2V_{s-1,r}.
\]
The boundary term \(V_{s,s}=\mathbb E[(X-2)^sQ(X)]\) is strictly positive for every integer \(s\ge6\). Indeed \(Q(0)=0\), \(Q(2)=-8\) contributes zero for \(s\ge1\), \(Q(1)=-1\), \(Q(3)=-15\), \(Q(4)=-16\), \(Q(5)=-5\), and \(Q(m)>0\) for all integers \(m\ge6\). Keeping only the positive \(m=6\) term in the Dobinski series and bounding the four negative terms gives the sufficient inequality
\[
\frac{4^s}{30}>1+\frac52+\frac{2^{s+1}}3+\frac{3^s}{24}.
\]
It holds at \(s=6\), and remains true for all larger integers because, after division by \(4^s\), each term on the right strictly decreases. Thus the boundary positivity is an **infinite** argument, not finite enumeration.

The complete exact row at \(s=7\) is
\[
(V_{7,0},\ldots,V_{7,7})=(5653,6023,5153,4107,3165,2399,1801,1347),
\]
all positive, with unique minimum at its last entry. Induction using the adjacent-difference identity and boundary positivity shows that for each \(s\ge8\), every \(V_{s,r}\) is positive and **strictly decreasing in \(r\)**. (The row \(s=7\) is positive but not itself monotone from its first entry.) Together with the finite rows below, this proves the positivity transition is exactly \(n=10\).

**4. Sharp comparison between sectors.** Subtracting the triangle boundary moment from the forest minimum gives, for every \(s\ge0\),
\[
U_{s+3,s+2}-V_{s,s}=2\mathbb E[X^2(X-2)^s]=2U_{s+2,s}>0,
\]
by Step 2. Therefore for \(s\ge7\) the smallest multiplier is the triangle boundary value \(V_{s,s}\), which is positive and attained only at the full-edge frequency. Since the zero-frequency eigenvalue is \(B_n\), and the triangle inequality ensures no Fourier multiplier has greater absolute value, the sharp inverse norm and condition number follow.

**5. All small orders without an extrapolation.** The rows for \(s=0,1,\ldots,6\), each listed in increasing \(r\), are exactly
\[
\begin{array}{c|l}
0&(-3)\\
1&(-7,-1)\\
2&(-18,-4,-2)\\
3&(-49,-13,-5,-1)\\
4&(-133,-35,-9,1,3)\\
5&(-310,-44,26,44,42,36)\\
6&(-185,435,523,471,383,299,227).
\end{array}
\]
All entries are nonzero. Their negative entries, counted with multiplicity \(\binom sr\), yield exactly the seven stated negative indices. Compare their absolute values with the strictly positive forest-sector minima \(A_{n-1}\) to obtain the seven stated spectral gaps. This is a complete finite integer calculation with an independently reproducible certificate, not an induction guess.

## Verification
The accompanying standalone Python 3 program `verify_triangle.py` performs exhaustive restricted-growth-word enumeration of every partition for \(3\le n\le9\), on two distinct triangle-unicyclic attachment topologies at each order. It computes the entire independent fast Walsh transform of the profile histogram and checks every coefficient against the contraction formula. It independently checks the finite inertia/gap rows and algebraic recurrence identities through \(n=180\). On execution, it reports `PASS 34286 exact integer tests`. These finite checks corroborate the formulas; the infinite positivity and exact gaps are proved in Steps 2–4 by recurrences and a rigorous Poisson-series domination.

## Relationship to prior work
Classical graphical Stirling and Bell counting for forests and cycles (Galvin–Thanh, 2012; Duncan–Peele, 2009) already describes unsigned proper-block partitions, and the tree co-block marginal law has been explicitly established. Chern–Diaconis–Kane–Rhoades (2014) study adjacent same-block statistics (levels), but do not supply this convolution inertia classification. OEIS A126617 records the **known** shifted Bell/Poisson moments \(\mathbb E[(X-2)^k]\), including their eventual positive sign; OEIS A000296 records the known no-singleton Bell numbers. These sequences and basic contraction/inclusion–exclusion are not claimed as novel. A preexisting published-finding corpus exact all-frequency **general-graph** inclusion–exclusion formula also covers the raw signed sums when one restricts its frequencies to this graph; that formula does **not** identify the full infinitely parametrized sign pattern, the sharp positive-definite threshold, all negative indices or the sharp minimum eigenvalue. The specific contribution assessed here is precisely those **global Fourier inertia and sharp recovery** conclusions across every attachment shape.

## Limitations
The theorem applies only to connected simple graphs with one triangular cycle. It does not extend to unique cycles of other lengths, to general equivalence-relation convolutions on all pair coordinates, to signed weights on partitions, or to arbitrary graph topology. The displayed exact spectral expressions are elementary specializations of earlier general inclusion–exclusion; historical priority is asserted only cautiously for the sign-transition and optimization conclusions. The independent mathematical audit has not been performed.

## References
1. D. Galvin and D. T. Thanh, *Stirling numbers of forests and cycles*, arXiv:1206.3591v1, first public version 2012-06-15, Section 2 and Eq. (10). https://arxiv.org/abs/1206.3591
2. B. Duncan and R. Peele, *Bell and Stirling Numbers for Graphs*, Journal of Integer Sequences 12 (2009), Article 09.7.1. https://cs.uwaterloo.ca/journals/JIS/VOL12/Peele/peele5.pdf
3. B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Closed expressions for averages of set partition statistics*, 2014-06-17. https://link.springer.com/article/10.1186/2197-9847-1-2
4. OEIS A126617, shifted Bell-number transform and Poisson moment, formula dated 2007-08-04. https://oeis.org/A126617
5. OEIS A000296, partitions without singleton blocks. https://oeis.org/A000296
6. *Exact dyadic Walsh valuations for equivalence-relation supports*, published-finding corpus, 2026-11-16, full RESULT.md compared. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-dyadic-walsh-valuations-for-equivalence-relation-supports--8c788e5d89ed
7. *Two shared edges force positive co-block covariance in fixed-block random partitions*, published-finding corpus, 2026-11-02, full RESULT.md compared. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-shared-edges-force-positive-co-block-covariance-in-fixed-blo--44a13e35c143
