# The complete strand-autodistance spectrum of balanced homopolymer-free DNA

## Finding
Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick complement \(\bar A=T\), \(\bar T=A\), \(\bar C=G\), \(\bar G=C\). For each integer \(m\ge1\), let \(\mathcal H_m\) be the set of length-\(2m\) words with precisely \(m\) letters from \(\{C,G\}\) and no identical neighboring symbols. Put \(R(x)=\bar x_{2m}\cdots\bar x_1\), and define \(N_m(r)=|\{x\in\mathcal H_m:d_H(x,R(x))=2r\}|\), for \(0\le r\le m\).

The following matrix formula gives every \(N_m(r)\) exactly. Index sixteen states by ordered pairs \(s=(a,b)\in\Sigma^2\). Set
\[
 g(a)=\mathbf1_{\{a\in\{C,G\}\}},\quad w_s=g(a)+g(b),\quad h_s=\mathbf1_{\{a\ne b\}},
\]
\[
 D(u,v)_{s,s}=u^{w_s}v^{h_s},\quad
 T_{(a,b),(c,d)}=\mathbf1_{\{a\ne c\}}\mathbf1_{\{b\ne d\}},\quad
 c_{(a,b)}=\mathbf1_{\{a\ne\bar b\}}.
\]
With \(\boldsymbol1\) the all-ones column, the complete strand-autodistance polynomial is
\[
 \boxed{\sum_{r=0}^{m}N_m(r)v^r=[u^m]\,\boldsymbol1^{\mathsf T}D(u,v)\bigl(TD(u,v)\bigr)^{m-1}c.}
\]
The exponent of \(v\) measures half the Hamming distance, not the full distance. For each \(m\), the exact support is
\[
 \boxed{\{r:N_m(r)>0\}=\{m\bmod2,m\bmod2+1,\ldots,m\}.}
\]
Consequently, \(\min_{x\in\mathcal H_m}d_H(x,R(x))=0\) for even \(m\), and \(2\) for odd \(m\); in all cases the maximum is \(2m\).

A uniformly chosen \(X_m\in\mathcal H_m\) has \(r_m=d_H(X_m,R(X_m))/2\) satisfying
\[
 \boxed{\frac{r_m-3m/4}{\sqrt{15m/64}}\ \Longrightarrow\ \mathcal N(0,1).}
\]
Moreover, the exact self-reverse-complement frequency is zero when \(m\) is odd and, as \(m\to\infty\) through even values,
\[
 \boxed{\frac{N_m(0)}{|\mathcal H_m|}\sim\sqrt2\,3^{-m}.}
\]
These statements concern aligned whole-word reverse-complement Hamming distance, not thermodynamic folding or all shifted stem alignments.

## Assumptions and scope
The alphabet and complement involution are fixed as above; all words are linear, labeled and oriented. No equality is allowed between consecutive letters, including the middle two. The GC count is exactly half of the even blocklength. The domain is every integer \(m\ge1\); no assertion about odd blocklengths, longer run constraints, or pairwise codebook distances is made. The transfer expression is exact over the integers, with no asymptotic approximation involved.

## Proof
**1. Paired-coordinate bijection.** Given \(x\), set \(a_i=x_i\) and \(b_i=\bar x_{2m+1-i}\), for \(1\le i\le m\). These two sequences determine \(x\) uniquely. The original nearest-neighbor inequalities are equivalent to \(a_i\ne a_{i+1}\) and \(b_i\ne b_{i+1}\), for all \(i<m\), together with the central inequality \(a_m\ne\bar b_m\). Since complementation preserves GC type, the GC count of \(x\) is \(\sum_i(g(a_i)+g(b_i))\). Each paired position contributes either zero or two mismatches to \(d_H(x,R(x))\); the number of mismatched pairs is \(\sum_i\mathbf1_{\{a_i\ne b_i\}}\). Enumerating the paired states with these transition weights proves the matrix identity, including \(m=1\).

**2. Complete support.** If \(r=0\), every pair has \(a_i=b_i\), so the GC count is even. Therefore when \(m\) is odd, \(r=0\) is impossible. For even \(m\), take \(a_i=A\) at odd \(i\), \(a_i=C\) at even \(i\); choose each \(b_i\) independently from the same GC type as \(a_i\). These choices make both coordinate tracks proper and ensure GC total \(m\). The center must be matched, \(b_m=a_m\), because the only unequal same-type letter is its Watson–Crick complement and would violate the central boundary. At any chosen subset of the first \(m-1\) indices, take \(b_i\ne a_i\); elsewhere take equality. This realizes each \(r=0,\ldots,m-1\). For odd \(m\), use the same alternating \(a_i\); take \(b_m=G\), \(b_{m-1}=C\) when \(m>1\), and for \(i<m-1\) choose \(b_i\) from the same GC type as \(a_i\). All nearest-neighbor inequalities hold, the changed center raises the GC total to \(m\), and choosing an arbitrary subset of the first \(m-2\) positions to mismatch realizes \(r=1,\ldots,m-1\). For \(m=1\), the center pair \((A,G)\) realizes \(r=1\). Finally, for any \(m\), alternating paired states \((A,C),(C,A),(A,C),\ldots\) yields GC total \(m\), satisfies the central inequality, and realizes \(r=m\). Thus the claimed support is both necessary and sufficient.

