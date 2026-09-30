# Independent Audit — 2026/09/14/022

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `0dd019ddb58737501e9d5d1d40278644033c2532`
- Disposition: **FAILED**

## Correctness

**PASS** — The stated trapping block is correct. The three base points and contracted curves of sigma_0 follow by direct factorization. Their forward images avoid the indeterminacy set, which gives algebraic stability and degree 2^n. In affine coordinates the Jacobian is exactly the displayed rational matrix; on y>=2.9, |z|<=0.2 its Frobenius norm is in fact below about 0.266 at the worst boundary point, so the submitted coarser <0.43 bound is safe. The strip is forward invariant, complete as a closed subset of R^2, and the contraction theorem gives a unique attracting fixed point.

## Originality

**PASS** — Bedford-Diller and related work already develop trapping-region/entropy-zero phenomena for plane birational maps, but the exact involution sigma_0=[Y^2+Z^2:XY:XZ], affine family L_a, and the uniform numerical strip certificate do not appear as a direct quoted specialization of the located sources. The narrow explicit block is therefore plausibly original as a worked family-level construction.

## Scientific value

**FAIL** — The record explicitly does not determine the global real entropy, prove a uniform entropy gap, establish maximality, or settle the target dichotomy. It certifies only that one forward-invariant region is contracting while another real saddle and possible dynamics outside the strip remain uncontrolled. That is useful exploratory evidence but not a scientifically decisive resolution or a general theorem strong enough to justify a validated finding.

## Sources

- Real dynamics of a family of plane birational maps: trapping regions and entropy zero (Eric Bedford; Jeffrey Diller): https://arxiv.org/abs/math/0609113 — Established prior framework for trapping regions and entropy-zero behavior in real plane birational dynamics.

## Limitations

- The audit accepts the local contraction and algebraic-stability calculations, but no global entropy conclusion follows from them alone.
- Topological entropy on the full real surface, and any uniform gap from log 2, remain open in the submitted record.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
