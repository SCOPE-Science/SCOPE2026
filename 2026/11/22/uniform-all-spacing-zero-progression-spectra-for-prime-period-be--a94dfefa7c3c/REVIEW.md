# Independent mathematical audit

## correctness

PASS

Under Touchard's recurrence the polynomial X^p−X−1 is irreducible: for a root ρ, iterated Frobenius gives ρ+i for i mod p, hence orbit size p. Nondegeneracy of the finite-field trace pairing gives a unique c with the first p Bell residues Tr(cρ^i); Touchard propagates the equality and c≠0 follows from B_0=1. A candidate period d imposes Tr(c(ρ^d−1)ρ^i)=0 on a basis, exactly equivalent to ρ^d=1. By the full-period hypothesis H=<ρ> has size N_p, coprime to p−1 since N_p≡1 mod (p−1). Thus cH contains exactly one nonzero vector on each base-field line. For any nonzero h modulo N_p, β=ρ^h is nonscalar; prime extension degree forces its degree to be p even if h is not a unit. The first ℓ powers are linearly independent, so their trace functionals have a common kernel of dimension p−ℓ. Counting its lines yields (p^(p−ℓ)−1)/(p−1), independently of h. At ℓ=p the kernel is zero; longer progressions imply an excluded p-term start. The proof is conditional at primes where the full period is not established. Independently generated exact Bell residues by Stirling rows S(n,k)=S(n−1,k−1)+kS(n−1,k) modulo p and summed over k, without using the frozen checker or its recurrence implementation. At p=2,3,5 the residues matched across period endpoints for the first p entries and not for any proper divisor shift; exhaustive cyclic counting gave respectively 4,36,3900 comparisons, with the p=5 spectrum [156,31,6,1,0] and unique consecutive quadruple start 587. The finite results corroborate rather than prove the general statement. Read checker.py and VERIFICATION.md without executing the frozen script.

## originality

PASS

The supported distinct claim is the uniform full progression spectrum at higher order for arbitrary nonzero spacings, with nonunit spacings included. Bell traces and classical projective one- and two-site counts are prior work, as is the maximal consecutive run. There is a short field-theoretic derivation from these ingredients plus a new-for-this-comparison rank argument; no inspected primary or indexed theorem already gives the full higher-order nonunit formulation or a general theorem that directly includes it. This is a bounded assessment, not a claim of priority for trace methods or power independence.

## value

PASS

This gives all exact progression counts on a classical cyclic Bell divisibility set; in particular every nonzero step has a unique longest run. The nonunit case is substantive because such a shift traverses only a subcycle, so invariance is not a reindexing of the known consecutive case. The rank observation explains why neither subcycles nor higher-order intersections break uniformity, a useful structure beyond recomputation of a single period or the two-site incidence parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
