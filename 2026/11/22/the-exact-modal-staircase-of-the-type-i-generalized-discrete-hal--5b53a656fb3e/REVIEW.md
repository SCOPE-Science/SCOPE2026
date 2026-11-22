# Scientific review of the modal-staircase theorem

## Correctness (C): PASS

The statement fixes the complete parameter domain \(\theta>0\), \(\alpha>0\), the precise bin law, every integer mode, all equality boundaries, and the fixed-rate asymptotic quantifiers. The proof proceeds from the model's exact CDF differences to a monotone-likelihood-ratio argument in the shape coordinate and a direct double-integral strict log-concavity inequality for the binned density when \(\alpha\ge1\). These yield unique thresholds and prohibit any nonadjacent or triple ties. The threshold asymptotic follows from \(\log\tanh(j\theta/2)=-2e^{-j\theta}+O(e^{-3j\theta})\), a strictly convex scalar root equation and a simple-root perturbation bound. An independent arithmetic checker ran 484 finite diagnostics. Those diagnostics do not replace the proof.

## Originality (O): PASS, with residual historical-priority uncertainty

Barbiero and Hitaj, *Annals of Operations Research* (2024), §4.1, give the exact distribution and show a particular double mode at indices zero and one for a chosen rate; §3.2 establishes log-concavity only for their one-parameter specialization; §4.1 notes a log-concavity failure for another parameter pair. The published statement does not cover the full family of ordered modal transition thresholds or their explicit asymptotic constant. A second full-text Barbiero–Hitaj study in the *Journal of the Indian Society for Probability and Statistics* (2024), §5, uses normalized sampled density values, a different discretization, so it cannot imply the bin-integrated mass theorem. Earlier continuous type-I half-logistic literature does not resolve the integer-bin staircase. Related published modal-staircase work for other distributions has nonidentical probabilities and threshold equations. Exact use of classical log-concavity and likelihood-ratio tools is disclosed; no novelty is assigned to those tools. Broad historical priority has not been independently certified.

## Value (V): PASS

The shape parameter controls whether a count model's most likely observed value is zero, one or higher. The source paper describes isolated modes and reports real-data use but does not give a method to determine every modal transition. This theorem gives the complete no-skipped-bins classification, exact one-dimensional thresholds, unique double-tie description and sharp large-index scaling constant. In particular, the correction quantifies how increasing concentration moves the most probable count across a coarse observation grid. These are mathematically useful global model-shape boundaries, not merely a numerical restatement of the first example.

## Closest literature and limits

The closest source is Barbiero and Hitaj (2024), DOI `10.1007/s10479-023-05807-3`, sections 3, 4, and 9. Another close but nonidentical construction is DOI `10.1007/s41096-024-00185-w` (2024); continuous context is DOI `10.1080/00949655.2015.1031233`. The theorem is fixed-bin, fixed-rate, and concerns global modes only. The rate-uniform high-index expansion and statistical estimation consequences have not been proved, and full historical priority remains subject to independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
