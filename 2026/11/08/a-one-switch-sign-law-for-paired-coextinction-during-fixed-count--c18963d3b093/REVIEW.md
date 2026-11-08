# Scientific review

## Correctness (C): PASS

The fixed-count removal law and \(q_s(r)\) are explicitly defined. Conditioning on set inclusion gives the covariance formula; nested-set covariance factors, while incomparable-set signs reduce to the unimodal ratio \(H_r\). The ratio of consecutive \(H_r\)'s has numerator deviation \(ab-c(r+1)\), which changes sign at most once. The endpoint identity \((nc-ab)/n^2\) fixes whether the unimodal path ever exceeds one. Boundary cases \(c=0\), \(c=\min(a,b)\), \(n=u\), and \(r\in\{0,n\}\) are treated explicitly. The standard-library checker passes 17,743 exact stage calculations and 1,737 independent subset-enumeration comparisons; finite tests support but do not replace the proof.

## Originality (O): PASS, with priority risk

The inspected primary full texts of Memmott–Waser–Price (2004), Kaiser-Bunbury et al. (2010), and Bane–Pocock–James (2018) analyze extinction curves, interaction rewiring and robustness distributions, not the full pairwise fixed-stage covariance sign law. The 1983 negative-association theorem covers disjoint coordinate families, not positive covariance from overlapping partner sets. A previous extinction-*rank* covariance result is not a stronger equivalent: the \(n=26\) example yields positive penultimate survival covariance but negative rank covariance. Actual scientific-record searches for coextinction covariance, overlapping subset inclusion, and hypergeometric phase changes returned no directly covering result. The remaining risk is a mathematically equivalent theorem in broader sampling-without-replacement or reliability literature; search failure alone does not prove novelty.

## Value (V): PASS

Network robustness curves give mean survival counts but hide pairwise uncertainty. The exact threshold \(nc>ab\), the one-switch restriction, and the contribution \(\sum_{i\ne j}\operatorname{Cov}(S_i,S_j)\) to the variance of the surviving-species count give a natural, complete, finite-network classification. The sharp sign reversal after a fixed number of pollinator losses is motivated by correlated coextinction risk, not a freely chosen coefficient or unmotivated special case. Scope is intentionally restricted to the static binary uniform-removal null model and does not imply realism under interaction rewiring.

## Closest literature and limitations

Direct comparisons: Memmott et al. (2004), DOI 10.1098/rspb.2004.2909; Kaiser-Bunbury et al. (2010), DOI 10.1111/j.1461-0248.2009.01437.x; Bane et al. (2018), DOI 10.1002/ece3.4529; Joag-Dev and Proschan (1983), DOI 10.1214/aos/1176346079. Full original PDF text and methods/results were inspected for the first three; the last was compared using its published abstract. The result proves no empirical causation, statistical significance, stochastic feedback claim, or historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
