# Self-review

## Correctness — PASS

The result has exact quantifiers: fixed \(0<\alpha<1\), \(\tau>0\), all \(0<t<1\), and the limit \(t\uparrow1\). The weight is submultiplicative, symmetric and GRS. The inverse coefficient formula is an absolutely convergent weighted geometric series, and its difference-coordinate mass is exactly the Green function of the symmetric random walk. The saddle point, curvature, Gaussian scale and sharp multiplicative prefactor follow from concavity and a uniform local Taylor expansion with negligible tails. The weak central limit for the weighted inverse coefficient distribution uses those same estimates. A standalone checker passed 82 direct and independent finite comparisons, which are corroboration and not a proof of infinite assertions.

## Originality — PASS relative to inspected sources

The closest literature is Spronk–Zhang, *Spectra of Beurling algebras of abelian groups* (2026, arXiv:2611.03437), which identifies the relevant GRS spectra; Chen–Wang, *Spectral Invariance and Gevrey Regularity* (2026, arXiv:2607.03074), which gives general inverse seminorm estimates; and Jaure, *Wiener's lemma for quasicrystals* (2026, arXiv:2610.12770), whose Theorem 5.13 provides norm-controlled inversion for stretched-exponential weights. All three 2026 primary texts were inspected, together with the 2018 quantitative weighted-inversion paper of Samei and Shepelska. Their statements do not give the sharp one-filter equivalent and Gaussian coefficient location. The two-dimensional filter projects to a one-dimensional random-walk Green function; that identity and Laplace asymptotics are explicitly acknowledged as classical ingredients rather than innovations. Actual search comparisons and priority risks appear in `AUDIT.json`.

## Mathematical value — PASS

The exact quantity measures stability of inverse filtering at a closing Fourier spectral gap. It exhibits a sharp, arbitrarily varying stretched-exponential blowup despite the torus Gelfand spectrum remaining identical for all weights. The Gaussian concentration law identifies the decisive lattice difference scale and width. This is a meaningful quantitative spectral-invariance boundary rather than just reparametrizing a known existence theorem.

## Limitations and remaining priority risks

The weight is nonproper, and the filter reduces to a one-dimensional random-walk resolvent. The statement is limited to this explicit filter, fixed weight parameters and weak Gaussian localization; it does not claim a global best inverse bound. The closest known arguments might yield an older equivalent result by combining classical random-walk Green formulas and saddle-point estimates. No claim of complete historical priority or independent validation is made.

Self-review: passed. Independent audit: not yet performed.
