# Independent mathematical audit

## correctness

PASS

On zero-sum a∈C^{2k}, f_a(X)=sum_{i∈X}a_i, the full uniform k-subset covariance is k/[2(2k-1)] times ||a||². Conditional shell t, within-block independent zero-sum contrasts (multiplicity 2k-2) have variance t(k-t)/[k(k-1)] times ||a||², the remaining block-normal line has deterministic value 2t-k. Normalize by global covariance: eigenvalues 2(2k-1)t(k-t)/[k²(k-1)] and (2k-1)(2t-k)²/k². The exact ratio r=2(k-1)d²/(k²-d²) with parity d≡k mod2 gives full rank iff 0<t<k and d>0. Tightness requires (2k-1)d²=k², contradicts gcd(k,2k-1)=1. Integer d² cases r>=1 and r<1 prove universal floor, equality iff k=2u²-1, odd u>=3. Monotonicity in d² localizes optimum to parity-neighbors of alpha_k=k/√(2k-1). Expansion about alpha_k gives κ-1=(2√2/√k)ρ_k+O(1/k); equality sequence yields liminf 1/2, k=2s² odd s gives rho→1 for limsup. Independent exact brute-force shell averages for k=3,4,5 reproduce both covariance eigenvalues for every shell; independent Fraction scan k=3..2500 verifies bound and equality family, supplementing proof.

## originality

PASS

The component eigenvalues live in established Johnson graph harmonic/Terwilliger neighborhood spectral theory. New best-of-knowledge contribution is exact optimization across ALL one-shell choices and its arithmetically classified non-tightness and two subsequential rates. The related prior 2021 single-neighborhood entanglement formula has different objective and no arithmetic optimum in inspected §4.3.

## value

PASS

The natural sampling-design problem of how close a single Johnson distance shell can approach a tight frame has a nontrivial arithmetic obstruction, infinitely many exact extremizers and sharp competing fluctuation scales. Those facts are useful for deterministic first-harmonic sampling and are not just an isolated small-parameter recomputation. Existing scheme representation theory is properly treated as input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
