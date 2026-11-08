# Prime-power cyclotomic strata and a sparse cyclic Gabor tomography transition

## Finding
Let \(n=p^k\), with \(p\) prime and \(k\ge1\). For every nonzero nonnegative rational window \(g\colon\mathbb Z/n\mathbb Z\to\mathbb Q_{\ge0}\), the entire nullity of the full Weyl-covariant rank-one-projector measurement operator is given by a finite collection of explicit rational **digit-fiber equalities**. More precisely, define \(h_a(x)=g(x)g(x-a)\) and, for \(1\le j\le k\),
\[
 H_{a,j}(r)=\sum_{\substack{0\le x<n\\x\equiv r\pmod {p^j}}}h_a(x),\qquad 0\le r<p^j.
\]
Put \(\varepsilon_{a,j}=1\) if there exist \(0\le r<p^{j-1}\) and \(0\le u,v<p\) for which
\[
 H_{a,j}(r+up^{j-1})\ne H_{a,j}(r+vp^{j-1}),
\]
and otherwise put \(\varepsilon_{a,j}=0\). Then the exact complex-linear operator-span rank is
\[
 \boxed{\operatorname{rank}\mathcal L_g=\sum_{a\in\mathbb Z/n\mathbb Z}\left[\mathbf1_{\{a\in S-S\}}+\sum_{j=1}^k(p^j-p^{j-1})\varepsilon_{a,j}\right],}\qquad S=\operatorname{supp}g.
\]
For a fixed \(a\), each Fourier modulation of additive order \(p^j\) is either present (all \(p^j-p^{j-1}\) such modulations) or absent, according precisely to \(\varepsilon_{a,j}\). For \(k=2\), the per-shift ranks are therefore drawn from \(\{0,1,p,p^2-p+1,p^2\}\).

There is a concrete sparsity-sensitive consequence for every **odd** prime \(p\). Set \(n=p^2\) and
\[
 S_p=\{0,1,\ldots,p-1\}\cup\{0,p,2p,\ldots,(p-1)p\}\subseteq\mathbb Z/n\mathbb Z.
\]
This canonical base-\(p\) digit cross has \(2p-1\) points and \(S_p-S_p=\mathbb Z/n\mathbb Z\). For its flat window \(u=\mathbf1_{S_p}\), the complete per-shift rank classification is
\[
 \operatorname{rank}_a\mathcal L_u=
 \begin{cases}
 p,&a\in\{p,2p,\ldots,(p-1)p\},\\
 p^2-p+1,&a\in\{1,-1\},\\
 p^2,&\text{otherwise}.
 \end{cases}
\]
Thus
\[
 \boxed{\operatorname{rank}\mathcal L_u=p^4-(p-1)(p^2-p+2).}
\]
The **same support**, with the explicit positive integer taper \(g(x)=2^x\mathbf1_{S_p}(x)\) for the standard representative \(0\le x<n\), gives
\[
 \boxed{\operatorname{rank}\mathcal L_g=p^4,}
\]
so all rank-one projectors form a basis of the complex matrix space. In fact, for any odd prime power \(n=p^k\) and any nonempty support \(S\subseteq\mathbb Z/n\mathbb Z\), the taper \(g_S(x)=2^x\mathbf1_S(x)\) satisfies \(\operatorname{rank}\mathcal L_{g_S}=n|S-S|\). The difference-cover lower bound \(|S|(|S|-1)\ge n-1\) shows that a fully informationally complete window on \(\mathbb Z/p^2\mathbb Z\) must occupy at least \(p+1\) sites; this construction uses \(2p-1\) sites.

## Assumptions and scope
The cyclic index set is identified with \(\{0,\ldots,n-1\}\) for defining the integer taper. Translation and modulation on \(\mathbb C^n\) are \((T_af)(x)=f(x-a)\) and \((M_bf)(x)=e^{2\pi ibx/n}f(x)\). For any window \(g\), form the \(n^2\) projectors \(P_{a,b}=(M_bT_ag)(M_bT_ag)^*\) and the complex-linear analysis map \(\mathcal L_g(A)=(\operatorname{tr}(AP_{a,b}))_{a,b}\), with \(A\) an arbitrary complex \(n\)-by-\(n\) matrix. Rank is invariant under normalizing \(g\), so unnormalized windows are used throughout. The general digit-fiber formula holds for \(p=2\) too; the explicit taper/digit-cross full-rank conclusion assumes odd \(p\). No claim about uniform conditioning, sparse phase retrieval with fewer measurements, or minimum possible support size is made.

