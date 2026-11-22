# Scientific review: a bulk–edge Schatten transition for a disk-truncated Fock Hankel operator

## Correctness — PASS
The normalized Fock monomials diagonalize the Hankel Gram matrix because the disk-truncated anti-analytic multiplier changes angular degree by exactly one. Direct Gaussian radial integrals give the squared singular values \((n+1)q_{n+1}-nq_n^2\) including the exceptional index zero. The identity \(\lambda_n=q_n+nq_n(1-q_n)-(n+1)r_n\), Poisson local limits and two-sided exponential tail bounds yield the boundary singular profile, all fixed \(p\)-power limits, the operator norm and counting law. The trace exponent requires and receives a separate proof: a pointwise square-root comparison shows that bulk and boundary contributions add with an \(o(T)\) remainder. A fresh execution of `CHECK.py` produced `DISK_HANKEL_BULK_EDGE_DIAGNOSTIC_OK 108`; the 108 finite checks corroborate rather than replace the analytic argument.

## Originality — PASS with documented residual risks
The closest published disk semi-commutator result (`12a369cea2df`) shares the same normal-tail product in its boundary window but has no growing interior population; its diagonal singular values remain bounded and its Schatten sums grow as \(\sqrt T\). The present big Hankel operator has an exact different spectrum, boundary singular values of order \(\sqrt T\), and a mixed trace constant \(1+I_1\). The published interlevel disk-transfer result (`04a288b07a35`) has a Gaussian density, not a normal-tail product, and lacks bulk modes. Both complete published statements and proofs were inspected. Qin's 2026 work gives broad semiclassical Schatten limit criteria, not the requested exact fixed family in its accessible abstract, but its entire preprint was not retrieved; implicit coverage by general methods remains a bibliographic risk. Other Fock Hankel and Toeplitz literature may contain special-case formulas. Neither search absence nor mathematical partition establishes absolute priority.

## Mathematical value — PASS
Cutting off the simplest anti-analytic Fock multiplier at a growing disk is a canonical localization test for Hankel and Toeplitz semiclassical asymptotics. The result shows two genuinely different singular-value scales and determines which controls the Schatten mass. At \(p=1\) the two populations balance, so neither a pure bulk limit nor a pure edge limit gives the sharp constant. It yields exact approximation-number data and counting laws for a natural compact family, without artificial tuning or a prespecified finite slice.

## Closest literature and scope
- Jie Qin, *Schatten limits for semi-commutators in Toeplitz quantization on Fock space*, arXiv:2610.30787v1 (2026-10-22): motivating framework, abstract-level comparison; full preprint inaccessible in this search.
- *A Gaussian boundary-interaction law for nested Fock disk semi-commutators*, published-finding corpus `12a369cea2df` (2026-11-08): full result inspected; shared Gaussian-tail mechanism but distinct operator and Schatten scaling.
- *Boundary-Gaussian singular spectrum of disk transfer between the first two Landau levels*, published-finding corpus `04a288b07a35` (2026-11-01): full result inspected; distinct interlevel map and Gaussian-density edge.
- *Sharp weak-Schatten tails for exterior Laurent Hankel operators on Gaussian Fock space*, published-finding corpus `9b772b00d2fc` (2026-11-02): full result inspected; fixed exterior inverse powers and large-degree tail, not expanding disk cutoff.

The proof covers fixed Gaussian dimension one and all fixed positive Schatten exponents. Independent priority determination, other geometries and uniform moving-exponent limits are not included.

Self-review: passed. Independent audit: not yet performed.
