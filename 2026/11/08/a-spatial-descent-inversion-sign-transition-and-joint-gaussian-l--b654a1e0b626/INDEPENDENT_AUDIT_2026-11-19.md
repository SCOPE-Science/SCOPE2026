# Independent mathematical audit

## correctness

PASS

For iid digits Z_i with Pr(Z_i=1)=r=1-p, the simultaneous inversion indicator is Z_j(1-Z_k) for j<k by the established inverse-shuffle bijection. The five shared-index overlap classes yield q(1-q)+(i-1)q(r^2-q)+(n-i-1)q(p^2-q)=q[1-q+(r-p)(i-1-p(n-2))]. The profile slope is q(r-p), and its worst boundary is negative iff n>2+(1-q)/(min(p,r)|r-p|), with the other endpoint always positive. Exact first/second moments are E D=(n-1)q, E I=binom(n,2)q, Var D=(n-1)q(1-q)-2(n-2)q^2, Var I=binom(n,2)q(1-q)+2binom(n,3)q(1-3q), Cov(D,I)=(n-1)q(1-q)+binom(n-1,2)q(r-p)^2. The exact centered-Bernoulli decomposition gives I-EI=sum_k(np-k+r)U_k -sum_{j<k}U_jU_k. The second term has L2 size O(n), negligible on n^(3/2). Combining the weighted U term with bounded one-dependent descent summands, remove separated blocks of length n^(1/3), apply Lindeberg--Feller and Cramer--Wold; exact moments identify Sigma=q[[1-3q,(r-p)^2/2],[(r-p)^2/2,(1-3q)/3]]. Its determinant q^2(1-12q^2)/12>0 for 0<q<=1/4, with covariance zero iff p=1/2, and limiting correlation increasing to sqrt(3)/2 only at excluded endpoints. All hypotheses require one forward shuffle, 0<p<1, fixed p for n->infinity; equality at threshold produces no strict both-sign outcome. Independent exact word enumeration and direct forward-cut distribution checks corroborate algebra, not the all-n proof.

## originality

PASS

The iid binary-word representation and separate marginal normality are prior Işlak results, not credited as new. A published fixed-composition Resultary finding on the same research date already gives an affine local descent--inversion covariance for uniformly rearranged multisets; conditioning and mixing may reproduce the finite-site identity, so its individual algebraic slope is not claimed as an isolated foundational novelty. The surviving final result combines a sharp binomial-bias finite-position sign criterion with a full fixed-p biased two-packet joint Gaussian limit and its explicitly positive limiting correlation away from balance. The inspected Işlak, Conger--Viswanath, Fulman, Féray and Dörr--Heiny statements do not establish this full combined theorem, and Thiel treats the major index rather than the unweighted descent count. This is a qualified best-of-knowledge judgment, not a historical priority or independence certificate.

## value

PASS

For a canonical Gilbert--Shannon--Reeds two-packet shuffle, dependence between local disorder (a particular descent), total disorder (inversions), and macroscopic fluctuations is a natural structural probabilistic question. The sharp site-dependent sign reversal across the deck at a computable finite threshold, and the nonzero bias-dependent limiting bivariate Gaussian correlation, reveal behavior absent from separate marginal CLTs; balanced cuts are exactly the asymptotically independent case. This is a motivated full-parameter classification for a natural model, not an arbitrary slice or an unverifiable numerical improvement. The site formula itself is elementary once the coupling is given and closely related to the same-day fixed-composition affine formula, which limits the scale of novelty but does not eliminate the independent utility of the combined joint law and sharp classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