## Proof
First, expand \(gg^*\) in the orthogonal Weyl matrix basis \(\{M_bT_a\}_{a,b}\). Under conjugation by \(M_sT_t\), each Weyl coefficient is multiplied by a character of the translation-modulation parameters. Orthogonality of the \(n^2\) characters gives a diagonal Fourier representation of the measurement analysis map. Its eigenvalue support is the nonvanishing set of
\[
 A_g(a,b)=\langle g,M_bT_ag\rangle=\sum_{x=0}^{n-1}g(x)g(x-a)e^{2\pi ibx/n},
\]
up to complex conjugation according to the inner-product convention. Hence \(\operatorname{rank}\mathcal L_g=\#\{(a,b):A_g(a,b)\ne0\}\). This Weyl-rank identity is classical; the arithmetic evaluation below is the added content.

Second, if \(b=0\), positivity gives \(A_g(a,0)>0\) exactly when \(a\in S-S\). If \(b\) has order \(p^j\), fold the rational coefficients \(h_a\) modulo \(p^j\). With \(\zeta\) a primitive \(p^j\)-th root and \(b=p^{k-j}v\), \(p\nmid v\), we obtain \(A_g(a,b)=\sum_{r=0}^{p^j-1}H_{a,j}(r)\zeta^{vr}\). The minimal polynomial over \(\mathbb Q\) is
\[
 \Phi_{p^j}(X)=1+X^{p^{j-1}}+\cdots+X^{(p-1)p^{j-1}}.
\]
A polynomial of degree less than \(p^j\) vanishes at \(\zeta^v\) precisely when it is \(\Phi_{p^j}(X)\) times a polynomial of degree at most \(p^{j-1}-1\). Comparing coefficients shows that this is exactly the condition that all \(p\) values \(H_{a,j}(r+tp^{j-1})\) agree for each \(r\). It holds simultaneously for all \(\varphi(p^j)=p^j-p^{j-1}\) primitive frequencies. Summing over \(a\) proves the displayed rank formula.

Third, for odd \(n\), fix a displacement \(a\). Wherever \(g_S(x)g_S(x-a)\ne0\), its value is the integral power \(2^{e_a(x)}\), with
\[
 e_a(x)=x+((x-a)\bmod n)=2x-a+n\mathbf1_{\{x<a\}}.
\]
These exponents are pairwise distinct: equality at two representatives would give \(2(x-y)\in\{0,n,-n\}\); because \(n\) is odd, only \(x=y\) is possible. Consequently every folded coefficient \(H_{a,j}(r)\) is a sum of **distinct binary powers**, and disjoint residue classes have disjoint collections of those powers. Such sums cannot be equal unless both are zero. If the overlap is nonempty, at least one digit fiber has a nonzero member, making \(\varepsilon_{a,j}=1\) for every \(j\). The zero-frequency term is then positive too. This establishes \(\operatorname{rank}\mathcal L_{g_S}=n|S-S|\).

Finally, every residue modulo \(p^2\) equals \(r-tp\) with \(0\le r,t<p\), proving the digit-cross difference-cover property. For the flat cross, \(a=0\) has all \(p^2\) modulations; every nonzero multiple of \(p\) has intersection \(S_p\cap(S_p+a)=\{0,p,\ldots,(p-1)p\}\), so exactly its \(p\) order-at-most-\(p\) modulations survive. For \(a=\pm1\), the intersection is \(p\) consecutive residues, exactly one in each class modulo \(p\): precisely the \(p-1\) order-\(p\) frequencies vanish. Every other nonzero shift has a nonempty intersection of size strictly less than \(p\), so neither digit-fiber condition can hold: all \(p^2\) modulations survive. To verify the intersection bound, split differences into pairs from the two axes; the cross-axis contributions give at most two pairs, while a displacement of magnitude \(r\) within the short axis gives \(p-r\) pairs, with one additional cross-axis pair and hence at most \(p-1\) for \(2\le r<p\). Counting the \(p-1\) multiples of \(p\) and two unit shifts yields the flat-cross rank formula. The tapered case follows from the previous paragraph.

## Verification
The accompanying `checker.py` tests the exact digit-fiber predictions against direct complex Fourier sums for randomized rational nonnegative windows on cyclic orders \(4,8,9,25,27,49\), including prime powers of both parities. It verifies the complete flat-cross per-shift histograms and tapered full rank for \(p=3,5,7,11\). An independently assembled \(81\)-projector Gabor analysis matrix in dimension \(9\) has numerical rank \(65\), agreeing with the exact flat-cross formula. Finite tests are checks, not the proof of the infinite statements; the cyclotomic argument above proves them.

## Relationship to prior work
Bojarovska–Flinth (2015) derive the nonzero-ambiguity sufficient condition for finite Gabor phase retrieval and treat difference-set windows. Bojarovska–Paternostro (2015) analyze difference-set Gabor fusion frames and their coherence. Goldberger–Kang–Okoudjou (2021) identify the general Gabor-projector rank with the number of nonzero Weyl ambiguity coefficients. None of these statements itself evaluates the rational prime-power valuation layers, the base-\(p\) cyclic digit-cross nullity, or its explicit amplitude-reweighted transition. This theorem builds on their Weyl diagonalization but does not reassert that diagonalization as new. The cyclotomic identity is standard, and the additional content is its complete quantitative application to these Gabor tomography ranks and the cyclic sparse construction.

## Limitations
The explicit taper \(2^x\) can have extremely large dynamic range and is **not** asserted to be numerically well-conditioned. Linear informational completeness of the lifted matrix map is stronger than ordinary phase retrieval but is not a claim of stable noisy recovery. The support size \(2p-1\) is within a factor approaching two of the simple counting lower bound; optimal sparsity is not claimed. The historical priority of these exact arithmetic specializations and of the cross-window rank needs independent verification against the broader finite Gabor literature.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first posted 2015-03-19; https://arxiv.org/abs/1503.05800.
2. I. Bojarovska and V. Paternostro, *Gabor fusion frames generated by difference sets*, arXiv:1507.01829, first posted 2015-07-07; https://arxiv.org/abs/1507.01829.
3. A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509, first posted 2021-06-02; https://arxiv.org/abs/2106.01509.
