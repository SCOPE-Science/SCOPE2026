# Independent mathematical audit

## correctness

PASS

For W=(0^a1^b)^t (a,b≥1,t≥2), the four-factor hit conditions 0^a,1^b,01,10 are necessary. Any long factor (length≥a+b) has overlapping period-shifted occurrences covering every internal 10 transition; any shorter unary factor embeds around a marked position of its maximal run; mixed shorter factors containing 10 embed at the selected internal 10 transition; the remaining short mixed 0^u1^v embed at a marked 01. Hence the certificate is sufficient for arbitrary position sets. Two symbol markers are necessary; distinct boundary configurations give the claimed 2t(t−1), (t−1)(bt+1), (t−1)(at+1) pair counts, including a=b=1. Direct fresh literal-factor enumeration verified the full four-factor equivalence for ALL 28,880 candidate subsets over 18 small parameter triples, and pair counts independently. This is finite corroboration, not the all-parameter proof.

## originality

FAIL

DECISIVE PRIOR IMPLICATION: November 2 published full proof for ALL minimum attractors of exactly W=(0^a1^b)^k gives the identical optimal pair sets, 2k(k−1) and (k−1)(k max(a,b)+1) counts and shortest-factor test for pairs. Another November 8 complete result independently repeats the same. Their long-factor period-interval lemma, unary-run embedding and two mixed-transition embeddings do NOT actually require that the marked set has cardinality two; substituting arbitrary Γ that meets the maximal unary factors and both transitions yields the submitted all-cardinality certificate without additional nontrivial lemma. Replacing the two single-symbol factor tests by maximal unary tests is immediate: a marked symbol anywhere within a maximal run covers every shorter unary factor. Thus the sole seemingly new all-set extension is a direct corollary of the earlier full proof, and the stated optimal enumerations are verbatim covered.

## value

FAIL

The optimal-pair classification and population formulas are already fully known for every parameter. The residual four-factor arbitrary-cardinality certificate is an immediate unbounded-cardinality restatement of the already-proved periodic occurrence and short-factor embedding lemmas, while the irredundance witnesses are small routine boundary checks. No independently valuable unknown exact result survives once those prior proofs are credited; correctness and larger test count do not create value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
