# Review of a finite-mode Fourier sign-set theorem

## Correctness — PASS

The function class is specified using the unitary \(2\pi\)-Fourier transform, the real span of odd-index Laguerre modes \(j=1,3,5\), and the pointwise condition \(f(0)=0\). The Laguerre generating function supplies the Fourier eigenvalue \(-1\). Exact rational polynomial identities reduce the constrained space to two dimensions; leading-coefficient analysis eliminates all negative-tail competitors. The remaining one-parameter quartic is covered by six parameter strips and two unbounded tails. Exact rational Bernstein certificates bound all strips, and a direct algebraic Bernstein certificate covers the negative tail. Every alternative is strictly worse; uniqueness of the positive ray follows. The standalone standard-library checker validates all critical finite polynomial identities and interval certificates. Risk: no independent proof replication has been conducted.

## Originality — PASS relative to checked evidence

Edwin's 2026 paper poses the broader sign-uncertainty context but the reviewed relevant material does not present the exact three-mode negative-eigenvalue optimizer. The nearest published exact sign-length result concerns eigenvalue \(+1\) and Hermite orders \(0,4,8\), and therefore does not imply the negative-eigenvalue result for orders \(2,6,10\). A classical Beurling/Hermite uncertainty treatment and a Wigner-nodal-set paper concern different quantities. Database comparisons included aliases, sign-radius problems, polynomial/annulus formulations, and higher-mode coverage. The full scientific statement and proof of the published nearest record were inspected; its eigenvalue and polynomial family are distinct. Absence of an indexed match is not proof of novelty.

## Mathematical value — PASS

A recently posed definite-set sign question motivates exact finite-mode benchmarks. The theorem gives a natural first negative-Fourier three-mode classification with a sharp algebraic negative-set length, a unique extremizer, and the substantive rigidity that an extra Hermite order cannot reduce the optimum. It treats an infinite continuous sign set, not a finite sampling experiment. It does not address the unrestricted problem.

## Closest literature and limitations

R. Edwin, arXiv:2611.08224v1, provides the motivating generalized sign-uncertainty question. The positive-Fourier three-mode benchmark has a different eigenvalue and different Hermite orders, with no statement that transfers to this case. Classical Gaussian-Hermite and Wigner studies do not establish this precise minimum. An older unindexed exact weighted-polynomial calculation remains a bibliographic risk.

Self-review: passed. Independent audit: not yet performed.