**3. Gaussian law.** For asymptotics normalize \(T\) by \(9\). Its kernel is the tensor square of the four-state proper-color transition \(P=(J-I)/3\), whose stationary distribution is uniform and whose eigenvalues are \(1,-1/3,-1/3,-1/3\). The paired chain is primitive and stationary-uniform. Put \(G_i=g(a_i)+g(b_i)\), \(H_i=\mathbf1_{\{a_i\ne b_i\}}\). The stationary means are \(\mathbb E G_i=1\), \(\mathbb E H_i=3/4\), and direct character decomposition gives, for all \(k\ge0\),
\[
 \operatorname{Cov}(G_i,G_{i+k})=\tfrac12(-\tfrac13)^k,\quad
 \operatorname{Cov}(H_i,H_{i+k})=\tfrac3{16}(\tfrac19)^k,
\]
with all cross-lag covariances \(\operatorname{Cov}(G_i,H_j)=0\). Summing these geometric covariances gives the asymptotic joint covariance matrix per paired coordinate \(\operatorname{diag}(1/4,15/64)\).

For completeness, the finite-state Markov additive local limit argument is nondegenerate: from state \((A,C)\), four-step return walks have additive totals \((\sum G,\sum H)=(3,2),(4,2),(3,3)\). Explicit visits for these respective walks are \((C,G),(A,A),(T,T),(A,C)\); \((C,A),(G,G),(T,T),(A,C)\); and \((C,A),(A,C),(T,T),(A,C)\). Their differences generate both coordinate unit directions. Together with the primitive transition kernel, this ensures no nontrivial Fourier phase has spectral radius one, modulo integer periods; Fourier inversion around the unique saddle establishes the bivariate lattice local limit theorem. Conditioning on \(\sum_iG_i=m\), and imposing the nonzero terminal factor \(\mathbf1_{\{a_m\ne\bar b_m\}}\), changes only the analytic boundary prefactor and not the Gaussian covariance. Because the limiting cross covariance is zero, the conditional fluctuation of \(\sum_iH_i\) retains variance \(15m/64\). This proves the stated central limit law (with mean \(3m/4+O(1)\)).

**4. Exact-distance-zero asymptotics.** For even \(m\), a self-reverse-complement word is specified by a proper halfword of length \(m\) with exactly \(m/2\) GC symbols; for odd \(m\) none can be balanced. Under uniform proper words, the GC indicator is a stationary binary Markov chain with transition correlation \(-1/3\), and its length-\(k\) count has asymptotic variance \(k/8\). The one-dimensional lattice local limit theorem therefore gives \(\Pr(\operatorname{GC}(Y_k)=k/2)\sim2/\sqrt{\pi k}\) for even \(k\). Thus \(N_m(0)\sim (8/3)3^m/\sqrt{\pi m}\). Similarly \(|\mathcal H_m|\sim(4/3)3^{2m}\sqrt{2/(\pi m)}\). Their ratio is \(\sqrt2\,3^{-m}(1+o(1))\), as claimed.

## Verification
The standalone `verify.py` enumerates directly every homopolymer-free balanced DNA word for \(m=1,\ldots,5\), independently checks the transfer formula through \(m=6\), and cross-checks exact first and second moments with a separate recurrence. The first six spectra, indexed by \(r=0,\ldots,m\), are:

- \(m=1\): \((0,8)\).
- \(m=2\): \((8,8,40)\).
- \(m=3\): \((0,80,112,232)\).
- \(m=4\): \((56,112,776,1056,1352)\).
- \(m=5\): \((0,848,2016,7168,8976,8200)\).
- \(m=6\): \((424,1232,11360,26120,63248,71520,50856)\).

Run `python3 verify.py` from the extracted package directory. No external dependencies are needed. Finite enumeration is an independent check, not the proof of the all-length formula or limit law.

## Relationship to prior work
Benerjee, Deb and Gupta (2019) motivate simultaneously GC-content, reverse-complement and conflict-free/homopolymer constraints and construct codebooks, but do not state a full all-length single-word aligned self-distance distribution or its conditional Gaussian fluctuations. Rasool et al. (2023) also study combined coding constraints using heuristic optimization rather than an exact joint distance enumerator. The published study *Reverse-complement-fixed necklaces with constrained homopolymer runs and GC content* (2026) concerns the special fixed-point case \(r=0\) for necklaces and related self-complement halfword counts; those are prior special cases and are not claimed as new here. The new claim is the simultaneous, complete \(r\)-spectrum and its sharp support and fluctuation law over labeled linear balanced proper words.

## Limitations
The formula does not give optimal sizes of codes with pairwise Hamming or reverse-complement separation, and does not model imperfect complement chemistry, off-register hybridization or folding. Fixed-point enumeration by itself is known; novelty of the complete positive-distance spectrum remains subject to independent historical priority review. An indexed related fixed-necklace study was identified by summary, but its complete text was not accessible during the comparison; this is a residual literature risk. Normality and asymptotic probabilities are limits, not claims of finite-block equality. All assertions are mathematical and require independent validation before external certification.

## References
1. K. G. Benerjee, S. Deb and M. K. Gupta, *On Conflict Free DNA Codes*, arXiv:1902.04419, first made public 2019-02-12; https://arxiv.org/abs/1902.04419.
2. A. Rasool, Q. Jiang, Y. Wang, X. Huang, Q. Qu and J. Dai, *Evolutionary approach to construct robust codes for DNA-based data storage*, Frontiers in Genetics 14 (2023), first published 2023-03-20; https://doi.org/10.3389/fgene.2023.1158337.
3. *Reverse-complement-fixed necklaces with constrained homopolymer runs and GC content*, published research record (2026-11-02), fixed-point comparison only.
4. X. Li, M. Chen and H. Wu, *Multiple errors correction for position-limited DNA sequences with GC balance and no homopolymer for DNA-based data storage*, Briefings in Bioinformatics 24 (2023), first published 2022-11-21; https://doi.org/10.1093/bib/bbac484.
