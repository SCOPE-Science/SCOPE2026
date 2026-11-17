# Sharp variation nonattainment threshold for cyclic entropy-smoothed maxima

## Finding

Fix integers \(n\ge2\) and \(1\le w\le n\), a temperature \(\tau>0\), and arbitrary positive site weights \(q_0,\ldots,q_{n-1}\). With all indices interpreted modulo \(n\), define the cyclic entropy-smoothed maximum
\[
(Fx)_i=\tau\log\!\left(\sum_{j=0}^{w-1}q_{i+j}\exp(x_{i+j}/\tau)\right),\qquad 0\le i<n.
\]
For the cyclic adjacent variation \(V(h)=\sum_{i=0}^{n-1}|h_{i+1}-h_i|\), the sharp **two-input** Lipschitz coefficient is
\[
\boxed{\sup_{V(x-y)>0}\frac{V(Fx-Fy)}{V(x-y)}=\begin{cases}1,&1\le w<n,\\0,&w=n.\end{cases}}
\]
For \(1\le w<n\), the sharp coefficient \(1\) is **attained by distinct finite input pairs if and only if** \(n\ge2w\). If \(w<n<2w\), every distinct input pair with positive input variation satisfies the **strict** inequality \(V(Fx-Fy)<V(x-y)\), yet no uniform constant below \(1\) works for all such pairs. These assertions hold independently of the temperature and of the positive weights.

## Assumptions and scope

Signals are all real \(n\)-tuples. The integer \(w\) counts consecutive cyclic sites with no repeats because \(w\le n\). The weights \(q_j\) are **fixed at sites**, not reindexed as arbitrary row-specific weights; this shared-weight condition is essential to the moving-window stochastic-order argument. All weights and \(\tau\) are finite and strictly positive. The operator acts simultaneously, in one filtering pass. Variation of a constant vector is zero, and the quotient excludes zero denominators. The map obeys \(F(x+c\mathbf1)=Fx+c\mathbf1\), so changing an input by a constant cannot change the output variation.

## Proof

**1. Positive Jacobian and a gradient factorization.** For \(w<n\), fix \(z\in\mathbb R^n\) and put \(a_j=q_j\exp(z_j/\tau)>0\), periodically extended to integer indices. Let \(W_i=\{i,\ldots,i+w-1\}\) in an unwrapped integer coordinate and \(Z_i=\sum_{j\in W_i}a_j\). Differentiating gives
\[
(J_z h)_i=\sum_{j\in W_i}\frac{a_j}{Z_i}h_j.
\]
Let \(\pi_i\) be the probability distribution on \(W_i\) with masses \(a_j/Z_i\), and let \(G_i(k)=\pi_i(({-}\infty,k])\). As \(W_i\) moves to \(W_{i+1}\), it loses its leftmost mass and gains a rightmost mass, with unchanged positive masses on the common sites. Thus \(\pi_i\) is stochastically no larger than \(\pi_{i+1}\), and, for every integer \(k\in\{i,\ldots,i+w-1\}\),
\[
 c_{i,k}:=G_i(k)-G_{i+1}(k)>0.
\]
Outside this range the difference is zero. One can check the strict sign directly: if \(i<k<i+w-1\), write the common-window mass to the left of \(k\) as \(P\) and to its right as \(Q\). The two cumulative probabilities are \((a_i+P)/(a_i+P+Q)\) and \(P/(P+Q+a_{i+w})\), respectively. The boundary cases are also strictly positive.

Summation by parts (both probability distributions have mass one) gives the **exact** identity
\[
 (J_z h)_{i+1}-(J_z h)_i=\sum_{k=i}^{i+w-1}c_{i,k}(h_{k+1}-h_k).
\]
Let \(D\) denote cyclic first differences. After reducing each integer index modulo \(n\), this reads \(D J_z=C_z D\), where \(C_z\) has strictly positive entries precisely in the \(w\) consecutive positions \(k=i,\ldots,i+w-1\) of row \(i\), and zero elsewhere. For fixed edge index \(k\), the column sum telescopes:
\[
\sum_{i=0}^{n-1}(C_z)_{i,k}
=\sum_{i=k-w+1}^{k}\bigl(G_i(k)-G_{i+1}(k)\bigr)
=G_{k-w+1}(k)-G_{k+1}(k)=1.
\]
Consequently \(C_z\) is nonnegative and column-stochastic; hence \(V(J_z h)=\|C_z D h\|_1\le\|D h\|_1=V(h)\).

**2. Global nonexpansivity.** Put \(h=y-x\). Differentiability and the fundamental theorem of calculus yield
\[
F(y)-F(x)=\int_0^1 J_{x+th}h\,dt.
\]
By the triangle inequality and part 1, \(V(Fy-Fx)\le\int_0^1V(J_{x+th}h)\,dt\le V(h)\). For \(w=n\), each window contains all sites and hence every output coordinate is identical; therefore the sharp coefficient is zero.

