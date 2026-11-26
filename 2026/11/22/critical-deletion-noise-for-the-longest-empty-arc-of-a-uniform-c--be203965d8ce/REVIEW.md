# Independent mathematical audit

## correctness

PASS

Root the cyclic order at a labeled point so its gaps have the Dirichlet(1,…,1) law without size-bias from an external cut. The sum of k<n adjacent gaps is Beta(k,n−k); both distinct endpoints must survive and the k−1 intervening points be deleted, giving the asserted exact expectation. Before normalization, the corresponding Erlang exceedance at log n+x has expected count tending to e^(−x) τ^(k−1)/(k−1)!. In each mixed factorial moment for finitely many lengths and disjoint height bins, overlapping prescribed retained gaps are incompatible. Disjoint blocks with a shared endpoint contribute O(n^(r−1)) choices times O(n^(−r)) probabilities; all other choices factor. The infinite geometric–Erlang sum is q_n exp(−q_n u), by summing the Erlang polynomial term by term. Subtracting the first K limiting terms supplies the vanishing upper-tail error for lengths above K; one/no survivor events are negligible. The expected number of lost original exceedances is (1−q_n²)e^(−x), so the original and retained length-one limits coincide. Normalizing by S_n changes either centered maximum by o_P(1) since (n/S_n−1) log n→0. This yields the joint CDF as the product of two no-point probabilities. Exact persistence requires a separate argument, not weak convergence on the diagonal: the two endpoints of the original maximizer survive with probability q_n², and then persistence is the event that the original maximum beats the largest genuinely new block. New and original block sums have no ties; comparing their independent limiting extremes gives ∫e^(−x)exp(−e^τ e^(−x))dx=e^(−τ). At τ=0, new exceedances vanish above each fixed cutoff; the original maximum is above a sufficiently low cutoff with arbitrarily high probability. Finally, in the stated high-noise regime the binomial survivor count is asymptotic to n and the marginal Gumbel tightness conditional on that count gives a centered shift (ε_n/q_n) log n+O_P(1), which diverges while the original maximum stays tight.

## originality

PASS

The Bernoulli critical-window joint limit and persistence probability are distinct from the inspected marginal Gumbel laws, generic Poisson splitting, and one-deletion statements. Neither the single-sample marginal nor the Dirichlet/Beta representation should be credited as new. The finding is assessed on the marked joint law and exact persistence across the critical scale, not on historical priority over all possible coupling theorems.

## value

PASS

The longest empty arc quantifies the worst uncovered part of a random circular sample. A deletion fraction tending to zero can change that extreme with order-one probability; the result identifies exactly when and separates unchanged extreme gaps from newly merged competitors, giving a joint calibration not obtainable from two marginal Gumbel fits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
