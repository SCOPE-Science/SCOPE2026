# Independent audit — 2026/09/09/039

Date: 2026-09-26. Disposition: failed; complete original package archived.

## Correctness — PASS for the actual finite claims

I independently formed each companion matrix at (q=0,1/8,ldots,3/4), iterated its powers through (k=200), and computed the largest singular value numerically. The first maximizing indices are (0,2,3,4,5,7,11), and values (1,1.133429075818,1.630232909448,2.999943894976,7.098087443811,20.739226120324,86.375712713561), all within the advertised two-sided intervals. At the selected rational resolvent radii, independent inverse/SVD calculations yield point values (0.998083543711,0.999062442050,1.032617186454,1.485012172459,3.191900464098,9.281926370283,39.179047169375), consistent with the stored point certificates. The mathematical infinite-tail argument is sound: (C_q=qI+N), (N^4=0), and after (k=121) each nonnegative coefficient (inom{k}{j}q^{k-j}) decreases for (jle3) and (qle3/4). The stored exact rational lower/LDL/Frobenius certificates support the finite exclusions; my numerical reproduction is corroboration rather than a second exact rational proof. The result appropriately does **not** assert a global Kreiss upper bound or the proposed (M/K) gap.

## Originality — PASS, narrowly

The Kreiss theorem, companion-matrix Jordan expansion, pseudospectral methods and transient examples are prior. I found no identical seven-parameter peak-index table in the checked Mitchell, Apkarian–Noll or Reuter papers. The novelty is the sampled rational certificate table, not a theorem about the companion family for general (q) or Kreiss sharpness.

## Scientific value — FAIL

Seven hand-picked values of (q) yield a coarse (0.02)-wide table of peak powers, while the central Kreiss question remains unanswered: the resolvent calculations are lower bounds at one selected point, with no global (K(q)) enclosure or certified (M/K) separation. The record establishes no law for peak indices, transition thresholds, optimization principle, or structural conclusion beyond straightforward instances of the Jordan expansion. The arbitrary parameter sample and numerical bounds do not constitute a sufficiently reusable scientific result in the proposed Kreiss-sharpness program. This verdict leaves the finite computations intact.

## Sources

- Mitchell, *Computing the Kreiss Constant of a Matrix*, arXiv:1907.06537: https://arxiv.org/abs/1907.06537
- Apkarian and Noll, *Optimizing the Kreiss constant*, arXiv:1910.12572: https://arxiv.org/abs/1910.12572
- Reuter, *Associating the Invariant Subspaces of a Non-Normal Matrix with Transient Effects*, arXiv:1909.05931: https://arxiv.org/abs/1909.05931
- Candidate `artifacts/certificates.json` and `artifacts/verify.py`; independent power and resolvent reproduction above.
