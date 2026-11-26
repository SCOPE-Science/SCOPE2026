# Independent mathematical audit

## correctness

PASS

Integration against the independent exponential clock gives discounted success u_i(r+s) and discounted reset c(1−u_i(r+s)), where c=r/(r+s). Averaging products over the uniform initial cyclic phase gives the block sum 1−(1−c)Σ_{k≥1}c^{k−1}B_k; iid replaces B_k by the mean failure probability to power k. A full block factors into the product P times shorter blocks. AM–GM bounds P, the symmetric-mean inequality bounds the shorter blocks that are full averages over pairs or triples, and for four modes the adjacent-pair sum factors as (q_1+q_3)(q_2+q_4). Thus B_k ≤ (mean q)^k for every k when m≤4, including q_i=0 or 1, and the full-block comparison is strict for nonconstant q. At s↓0, P(r)<1 by the capture assumption, so blockwise geometric domination in a neighborhood of zero justifies passage to the means after division by s. Independently solved the mode-specific renewal equations F_i=u_i+cq_i F_{i+1} with fractions at the Brownian witness. The cyclic and iid transforms are 2729396/5242745 and 12/23 respectively, with difference −136832/120583135. The distances yield u_i(4)=1/4,1/4,1/4,3/4,3/4 in the stated cyclic order. Strictness gives distinct perturbed sites by continuity. More generally, three consecutive ones and zeros elsewhere give B_2=2/m>9/m² for m≥5; interior perturbation and the uniform O(c²) tail give the claimed small-c reversal and Brownian realizability.

## originality

PASS

The supported distinct claim is the sharp four/five boundary for Laplace dominance over iid uniform destinations, including the Brownian obstruction, and the extensions beyond the known two-site mean comparison. The m=2 mean subclaim directly overlaps the inspected same-day Markov reset-site record and is not counted as a distinct contribution; relative priority is not established. Renewal identities and the Brownian free transform are antecedents, not novelty claims.

## value

PASS

Matching single-attempt marginals do not determine the ordering of the total search time. The sharp cutoff in the number of modes, uniform over free hitting-time laws, gives a reusable policy comparison for regenerative searches; the Brownian counterexample rules out extrapolating it even for standard first-passage laws at finite positive locations. A positive-discount obstruction is informative without claiming a mean or survival reversal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
