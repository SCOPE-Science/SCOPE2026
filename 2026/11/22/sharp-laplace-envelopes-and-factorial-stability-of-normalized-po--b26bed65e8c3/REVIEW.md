# Mathematical review: sharp normalized-chain Laplace envelopes

## Correctness — PASS

The claim is for arbitrary integer depth and probability-valued positive chains. The definition of \(G\) is legitimate because the Lévy measure \(\nu(dx)/x\) satisfies the standard integrability requirement. The Laplace transform identity \(q_{G\nu}=\mathcal Tq_\nu\) and injectivity of the transform show \(F(G\nu)=\nu\). At every depth, the initial transform is \(\mathcal T^Nq_N\), with \(0\le q_N\le1\). Since \(\mathcal T\) reverses order, this proves the envelope. The \(h_{N+1}\) endpoint is realized using \(\delta_0\); the limiting terminal transform \(e^{-Ms}\to0\) approaches the \(h_N\) endpoint through dominated convergence. The exponential fixed point lies in the envelope. The iterated Volterra-Lipschitz inequality proves a global \(s^N/N!\) deviation, and a Taylor induction for the approaching endpoint proves coefficient-one local sharpness. Checks were run on the provided `check.py` and gave 5539 passed finite diagnostics; finite tests are corroborative only. The conclusion is exact in all stated quantifiers.

## Originality — PASS against accessible evidence

Grabchak's November 2026 full text, especially Proposition 3, Theorem 1 and Corollary 2, supplies the construction and fixed/periodic-point classification but not the pointwise sharp transform envelope or factorial uniform compact approximation. An earlier normalized finite-chain theorem already has moment matching, weak/Wasserstein convergence, and a weaker short-argument transform inequality; those statements are **not** claimed as new and do not imply the exact worst-case pointwise transform capacity or the global factorial estimate with optimal local constant. Bar-Lev and Letac's related second-derivative transform is structurally different; its full article was not accessible. Targeted semantic-record and primary-literature searches found no stronger covering result, but absence of search hits is not a uniqueness proof.

## Mathematical value — PASS

Finite-depth approximate exponential behavior is natural when only a finite number of normalized size-bias/Lévy derivatives are observed. The theorem provides the complete sharp feasible transform interval for every depth and Laplace argument, not merely a finite-moment condition or an asymptotic assertion; it exhibits the extremizing probability-law constructions and gives an explicit factorial error for each compact frequency range with best possible local constant. This quantitative, extremal characterization is a useful stability boundary for the positive-chain transform, and not a numerical example or a restatement of the motivating construction.

## Closest literature and limitations

- M. Grabchak, arXiv:2611.11109v1, full text, Section 3: normalized positive-chain construction and scaled periodic points.
- Bar-Lev and Letac (2025), DOI 10.1016/j.spl.2024.110256: related but distinct second-derivative chain; full text inaccessible in this review.
- An earlier finite-depth moment result provides a weaker comparison rate, and does not provide the exact transform envelopes.

No independently verified precedence claim or independent correctness judgment is asserted. The sharpness concerns Laplace transforms, not total variation. A boundary is approached by terminal laws escaping to infinity.

Self-review: passed. Independent audit: not yet performed.
