# Scientific review

## Correctness — PASS

At zero interaction-decay exponent, the energy at fixed number of plus spins is exactly \(2Jk(N-k)-2hk\) relative to all-minus; for \(0<h<J\), the unique highest layer is \(m=\lfloor N/2\rfloor\), with a finite uniform energy gap to all other layers. The two basin graphs remain connected for all sufficiently small nonnegative exponents, and all central-layer neighbors are downhill. A one-dimensional within-group compression argument proves the two end blocks uniquely minimize any strictly decreasing positive distance cut, giving the strict logarithmic gap. The reversible Dirichlet principle then reduces the network to disjoint parallel stars of degree \(m\) and \(N-m\), with exact effective conductance \(m(N-m)/N^2\) times the Gibbs weight of each star. The exact mean/capacity identity supplies the prefactor, uniformly through the coalescing gate energies. A direct finite-state checker passed 2,049 consistency checks. The proof, not the finite examples, establishes the infinite-inverse-temperature limit.

## Originality — PASS, with stated priority risk

The precise object is a finite open one-dimensional ferromagnet with couplings \(Jr^{-q}\), its one-attempt-per-step Metropolis mean transition time, and the simultaneous \(\beta\to\infty\), \(q\to0\), \(\beta q\to\lambda\) limit. Van Enter et al. (2019), Theorem 3.2, gives the logarithmic Arrhenius exponent and boundary droplet geometry but no explicit finite-temperature, weak-exponent gate multiplicity function. Jacquier's 2025 metastability review discusses sharp prefactors generally without deriving this function. The general graph prefactor work by Dommers et al. (2016) and random-graph long-range study by Jacquier (2025) concern either general methods or other graph structures, not the stated explicit weak-exponent crossover. Targeted literature comparisons did not identify an identical statement or a stronger covering implication. These comparisons are limited to the stated inspected material; an implicit reduction within broader potential-theoretic literature remains a residual publication-priority risk.

## Value — PASS

This is a natural sharp symmetry-breaking question rather than an arbitrary parameter slice: homogeneous all-to-all couplings give exponentially many equal-energy saddle configurations, whereas any fixed small positive decay exponent selects only the two boundary gates. The theorem identifies the unique temperature-dependent crossover scale and all its intermediate coefficients, with an explicit four-spin example and a normalized exact rate prefactor. It supplies a benchmark for interpreting finite-temperature nucleation data near the mean-field boundary. It makes no thermodynamic-limit or noise-robustness claim.

## Closest literature and scientific limits

The primary comparison is van Enter et al., *Nucleation for One-Dimensional Long-Range Ising Models* (2019), https://doi.org/10.1007/s10955-019-02238-y. The initiating literature is Jacquier, *Exploring Metastability in Ising Models* (first public version 10 January 2025), https://arxiv.org/abs/2501.06163. The independent broader graph-side comparison is Dommers et al., *Metastability for Glauber Dynamics on Random Graphs* (2016), https://arxiv.org/abs/1602.08900. The result fixes \(N\), requires \(0<h<J\), and uses a sufficiently small decay exponent. Potential undiscovered equivalent general-capacity specializations are the main originality risk.

Self-review: passed. Independent audit: not yet performed.
