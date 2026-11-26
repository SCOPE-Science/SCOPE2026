# Independent mathematical audit

## correctness

PASS

Writing n=aU+dt, all solutions give T=t+ja and L=U−jd, j≥0, where T is the weight of a partition into 1,2,3 and L its available length. At minimum length ceil(T/3), the deficit from all 3's is 0,1, or 2, giving at most two partitions. The listed witnesses show that one extra part gives three for T≥4, with second thresholds b(T). For t≥4 and for t=3 no higher j contributes early. At t=2 exactly two j=0 partitions are already present when the first j=1 partition arrives. At t=0,1 the second j=1 partition arrives no later than the first j=2 partition, so the displayed N_t are exact even for a=4 or d=1. On each residue monotonicity gives M_t as the cutoff; taking max(M_t)−a gives the stated branches, including competition between t=1 and t=2 for a≡1. Summing the residue lengths gives ΣN_t plus the coprime floor sum (a−1)(d−1)/2, and yields H_3 including n=0. Independently ran `python3 /workspace/reviews/evidence/reproduce.py 3`: direct enumeration of quadruples on 198 coprime parameter pairs, testing 44,287 integer positions. This corroborates rather than proves the infinite law. The frozen verifier was inspected, not executed.

## originality

PASS

Supported for the full four-term, variable-step residue law and its uniform threshold and genus consequences, not for the Apéry definitions or the previously settled odd a≥9, d=2 subfamily. Neither the earlier fixed-step theorem nor the three-generator and lower-multiplicity theorems cover the varying progression step and competing maxima.

## value

PASS

For a standard family of denumerants, the uniform result gives all low-representation exceptional integers, not just an extremal number, and explains the change of maximizing residue as the progression step increases. The variable-step extension is more than substituting a parameter in the known odd-denomination theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
