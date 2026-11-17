# Scientific review: universal tangent-contact pair law

## Correctness — PASS

The exact area-normalized probability is a four-dimensional Lebesgue integral. In local tangent coordinates the graph expansions are \(g_\pm(y)=\kappa_\pm y^2/2+O(|y|^3)\), and the close-pair event forces \(y=O(\sqrt r)\), transverse difference \(O(r)\), and interior depths \(O(r)\). The exact coordinate Jacobian is \(r^{7/2}\). Pointwise convergence of event indicators and uniform compact localization give \(L^1\) convergence and therefore total-variation convergence for the conditional marks. The four-dimensional limiting volume evaluates to \(4B(5/4,3/2)/(3\sqrt{k})\); the gap-crossover formula follows from the same integral. Transforming \(q=kt^2\) produces an independent Dirichlet splitting of the positive horizontal mark, whose square has the stated beta law. The executable checker verifies the constant against a second, exact two-disk overlap calculation. The proof requires positive curvature and unique contact, and makes no finite-sample equalities.

## Originality — PASS, with residual historical uncertainty

Searched for the same parameterized pair-distance event, both equivalent point-pair/translation-overlap formulations and broader cross-region distance formulas. The primary closest literature:

- Ehlers–Enns (1981), DOI `10.2307/3213176`, identifies overlap-volume methods extending to disconnected regions. This covers a general *representation*, but the accessible abstract does not assert the sharp curved-contact exponent, coefficient, crossover or conditional marked law. Full text was inaccessible.
- Sheng (1985), DOI `10.2307/1427086`, gives general integral formulations for pairs of regions and shapes such as ellipses and circles. This may be a powerful precursor and is expressly credited; its abstract does not supply the marked tangent-contact limit. Full text unavailable; institutional full-text retrieval could not proceed.
- Tong–Ahmadi–Pan (2013), arXiv:`1312.2498`, derives cross-triangle distance distributions for adjacent shared-edge polygons. Shared edges, rather than isolated positive-curvature tangency, give a different local geometry. Abstract and limited accessible text were read.
- Lellouche–Souris (2019), DOI `10.3390/stats3010001`, full HTML text and relevant sections were inspected. The paper derives general same-body convolution and disc formulas, not a cross-body curvature-universal tangent asymptotic or beta–Dirichlet conditional marks.

Related indexed research on short distances within one body and small overlap under random translation has a different geometric observable or hypotheses. The genuinely compared claim is **the joint new curvature constant, crossover and conditional law**, not the already-known convolution identity. Absence from an index is not proof of priority, and inaccessible specialized literature remains a residual risk.

## Mathematical value — PASS

Two sets having zero-area intersection can nevertheless admit rare near neighbors in a meaningful spatial interaction model. The law identifies the sharp contact exponent \(7/2\), reveals that only the *sum* of the two curvatures enters, quantifies the transition upon an \(O(r)\) normal separation, and gives a complete probability law for the spatial arrangement of those rare pairs. The beta–Dirichlet factorization is an interpretable, geometry-driven structural statement, not a standalone arbitrary integral value. The result concerns smooth contact; other contact orders and arclength sampling are outside scope.

## Remaining limitations

No full-text inspection was possible for Ehlers–Enns (1981) or Sheng (1985), and the historical precedence of an equivalent specialized curved-contact asymptotic cannot be ruled out absolutely. External independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
