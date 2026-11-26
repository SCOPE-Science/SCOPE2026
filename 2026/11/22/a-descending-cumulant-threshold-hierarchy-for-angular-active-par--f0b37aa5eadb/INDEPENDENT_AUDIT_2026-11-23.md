# Independent mathematical audit

## correctness

PASS

The even solution of Df''=sf with endpoint value 1 is the cosh quotient; multiplying Euler factors gives v+(1-v)λ_j/(λ_j+s), v=u². The sum of independent Bernoulli-thinned exponentials is integrable and has a finite mgf for z<λ_0 near zero: the logarithms converge locally normally by ∑1/λ_j<∞. Expanding log(1-vz/λ_j)-log(1-z/λ_j) gives (m-1)!(1-v^m)∑λ_j^{-m}. Uniform Poisson redirection has exit probability 1-a/π per tumble, so its matched rate is 1/μ, verifying all scale factors. The log derivative of (1-v^m)/(1-v)^m is positive and C_m<1 by ∑q_j=1. Confirmed C_2=2/3 and C_3=8/15 from the odd zeta sums. Independently checked rational bounds using 157/50<π<22/7: v_0>0.1886, v_0<0.1901, H_2<0.01632<0.02845<(4/5)v_0². Hence H_m<(4/5)v_0^m for all m≥2. On [v_0,1/5], P_m=(1+H_m)(1-v^m) lies strictly below 1 and its increment is >v^m(1-v)-H_m>0, so P_m^(1/m) strictly increases. This places and orders all unique crossings. From the root equation v_m-v_0=O(5^{-m}/m); therefore v_m^m/v_0^m→1 and H_m=o(v_0^m), giving the sharp coefficient q_0/m. The principal heat-survival coefficient is (4/π)cos(πu/2)>0. At equality u²=1-8/π² put x²=π²/4-2; the Taylor upper bound cos x≤1-x²/2+x⁴/24 and the rational π bounds give a prefactor <0.990. Thus rate and equality comparisons, and the strict variance-versus-tail window, follow. Inspected checker.py only; its finite root and product diagnostics are not proof of the infinite hierarchy.

## originality

PASS

Best-of-knowledge PASS for strict ordering across every integer cumulant order and the sharp approach rate of the crossings. The individual transforms, Brownian principal decay, fair comparison by equating means, low-order variance crossing, and the derivable variance-versus-tail comparison are not independently strong priority claims. The all-order spectral dominance inequality and quantified asymptotic are the surviving structural contribution.

## value

PASS

Equal means remove the trivial scale difference in trapping duration. The strict infinite hierarchy determines which fluctuation orders exceed the clock at each offset and how the transition approaches a spectral threshold. This gives more than a single low-order sign or a few sampled angles and clarifies why larger rare-event survival need not mean larger variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