**3. Nonattainment below the half-cycle window threshold.** Suppose \(w<n<2w\). Each column of \(C_z\) has strictly positive entries on a circular arc of exactly \(w\) output edges. Any two such arcs intersect because \(2w>n\). For a nonconstant \(h\), the real edge gradient \(g=Dh\) is nonzero and has both a positive and a negative entry since \(\sum_i g_i=0\). The corresponding positive and negative columns of \(C_z\) overlap on at least one row, where their contributions cancel strictly in the absolute-value triangle inequality. Hence
\[
\|C_z g\|_1<\|g\|_1.
\]
This is true at every point on the segment between any finite \(x\) and \(y\) with \(V(y-x)>0\). Continuity along the compact segment makes the integrated inequality strict. No finite pair can attain coefficient one.

**4. Exact attainment at and above the threshold.** Suppose \(n\ge2w\), and let \(S\) be a contiguous circular arc containing exactly \(w\) sites. Set \(h=\mathbf1_S\), so \(V(h)=2\), and take arbitrary \(x\) and \(y=x+h\). Some complete window is contained in \(S\), while another complete window is contained in its complement. The output difference \(F(y)-F(x)\) equals exactly \(1\) on the first window and exactly \(0\) on the second; it lies in \([0,1]\) everywhere else by monotonicity and translation equivariance. Any cyclic vector taking both values \(0\) and \(1\) has variation at least \(2\). By nonexpansivity it has variation at most \(2\), so equality holds.

**5. Sharp but unattained coefficient on shorter cycles.** For any \(1\le w<n\), fix a site \(j\) and take \(x^{(M)}=M\mathbf1_{\{j\}}\) and \(y^{(M)}=(M+1)\mathbf1_{\{j\}}\). The input difference has variation \(2\). As \(M\to\infty\), the output difference tends to \(1\) on each of the exactly \(w\) windows containing \(j\), and to \(0\) on the remaining windows, since the positive weight on \(j\) dominates each containing window. The limiting output is the indicator of a proper cyclic arc and has variation \(2\). Thus the sharp supremum is \(1\) even when part 3 prevents exact attainment.

## Verification

Run `python3 check_cyclic_softmax_bv.py` from the package directory. The standalone checker uses Python standard-library exact rational arithmetic to test the Jacobian–gradient factorization, positivity and column sums for \(792\) positive-weight cases through \(12\) sites; verifies strict overlap in \(360\) cases; checks \(36\) explicit finite-attainment configurations, \(198\) weighted-temperature two-input secants, and full-window constant outputs. Finite checks are corroboration only: the statements for all lengths, all positive weights and all temperatures follow from the proof above.

## Relationship to prior work

Nesterov's dated 2003 preprint develops entropy smoothing of finite maxima and explicitly gives the log-sum-exp value and softmax derivative (Section 4.1, Lemma 4). Its results concern optimization smoothing and do not assert cyclic-variation stability or an equality-versus-nonattainment threshold. Published finite-window morphological analysis establishes two-input variation contraction of sliding minima and maxima **on nonperiodic paths**, not the strict-attainment geometry for the cyclic entropy-smoothed operator. The nonexpansivity half of this finding can also be seen as a consequence of the known Gumbel random-maximum representation together with a suitable running-maximum contraction inequality; it is **not** claimed as an independent new principle. The specific result here is the complete sharp *attainment classification* for the smooth cyclic operator, including strict finite-pair contraction whenever the window covers more than half the cycle. Aldaz and Pérez Lázaro's one-dimensional maximal-function BV estimates concern a supremum over averaging radii and a one-input variation estimate, not this two-input smooth-window problem.

## Limitations

The result does not apply to row-adaptive weights that fail to come from one shared set of site masses, noncontiguous neighborhoods, multidimensional arrays, or arbitrary graph neighborhoods. The strict inequality for \(w<n<2w\) is not a uniform contraction by a factor below one on the whole unbounded input space; the concentrating construction proves that no such factor exists. The proof does not quantify the optimal coefficient on bounded-contrast subsets. Historical priority remains provisional against unindexed older literature on ordered Markov kernels and entropy-smoothed morphological operators; the nonperiodic morphological source was examined in its available repository full text, while some older general texts were not fully accessible.

## References

1. Yu. Nesterov, *Smooth minimization of non-smooth functions*, CORE Discussion Paper 2003/12, dated 10 January 2003 on the original open preprint cover, https://research.dial.uclouvain.be/bitstreams/5e279fca-57a4-4476-9fe8-e8df213808c4/download ; journal version *Mathematical Programming* 103 (2005), 127–152, DOI: 10.1007/s10107-004-0552-5.
2. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, public mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2/RESULT.md ; explicit nonperiodic path setting and sharp variation statement read in full.
3. J. M. Aldaz and J. Pérez Lázaro, *Functions of bounded variation, the derivative of the one dimensional maximal function, and applications to inequalities*, arXiv:math/0601044, submitted 3 January 2006; *Transactions of the American Mathematical Society* 359 (2007), 2443–2461, https://arxiv.org/abs/math/0601044 .
4. J. Goutsias and H. J. A. M. Heijmans, *Nonlinear multiresolution signal decomposition schemes. I. Morphological pyramids*, *IEEE Transactions on Image Processing* 9 (2000), 1862–1876, DOI: 10.1109/83.877209 (abstract/bibliographic comparison only).
